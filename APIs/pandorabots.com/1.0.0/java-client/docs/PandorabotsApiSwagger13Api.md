# PandorabotsApiSwagger13Api

All URIs are relative to *https://aiaas.pandorabots.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**atalkBot**](PandorabotsApiSwagger13Api.md#atalkBot) | **POST** /atalk/{app_id}/{botname} | Anonymous Talk |
| [**compileBot**](PandorabotsApiSwagger13Api.md#compileBot) | **GET** /bot/{app_id}/{botname}/verify | Compile a bot |
| [**createBot**](PandorabotsApiSwagger13Api.md#createBot) | **PUT** /bot/{app_id}/{botname} | Create a bot |
| [**debugBot**](PandorabotsApiSwagger13Api.md#debugBot) | **POST** /talk/{app_id}/{botname} | Debug a bot conversation |
| [**deleteBot**](PandorabotsApiSwagger13Api.md#deleteBot) | **DELETE** /bot/{app_id}/{botname} | Delete a bot |
| [**deleteBotFile1**](PandorabotsApiSwagger13Api.md#deleteBotFile1) | **DELETE** /bot/{app_id}/{botname}/{file-kind}/{filename} | Delete a bot file (AIML, set, map, substitution) |
| [**deleteBotFile2**](PandorabotsApiSwagger13Api.md#deleteBotFile2) | **DELETE** /bot/{app_id}/{botname}/{file-kind} | Delete a bot file (pdefaults, properties) |
| [**getBotFile1**](PandorabotsApiSwagger13Api.md#getBotFile1) | **GET** /bot/{app_id}/{botname}/{file-kind}/{filename} | Retrieve a bot file (AIML, set, map, substitution) |
| [**getBotFile2**](PandorabotsApiSwagger13Api.md#getBotFile2) | **GET** /bot/{app_id}/{botname}/{file-kind} | Retrieve a bot file (pdefaults, properties) |
| [**listBotFiles**](PandorabotsApiSwagger13Api.md#listBotFiles) | **GET** /bot/{app_id}/{botname} | List of bot files |
| [**listBots**](PandorabotsApiSwagger13Api.md#listBots) | **GET** /bot/{app_id} | List of bots |
| [**uploadFile1**](PandorabotsApiSwagger13Api.md#uploadFile1) | **PUT** /bot/{app_id}/{botname}/{file-kind}/{filename} | Upload a bot file (AIML, set, substitution, map) |
| [**uploadFile2**](PandorabotsApiSwagger13Api.md#uploadFile2) | **PUT** /bot/{app_id}/{botname}/{file-kind} | Upload a bot file (pdefaults, properties) |


<a id="atalkBot"></a>
# **atalkBot**
> atalkBot(appId, botname, input, clientName, sessionid, recent)

Anonymous Talk

Start a conversation with the bot using the Anonymous Talk API. This method will allow you to request creation of an end-user client_name that can maintain persistent predicates per end-user talking to your bot. If client_name is NOT sent in the request, then Pandorabots will create a end-user client_name and return it in the response. Similar to the Talk to Bot API, Pandorabots will also return a new session ID if not included in the call. Use the session ID returned to group interactions together. &lt;p&gt;In addition to bot response and session ID, the HTTP response will include a new end-user client_name in the following format:&lt;br&gt;aiaas-XXX-user-nnnn, where XXX is your app_ID and nnnn is numeric starting with 0000 and incrementing after each request.&lt;br/&gt; &lt;/p&gt;&lt;p&gt;Malformed requests such as exceeding size of input or unknown end-user client_name returns 400 error code. Error code 412 is returned if the bot is not compiled or does not exist. Error code 429 is returned if your application has reached maximum plan API call limit.&lt;/p&gt;&lt;p&gt;&lt;pre class&#x3D;&#39;prettyprint&#39;&gt;curl -v  -X POST &#39;https://aiaas.pandorabots.com/atalk/APP_ID/BOTNAME?user_key&#x3D;USER_KEY&amp;input&#x3D;INPUT&#39;&lt;/pre&gt;&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PandorabotsApiSwagger13Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://aiaas.pandorabots.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    PandorabotsApiSwagger13Api apiInstance = new PandorabotsApiSwagger13Api(defaultClient);
    String appId = "appId_example"; // String | Your Application ID
    String botname = "botname_example"; // String | The name of the bot. Format required is 3-64 characters in length and only numbers or lower-case letters [0-9][a-z]
    String input = "input_example"; // String | Message to be sent to the bot. This can contain multiple sentences. Currently the limit is 500 characters.
    String clientName = "clientName_example"; // String | Leave blank to request Pandorabots to create a client_name which will support persistent predicates. Including a valid client_name in this parameter will work in the same way that Talk to Bot API but with persistent predicates. It is recommended to use this API only to create an end-user client_name, and then use normal Talk to Bot API to continue conversation with the bot.
    String sessionid = "sessionid_example"; // String | Session ID generated by Pandorabots. This allows the application to group individual conversations into a collection as needed. If not included in the call, Pandorabots will issue a new session ID. (4-byte integer type)
    String recent = "recent_example"; // String | If true, the system will not signal an error if the bot is uncompiled, and will instead look for a previous version of the bot that is available.
    try {
      apiInstance.atalkBot(appId, botname, input, clientName, sessionid, recent);
    } catch (ApiException e) {
      System.err.println("Exception when calling PandorabotsApiSwagger13Api#atalkBot");
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
| **appId** | **String**| Your Application ID | |
| **botname** | **String**| The name of the bot. Format required is 3-64 characters in length and only numbers or lower-case letters [0-9][a-z] | |
| **input** | **String**| Message to be sent to the bot. This can contain multiple sentences. Currently the limit is 500 characters. | |
| **clientName** | **String**| Leave blank to request Pandorabots to create a client_name which will support persistent predicates. Including a valid client_name in this parameter will work in the same way that Talk to Bot API but with persistent predicates. It is recommended to use this API only to create an end-user client_name, and then use normal Talk to Bot API to continue conversation with the bot. | [optional] |
| **sessionid** | **String**| Session ID generated by Pandorabots. This allows the application to group individual conversations into a collection as needed. If not included in the call, Pandorabots will issue a new session ID. (4-byte integer type) | [optional] |
| **recent** | **String**| If true, the system will not signal an error if the bot is uncompiled, and will instead look for a previous version of the bot that is available. | [optional] |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="compileBot"></a>
# **compileBot**
> compileBot(appId, botname)

Compile a bot

A bot personality is created by uploading AIML and other file types to Pandorabots. The files must compile correctly in order for the bot to run. By issuing a call to this API, Pandorabots will compile the bot, updating any changes that have been made to the files.&lt;p&gt;Compiling the bot makes its most recent version available for talk. A 400 error means that we were unable to compile your bot (you should check your files for syntax issues) or the botname was not found. &lt;/p&gt;&lt;p&gt;You can see any thrown errors in the results field of the returned JSON object:&lt;/p&gt;&lt;p&gt;&lt;pre class&#x3D;&#39;prettyprint&#39;&gt;curl -v  -X GET &#39;https://aiaas.pandorabots.com/bot/APP_ID/BOTNAME/verify?user_key&#x3D;USER_KEY&#39;&lt;/pre&gt;&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PandorabotsApiSwagger13Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://aiaas.pandorabots.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    PandorabotsApiSwagger13Api apiInstance = new PandorabotsApiSwagger13Api(defaultClient);
    String appId = "appId_example"; // String | Your Application ID
    String botname = "botname_example"; // String | Your bot's name
    try {
      apiInstance.compileBot(appId, botname);
    } catch (ApiException e) {
      System.err.println("Exception when calling PandorabotsApiSwagger13Api#compileBot");
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
| **appId** | **String**| Your Application ID | |
| **botname** | **String**| Your bot&#39;s name | |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="createBot"></a>
# **createBot**
> createBot(appId, botname)

Create a bot

Create a new instance of a bot on the Pandorabots server.&lt;p&gt;If there is already a bot under the same app_id and botname, a 409 error is returned. Invalid botname will return a 400 error.&lt;/p&gt;&lt;p&gt;Creating more bots than your plan allows or using an invalid app_id or user_key (or if applicable referrer filter) returns a 401 error.&lt;/p&gt;&lt;p&gt;&lt;pre class&#x3D;&#39;prettyprint&#39;&gt;curl -v  -X PUT &#39;https://aiaas.pandorabots.com/bot/APP_ID/BOTNAME?user_key&#x3D;USER_KEY&#39;&lt;/pre&gt;&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PandorabotsApiSwagger13Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://aiaas.pandorabots.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    PandorabotsApiSwagger13Api apiInstance = new PandorabotsApiSwagger13Api(defaultClient);
    String appId = "appId_example"; // String | Your Application ID
    String botname = "botname_example"; // String | Must be unique from all the other bots you have created under this app_id. Can only be numbers and lowercase letters, and must be between 3 and 64 characters long.
    try {
      apiInstance.createBot(appId, botname);
    } catch (ApiException e) {
      System.err.println("Exception when calling PandorabotsApiSwagger13Api#createBot");
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
| **appId** | **String**| Your Application ID | |
| **botname** | **String**| Must be unique from all the other bots you have created under this app_id. Can only be numbers and lowercase letters, and must be between 3 and 64 characters long. | |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="debugBot"></a>
# **debugBot**
> debugBot(appId, botname, input, clientName, sessionid, that, topic, extra, reset, trace, reload, recent)

Debug a bot conversation

Use these tools to test/debug/trace bot categories. &lt;p&gt;Malformed requests such as exceeding size of input or invalid clientname returns 400 error code. Error code 412 is returned if the bot is not compiled or does not exist.&lt;/p&gt;&lt;p&gt;&lt;pre class&#x3D;&#39;prettyprint&#39;&gt;curl -v  -X POST &#39;https://aiaas.pandorabots.com/talk/APP_ID/BOTNAME?user_key&#x3D;USER_KEY&amp;input&#x3D;INPUT&#39;&lt;/pre&gt;&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PandorabotsApiSwagger13Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://aiaas.pandorabots.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    PandorabotsApiSwagger13Api apiInstance = new PandorabotsApiSwagger13Api(defaultClient);
    String appId = "appId_example"; // String | Your Application ID
    String botname = "botname_example"; // String | The name of the bot. Format required is 3-64 characters in length and only numbers or lower-case letters [0-9][a-z]
    String input = "input_example"; // String | Message to be sent to the bot. This can contain multiple sentences. Currently the limit is 500 characters.
    String clientName = "clientName_example"; // String | Identifies your application's end user. You can assign each of your end users a unique client_name. This will allow you to set predicates and other variable information that is specific to an individual. Format required is 3-64 characters in length and only numbers or lower-case letters [0-9][a-z]
    String sessionid = "sessionid_example"; // String | Session ID generated by Pandorabots. This allows the application to group individual conversations into a collection. While testing your bot, not including this parameter, Pandorabots will issue a new session ID. (4-byte integer type)
    String that = "that_example"; // String | For debugging purposes, you can specify a 'that' with the input that supersedes the existing that in bot memory.
    String topic = "topic_example"; // String | For debugging purposes, you can specify a 'topic' with the input that supersedes the existing topic in bot memory.
    String extra = "extra_example"; // String | Return extra conversation information. If true, input, pattern, that, topic, filename, and template associated with the pattern matched are returned in addition to response and sessionid.
    String reset = "reset_example"; // String | Reset the bot memory. If true, all predicate values in the bot will be discarded, and the user can talk to the bot as if it is the first time
    String trace = "trace_example"; // String | Include trace data in the response. If true, the system will generate AIML trace information for the input. Trace data includes pattern matched, filename, input, template for all recursion levels. NOTE: for security reasons, trace does not work with client_name.
    String reload = "reload_example"; // String | If true, the system will force a reload of the bot into memory. This can be useful if you've recently uploaded an AIML file, recompiled your bot and want access to your bot's latest changes.
    String recent = "recent_example"; // String | If true, the system will not signal an error if the bot is uncompiled, and will instead look for a previous version of the bot that is available.
    try {
      apiInstance.debugBot(appId, botname, input, clientName, sessionid, that, topic, extra, reset, trace, reload, recent);
    } catch (ApiException e) {
      System.err.println("Exception when calling PandorabotsApiSwagger13Api#debugBot");
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
| **appId** | **String**| Your Application ID | |
| **botname** | **String**| The name of the bot. Format required is 3-64 characters in length and only numbers or lower-case letters [0-9][a-z] | |
| **input** | **String**| Message to be sent to the bot. This can contain multiple sentences. Currently the limit is 500 characters. | |
| **clientName** | **String**| Identifies your application&#39;s end user. You can assign each of your end users a unique client_name. This will allow you to set predicates and other variable information that is specific to an individual. Format required is 3-64 characters in length and only numbers or lower-case letters [0-9][a-z] | [optional] |
| **sessionid** | **String**| Session ID generated by Pandorabots. This allows the application to group individual conversations into a collection. While testing your bot, not including this parameter, Pandorabots will issue a new session ID. (4-byte integer type) | [optional] |
| **that** | **String**| For debugging purposes, you can specify a &#39;that&#39; with the input that supersedes the existing that in bot memory. | [optional] |
| **topic** | **String**| For debugging purposes, you can specify a &#39;topic&#39; with the input that supersedes the existing topic in bot memory. | [optional] |
| **extra** | **String**| Return extra conversation information. If true, input, pattern, that, topic, filename, and template associated with the pattern matched are returned in addition to response and sessionid. | [optional] |
| **reset** | **String**| Reset the bot memory. If true, all predicate values in the bot will be discarded, and the user can talk to the bot as if it is the first time | [optional] |
| **trace** | **String**| Include trace data in the response. If true, the system will generate AIML trace information for the input. Trace data includes pattern matched, filename, input, template for all recursion levels. NOTE: for security reasons, trace does not work with client_name. | [optional] |
| **reload** | **String**| If true, the system will force a reload of the bot into memory. This can be useful if you&#39;ve recently uploaded an AIML file, recompiled your bot and want access to your bot&#39;s latest changes. | [optional] |
| **recent** | **String**| If true, the system will not signal an error if the bot is uncompiled, and will instead look for a previous version of the bot that is available. | [optional] |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="deleteBot"></a>
# **deleteBot**
> deleteBot(appId, botname)

Delete a bot

Delete a bot on the Pandorabots server.&lt;p&gt;Deleting a bot that does not exist returns a 412 error. Invalid botname will return a 400 error. Invalid app_id, user_key, or referrer filter will return a 401 error.&lt;/p&gt;&lt;p&gt;&lt;pre class&#x3D;&#39;prettyprint&#39;&gt;curl -v  -X DELETE &#39;https://aiaas.pandorabots.com/bot/APP_ID/BOTNAME?user_key&#x3D;USER_KEY&#39;&lt;/pre&gt;&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PandorabotsApiSwagger13Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://aiaas.pandorabots.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    PandorabotsApiSwagger13Api apiInstance = new PandorabotsApiSwagger13Api(defaultClient);
    String appId = "appId_example"; // String | Your Application ID
    String botname = "botname_example"; // String | Name of the bot to delete.
    try {
      apiInstance.deleteBot(appId, botname);
    } catch (ApiException e) {
      System.err.println("Exception when calling PandorabotsApiSwagger13Api#deleteBot");
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
| **appId** | **String**| Your Application ID | |
| **botname** | **String**| Name of the bot to delete. | |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="deleteBotFile1"></a>
# **deleteBotFile1**
> deleteBotFile1(appId, botname, fileKind, filename)

Delete a bot file (AIML, set, map, substitution)

Delete an AIML, set, map or substitution bot file&lt;p&gt;For malformed file-kind, a 404 error is returned. For invalid file or botname, a 412 error is returned.&lt;/p&gt;&lt;pre&gt;&lt;p&gt;curl -v -X DELETE &#39;https://aiaas.pandorabots.com/bot/APP_ID/BOTNAME/FILE-KIND/FILENAME?user_key&#x3D;USER_KEY&#39;&lt;/p&gt;&lt;/pre&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PandorabotsApiSwagger13Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://aiaas.pandorabots.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    PandorabotsApiSwagger13Api apiInstance = new PandorabotsApiSwagger13Api(defaultClient);
    String appId = "appId_example"; // String | Your Application ID
    String botname = "botname_example"; // String | Name of the bot.
    String fileKind = "fileKind_example"; // String | Specify the type of file being deleted: file (for AIML files), map, substitution, set
    String filename = "filename_example"; // String | Filename to delete. Note: for non-AIML files, do not include the file extension in the path.
    try {
      apiInstance.deleteBotFile1(appId, botname, fileKind, filename);
    } catch (ApiException e) {
      System.err.println("Exception when calling PandorabotsApiSwagger13Api#deleteBotFile1");
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
| **appId** | **String**| Your Application ID | |
| **botname** | **String**| Name of the bot. | |
| **fileKind** | **String**| Specify the type of file being deleted: file (for AIML files), map, substitution, set | |
| **filename** | **String**| Filename to delete. Note: for non-AIML files, do not include the file extension in the path. | |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="deleteBotFile2"></a>
# **deleteBotFile2**
> deleteBotFile2(appId, botname, fileKind)

Delete a bot file (pdefaults, properties)

Delete pdefaults or properties bot file.&lt;p&gt;For malformed file-kind, a 404 error is returned. For invalid botname, a 412 error is returned.&lt;/p&gt;&lt;pre&gt;&lt;p&gt;curl -v -X DELETE &#39;https://aiaas.pandorabots.com/bot/APP_ID/BOTNAME/FILE-KIND?user_key&#x3D;USER_KEY&#39;&lt;/p&gt;&lt;/pre&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PandorabotsApiSwagger13Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://aiaas.pandorabots.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    PandorabotsApiSwagger13Api apiInstance = new PandorabotsApiSwagger13Api(defaultClient);
    String appId = "appId_example"; // String | Your Application ID
    String botname = "botname_example"; // String | Name of the bot.
    String fileKind = "fileKind_example"; // String | Specify the type of file being deleted: pdefaults, properties
    try {
      apiInstance.deleteBotFile2(appId, botname, fileKind);
    } catch (ApiException e) {
      System.err.println("Exception when calling PandorabotsApiSwagger13Api#deleteBotFile2");
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
| **appId** | **String**| Your Application ID | |
| **botname** | **String**| Name of the bot. | |
| **fileKind** | **String**| Specify the type of file being deleted: pdefaults, properties | |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="getBotFile1"></a>
# **getBotFile1**
> getBotFile1(appId, botname, fileKind, filename)

Retrieve a bot file (AIML, set, map, substitution)

Retrieve an AIML, set, map or substitution bot file.&lt;p&gt;For malformed file-kind, a 404 error is returned. For invalid filename or botname, a 400 error is returned. For unknown bot or file, a 412 error is returned.&lt;/p&gt;&lt;pre&gt;&lt;p&gt;curl -v -X GET &#39;https://aiaas.pandorabots.com/bot/APP_ID/BOTNAME/FILE-KIND/FILENAME?user_key&#x3D;USER_KEY&#39;&lt;/p&gt;&lt;/pre&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PandorabotsApiSwagger13Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://aiaas.pandorabots.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    PandorabotsApiSwagger13Api apiInstance = new PandorabotsApiSwagger13Api(defaultClient);
    String appId = "appId_example"; // String | Your Application ID
    String botname = "botname_example"; // String | Name of the bot.
    String fileKind = "fileKind_example"; // String | Specify the type of file being retrieved: file (for AIML files), map, substitution, set
    String filename = "filename_example"; // String | Filename to retrieve. Note: for non-AIML files, do not include the file extension in the path.
    try {
      apiInstance.getBotFile1(appId, botname, fileKind, filename);
    } catch (ApiException e) {
      System.err.println("Exception when calling PandorabotsApiSwagger13Api#getBotFile1");
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
| **appId** | **String**| Your Application ID | |
| **botname** | **String**| Name of the bot. | |
| **fileKind** | **String**| Specify the type of file being retrieved: file (for AIML files), map, substitution, set | |
| **filename** | **String**| Filename to retrieve. Note: for non-AIML files, do not include the file extension in the path. | |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="getBotFile2"></a>
# **getBotFile2**
> getBotFile2(appId, botname, fileKind)

Retrieve a bot file (pdefaults, properties)

Retrieve pdefaults or properties bot file.&lt;p&gt;For malformed file-kind, a 404 error is returned. For invalid botname, a 400 error is returned. For unknown bot or file, a 412 error is returned.&lt;/p&gt;&lt;pre&gt;&lt;p&gt;curl -v -X GET &#39;https://aiaas.pandorabots.com/bot/APP_ID/BOTNAME/FILE-KIND?user_key&#x3D;USER_KEY&#39;&lt;/p&gt;&lt;/pre&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PandorabotsApiSwagger13Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://aiaas.pandorabots.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    PandorabotsApiSwagger13Api apiInstance = new PandorabotsApiSwagger13Api(defaultClient);
    String appId = "appId_example"; // String | Your Application ID
    String botname = "botname_example"; // String | Name of the bot.
    String fileKind = "fileKind_example"; // String | Specify the type of file being retrieved: pdefaults, properties
    try {
      apiInstance.getBotFile2(appId, botname, fileKind);
    } catch (ApiException e) {
      System.err.println("Exception when calling PandorabotsApiSwagger13Api#getBotFile2");
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
| **appId** | **String**| Your Application ID | |
| **botname** | **String**| Name of the bot. | |
| **fileKind** | **String**| Specify the type of file being retrieved: pdefaults, properties | |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="listBotFiles"></a>
# **listBotFiles**
> listBotFiles(appId, botname, _return)

List of bot files

Retrieve a list of a bot&#39;s files. Returns a JSON object with each bot file associated with bot specified.&lt;p&gt;Returns a 404 error code for bot not found. Returns a 401 error code for invalid app_ID, user_key, or referrer filter.&lt;/p&gt;&lt;p&gt;The &lt;code color&#x3D;blue&gt;return&#x3D;zip&lt;/code&gt; option may not behave as expected using Active Docs 1.2&lt;/p&gt;&lt;p&gt;&lt;pre class&#x3D;&#39;prettyprint&#39;&gt;curl -v  -X GET &#39;https://aiaas.pandorabots.com/bot/APP_ID/BOTNAME?user_key&#x3D;USER_KEY&#39;&lt;/pre&gt;&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PandorabotsApiSwagger13Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://aiaas.pandorabots.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    PandorabotsApiSwagger13Api apiInstance = new PandorabotsApiSwagger13Api(defaultClient);
    String appId = "appId_example"; // String | Your Application ID
    String botname = "botname_example"; // String | The name of the bot.
    String _return = "_return_example"; // String | If set to zip, a zip file with all bot files will be returned.
    try {
      apiInstance.listBotFiles(appId, botname, _return);
    } catch (ApiException e) {
      System.err.println("Exception when calling PandorabotsApiSwagger13Api#listBotFiles");
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
| **appId** | **String**| Your Application ID | |
| **botname** | **String**| The name of the bot. | |
| **_return** | **String**| If set to zip, a zip file with all bot files will be returned. | [optional] |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="listBots"></a>
# **listBots**
> listBots(appId)

List of bots

Retrieve a list of your application&#39;s bots. Response returns JSON object with info for each bot.&lt;p&gt;Returns a 401 error code for invalid app_ID or user_key, or if applicable, invalid referrer.&lt;/p&gt;&lt;p&gt;&lt;pre class&#x3D;&#39;prettyprint&#39;&gt;curl -v  -X GET &#39;https://aiaas.pandorabots.com/bot/APP_ID?user_key&#x3D;USER_KEY&#39;&lt;/pre&gt;&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PandorabotsApiSwagger13Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://aiaas.pandorabots.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    PandorabotsApiSwagger13Api apiInstance = new PandorabotsApiSwagger13Api(defaultClient);
    String appId = "appId_example"; // String | Your Application ID
    try {
      apiInstance.listBots(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PandorabotsApiSwagger13Api#listBots");
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
| **appId** | **String**| Your Application ID | |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="uploadFile1"></a>
# **uploadFile1**
> uploadFile1(appId, botname, fileKind, filename, content)

Upload a bot file (AIML, set, substitution, map)

Upload bot personality files to your bot. Files must be named with only lowercase letters and numbers with one of the following extensions: &lt;p&gt;&lt;b&gt;AIML: &lt;/b&gt;Extention - .aiml, file-kind - file&lt;/p&gt;&lt;p&gt;&lt;b&gt;Sets: &lt;/b&gt;Extension - .set, file-kind - set&lt;/p&gt;&lt;p&gt;&lt;b&gt;Maps: &lt;/b&gt;Extension - .map, file-kind - map&lt;/p&gt;&lt;p&gt;&lt;b&gt;Substitutions: &lt;/b&gt;Extension - .substitution, file-kind - substitution&lt;/p&gt;&lt;p&gt;The system will overwrite existing files with the file being uploaded.&lt;/p&gt;&lt;p&gt;If the request is malformed because the file name is invalid or malformed JSON for non-AIML files, a 400 error is returned. For malformed file-kind, a 404 error is returned. For invalid file or botname, a 412 error is returned. &lt;/p&gt;&lt;p&gt;If Active Doc spec is not working with this API, please use the following curl command examples:&lt;/p&gt;&lt;pre class&#x3D;&#39;prettyprint&#39;&gt;&lt;p&gt;curl -v -X PUT &#39;https://aiaas.pandorabots.com/bot/APP_ID/BOTNAME/file/foobot.aiml?user_key&#x3D;USER_KEY&#39;&lt;br/&gt;&amp;nbsp;&amp;nbsp;--data-binary @/home/foo/foobot.aiml&lt;/p&gt;&lt;/pre&gt;&lt;br/&gt;&lt;pre class&#x3D;&#39;prettyprint&#39;&gt;&lt;p&gt;curl -v -X PUT &#39;https://aiaas.pandorabots.com/bot/APP_ID/BOTNAME/set/colors?user_key&#x3D;USER_KEY&#39;&lt;br/&gt;&amp;nbsp;&amp;nbsp;--data-binary @/home/foo/colors.set&lt;/p&gt;&lt;/pre&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PandorabotsApiSwagger13Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://aiaas.pandorabots.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    PandorabotsApiSwagger13Api apiInstance = new PandorabotsApiSwagger13Api(defaultClient);
    String appId = "appId_example"; // String | Your Application ID
    String botname = "botname_example"; // String | Your bot's name
    String fileKind = "fileKind_example"; // String | Specify the type of file being uploaded: file (for AIML files), map, substitution, set
    String filename = "filename_example"; // String | Filename to upload, must be named with only lowercase letters and numbers. Note: for non-AIML files, do not include the file extension in the path.
    String content = "content_example"; // String | Type or Paste in file contents.
    try {
      apiInstance.uploadFile1(appId, botname, fileKind, filename, content);
    } catch (ApiException e) {
      System.err.println("Exception when calling PandorabotsApiSwagger13Api#uploadFile1");
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
| **appId** | **String**| Your Application ID | |
| **botname** | **String**| Your bot&#39;s name | |
| **fileKind** | **String**| Specify the type of file being uploaded: file (for AIML files), map, substitution, set | |
| **filename** | **String**| Filename to upload, must be named with only lowercase letters and numbers. Note: for non-AIML files, do not include the file extension in the path. | |
| **content** | **String**| Type or Paste in file contents. | |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="uploadFile2"></a>
# **uploadFile2**
> uploadFile2(appId, botname, fileKind, content)

Upload a bot file (pdefaults, properties)

Upload bot personality files to your bot. Files must be named with only lowercase letters and numbers with one of the following extensions: &lt;p&gt;&lt;b&gt;Properties: &lt;/b&gt;Extension - .properties, file-kind - properties, No filename required in path&lt;/p&gt;&lt;p&gt;&lt;b&gt;Predicate defaults: &lt;/b&gt;Extension - .pdefaults, file-kind - pdefaults, No filename required in path&lt;/p&gt;&lt;p&gt;The system will overwrite existing files with the file being uploaded.&lt;/p&gt;&lt;p&gt;For malformed JSON in non-AIML files, a 400 error is returned. For malformed file-kind, a 404 error is returned. For invalid file or botname, a 412 error is returned. &lt;/p&gt;&lt;p&gt;If Active Doc spec is not working with this API, please use the following curl command examples:&lt;/p&gt;&lt;pre class&#x3D;&#39;prettyprint&#39;&gt;&lt;p&gt;curl -v -X PUT &#39;https://aiaas.pandorabots.com/bot/APP_ID/BOTNAME/properties?user_key&#x3D;USER_KEY&#39;&lt;br/&gt;&amp;nbsp;&amp;nbsp;--data-binary @/home/foo/foobot.properties&lt;/p&gt;&lt;/pre&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PandorabotsApiSwagger13Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://aiaas.pandorabots.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    PandorabotsApiSwagger13Api apiInstance = new PandorabotsApiSwagger13Api(defaultClient);
    String appId = "appId_example"; // String | Your Application ID
    String botname = "botname_example"; // String | Your bot's name
    String fileKind = "fileKind_example"; // String | Specify the type of file being uploaded: pdefaults, properties
    String content = "content_example"; // String | Type or Paste in file contents.
    try {
      apiInstance.uploadFile2(appId, botname, fileKind, content);
    } catch (ApiException e) {
      System.err.println("Exception when calling PandorabotsApiSwagger13Api#uploadFile2");
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
| **appId** | **String**| Your Application ID | |
| **botname** | **String**| Your bot&#39;s name | |
| **fileKind** | **String**| Specify the type of file being uploaded: pdefaults, properties | |
| **content** | **String**| Type or Paste in file contents. | |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

