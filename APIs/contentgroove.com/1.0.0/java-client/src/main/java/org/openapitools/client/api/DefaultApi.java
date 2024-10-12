/*
 * ContentGroove API
 * # Overview  The ContentGroove Developer API enables you to add the power of ContentGroove's video AI to your own applications and workflows.  Webhooks are a way for ContentGroove to send video information to your application, to update your system and/or trigger other business processes.  You can use Webhooks and the Developer API separately or together.  # Getting Started with Webhooks  - Sign up for an account at [app.contentgroove.com](https://app.contentgroove.com) - Read \"Using Webhooks\" on the [API Reference page](https://developers.contentgroove.com/api_reference) - Visit the [Webhooks page](https://app.contentgroove.com/webhook_subscriptions) and create a new webhook  # Using Webhooks  Webhooks, also known as callbacks, are a way for ContentGroove to notify your application as soon as possible after an event has occurred in ContentGroove. For example after a media completes processing, ContentGroove can use a webhook to notify your application with information about the video: Suggested clips, transcription, and so on. You can use the information sent to update your system and/or use the webhook to trigger other business processes.  The webhook request is sent as an HTTP POST containing a payload of JSON-formatted data. For the details of the payload format see the \"CALLBACKS\" sections below.  When your application receives the webhook request, it must respond with a 200 HTTP status code (success). If a 200 HTTP status code is not returned, ContentGroove will assume that the webhook was not delivered and will retry a limited number of times, using an exponential backoff algorithm.  ContentGroove makes a best effort to attempt to send the webhook at least once. Applications receiving webhooks must tolerate the possibility of a single webhook payload being sent more than once (idempotent behavior). Applications receiving webhooks should tolerate the possibility that a webhook could not be delivered (for example your application was down when delivery was attempted).  # Getting Started with the Developer API  - Sign up for an account at [app.contentgroove.com](https://app.contentgroove.com) - Visit the [API Keys page](https://app.contentgroove.com/api_keys)   - Create a new API Key then copy and save the value.     > ⚠️ **IMPORTANT**: This API Key is intended only for use on the server side. Be sure never to use a server-side API Key in client-side (web, mobile, or otherwise) code. ⚠️ - View all available endpoints, and try the API, on our [API Reference page](https://developers.contentgroove.com/api_reference)  # Using the Developer API  - Create a new media (video or audio) in ContentGroove   - If the video or audio is available from a URL, you can create a media by providing the `source_url` parameter. ContentGroove will fetch the video or audio from the URL if possible.   - Or, you can create a media from a video or audio file which you upload directly to ContentGroove (see File Uploading section below). - After the new media is created, at first it will be in a \"processing\" state.   Depending on the size and duration of the video or audio file, it will take some time for processing to complete.   - You can use ContentGroove Webhooks to be notified immediately when processing has completed. (Details coming soon.)   - You can also use the API to read the state of the media, to determine if the media has completed processing yet. - After the media has completed processing, you can access all of these details about the media:   - The media name and description   - The transcription of spoken words   - Topics and keywords which were discussed in the transcription   - Suggested video clips are automatically created - In addition to the automatically created video clips, you can create more video clips from the media  # Response Codes  The following is a comprehensive list of the status codes you may receive while using the ContentGroove API:  - 200 \"Ok\"   - The request was valid - 400 \"Bad Request   - This is returned when there was a problem parsing the JSON body of your request if you supplied the 'Content-Type': 'application/json' header, or if your request is missing the 'Content-Type' header altogether - 401 \"Unauthorized\"   - This is returned when you are attempting to perform an action on a resource that you are not authorized to do - 402 \"Payment Required\"   - This is returned when you are attempting to perform an action that would push your account above a usage limit. You can view your usage at: https://app.contentgroove.com/quota_usage - 404 \"Not Found\"   - This is returned when the resource you are trying to view does not exist - 429 \"Too Many Requests\"   - This is returned when you have performed too many requests within a given period of time - 500 \"Internal Server Error\"   - This is returned when your request was valid but there was a problem on our end  # File Uploading  - Step 1: Make a GET request to the direct uploads URL endpoint (/api/v1/direct_uploads) to receive an upload URL to upload the file to and an upload id. - Step 2: Make a PUT request with the file as the body to the upload URL received in step 1. The response will have a 200 status with no body if the upload is successful.   ```   curl -T /path/to/file upload_url   ``` - Step 3: After uploading the file to the upload URL, make a POST request to the create medias endpoint (/api/v1/medias), with the upload id and optionally a name and description for the new media.   > At this time, file uploads are limited to 5gb per file.  # Allowed media types  Video:  - Supported: Most common video formats and codecs are supported. - Recommended: mp4  Audio:  - Supported: aac, mp3, flac, ogg, wav, and wma - Recommended: aac  # Authentication  You can use the API Key to authenticate your API requests using any of these methods. (Replace abc123 with your actual API Key.)  - Request header `Authorization: Bearer abc123` - Request header `X-API-KEY: abc123` - Query parameter `api_key=abc123`   > ⚠️ **IMPORTANT**: This API Key is intended only for use on the server side. Be sure never to use a server-side API Key in client-side (web, mobile, or otherwise) code. ⚠️  # Link to openapi.json spec  - https://api.contentgroove.com/api-docs/v1/openapi.json 
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiCallback;
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.Pair;
import org.openapitools.client.ProgressRequestBody;
import org.openapitools.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


import org.openapitools.client.model.ClipResponseObject;
import org.openapitools.client.model.ClipsResponseObject;
import org.openapitools.client.model.CreateClipRequest;
import org.openapitools.client.model.CreateMediaRequest;
import org.openapitools.client.model.CreateWebhookSubscriptionRequest;
import org.openapitools.client.model.DirectUploadResponseObject;
import org.openapitools.client.model.MediaResponseObject;
import org.openapitools.client.model.MediasResponseObject;
import org.openapitools.client.model.PaymentRequiredErrorResponseObject;
import org.openapitools.client.model.TooManyRequestsErrorResponseObject;
import org.openapitools.client.model.UnauthorizedErrorResponseObject;
import org.openapitools.client.model.UpdateClipByIdRequest;
import org.openapitools.client.model.UpdateMediaByIdRequest;
import org.openapitools.client.model.WebhookSubscriptionResponseObject;
import org.openapitools.client.model.WebhookSubscriptionsResponseObject;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DefaultApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public DefaultApi() {
        this(Configuration.getDefaultApiClient());
    }

    public DefaultApi(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return localVarApiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public int getHostIndex() {
        return localHostIndex;
    }

    public void setHostIndex(int hostIndex) {
        this.localHostIndex = hostIndex;
    }

    public String getCustomBaseUrl() {
        return localCustomBaseUrl;
    }

    public void setCustomBaseUrl(String customBaseUrl) {
        this.localCustomBaseUrl = customBaseUrl;
    }

    /**
     * Build call for createClip
     * @param createClipRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> payment required </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createClipCall(CreateClipRequest createClipRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = createClipRequest;

        // create path and map variables
        String localVarPath = "/clips";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "BearerHeader" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call createClipValidateBeforeCall(CreateClipRequest createClipRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'createClipRequest' is set
        if (createClipRequest == null) {
            throw new ApiException("Missing the required parameter 'createClipRequest' when calling createClip(Async)");
        }

        return createClipCall(createClipRequest, _callback);

    }

    /**
     * create clip
     * 
     * @param createClipRequest  (required)
     * @return ClipResponseObject
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> payment required </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public ClipResponseObject createClip(CreateClipRequest createClipRequest) throws ApiException {
        ApiResponse<ClipResponseObject> localVarResp = createClipWithHttpInfo(createClipRequest);
        return localVarResp.getData();
    }

    /**
     * create clip
     * 
     * @param createClipRequest  (required)
     * @return ApiResponse&lt;ClipResponseObject&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> payment required </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ClipResponseObject> createClipWithHttpInfo(CreateClipRequest createClipRequest) throws ApiException {
        okhttp3.Call localVarCall = createClipValidateBeforeCall(createClipRequest, null);
        Type localVarReturnType = new TypeToken<ClipResponseObject>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * create clip (asynchronously)
     * 
     * @param createClipRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> payment required </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createClipAsync(CreateClipRequest createClipRequest, final ApiCallback<ClipResponseObject> _callback) throws ApiException {

        okhttp3.Call localVarCall = createClipValidateBeforeCall(createClipRequest, _callback);
        Type localVarReturnType = new TypeToken<ClipResponseObject>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createMedia
     * @param createMediaRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> payment required </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createMediaCall(CreateMediaRequest createMediaRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = createMediaRequest;

        // create path and map variables
        String localVarPath = "/medias";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "BearerHeader" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call createMediaValidateBeforeCall(CreateMediaRequest createMediaRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'createMediaRequest' is set
        if (createMediaRequest == null) {
            throw new ApiException("Missing the required parameter 'createMediaRequest' when calling createMedia(Async)");
        }

        return createMediaCall(createMediaRequest, _callback);

    }

    /**
     * create media
     * 
     * @param createMediaRequest  (required)
     * @return MediaResponseObject
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> payment required </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public MediaResponseObject createMedia(CreateMediaRequest createMediaRequest) throws ApiException {
        ApiResponse<MediaResponseObject> localVarResp = createMediaWithHttpInfo(createMediaRequest);
        return localVarResp.getData();
    }

    /**
     * create media
     * 
     * @param createMediaRequest  (required)
     * @return ApiResponse&lt;MediaResponseObject&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> payment required </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<MediaResponseObject> createMediaWithHttpInfo(CreateMediaRequest createMediaRequest) throws ApiException {
        okhttp3.Call localVarCall = createMediaValidateBeforeCall(createMediaRequest, null);
        Type localVarReturnType = new TypeToken<MediaResponseObject>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * create media (asynchronously)
     * 
     * @param createMediaRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> payment required </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createMediaAsync(CreateMediaRequest createMediaRequest, final ApiCallback<MediaResponseObject> _callback) throws ApiException {

        okhttp3.Call localVarCall = createMediaValidateBeforeCall(createMediaRequest, _callback);
        Type localVarReturnType = new TypeToken<MediaResponseObject>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createWebhookSubscription
     * @param createWebhookSubscriptionRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createWebhookSubscriptionCall(CreateWebhookSubscriptionRequest createWebhookSubscriptionRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = createWebhookSubscriptionRequest;

        // create path and map variables
        String localVarPath = "/webhook_subscriptions";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "BearerHeader" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call createWebhookSubscriptionValidateBeforeCall(CreateWebhookSubscriptionRequest createWebhookSubscriptionRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'createWebhookSubscriptionRequest' is set
        if (createWebhookSubscriptionRequest == null) {
            throw new ApiException("Missing the required parameter 'createWebhookSubscriptionRequest' when calling createWebhookSubscription(Async)");
        }

        return createWebhookSubscriptionCall(createWebhookSubscriptionRequest, _callback);

    }

    /**
     * create webhook subscription
     * 
     * @param createWebhookSubscriptionRequest  (required)
     * @return WebhookSubscriptionResponseObject
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public WebhookSubscriptionResponseObject createWebhookSubscription(CreateWebhookSubscriptionRequest createWebhookSubscriptionRequest) throws ApiException {
        ApiResponse<WebhookSubscriptionResponseObject> localVarResp = createWebhookSubscriptionWithHttpInfo(createWebhookSubscriptionRequest);
        return localVarResp.getData();
    }

    /**
     * create webhook subscription
     * 
     * @param createWebhookSubscriptionRequest  (required)
     * @return ApiResponse&lt;WebhookSubscriptionResponseObject&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<WebhookSubscriptionResponseObject> createWebhookSubscriptionWithHttpInfo(CreateWebhookSubscriptionRequest createWebhookSubscriptionRequest) throws ApiException {
        okhttp3.Call localVarCall = createWebhookSubscriptionValidateBeforeCall(createWebhookSubscriptionRequest, null);
        Type localVarReturnType = new TypeToken<WebhookSubscriptionResponseObject>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * create webhook subscription (asynchronously)
     * 
     * @param createWebhookSubscriptionRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createWebhookSubscriptionAsync(CreateWebhookSubscriptionRequest createWebhookSubscriptionRequest, final ApiCallback<WebhookSubscriptionResponseObject> _callback) throws ApiException {

        okhttp3.Call localVarCall = createWebhookSubscriptionValidateBeforeCall(createWebhookSubscriptionRequest, _callback);
        Type localVarReturnType = new TypeToken<WebhookSubscriptionResponseObject>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteClipById
     * @param id The id of the clip to be retrieved (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> no content </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteClipByIdCall(String id, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/clips/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "BearerHeader" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteClipByIdValidateBeforeCall(String id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling deleteClipById(Async)");
        }

        return deleteClipByIdCall(id, _callback);

    }

    /**
     * delete clip
     * 
     * @param id The id of the clip to be retrieved (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> no content </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public void deleteClipById(String id) throws ApiException {
        deleteClipByIdWithHttpInfo(id);
    }

    /**
     * delete clip
     * 
     * @param id The id of the clip to be retrieved (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> no content </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteClipByIdWithHttpInfo(String id) throws ApiException {
        okhttp3.Call localVarCall = deleteClipByIdValidateBeforeCall(id, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * delete clip (asynchronously)
     * 
     * @param id The id of the clip to be retrieved (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> no content </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteClipByIdAsync(String id, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteClipByIdValidateBeforeCall(id, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteMediaById
     * @param id id (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> no content </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteMediaByIdCall(String id, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/medias/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "BearerHeader" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteMediaByIdValidateBeforeCall(String id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling deleteMediaById(Async)");
        }

        return deleteMediaByIdCall(id, _callback);

    }

    /**
     * delete media
     * 
     * @param id id (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> no content </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public void deleteMediaById(String id) throws ApiException {
        deleteMediaByIdWithHttpInfo(id);
    }

    /**
     * delete media
     * 
     * @param id id (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> no content </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteMediaByIdWithHttpInfo(String id) throws ApiException {
        okhttp3.Call localVarCall = deleteMediaByIdValidateBeforeCall(id, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * delete media (asynchronously)
     * 
     * @param id id (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> no content </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteMediaByIdAsync(String id, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteMediaByIdValidateBeforeCall(id, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteWebhookSubscriptionById
     * @param id The id of the webhook subscription to be retrieved (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> no content </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteWebhookSubscriptionByIdCall(String id, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/webhook_subscriptions/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "BearerHeader" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteWebhookSubscriptionByIdValidateBeforeCall(String id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling deleteWebhookSubscriptionById(Async)");
        }

        return deleteWebhookSubscriptionByIdCall(id, _callback);

    }

    /**
     * delete webhook subscription
     * 
     * @param id The id of the webhook subscription to be retrieved (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> no content </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public void deleteWebhookSubscriptionById(String id) throws ApiException {
        deleteWebhookSubscriptionByIdWithHttpInfo(id);
    }

    /**
     * delete webhook subscription
     * 
     * @param id The id of the webhook subscription to be retrieved (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> no content </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteWebhookSubscriptionByIdWithHttpInfo(String id) throws ApiException {
        okhttp3.Call localVarCall = deleteWebhookSubscriptionByIdValidateBeforeCall(id, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * delete webhook subscription (asynchronously)
     * 
     * @param id The id of the webhook subscription to be retrieved (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> no content </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteWebhookSubscriptionByIdAsync(String id, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteWebhookSubscriptionByIdValidateBeforeCall(id, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getClipById
     * @param id The id of the clip to be retrieved (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getClipByIdCall(String id, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/clips/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "BearerHeader" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getClipByIdValidateBeforeCall(String id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getClipById(Async)");
        }

        return getClipByIdCall(id, _callback);

    }

    /**
     * show clip
     * 
     * @param id The id of the clip to be retrieved (required)
     * @return ClipResponseObject
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public ClipResponseObject getClipById(String id) throws ApiException {
        ApiResponse<ClipResponseObject> localVarResp = getClipByIdWithHttpInfo(id);
        return localVarResp.getData();
    }

    /**
     * show clip
     * 
     * @param id The id of the clip to be retrieved (required)
     * @return ApiResponse&lt;ClipResponseObject&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ClipResponseObject> getClipByIdWithHttpInfo(String id) throws ApiException {
        okhttp3.Call localVarCall = getClipByIdValidateBeforeCall(id, null);
        Type localVarReturnType = new TypeToken<ClipResponseObject>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * show clip (asynchronously)
     * 
     * @param id The id of the clip to be retrieved (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getClipByIdAsync(String id, final ApiCallback<ClipResponseObject> _callback) throws ApiException {

        okhttp3.Call localVarCall = getClipByIdValidateBeforeCall(id, _callback);
        Type localVarReturnType = new TypeToken<ClipResponseObject>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getClips
     * @param filter Filters to be applied to the query.  Query params in the url must look like this: \&quot;filter[attributeName_*matcher*]\&quot;  (i.e. filter[name_eq]&#x3D;chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/   (optional)
     * @param page Specify page number and page size for the query (optional)
     * @param sort Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getClipsCall(Object filter, Object page, String sort, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/clips";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (filter != null) {
            localVarQueryParams.addAll(localVarApiClient.freeFormParameterToPairs(filter));
        }

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.freeFormParameterToPairs(page));
        }

        if (sort != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sort", sort));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "BearerHeader" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getClipsValidateBeforeCall(Object filter, Object page, String sort, final ApiCallback _callback) throws ApiException {
        return getClipsCall(filter, page, sort, _callback);

    }

    /**
     * list clips
     * 
     * @param filter Filters to be applied to the query.  Query params in the url must look like this: \&quot;filter[attributeName_*matcher*]\&quot;  (i.e. filter[name_eq]&#x3D;chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/   (optional)
     * @param page Specify page number and page size for the query (optional)
     * @param sort Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting (optional)
     * @return ClipsResponseObject
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public ClipsResponseObject getClips(Object filter, Object page, String sort) throws ApiException {
        ApiResponse<ClipsResponseObject> localVarResp = getClipsWithHttpInfo(filter, page, sort);
        return localVarResp.getData();
    }

    /**
     * list clips
     * 
     * @param filter Filters to be applied to the query.  Query params in the url must look like this: \&quot;filter[attributeName_*matcher*]\&quot;  (i.e. filter[name_eq]&#x3D;chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/   (optional)
     * @param page Specify page number and page size for the query (optional)
     * @param sort Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting (optional)
     * @return ApiResponse&lt;ClipsResponseObject&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ClipsResponseObject> getClipsWithHttpInfo(Object filter, Object page, String sort) throws ApiException {
        okhttp3.Call localVarCall = getClipsValidateBeforeCall(filter, page, sort, null);
        Type localVarReturnType = new TypeToken<ClipsResponseObject>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * list clips (asynchronously)
     * 
     * @param filter Filters to be applied to the query.  Query params in the url must look like this: \&quot;filter[attributeName_*matcher*]\&quot;  (i.e. filter[name_eq]&#x3D;chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/   (optional)
     * @param page Specify page number and page size for the query (optional)
     * @param sort Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getClipsAsync(Object filter, Object page, String sort, final ApiCallback<ClipsResponseObject> _callback) throws ApiException {

        okhttp3.Call localVarCall = getClipsValidateBeforeCall(filter, page, sort, _callback);
        Type localVarReturnType = new TypeToken<ClipsResponseObject>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getMediaById
     * @param id id (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getMediaByIdCall(String id, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/medias/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "BearerHeader" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getMediaByIdValidateBeforeCall(String id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getMediaById(Async)");
        }

        return getMediaByIdCall(id, _callback);

    }

    /**
     * show media
     * 
     * @param id id (required)
     * @return MediaResponseObject
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public MediaResponseObject getMediaById(String id) throws ApiException {
        ApiResponse<MediaResponseObject> localVarResp = getMediaByIdWithHttpInfo(id);
        return localVarResp.getData();
    }

    /**
     * show media
     * 
     * @param id id (required)
     * @return ApiResponse&lt;MediaResponseObject&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<MediaResponseObject> getMediaByIdWithHttpInfo(String id) throws ApiException {
        okhttp3.Call localVarCall = getMediaByIdValidateBeforeCall(id, null);
        Type localVarReturnType = new TypeToken<MediaResponseObject>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * show media (asynchronously)
     * 
     * @param id id (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getMediaByIdAsync(String id, final ApiCallback<MediaResponseObject> _callback) throws ApiException {

        okhttp3.Call localVarCall = getMediaByIdValidateBeforeCall(id, _callback);
        Type localVarReturnType = new TypeToken<MediaResponseObject>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getMedias
     * @param filter Filters to be applied to the query.  Query params in the url must look like this: \&quot;filter[attributeName_*matcher*]\&quot;  (i.e. filter[name_eq]&#x3D;chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/   (optional)
     * @param page Specify page number and page size for the query (optional)
     * @param sort Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getMediasCall(Object filter, Object page, String sort, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/medias";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (filter != null) {
            localVarQueryParams.addAll(localVarApiClient.freeFormParameterToPairs(filter));
        }

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.freeFormParameterToPairs(page));
        }

        if (sort != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sort", sort));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "BearerHeader" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getMediasValidateBeforeCall(Object filter, Object page, String sort, final ApiCallback _callback) throws ApiException {
        return getMediasCall(filter, page, sort, _callback);

    }

    /**
     * list medias
     * 
     * @param filter Filters to be applied to the query.  Query params in the url must look like this: \&quot;filter[attributeName_*matcher*]\&quot;  (i.e. filter[name_eq]&#x3D;chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/   (optional)
     * @param page Specify page number and page size for the query (optional)
     * @param sort Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting (optional)
     * @return MediasResponseObject
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public MediasResponseObject getMedias(Object filter, Object page, String sort) throws ApiException {
        ApiResponse<MediasResponseObject> localVarResp = getMediasWithHttpInfo(filter, page, sort);
        return localVarResp.getData();
    }

    /**
     * list medias
     * 
     * @param filter Filters to be applied to the query.  Query params in the url must look like this: \&quot;filter[attributeName_*matcher*]\&quot;  (i.e. filter[name_eq]&#x3D;chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/   (optional)
     * @param page Specify page number and page size for the query (optional)
     * @param sort Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting (optional)
     * @return ApiResponse&lt;MediasResponseObject&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<MediasResponseObject> getMediasWithHttpInfo(Object filter, Object page, String sort) throws ApiException {
        okhttp3.Call localVarCall = getMediasValidateBeforeCall(filter, page, sort, null);
        Type localVarReturnType = new TypeToken<MediasResponseObject>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * list medias (asynchronously)
     * 
     * @param filter Filters to be applied to the query.  Query params in the url must look like this: \&quot;filter[attributeName_*matcher*]\&quot;  (i.e. filter[name_eq]&#x3D;chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/   (optional)
     * @param page Specify page number and page size for the query (optional)
     * @param sort Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getMediasAsync(Object filter, Object page, String sort, final ApiCallback<MediasResponseObject> _callback) throws ApiException {

        okhttp3.Call localVarCall = getMediasValidateBeforeCall(filter, page, sort, _callback);
        Type localVarReturnType = new TypeToken<MediasResponseObject>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getUploadUrl
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getUploadUrlCall(final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/direct_uploads";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "BearerHeader" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getUploadUrlValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return getUploadUrlCall(_callback);

    }

    /**
     * prepare presigned upload url
     * 
     * @return DirectUploadResponseObject
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public DirectUploadResponseObject getUploadUrl() throws ApiException {
        ApiResponse<DirectUploadResponseObject> localVarResp = getUploadUrlWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * prepare presigned upload url
     * 
     * @return ApiResponse&lt;DirectUploadResponseObject&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DirectUploadResponseObject> getUploadUrlWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getUploadUrlValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<DirectUploadResponseObject>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * prepare presigned upload url (asynchronously)
     * 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getUploadUrlAsync(final ApiCallback<DirectUploadResponseObject> _callback) throws ApiException {

        okhttp3.Call localVarCall = getUploadUrlValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<DirectUploadResponseObject>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getWebhookSubscriptionById
     * @param id The id of the webhook subscription to be retrieved (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getWebhookSubscriptionByIdCall(String id, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/webhook_subscriptions/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "BearerHeader" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getWebhookSubscriptionByIdValidateBeforeCall(String id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getWebhookSubscriptionById(Async)");
        }

        return getWebhookSubscriptionByIdCall(id, _callback);

    }

    /**
     * show webhook subscription
     * 
     * @param id The id of the webhook subscription to be retrieved (required)
     * @return WebhookSubscriptionResponseObject
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public WebhookSubscriptionResponseObject getWebhookSubscriptionById(String id) throws ApiException {
        ApiResponse<WebhookSubscriptionResponseObject> localVarResp = getWebhookSubscriptionByIdWithHttpInfo(id);
        return localVarResp.getData();
    }

    /**
     * show webhook subscription
     * 
     * @param id The id of the webhook subscription to be retrieved (required)
     * @return ApiResponse&lt;WebhookSubscriptionResponseObject&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<WebhookSubscriptionResponseObject> getWebhookSubscriptionByIdWithHttpInfo(String id) throws ApiException {
        okhttp3.Call localVarCall = getWebhookSubscriptionByIdValidateBeforeCall(id, null);
        Type localVarReturnType = new TypeToken<WebhookSubscriptionResponseObject>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * show webhook subscription (asynchronously)
     * 
     * @param id The id of the webhook subscription to be retrieved (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> not found </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getWebhookSubscriptionByIdAsync(String id, final ApiCallback<WebhookSubscriptionResponseObject> _callback) throws ApiException {

        okhttp3.Call localVarCall = getWebhookSubscriptionByIdValidateBeforeCall(id, _callback);
        Type localVarReturnType = new TypeToken<WebhookSubscriptionResponseObject>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getWebhookSubscriptions
     * @param filter Filters to be applied to the query.  Query params in the url must look like this: \&quot;filter[attributeName_*matcher*]\&quot;  (i.e. filter[name_eq]&#x3D;chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/   (optional)
     * @param sort Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getWebhookSubscriptionsCall(Object filter, String sort, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/webhook_subscriptions";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (filter != null) {
            localVarQueryParams.addAll(localVarApiClient.freeFormParameterToPairs(filter));
        }

        if (sort != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sort", sort));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "BearerHeader" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getWebhookSubscriptionsValidateBeforeCall(Object filter, String sort, final ApiCallback _callback) throws ApiException {
        return getWebhookSubscriptionsCall(filter, sort, _callback);

    }

    /**
     * list webhook subscriptions
     * 
     * @param filter Filters to be applied to the query.  Query params in the url must look like this: \&quot;filter[attributeName_*matcher*]\&quot;  (i.e. filter[name_eq]&#x3D;chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/   (optional)
     * @param sort Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting (optional)
     * @return WebhookSubscriptionsResponseObject
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public WebhookSubscriptionsResponseObject getWebhookSubscriptions(Object filter, String sort) throws ApiException {
        ApiResponse<WebhookSubscriptionsResponseObject> localVarResp = getWebhookSubscriptionsWithHttpInfo(filter, sort);
        return localVarResp.getData();
    }

    /**
     * list webhook subscriptions
     * 
     * @param filter Filters to be applied to the query.  Query params in the url must look like this: \&quot;filter[attributeName_*matcher*]\&quot;  (i.e. filter[name_eq]&#x3D;chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/   (optional)
     * @param sort Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting (optional)
     * @return ApiResponse&lt;WebhookSubscriptionsResponseObject&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<WebhookSubscriptionsResponseObject> getWebhookSubscriptionsWithHttpInfo(Object filter, String sort) throws ApiException {
        okhttp3.Call localVarCall = getWebhookSubscriptionsValidateBeforeCall(filter, sort, null);
        Type localVarReturnType = new TypeToken<WebhookSubscriptionsResponseObject>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * list webhook subscriptions (asynchronously)
     * 
     * @param filter Filters to be applied to the query.  Query params in the url must look like this: \&quot;filter[attributeName_*matcher*]\&quot;  (i.e. filter[name_eq]&#x3D;chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/   (optional)
     * @param sort Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> unauthorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getWebhookSubscriptionsAsync(Object filter, String sort, final ApiCallback<WebhookSubscriptionsResponseObject> _callback) throws ApiException {

        okhttp3.Call localVarCall = getWebhookSubscriptionsValidateBeforeCall(filter, sort, _callback);
        Type localVarReturnType = new TypeToken<WebhookSubscriptionsResponseObject>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateClipById
     * @param id The id of the clip to be retrieved (required)
     * @param updateClipByIdRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateClipByIdCall(String id, UpdateClipByIdRequest updateClipByIdRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = updateClipByIdRequest;

        // create path and map variables
        String localVarPath = "/clips/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "BearerHeader" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updateClipByIdValidateBeforeCall(String id, UpdateClipByIdRequest updateClipByIdRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling updateClipById(Async)");
        }

        // verify the required parameter 'updateClipByIdRequest' is set
        if (updateClipByIdRequest == null) {
            throw new ApiException("Missing the required parameter 'updateClipByIdRequest' when calling updateClipById(Async)");
        }

        return updateClipByIdCall(id, updateClipByIdRequest, _callback);

    }

    /**
     * update clip
     * 
     * @param id The id of the clip to be retrieved (required)
     * @param updateClipByIdRequest  (required)
     * @return ClipResponseObject
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public ClipResponseObject updateClipById(String id, UpdateClipByIdRequest updateClipByIdRequest) throws ApiException {
        ApiResponse<ClipResponseObject> localVarResp = updateClipByIdWithHttpInfo(id, updateClipByIdRequest);
        return localVarResp.getData();
    }

    /**
     * update clip
     * 
     * @param id The id of the clip to be retrieved (required)
     * @param updateClipByIdRequest  (required)
     * @return ApiResponse&lt;ClipResponseObject&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ClipResponseObject> updateClipByIdWithHttpInfo(String id, UpdateClipByIdRequest updateClipByIdRequest) throws ApiException {
        okhttp3.Call localVarCall = updateClipByIdValidateBeforeCall(id, updateClipByIdRequest, null);
        Type localVarReturnType = new TypeToken<ClipResponseObject>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * update clip (asynchronously)
     * 
     * @param id The id of the clip to be retrieved (required)
     * @param updateClipByIdRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateClipByIdAsync(String id, UpdateClipByIdRequest updateClipByIdRequest, final ApiCallback<ClipResponseObject> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateClipByIdValidateBeforeCall(id, updateClipByIdRequest, _callback);
        Type localVarReturnType = new TypeToken<ClipResponseObject>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateMediaById
     * @param id id (required)
     * @param updateMediaByIdRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateMediaByIdCall(String id, UpdateMediaByIdRequest updateMediaByIdRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = updateMediaByIdRequest;

        // create path and map variables
        String localVarPath = "/medias/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "BearerHeader" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updateMediaByIdValidateBeforeCall(String id, UpdateMediaByIdRequest updateMediaByIdRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling updateMediaById(Async)");
        }

        // verify the required parameter 'updateMediaByIdRequest' is set
        if (updateMediaByIdRequest == null) {
            throw new ApiException("Missing the required parameter 'updateMediaByIdRequest' when calling updateMediaById(Async)");
        }

        return updateMediaByIdCall(id, updateMediaByIdRequest, _callback);

    }

    /**
     * update media
     * 
     * @param id id (required)
     * @param updateMediaByIdRequest  (required)
     * @return MediaResponseObject
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public MediaResponseObject updateMediaById(String id, UpdateMediaByIdRequest updateMediaByIdRequest) throws ApiException {
        ApiResponse<MediaResponseObject> localVarResp = updateMediaByIdWithHttpInfo(id, updateMediaByIdRequest);
        return localVarResp.getData();
    }

    /**
     * update media
     * 
     * @param id id (required)
     * @param updateMediaByIdRequest  (required)
     * @return ApiResponse&lt;MediaResponseObject&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<MediaResponseObject> updateMediaByIdWithHttpInfo(String id, UpdateMediaByIdRequest updateMediaByIdRequest) throws ApiException {
        okhttp3.Call localVarCall = updateMediaByIdValidateBeforeCall(id, updateMediaByIdRequest, null);
        Type localVarReturnType = new TypeToken<MediaResponseObject>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * update media (asynchronously)
     * 
     * @param id id (required)
     * @param updateMediaByIdRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> not authorized </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many requests </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateMediaByIdAsync(String id, UpdateMediaByIdRequest updateMediaByIdRequest, final ApiCallback<MediaResponseObject> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateMediaByIdValidateBeforeCall(id, updateMediaByIdRequest, _callback);
        Type localVarReturnType = new TypeToken<MediaResponseObject>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
