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

import org.openapitools.client.ApiException;
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
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DefaultApi
 */
@Disabled
public class DefaultApiTest {

    private final DefaultApi api = new DefaultApi();

    /**
     * create clip
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createClipTest() throws ApiException {
        CreateClipRequest createClipRequest = null;
        ClipResponseObject response = api.createClip(createClipRequest);
        // TODO: test validations
    }

    /**
     * create media
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createMediaTest() throws ApiException {
        CreateMediaRequest createMediaRequest = null;
        MediaResponseObject response = api.createMedia(createMediaRequest);
        // TODO: test validations
    }

    /**
     * create webhook subscription
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createWebhookSubscriptionTest() throws ApiException {
        CreateWebhookSubscriptionRequest createWebhookSubscriptionRequest = null;
        WebhookSubscriptionResponseObject response = api.createWebhookSubscription(createWebhookSubscriptionRequest);
        // TODO: test validations
    }

    /**
     * delete clip
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteClipByIdTest() throws ApiException {
        String id = null;
        api.deleteClipById(id);
        // TODO: test validations
    }

    /**
     * delete media
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteMediaByIdTest() throws ApiException {
        String id = null;
        api.deleteMediaById(id);
        // TODO: test validations
    }

    /**
     * delete webhook subscription
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteWebhookSubscriptionByIdTest() throws ApiException {
        String id = null;
        api.deleteWebhookSubscriptionById(id);
        // TODO: test validations
    }

    /**
     * show clip
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getClipByIdTest() throws ApiException {
        String id = null;
        ClipResponseObject response = api.getClipById(id);
        // TODO: test validations
    }

    /**
     * list clips
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getClipsTest() throws ApiException {
        Object filter = null;
        Object page = null;
        String sort = null;
        ClipsResponseObject response = api.getClips(filter, page, sort);
        // TODO: test validations
    }

    /**
     * show media
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getMediaByIdTest() throws ApiException {
        String id = null;
        MediaResponseObject response = api.getMediaById(id);
        // TODO: test validations
    }

    /**
     * list medias
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getMediasTest() throws ApiException {
        Object filter = null;
        Object page = null;
        String sort = null;
        MediasResponseObject response = api.getMedias(filter, page, sort);
        // TODO: test validations
    }

    /**
     * prepare presigned upload url
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getUploadUrlTest() throws ApiException {
        DirectUploadResponseObject response = api.getUploadUrl();
        // TODO: test validations
    }

    /**
     * show webhook subscription
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getWebhookSubscriptionByIdTest() throws ApiException {
        String id = null;
        WebhookSubscriptionResponseObject response = api.getWebhookSubscriptionById(id);
        // TODO: test validations
    }

    /**
     * list webhook subscriptions
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getWebhookSubscriptionsTest() throws ApiException {
        Object filter = null;
        String sort = null;
        WebhookSubscriptionsResponseObject response = api.getWebhookSubscriptions(filter, sort);
        // TODO: test validations
    }

    /**
     * update clip
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateClipByIdTest() throws ApiException {
        String id = null;
        UpdateClipByIdRequest updateClipByIdRequest = null;
        ClipResponseObject response = api.updateClipById(id, updateClipByIdRequest);
        // TODO: test validations
    }

    /**
     * update media
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateMediaByIdTest() throws ApiException {
        String id = null;
        UpdateMediaByIdRequest updateMediaByIdRequest = null;
        MediaResponseObject response = api.updateMediaById(id, updateMediaByIdRequest);
        // TODO: test validations
    }

}
