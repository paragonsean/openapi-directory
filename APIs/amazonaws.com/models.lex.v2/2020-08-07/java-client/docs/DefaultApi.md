# DefaultApi

All URIs are relative to *http://models-v2-lex.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**batchCreateCustomVocabularyItem**](DefaultApi.md#batchCreateCustomVocabularyItem) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/customvocabulary/DEFAULT/batchcreate |  |
| [**batchDeleteCustomVocabularyItem**](DefaultApi.md#batchDeleteCustomVocabularyItem) | **POST** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/customvocabulary/DEFAULT/batchdelete |  |
| [**batchUpdateCustomVocabularyItem**](DefaultApi.md#batchUpdateCustomVocabularyItem) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/customvocabulary/DEFAULT/batchupdate |  |
| [**buildBotLocale**](DefaultApi.md#buildBotLocale) | **POST** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/ |  |
| [**createBot**](DefaultApi.md#createBot) | **PUT** /bots/ |  |
| [**createBotAlias**](DefaultApi.md#createBotAlias) | **PUT** /bots/{botId}/botaliases/ |  |
| [**createBotLocale**](DefaultApi.md#createBotLocale) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/ |  |
| [**createBotVersion**](DefaultApi.md#createBotVersion) | **PUT** /bots/{botId}/botversions/ |  |
| [**createExport**](DefaultApi.md#createExport) | **PUT** /exports/ |  |
| [**createIntent**](DefaultApi.md#createIntent) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/intents/ |  |
| [**createResourcePolicy**](DefaultApi.md#createResourcePolicy) | **POST** /policy/{resourceArn}/ |  |
| [**createResourcePolicyStatement**](DefaultApi.md#createResourcePolicyStatement) | **POST** /policy/{resourceArn}/statements/ |  |
| [**createSlot**](DefaultApi.md#createSlot) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/intents/{intentId}/slots/ |  |
| [**createSlotType**](DefaultApi.md#createSlotType) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/slottypes/ |  |
| [**createTestSetDiscrepancyReport**](DefaultApi.md#createTestSetDiscrepancyReport) | **POST** /testsets/{testSetId}/testsetdiscrepancy |  |
| [**createUploadUrl**](DefaultApi.md#createUploadUrl) | **POST** /createuploadurl/ |  |
| [**deleteBot**](DefaultApi.md#deleteBot) | **DELETE** /bots/{botId}/ |  |
| [**deleteBotAlias**](DefaultApi.md#deleteBotAlias) | **DELETE** /bots/{botId}/botaliases/{botAliasId}/ |  |
| [**deleteBotLocale**](DefaultApi.md#deleteBotLocale) | **DELETE** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/ |  |
| [**deleteBotVersion**](DefaultApi.md#deleteBotVersion) | **DELETE** /bots/{botId}/botversions/{botVersion}/ |  |
| [**deleteCustomVocabulary**](DefaultApi.md#deleteCustomVocabulary) | **DELETE** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/customvocabulary |  |
| [**deleteExport**](DefaultApi.md#deleteExport) | **DELETE** /exports/{exportId}/ |  |
| [**deleteImport**](DefaultApi.md#deleteImport) | **DELETE** /imports/{importId}/ |  |
| [**deleteIntent**](DefaultApi.md#deleteIntent) | **DELETE** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/intents/{intentId}/ |  |
| [**deleteResourcePolicy**](DefaultApi.md#deleteResourcePolicy) | **DELETE** /policy/{resourceArn}/ |  |
| [**deleteResourcePolicyStatement**](DefaultApi.md#deleteResourcePolicyStatement) | **DELETE** /policy/{resourceArn}/statements/{statementId}/ |  |
| [**deleteSlot**](DefaultApi.md#deleteSlot) | **DELETE** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/intents/{intentId}/slots/{slotId}/ |  |
| [**deleteSlotType**](DefaultApi.md#deleteSlotType) | **DELETE** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/slottypes/{slotTypeId}/ |  |
| [**deleteTestSet**](DefaultApi.md#deleteTestSet) | **DELETE** /testsets/{testSetId} |  |
| [**deleteUtterances**](DefaultApi.md#deleteUtterances) | **DELETE** /bots/{botId}/utterances/ |  |
| [**describeBot**](DefaultApi.md#describeBot) | **GET** /bots/{botId}/ |  |
| [**describeBotAlias**](DefaultApi.md#describeBotAlias) | **GET** /bots/{botId}/botaliases/{botAliasId}/ |  |
| [**describeBotLocale**](DefaultApi.md#describeBotLocale) | **GET** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/ |  |
| [**describeBotRecommendation**](DefaultApi.md#describeBotRecommendation) | **GET** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/botrecommendations/{botRecommendationId}/ |  |
| [**describeBotVersion**](DefaultApi.md#describeBotVersion) | **GET** /bots/{botId}/botversions/{botVersion}/ |  |
| [**describeCustomVocabularyMetadata**](DefaultApi.md#describeCustomVocabularyMetadata) | **GET** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/customvocabulary/DEFAULT/metadata |  |
| [**describeExport**](DefaultApi.md#describeExport) | **GET** /exports/{exportId}/ |  |
| [**describeImport**](DefaultApi.md#describeImport) | **GET** /imports/{importId}/ |  |
| [**describeIntent**](DefaultApi.md#describeIntent) | **GET** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/intents/{intentId}/ |  |
| [**describeResourcePolicy**](DefaultApi.md#describeResourcePolicy) | **GET** /policy/{resourceArn}/ |  |
| [**describeSlot**](DefaultApi.md#describeSlot) | **GET** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/intents/{intentId}/slots/{slotId}/ |  |
| [**describeSlotType**](DefaultApi.md#describeSlotType) | **GET** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/slottypes/{slotTypeId}/ |  |
| [**describeTestExecution**](DefaultApi.md#describeTestExecution) | **GET** /testexecutions/{testExecutionId} |  |
| [**describeTestSet**](DefaultApi.md#describeTestSet) | **GET** /testsets/{testSetId} |  |
| [**describeTestSetDiscrepancyReport**](DefaultApi.md#describeTestSetDiscrepancyReport) | **GET** /testsetdiscrepancy/{testSetDiscrepancyReportId} |  |
| [**describeTestSetGeneration**](DefaultApi.md#describeTestSetGeneration) | **GET** /testsetgenerations/{testSetGenerationId} |  |
| [**getTestExecutionArtifactsUrl**](DefaultApi.md#getTestExecutionArtifactsUrl) | **GET** /testexecutions/{testExecutionId}/artifacturl |  |
| [**listAggregatedUtterances**](DefaultApi.md#listAggregatedUtterances) | **POST** /bots/{botId}/aggregatedutterances/ |  |
| [**listBotAliases**](DefaultApi.md#listBotAliases) | **POST** /bots/{botId}/botaliases/ |  |
| [**listBotLocales**](DefaultApi.md#listBotLocales) | **POST** /bots/{botId}/botversions/{botVersion}/botlocales/ |  |
| [**listBotRecommendations**](DefaultApi.md#listBotRecommendations) | **POST** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/botrecommendations/ |  |
| [**listBotVersions**](DefaultApi.md#listBotVersions) | **POST** /bots/{botId}/botversions/ |  |
| [**listBots**](DefaultApi.md#listBots) | **POST** /bots/ |  |
| [**listBuiltInIntents**](DefaultApi.md#listBuiltInIntents) | **POST** /builtins/locales/{localeId}/intents/ |  |
| [**listBuiltInSlotTypes**](DefaultApi.md#listBuiltInSlotTypes) | **POST** /builtins/locales/{localeId}/slottypes/ |  |
| [**listCustomVocabularyItems**](DefaultApi.md#listCustomVocabularyItems) | **POST** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/customvocabulary/DEFAULT/list |  |
| [**listExports**](DefaultApi.md#listExports) | **POST** /exports/ |  |
| [**listImports**](DefaultApi.md#listImports) | **POST** /imports/ |  |
| [**listIntentMetrics**](DefaultApi.md#listIntentMetrics) | **POST** /bots/{botId}/analytics/intentmetrics |  |
| [**listIntentPaths**](DefaultApi.md#listIntentPaths) | **POST** /bots/{botId}/analytics/intentpaths |  |
| [**listIntentStageMetrics**](DefaultApi.md#listIntentStageMetrics) | **POST** /bots/{botId}/analytics/intentstagemetrics |  |
| [**listIntents**](DefaultApi.md#listIntents) | **POST** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/intents/ |  |
| [**listRecommendedIntents**](DefaultApi.md#listRecommendedIntents) | **POST** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/botrecommendations/{botRecommendationId}/intents |  |
| [**listSessionAnalyticsData**](DefaultApi.md#listSessionAnalyticsData) | **POST** /bots/{botId}/analytics/sessions |  |
| [**listSessionMetrics**](DefaultApi.md#listSessionMetrics) | **POST** /bots/{botId}/analytics/sessionmetrics |  |
| [**listSlotTypes**](DefaultApi.md#listSlotTypes) | **POST** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/slottypes/ |  |
| [**listSlots**](DefaultApi.md#listSlots) | **POST** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/intents/{intentId}/slots/ |  |
| [**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceARN} |  |
| [**listTestExecutionResultItems**](DefaultApi.md#listTestExecutionResultItems) | **POST** /testexecutions/{testExecutionId}/results |  |
| [**listTestExecutions**](DefaultApi.md#listTestExecutions) | **POST** /testexecutions |  |
| [**listTestSetRecords**](DefaultApi.md#listTestSetRecords) | **POST** /testsets/{testSetId}/records |  |
| [**listTestSets**](DefaultApi.md#listTestSets) | **POST** /testsets |  |
| [**listUtteranceAnalyticsData**](DefaultApi.md#listUtteranceAnalyticsData) | **POST** /bots/{botId}/analytics/utterances |  |
| [**listUtteranceMetrics**](DefaultApi.md#listUtteranceMetrics) | **POST** /bots/{botId}/analytics/utterancemetrics |  |
| [**searchAssociatedTranscripts**](DefaultApi.md#searchAssociatedTranscripts) | **POST** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/botrecommendations/{botRecommendationId}/associatedtranscripts |  |
| [**startBotRecommendation**](DefaultApi.md#startBotRecommendation) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/botrecommendations/ |  |
| [**startImport**](DefaultApi.md#startImport) | **PUT** /imports/ |  |
| [**startTestExecution**](DefaultApi.md#startTestExecution) | **POST** /testsets/{testSetId}/testexecutions |  |
| [**startTestSetGeneration**](DefaultApi.md#startTestSetGeneration) | **PUT** /testsetgenerations |  |
| [**stopBotRecommendation**](DefaultApi.md#stopBotRecommendation) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/botrecommendations/{botRecommendationId}/stopbotrecommendation |  |
| [**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceARN} |  |
| [**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceARN}#tagKeys |  |
| [**updateBot**](DefaultApi.md#updateBot) | **PUT** /bots/{botId}/ |  |
| [**updateBotAlias**](DefaultApi.md#updateBotAlias) | **PUT** /bots/{botId}/botaliases/{botAliasId}/ |  |
| [**updateBotLocale**](DefaultApi.md#updateBotLocale) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/ |  |
| [**updateBotRecommendation**](DefaultApi.md#updateBotRecommendation) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/botrecommendations/{botRecommendationId}/ |  |
| [**updateExport**](DefaultApi.md#updateExport) | **PUT** /exports/{exportId}/ |  |
| [**updateIntent**](DefaultApi.md#updateIntent) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/intents/{intentId}/ |  |
| [**updateResourcePolicy**](DefaultApi.md#updateResourcePolicy) | **PUT** /policy/{resourceArn}/ |  |
| [**updateSlot**](DefaultApi.md#updateSlot) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/intents/{intentId}/slots/{slotId}/ |  |
| [**updateSlotType**](DefaultApi.md#updateSlotType) | **PUT** /bots/{botId}/botversions/{botVersion}/botlocales/{localeId}/slottypes/{slotTypeId}/ |  |
| [**updateTestSet**](DefaultApi.md#updateTestSet) | **PUT** /testsets/{testSetId} |  |


<a id="batchCreateCustomVocabularyItem"></a>
# **batchCreateCustomVocabularyItem**
> BatchCreateCustomVocabularyItemResponse batchCreateCustomVocabularyItem(botId, botVersion, localeId, batchCreateCustomVocabularyItemRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Create a batch of custom vocabulary items for a given bot locale&#39;s custom vocabulary.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The identifier of the bot associated with this custom vocabulary.
    String botVersion = "botVersion_example"; // String | The identifier of the version of the bot associated with this custom vocabulary.
    String localeId = "localeId_example"; // String | The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\"> Supported Languages </a>.
    BatchCreateCustomVocabularyItemRequest batchCreateCustomVocabularyItemRequest = new BatchCreateCustomVocabularyItemRequest(); // BatchCreateCustomVocabularyItemRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      BatchCreateCustomVocabularyItemResponse result = apiInstance.batchCreateCustomVocabularyItem(botId, botVersion, localeId, batchCreateCustomVocabularyItemRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchCreateCustomVocabularyItem");
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
| **botId** | **String**| The identifier of the bot associated with this custom vocabulary. | |
| **botVersion** | **String**| The identifier of the version of the bot associated with this custom vocabulary. | |
| **localeId** | **String**| The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt; Supported Languages &lt;/a&gt;. | |
| **batchCreateCustomVocabularyItemRequest** | [**BatchCreateCustomVocabularyItemRequest**](BatchCreateCustomVocabularyItemRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**BatchCreateCustomVocabularyItemResponse**](BatchCreateCustomVocabularyItemResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | InternalServerException |  -  |

<a id="batchDeleteCustomVocabularyItem"></a>
# **batchDeleteCustomVocabularyItem**
> BatchDeleteCustomVocabularyItemResponse batchDeleteCustomVocabularyItem(botId, botVersion, localeId, batchDeleteCustomVocabularyItemRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Delete a batch of custom vocabulary items for a given bot locale&#39;s custom vocabulary.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The identifier of the bot associated with this custom vocabulary.
    String botVersion = "botVersion_example"; // String | The identifier of the version of the bot associated with this custom vocabulary.
    String localeId = "localeId_example"; // String | The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\"> Supported Languages </a>.
    BatchDeleteCustomVocabularyItemRequest batchDeleteCustomVocabularyItemRequest = new BatchDeleteCustomVocabularyItemRequest(); // BatchDeleteCustomVocabularyItemRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      BatchDeleteCustomVocabularyItemResponse result = apiInstance.batchDeleteCustomVocabularyItem(botId, botVersion, localeId, batchDeleteCustomVocabularyItemRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchDeleteCustomVocabularyItem");
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
| **botId** | **String**| The identifier of the bot associated with this custom vocabulary. | |
| **botVersion** | **String**| The identifier of the version of the bot associated with this custom vocabulary. | |
| **localeId** | **String**| The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt; Supported Languages &lt;/a&gt;. | |
| **batchDeleteCustomVocabularyItemRequest** | [**BatchDeleteCustomVocabularyItemRequest**](BatchDeleteCustomVocabularyItemRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**BatchDeleteCustomVocabularyItemResponse**](BatchDeleteCustomVocabularyItemResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | InternalServerException |  -  |

<a id="batchUpdateCustomVocabularyItem"></a>
# **batchUpdateCustomVocabularyItem**
> BatchUpdateCustomVocabularyItemResponse batchUpdateCustomVocabularyItem(botId, botVersion, localeId, batchUpdateCustomVocabularyItemRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Update a batch of custom vocabulary items for a given bot locale&#39;s custom vocabulary.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The identifier of the bot associated with this custom vocabulary
    String botVersion = "botVersion_example"; // String | The identifier of the version of the bot associated with this custom vocabulary.
    String localeId = "localeId_example"; // String | The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\"> Supported Languages </a>.
    BatchUpdateCustomVocabularyItemRequest batchUpdateCustomVocabularyItemRequest = new BatchUpdateCustomVocabularyItemRequest(); // BatchUpdateCustomVocabularyItemRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      BatchUpdateCustomVocabularyItemResponse result = apiInstance.batchUpdateCustomVocabularyItem(botId, botVersion, localeId, batchUpdateCustomVocabularyItemRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchUpdateCustomVocabularyItem");
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
| **botId** | **String**| The identifier of the bot associated with this custom vocabulary | |
| **botVersion** | **String**| The identifier of the version of the bot associated with this custom vocabulary. | |
| **localeId** | **String**| The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt; Supported Languages &lt;/a&gt;. | |
| **batchUpdateCustomVocabularyItemRequest** | [**BatchUpdateCustomVocabularyItemRequest**](BatchUpdateCustomVocabularyItemRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**BatchUpdateCustomVocabularyItemResponse**](BatchUpdateCustomVocabularyItemResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | InternalServerException |  -  |

<a id="buildBotLocale"></a>
# **buildBotLocale**
> BuildBotLocaleResponse buildBotLocale(botId, botVersion, localeId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Builds a bot, its intents, and its slot types into a specific locale. A bot can be built into multiple locales. At runtime the locale is used to choose a specific build of the bot.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The identifier of the bot to build. The identifier is returned in the response from the <a href=\"https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html\">CreateBot</a> operation.
    String botVersion = "botVersion_example"; // String | The version of the bot to build. This can only be the draft version of the bot.
    String localeId = "localeId_example"; // String | The identifier of the language and locale that the bot will be used in. The string must match one of the supported locales. All of the intents, slot types, and slots used in the bot must have the same locale. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      BuildBotLocaleResponse result = apiInstance.buildBotLocale(botId, botVersion, localeId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#buildBotLocale");
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
| **botId** | **String**| The identifier of the bot to build. The identifier is returned in the response from the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html\&quot;&gt;CreateBot&lt;/a&gt; operation. | |
| **botVersion** | **String**| The version of the bot to build. This can only be the draft version of the bot. | |
| **localeId** | **String**| The identifier of the language and locale that the bot will be used in. The string must match one of the supported locales. All of the intents, slot types, and slots used in the bot must have the same locale. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**BuildBotLocaleResponse**](BuildBotLocaleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | PreconditionFailedException |  -  |
| **484** | ConflictException |  -  |
| **485** | InternalServerException |  -  |

<a id="createBot"></a>
# **createBot**
> CreateBotResponse createBot(createBotRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates an Amazon Lex conversational bot. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateBotRequest createBotRequest = new CreateBotRequest(); // CreateBotRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateBotResponse result = apiInstance.createBot(createBotRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createBot");
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
| **createBotRequest** | [**CreateBotRequest**](CreateBotRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateBotResponse**](CreateBotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | PreconditionFailedException |  -  |
| **484** | ConflictException |  -  |
| **485** | InternalServerException |  -  |

<a id="createBotAlias"></a>
# **createBotAlias**
> CreateBotAliasResponse createBotAlias(botId, createBotAliasRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates an alias for the specified version of a bot. Use an alias to enable you to change the version of a bot without updating applications that use the bot.&lt;/p&gt; &lt;p&gt;For example, you can create an alias called \&quot;PROD\&quot; that your applications use to call the Amazon Lex bot. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The unique identifier of the bot that the alias applies to.
    CreateBotAliasRequest createBotAliasRequest = new CreateBotAliasRequest(); // CreateBotAliasRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateBotAliasResponse result = apiInstance.createBotAlias(botId, createBotAliasRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createBotAlias");
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
| **botId** | **String**| The unique identifier of the bot that the alias applies to. | |
| **createBotAliasRequest** | [**CreateBotAliasRequest**](CreateBotAliasRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateBotAliasResponse**](CreateBotAliasResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | PreconditionFailedException |  -  |
| **484** | ConflictException |  -  |
| **485** | InternalServerException |  -  |

<a id="createBotLocale"></a>
# **createBotLocale**
> CreateBotLocaleResponse createBotLocale(botId, botVersion, createBotLocaleRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates a locale in the bot. The locale contains the intents and slot types that the bot uses in conversations with users in the specified language and locale. You must add a locale to a bot before you can add intents and slot types to the bot.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The identifier of the bot to create the locale for.
    String botVersion = "botVersion_example"; // String | The version of the bot to create the locale for. This can only be the draft version of the bot.
    CreateBotLocaleRequest createBotLocaleRequest = new CreateBotLocaleRequest(); // CreateBotLocaleRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateBotLocaleResponse result = apiInstance.createBotLocale(botId, botVersion, createBotLocaleRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createBotLocale");
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
| **botId** | **String**| The identifier of the bot to create the locale for. | |
| **botVersion** | **String**| The version of the bot to create the locale for. This can only be the draft version of the bot. | |
| **createBotLocaleRequest** | [**CreateBotLocaleRequest**](CreateBotLocaleRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateBotLocaleResponse**](CreateBotLocaleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | PreconditionFailedException |  -  |
| **484** | ConflictException |  -  |
| **485** | InternalServerException |  -  |

<a id="createBotVersion"></a>
# **createBotVersion**
> CreateBotVersionResponse createBotVersion(botId, createBotVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a new version of the bot based on the &lt;code&gt;DRAFT&lt;/code&gt; version. If the &lt;code&gt;DRAFT&lt;/code&gt; version of this resource hasn&#39;t changed since you created the last version, Amazon Lex doesn&#39;t create a new version, it returns the last created version.&lt;/p&gt; &lt;p&gt;When you create the first version of a bot, Amazon Lex sets the version to 1. Subsequent versions increment by 1.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The identifier of the bot to create the version for.
    CreateBotVersionRequest createBotVersionRequest = new CreateBotVersionRequest(); // CreateBotVersionRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateBotVersionResponse result = apiInstance.createBotVersion(botId, createBotVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createBotVersion");
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
| **botId** | **String**| The identifier of the bot to create the version for. | |
| **createBotVersionRequest** | [**CreateBotVersionRequest**](CreateBotVersionRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateBotVersionResponse**](CreateBotVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | PreconditionFailedException |  -  |
| **484** | ConflictException |  -  |
| **485** | InternalServerException |  -  |

<a id="createExport"></a>
# **createExport**
> CreateExportResponse createExport(createExportRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a zip archive containing the contents of a bot or a bot locale. The archive contains a directory structure that contains JSON files that define the bot.&lt;/p&gt; &lt;p&gt;You can create an archive that contains the complete definition of a bot, or you can specify that the archive contain only the definition of a single bot locale.&lt;/p&gt; &lt;p&gt;For more information about exporting bots, and about the structure of the export archive, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/importing-exporting.html\&quot;&gt; Importing and exporting bots &lt;/a&gt; &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateExportRequest createExportRequest = new CreateExportRequest(); // CreateExportRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateExportResponse result = apiInstance.createExport(createExportRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createExport");
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
| **createExportRequest** | [**CreateExportRequest**](CreateExportRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateExportResponse**](CreateExportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ConflictException |  -  |
| **485** | InternalServerException |  -  |

<a id="createIntent"></a>
# **createIntent**
> CreateIntentResponse createIntent(botId, botVersion, localeId, createIntentRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates an intent.&lt;/p&gt; &lt;p&gt;To define the interaction between the user and your bot, you define one or more intents. For example, for a pizza ordering bot you would create an &lt;code&gt;OrderPizza&lt;/code&gt; intent.&lt;/p&gt; &lt;p&gt;When you create an intent, you must provide a name. You can optionally provide the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Sample utterances. For example, \&quot;I want to order a pizza\&quot; and \&quot;Can I order a pizza.\&quot; You can&#39;t provide utterances for built-in intents.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Information to be gathered. You specify slots for the information that you bot requests from the user. You can specify standard slot types, such as date and time, or custom slot types for your application.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;How the intent is fulfilled. You can provide a Lambda function or configure the intent to return the intent information to your client application. If you use a Lambda function, Amazon Lex invokes the function when all of the intent information is available.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A confirmation prompt to send to the user to confirm an intent. For example, \&quot;Shall I order your pizza?\&quot;&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A conclusion statement to send to the user after the intent is fulfilled. For example, \&quot;I ordered your pizza.\&quot;&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A follow-up prompt that asks the user for additional activity. For example, \&quot;Do you want a drink with your pizza?\&quot;&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The identifier of the bot associated with this intent.
    String botVersion = "botVersion_example"; // String | The version of the bot associated with this intent.
    String localeId = "localeId_example"; // String | The identifier of the language and locale where this intent is used. All of the bots, slot types, and slots used by the intent must have the same locale. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
    CreateIntentRequest createIntentRequest = new CreateIntentRequest(); // CreateIntentRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateIntentResponse result = apiInstance.createIntent(botId, botVersion, localeId, createIntentRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createIntent");
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
| **botId** | **String**| The identifier of the bot associated with this intent. | |
| **botVersion** | **String**| The version of the bot associated with this intent. | |
| **localeId** | **String**| The identifier of the language and locale where this intent is used. All of the bots, slot types, and slots used by the intent must have the same locale. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | |
| **createIntentRequest** | [**CreateIntentRequest**](CreateIntentRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateIntentResponse**](CreateIntentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | PreconditionFailedException |  -  |
| **484** | ConflictException |  -  |
| **485** | InternalServerException |  -  |

<a id="createResourcePolicy"></a>
# **createResourcePolicy**
> CreateResourcePolicyResponse createResourcePolicy(resourceArn, updateResourcePolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates a new resource policy with the specified policy statements.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.
    UpdateResourcePolicyRequest updateResourcePolicyRequest = new UpdateResourcePolicyRequest(); // UpdateResourcePolicyRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateResourcePolicyResponse result = apiInstance.createResourcePolicy(resourceArn, updateResourcePolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createResourcePolicy");
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
| **resourceArn** | **String**| The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to. | |
| **updateResourcePolicyRequest** | [**UpdateResourcePolicyRequest**](UpdateResourcePolicyRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateResourcePolicyResponse**](CreateResourcePolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | PreconditionFailedException |  -  |
| **483** | ValidationException |  -  |
| **484** | InternalServerException |  -  |
| **485** | ThrottlingException |  -  |

<a id="createResourcePolicyStatement"></a>
# **createResourcePolicyStatement**
> CreateResourcePolicyStatementResponse createResourcePolicyStatement(resourceArn, createResourcePolicyStatementRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, expectedRevisionId)



&lt;p&gt;Adds a new resource policy statement to a bot or bot alias. If a resource policy exists, the statement is added to the current resource policy. If a policy doesn&#39;t exist, a new policy is created.&lt;/p&gt; &lt;p&gt;You can&#39;t create a resource policy statement that allows cross-account access.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.
    CreateResourcePolicyStatementRequest createResourcePolicyStatementRequest = new CreateResourcePolicyStatementRequest(); // CreateResourcePolicyStatementRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String expectedRevisionId = "expectedRevisionId_example"; // String | <p>The identifier of the revision of the policy to edit. If this revision ID doesn't match the current revision ID, Amazon Lex throws an exception.</p> <p>If you don't specify a revision, Amazon Lex overwrites the contents of the policy with the new values.</p>
    try {
      CreateResourcePolicyStatementResponse result = apiInstance.createResourcePolicyStatement(resourceArn, createResourcePolicyStatementRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, expectedRevisionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createResourcePolicyStatement");
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
| **resourceArn** | **String**| The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to. | |
| **createResourcePolicyStatementRequest** | [**CreateResourcePolicyStatementRequest**](CreateResourcePolicyStatementRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **expectedRevisionId** | **String**| &lt;p&gt;The identifier of the revision of the policy to edit. If this revision ID doesn&#39;t match the current revision ID, Amazon Lex throws an exception.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a revision, Amazon Lex overwrites the contents of the policy with the new values.&lt;/p&gt; | [optional] |

### Return type

[**CreateResourcePolicyStatementResponse**](CreateResourcePolicyStatementResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | ConflictException |  -  |
| **482** | ServiceQuotaExceededException |  -  |
| **483** | PreconditionFailedException |  -  |
| **484** | ValidationException |  -  |
| **485** | InternalServerException |  -  |
| **486** | ThrottlingException |  -  |

<a id="createSlot"></a>
# **createSlot**
> CreateSlotResponse createSlot(botId, botVersion, localeId, intentId, createSlotRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates a slot in an intent. A slot is a variable needed to fulfill an intent. For example, an &lt;code&gt;OrderPizza&lt;/code&gt; intent might need slots for size, crust, and number of pizzas. For each slot, you define one or more utterances that Amazon Lex uses to elicit a response from the user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The identifier of the bot associated with the slot.
    String botVersion = "botVersion_example"; // String | The version of the bot associated with the slot.
    String localeId = "localeId_example"; // String | The identifier of the language and locale that the slot will be used in. The string must match one of the supported locales. All of the bots, intents, slot types used by the slot must have the same locale. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
    String intentId = "intentId_example"; // String | The identifier of the intent that contains the slot.
    CreateSlotRequest createSlotRequest = new CreateSlotRequest(); // CreateSlotRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateSlotResponse result = apiInstance.createSlot(botId, botVersion, localeId, intentId, createSlotRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createSlot");
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
| **botId** | **String**| The identifier of the bot associated with the slot. | |
| **botVersion** | **String**| The version of the bot associated with the slot. | |
| **localeId** | **String**| The identifier of the language and locale that the slot will be used in. The string must match one of the supported locales. All of the bots, intents, slot types used by the slot must have the same locale. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | |
| **intentId** | **String**| The identifier of the intent that contains the slot. | |
| **createSlotRequest** | [**CreateSlotRequest**](CreateSlotRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateSlotResponse**](CreateSlotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | PreconditionFailedException |  -  |
| **484** | ConflictException |  -  |
| **485** | InternalServerException |  -  |

<a id="createSlotType"></a>
# **createSlotType**
> CreateSlotTypeResponse createSlotType(botId, botVersion, localeId, createSlotTypeRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a custom slot type&lt;/p&gt; &lt;p&gt; To create a custom slot type, specify a name for the slot type and a set of enumeration values, the values that a slot of this type can assume. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The identifier of the bot associated with this slot type.
    String botVersion = "botVersion_example"; // String | The identifier of the bot version associated with this slot type.
    String localeId = "localeId_example"; // String | The identifier of the language and locale that the slot type will be used in. The string must match one of the supported locales. All of the bots, intents, and slots used by the slot type must have the same locale. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
    CreateSlotTypeRequest createSlotTypeRequest = new CreateSlotTypeRequest(); // CreateSlotTypeRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateSlotTypeResponse result = apiInstance.createSlotType(botId, botVersion, localeId, createSlotTypeRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createSlotType");
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
| **botId** | **String**| The identifier of the bot associated with this slot type. | |
| **botVersion** | **String**| The identifier of the bot version associated with this slot type. | |
| **localeId** | **String**| The identifier of the language and locale that the slot type will be used in. The string must match one of the supported locales. All of the bots, intents, and slots used by the slot type must have the same locale. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | |
| **createSlotTypeRequest** | [**CreateSlotTypeRequest**](CreateSlotTypeRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateSlotTypeResponse**](CreateSlotTypeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | PreconditionFailedException |  -  |
| **484** | ConflictException |  -  |
| **485** | InternalServerException |  -  |

<a id="createTestSetDiscrepancyReport"></a>
# **createTestSetDiscrepancyReport**
> CreateTestSetDiscrepancyReportResponse createTestSetDiscrepancyReport(testSetId, createTestSetDiscrepancyReportRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Create a report that describes the differences between the bot and the test set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String testSetId = "testSetId_example"; // String | The test set Id for the test set discrepancy report.
    CreateTestSetDiscrepancyReportRequest createTestSetDiscrepancyReportRequest = new CreateTestSetDiscrepancyReportRequest(); // CreateTestSetDiscrepancyReportRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateTestSetDiscrepancyReportResponse result = apiInstance.createTestSetDiscrepancyReport(testSetId, createTestSetDiscrepancyReportRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createTestSetDiscrepancyReport");
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
| **testSetId** | **String**| The test set Id for the test set discrepancy report. | |
| **createTestSetDiscrepancyReportRequest** | [**CreateTestSetDiscrepancyReportRequest**](CreateTestSetDiscrepancyReportRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateTestSetDiscrepancyReportResponse**](CreateTestSetDiscrepancyReportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ConflictException |  -  |
| **484** | InternalServerException |  -  |
| **485** | ResourceNotFoundException |  -  |

<a id="createUploadUrl"></a>
# **createUploadUrl**
> CreateUploadUrlResponse createUploadUrl(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets a pre-signed S3 write URL that you use to upload the zip archive when importing a bot or a bot locale. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateUploadUrlResponse result = apiInstance.createUploadUrl(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createUploadUrl");
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
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateUploadUrlResponse**](CreateUploadUrlResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ValidationException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ConflictException |  -  |
| **484** | InternalServerException |  -  |

<a id="deleteBot"></a>
# **deleteBot**
> DeleteBotResponse deleteBot(botId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, skipResourceInUseCheck)



&lt;p&gt;Deletes all versions of a bot, including the &lt;code&gt;Draft&lt;/code&gt; version. To delete a specific version, use the &lt;code&gt;DeleteBotVersion&lt;/code&gt; operation.&lt;/p&gt; &lt;p&gt;When you delete a bot, all of the resources contained in the bot are also deleted. Deleting a bot removes all locales, intents, slot, and slot types defined for the bot.&lt;/p&gt; &lt;p&gt;If a bot has an alias, the &lt;code&gt;DeleteBot&lt;/code&gt; operation returns a &lt;code&gt;ResourceInUseException&lt;/code&gt; exception. If you want to delete the bot and the alias, set the &lt;code&gt;skipResourceInUseCheck&lt;/code&gt; parameter to &lt;code&gt;true&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The identifier of the bot to delete. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Boolean skipResourceInUseCheck = true; // Boolean | By default, Amazon Lex checks if any other resource, such as an alias or bot network, is using the bot version before it is deleted and throws a <code>ResourceInUseException</code> exception if the bot is being used by another resource. Set this parameter to <code>true</code> to skip this check and remove the bot even if it is being used by another resource.
    try {
      DeleteBotResponse result = apiInstance.deleteBot(botId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, skipResourceInUseCheck);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteBot");
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
| **botId** | **String**| The identifier of the bot to delete.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **skipResourceInUseCheck** | **Boolean**| By default, Amazon Lex checks if any other resource, such as an alias or bot network, is using the bot version before it is deleted and throws a &lt;code&gt;ResourceInUseException&lt;/code&gt; exception if the bot is being used by another resource. Set this parameter to &lt;code&gt;true&lt;/code&gt; to skip this check and remove the bot even if it is being used by another resource. | [optional] |

### Return type

[**DeleteBotResponse**](DeleteBotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ConflictException |  -  |
| **484** | PreconditionFailedException |  -  |
| **485** | InternalServerException |  -  |

<a id="deleteBotAlias"></a>
# **deleteBotAlias**
> DeleteBotAliasResponse deleteBotAlias(botAliasId, botId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, skipResourceInUseCheck)



Deletes the specified bot alias.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botAliasId = "botAliasId_example"; // String | The unique identifier of the bot alias to delete.
    String botId = "botId_example"; // String | The unique identifier of the bot associated with the alias to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Boolean skipResourceInUseCheck = true; // Boolean | By default, Amazon Lex checks if any other resource, such as a bot network, is using the bot alias before it is deleted and throws a <code>ResourceInUseException</code> exception if the alias is being used by another resource. Set this parameter to <code>true</code> to skip this check and remove the alias even if it is being used by another resource.
    try {
      DeleteBotAliasResponse result = apiInstance.deleteBotAlias(botAliasId, botId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, skipResourceInUseCheck);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteBotAlias");
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
| **botAliasId** | **String**| The unique identifier of the bot alias to delete. | |
| **botId** | **String**| The unique identifier of the bot associated with the alias to delete. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **skipResourceInUseCheck** | **Boolean**| By default, Amazon Lex checks if any other resource, such as a bot network, is using the bot alias before it is deleted and throws a &lt;code&gt;ResourceInUseException&lt;/code&gt; exception if the alias is being used by another resource. Set this parameter to &lt;code&gt;true&lt;/code&gt; to skip this check and remove the alias even if it is being used by another resource. | [optional] |

### Return type

[**DeleteBotAliasResponse**](DeleteBotAliasResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ConflictException |  -  |
| **484** | PreconditionFailedException |  -  |
| **485** | InternalServerException |  -  |

<a id="deleteBotLocale"></a>
# **deleteBotLocale**
> DeleteBotLocaleResponse deleteBotLocale(botId, botVersion, localeId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Removes a locale from a bot.&lt;/p&gt; &lt;p&gt;When you delete a locale, all intents, slots, and slot types defined for the locale are also deleted.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The unique identifier of the bot that contains the locale.
    String botVersion = "botVersion_example"; // String | The version of the bot that contains the locale. 
    String localeId = "localeId_example"; // String | The identifier of the language and locale that will be deleted. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeleteBotLocaleResponse result = apiInstance.deleteBotLocale(botId, botVersion, localeId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteBotLocale");
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
| **botId** | **String**| The unique identifier of the bot that contains the locale. | |
| **botVersion** | **String**| The version of the bot that contains the locale.  | |
| **localeId** | **String**| The identifier of the language and locale that will be deleted. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeleteBotLocaleResponse**](DeleteBotLocaleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | PreconditionFailedException |  -  |
| **484** | ConflictException |  -  |
| **485** | InternalServerException |  -  |

<a id="deleteBotVersion"></a>
# **deleteBotVersion**
> DeleteBotVersionResponse deleteBotVersion(botId, botVersion, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, skipResourceInUseCheck)



Deletes a specific version of a bot. To delete all versions of a bot, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteBot.html\&quot;&gt;DeleteBot&lt;/a&gt; operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The identifier of the bot that contains the version.
    String botVersion = "botVersion_example"; // String | The version of the bot to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Boolean skipResourceInUseCheck = true; // Boolean | By default, Amazon Lex checks if any other resource, such as an alias or bot network, is using the bot version before it is deleted and throws a <code>ResourceInUseException</code> exception if the version is being used by another resource. Set this parameter to <code>true</code> to skip this check and remove the version even if it is being used by another resource.
    try {
      DeleteBotVersionResponse result = apiInstance.deleteBotVersion(botId, botVersion, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, skipResourceInUseCheck);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteBotVersion");
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
| **botId** | **String**| The identifier of the bot that contains the version. | |
| **botVersion** | **String**| The version of the bot to delete. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **skipResourceInUseCheck** | **Boolean**| By default, Amazon Lex checks if any other resource, such as an alias or bot network, is using the bot version before it is deleted and throws a &lt;code&gt;ResourceInUseException&lt;/code&gt; exception if the version is being used by another resource. Set this parameter to &lt;code&gt;true&lt;/code&gt; to skip this check and remove the version even if it is being used by another resource. | [optional] |

### Return type

[**DeleteBotVersionResponse**](DeleteBotVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ConflictException |  -  |
| **484** | PreconditionFailedException |  -  |
| **485** | InternalServerException |  -  |

<a id="deleteCustomVocabulary"></a>
# **deleteCustomVocabulary**
> DeleteCustomVocabularyResponse deleteCustomVocabulary(botId, botVersion, localeId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Removes a custom vocabulary from the specified locale in the specified bot.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The unique identifier of the bot to remove the custom vocabulary from.
    String botVersion = "botVersion_example"; // String | The version of the bot to remove the custom vocabulary from.
    String localeId = "localeId_example"; // String | The locale identifier for the locale that contains the custom vocabulary to remove.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeleteCustomVocabularyResponse result = apiInstance.deleteCustomVocabulary(botId, botVersion, localeId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteCustomVocabulary");
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
| **botId** | **String**| The unique identifier of the bot to remove the custom vocabulary from. | |
| **botVersion** | **String**| The version of the bot to remove the custom vocabulary from. | |
| **localeId** | **String**| The locale identifier for the locale that contains the custom vocabulary to remove. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeleteCustomVocabularyResponse**](DeleteCustomVocabularyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | PreconditionFailedException |  -  |
| **484** | ConflictException |  -  |
| **485** | InternalServerException |  -  |

<a id="deleteExport"></a>
# **deleteExport**
> DeleteExportResponse deleteExport(exportId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Removes a previous export and the associated files stored in an S3 bucket.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String exportId = "exportId_example"; // String | The unique identifier of the export to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeleteExportResponse result = apiInstance.deleteExport(exportId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteExport");
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
| **exportId** | **String**| The unique identifier of the export to delete. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeleteExportResponse**](DeleteExportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | PreconditionFailedException |  -  |
| **484** | InternalServerException |  -  |

<a id="deleteImport"></a>
# **deleteImport**
> DeleteImportResponse deleteImport(importId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Removes a previous import and the associated file stored in an S3 bucket.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String importId = "importId_example"; // String | The unique identifier of the import to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeleteImportResponse result = apiInstance.deleteImport(importId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteImport");
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
| **importId** | **String**| The unique identifier of the import to delete. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeleteImportResponse**](DeleteImportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | PreconditionFailedException |  -  |
| **484** | InternalServerException |  -  |

<a id="deleteIntent"></a>
# **deleteIntent**
> deleteIntent(intentId, botId, botVersion, localeId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Removes the specified intent.&lt;/p&gt; &lt;p&gt;Deleting an intent also deletes the slots associated with the intent.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String intentId = "intentId_example"; // String | The unique identifier of the intent to delete.
    String botId = "botId_example"; // String | The identifier of the bot associated with the intent.
    String botVersion = "botVersion_example"; // String | The version of the bot associated with the intent.
    String localeId = "localeId_example"; // String | The identifier of the language and locale where the bot will be deleted. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteIntent(intentId, botId, botVersion, localeId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteIntent");
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
| **intentId** | **String**| The unique identifier of the intent to delete. | |
| **botId** | **String**| The identifier of the bot associated with the intent. | |
| **botVersion** | **String**| The version of the bot associated with the intent. | |
| **localeId** | **String**| The identifier of the language and locale where the bot will be deleted. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ConflictException |  -  |
| **484** | PreconditionFailedException |  -  |
| **485** | InternalServerException |  -  |

<a id="deleteResourcePolicy"></a>
# **deleteResourcePolicy**
> DeleteResourcePolicyResponse deleteResourcePolicy(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, expectedRevisionId)



Removes an existing policy from a bot or bot alias. If the resource doesn&#39;t have a policy attached, Amazon Lex returns an exception.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the bot or bot alias that has the resource policy attached.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String expectedRevisionId = "expectedRevisionId_example"; // String | <p>The identifier of the revision to edit. If this ID doesn't match the current revision number, Amazon Lex returns an exception</p> <p>If you don't specify a revision ID, Amazon Lex will delete the current policy.</p>
    try {
      DeleteResourcePolicyResponse result = apiInstance.deleteResourcePolicy(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, expectedRevisionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteResourcePolicy");
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
| **resourceArn** | **String**| The Amazon Resource Name (ARN) of the bot or bot alias that has the resource policy attached. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **expectedRevisionId** | **String**| &lt;p&gt;The identifier of the revision to edit. If this ID doesn&#39;t match the current revision number, Amazon Lex returns an exception&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a revision ID, Amazon Lex will delete the current policy.&lt;/p&gt; | [optional] |

### Return type

[**DeleteResourcePolicyResponse**](DeleteResourcePolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | PreconditionFailedException |  -  |
| **482** | InternalServerException |  -  |
| **483** | ThrottlingException |  -  |

<a id="deleteResourcePolicyStatement"></a>
# **deleteResourcePolicyStatement**
> DeleteResourcePolicyStatementResponse deleteResourcePolicyStatement(resourceArn, statementId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, expectedRevisionId)



Deletes a policy statement from a resource policy. If you delete the last statement from a policy, the policy is deleted. If you specify a statement ID that doesn&#39;t exist in the policy, or if the bot or bot alias doesn&#39;t have a policy attached, Amazon Lex returns an exception.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.
    String statementId = "statementId_example"; // String | The name of the statement (SID) to delete from the policy.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String expectedRevisionId = "expectedRevisionId_example"; // String | <p>The identifier of the revision of the policy to delete the statement from. If this revision ID doesn't match the current revision ID, Amazon Lex throws an exception.</p> <p>If you don't specify a revision, Amazon Lex removes the current contents of the statement. </p>
    try {
      DeleteResourcePolicyStatementResponse result = apiInstance.deleteResourcePolicyStatement(resourceArn, statementId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, expectedRevisionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteResourcePolicyStatement");
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
| **resourceArn** | **String**| The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to. | |
| **statementId** | **String**| The name of the statement (SID) to delete from the policy. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **expectedRevisionId** | **String**| &lt;p&gt;The identifier of the revision of the policy to delete the statement from. If this revision ID doesn&#39;t match the current revision ID, Amazon Lex throws an exception.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a revision, Amazon Lex removes the current contents of the statement. &lt;/p&gt; | [optional] |

### Return type

[**DeleteResourcePolicyStatementResponse**](DeleteResourcePolicyStatementResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | PreconditionFailedException |  -  |
| **482** | InternalServerException |  -  |
| **483** | ThrottlingException |  -  |

<a id="deleteSlot"></a>
# **deleteSlot**
> deleteSlot(slotId, botId, botVersion, localeId, intentId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Deletes the specified slot from an intent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String slotId = "slotId_example"; // String | The identifier of the slot to delete. 
    String botId = "botId_example"; // String | The identifier of the bot associated with the slot to delete.
    String botVersion = "botVersion_example"; // String | The version of the bot associated with the slot to delete.
    String localeId = "localeId_example"; // String | The identifier of the language and locale that the slot will be deleted from. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
    String intentId = "intentId_example"; // String | The identifier of the intent associated with the slot.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteSlot(slotId, botId, botVersion, localeId, intentId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteSlot");
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
| **slotId** | **String**| The identifier of the slot to delete.  | |
| **botId** | **String**| The identifier of the bot associated with the slot to delete. | |
| **botVersion** | **String**| The version of the bot associated with the slot to delete. | |
| **localeId** | **String**| The identifier of the language and locale that the slot will be deleted from. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | |
| **intentId** | **String**| The identifier of the intent associated with the slot. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ConflictException |  -  |
| **484** | PreconditionFailedException |  -  |
| **485** | InternalServerException |  -  |

<a id="deleteSlotType"></a>
# **deleteSlotType**
> deleteSlotType(slotTypeId, botId, botVersion, localeId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, skipResourceInUseCheck)



&lt;p&gt;Deletes a slot type from a bot locale.&lt;/p&gt; &lt;p&gt;If a slot is using the slot type, Amazon Lex throws a &lt;code&gt;ResourceInUseException&lt;/code&gt; exception. To avoid the exception, set the &lt;code&gt;skipResourceInUseCheck&lt;/code&gt; parameter to &lt;code&gt;true&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String slotTypeId = "slotTypeId_example"; // String | The identifier of the slot type to delete.
    String botId = "botId_example"; // String | The identifier of the bot associated with the slot type.
    String botVersion = "botVersion_example"; // String | The version of the bot associated with the slot type.
    String localeId = "localeId_example"; // String | The identifier of the language and locale that the slot type will be deleted from. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Boolean skipResourceInUseCheck = true; // Boolean | By default, the <code>DeleteSlotType</code> operations throws a <code>ResourceInUseException</code> exception if you try to delete a slot type used by a slot. Set the <code>skipResourceInUseCheck</code> parameter to <code>true</code> to skip this check and remove the slot type even if a slot uses it.
    try {
      apiInstance.deleteSlotType(slotTypeId, botId, botVersion, localeId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, skipResourceInUseCheck);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteSlotType");
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
| **slotTypeId** | **String**| The identifier of the slot type to delete. | |
| **botId** | **String**| The identifier of the bot associated with the slot type. | |
| **botVersion** | **String**| The version of the bot associated with the slot type. | |
| **localeId** | **String**| The identifier of the language and locale that the slot type will be deleted from. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **skipResourceInUseCheck** | **Boolean**| By default, the &lt;code&gt;DeleteSlotType&lt;/code&gt; operations throws a &lt;code&gt;ResourceInUseException&lt;/code&gt; exception if you try to delete a slot type used by a slot. Set the &lt;code&gt;skipResourceInUseCheck&lt;/code&gt; parameter to &lt;code&gt;true&lt;/code&gt; to skip this check and remove the slot type even if a slot uses it. | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ConflictException |  -  |
| **484** | PreconditionFailedException |  -  |
| **485** | InternalServerException |  -  |

<a id="deleteTestSet"></a>
# **deleteTestSet**
> deleteTestSet(testSetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



The action to delete the selected test set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String testSetId = "testSetId_example"; // String | The test set Id of the test set to be deleted.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteTestSet(testSetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteTestSet");
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
| **testSetId** | **String**| The test set Id of the test set to be deleted. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ConflictException |  -  |
| **484** | PreconditionFailedException |  -  |
| **485** | InternalServerException |  -  |

<a id="deleteUtterances"></a>
# **deleteUtterances**
> Object deleteUtterances(botId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, localeId, sessionId)



&lt;p&gt;Deletes stored utterances.&lt;/p&gt; &lt;p&gt;Amazon Lex stores the utterances that users send to your bot. Utterances are stored for 15 days for use with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListAggregatedUtterances.html\&quot;&gt;ListAggregatedUtterances&lt;/a&gt; operation, and then stored indefinitely for use in improving the ability of your bot to respond to user input..&lt;/p&gt; &lt;p&gt;Use the &lt;code&gt;DeleteUtterances&lt;/code&gt; operation to manually delete utterances for a specific session. When you use the &lt;code&gt;DeleteUtterances&lt;/code&gt; operation, utterances stored for improving your bot&#39;s ability to respond to user input are deleted immediately. Utterances stored for use with the &lt;code&gt;ListAggregatedUtterances&lt;/code&gt; operation are deleted after 15 days.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The unique identifier of the bot that contains the utterances.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String localeId = "localeId_example"; // String | The identifier of the language and locale where the utterances were collected. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
    String sessionId = "sessionId_example"; // String | The unique identifier of the session with the user. The ID is returned in the response from the <a href=\"https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeText.html\">RecognizeText</a> and <a href=\"https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeUtterance.html\">RecognizeUtterance</a> operations.
    try {
      Object result = apiInstance.deleteUtterances(botId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, localeId, sessionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteUtterances");
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
| **botId** | **String**| The unique identifier of the bot that contains the utterances. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **localeId** | **String**| The identifier of the language and locale where the utterances were collected. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | [optional] |
| **sessionId** | **String**| The unique identifier of the session with the user. The ID is returned in the response from the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeText.html\&quot;&gt;RecognizeText&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeUtterance.html\&quot;&gt;RecognizeUtterance&lt;/a&gt; operations. | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | ValidationException |  -  |
| **481** | ThrottlingException |  -  |
| **482** | InternalServerException |  -  |

<a id="describeBot"></a>
# **describeBot**
> DescribeBotResponse describeBot(botId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Provides metadata information about a bot. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The unique identifier of the bot to describe.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeBotResponse result = apiInstance.describeBot(botId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeBot");
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
| **botId** | **String**| The unique identifier of the bot to describe. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeBotResponse**](DescribeBotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | InternalServerException |  -  |

<a id="describeBotAlias"></a>
# **describeBotAlias**
> DescribeBotAliasResponse describeBotAlias(botAliasId, botId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Get information about a specific bot alias.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botAliasId = "botAliasId_example"; // String | The identifier of the bot alias to describe.
    String botId = "botId_example"; // String | The identifier of the bot associated with the bot alias to describe.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeBotAliasResponse result = apiInstance.describeBotAlias(botAliasId, botId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeBotAlias");
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
| **botAliasId** | **String**| The identifier of the bot alias to describe. | |
| **botId** | **String**| The identifier of the bot associated with the bot alias to describe. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeBotAliasResponse**](DescribeBotAliasResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | InternalServerException |  -  |

<a id="describeBotLocale"></a>
# **describeBotLocale**
> DescribeBotLocaleResponse describeBotLocale(botId, botVersion, localeId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Describes the settings that a bot has for a specific locale. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The identifier of the bot associated with the locale.
    String botVersion = "botVersion_example"; // String | The version of the bot associated with the locale.
    String localeId = "localeId_example"; // String | The unique identifier of the locale to describe. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeBotLocaleResponse result = apiInstance.describeBotLocale(botId, botVersion, localeId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeBotLocale");
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
| **botId** | **String**| The identifier of the bot associated with the locale. | |
| **botVersion** | **String**| The version of the bot associated with the locale. | |
| **localeId** | **String**| The unique identifier of the locale to describe. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeBotLocaleResponse**](DescribeBotLocaleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | InternalServerException |  -  |

<a id="describeBotRecommendation"></a>
# **describeBotRecommendation**
> DescribeBotRecommendationResponse describeBotRecommendation(botId, botVersion, localeId, botRecommendationId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Provides metadata information about a bot recommendation. This information will enable you to get a description on the request inputs, to download associated transcripts after processing is complete, and to download intents and slot-types generated by the bot recommendation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The unique identifier of the bot associated with the bot recommendation.
    String botVersion = "botVersion_example"; // String | The version of the bot associated with the bot recommendation.
    String localeId = "localeId_example"; // String | The identifier of the language and locale of the bot recommendation to describe. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
    String botRecommendationId = "botRecommendationId_example"; // String | The identifier of the bot recommendation to describe.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeBotRecommendationResponse result = apiInstance.describeBotRecommendation(botId, botVersion, localeId, botRecommendationId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeBotRecommendation");
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
| **botId** | **String**| The unique identifier of the bot associated with the bot recommendation. | |
| **botVersion** | **String**| The version of the bot associated with the bot recommendation. | |
| **localeId** | **String**| The identifier of the language and locale of the bot recommendation to describe. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | |
| **botRecommendationId** | **String**| The identifier of the bot recommendation to describe. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeBotRecommendationResponse**](DescribeBotRecommendationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ValidationException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | InternalServerException |  -  |

<a id="describeBotVersion"></a>
# **describeBotVersion**
> DescribeBotVersionResponse describeBotVersion(botId, botVersion, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Provides metadata about a version of a bot.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The identifier of the bot containing the version to return metadata for.
    String botVersion = "botVersion_example"; // String | The version of the bot to return metadata for.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeBotVersionResponse result = apiInstance.describeBotVersion(botId, botVersion, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeBotVersion");
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
| **botId** | **String**| The identifier of the bot containing the version to return metadata for. | |
| **botVersion** | **String**| The version of the bot to return metadata for. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeBotVersionResponse**](DescribeBotVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | InternalServerException |  -  |

<a id="describeCustomVocabularyMetadata"></a>
# **describeCustomVocabularyMetadata**
> DescribeCustomVocabularyMetadataResponse describeCustomVocabularyMetadata(botId, botVersion, localeId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Provides metadata information about a custom vocabulary.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The unique identifier of the bot that contains the custom vocabulary.
    String botVersion = "botVersion_example"; // String | The bot version of the bot to return metadata for.
    String localeId = "localeId_example"; // String | The locale to return the custom vocabulary information for. The locale must be <code>en_GB</code>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeCustomVocabularyMetadataResponse result = apiInstance.describeCustomVocabularyMetadata(botId, botVersion, localeId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeCustomVocabularyMetadata");
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
| **botId** | **String**| The unique identifier of the bot that contains the custom vocabulary. | |
| **botVersion** | **String**| The bot version of the bot to return metadata for. | |
| **localeId** | **String**| The locale to return the custom vocabulary information for. The locale must be &lt;code&gt;en_GB&lt;/code&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeCustomVocabularyMetadataResponse**](DescribeCustomVocabularyMetadataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | InternalServerException |  -  |

<a id="describeExport"></a>
# **describeExport**
> DescribeExportResponse describeExport(exportId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets information about a specific export.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String exportId = "exportId_example"; // String | The unique identifier of the export to describe.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeExportResponse result = apiInstance.describeExport(exportId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeExport");
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
| **exportId** | **String**| The unique identifier of the export to describe. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeExportResponse**](DescribeExportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ValidationException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | InternalServerException |  -  |

<a id="describeImport"></a>
# **describeImport**
> DescribeImportResponse describeImport(importId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets information about a specific import.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String importId = "importId_example"; // String | The unique identifier of the import to describe.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeImportResponse result = apiInstance.describeImport(importId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeImport");
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
| **importId** | **String**| The unique identifier of the import to describe. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeImportResponse**](DescribeImportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ValidationException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | InternalServerException |  -  |

<a id="describeIntent"></a>
# **describeIntent**
> DescribeIntentResponse describeIntent(intentId, botId, botVersion, localeId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Returns metadata about an intent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String intentId = "intentId_example"; // String | The identifier of the intent to describe.
    String botId = "botId_example"; // String | The identifier of the bot associated with the intent.
    String botVersion = "botVersion_example"; // String | The version of the bot associated with the intent.
    String localeId = "localeId_example"; // String | The identifier of the language and locale of the intent to describe. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeIntentResponse result = apiInstance.describeIntent(intentId, botId, botVersion, localeId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeIntent");
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
| **intentId** | **String**| The identifier of the intent to describe. | |
| **botId** | **String**| The identifier of the bot associated with the intent. | |
| **botVersion** | **String**| The version of the bot associated with the intent. | |
| **localeId** | **String**| The identifier of the language and locale of the intent to describe. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeIntentResponse**](DescribeIntentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | InternalServerException |  -  |

<a id="describeResourcePolicy"></a>
# **describeResourcePolicy**
> DescribeResourcePolicyResponse describeResourcePolicy(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets the resource policy and policy revision for a bot or bot alias.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeResourcePolicyResponse result = apiInstance.describeResourcePolicy(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeResourcePolicy");
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
| **resourceArn** | **String**| The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeResourcePolicyResponse**](DescribeResourcePolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ThrottlingException |  -  |

<a id="describeSlot"></a>
# **describeSlot**
> DescribeSlotResponse describeSlot(slotId, botId, botVersion, localeId, intentId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets metadata information about a slot.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String slotId = "slotId_example"; // String | The unique identifier for the slot.
    String botId = "botId_example"; // String | The identifier of the bot associated with the slot.
    String botVersion = "botVersion_example"; // String | The version of the bot associated with the slot.
    String localeId = "localeId_example"; // String | The identifier of the language and locale of the slot to describe. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
    String intentId = "intentId_example"; // String | The identifier of the intent that contains the slot.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeSlotResponse result = apiInstance.describeSlot(slotId, botId, botVersion, localeId, intentId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeSlot");
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
| **slotId** | **String**| The unique identifier for the slot. | |
| **botId** | **String**| The identifier of the bot associated with the slot. | |
| **botVersion** | **String**| The version of the bot associated with the slot. | |
| **localeId** | **String**| The identifier of the language and locale of the slot to describe. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | |
| **intentId** | **String**| The identifier of the intent that contains the slot. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeSlotResponse**](DescribeSlotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | InternalServerException |  -  |

<a id="describeSlotType"></a>
# **describeSlotType**
> DescribeSlotTypeResponse describeSlotType(slotTypeId, botId, botVersion, localeId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets metadata information about a slot type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String slotTypeId = "slotTypeId_example"; // String | The identifier of the slot type.
    String botId = "botId_example"; // String | The identifier of the bot associated with the slot type.
    String botVersion = "botVersion_example"; // String | The version of the bot associated with the slot type.
    String localeId = "localeId_example"; // String | The identifier of the language and locale of the slot type to describe. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeSlotTypeResponse result = apiInstance.describeSlotType(slotTypeId, botId, botVersion, localeId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeSlotType");
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
| **slotTypeId** | **String**| The identifier of the slot type. | |
| **botId** | **String**| The identifier of the bot associated with the slot type. | |
| **botVersion** | **String**| The version of the bot associated with the slot type. | |
| **localeId** | **String**| The identifier of the language and locale of the slot type to describe. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeSlotTypeResponse**](DescribeSlotTypeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | InternalServerException |  -  |

<a id="describeTestExecution"></a>
# **describeTestExecution**
> DescribeTestExecutionResponse describeTestExecution(testExecutionId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets metadata information about the test execution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String testExecutionId = "testExecutionId_example"; // String | The execution Id of the test set execution.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeTestExecutionResponse result = apiInstance.describeTestExecution(testExecutionId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeTestExecution");
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
| **testExecutionId** | **String**| The execution Id of the test set execution. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeTestExecutionResponse**](DescribeTestExecutionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | InternalServerException |  -  |

<a id="describeTestSet"></a>
# **describeTestSet**
> DescribeTestSetResponse describeTestSet(testSetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets metadata information about the test set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String testSetId = "testSetId_example"; // String | The test set Id for the test set request.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeTestSetResponse result = apiInstance.describeTestSet(testSetId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeTestSet");
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
| **testSetId** | **String**| The test set Id for the test set request. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeTestSetResponse**](DescribeTestSetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | InternalServerException |  -  |

<a id="describeTestSetDiscrepancyReport"></a>
# **describeTestSetDiscrepancyReport**
> DescribeTestSetDiscrepancyReportResponse describeTestSetDiscrepancyReport(testSetDiscrepancyReportId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets metadata information about the test set discrepancy report.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String testSetDiscrepancyReportId = "testSetDiscrepancyReportId_example"; // String | The unique identifier of the test set discrepancy report.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeTestSetDiscrepancyReportResponse result = apiInstance.describeTestSetDiscrepancyReport(testSetDiscrepancyReportId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeTestSetDiscrepancyReport");
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
| **testSetDiscrepancyReportId** | **String**| The unique identifier of the test set discrepancy report. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeTestSetDiscrepancyReportResponse**](DescribeTestSetDiscrepancyReportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | InternalServerException |  -  |

<a id="describeTestSetGeneration"></a>
# **describeTestSetGeneration**
> DescribeTestSetGenerationResponse describeTestSetGeneration(testSetGenerationId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets metadata information about the test set generation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String testSetGenerationId = "testSetGenerationId_example"; // String | The unique identifier of the test set generation.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeTestSetGenerationResponse result = apiInstance.describeTestSetGeneration(testSetGenerationId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeTestSetGeneration");
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
| **testSetGenerationId** | **String**| The unique identifier of the test set generation. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeTestSetGenerationResponse**](DescribeTestSetGenerationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | InternalServerException |  -  |

<a id="getTestExecutionArtifactsUrl"></a>
# **getTestExecutionArtifactsUrl**
> GetTestExecutionArtifactsUrlResponse getTestExecutionArtifactsUrl(testExecutionId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



The pre-signed Amazon S3 URL to download the test execution result artifacts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String testExecutionId = "testExecutionId_example"; // String | The unique identifier of the completed test execution.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetTestExecutionArtifactsUrlResponse result = apiInstance.getTestExecutionArtifactsUrl(testExecutionId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getTestExecutionArtifactsUrl");
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
| **testExecutionId** | **String**| The unique identifier of the completed test execution. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetTestExecutionArtifactsUrlResponse**](GetTestExecutionArtifactsUrlResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | InternalServerException |  -  |

<a id="listAggregatedUtterances"></a>
# **listAggregatedUtterances**
> ListAggregatedUtterancesResponse listAggregatedUtterances(botId, listAggregatedUtterancesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



&lt;p&gt;Provides a list of utterances that users have sent to the bot.&lt;/p&gt; &lt;p&gt;Utterances are aggregated by the text of the utterance. For example, all instances where customers used the phrase \&quot;I want to order pizza\&quot; are aggregated into the same line in the response.&lt;/p&gt; &lt;p&gt;You can see both detected utterances and missed utterances. A detected utterance is where the bot properly recognized the utterance and activated the associated intent. A missed utterance was not recognized by the bot and didn&#39;t activate an intent.&lt;/p&gt; &lt;p&gt;Utterances can be aggregated for a bot alias or for a bot version, but not both at the same time.&lt;/p&gt; &lt;p&gt;Utterances statistics are not generated under the following conditions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;childDirected&lt;/code&gt; field was set to true when the bot was created.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You are using slot obfuscation with one or more slots.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You opted out of participating in improving Amazon Lex.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The unique identifier of the bot associated with this request.
    ListAggregatedUtterancesRequest listAggregatedUtterancesRequest = new ListAggregatedUtterancesRequest(); // ListAggregatedUtterancesRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListAggregatedUtterancesResponse result = apiInstance.listAggregatedUtterances(botId, listAggregatedUtterancesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAggregatedUtterances");
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
| **botId** | **String**| The unique identifier of the bot associated with this request. | |
| **listAggregatedUtterancesRequest** | [**ListAggregatedUtterancesRequest**](ListAggregatedUtterancesRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListAggregatedUtterancesResponse**](ListAggregatedUtterancesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ValidationException |  -  |
| **481** | PreconditionFailedException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | InternalServerException |  -  |

<a id="listBotAliases"></a>
# **listBotAliases**
> ListBotAliasesResponse listBotAliases(botId, listBotAliasesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Gets a list of aliases for the specified bot.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The identifier of the bot to list aliases for.
    ListBotAliasesRequest listBotAliasesRequest = new ListBotAliasesRequest(); // ListBotAliasesRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListBotAliasesResponse result = apiInstance.listBotAliases(botId, listBotAliasesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listBotAliases");
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
| **botId** | **String**| The identifier of the bot to list aliases for. | |
| **listBotAliasesRequest** | [**ListBotAliasesRequest**](ListBotAliasesRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListBotAliasesResponse**](ListBotAliasesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | InternalServerException |  -  |

<a id="listBotLocales"></a>
# **listBotLocales**
> ListBotLocalesResponse listBotLocales(botId, botVersion, listBotLocalesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Gets a list of locales for the specified bot.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The identifier of the bot to list locales for.
    String botVersion = "botVersion_example"; // String | The version of the bot to list locales for.
    ListBotLocalesRequest listBotLocalesRequest = new ListBotLocalesRequest(); // ListBotLocalesRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListBotLocalesResponse result = apiInstance.listBotLocales(botId, botVersion, listBotLocalesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listBotLocales");
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
| **botId** | **String**| The identifier of the bot to list locales for. | |
| **botVersion** | **String**| The version of the bot to list locales for. | |
| **listBotLocalesRequest** | [**ListBotLocalesRequest**](ListBotLocalesRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListBotLocalesResponse**](ListBotLocalesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | InternalServerException |  -  |

<a id="listBotRecommendations"></a>
# **listBotRecommendations**
> ListBotRecommendationsResponse listBotRecommendations(botId, botVersion, localeId, listBotRecommendationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Get a list of bot recommendations that meet the specified criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The unique identifier of the bot that contains the bot recommendation list.
    String botVersion = "botVersion_example"; // String | The version of the bot that contains the bot recommendation list.
    String localeId = "localeId_example"; // String | The identifier of the language and locale of the bot recommendation list.
    ListBotRecommendationsRequest listBotRecommendationsRequest = new ListBotRecommendationsRequest(); // ListBotRecommendationsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListBotRecommendationsResponse result = apiInstance.listBotRecommendations(botId, botVersion, localeId, listBotRecommendationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listBotRecommendations");
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
| **botId** | **String**| The unique identifier of the bot that contains the bot recommendation list. | |
| **botVersion** | **String**| The version of the bot that contains the bot recommendation list. | |
| **localeId** | **String**| The identifier of the language and locale of the bot recommendation list. | |
| **listBotRecommendationsRequest** | [**ListBotRecommendationsRequest**](ListBotRecommendationsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListBotRecommendationsResponse**](ListBotRecommendationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ValidationException |  -  |
| **482** | InternalServerException |  -  |
| **483** | ResourceNotFoundException |  -  |

<a id="listBotVersions"></a>
# **listBotVersions**
> ListBotVersionsResponse listBotVersions(botId, listBotVersionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



&lt;p&gt;Gets information about all of the versions of a bot.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;ListBotVersions&lt;/code&gt; operation returns a summary of each version of a bot. For example, if a bot has three numbered versions, the &lt;code&gt;ListBotVersions&lt;/code&gt; operation returns for summaries, one for each numbered version and one for the &lt;code&gt;DRAFT&lt;/code&gt; version.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;ListBotVersions&lt;/code&gt; operation always returns at least one version, the &lt;code&gt;DRAFT&lt;/code&gt; version.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The identifier of the bot to list versions for.
    ListBotVersionsRequest listBotVersionsRequest = new ListBotVersionsRequest(); // ListBotVersionsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListBotVersionsResponse result = apiInstance.listBotVersions(botId, listBotVersionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listBotVersions");
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
| **botId** | **String**| The identifier of the bot to list versions for. | |
| **listBotVersionsRequest** | [**ListBotVersionsRequest**](ListBotVersionsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListBotVersionsResponse**](ListBotVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | InternalServerException |  -  |

<a id="listBots"></a>
# **listBots**
> ListBotsResponse listBots(listBotsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Gets a list of available bots.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ListBotsRequest listBotsRequest = new ListBotsRequest(); // ListBotsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListBotsResponse result = apiInstance.listBots(listBotsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listBots");
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
| **listBotsRequest** | [**ListBotsRequest**](ListBotsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListBotsResponse**](ListBotsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | InternalServerException |  -  |

<a id="listBuiltInIntents"></a>
# **listBuiltInIntents**
> ListBuiltInIntentsResponse listBuiltInIntents(localeId, listBuiltInIntentsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



&lt;p&gt;Gets a list of built-in intents provided by Amazon Lex that you can use in your bot. &lt;/p&gt; &lt;p&gt;To use a built-in intent as a the base for your own intent, include the built-in intent signature in the &lt;code&gt;parentIntentSignature&lt;/code&gt; parameter when you call the &lt;code&gt;CreateIntent&lt;/code&gt; operation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateIntent.html\&quot;&gt;CreateIntent&lt;/a&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String localeId = "localeId_example"; // String | The identifier of the language and locale of the intents to list. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
    ListBuiltInIntentsRequest listBuiltInIntentsRequest = new ListBuiltInIntentsRequest(); // ListBuiltInIntentsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListBuiltInIntentsResponse result = apiInstance.listBuiltInIntents(localeId, listBuiltInIntentsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listBuiltInIntents");
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
| **localeId** | **String**| The identifier of the language and locale of the intents to list. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | |
| **listBuiltInIntentsRequest** | [**ListBuiltInIntentsRequest**](ListBuiltInIntentsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListBuiltInIntentsResponse**](ListBuiltInIntentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | InternalServerException |  -  |

<a id="listBuiltInSlotTypes"></a>
# **listBuiltInSlotTypes**
> ListBuiltInSlotTypesResponse listBuiltInSlotTypes(localeId, listBuiltInSlotTypesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Gets a list of built-in slot types that meet the specified criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String localeId = "localeId_example"; // String | The identifier of the language and locale of the slot types to list. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
    ListBuiltInSlotTypesRequest listBuiltInSlotTypesRequest = new ListBuiltInSlotTypesRequest(); // ListBuiltInSlotTypesRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListBuiltInSlotTypesResponse result = apiInstance.listBuiltInSlotTypes(localeId, listBuiltInSlotTypesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listBuiltInSlotTypes");
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
| **localeId** | **String**| The identifier of the language and locale of the slot types to list. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | |
| **listBuiltInSlotTypesRequest** | [**ListBuiltInSlotTypesRequest**](ListBuiltInSlotTypesRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListBuiltInSlotTypesResponse**](ListBuiltInSlotTypesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | InternalServerException |  -  |

<a id="listCustomVocabularyItems"></a>
# **listCustomVocabularyItems**
> ListCustomVocabularyItemsResponse listCustomVocabularyItems(botId, botVersion, localeId, listCustomVocabularyItemsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Paginated list of custom vocabulary items for a given bot locale&#39;s custom vocabulary.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The identifier of the version of the bot associated with this custom vocabulary.
    String botVersion = "botVersion_example"; // String | The bot version of the bot to the list custom vocabulary request.
    String localeId = "localeId_example"; // String | The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see Supported languages (https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html).
    ListCustomVocabularyItemsRequest listCustomVocabularyItemsRequest = new ListCustomVocabularyItemsRequest(); // ListCustomVocabularyItemsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListCustomVocabularyItemsResponse result = apiInstance.listCustomVocabularyItems(botId, botVersion, localeId, listCustomVocabularyItemsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listCustomVocabularyItems");
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
| **botId** | **String**| The identifier of the version of the bot associated with this custom vocabulary. | |
| **botVersion** | **String**| The bot version of the bot to the list custom vocabulary request. | |
| **localeId** | **String**| The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see Supported languages (https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html). | |
| **listCustomVocabularyItemsRequest** | [**ListCustomVocabularyItemsRequest**](ListCustomVocabularyItemsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListCustomVocabularyItemsResponse**](ListCustomVocabularyItemsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | InternalServerException |  -  |

<a id="listExports"></a>
# **listExports**
> ListExportsResponse listExports(listExportsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Lists the exports for a bot, bot locale, or custom vocabulary. Exports are kept in the list for 7 days.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ListExportsRequest listExportsRequest = new ListExportsRequest(); // ListExportsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListExportsResponse result = apiInstance.listExports(listExportsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listExports");
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
| **listExportsRequest** | [**ListExportsRequest**](ListExportsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListExportsResponse**](ListExportsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ValidationException |  -  |
| **482** | InternalServerException |  -  |

<a id="listImports"></a>
# **listImports**
> ListImportsResponse listImports(listImportsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Lists the imports for a bot, bot locale, or custom vocabulary. Imports are kept in the list for 7 days.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ListImportsRequest listImportsRequest = new ListImportsRequest(); // ListImportsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListImportsResponse result = apiInstance.listImports(listImportsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listImports");
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
| **listImportsRequest** | [**ListImportsRequest**](ListImportsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListImportsResponse**](ListImportsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ValidationException |  -  |
| **482** | InternalServerException |  -  |

<a id="listIntentMetrics"></a>
# **listIntentMetrics**
> ListIntentMetricsResponse listIntentMetrics(botId, listIntentMetricsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



&lt;p&gt;Retrieves summary metrics for the intents in your bot. The following fields are required:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;metrics&lt;/code&gt; – A list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsIntentMetric.html\&quot;&gt;AnalyticsIntentMetric&lt;/a&gt; objects. In each object, use the &lt;code&gt;name&lt;/code&gt; field to specify the metric to calculate, the &lt;code&gt;statistic&lt;/code&gt; field to specify whether to calculate the &lt;code&gt;Sum&lt;/code&gt;, &lt;code&gt;Average&lt;/code&gt;, or &lt;code&gt;Max&lt;/code&gt; number, and the &lt;code&gt;order&lt;/code&gt; field to specify whether to sort the results in &lt;code&gt;Ascending&lt;/code&gt; or &lt;code&gt;Descending&lt;/code&gt; order.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;startDateTime&lt;/code&gt; and &lt;code&gt;endDateTime&lt;/code&gt; – Define a time range for which you want to retrieve results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Of the optional fields, you can organize the results in the following ways:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;filters&lt;/code&gt; field to filter the results, the &lt;code&gt;groupBy&lt;/code&gt; field to specify categories by which to group the results, and the &lt;code&gt;binBy&lt;/code&gt; field to specify time intervals by which to group the results.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;maxResults&lt;/code&gt; field to limit the number of results to return in a single response and the &lt;code&gt;nextToken&lt;/code&gt; field to return the next batch of results if the response does not return the full set of results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Note that an &lt;code&gt;order&lt;/code&gt; field exists in both &lt;code&gt;binBy&lt;/code&gt; and &lt;code&gt;metrics&lt;/code&gt;. You can specify only one &lt;code&gt;order&lt;/code&gt; in a given request.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The identifier for the bot for which you want to retrieve intent metrics.
    ListIntentMetricsRequest listIntentMetricsRequest = new ListIntentMetricsRequest(); // ListIntentMetricsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListIntentMetricsResponse result = apiInstance.listIntentMetrics(botId, listIntentMetricsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listIntentMetrics");
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
| **botId** | **String**| The identifier for the bot for which you want to retrieve intent metrics. | |
| **listIntentMetricsRequest** | [**ListIntentMetricsRequest**](ListIntentMetricsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListIntentMetricsResponse**](ListIntentMetricsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ValidationException |  -  |
| **482** | PreconditionFailedException |  -  |
| **483** | ServiceQuotaExceededException |  -  |
| **484** | InternalServerException |  -  |

<a id="listIntentPaths"></a>
# **listIntentPaths**
> ListIntentPathsResponse listIntentPaths(botId, listIntentPathsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Retrieves summary statistics for a path of intents that users take over sessions with your bot. The following fields are required:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;startDateTime&lt;/code&gt; and &lt;code&gt;endDateTime&lt;/code&gt; – Define a time range for which you want to retrieve results.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;intentPath&lt;/code&gt; – Define an order of intents for which you want to retrieve metrics. Separate intents in the path with a forward slash. For example, populate the &lt;code&gt;intentPath&lt;/code&gt; field with &lt;code&gt;/BookCar/BookHotel&lt;/code&gt; to see details about how many times users invoked the &lt;code&gt;BookCar&lt;/code&gt; and &lt;code&gt;BookHotel&lt;/code&gt; intents in that order.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Use the optional &lt;code&gt;filters&lt;/code&gt; field to filter the results.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The identifier for the bot for which you want to retrieve intent path metrics.
    ListIntentPathsRequest listIntentPathsRequest = new ListIntentPathsRequest(); // ListIntentPathsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListIntentPathsResponse result = apiInstance.listIntentPaths(botId, listIntentPathsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listIntentPaths");
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
| **botId** | **String**| The identifier for the bot for which you want to retrieve intent path metrics. | |
| **listIntentPathsRequest** | [**ListIntentPathsRequest**](ListIntentPathsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListIntentPathsResponse**](ListIntentPathsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ValidationException |  -  |
| **482** | PreconditionFailedException |  -  |
| **483** | ServiceQuotaExceededException |  -  |
| **484** | InternalServerException |  -  |

<a id="listIntentStageMetrics"></a>
# **listIntentStageMetrics**
> ListIntentStageMetricsResponse listIntentStageMetrics(botId, listIntentStageMetricsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



&lt;p&gt;Retrieves summary metrics for the stages within intents in your bot. The following fields are required:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;metrics&lt;/code&gt; – A list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsIntentStageMetric.html\&quot;&gt;AnalyticsIntentStageMetric&lt;/a&gt; objects. In each object, use the &lt;code&gt;name&lt;/code&gt; field to specify the metric to calculate, the &lt;code&gt;statistic&lt;/code&gt; field to specify whether to calculate the &lt;code&gt;Sum&lt;/code&gt;, &lt;code&gt;Average&lt;/code&gt;, or &lt;code&gt;Max&lt;/code&gt; number, and the &lt;code&gt;order&lt;/code&gt; field to specify whether to sort the results in &lt;code&gt;Ascending&lt;/code&gt; or &lt;code&gt;Descending&lt;/code&gt; order.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;startDateTime&lt;/code&gt; and &lt;code&gt;endDateTime&lt;/code&gt; – Define a time range for which you want to retrieve results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Of the optional fields, you can organize the results in the following ways:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;filters&lt;/code&gt; field to filter the results, the &lt;code&gt;groupBy&lt;/code&gt; field to specify categories by which to group the results, and the &lt;code&gt;binBy&lt;/code&gt; field to specify time intervals by which to group the results.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;maxResults&lt;/code&gt; field to limit the number of results to return in a single response and the &lt;code&gt;nextToken&lt;/code&gt; field to return the next batch of results if the response does not return the full set of results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Note that an &lt;code&gt;order&lt;/code&gt; field exists in both &lt;code&gt;binBy&lt;/code&gt; and &lt;code&gt;metrics&lt;/code&gt;. You can only specify one &lt;code&gt;order&lt;/code&gt; in a given request.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The identifier for the bot for which you want to retrieve intent stage metrics.
    ListIntentStageMetricsRequest listIntentStageMetricsRequest = new ListIntentStageMetricsRequest(); // ListIntentStageMetricsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListIntentStageMetricsResponse result = apiInstance.listIntentStageMetrics(botId, listIntentStageMetricsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listIntentStageMetrics");
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
| **botId** | **String**| The identifier for the bot for which you want to retrieve intent stage metrics. | |
| **listIntentStageMetricsRequest** | [**ListIntentStageMetricsRequest**](ListIntentStageMetricsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListIntentStageMetricsResponse**](ListIntentStageMetricsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ValidationException |  -  |
| **482** | PreconditionFailedException |  -  |
| **483** | ServiceQuotaExceededException |  -  |
| **484** | InternalServerException |  -  |

<a id="listIntents"></a>
# **listIntents**
> ListIntentsResponse listIntents(botId, botVersion, localeId, listIntentsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Get a list of intents that meet the specified criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The unique identifier of the bot that contains the intent.
    String botVersion = "botVersion_example"; // String | The version of the bot that contains the intent.
    String localeId = "localeId_example"; // String | The identifier of the language and locale of the intents to list. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
    ListIntentsRequest listIntentsRequest = new ListIntentsRequest(); // ListIntentsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListIntentsResponse result = apiInstance.listIntents(botId, botVersion, localeId, listIntentsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listIntents");
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
| **botId** | **String**| The unique identifier of the bot that contains the intent. | |
| **botVersion** | **String**| The version of the bot that contains the intent. | |
| **localeId** | **String**| The identifier of the language and locale of the intents to list. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | |
| **listIntentsRequest** | [**ListIntentsRequest**](ListIntentsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListIntentsResponse**](ListIntentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | InternalServerException |  -  |

<a id="listRecommendedIntents"></a>
# **listRecommendedIntents**
> ListRecommendedIntentsResponse listRecommendedIntents(botId, botVersion, localeId, botRecommendationId, listRecommendedIntentsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Gets a list of recommended intents provided by the bot recommendation that you can use in your bot. Intents in the response are ordered by relevance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The unique identifier of the bot associated with the recommended intents.
    String botVersion = "botVersion_example"; // String | The version of the bot that contains the recommended intents.
    String localeId = "localeId_example"; // String | The identifier of the language and locale of the recommended intents.
    String botRecommendationId = "botRecommendationId_example"; // String | The identifier of the bot recommendation that contains the recommended intents.
    ListRecommendedIntentsRequest listRecommendedIntentsRequest = new ListRecommendedIntentsRequest(); // ListRecommendedIntentsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListRecommendedIntentsResponse result = apiInstance.listRecommendedIntents(botId, botVersion, localeId, botRecommendationId, listRecommendedIntentsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listRecommendedIntents");
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
| **botId** | **String**| The unique identifier of the bot associated with the recommended intents. | |
| **botVersion** | **String**| The version of the bot that contains the recommended intents. | |
| **localeId** | **String**| The identifier of the language and locale of the recommended intents. | |
| **botRecommendationId** | **String**| The identifier of the bot recommendation that contains the recommended intents. | |
| **listRecommendedIntentsRequest** | [**ListRecommendedIntentsRequest**](ListRecommendedIntentsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListRecommendedIntentsResponse**](ListRecommendedIntentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | InternalServerException |  -  |
| **484** | ResourceNotFoundException |  -  |

<a id="listSessionAnalyticsData"></a>
# **listSessionAnalyticsData**
> ListSessionAnalyticsDataResponse listSessionAnalyticsData(botId, listSessionAnalyticsDataRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



&lt;p&gt;Retrieves a list of metadata for individual user sessions with your bot. The &lt;code&gt;startDateTime&lt;/code&gt; and &lt;code&gt;endDateTime&lt;/code&gt; fields are required. These fields define a time range for which you want to retrieve results. Of the optional fields, you can organize the results in the following ways:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;filters&lt;/code&gt; field to filter the results and the &lt;code&gt;sortBy&lt;/code&gt; field to specify the values by which to sort the results.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;maxResults&lt;/code&gt; field to limit the number of results to return in a single response and the &lt;code&gt;nextToken&lt;/code&gt; field to return the next batch of results if the response does not return the full set of results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The identifier for the bot for which you want to retrieve session analytics.
    ListSessionAnalyticsDataRequest listSessionAnalyticsDataRequest = new ListSessionAnalyticsDataRequest(); // ListSessionAnalyticsDataRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListSessionAnalyticsDataResponse result = apiInstance.listSessionAnalyticsData(botId, listSessionAnalyticsDataRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listSessionAnalyticsData");
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
| **botId** | **String**| The identifier for the bot for which you want to retrieve session analytics. | |
| **listSessionAnalyticsDataRequest** | [**ListSessionAnalyticsDataRequest**](ListSessionAnalyticsDataRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListSessionAnalyticsDataResponse**](ListSessionAnalyticsDataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ValidationException |  -  |
| **482** | PreconditionFailedException |  -  |
| **483** | ServiceQuotaExceededException |  -  |
| **484** | InternalServerException |  -  |

<a id="listSessionMetrics"></a>
# **listSessionMetrics**
> ListSessionMetricsResponse listSessionMetrics(botId, listSessionMetricsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



&lt;p&gt;Retrieves summary metrics for the user sessions with your bot. The following fields are required:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;metrics&lt;/code&gt; – A list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsSessionMetric.html\&quot;&gt;AnalyticsSessionMetric&lt;/a&gt; objects. In each object, use the &lt;code&gt;name&lt;/code&gt; field to specify the metric to calculate, the &lt;code&gt;statistic&lt;/code&gt; field to specify whether to calculate the &lt;code&gt;Sum&lt;/code&gt;, &lt;code&gt;Average&lt;/code&gt;, or &lt;code&gt;Max&lt;/code&gt; number, and the &lt;code&gt;order&lt;/code&gt; field to specify whether to sort the results in &lt;code&gt;Ascending&lt;/code&gt; or &lt;code&gt;Descending&lt;/code&gt; order.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;startDateTime&lt;/code&gt; and &lt;code&gt;endDateTime&lt;/code&gt; – Define a time range for which you want to retrieve results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Of the optional fields, you can organize the results in the following ways:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;filters&lt;/code&gt; field to filter the results, the &lt;code&gt;groupBy&lt;/code&gt; field to specify categories by which to group the results, and the &lt;code&gt;binBy&lt;/code&gt; field to specify time intervals by which to group the results.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;maxResults&lt;/code&gt; field to limit the number of results to return in a single response and the &lt;code&gt;nextToken&lt;/code&gt; field to return the next batch of results if the response does not return the full set of results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Note that an &lt;code&gt;order&lt;/code&gt; field exists in both &lt;code&gt;binBy&lt;/code&gt; and &lt;code&gt;metrics&lt;/code&gt;. Currently, you can specify it in either field, but not in both.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The identifier for the bot for which you want to retrieve session metrics.
    ListSessionMetricsRequest listSessionMetricsRequest = new ListSessionMetricsRequest(); // ListSessionMetricsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListSessionMetricsResponse result = apiInstance.listSessionMetrics(botId, listSessionMetricsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listSessionMetrics");
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
| **botId** | **String**| The identifier for the bot for which you want to retrieve session metrics. | |
| **listSessionMetricsRequest** | [**ListSessionMetricsRequest**](ListSessionMetricsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListSessionMetricsResponse**](ListSessionMetricsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ValidationException |  -  |
| **482** | PreconditionFailedException |  -  |
| **483** | ServiceQuotaExceededException |  -  |
| **484** | InternalServerException |  -  |

<a id="listSlotTypes"></a>
# **listSlotTypes**
> ListSlotTypesResponse listSlotTypes(botId, botVersion, localeId, listSlotTypesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Gets a list of slot types that match the specified criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The unique identifier of the bot that contains the slot types.
    String botVersion = "botVersion_example"; // String | The version of the bot that contains the slot type.
    String localeId = "localeId_example"; // String | The identifier of the language and locale of the slot types to list. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
    ListSlotTypesRequest listSlotTypesRequest = new ListSlotTypesRequest(); // ListSlotTypesRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListSlotTypesResponse result = apiInstance.listSlotTypes(botId, botVersion, localeId, listSlotTypesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listSlotTypes");
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
| **botId** | **String**| The unique identifier of the bot that contains the slot types. | |
| **botVersion** | **String**| The version of the bot that contains the slot type. | |
| **localeId** | **String**| The identifier of the language and locale of the slot types to list. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | |
| **listSlotTypesRequest** | [**ListSlotTypesRequest**](ListSlotTypesRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListSlotTypesResponse**](ListSlotTypesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | InternalServerException |  -  |

<a id="listSlots"></a>
# **listSlots**
> ListSlotsResponse listSlots(botId, botVersion, localeId, intentId, listSlotsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Gets a list of slots that match the specified criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The identifier of the bot that contains the slot.
    String botVersion = "botVersion_example"; // String | The version of the bot that contains the slot.
    String localeId = "localeId_example"; // String | The identifier of the language and locale of the slots to list. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
    String intentId = "intentId_example"; // String | The unique identifier of the intent that contains the slot.
    ListSlotsRequest listSlotsRequest = new ListSlotsRequest(); // ListSlotsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListSlotsResponse result = apiInstance.listSlots(botId, botVersion, localeId, intentId, listSlotsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listSlots");
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
| **botId** | **String**| The identifier of the bot that contains the slot. | |
| **botVersion** | **String**| The version of the bot that contains the slot. | |
| **localeId** | **String**| The identifier of the language and locale of the slots to list. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | |
| **intentId** | **String**| The unique identifier of the intent that contains the slot. | |
| **listSlotsRequest** | [**ListSlotsRequest**](ListSlotsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListSlotsResponse**](ListSlotsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | InternalServerException |  -  |

<a id="listTagsForResource"></a>
# **listTagsForResource**
> ListTagsForResourceResponse listTagsForResource(resourceARN, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets a list of tags associated with a resource. Only bots, bot aliases, and bot channels can have tags associated with them.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceARN = "resourceARN_example"; // String | The Amazon Resource Name (ARN) of the resource to get a list of tags for.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListTagsForResourceResponse result = apiInstance.listTagsForResource(resourceARN, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTagsForResource");
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
| **resourceARN** | **String**| The Amazon Resource Name (ARN) of the resource to get a list of tags for. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ThrottlingException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ValidationException |  -  |

<a id="listTestExecutionResultItems"></a>
# **listTestExecutionResultItems**
> ListTestExecutionResultItemsResponse listTestExecutionResultItems(testExecutionId, listTestExecutionResultItemsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



Gets a list of test execution result items.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String testExecutionId = "testExecutionId_example"; // String | The unique identifier of the test execution to list the result items.
    ListTestExecutionResultItemsRequest listTestExecutionResultItemsRequest = new ListTestExecutionResultItemsRequest(); // ListTestExecutionResultItemsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListTestExecutionResultItemsResponse result = apiInstance.listTestExecutionResultItems(testExecutionId, listTestExecutionResultItemsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTestExecutionResultItems");
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
| **testExecutionId** | **String**| The unique identifier of the test execution to list the result items. | |
| **listTestExecutionResultItemsRequest** | [**ListTestExecutionResultItemsRequest**](ListTestExecutionResultItemsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListTestExecutionResultItemsResponse**](ListTestExecutionResultItemsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | InternalServerException |  -  |

<a id="listTestExecutions"></a>
# **listTestExecutions**
> ListTestExecutionsResponse listTestExecutions(listTestExecutionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



The list of test set executions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ListTestExecutionsRequest listTestExecutionsRequest = new ListTestExecutionsRequest(); // ListTestExecutionsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListTestExecutionsResponse result = apiInstance.listTestExecutions(listTestExecutionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTestExecutions");
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
| **listTestExecutionsRequest** | [**ListTestExecutionsRequest**](ListTestExecutionsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListTestExecutionsResponse**](ListTestExecutionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | InternalServerException |  -  |

<a id="listTestSetRecords"></a>
# **listTestSetRecords**
> ListTestSetRecordsResponse listTestSetRecords(testSetId, listTestSetRecordsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



The list of test set records.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String testSetId = "testSetId_example"; // String | The identifier of the test set to list its test set records.
    ListTestSetRecordsRequest listTestSetRecordsRequest = new ListTestSetRecordsRequest(); // ListTestSetRecordsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListTestSetRecordsResponse result = apiInstance.listTestSetRecords(testSetId, listTestSetRecordsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTestSetRecords");
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
| **testSetId** | **String**| The identifier of the test set to list its test set records. | |
| **listTestSetRecordsRequest** | [**ListTestSetRecordsRequest**](ListTestSetRecordsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListTestSetRecordsResponse**](ListTestSetRecordsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | InternalServerException |  -  |

<a id="listTestSets"></a>
# **listTestSets**
> ListTestSetsResponse listTestSets(listTestSetsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



The list of the test sets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ListTestSetsRequest listTestSetsRequest = new ListTestSetsRequest(); // ListTestSetsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListTestSetsResponse result = apiInstance.listTestSets(listTestSetsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTestSets");
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
| **listTestSetsRequest** | [**ListTestSetsRequest**](ListTestSetsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListTestSetsResponse**](ListTestSetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | InternalServerException |  -  |

<a id="listUtteranceAnalyticsData"></a>
# **listUtteranceAnalyticsData**
> ListUtteranceAnalyticsDataResponse listUtteranceAnalyticsData(botId, listUtteranceAnalyticsDataRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



&lt;note&gt; &lt;p&gt;To use this API operation, your IAM role must have permissions to perform the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListAggregatedUtterances.html\&quot;&gt;ListAggregatedUtterances&lt;/a&gt; operation, which provides access to utterance-related analytics. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/monitoring-utterances.html\&quot;&gt;Viewing utterance statistics&lt;/a&gt; for the IAM policy to apply to the IAM role.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Retrieves a list of metadata for individual user utterances to your bot. The following fields are required:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;startDateTime&lt;/code&gt; and &lt;code&gt;endDateTime&lt;/code&gt; – Define a time range for which you want to retrieve results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Of the optional fields, you can organize the results in the following ways:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;filters&lt;/code&gt; field to filter the results and the &lt;code&gt;sortBy&lt;/code&gt; field to specify the values by which to sort the results.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;maxResults&lt;/code&gt; field to limit the number of results to return in a single response and the &lt;code&gt;nextToken&lt;/code&gt; field to return the next batch of results if the response does not return the full set of results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The identifier for the bot for which you want to retrieve utterance analytics.
    ListUtteranceAnalyticsDataRequest listUtteranceAnalyticsDataRequest = new ListUtteranceAnalyticsDataRequest(); // ListUtteranceAnalyticsDataRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListUtteranceAnalyticsDataResponse result = apiInstance.listUtteranceAnalyticsData(botId, listUtteranceAnalyticsDataRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listUtteranceAnalyticsData");
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
| **botId** | **String**| The identifier for the bot for which you want to retrieve utterance analytics. | |
| **listUtteranceAnalyticsDataRequest** | [**ListUtteranceAnalyticsDataRequest**](ListUtteranceAnalyticsDataRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListUtteranceAnalyticsDataResponse**](ListUtteranceAnalyticsDataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ValidationException |  -  |
| **482** | PreconditionFailedException |  -  |
| **483** | ServiceQuotaExceededException |  -  |
| **484** | InternalServerException |  -  |

<a id="listUtteranceMetrics"></a>
# **listUtteranceMetrics**
> ListUtteranceMetricsResponse listUtteranceMetrics(botId, listUtteranceMetricsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken)



&lt;note&gt; &lt;p&gt;To use this API operation, your IAM role must have permissions to perform the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListAggregatedUtterances.html\&quot;&gt;ListAggregatedUtterances&lt;/a&gt; operation, which provides access to utterance-related analytics. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/monitoring-utterances.html\&quot;&gt;Viewing utterance statistics&lt;/a&gt; for the IAM policy to apply to the IAM role.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Retrieves summary metrics for the utterances in your bot. The following fields are required:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;metrics&lt;/code&gt; – A list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsUtteranceMetric.html\&quot;&gt;AnalyticsUtteranceMetric&lt;/a&gt; objects. In each object, use the &lt;code&gt;name&lt;/code&gt; field to specify the metric to calculate, the &lt;code&gt;statistic&lt;/code&gt; field to specify whether to calculate the &lt;code&gt;Sum&lt;/code&gt;, &lt;code&gt;Average&lt;/code&gt;, or &lt;code&gt;Max&lt;/code&gt; number, and the &lt;code&gt;order&lt;/code&gt; field to specify whether to sort the results in &lt;code&gt;Ascending&lt;/code&gt; or &lt;code&gt;Descending&lt;/code&gt; order.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;startDateTime&lt;/code&gt; and &lt;code&gt;endDateTime&lt;/code&gt; – Define a time range for which you want to retrieve results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Of the optional fields, you can organize the results in the following ways:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;filters&lt;/code&gt; field to filter the results, the &lt;code&gt;groupBy&lt;/code&gt; field to specify categories by which to group the results, and the &lt;code&gt;binBy&lt;/code&gt; field to specify time intervals by which to group the results.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;maxResults&lt;/code&gt; field to limit the number of results to return in a single response and the &lt;code&gt;nextToken&lt;/code&gt; field to return the next batch of results if the response does not return the full set of results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Note that an &lt;code&gt;order&lt;/code&gt; field exists in both &lt;code&gt;binBy&lt;/code&gt; and &lt;code&gt;metrics&lt;/code&gt;. Currently, you can specify it in either field, but not in both.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The identifier for the bot for which you want to retrieve utterance metrics.
    ListUtteranceMetricsRequest listUtteranceMetricsRequest = new ListUtteranceMetricsRequest(); // ListUtteranceMetricsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String maxResults = "maxResults_example"; // String | Pagination limit
    String nextToken = "nextToken_example"; // String | Pagination token
    try {
      ListUtteranceMetricsResponse result = apiInstance.listUtteranceMetrics(botId, listUtteranceMetricsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listUtteranceMetrics");
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
| **botId** | **String**| The identifier for the bot for which you want to retrieve utterance metrics. | |
| **listUtteranceMetricsRequest** | [**ListUtteranceMetricsRequest**](ListUtteranceMetricsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **String**| Pagination limit | [optional] |
| **nextToken** | **String**| Pagination token | [optional] |

### Return type

[**ListUtteranceMetricsResponse**](ListUtteranceMetricsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ValidationException |  -  |
| **482** | PreconditionFailedException |  -  |
| **483** | ServiceQuotaExceededException |  -  |
| **484** | InternalServerException |  -  |

<a id="searchAssociatedTranscripts"></a>
# **searchAssociatedTranscripts**
> SearchAssociatedTranscriptsResponse searchAssociatedTranscripts(botId, botVersion, localeId, botRecommendationId, searchAssociatedTranscriptsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Search for associated transcripts that meet the specified criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The unique identifier of the bot associated with the transcripts that you are searching.
    String botVersion = "botVersion_example"; // String | The version of the bot containing the transcripts that you are searching.
    String localeId = "localeId_example"; // String | The identifier of the language and locale of the transcripts to search. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a> 
    String botRecommendationId = "botRecommendationId_example"; // String | The unique identifier of the bot recommendation associated with the transcripts to search.
    SearchAssociatedTranscriptsRequest searchAssociatedTranscriptsRequest = new SearchAssociatedTranscriptsRequest(); // SearchAssociatedTranscriptsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      SearchAssociatedTranscriptsResponse result = apiInstance.searchAssociatedTranscripts(botId, botVersion, localeId, botRecommendationId, searchAssociatedTranscriptsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#searchAssociatedTranscripts");
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
| **botId** | **String**| The unique identifier of the bot associated with the transcripts that you are searching. | |
| **botVersion** | **String**| The version of the bot containing the transcripts that you are searching. | |
| **localeId** | **String**| The identifier of the language and locale of the transcripts to search. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;  | |
| **botRecommendationId** | **String**| The unique identifier of the bot recommendation associated with the transcripts to search. | |
| **searchAssociatedTranscriptsRequest** | [**SearchAssociatedTranscriptsRequest**](SearchAssociatedTranscriptsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**SearchAssociatedTranscriptsResponse**](SearchAssociatedTranscriptsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | InternalServerException |  -  |
| **484** | ResourceNotFoundException |  -  |

<a id="startBotRecommendation"></a>
# **startBotRecommendation**
> StartBotRecommendationResponse startBotRecommendation(botId, botVersion, localeId, startBotRecommendationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Use this to provide your transcript data, and to start the bot recommendation process.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The unique identifier of the bot containing the bot recommendation.
    String botVersion = "botVersion_example"; // String | The version of the bot containing the bot recommendation.
    String localeId = "localeId_example"; // String | The identifier of the language and locale of the bot recommendation to start. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a> 
    StartBotRecommendationRequest startBotRecommendationRequest = new StartBotRecommendationRequest(); // StartBotRecommendationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StartBotRecommendationResponse result = apiInstance.startBotRecommendation(botId, botVersion, localeId, startBotRecommendationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startBotRecommendation");
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
| **botId** | **String**| The unique identifier of the bot containing the bot recommendation. | |
| **botVersion** | **String**| The version of the bot containing the bot recommendation. | |
| **localeId** | **String**| The identifier of the language and locale of the bot recommendation to start. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;  | |
| **startBotRecommendationRequest** | [**StartBotRecommendationRequest**](StartBotRecommendationRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StartBotRecommendationResponse**](StartBotRecommendationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ConflictException |  -  |
| **485** | PreconditionFailedException |  -  |
| **486** | ConflictException |  -  |
| **487** | InternalServerException |  -  |

<a id="startImport"></a>
# **startImport**
> StartImportResponse startImport(startImportRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Starts importing a bot, bot locale, or custom vocabulary from a zip archive that you uploaded to an S3 bucket.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    StartImportRequest startImportRequest = new StartImportRequest(); // StartImportRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StartImportResponse result = apiInstance.startImport(startImportRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startImport");
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
| **startImportRequest** | [**StartImportRequest**](StartImportRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StartImportResponse**](StartImportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ConflictException |  -  |
| **485** | InternalServerException |  -  |

<a id="startTestExecution"></a>
# **startTestExecution**
> StartTestExecutionResponse startTestExecution(testSetId, startTestExecutionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



The action to start test set execution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String testSetId = "testSetId_example"; // String | The test set Id for the test set execution.
    StartTestExecutionRequest startTestExecutionRequest = new StartTestExecutionRequest(); // StartTestExecutionRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StartTestExecutionResponse result = apiInstance.startTestExecution(testSetId, startTestExecutionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startTestExecution");
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
| **testSetId** | **String**| The test set Id for the test set execution. | |
| **startTestExecutionRequest** | [**StartTestExecutionRequest**](StartTestExecutionRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StartTestExecutionResponse**](StartTestExecutionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ValidationException |  -  |
| **484** | ConflictException |  -  |
| **485** | InternalServerException |  -  |

<a id="startTestSetGeneration"></a>
# **startTestSetGeneration**
> StartTestSetGenerationResponse startTestSetGeneration(startTestSetGenerationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



The action to start the generation of test set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    StartTestSetGenerationRequest startTestSetGenerationRequest = new StartTestSetGenerationRequest(); // StartTestSetGenerationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StartTestSetGenerationResponse result = apiInstance.startTestSetGeneration(startTestSetGenerationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startTestSetGeneration");
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
| **startTestSetGenerationRequest** | [**StartTestSetGenerationRequest**](StartTestSetGenerationRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StartTestSetGenerationResponse**](StartTestSetGenerationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ConflictException |  -  |
| **484** | ResourceNotFoundException |  -  |
| **485** | InternalServerException |  -  |

<a id="stopBotRecommendation"></a>
# **stopBotRecommendation**
> StopBotRecommendationResponse stopBotRecommendation(botId, botVersion, localeId, botRecommendationId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Stop an already running Bot Recommendation request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The unique identifier of the bot containing the bot recommendation to be stopped.
    String botVersion = "botVersion_example"; // String | The version of the bot containing the bot recommendation.
    String localeId = "localeId_example"; // String | The identifier of the language and locale of the bot recommendation to stop. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a> 
    String botRecommendationId = "botRecommendationId_example"; // String | The unique identifier of the bot recommendation to be stopped.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StopBotRecommendationResponse result = apiInstance.stopBotRecommendation(botId, botVersion, localeId, botRecommendationId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#stopBotRecommendation");
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
| **botId** | **String**| The unique identifier of the bot containing the bot recommendation to be stopped. | |
| **botVersion** | **String**| The version of the bot containing the bot recommendation. | |
| **localeId** | **String**| The identifier of the language and locale of the bot recommendation to stop. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;  | |
| **botRecommendationId** | **String**| The unique identifier of the bot recommendation to be stopped. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StopBotRecommendationResponse**](StopBotRecommendationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ConflictException |  -  |
| **485** | PreconditionFailedException |  -  |
| **486** | ConflictException |  -  |
| **487** | InternalServerException |  -  |

<a id="tagResource"></a>
# **tagResource**
> Object tagResource(resourceARN, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Adds the specified tags to the specified resource. If a tag key already exists, the existing value is replaced with the new value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceARN = "resourceARN_example"; // String | The Amazon Resource Name (ARN) of the bot, bot alias, or bot channel to tag.
    TagResourceRequest tagResourceRequest = new TagResourceRequest(); // TagResourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.tagResource(resourceARN, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tagResource");
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
| **resourceARN** | **String**| The Amazon Resource Name (ARN) of the bot, bot alias, or bot channel to tag. | |
| **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ThrottlingException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ValidationException |  -  |

<a id="untagResource"></a>
# **untagResource**
> Object untagResource(resourceARN, tagKeys, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Removes tags from a bot, bot alias, or bot channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceARN = "resourceARN_example"; // String | The Amazon Resource Name (ARN) of the resource to remove the tags from.
    List<String> tagKeys = Arrays.asList(); // List<String> | A list of tag keys to remove from the resource. If a tag key does not exist on the resource, it is ignored.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.untagResource(resourceARN, tagKeys, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#untagResource");
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
| **resourceARN** | **String**| The Amazon Resource Name (ARN) of the resource to remove the tags from. | |
| **tagKeys** | [**List&lt;String&gt;**](String.md)| A list of tag keys to remove from the resource. If a tag key does not exist on the resource, it is ignored. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ThrottlingException |  -  |
| **482** | ResourceNotFoundException |  -  |
| **483** | ValidationException |  -  |

<a id="updateBot"></a>
# **updateBot**
> UpdateBotResponse updateBot(botId, updateBotRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates the configuration of an existing bot. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The unique identifier of the bot to update. This identifier is returned by the <a href=\"https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html\">CreateBot</a> operation.
    UpdateBotRequest updateBotRequest = new UpdateBotRequest(); // UpdateBotRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateBotResponse result = apiInstance.updateBot(botId, updateBotRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateBot");
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
| **botId** | **String**| The unique identifier of the bot to update. This identifier is returned by the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html\&quot;&gt;CreateBot&lt;/a&gt; operation. | |
| **updateBotRequest** | [**UpdateBotRequest**](UpdateBotRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateBotResponse**](UpdateBotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | PreconditionFailedException |  -  |
| **484** | ConflictException |  -  |
| **485** | InternalServerException |  -  |

<a id="updateBotAlias"></a>
# **updateBotAlias**
> UpdateBotAliasResponse updateBotAlias(botAliasId, botId, updateBotAliasRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates the configuration of an existing bot alias.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botAliasId = "botAliasId_example"; // String | The unique identifier of the bot alias.
    String botId = "botId_example"; // String | The identifier of the bot with the updated alias.
    UpdateBotAliasRequest updateBotAliasRequest = new UpdateBotAliasRequest(); // UpdateBotAliasRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateBotAliasResponse result = apiInstance.updateBotAlias(botAliasId, botId, updateBotAliasRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateBotAlias");
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
| **botAliasId** | **String**| The unique identifier of the bot alias. | |
| **botId** | **String**| The identifier of the bot with the updated alias. | |
| **updateBotAliasRequest** | [**UpdateBotAliasRequest**](UpdateBotAliasRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateBotAliasResponse**](UpdateBotAliasResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | PreconditionFailedException |  -  |
| **484** | ConflictException |  -  |
| **485** | InternalServerException |  -  |

<a id="updateBotLocale"></a>
# **updateBotLocale**
> UpdateBotLocaleResponse updateBotLocale(botId, botVersion, localeId, updateBotLocaleRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates the settings that a bot has for a specific locale.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The unique identifier of the bot that contains the locale.
    String botVersion = "botVersion_example"; // String | The version of the bot that contains the locale to be updated. The version can only be the <code>DRAFT</code> version.
    String localeId = "localeId_example"; // String | The identifier of the language and locale to update. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
    UpdateBotLocaleRequest updateBotLocaleRequest = new UpdateBotLocaleRequest(); // UpdateBotLocaleRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateBotLocaleResponse result = apiInstance.updateBotLocale(botId, botVersion, localeId, updateBotLocaleRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateBotLocale");
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
| **botId** | **String**| The unique identifier of the bot that contains the locale. | |
| **botVersion** | **String**| The version of the bot that contains the locale to be updated. The version can only be the &lt;code&gt;DRAFT&lt;/code&gt; version. | |
| **localeId** | **String**| The identifier of the language and locale to update. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | |
| **updateBotLocaleRequest** | [**UpdateBotLocaleRequest**](UpdateBotLocaleRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateBotLocaleResponse**](UpdateBotLocaleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | PreconditionFailedException |  -  |
| **484** | ConflictException |  -  |
| **485** | InternalServerException |  -  |

<a id="updateBotRecommendation"></a>
# **updateBotRecommendation**
> UpdateBotRecommendationResponse updateBotRecommendation(botId, botVersion, localeId, botRecommendationId, updateBotRecommendationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates an existing bot recommendation request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botId = "botId_example"; // String | The unique identifier of the bot containing the bot recommendation to be updated.
    String botVersion = "botVersion_example"; // String | The version of the bot containing the bot recommendation to be updated.
    String localeId = "localeId_example"; // String | The identifier of the language and locale of the bot recommendation to update. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a> 
    String botRecommendationId = "botRecommendationId_example"; // String | The unique identifier of the bot recommendation to be updated.
    UpdateBotRecommendationRequest updateBotRecommendationRequest = new UpdateBotRecommendationRequest(); // UpdateBotRecommendationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateBotRecommendationResponse result = apiInstance.updateBotRecommendation(botId, botVersion, localeId, botRecommendationId, updateBotRecommendationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateBotRecommendation");
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
| **botId** | **String**| The unique identifier of the bot containing the bot recommendation to be updated. | |
| **botVersion** | **String**| The version of the bot containing the bot recommendation to be updated. | |
| **localeId** | **String**| The identifier of the language and locale of the bot recommendation to update. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;  | |
| **botRecommendationId** | **String**| The unique identifier of the bot recommendation to be updated. | |
| **updateBotRecommendationRequest** | [**UpdateBotRecommendationRequest**](UpdateBotRecommendationRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateBotRecommendationResponse**](UpdateBotRecommendationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ConflictException |  -  |
| **485** | PreconditionFailedException |  -  |
| **486** | ConflictException |  -  |
| **487** | InternalServerException |  -  |

<a id="updateExport"></a>
# **updateExport**
> UpdateExportResponse updateExport(exportId, updateExportRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates the password used to protect an export zip archive.&lt;/p&gt; &lt;p&gt;The password is not required. If you don&#39;t supply a password, Amazon Lex generates a zip file that is not protected by a password. This is the archive that is available at the pre-signed S3 URL provided by the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeExport.html\&quot;&gt;DescribeExport&lt;/a&gt; operation.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String exportId = "exportId_example"; // String | The unique identifier Amazon Lex assigned to the export.
    UpdateExportRequest updateExportRequest = new UpdateExportRequest(); // UpdateExportRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateExportResponse result = apiInstance.updateExport(exportId, updateExportRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateExport");
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
| **exportId** | **String**| The unique identifier Amazon Lex assigned to the export. | |
| **updateExportRequest** | [**UpdateExportRequest**](UpdateExportRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateExportResponse**](UpdateExportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | ResourceNotFoundException |  -  |
| **484** | ConflictException |  -  |
| **485** | InternalServerException |  -  |

<a id="updateIntent"></a>
# **updateIntent**
> UpdateIntentResponse updateIntent(intentId, botId, botVersion, localeId, updateIntentRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates the settings for an intent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String intentId = "intentId_example"; // String | The unique identifier of the intent to update.
    String botId = "botId_example"; // String | The identifier of the bot that contains the intent.
    String botVersion = "botVersion_example"; // String | The version of the bot that contains the intent. Must be <code>DRAFT</code>.
    String localeId = "localeId_example"; // String | The identifier of the language and locale where this intent is used. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
    UpdateIntentRequest updateIntentRequest = new UpdateIntentRequest(); // UpdateIntentRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateIntentResponse result = apiInstance.updateIntent(intentId, botId, botVersion, localeId, updateIntentRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateIntent");
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
| **intentId** | **String**| The unique identifier of the intent to update. | |
| **botId** | **String**| The identifier of the bot that contains the intent. | |
| **botVersion** | **String**| The version of the bot that contains the intent. Must be &lt;code&gt;DRAFT&lt;/code&gt;. | |
| **localeId** | **String**| The identifier of the language and locale where this intent is used. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | |
| **updateIntentRequest** | [**UpdateIntentRequest**](UpdateIntentRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateIntentResponse**](UpdateIntentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | PreconditionFailedException |  -  |
| **484** | ConflictException |  -  |
| **485** | InternalServerException |  -  |

<a id="updateResourcePolicy"></a>
# **updateResourcePolicy**
> UpdateResourcePolicyResponse updateResourcePolicy(resourceArn, updateResourcePolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, expectedRevisionId)



Replaces the existing resource policy for a bot or bot alias with a new one. If the policy doesn&#39;t exist, Amazon Lex returns an exception.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.
    UpdateResourcePolicyRequest updateResourcePolicyRequest = new UpdateResourcePolicyRequest(); // UpdateResourcePolicyRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String expectedRevisionId = "expectedRevisionId_example"; // String | <p>The identifier of the revision of the policy to update. If this revision ID doesn't match the current revision ID, Amazon Lex throws an exception.</p> <p>If you don't specify a revision, Amazon Lex overwrites the contents of the policy with the new values.</p>
    try {
      UpdateResourcePolicyResponse result = apiInstance.updateResourcePolicy(resourceArn, updateResourcePolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, expectedRevisionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateResourcePolicy");
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
| **resourceArn** | **String**| The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to. | |
| **updateResourcePolicyRequest** | [**UpdateResourcePolicyRequest**](UpdateResourcePolicyRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **expectedRevisionId** | **String**| &lt;p&gt;The identifier of the revision of the policy to update. If this revision ID doesn&#39;t match the current revision ID, Amazon Lex throws an exception.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a revision, Amazon Lex overwrites the contents of the policy with the new values.&lt;/p&gt; | [optional] |

### Return type

[**UpdateResourcePolicyResponse**](UpdateResourcePolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | PreconditionFailedException |  -  |
| **483** | ValidationException |  -  |
| **484** | InternalServerException |  -  |
| **485** | ThrottlingException |  -  |

<a id="updateSlot"></a>
# **updateSlot**
> UpdateSlotResponse updateSlot(slotId, botId, botVersion, localeId, intentId, updateSlotRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates the settings for a slot.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String slotId = "slotId_example"; // String | The unique identifier for the slot to update.
    String botId = "botId_example"; // String | The unique identifier of the bot that contains the slot.
    String botVersion = "botVersion_example"; // String | The version of the bot that contains the slot. Must always be <code>DRAFT</code>.
    String localeId = "localeId_example"; // String | The identifier of the language and locale that contains the slot. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
    String intentId = "intentId_example"; // String | The identifier of the intent that contains the slot.
    UpdateSlotRequest updateSlotRequest = new UpdateSlotRequest(); // UpdateSlotRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateSlotResponse result = apiInstance.updateSlot(slotId, botId, botVersion, localeId, intentId, updateSlotRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateSlot");
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
| **slotId** | **String**| The unique identifier for the slot to update. | |
| **botId** | **String**| The unique identifier of the bot that contains the slot. | |
| **botVersion** | **String**| The version of the bot that contains the slot. Must always be &lt;code&gt;DRAFT&lt;/code&gt;. | |
| **localeId** | **String**| The identifier of the language and locale that contains the slot. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | |
| **intentId** | **String**| The identifier of the intent that contains the slot. | |
| **updateSlotRequest** | [**UpdateSlotRequest**](UpdateSlotRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateSlotResponse**](UpdateSlotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | PreconditionFailedException |  -  |
| **484** | ConflictException |  -  |
| **485** | InternalServerException |  -  |

<a id="updateSlotType"></a>
# **updateSlotType**
> UpdateSlotTypeResponse updateSlotType(slotTypeId, botId, botVersion, localeId, updateSlotTypeRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates the configuration of an existing slot type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String slotTypeId = "slotTypeId_example"; // String | The unique identifier of the slot type to update.
    String botId = "botId_example"; // String | The identifier of the bot that contains the slot type.
    String botVersion = "botVersion_example"; // String | The version of the bot that contains the slot type. Must be <code>DRAFT</code>.
    String localeId = "localeId_example"; // String | The identifier of the language and locale that contains the slot type. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.
    UpdateSlotTypeRequest updateSlotTypeRequest = new UpdateSlotTypeRequest(); // UpdateSlotTypeRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateSlotTypeResponse result = apiInstance.updateSlotType(slotTypeId, botId, botVersion, localeId, updateSlotTypeRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateSlotType");
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
| **slotTypeId** | **String**| The unique identifier of the slot type to update. | |
| **botId** | **String**| The identifier of the bot that contains the slot type. | |
| **botVersion** | **String**| The version of the bot that contains the slot type. Must be &lt;code&gt;DRAFT&lt;/code&gt;. | |
| **localeId** | **String**| The identifier of the language and locale that contains the slot type. The string must match one of the supported locales. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | |
| **updateSlotTypeRequest** | [**UpdateSlotTypeRequest**](UpdateSlotTypeRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateSlotTypeResponse**](UpdateSlotTypeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | PreconditionFailedException |  -  |
| **484** | ConflictException |  -  |
| **485** | InternalServerException |  -  |

<a id="updateTestSet"></a>
# **updateTestSet**
> UpdateTestSetResponse updateTestSet(testSetId, updateTestSetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



The action to update the test set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://models-v2-lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String testSetId = "testSetId_example"; // String | The test set Id for which update test operation to be performed.
    UpdateTestSetRequest updateTestSetRequest = new UpdateTestSetRequest(); // UpdateTestSetRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateTestSetResponse result = apiInstance.updateTestSet(testSetId, updateTestSetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateTestSet");
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
| **testSetId** | **String**| The test set Id for which update test operation to be performed. | |
| **updateTestSetRequest** | [**UpdateTestSetRequest**](UpdateTestSetRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateTestSetResponse**](UpdateTestSetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ThrottlingException |  -  |
| **481** | ServiceQuotaExceededException |  -  |
| **482** | ValidationException |  -  |
| **483** | PreconditionFailedException |  -  |
| **484** | ConflictException |  -  |
| **485** | InternalServerException |  -  |

