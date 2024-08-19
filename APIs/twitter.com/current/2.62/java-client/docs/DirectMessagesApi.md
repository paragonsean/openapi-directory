# DirectMessagesApi

All URIs are relative to *https://api.twitter.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dmConversationByIdEventIdCreate**](DirectMessagesApi.md#dmConversationByIdEventIdCreate) | **POST** /2/dm_conversations/{dm_conversation_id}/messages | Send a new message to a DM Conversation |
| [**dmConversationIdCreate**](DirectMessagesApi.md#dmConversationIdCreate) | **POST** /2/dm_conversations | Create a new DM Conversation |
| [**dmConversationWithUserEventIdCreate**](DirectMessagesApi.md#dmConversationWithUserEventIdCreate) | **POST** /2/dm_conversations/with/{participant_id}/messages | Send a new message to a user |
| [**getDmConversationsIdDmEvents**](DirectMessagesApi.md#getDmConversationsIdDmEvents) | **GET** /2/dm_conversations/{id}/dm_events | Get DM Events for a DM Conversation |
| [**getDmConversationsWithParticipantIdDmEvents**](DirectMessagesApi.md#getDmConversationsWithParticipantIdDmEvents) | **GET** /2/dm_conversations/with/{participant_id}/dm_events | Get DM Events for a DM Conversation |
| [**getDmEvents**](DirectMessagesApi.md#getDmEvents) | **GET** /2/dm_events | Get recent DM Events |


<a id="dmConversationByIdEventIdCreate"></a>
# **dmConversationByIdEventIdCreate**
> CreateDmEventResponse dmConversationByIdEventIdCreate(dmConversationId, createMessageRequest)

Send a new message to a DM Conversation

Creates a new message for a DM Conversation specified by DM Conversation ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectMessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twitter.com");
    
    // Configure OAuth2 access token for authorization: OAuth2UserToken
    OAuth OAuth2UserToken = (OAuth) defaultClient.getAuthentication("OAuth2UserToken");
    OAuth2UserToken.setAccessToken("YOUR ACCESS TOKEN");


    DirectMessagesApi apiInstance = new DirectMessagesApi(defaultClient);
    String dmConversationId = "dmConversationId_example"; // String | The DM Conversation ID.
    CreateMessageRequest createMessageRequest = new CreateMessageRequest(); // CreateMessageRequest | 
    try {
      CreateDmEventResponse result = apiInstance.dmConversationByIdEventIdCreate(dmConversationId, createMessageRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectMessagesApi#dmConversationByIdEventIdCreate");
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
| **dmConversationId** | **String**| The DM Conversation ID. | |
| **createMessageRequest** | [**CreateMessageRequest**](CreateMessageRequest.md)|  | [optional] |

### Return type

[**CreateDmEventResponse**](CreateDmEventResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The request has succeeded. |  -  |
| **0** | The request has failed. |  -  |

<a id="dmConversationIdCreate"></a>
# **dmConversationIdCreate**
> CreateDmEventResponse dmConversationIdCreate(createDmConversationRequest)

Create a new DM Conversation

Creates a new DM Conversation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectMessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twitter.com");
    
    // Configure OAuth2 access token for authorization: OAuth2UserToken
    OAuth OAuth2UserToken = (OAuth) defaultClient.getAuthentication("OAuth2UserToken");
    OAuth2UserToken.setAccessToken("YOUR ACCESS TOKEN");


    DirectMessagesApi apiInstance = new DirectMessagesApi(defaultClient);
    CreateDmConversationRequest createDmConversationRequest = new CreateDmConversationRequest(); // CreateDmConversationRequest | 
    try {
      CreateDmEventResponse result = apiInstance.dmConversationIdCreate(createDmConversationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectMessagesApi#dmConversationIdCreate");
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
| **createDmConversationRequest** | [**CreateDmConversationRequest**](CreateDmConversationRequest.md)|  | [optional] |

### Return type

[**CreateDmEventResponse**](CreateDmEventResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The request has succeeded. |  -  |
| **0** | The request has failed. |  -  |

<a id="dmConversationWithUserEventIdCreate"></a>
# **dmConversationWithUserEventIdCreate**
> CreateDmEventResponse dmConversationWithUserEventIdCreate(participantId, createMessageRequest)

Send a new message to a user

Creates a new message for a DM Conversation with a participant user by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectMessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twitter.com");
    
    // Configure OAuth2 access token for authorization: OAuth2UserToken
    OAuth OAuth2UserToken = (OAuth) defaultClient.getAuthentication("OAuth2UserToken");
    OAuth2UserToken.setAccessToken("YOUR ACCESS TOKEN");


    DirectMessagesApi apiInstance = new DirectMessagesApi(defaultClient);
    String participantId = "participantId_example"; // String | The ID of the recipient user that will receive the DM.
    CreateMessageRequest createMessageRequest = new CreateMessageRequest(); // CreateMessageRequest | 
    try {
      CreateDmEventResponse result = apiInstance.dmConversationWithUserEventIdCreate(participantId, createMessageRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectMessagesApi#dmConversationWithUserEventIdCreate");
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
| **participantId** | **String**| The ID of the recipient user that will receive the DM. | |
| **createMessageRequest** | [**CreateMessageRequest**](CreateMessageRequest.md)|  | [optional] |

### Return type

[**CreateDmEventResponse**](CreateDmEventResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The request has succeeded. |  -  |
| **0** | The request has failed. |  -  |

<a id="getDmConversationsIdDmEvents"></a>
# **getDmConversationsIdDmEvents**
> Get2DmConversationsIdDmEventsResponse getDmConversationsIdDmEvents(id, maxResults, paginationToken, eventTypes, dmEventFields, expansions, mediaFields, userFields, tweetFields)

Get DM Events for a DM Conversation

Returns DM Events for a DM Conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectMessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twitter.com");
    
    // Configure OAuth2 access token for authorization: OAuth2UserToken
    OAuth OAuth2UserToken = (OAuth) defaultClient.getAuthentication("OAuth2UserToken");
    OAuth2UserToken.setAccessToken("YOUR ACCESS TOKEN");


    DirectMessagesApi apiInstance = new DirectMessagesApi(defaultClient);
    String id = "id_example"; // String | The DM Conversation ID.
    Integer maxResults = 100; // Integer | The maximum number of results.
    String paginationToken = "paginationToken_example"; // String | This parameter is used to get a specified 'page' of results.
    Set<String> eventTypes = Arrays.asList(); // Set<String> | The set of event_types to include in the results.
    Set<String> dmEventFields = Arrays.asList(); // Set<String> | A comma separated list of DmEvent fields to display.
    Set<String> expansions = Arrays.asList(); // Set<String> | A comma separated list of fields to expand.
    Set<String> mediaFields = Arrays.asList(); // Set<String> | A comma separated list of Media fields to display.
    Set<String> userFields = Arrays.asList(); // Set<String> | A comma separated list of User fields to display.
    Set<String> tweetFields = Arrays.asList(); // Set<String> | A comma separated list of Tweet fields to display.
    try {
      Get2DmConversationsIdDmEventsResponse result = apiInstance.getDmConversationsIdDmEvents(id, maxResults, paginationToken, eventTypes, dmEventFields, expansions, mediaFields, userFields, tweetFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectMessagesApi#getDmConversationsIdDmEvents");
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
| **id** | **String**| The DM Conversation ID. | |
| **maxResults** | **Integer**| The maximum number of results. | [optional] [default to 100] |
| **paginationToken** | **String**| This parameter is used to get a specified &#39;page&#39; of results. | [optional] |
| **eventTypes** | [**Set&lt;String&gt;**](String.md)| The set of event_types to include in the results. | [optional] [enum: MessageCreate, ParticipantsJoin, ParticipantsLeave] |
| **dmEventFields** | [**Set&lt;String&gt;**](String.md)| A comma separated list of DmEvent fields to display. | [optional] [enum: attachments, created_at, dm_conversation_id, event_type, id, participant_ids, referenced_tweets, sender_id, text] |
| **expansions** | [**Set&lt;String&gt;**](String.md)| A comma separated list of fields to expand. | [optional] [enum: attachments.media_keys, participant_ids, referenced_tweets.id, sender_id] |
| **mediaFields** | [**Set&lt;String&gt;**](String.md)| A comma separated list of Media fields to display. | [optional] [enum: alt_text, duration_ms, height, media_key, non_public_metrics, organic_metrics, preview_image_url, promoted_metrics, public_metrics, type, url, variants, width] |
| **userFields** | [**Set&lt;String&gt;**](String.md)| A comma separated list of User fields to display. | [optional] [enum: created_at, description, entities, id, location, name, pinned_tweet_id, profile_image_url, protected, public_metrics, url, username, verified, verified_type, withheld] |
| **tweetFields** | [**Set&lt;String&gt;**](String.md)| A comma separated list of Tweet fields to display. | [optional] [enum: attachments, author_id, context_annotations, conversation_id, created_at, edit_controls, edit_history_tweet_ids, entities, geo, id, in_reply_to_user_id, lang, non_public_metrics, organic_metrics, possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets, reply_settings, source, text, withheld] |

### Return type

[**Get2DmConversationsIdDmEventsResponse**](Get2DmConversationsIdDmEventsResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request has succeeded. |  -  |
| **0** | The request has failed. |  -  |

<a id="getDmConversationsWithParticipantIdDmEvents"></a>
# **getDmConversationsWithParticipantIdDmEvents**
> Get2DmConversationsWithParticipantIdDmEventsResponse getDmConversationsWithParticipantIdDmEvents(participantId, maxResults, paginationToken, eventTypes, dmEventFields, expansions, mediaFields, userFields, tweetFields)

Get DM Events for a DM Conversation

Returns DM Events for a DM Conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectMessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twitter.com");
    
    // Configure OAuth2 access token for authorization: OAuth2UserToken
    OAuth OAuth2UserToken = (OAuth) defaultClient.getAuthentication("OAuth2UserToken");
    OAuth2UserToken.setAccessToken("YOUR ACCESS TOKEN");


    DirectMessagesApi apiInstance = new DirectMessagesApi(defaultClient);
    String participantId = "participantId_example"; // String | The ID of the participant user for the One to One DM conversation.
    Integer maxResults = 100; // Integer | The maximum number of results.
    String paginationToken = "paginationToken_example"; // String | This parameter is used to get a specified 'page' of results.
    Set<String> eventTypes = Arrays.asList(); // Set<String> | The set of event_types to include in the results.
    Set<String> dmEventFields = Arrays.asList(); // Set<String> | A comma separated list of DmEvent fields to display.
    Set<String> expansions = Arrays.asList(); // Set<String> | A comma separated list of fields to expand.
    Set<String> mediaFields = Arrays.asList(); // Set<String> | A comma separated list of Media fields to display.
    Set<String> userFields = Arrays.asList(); // Set<String> | A comma separated list of User fields to display.
    Set<String> tweetFields = Arrays.asList(); // Set<String> | A comma separated list of Tweet fields to display.
    try {
      Get2DmConversationsWithParticipantIdDmEventsResponse result = apiInstance.getDmConversationsWithParticipantIdDmEvents(participantId, maxResults, paginationToken, eventTypes, dmEventFields, expansions, mediaFields, userFields, tweetFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectMessagesApi#getDmConversationsWithParticipantIdDmEvents");
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
| **participantId** | **String**| The ID of the participant user for the One to One DM conversation. | |
| **maxResults** | **Integer**| The maximum number of results. | [optional] [default to 100] |
| **paginationToken** | **String**| This parameter is used to get a specified &#39;page&#39; of results. | [optional] |
| **eventTypes** | [**Set&lt;String&gt;**](String.md)| The set of event_types to include in the results. | [optional] [enum: MessageCreate, ParticipantsJoin, ParticipantsLeave] |
| **dmEventFields** | [**Set&lt;String&gt;**](String.md)| A comma separated list of DmEvent fields to display. | [optional] [enum: attachments, created_at, dm_conversation_id, event_type, id, participant_ids, referenced_tweets, sender_id, text] |
| **expansions** | [**Set&lt;String&gt;**](String.md)| A comma separated list of fields to expand. | [optional] [enum: attachments.media_keys, participant_ids, referenced_tweets.id, sender_id] |
| **mediaFields** | [**Set&lt;String&gt;**](String.md)| A comma separated list of Media fields to display. | [optional] [enum: alt_text, duration_ms, height, media_key, non_public_metrics, organic_metrics, preview_image_url, promoted_metrics, public_metrics, type, url, variants, width] |
| **userFields** | [**Set&lt;String&gt;**](String.md)| A comma separated list of User fields to display. | [optional] [enum: created_at, description, entities, id, location, name, pinned_tweet_id, profile_image_url, protected, public_metrics, url, username, verified, verified_type, withheld] |
| **tweetFields** | [**Set&lt;String&gt;**](String.md)| A comma separated list of Tweet fields to display. | [optional] [enum: attachments, author_id, context_annotations, conversation_id, created_at, edit_controls, edit_history_tweet_ids, entities, geo, id, in_reply_to_user_id, lang, non_public_metrics, organic_metrics, possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets, reply_settings, source, text, withheld] |

### Return type

[**Get2DmConversationsWithParticipantIdDmEventsResponse**](Get2DmConversationsWithParticipantIdDmEventsResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request has succeeded. |  -  |
| **0** | The request has failed. |  -  |

<a id="getDmEvents"></a>
# **getDmEvents**
> Get2DmEventsResponse getDmEvents(maxResults, paginationToken, eventTypes, dmEventFields, expansions, mediaFields, userFields, tweetFields)

Get recent DM Events

Returns recent DM Events across DM conversations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectMessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twitter.com");
    
    // Configure OAuth2 access token for authorization: OAuth2UserToken
    OAuth OAuth2UserToken = (OAuth) defaultClient.getAuthentication("OAuth2UserToken");
    OAuth2UserToken.setAccessToken("YOUR ACCESS TOKEN");


    DirectMessagesApi apiInstance = new DirectMessagesApi(defaultClient);
    Integer maxResults = 100; // Integer | The maximum number of results.
    String paginationToken = "paginationToken_example"; // String | This parameter is used to get a specified 'page' of results.
    Set<String> eventTypes = Arrays.asList(); // Set<String> | The set of event_types to include in the results.
    Set<String> dmEventFields = Arrays.asList(); // Set<String> | A comma separated list of DmEvent fields to display.
    Set<String> expansions = Arrays.asList(); // Set<String> | A comma separated list of fields to expand.
    Set<String> mediaFields = Arrays.asList(); // Set<String> | A comma separated list of Media fields to display.
    Set<String> userFields = Arrays.asList(); // Set<String> | A comma separated list of User fields to display.
    Set<String> tweetFields = Arrays.asList(); // Set<String> | A comma separated list of Tweet fields to display.
    try {
      Get2DmEventsResponse result = apiInstance.getDmEvents(maxResults, paginationToken, eventTypes, dmEventFields, expansions, mediaFields, userFields, tweetFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectMessagesApi#getDmEvents");
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
| **maxResults** | **Integer**| The maximum number of results. | [optional] [default to 100] |
| **paginationToken** | **String**| This parameter is used to get a specified &#39;page&#39; of results. | [optional] |
| **eventTypes** | [**Set&lt;String&gt;**](String.md)| The set of event_types to include in the results. | [optional] [enum: MessageCreate, ParticipantsJoin, ParticipantsLeave] |
| **dmEventFields** | [**Set&lt;String&gt;**](String.md)| A comma separated list of DmEvent fields to display. | [optional] [enum: attachments, created_at, dm_conversation_id, event_type, id, participant_ids, referenced_tweets, sender_id, text] |
| **expansions** | [**Set&lt;String&gt;**](String.md)| A comma separated list of fields to expand. | [optional] [enum: attachments.media_keys, participant_ids, referenced_tweets.id, sender_id] |
| **mediaFields** | [**Set&lt;String&gt;**](String.md)| A comma separated list of Media fields to display. | [optional] [enum: alt_text, duration_ms, height, media_key, non_public_metrics, organic_metrics, preview_image_url, promoted_metrics, public_metrics, type, url, variants, width] |
| **userFields** | [**Set&lt;String&gt;**](String.md)| A comma separated list of User fields to display. | [optional] [enum: created_at, description, entities, id, location, name, pinned_tweet_id, profile_image_url, protected, public_metrics, url, username, verified, verified_type, withheld] |
| **tweetFields** | [**Set&lt;String&gt;**](String.md)| A comma separated list of Tweet fields to display. | [optional] [enum: attachments, author_id, context_annotations, conversation_id, created_at, edit_controls, edit_history_tweet_ids, entities, geo, id, in_reply_to_user_id, lang, non_public_metrics, organic_metrics, possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets, reply_settings, source, text, withheld] |

### Return type

[**Get2DmEventsResponse**](Get2DmEventsResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request has succeeded. |  -  |
| **0** | The request has failed. |  -  |

