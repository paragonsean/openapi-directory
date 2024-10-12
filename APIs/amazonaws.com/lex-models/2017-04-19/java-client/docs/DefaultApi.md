# DefaultApi

All URIs are relative to *http://models.lex.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createBotVersion**](DefaultApi.md#createBotVersion) | **POST** /bots/{name}/versions |  |
| [**createIntentVersion**](DefaultApi.md#createIntentVersion) | **POST** /intents/{name}/versions |  |
| [**createSlotTypeVersion**](DefaultApi.md#createSlotTypeVersion) | **POST** /slottypes/{name}/versions |  |
| [**deleteBot**](DefaultApi.md#deleteBot) | **DELETE** /bots/{name} |  |
| [**deleteBotAlias**](DefaultApi.md#deleteBotAlias) | **DELETE** /bots/{botName}/aliases/{name} |  |
| [**deleteBotChannelAssociation**](DefaultApi.md#deleteBotChannelAssociation) | **DELETE** /bots/{botName}/aliases/{aliasName}/channels/{name} |  |
| [**deleteBotVersion**](DefaultApi.md#deleteBotVersion) | **DELETE** /bots/{name}/versions/{version} |  |
| [**deleteIntent**](DefaultApi.md#deleteIntent) | **DELETE** /intents/{name} |  |
| [**deleteIntentVersion**](DefaultApi.md#deleteIntentVersion) | **DELETE** /intents/{name}/versions/{version} |  |
| [**deleteSlotType**](DefaultApi.md#deleteSlotType) | **DELETE** /slottypes/{name} |  |
| [**deleteSlotTypeVersion**](DefaultApi.md#deleteSlotTypeVersion) | **DELETE** /slottypes/{name}/version/{version} |  |
| [**deleteUtterances**](DefaultApi.md#deleteUtterances) | **DELETE** /bots/{botName}/utterances/{userId} |  |
| [**getBot**](DefaultApi.md#getBot) | **GET** /bots/{name}/versions/{versionoralias} |  |
| [**getBotAlias**](DefaultApi.md#getBotAlias) | **GET** /bots/{botName}/aliases/{name} |  |
| [**getBotAliases**](DefaultApi.md#getBotAliases) | **GET** /bots/{botName}/aliases/ |  |
| [**getBotChannelAssociation**](DefaultApi.md#getBotChannelAssociation) | **GET** /bots/{botName}/aliases/{aliasName}/channels/{name} |  |
| [**getBotChannelAssociations**](DefaultApi.md#getBotChannelAssociations) | **GET** /bots/{botName}/aliases/{aliasName}/channels/ |  |
| [**getBotVersions**](DefaultApi.md#getBotVersions) | **GET** /bots/{name}/versions/ |  |
| [**getBots**](DefaultApi.md#getBots) | **GET** /bots/ |  |
| [**getBuiltinIntent**](DefaultApi.md#getBuiltinIntent) | **GET** /builtins/intents/{signature} |  |
| [**getBuiltinIntents**](DefaultApi.md#getBuiltinIntents) | **GET** /builtins/intents/ |  |
| [**getBuiltinSlotTypes**](DefaultApi.md#getBuiltinSlotTypes) | **GET** /builtins/slottypes/ |  |
| [**getExport**](DefaultApi.md#getExport) | **GET** /exports/#name&amp;version&amp;resourceType&amp;exportType |  |
| [**getImport**](DefaultApi.md#getImport) | **GET** /imports/{importId} |  |
| [**getIntent**](DefaultApi.md#getIntent) | **GET** /intents/{name}/versions/{version} |  |
| [**getIntentVersions**](DefaultApi.md#getIntentVersions) | **GET** /intents/{name}/versions/ |  |
| [**getIntents**](DefaultApi.md#getIntents) | **GET** /intents/ |  |
| [**getMigration**](DefaultApi.md#getMigration) | **GET** /migrations/{migrationId} |  |
| [**getMigrations**](DefaultApi.md#getMigrations) | **GET** /migrations |  |
| [**getSlotType**](DefaultApi.md#getSlotType) | **GET** /slottypes/{name}/versions/{version} |  |
| [**getSlotTypeVersions**](DefaultApi.md#getSlotTypeVersions) | **GET** /slottypes/{name}/versions/ |  |
| [**getSlotTypes**](DefaultApi.md#getSlotTypes) | **GET** /slottypes/ |  |
| [**getUtterancesView**](DefaultApi.md#getUtterancesView) | **GET** /bots/{botname}/utterances#view&#x3D;aggregation&amp;bot_versions&amp;status_type |  |
| [**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} |  |
| [**putBot**](DefaultApi.md#putBot) | **PUT** /bots/{name}/versions/$LATEST |  |
| [**putBotAlias**](DefaultApi.md#putBotAlias) | **PUT** /bots/{botName}/aliases/{name} |  |
| [**putIntent**](DefaultApi.md#putIntent) | **PUT** /intents/{name}/versions/$LATEST |  |
| [**putSlotType**](DefaultApi.md#putSlotType) | **PUT** /slottypes/{name}/versions/$LATEST |  |
| [**startImport**](DefaultApi.md#startImport) | **POST** /imports/ |  |
| [**startMigration**](DefaultApi.md#startMigration) | **POST** /migrations |  |
| [**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} |  |
| [**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys |  |


<a id="createBotVersion"></a>
# **createBotVersion**
> CreateBotVersionResponse createBotVersion(name, createBotVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a new version of the bot based on the &lt;code&gt;$LATEST&lt;/code&gt; version. If the &lt;code&gt;$LATEST&lt;/code&gt; version of this resource hasn&#39;t changed since you created the last version, Amazon Lex doesn&#39;t create a new version. It returns the last created version.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can update only the &lt;code&gt;$LATEST&lt;/code&gt; version of the bot. You can&#39;t update the numbered versions that you create with the &lt;code&gt;CreateBotVersion&lt;/code&gt; operation.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; When you create the first version of a bot, Amazon Lex sets the version to 1. Subsequent versions increment by 1. For more information, see &lt;a&gt;versioning-intro&lt;/a&gt;. &lt;/p&gt; &lt;p&gt; This operation requires permission for the &lt;code&gt;lex:CreateBotVersion&lt;/code&gt; action. &lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the bot that you want to create a new version of. The name is case sensitive. 
    CreateBotVersionRequest createBotVersionRequest = new CreateBotVersionRequest(); // CreateBotVersionRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateBotVersionResponse result = apiInstance.createBotVersion(name, createBotVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
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
| **name** | **String**| The name of the bot that you want to create a new version of. The name is case sensitive.  | |
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
| **201** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | ConflictException |  -  |
| **482** | LimitExceededException |  -  |
| **483** | InternalFailureException |  -  |
| **484** | BadRequestException |  -  |
| **485** | PreconditionFailedException |  -  |

<a id="createIntentVersion"></a>
# **createIntentVersion**
> CreateIntentVersionResponse createIntentVersion(name, createIntentVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a new version of an intent based on the &lt;code&gt;$LATEST&lt;/code&gt; version of the intent. If the &lt;code&gt;$LATEST&lt;/code&gt; version of this intent hasn&#39;t changed since you last updated it, Amazon Lex doesn&#39;t create a new version. It returns the last version you created.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can update only the &lt;code&gt;$LATEST&lt;/code&gt; version of the intent. You can&#39;t update the numbered versions that you create with the &lt;code&gt;CreateIntentVersion&lt;/code&gt; operation.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; When you create a version of an intent, Amazon Lex sets the version to 1. Subsequent versions increment by 1. For more information, see &lt;a&gt;versioning-intro&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;lex:CreateIntentVersion&lt;/code&gt; action. &lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the intent that you want to create a new version of. The name is case sensitive. 
    CreateIntentVersionRequest createIntentVersionRequest = new CreateIntentVersionRequest(); // CreateIntentVersionRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateIntentVersionResponse result = apiInstance.createIntentVersion(name, createIntentVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createIntentVersion");
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
| **name** | **String**| The name of the intent that you want to create a new version of. The name is case sensitive.  | |
| **createIntentVersionRequest** | [**CreateIntentVersionRequest**](CreateIntentVersionRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateIntentVersionResponse**](CreateIntentVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | ConflictException |  -  |
| **482** | LimitExceededException |  -  |
| **483** | InternalFailureException |  -  |
| **484** | BadRequestException |  -  |
| **485** | PreconditionFailedException |  -  |

<a id="createSlotTypeVersion"></a>
# **createSlotTypeVersion**
> CreateSlotTypeVersionResponse createSlotTypeVersion(name, createSlotTypeVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a new version of a slot type based on the &lt;code&gt;$LATEST&lt;/code&gt; version of the specified slot type. If the &lt;code&gt;$LATEST&lt;/code&gt; version of this resource has not changed since the last version that you created, Amazon Lex doesn&#39;t create a new version. It returns the last version that you created. &lt;/p&gt; &lt;note&gt; &lt;p&gt;You can update only the &lt;code&gt;$LATEST&lt;/code&gt; version of a slot type. You can&#39;t update the numbered versions that you create with the &lt;code&gt;CreateSlotTypeVersion&lt;/code&gt; operation.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;When you create a version of a slot type, Amazon Lex sets the version to 1. Subsequent versions increment by 1. For more information, see &lt;a&gt;versioning-intro&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:CreateSlotTypeVersion&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the slot type that you want to create a new version for. The name is case sensitive. 
    CreateSlotTypeVersionRequest createSlotTypeVersionRequest = new CreateSlotTypeVersionRequest(); // CreateSlotTypeVersionRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateSlotTypeVersionResponse result = apiInstance.createSlotTypeVersion(name, createSlotTypeVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createSlotTypeVersion");
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
| **name** | **String**| The name of the slot type that you want to create a new version for. The name is case sensitive.  | |
| **createSlotTypeVersionRequest** | [**CreateSlotTypeVersionRequest**](CreateSlotTypeVersionRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateSlotTypeVersionResponse**](CreateSlotTypeVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | ConflictException |  -  |
| **482** | LimitExceededException |  -  |
| **483** | InternalFailureException |  -  |
| **484** | BadRequestException |  -  |
| **485** | PreconditionFailedException |  -  |

<a id="deleteBot"></a>
# **deleteBot**
> deleteBot(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes all versions of the bot, including the &lt;code&gt;$LATEST&lt;/code&gt; version. To delete a specific version of the bot, use the &lt;a&gt;DeleteBotVersion&lt;/a&gt; operation. The &lt;code&gt;DeleteBot&lt;/code&gt; operation doesn&#39;t immediately remove the bot schema. Instead, it is marked for deletion and removed later.&lt;/p&gt; &lt;p&gt;Amazon Lex stores utterances indefinitely for improving the ability of your bot to respond to user inputs. These utterances are not removed when the bot is deleted. To remove the utterances, use the &lt;a&gt;DeleteUtterances&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;If a bot has an alias, you can&#39;t delete it. Instead, the &lt;code&gt;DeleteBot&lt;/code&gt; operation returns a &lt;code&gt;ResourceInUseException&lt;/code&gt; exception that includes a reference to the alias that refers to the bot. To remove the reference to the bot, delete the alias. If you get the same exception again, delete the referring alias until the &lt;code&gt;DeleteBot&lt;/code&gt; operation is successful.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:DeleteBot&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the bot. The name is case sensitive. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteBot(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
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
| **name** | **String**| The name of the bot. The name is case sensitive.  | |
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
| **480** | NotFoundException |  -  |
| **481** | ConflictException |  -  |
| **482** | LimitExceededException |  -  |
| **483** | InternalFailureException |  -  |
| **484** | BadRequestException |  -  |
| **485** | ResourceInUseException |  -  |

<a id="deleteBotAlias"></a>
# **deleteBotAlias**
> deleteBotAlias(name, botName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes an alias for the specified bot. &lt;/p&gt; &lt;p&gt;You can&#39;t delete an alias that is used in the association between a bot and a messaging channel. If an alias is used in a channel association, the &lt;code&gt;DeleteBot&lt;/code&gt; operation returns a &lt;code&gt;ResourceInUseException&lt;/code&gt; exception that includes a reference to the channel association that refers to the bot. You can remove the reference to the alias by deleting the channel association. If you get the same exception again, delete the referring association until the &lt;code&gt;DeleteBotAlias&lt;/code&gt; operation is successful.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the alias to delete. The name is case sensitive. 
    String botName = "botName_example"; // String | The name of the bot that the alias points to.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteBotAlias(name, botName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
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
| **name** | **String**| The name of the alias to delete. The name is case sensitive.  | |
| **botName** | **String**| The name of the bot that the alias points to. | |
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
| **480** | NotFoundException |  -  |
| **481** | ConflictException |  -  |
| **482** | LimitExceededException |  -  |
| **483** | InternalFailureException |  -  |
| **484** | BadRequestException |  -  |
| **485** | ResourceInUseException |  -  |

<a id="deleteBotChannelAssociation"></a>
# **deleteBotChannelAssociation**
> deleteBotChannelAssociation(name, botName, aliasName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes the association between an Amazon Lex bot and a messaging platform.&lt;/p&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;lex:DeleteBotChannelAssociation&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the association. The name is case sensitive. 
    String botName = "botName_example"; // String | The name of the Amazon Lex bot.
    String aliasName = "aliasName_example"; // String | An alias that points to the specific version of the Amazon Lex bot to which this association is being made.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteBotChannelAssociation(name, botName, aliasName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteBotChannelAssociation");
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
| **name** | **String**| The name of the association. The name is case sensitive.  | |
| **botName** | **String**| The name of the Amazon Lex bot. | |
| **aliasName** | **String**| An alias that points to the specific version of the Amazon Lex bot to which this association is being made. | |
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
| **480** | NotFoundException |  -  |
| **481** | ConflictException |  -  |
| **482** | LimitExceededException |  -  |
| **483** | InternalFailureException |  -  |
| **484** | BadRequestException |  -  |

<a id="deleteBotVersion"></a>
# **deleteBotVersion**
> deleteBotVersion(name, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes a specific version of a bot. To delete all versions of a bot, use the &lt;a&gt;DeleteBot&lt;/a&gt; operation. &lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:DeleteBotVersion&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the bot.
    String version = "version_example"; // String | The version of the bot to delete. You cannot delete the <code>$LATEST</code> version of the bot. To delete the <code>$LATEST</code> version, use the <a>DeleteBot</a> operation.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteBotVersion(name, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
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
| **name** | **String**| The name of the bot. | |
| **version** | **String**| The version of the bot to delete. You cannot delete the &lt;code&gt;$LATEST&lt;/code&gt; version of the bot. To delete the &lt;code&gt;$LATEST&lt;/code&gt; version, use the &lt;a&gt;DeleteBot&lt;/a&gt; operation. | |
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
| **480** | NotFoundException |  -  |
| **481** | ConflictException |  -  |
| **482** | LimitExceededException |  -  |
| **483** | InternalFailureException |  -  |
| **484** | BadRequestException |  -  |
| **485** | ResourceInUseException |  -  |

<a id="deleteIntent"></a>
# **deleteIntent**
> deleteIntent(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes all versions of the intent, including the &lt;code&gt;$LATEST&lt;/code&gt; version. To delete a specific version of the intent, use the &lt;a&gt;DeleteIntentVersion&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt; You can delete a version of an intent only if it is not referenced. To delete an intent that is referred to in one or more bots (see &lt;a&gt;how-it-works&lt;/a&gt;), you must remove those references first. &lt;/p&gt; &lt;note&gt; &lt;p&gt; If you get the &lt;code&gt;ResourceInUseException&lt;/code&gt; exception, it provides an example reference that shows where the intent is referenced. To remove the reference to the intent, either update the bot or delete it. If you get the same exception when you attempt to delete the intent again, repeat until the intent has no references and the call to &lt;code&gt;DeleteIntent&lt;/code&gt; is successful. &lt;/p&gt; &lt;/note&gt; &lt;p&gt; This operation requires permission for the &lt;code&gt;lex:DeleteIntent&lt;/code&gt; action. &lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the intent. The name is case sensitive. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteIntent(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
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
| **name** | **String**| The name of the intent. The name is case sensitive.  | |
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
| **480** | NotFoundException |  -  |
| **481** | ConflictException |  -  |
| **482** | LimitExceededException |  -  |
| **483** | InternalFailureException |  -  |
| **484** | BadRequestException |  -  |
| **485** | ResourceInUseException |  -  |

<a id="deleteIntentVersion"></a>
# **deleteIntentVersion**
> deleteIntentVersion(name, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes a specific version of an intent. To delete all versions of a intent, use the &lt;a&gt;DeleteIntent&lt;/a&gt; operation. &lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:DeleteIntentVersion&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the intent.
    String version = "version_example"; // String | The version of the intent to delete. You cannot delete the <code>$LATEST</code> version of the intent. To delete the <code>$LATEST</code> version, use the <a>DeleteIntent</a> operation.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteIntentVersion(name, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteIntentVersion");
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
| **name** | **String**| The name of the intent. | |
| **version** | **String**| The version of the intent to delete. You cannot delete the &lt;code&gt;$LATEST&lt;/code&gt; version of the intent. To delete the &lt;code&gt;$LATEST&lt;/code&gt; version, use the &lt;a&gt;DeleteIntent&lt;/a&gt; operation. | |
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
| **480** | NotFoundException |  -  |
| **481** | ConflictException |  -  |
| **482** | LimitExceededException |  -  |
| **483** | InternalFailureException |  -  |
| **484** | BadRequestException |  -  |
| **485** | ResourceInUseException |  -  |

<a id="deleteSlotType"></a>
# **deleteSlotType**
> deleteSlotType(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes all versions of the slot type, including the &lt;code&gt;$LATEST&lt;/code&gt; version. To delete a specific version of the slot type, use the &lt;a&gt;DeleteSlotTypeVersion&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt; You can delete a version of a slot type only if it is not referenced. To delete a slot type that is referred to in one or more intents, you must remove those references first. &lt;/p&gt; &lt;note&gt; &lt;p&gt; If you get the &lt;code&gt;ResourceInUseException&lt;/code&gt; exception, the exception provides an example reference that shows the intent where the slot type is referenced. To remove the reference to the slot type, either update the intent or delete it. If you get the same exception when you attempt to delete the slot type again, repeat until the slot type has no references and the &lt;code&gt;DeleteSlotType&lt;/code&gt; call is successful. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;lex:DeleteSlotType&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the slot type. The name is case sensitive. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteSlotType(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
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
| **name** | **String**| The name of the slot type. The name is case sensitive.  | |
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
| **480** | NotFoundException |  -  |
| **481** | ConflictException |  -  |
| **482** | LimitExceededException |  -  |
| **483** | InternalFailureException |  -  |
| **484** | BadRequestException |  -  |
| **485** | ResourceInUseException |  -  |

<a id="deleteSlotTypeVersion"></a>
# **deleteSlotTypeVersion**
> deleteSlotTypeVersion(name, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes a specific version of a slot type. To delete all versions of a slot type, use the &lt;a&gt;DeleteSlotType&lt;/a&gt; operation. &lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:DeleteSlotTypeVersion&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the slot type.
    String version = "version_example"; // String | The version of the slot type to delete. You cannot delete the <code>$LATEST</code> version of the slot type. To delete the <code>$LATEST</code> version, use the <a>DeleteSlotType</a> operation.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteSlotTypeVersion(name, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteSlotTypeVersion");
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
| **name** | **String**| The name of the slot type. | |
| **version** | **String**| The version of the slot type to delete. You cannot delete the &lt;code&gt;$LATEST&lt;/code&gt; version of the slot type. To delete the &lt;code&gt;$LATEST&lt;/code&gt; version, use the &lt;a&gt;DeleteSlotType&lt;/a&gt; operation. | |
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
| **480** | NotFoundException |  -  |
| **481** | ConflictException |  -  |
| **482** | LimitExceededException |  -  |
| **483** | InternalFailureException |  -  |
| **484** | BadRequestException |  -  |
| **485** | ResourceInUseException |  -  |

<a id="deleteUtterances"></a>
# **deleteUtterances**
> deleteUtterances(botName, userId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes stored utterances.&lt;/p&gt; &lt;p&gt;Amazon Lex stores the utterances that users send to your bot. Utterances are stored for 15 days for use with the &lt;a&gt;GetUtterancesView&lt;/a&gt; operation, and then stored indefinitely for use in improving the ability of your bot to respond to user input.&lt;/p&gt; &lt;p&gt;Use the &lt;code&gt;DeleteUtterances&lt;/code&gt; operation to manually delete stored utterances for a specific user. When you use the &lt;code&gt;DeleteUtterances&lt;/code&gt; operation, utterances stored for improving your bot&#39;s ability to respond to user input are deleted immediately. Utterances stored for use with the &lt;code&gt;GetUtterancesView&lt;/code&gt; operation are deleted after 15 days.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:DeleteUtterances&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botName = "botName_example"; // String | The name of the bot that stored the utterances.
    String userId = "userId_example"; // String |  The unique identifier for the user that made the utterances. This is the user ID that was sent in the <a href=\"http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostContent.html\">PostContent</a> or <a href=\"http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html\">PostText</a> operation request that contained the utterance.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteUtterances(botName, userId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
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
| **botName** | **String**| The name of the bot that stored the utterances. | |
| **userId** | **String**|  The unique identifier for the user that made the utterances. This is the user ID that was sent in the &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostContent.html\&quot;&gt;PostContent&lt;/a&gt; or &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html\&quot;&gt;PostText&lt;/a&gt; operation request that contained the utterance. | |
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
| **480** | NotFoundException |  -  |
| **481** | LimitExceededException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | BadRequestException |  -  |

<a id="getBot"></a>
# **getBot**
> GetBotResponse getBot(name, versionoralias, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns metadata information for a specific bot. You must provide the bot name and the bot version or alias. &lt;/p&gt; &lt;p&gt; This operation requires permissions for the &lt;code&gt;lex:GetBot&lt;/code&gt; action. &lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the bot. The name is case sensitive. 
    String versionoralias = "versionoralias_example"; // String | The version or alias of the bot.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetBotResponse result = apiInstance.getBot(name, versionoralias, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getBot");
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
| **name** | **String**| The name of the bot. The name is case sensitive.  | |
| **versionoralias** | **String**| The version or alias of the bot. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetBotResponse**](GetBotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | LimitExceededException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | BadRequestException |  -  |

<a id="getBotAlias"></a>
# **getBotAlias**
> GetBotAliasResponse getBotAlias(name, botName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns information about an Amazon Lex bot alias. For more information about aliases, see &lt;a&gt;versioning-aliases&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:GetBotAlias&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the bot alias. The name is case sensitive.
    String botName = "botName_example"; // String | The name of the bot.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetBotAliasResponse result = apiInstance.getBotAlias(name, botName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getBotAlias");
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
| **name** | **String**| The name of the bot alias. The name is case sensitive. | |
| **botName** | **String**| The name of the bot. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetBotAliasResponse**](GetBotAliasResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | LimitExceededException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | BadRequestException |  -  |

<a id="getBotAliases"></a>
# **getBotAliases**
> GetBotAliasesResponse getBotAliases(botName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, nameContains)



&lt;p&gt;Returns a list of aliases for a specified Amazon Lex bot.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:GetBotAliases&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botName = "botName_example"; // String | The name of the bot.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | A pagination token for fetching the next page of aliases. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of aliases, specify the pagination token in the next request. 
    Integer maxResults = 56; // Integer | The maximum number of aliases to return in the response. The default is 50. . 
    String nameContains = "nameContains_example"; // String | Substring to match in bot alias names. An alias will be returned if any part of its name matches the substring. For example, \"xyz\" matches both \"xyzabc\" and \"abcxyz.\"
    try {
      GetBotAliasesResponse result = apiInstance.getBotAliases(botName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, nameContains);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getBotAliases");
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
| **botName** | **String**| The name of the bot. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| A pagination token for fetching the next page of aliases. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of aliases, specify the pagination token in the next request.  | [optional] |
| **maxResults** | **Integer**| The maximum number of aliases to return in the response. The default is 50. .  | [optional] |
| **nameContains** | **String**| Substring to match in bot alias names. An alias will be returned if any part of its name matches the substring. For example, \&quot;xyz\&quot; matches both \&quot;xyzabc\&quot; and \&quot;abcxyz.\&quot; | [optional] |

### Return type

[**GetBotAliasesResponse**](GetBotAliasesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | LimitExceededException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | BadRequestException |  -  |

<a id="getBotChannelAssociation"></a>
# **getBotChannelAssociation**
> GetBotChannelAssociationResponse getBotChannelAssociation(name, botName, aliasName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns information about the association between an Amazon Lex bot and a messaging platform.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:GetBotChannelAssociation&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the association between the bot and the channel. The name is case sensitive. 
    String botName = "botName_example"; // String | The name of the Amazon Lex bot.
    String aliasName = "aliasName_example"; // String | An alias pointing to the specific version of the Amazon Lex bot to which this association is being made.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetBotChannelAssociationResponse result = apiInstance.getBotChannelAssociation(name, botName, aliasName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getBotChannelAssociation");
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
| **name** | **String**| The name of the association between the bot and the channel. The name is case sensitive.  | |
| **botName** | **String**| The name of the Amazon Lex bot. | |
| **aliasName** | **String**| An alias pointing to the specific version of the Amazon Lex bot to which this association is being made. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetBotChannelAssociationResponse**](GetBotChannelAssociationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | LimitExceededException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | BadRequestException |  -  |

<a id="getBotChannelAssociations"></a>
# **getBotChannelAssociations**
> GetBotChannelAssociationsResponse getBotChannelAssociations(botName, aliasName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, nameContains)



&lt;p&gt; Returns a list of all of the channels associated with the specified bot. &lt;/p&gt; &lt;p&gt;The &lt;code&gt;GetBotChannelAssociations&lt;/code&gt; operation requires permissions for the &lt;code&gt;lex:GetBotChannelAssociations&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botName = "botName_example"; // String | The name of the Amazon Lex bot in the association.
    String aliasName = "aliasName_example"; // String | An alias pointing to the specific version of the Amazon Lex bot to which this association is being made.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | A pagination token for fetching the next page of associations. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of associations, specify the pagination token in the next request. 
    Integer maxResults = 56; // Integer | The maximum number of associations to return in the response. The default is 50. 
    String nameContains = "nameContains_example"; // String | Substring to match in channel association names. An association will be returned if any part of its name matches the substring. For example, \"xyz\" matches both \"xyzabc\" and \"abcxyz.\" To return all bot channel associations, use a hyphen (\"-\") as the <code>nameContains</code> parameter.
    try {
      GetBotChannelAssociationsResponse result = apiInstance.getBotChannelAssociations(botName, aliasName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, nameContains);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getBotChannelAssociations");
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
| **botName** | **String**| The name of the Amazon Lex bot in the association. | |
| **aliasName** | **String**| An alias pointing to the specific version of the Amazon Lex bot to which this association is being made. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| A pagination token for fetching the next page of associations. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of associations, specify the pagination token in the next request.  | [optional] |
| **maxResults** | **Integer**| The maximum number of associations to return in the response. The default is 50.  | [optional] |
| **nameContains** | **String**| Substring to match in channel association names. An association will be returned if any part of its name matches the substring. For example, \&quot;xyz\&quot; matches both \&quot;xyzabc\&quot; and \&quot;abcxyz.\&quot; To return all bot channel associations, use a hyphen (\&quot;-\&quot;) as the &lt;code&gt;nameContains&lt;/code&gt; parameter. | [optional] |

### Return type

[**GetBotChannelAssociationsResponse**](GetBotChannelAssociationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | LimitExceededException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | BadRequestException |  -  |

<a id="getBotVersions"></a>
# **getBotVersions**
> GetBotVersionsResponse getBotVersions(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults)



&lt;p&gt;Gets information about all of the versions of a bot.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;GetBotVersions&lt;/code&gt; operation returns a &lt;code&gt;BotMetadata&lt;/code&gt; object for each version of a bot. For example, if a bot has three numbered versions, the &lt;code&gt;GetBotVersions&lt;/code&gt; operation returns four &lt;code&gt;BotMetadata&lt;/code&gt; objects in the response, one for each numbered version and one for the &lt;code&gt;$LATEST&lt;/code&gt; version. &lt;/p&gt; &lt;p&gt;The &lt;code&gt;GetBotVersions&lt;/code&gt; operation always returns at least one version, the &lt;code&gt;$LATEST&lt;/code&gt; version.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:GetBotVersions&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the bot for which versions should be returned.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | A pagination token for fetching the next page of bot versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request. 
    Integer maxResults = 56; // Integer | The maximum number of bot versions to return in the response. The default is 10.
    try {
      GetBotVersionsResponse result = apiInstance.getBotVersions(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getBotVersions");
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
| **name** | **String**| The name of the bot for which versions should be returned. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| A pagination token for fetching the next page of bot versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request.  | [optional] |
| **maxResults** | **Integer**| The maximum number of bot versions to return in the response. The default is 10. | [optional] |

### Return type

[**GetBotVersionsResponse**](GetBotVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | LimitExceededException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | BadRequestException |  -  |

<a id="getBots"></a>
# **getBots**
> GetBotsResponse getBots(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, nameContains)



&lt;p&gt;Returns bot information as follows: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you provide the &lt;code&gt;nameContains&lt;/code&gt; field, the response includes information for the &lt;code&gt;$LATEST&lt;/code&gt; version of all bots whose name contains the specified string.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you don&#39;t specify the &lt;code&gt;nameContains&lt;/code&gt; field, the operation returns information about the &lt;code&gt;$LATEST&lt;/code&gt; version of all of your bots.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;lex:GetBots&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
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
    String nextToken = "nextToken_example"; // String | A pagination token that fetches the next page of bots. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of bots, specify the pagination token in the next request. 
    Integer maxResults = 56; // Integer | The maximum number of bots to return in the response that the request will return. The default is 10.
    String nameContains = "nameContains_example"; // String | Substring to match in bot names. A bot will be returned if any part of its name matches the substring. For example, \"xyz\" matches both \"xyzabc\" and \"abcxyz.\"
    try {
      GetBotsResponse result = apiInstance.getBots(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, nameContains);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getBots");
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
| **nextToken** | **String**| A pagination token that fetches the next page of bots. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of bots, specify the pagination token in the next request.  | [optional] |
| **maxResults** | **Integer**| The maximum number of bots to return in the response that the request will return. The default is 10. | [optional] |
| **nameContains** | **String**| Substring to match in bot names. A bot will be returned if any part of its name matches the substring. For example, \&quot;xyz\&quot; matches both \&quot;xyzabc\&quot; and \&quot;abcxyz.\&quot; | [optional] |

### Return type

[**GetBotsResponse**](GetBotsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | LimitExceededException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | BadRequestException |  -  |

<a id="getBuiltinIntent"></a>
# **getBuiltinIntent**
> GetBuiltinIntentResponse getBuiltinIntent(signature, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns information about a built-in intent.&lt;/p&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;lex:GetBuiltinIntent&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String signature = "signature_example"; // String | The unique identifier for a built-in intent. To find the signature for an intent, see <a href=\"https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents\">Standard Built-in Intents</a> in the <i>Alexa Skills Kit</i>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetBuiltinIntentResponse result = apiInstance.getBuiltinIntent(signature, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getBuiltinIntent");
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
| **signature** | **String**| The unique identifier for a built-in intent. To find the signature for an intent, see &lt;a href&#x3D;\&quot;https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents\&quot;&gt;Standard Built-in Intents&lt;/a&gt; in the &lt;i&gt;Alexa Skills Kit&lt;/i&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetBuiltinIntentResponse**](GetBuiltinIntentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | LimitExceededException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | BadRequestException |  -  |

<a id="getBuiltinIntents"></a>
# **getBuiltinIntents**
> GetBuiltinIntentsResponse getBuiltinIntents(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, locale, signatureContains, nextToken, maxResults)



&lt;p&gt;Gets a list of built-in intents that meet the specified criteria.&lt;/p&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;lex:GetBuiltinIntents&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
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
    String locale = "de-DE"; // String | A list of locales that the intent supports.
    String signatureContains = "signatureContains_example"; // String | Substring to match in built-in intent signatures. An intent will be returned if any part of its signature matches the substring. For example, \"xyz\" matches both \"xyzabc\" and \"abcxyz.\" To find the signature for an intent, see <a href=\"https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents\">Standard Built-in Intents</a> in the <i>Alexa Skills Kit</i>.
    String nextToken = "nextToken_example"; // String | A pagination token that fetches the next page of intents. If this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of intents, use the pagination token in the next request.
    Integer maxResults = 56; // Integer | The maximum number of intents to return in the response. The default is 10.
    try {
      GetBuiltinIntentsResponse result = apiInstance.getBuiltinIntents(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, locale, signatureContains, nextToken, maxResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getBuiltinIntents");
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
| **locale** | **String**| A list of locales that the intent supports. | [optional] [enum: de-DE, en-AU, en-GB, en-IN, en-US, es-419, es-ES, es-US, fr-FR, fr-CA, it-IT, ja-JP, ko-KR] |
| **signatureContains** | **String**| Substring to match in built-in intent signatures. An intent will be returned if any part of its signature matches the substring. For example, \&quot;xyz\&quot; matches both \&quot;xyzabc\&quot; and \&quot;abcxyz.\&quot; To find the signature for an intent, see &lt;a href&#x3D;\&quot;https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents\&quot;&gt;Standard Built-in Intents&lt;/a&gt; in the &lt;i&gt;Alexa Skills Kit&lt;/i&gt;. | [optional] |
| **nextToken** | **String**| A pagination token that fetches the next page of intents. If this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of intents, use the pagination token in the next request. | [optional] |
| **maxResults** | **Integer**| The maximum number of intents to return in the response. The default is 10. | [optional] |

### Return type

[**GetBuiltinIntentsResponse**](GetBuiltinIntentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | LimitExceededException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | BadRequestException |  -  |

<a id="getBuiltinSlotTypes"></a>
# **getBuiltinSlotTypes**
> GetBuiltinSlotTypesResponse getBuiltinSlotTypes(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, locale, signatureContains, nextToken, maxResults)



&lt;p&gt;Gets a list of built-in slot types that meet the specified criteria.&lt;/p&gt; &lt;p&gt;For a list of built-in slot types, see &lt;a href&#x3D;\&quot;https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference\&quot;&gt;Slot Type Reference&lt;/a&gt; in the &lt;i&gt;Alexa Skills Kit&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;lex:GetBuiltInSlotTypes&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
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
    String locale = "de-DE"; // String | A list of locales that the slot type supports.
    String signatureContains = "signatureContains_example"; // String | Substring to match in built-in slot type signatures. A slot type will be returned if any part of its signature matches the substring. For example, \"xyz\" matches both \"xyzabc\" and \"abcxyz.\"
    String nextToken = "nextToken_example"; // String | A pagination token that fetches the next page of slot types. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of slot types, specify the pagination token in the next request.
    Integer maxResults = 56; // Integer | The maximum number of slot types to return in the response. The default is 10.
    try {
      GetBuiltinSlotTypesResponse result = apiInstance.getBuiltinSlotTypes(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, locale, signatureContains, nextToken, maxResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getBuiltinSlotTypes");
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
| **locale** | **String**| A list of locales that the slot type supports. | [optional] [enum: de-DE, en-AU, en-GB, en-IN, en-US, es-419, es-ES, es-US, fr-FR, fr-CA, it-IT, ja-JP, ko-KR] |
| **signatureContains** | **String**| Substring to match in built-in slot type signatures. A slot type will be returned if any part of its signature matches the substring. For example, \&quot;xyz\&quot; matches both \&quot;xyzabc\&quot; and \&quot;abcxyz.\&quot; | [optional] |
| **nextToken** | **String**| A pagination token that fetches the next page of slot types. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of slot types, specify the pagination token in the next request. | [optional] |
| **maxResults** | **Integer**| The maximum number of slot types to return in the response. The default is 10. | [optional] |

### Return type

[**GetBuiltinSlotTypesResponse**](GetBuiltinSlotTypesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | LimitExceededException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | BadRequestException |  -  |

<a id="getExport"></a>
# **getExport**
> GetExportResponse getExport(name, version, resourceType, exportType, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Exports the contents of a Amazon Lex resource in a specified format. 

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the bot to export.
    String version = "version_example"; // String | The version of the bot to export.
    String resourceType = "BOT"; // String | The type of resource to export. 
    String exportType = "ALEXA_SKILLS_KIT"; // String | The format of the exported data.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetExportResponse result = apiInstance.getExport(name, version, resourceType, exportType, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getExport");
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
| **name** | **String**| The name of the bot to export. | |
| **version** | **String**| The version of the bot to export. | |
| **resourceType** | **String**| The type of resource to export.  | [enum: BOT, INTENT, SLOT_TYPE] |
| **exportType** | **String**| The format of the exported data. | [enum: ALEXA_SKILLS_KIT, LEX] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetExportResponse**](GetExportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | LimitExceededException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | BadRequestException |  -  |

<a id="getImport"></a>
# **getImport**
> GetImportResponse getImport(importId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets information about an import job started with the &lt;code&gt;StartImport&lt;/code&gt; operation.

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String importId = "importId_example"; // String | The identifier of the import job information to return.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetImportResponse result = apiInstance.getImport(importId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getImport");
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
| **importId** | **String**| The identifier of the import job information to return. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetImportResponse**](GetImportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | LimitExceededException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | BadRequestException |  -  |

<a id="getIntent"></a>
# **getIntent**
> GetIntentResponse getIntent(name, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt; Returns information about an intent. In addition to the intent name, you must specify the intent version. &lt;/p&gt; &lt;p&gt; This operation requires permissions to perform the &lt;code&gt;lex:GetIntent&lt;/code&gt; action. &lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the intent. The name is case sensitive. 
    String version = "version_example"; // String | The version of the intent.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetIntentResponse result = apiInstance.getIntent(name, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getIntent");
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
| **name** | **String**| The name of the intent. The name is case sensitive.  | |
| **version** | **String**| The version of the intent. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetIntentResponse**](GetIntentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | LimitExceededException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | BadRequestException |  -  |

<a id="getIntentVersions"></a>
# **getIntentVersions**
> GetIntentVersionsResponse getIntentVersions(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults)



&lt;p&gt;Gets information about all of the versions of an intent.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;GetIntentVersions&lt;/code&gt; operation returns an &lt;code&gt;IntentMetadata&lt;/code&gt; object for each version of an intent. For example, if an intent has three numbered versions, the &lt;code&gt;GetIntentVersions&lt;/code&gt; operation returns four &lt;code&gt;IntentMetadata&lt;/code&gt; objects in the response, one for each numbered version and one for the &lt;code&gt;$LATEST&lt;/code&gt; version. &lt;/p&gt; &lt;p&gt;The &lt;code&gt;GetIntentVersions&lt;/code&gt; operation always returns at least one version, the &lt;code&gt;$LATEST&lt;/code&gt; version.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:GetIntentVersions&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the intent for which versions should be returned.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | A pagination token for fetching the next page of intent versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request. 
    Integer maxResults = 56; // Integer | The maximum number of intent versions to return in the response. The default is 10.
    try {
      GetIntentVersionsResponse result = apiInstance.getIntentVersions(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getIntentVersions");
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
| **name** | **String**| The name of the intent for which versions should be returned. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| A pagination token for fetching the next page of intent versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request.  | [optional] |
| **maxResults** | **Integer**| The maximum number of intent versions to return in the response. The default is 10. | [optional] |

### Return type

[**GetIntentVersionsResponse**](GetIntentVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | LimitExceededException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | BadRequestException |  -  |

<a id="getIntents"></a>
# **getIntents**
> GetIntentsResponse getIntents(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, nameContains)



&lt;p&gt;Returns intent information as follows: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you specify the &lt;code&gt;nameContains&lt;/code&gt; field, returns the &lt;code&gt;$LATEST&lt;/code&gt; version of all intents that contain the specified string.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; If you don&#39;t specify the &lt;code&gt;nameContains&lt;/code&gt; field, returns information about the &lt;code&gt;$LATEST&lt;/code&gt; version of all intents. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; The operation requires permission for the &lt;code&gt;lex:GetIntents&lt;/code&gt; action. &lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
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
    String nextToken = "nextToken_example"; // String | A pagination token that fetches the next page of intents. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of intents, specify the pagination token in the next request. 
    Integer maxResults = 56; // Integer | The maximum number of intents to return in the response. The default is 10.
    String nameContains = "nameContains_example"; // String | Substring to match in intent names. An intent will be returned if any part of its name matches the substring. For example, \"xyz\" matches both \"xyzabc\" and \"abcxyz.\"
    try {
      GetIntentsResponse result = apiInstance.getIntents(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, nameContains);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getIntents");
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
| **nextToken** | **String**| A pagination token that fetches the next page of intents. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of intents, specify the pagination token in the next request.  | [optional] |
| **maxResults** | **Integer**| The maximum number of intents to return in the response. The default is 10. | [optional] |
| **nameContains** | **String**| Substring to match in intent names. An intent will be returned if any part of its name matches the substring. For example, \&quot;xyz\&quot; matches both \&quot;xyzabc\&quot; and \&quot;abcxyz.\&quot; | [optional] |

### Return type

[**GetIntentsResponse**](GetIntentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | LimitExceededException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | BadRequestException |  -  |

<a id="getMigration"></a>
# **getMigration**
> GetMigrationResponse getMigration(migrationId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Provides details about an ongoing or complete migration from an Amazon Lex V1 bot to an Amazon Lex V2 bot. Use this operation to view the migration alerts and warnings related to the migration.

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String migrationId = "migrationId_example"; // String | The unique identifier of the migration to view. The <code>migrationID</code> is returned by the operation.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetMigrationResponse result = apiInstance.getMigration(migrationId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getMigration");
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
| **migrationId** | **String**| The unique identifier of the migration to view. The &lt;code&gt;migrationID&lt;/code&gt; is returned by the operation. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetMigrationResponse**](GetMigrationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | LimitExceededException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | BadRequestException |  -  |
| **483** | NotFoundException |  -  |

<a id="getMigrations"></a>
# **getMigrations**
> GetMigrationsResponse getMigrations(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, sortByAttribute, sortByOrder, v1BotNameContains, migrationStatusEquals, maxResults, nextToken)



Gets a list of migrations between Amazon Lex V1 and Amazon Lex V2.

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
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
    String sortByAttribute = "V1_BOT_NAME"; // String | The field to sort the list of migrations by. You can sort by the Amazon Lex V1 bot name or the date and time that the migration was started.
    String sortByOrder = "ASCENDING"; // String | The order so sort the list.
    String v1BotNameContains = "v1BotNameContains_example"; // String | Filters the list to contain only bots whose name contains the specified string. The string is matched anywhere in bot name.
    String migrationStatusEquals = "IN_PROGRESS"; // String | Filters the list to contain only migrations in the specified state.
    Integer maxResults = 56; // Integer | The maximum number of migrations to return in the response. The default is 10.
    String nextToken = "nextToken_example"; // String | A pagination token that fetches the next page of migrations. If the response to this operation is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of migrations, specify the pagination token in the request.
    try {
      GetMigrationsResponse result = apiInstance.getMigrations(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, sortByAttribute, sortByOrder, v1BotNameContains, migrationStatusEquals, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getMigrations");
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
| **sortByAttribute** | **String**| The field to sort the list of migrations by. You can sort by the Amazon Lex V1 bot name or the date and time that the migration was started. | [optional] [enum: V1_BOT_NAME, MIGRATION_DATE_TIME] |
| **sortByOrder** | **String**| The order so sort the list. | [optional] [enum: ASCENDING, DESCENDING] |
| **v1BotNameContains** | **String**| Filters the list to contain only bots whose name contains the specified string. The string is matched anywhere in bot name. | [optional] |
| **migrationStatusEquals** | **String**| Filters the list to contain only migrations in the specified state. | [optional] [enum: IN_PROGRESS, COMPLETED, FAILED] |
| **maxResults** | **Integer**| The maximum number of migrations to return in the response. The default is 10. | [optional] |
| **nextToken** | **String**| A pagination token that fetches the next page of migrations. If the response to this operation is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of migrations, specify the pagination token in the request. | [optional] |

### Return type

[**GetMigrationsResponse**](GetMigrationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | LimitExceededException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | BadRequestException |  -  |

<a id="getSlotType"></a>
# **getSlotType**
> GetSlotTypeResponse getSlotType(name, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns information about a specific version of a slot type. In addition to specifying the slot type name, you must specify the slot type version.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:GetSlotType&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the slot type. The name is case sensitive. 
    String version = "version_example"; // String | The version of the slot type. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetSlotTypeResponse result = apiInstance.getSlotType(name, version, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSlotType");
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
| **name** | **String**| The name of the slot type. The name is case sensitive.  | |
| **version** | **String**| The version of the slot type.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetSlotTypeResponse**](GetSlotTypeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | LimitExceededException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | BadRequestException |  -  |

<a id="getSlotTypeVersions"></a>
# **getSlotTypeVersions**
> GetSlotTypeVersionsResponse getSlotTypeVersions(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults)



&lt;p&gt;Gets information about all versions of a slot type.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;GetSlotTypeVersions&lt;/code&gt; operation returns a &lt;code&gt;SlotTypeMetadata&lt;/code&gt; object for each version of a slot type. For example, if a slot type has three numbered versions, the &lt;code&gt;GetSlotTypeVersions&lt;/code&gt; operation returns four &lt;code&gt;SlotTypeMetadata&lt;/code&gt; objects in the response, one for each numbered version and one for the &lt;code&gt;$LATEST&lt;/code&gt; version. &lt;/p&gt; &lt;p&gt;The &lt;code&gt;GetSlotTypeVersions&lt;/code&gt; operation always returns at least one version, the &lt;code&gt;$LATEST&lt;/code&gt; version.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:GetSlotTypeVersions&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the slot type for which versions should be returned.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | A pagination token for fetching the next page of slot type versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request. 
    Integer maxResults = 56; // Integer | The maximum number of slot type versions to return in the response. The default is 10.
    try {
      GetSlotTypeVersionsResponse result = apiInstance.getSlotTypeVersions(name, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSlotTypeVersions");
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
| **name** | **String**| The name of the slot type for which versions should be returned. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| A pagination token for fetching the next page of slot type versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request.  | [optional] |
| **maxResults** | **Integer**| The maximum number of slot type versions to return in the response. The default is 10. | [optional] |

### Return type

[**GetSlotTypeVersionsResponse**](GetSlotTypeVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | LimitExceededException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | BadRequestException |  -  |

<a id="getSlotTypes"></a>
# **getSlotTypes**
> GetSlotTypesResponse getSlotTypes(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, nameContains)



&lt;p&gt;Returns slot type information as follows: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you specify the &lt;code&gt;nameContains&lt;/code&gt; field, returns the &lt;code&gt;$LATEST&lt;/code&gt; version of all slot types that contain the specified string.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; If you don&#39;t specify the &lt;code&gt;nameContains&lt;/code&gt; field, returns information about the &lt;code&gt;$LATEST&lt;/code&gt; version of all slot types. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; The operation requires permission for the &lt;code&gt;lex:GetSlotTypes&lt;/code&gt; action. &lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
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
    String nextToken = "nextToken_example"; // String | A pagination token that fetches the next page of slot types. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch next page of slot types, specify the pagination token in the next request.
    Integer maxResults = 56; // Integer | The maximum number of slot types to return in the response. The default is 10.
    String nameContains = "nameContains_example"; // String | Substring to match in slot type names. A slot type will be returned if any part of its name matches the substring. For example, \"xyz\" matches both \"xyzabc\" and \"abcxyz.\"
    try {
      GetSlotTypesResponse result = apiInstance.getSlotTypes(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, nameContains);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSlotTypes");
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
| **nextToken** | **String**| A pagination token that fetches the next page of slot types. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch next page of slot types, specify the pagination token in the next request. | [optional] |
| **maxResults** | **Integer**| The maximum number of slot types to return in the response. The default is 10. | [optional] |
| **nameContains** | **String**| Substring to match in slot type names. A slot type will be returned if any part of its name matches the substring. For example, \&quot;xyz\&quot; matches both \&quot;xyzabc\&quot; and \&quot;abcxyz.\&quot; | [optional] |

### Return type

[**GetSlotTypesResponse**](GetSlotTypesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | LimitExceededException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | BadRequestException |  -  |

<a id="getUtterancesView"></a>
# **getUtterancesView**
> GetUtterancesViewResponse getUtterancesView(botname, botVersions, statusType, view, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Use the &lt;code&gt;GetUtterancesView&lt;/code&gt; operation to get information about the utterances that your users have made to your bot. You can use this list to tune the utterances that your bot responds to.&lt;/p&gt; &lt;p&gt;For example, say that you have created a bot to order flowers. After your users have used your bot for a while, use the &lt;code&gt;GetUtterancesView&lt;/code&gt; operation to see the requests that they have made and whether they have been successful. You might find that the utterance \&quot;I want flowers\&quot; is not being recognized. You could add this utterance to the &lt;code&gt;OrderFlowers&lt;/code&gt; intent so that your bot recognizes that utterance.&lt;/p&gt; &lt;p&gt;After you publish a new version of a bot, you can get information about the old version and the new so that you can compare the performance across the two versions. &lt;/p&gt; &lt;p&gt;Utterance statistics are generated once a day. Data is available for the last 15 days. You can request information for up to 5 versions of your bot in each request. Amazon Lex returns the most frequent utterances received by the bot in the last 15 days. The response contains information about a maximum of 100 utterances for each version.&lt;/p&gt; &lt;p&gt;If you set &lt;code&gt;childDirected&lt;/code&gt; field to true when you created your bot, if you are using slot obfuscation with one or more slots, or if you opted out of participating in improving Amazon Lex, utterances are not available.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:GetUtterancesView&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String botname = "botname_example"; // String | The name of the bot for which utterance information should be returned.
    List<String> botVersions = Arrays.asList(); // List<String> | An array of bot versions for which utterance information should be returned. The limit is 5 versions per request.
    String statusType = "Detected"; // String | To return utterances that were recognized and handled, use <code>Detected</code>. To return utterances that were not recognized, use <code>Missed</code>.
    String view = "aggregation"; // String | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetUtterancesViewResponse result = apiInstance.getUtterancesView(botname, botVersions, statusType, view, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getUtterancesView");
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
| **botname** | **String**| The name of the bot for which utterance information should be returned. | |
| **botVersions** | [**List&lt;String&gt;**](String.md)| An array of bot versions for which utterance information should be returned. The limit is 5 versions per request. | |
| **statusType** | **String**| To return utterances that were recognized and handled, use &lt;code&gt;Detected&lt;/code&gt;. To return utterances that were not recognized, use &lt;code&gt;Missed&lt;/code&gt;. | [enum: Detected, Missed] |
| **view** | **String**|  | [enum: aggregation] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetUtterancesViewResponse**](GetUtterancesViewResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | LimitExceededException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | BadRequestException |  -  |

<a id="listTagsForResource"></a>
# **listTagsForResource**
> ListTagsForResourceResponse listTagsForResource(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets a list of tags associated with the specified resource. Only bots, bot aliases, and bot channels can have tags associated with them.

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource to get a list of tags for.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListTagsForResourceResponse result = apiInstance.listTagsForResource(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
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
| **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource to get a list of tags for. | |
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
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | LimitExceededException |  -  |

<a id="putBot"></a>
# **putBot**
> PutBotResponse putBot(name, putBotRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates an Amazon Lex conversational bot or replaces an existing bot. When you create or update a bot you are only required to specify a name, a locale, and whether the bot is directed toward children under age 13. You can use this to add intents later, or to remove intents from an existing bot. When you create a bot with the minimum information, the bot is created or updated but Amazon Lex returns the &lt;code/&gt; response &lt;code&gt;FAILED&lt;/code&gt;. You can build the bot after you add one or more intents. For more information about Amazon Lex bots, see &lt;a&gt;how-it-works&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;If you specify the name of an existing bot, the fields in the request replace the existing values in the &lt;code&gt;$LATEST&lt;/code&gt; version of the bot. Amazon Lex removes any fields that you don&#39;t provide values for in the request, except for the &lt;code&gt;idleTTLInSeconds&lt;/code&gt; and &lt;code&gt;privacySettings&lt;/code&gt; fields, which are set to their default values. If you don&#39;t specify values for required fields, Amazon Lex throws an exception.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:PutBot&lt;/code&gt; action. For more information, see &lt;a&gt;security-iam&lt;/a&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the bot. The name is <i>not</i> case sensitive. 
    PutBotRequest putBotRequest = new PutBotRequest(); // PutBotRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PutBotResponse result = apiInstance.putBot(name, putBotRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putBot");
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
| **name** | **String**| The name of the bot. The name is &lt;i&gt;not&lt;/i&gt; case sensitive.  | |
| **putBotRequest** | [**PutBotRequest**](PutBotRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PutBotResponse**](PutBotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ConflictException |  -  |
| **481** | LimitExceededException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | BadRequestException |  -  |
| **484** | PreconditionFailedException |  -  |

<a id="putBotAlias"></a>
# **putBotAlias**
> PutBotAliasResponse putBotAlias(name, botName, putBotAliasRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates an alias for the specified version of the bot or replaces an alias for the specified bot. To change the version of the bot that the alias points to, replace the alias. For more information about aliases, see &lt;a&gt;versioning-aliases&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:PutBotAlias&lt;/code&gt; action. &lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the alias. The name is <i>not</i> case sensitive.
    String botName = "botName_example"; // String | The name of the bot.
    PutBotAliasRequest putBotAliasRequest = new PutBotAliasRequest(); // PutBotAliasRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PutBotAliasResponse result = apiInstance.putBotAlias(name, botName, putBotAliasRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putBotAlias");
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
| **name** | **String**| The name of the alias. The name is &lt;i&gt;not&lt;/i&gt; case sensitive. | |
| **botName** | **String**| The name of the bot. | |
| **putBotAliasRequest** | [**PutBotAliasRequest**](PutBotAliasRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PutBotAliasResponse**](PutBotAliasResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ConflictException |  -  |
| **481** | LimitExceededException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | BadRequestException |  -  |
| **484** | PreconditionFailedException |  -  |

<a id="putIntent"></a>
# **putIntent**
> PutIntentResponse putIntent(name, putIntentRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates an intent or replaces an existing intent.&lt;/p&gt; &lt;p&gt;To define the interaction between the user and your bot, you use one or more intents. For a pizza ordering bot, for example, you would create an &lt;code&gt;OrderPizza&lt;/code&gt; intent. &lt;/p&gt; &lt;p&gt;To create an intent or replace an existing intent, you must provide the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Intent name. For example, &lt;code&gt;OrderPizza&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Sample utterances. For example, \&quot;Can I order a pizza, please.\&quot; and \&quot;I want to order a pizza.\&quot;&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Information to be gathered. You specify slot types for the information that your bot will request from the user. You can specify standard slot types, such as a date or a time, or custom slot types such as the size and crust of a pizza.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;How the intent will be fulfilled. You can provide a Lambda function or configure the intent to return the intent information to the client application. If you use a Lambda function, when all of the intent information is available, Amazon Lex invokes your Lambda function. If you configure your intent to return the intent information to the client application. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You can specify other optional information in the request, such as:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;A confirmation prompt to ask the user to confirm an intent. For example, \&quot;Shall I order your pizza?\&quot;&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A conclusion statement to send to the user after the intent has been fulfilled. For example, \&quot;I placed your pizza order.\&quot;&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A follow-up prompt that asks the user for additional activity. For example, asking \&quot;Do you want to order a drink with your pizza?\&quot;&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you specify an existing intent name to update the intent, Amazon Lex replaces the values in the &lt;code&gt;$LATEST&lt;/code&gt; version of the intent with the values in the request. Amazon Lex removes fields that you don&#39;t provide in the request. If you don&#39;t specify the required fields, Amazon Lex throws an exception. When you update the &lt;code&gt;$LATEST&lt;/code&gt; version of an intent, the &lt;code&gt;status&lt;/code&gt; field of any bot that uses the &lt;code&gt;$LATEST&lt;/code&gt; version of the intent is set to &lt;code&gt;NOT_BUILT&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a&gt;how-it-works&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:PutIntent&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | <p>The name of the intent. The name is <i>not</i> case sensitive. </p> <p>The name can't match a built-in intent name, or a built-in intent name with \"AMAZON.\" removed. For example, because there is a built-in intent called <code>AMAZON.HelpIntent</code>, you can't create a custom intent called <code>HelpIntent</code>.</p> <p>For a list of built-in intents, see <a href=\"https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents\">Standard Built-in Intents</a> in the <i>Alexa Skills Kit</i>.</p>
    PutIntentRequest putIntentRequest = new PutIntentRequest(); // PutIntentRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PutIntentResponse result = apiInstance.putIntent(name, putIntentRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putIntent");
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
| **name** | **String**| &lt;p&gt;The name of the intent. The name is &lt;i&gt;not&lt;/i&gt; case sensitive. &lt;/p&gt; &lt;p&gt;The name can&#39;t match a built-in intent name, or a built-in intent name with \&quot;AMAZON.\&quot; removed. For example, because there is a built-in intent called &lt;code&gt;AMAZON.HelpIntent&lt;/code&gt;, you can&#39;t create a custom intent called &lt;code&gt;HelpIntent&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For a list of built-in intents, see &lt;a href&#x3D;\&quot;https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents\&quot;&gt;Standard Built-in Intents&lt;/a&gt; in the &lt;i&gt;Alexa Skills Kit&lt;/i&gt;.&lt;/p&gt; | |
| **putIntentRequest** | [**PutIntentRequest**](PutIntentRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PutIntentResponse**](PutIntentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ConflictException |  -  |
| **481** | LimitExceededException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | BadRequestException |  -  |
| **484** | PreconditionFailedException |  -  |

<a id="putSlotType"></a>
# **putSlotType**
> PutSlotTypeResponse putSlotType(name, putSlotTypeRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a custom slot type or replaces an existing custom slot type.&lt;/p&gt; &lt;p&gt;To create a custom slot type, specify a name for the slot type and a set of enumeration values, which are the values that a slot of this type can assume. For more information, see &lt;a&gt;how-it-works&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you specify the name of an existing slot type, the fields in the request replace the existing values in the &lt;code&gt;$LATEST&lt;/code&gt; version of the slot type. Amazon Lex removes the fields that you don&#39;t provide in the request. If you don&#39;t specify required fields, Amazon Lex throws an exception. When you update the &lt;code&gt;$LATEST&lt;/code&gt; version of a slot type, if a bot uses the &lt;code&gt;$LATEST&lt;/code&gt; version of an intent that contains the slot type, the bot&#39;s &lt;code&gt;status&lt;/code&gt; field is set to &lt;code&gt;NOT_BUILT&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:PutSlotType&lt;/code&gt; action.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | <p>The name of the slot type. The name is <i>not</i> case sensitive. </p> <p>The name can't match a built-in slot type name, or a built-in slot type name with \"AMAZON.\" removed. For example, because there is a built-in slot type called <code>AMAZON.DATE</code>, you can't create a custom slot type called <code>DATE</code>.</p> <p>For a list of built-in slot types, see <a href=\"https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference\">Slot Type Reference</a> in the <i>Alexa Skills Kit</i>.</p>
    PutSlotTypeRequest putSlotTypeRequest = new PutSlotTypeRequest(); // PutSlotTypeRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PutSlotTypeResponse result = apiInstance.putSlotType(name, putSlotTypeRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putSlotType");
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
| **name** | **String**| &lt;p&gt;The name of the slot type. The name is &lt;i&gt;not&lt;/i&gt; case sensitive. &lt;/p&gt; &lt;p&gt;The name can&#39;t match a built-in slot type name, or a built-in slot type name with \&quot;AMAZON.\&quot; removed. For example, because there is a built-in slot type called &lt;code&gt;AMAZON.DATE&lt;/code&gt;, you can&#39;t create a custom slot type called &lt;code&gt;DATE&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For a list of built-in slot types, see &lt;a href&#x3D;\&quot;https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference\&quot;&gt;Slot Type Reference&lt;/a&gt; in the &lt;i&gt;Alexa Skills Kit&lt;/i&gt;.&lt;/p&gt; | |
| **putSlotTypeRequest** | [**PutSlotTypeRequest**](PutSlotTypeRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PutSlotTypeResponse**](PutSlotTypeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ConflictException |  -  |
| **481** | LimitExceededException |  -  |
| **482** | InternalFailureException |  -  |
| **483** | BadRequestException |  -  |
| **484** | PreconditionFailedException |  -  |

<a id="startImport"></a>
# **startImport**
> StartImportResponse startImport(startImportRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Starts a job to import a resource to Amazon Lex.

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
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
| **201** | Success |  -  |
| **480** | LimitExceededException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | BadRequestException |  -  |

<a id="startMigration"></a>
# **startMigration**
> StartMigrationResponse startMigration(startMigrationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Starts migrating a bot from Amazon Lex V1 to Amazon Lex V2. Migrate your bot when you want to take advantage of the new features of Amazon Lex V2.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lex/latest/dg/migrate.html\&quot;&gt;Migrating a bot&lt;/a&gt; in the &lt;i&gt;Amazon Lex developer guide&lt;/i&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    StartMigrationRequest startMigrationRequest = new StartMigrationRequest(); // StartMigrationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      StartMigrationResponse result = apiInstance.startMigration(startMigrationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startMigration");
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
| **startMigrationRequest** | [**StartMigrationRequest**](StartMigrationRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**StartMigrationResponse**](StartMigrationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | LimitExceededException |  -  |
| **481** | InternalFailureException |  -  |
| **482** | BadRequestException |  -  |
| **483** | AccessDeniedException |  -  |
| **484** | NotFoundException |  -  |

<a id="tagResource"></a>
# **tagResource**
> Object tagResource(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the bot, bot alias, or bot channel to tag.
    TagResourceRequest tagResourceRequest = new TagResourceRequest(); // TagResourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.tagResource(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
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
| **resourceArn** | **String**| The Amazon Resource Name (ARN) of the bot, bot alias, or bot channel to tag. | |
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
| **204** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | ConflictException |  -  |
| **483** | InternalFailureException |  -  |
| **484** | LimitExceededException |  -  |

<a id="untagResource"></a>
# **untagResource**
> Object untagResource(resourceArn, tagKeys, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Removes tags from a bot, bot alias or bot channel.

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
    defaultClient.setBasePath("http://models.lex.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource to remove the tags from.
    List<String> tagKeys = Arrays.asList(); // List<String> | A list of tag keys to remove from the resource. If a tag key does not exist on the resource, it is ignored.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.untagResource(resourceArn, tagKeys, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
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
| **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource to remove the tags from. | |
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
| **204** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | ConflictException |  -  |
| **483** | InternalFailureException |  -  |
| **484** | LimitExceededException |  -  |

