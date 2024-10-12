/**
 * ContentGroove API
 * # Overview  The ContentGroove Developer API enables you to add the power of ContentGroove's video AI to your own applications and workflows.  Webhooks are a way for ContentGroove to send video information to your application, to update your system and/or trigger other business processes.  You can use Webhooks and the Developer API separately or together.  # Getting Started with Webhooks  - Sign up for an account at [app.contentgroove.com](https://app.contentgroove.com) - Read \"Using Webhooks\" on the [API Reference page](https://developers.contentgroove.com/api_reference) - Visit the [Webhooks page](https://app.contentgroove.com/webhook_subscriptions) and create a new webhook  # Using Webhooks  Webhooks, also known as callbacks, are a way for ContentGroove to notify your application as soon as possible after an event has occurred in ContentGroove. For example after a media completes processing, ContentGroove can use a webhook to notify your application with information about the video: Suggested clips, transcription, and so on. You can use the information sent to update your system and/or use the webhook to trigger other business processes.  The webhook request is sent as an HTTP POST containing a payload of JSON-formatted data. For the details of the payload format see the \"CALLBACKS\" sections below.  When your application receives the webhook request, it must respond with a 200 HTTP status code (success). If a 200 HTTP status code is not returned, ContentGroove will assume that the webhook was not delivered and will retry a limited number of times, using an exponential backoff algorithm.  ContentGroove makes a best effort to attempt to send the webhook at least once. Applications receiving webhooks must tolerate the possibility of a single webhook payload being sent more than once (idempotent behavior). Applications receiving webhooks should tolerate the possibility that a webhook could not be delivered (for example your application was down when delivery was attempted).  # Getting Started with the Developer API  - Sign up for an account at [app.contentgroove.com](https://app.contentgroove.com) - Visit the [API Keys page](https://app.contentgroove.com/api_keys)   - Create a new API Key then copy and save the value.     > ⚠️ **IMPORTANT**: This API Key is intended only for use on the server side. Be sure never to use a server-side API Key in client-side (web, mobile, or otherwise) code. ⚠️ - View all available endpoints, and try the API, on our [API Reference page](https://developers.contentgroove.com/api_reference)  # Using the Developer API  - Create a new media (video or audio) in ContentGroove   - If the video or audio is available from a URL, you can create a media by providing the `source_url` parameter. ContentGroove will fetch the video or audio from the URL if possible.   - Or, you can create a media from a video or audio file which you upload directly to ContentGroove (see File Uploading section below). - After the new media is created, at first it will be in a \"processing\" state.   Depending on the size and duration of the video or audio file, it will take some time for processing to complete.   - You can use ContentGroove Webhooks to be notified immediately when processing has completed. (Details coming soon.)   - You can also use the API to read the state of the media, to determine if the media has completed processing yet. - After the media has completed processing, you can access all of these details about the media:   - The media name and description   - The transcription of spoken words   - Topics and keywords which were discussed in the transcription   - Suggested video clips are automatically created - In addition to the automatically created video clips, you can create more video clips from the media  # Response Codes  The following is a comprehensive list of the status codes you may receive while using the ContentGroove API:  - 200 \"Ok\"   - The request was valid - 400 \"Bad Request   - This is returned when there was a problem parsing the JSON body of your request if you supplied the 'Content-Type': 'application/json' header, or if your request is missing the 'Content-Type' header altogether - 401 \"Unauthorized\"   - This is returned when you are attempting to perform an action on a resource that you are not authorized to do - 402 \"Payment Required\"   - This is returned when you are attempting to perform an action that would push your account above a usage limit. You can view your usage at: https://app.contentgroove.com/quota_usage - 404 \"Not Found\"   - This is returned when the resource you are trying to view does not exist - 429 \"Too Many Requests\"   - This is returned when you have performed too many requests within a given period of time - 500 \"Internal Server Error\"   - This is returned when your request was valid but there was a problem on our end  # File Uploading  - Step 1: Make a GET request to the direct uploads URL endpoint (/api/v1/direct_uploads) to receive an upload URL to upload the file to and an upload id. - Step 2: Make a PUT request with the file as the body to the upload URL received in step 1. The response will have a 200 status with no body if the upload is successful.   ```   curl -T /path/to/file upload_url   ``` - Step 3: After uploading the file to the upload URL, make a POST request to the create medias endpoint (/api/v1/medias), with the upload id and optionally a name and description for the new media.   > At this time, file uploads are limited to 5gb per file.  # Allowed media types  Video:  - Supported: Most common video formats and codecs are supported. - Recommended: mp4  Audio:  - Supported: aac, mp3, flac, ogg, wav, and wma - Recommended: aac  # Authentication  You can use the API Key to authenticate your API requests using any of these methods. (Replace abc123 with your actual API Key.)  - Request header `Authorization: Bearer abc123` - Request header `X-API-KEY: abc123` - Query parameter `api_key=abc123`   > ⚠️ **IMPORTANT**: This API Key is intended only for use on the server side. Be sure never to use a server-side API Key in client-side (web, mobile, or otherwise) code. ⚠️  # Link to openapi.json spec  - https://api.contentgroove.com/api-docs/v1/openapi.json 
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import ClipResponseObject from './model/ClipResponseObject';
import ClipResponseObjectData from './model/ClipResponseObjectData';
import ClipResponseObjectDataAttributes from './model/ClipResponseObjectDataAttributes';
import ClipResponseObjectDataRelationships from './model/ClipResponseObjectDataRelationships';
import ClipResponseObjectDataRelationshipsMedia from './model/ClipResponseObjectDataRelationshipsMedia';
import ClipResponseObjectDataRelationshipsMediaData from './model/ClipResponseObjectDataRelationshipsMediaData';
import ClipsResponseObject from './model/ClipsResponseObject';
import CreateClipRequest from './model/CreateClipRequest';
import CreateClipRequestData from './model/CreateClipRequestData';
import CreateClipRequestDataAttributes from './model/CreateClipRequestDataAttributes';
import CreateMediaRequest from './model/CreateMediaRequest';
import CreateMediaRequestData from './model/CreateMediaRequestData';
import CreateMediaRequestDataAttributes from './model/CreateMediaRequestDataAttributes';
import CreateWebhookSubscriptionRequest from './model/CreateWebhookSubscriptionRequest';
import CreateWebhookSubscriptionRequestData from './model/CreateWebhookSubscriptionRequestData';
import CreateWebhookSubscriptionRequestDataAttributes from './model/CreateWebhookSubscriptionRequestDataAttributes';
import DirectUploadResponseObject from './model/DirectUploadResponseObject';
import DirectUploadResponseObjectData from './model/DirectUploadResponseObjectData';
import DirectUploadResponseObjectDataAttributes from './model/DirectUploadResponseObjectDataAttributes';
import LinksObjectData from './model/LinksObjectData';
import MediaResponseObject from './model/MediaResponseObject';
import MediaResponseObjectData from './model/MediaResponseObjectData';
import MediaResponseObjectDataAttributes from './model/MediaResponseObjectDataAttributes';
import MediaResponseObjectDataRelationships from './model/MediaResponseObjectDataRelationships';
import MediaResponseObjectDataRelationshipsClips from './model/MediaResponseObjectDataRelationshipsClips';
import MediasPostRequest from './model/MediasPostRequest';
import MediasPostRequestPayload from './model/MediasPostRequestPayload';
import MediasPostRequestPayloadData from './model/MediasPostRequestPayloadData';
import MediasPostRequestPayloadDataAttributes from './model/MediasPostRequestPayloadDataAttributes';
import MediasPostRequestPayloadDataRelationships from './model/MediasPostRequestPayloadDataRelationships';
import MediasPostRequestPayloadDataRelationshipsClips from './model/MediasPostRequestPayloadDataRelationshipsClips';
import MediasPostRequestPayloadDataRelationshipsClipsDataInner from './model/MediasPostRequestPayloadDataRelationshipsClipsDataInner';
import MediasPostRequestPayloadDataTranscription from './model/MediasPostRequestPayloadDataTranscription';
import MediasPostRequestPayloadDataTranscriptionData from './model/MediasPostRequestPayloadDataTranscriptionData';
import MediasPostRequestPayloadIncludedInner from './model/MediasPostRequestPayloadIncludedInner';
import MediasPostRequestPayloadIncludedInnerOneOf from './model/MediasPostRequestPayloadIncludedInnerOneOf';
import MediasPostRequestPayloadIncludedInnerOneOf1 from './model/MediasPostRequestPayloadIncludedInnerOneOf1';
import MediasPostRequestPayloadIncludedInnerOneOf1Attributes from './model/MediasPostRequestPayloadIncludedInnerOneOf1Attributes';
import MediasPostRequestPayloadIncludedInnerOneOfAttributes from './model/MediasPostRequestPayloadIncludedInnerOneOfAttributes';
import MediasPostRequestPayloadIncludedInnerOneOfRelationships from './model/MediasPostRequestPayloadIncludedInnerOneOfRelationships';
import MediasPostRequestPayloadIncludedInnerOneOfRelationshipsMedia from './model/MediasPostRequestPayloadIncludedInnerOneOfRelationshipsMedia';
import MediasPostRequestPayloadIncludedInnerOneOfRelationshipsMediaData from './model/MediasPostRequestPayloadIncludedInnerOneOfRelationshipsMediaData';
import MediasResponseObject from './model/MediasResponseObject';
import PaymentRequiredErrorResponseObject from './model/PaymentRequiredErrorResponseObject';
import PaymentRequiredErrorResponseObjectErrorsInner from './model/PaymentRequiredErrorResponseObjectErrorsInner';
import PaymentRequiredErrorResponseObjectErrorsInnerSource from './model/PaymentRequiredErrorResponseObjectErrorsInnerSource';
import TooManyRequestsErrorResponseObject from './model/TooManyRequestsErrorResponseObject';
import TooManyRequestsErrorResponseObjectErrorsInner from './model/TooManyRequestsErrorResponseObjectErrorsInner';
import UnauthorizedErrorResponseObject from './model/UnauthorizedErrorResponseObject';
import UnauthorizedErrorResponseObjectErrorsInner from './model/UnauthorizedErrorResponseObjectErrorsInner';
import UpdateClipByIdRequest from './model/UpdateClipByIdRequest';
import UpdateClipByIdRequestData from './model/UpdateClipByIdRequestData';
import UpdateClipByIdRequestDataAttributes from './model/UpdateClipByIdRequestDataAttributes';
import UpdateMediaByIdRequest from './model/UpdateMediaByIdRequest';
import UpdateMediaByIdRequestData from './model/UpdateMediaByIdRequestData';
import UpdateMediaByIdRequestDataAttributes from './model/UpdateMediaByIdRequestDataAttributes';
import WebhookSubscriptionResponseObject from './model/WebhookSubscriptionResponseObject';
import WebhookSubscriptionResponseObjectData from './model/WebhookSubscriptionResponseObjectData';
import WebhookSubscriptionResponseObjectDataAttributes from './model/WebhookSubscriptionResponseObjectDataAttributes';
import WebhookSubscriptionResponseObjectDataRelationships from './model/WebhookSubscriptionResponseObjectDataRelationships';
import WebhookSubscriptionsResponseObject from './model/WebhookSubscriptionsResponseObject';
import DefaultApi from './api/DefaultApi';


/**
* # Overview  The ContentGroove Developer API enables you to add the power of ContentGroove&#39;s video AI to your own applications and workflows.  Webhooks are a way for ContentGroove to send video information to your application, to update your system and/or trigger other business processes.  You can use Webhooks and the Developer API separately or together.  # Getting Started with Webhooks  - Sign up for an account at [app.contentgroove.com](https://app.contentgroove.com) - Read \&quot;Using Webhooks\&quot; on the [API Reference page](https://developers.contentgroove.com/api_reference) - Visit the [Webhooks page](https://app.contentgroove.com/webhook_subscriptions) and create a new webhook  # Using Webhooks  Webhooks, also known as callbacks, are a way for ContentGroove to notify your application as soon as possible after an event has occurred in ContentGroove. For example after a media completes processing, ContentGroove can use a webhook to notify your application with information about the video: Suggested clips, transcription, and so on. You can use the information sent to update your system and/or use the webhook to trigger other business processes.  The webhook request is sent as an HTTP POST containing a payload of JSON-formatted data. For the details of the payload format see the \&quot;CALLBACKS\&quot; sections below.  When your application receives the webhook request, it must respond with a 200 HTTP status code (success). If a 200 HTTP status code is not returned, ContentGroove will assume that the webhook was not delivered and will retry a limited number of times, using an exponential backoff algorithm.  ContentGroove makes a best effort to attempt to send the webhook at least once. Applications receiving webhooks must tolerate the possibility of a single webhook payload being sent more than once (idempotent behavior). Applications receiving webhooks should tolerate the possibility that a webhook could not be delivered (for example your application was down when delivery was attempted).  # Getting Started with the Developer API  - Sign up for an account at [app.contentgroove.com](https://app.contentgroove.com) - Visit the [API Keys page](https://app.contentgroove.com/api_keys)   - Create a new API Key then copy and save the value.     &gt; ⚠️ **IMPORTANT**: This API Key is intended only for use on the server side. Be sure never to use a server-side API Key in client-side (web, mobile, or otherwise) code. ⚠️ - View all available endpoints, and try the API, on our [API Reference page](https://developers.contentgroove.com/api_reference)  # Using the Developer API  - Create a new media (video or audio) in ContentGroove   - If the video or audio is available from a URL, you can create a media by providing the &#x60;source_url&#x60; parameter. ContentGroove will fetch the video or audio from the URL if possible.   - Or, you can create a media from a video or audio file which you upload directly to ContentGroove (see File Uploading section below). - After the new media is created, at first it will be in a \&quot;processing\&quot; state.   Depending on the size and duration of the video or audio file, it will take some time for processing to complete.   - You can use ContentGroove Webhooks to be notified immediately when processing has completed. (Details coming soon.)   - You can also use the API to read the state of the media, to determine if the media has completed processing yet. - After the media has completed processing, you can access all of these details about the media:   - The media name and description   - The transcription of spoken words   - Topics and keywords which were discussed in the transcription   - Suggested video clips are automatically created - In addition to the automatically created video clips, you can create more video clips from the media  # Response Codes  The following is a comprehensive list of the status codes you may receive while using the ContentGroove API:  - 200 \&quot;Ok\&quot;   - The request was valid - 400 \&quot;Bad Request   - This is returned when there was a problem parsing the JSON body of your request if you supplied the &#39;Content-Type&#39;: &#39;application/json&#39; header, or if your request is missing the &#39;Content-Type&#39; header altogether - 401 \&quot;Unauthorized\&quot;   - This is returned when you are attempting to perform an action on a resource that you are not authorized to do - 402 \&quot;Payment Required\&quot;   - This is returned when you are attempting to perform an action that would push your account above a usage limit. You can view your usage at: https://app.contentgroove.com/quota_usage - 404 \&quot;Not Found\&quot;   - This is returned when the resource you are trying to view does not exist - 429 \&quot;Too Many Requests\&quot;   - This is returned when you have performed too many requests within a given period of time - 500 \&quot;Internal Server Error\&quot;   - This is returned when your request was valid but there was a problem on our end  # File Uploading  - Step 1: Make a GET request to the direct uploads URL endpoint (/api/v1/direct_uploads) to receive an upload URL to upload the file to and an upload id. - Step 2: Make a PUT request with the file as the body to the upload URL received in step 1. The response will have a 200 status with no body if the upload is successful.   &#x60;&#x60;&#x60;   curl -T /path/to/file upload_url   &#x60;&#x60;&#x60; - Step 3: After uploading the file to the upload URL, make a POST request to the create medias endpoint (/api/v1/medias), with the upload id and optionally a name and description for the new media.   &gt; At this time, file uploads are limited to 5gb per file.  # Allowed media types  Video:  - Supported: Most common video formats and codecs are supported. - Recommended: mp4  Audio:  - Supported: aac, mp3, flac, ogg, wav, and wma - Recommended: aac  # Authentication  You can use the API Key to authenticate your API requests using any of these methods. (Replace abc123 with your actual API Key.)  - Request header &#x60;Authorization: Bearer abc123&#x60; - Request header &#x60;X-API-KEY: abc123&#x60; - Query parameter &#x60;api_key&#x3D;abc123&#x60;   &gt; ⚠️ **IMPORTANT**: This API Key is intended only for use on the server side. Be sure never to use a server-side API Key in client-side (web, mobile, or otherwise) code. ⚠️  # Link to openapi.json spec  - https://api.contentgroove.com/api-docs/v1/openapi.json .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var ContentGrooveApi = require('index'); // See note below*.
* var xxxSvc = new ContentGrooveApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new ContentGrooveApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new ContentGrooveApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new ContentGrooveApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.0.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The ClipResponseObject model constructor.
     * @property {module:model/ClipResponseObject}
     */
    ClipResponseObject,

    /**
     * The ClipResponseObjectData model constructor.
     * @property {module:model/ClipResponseObjectData}
     */
    ClipResponseObjectData,

    /**
     * The ClipResponseObjectDataAttributes model constructor.
     * @property {module:model/ClipResponseObjectDataAttributes}
     */
    ClipResponseObjectDataAttributes,

    /**
     * The ClipResponseObjectDataRelationships model constructor.
     * @property {module:model/ClipResponseObjectDataRelationships}
     */
    ClipResponseObjectDataRelationships,

    /**
     * The ClipResponseObjectDataRelationshipsMedia model constructor.
     * @property {module:model/ClipResponseObjectDataRelationshipsMedia}
     */
    ClipResponseObjectDataRelationshipsMedia,

    /**
     * The ClipResponseObjectDataRelationshipsMediaData model constructor.
     * @property {module:model/ClipResponseObjectDataRelationshipsMediaData}
     */
    ClipResponseObjectDataRelationshipsMediaData,

    /**
     * The ClipsResponseObject model constructor.
     * @property {module:model/ClipsResponseObject}
     */
    ClipsResponseObject,

    /**
     * The CreateClipRequest model constructor.
     * @property {module:model/CreateClipRequest}
     */
    CreateClipRequest,

    /**
     * The CreateClipRequestData model constructor.
     * @property {module:model/CreateClipRequestData}
     */
    CreateClipRequestData,

    /**
     * The CreateClipRequestDataAttributes model constructor.
     * @property {module:model/CreateClipRequestDataAttributes}
     */
    CreateClipRequestDataAttributes,

    /**
     * The CreateMediaRequest model constructor.
     * @property {module:model/CreateMediaRequest}
     */
    CreateMediaRequest,

    /**
     * The CreateMediaRequestData model constructor.
     * @property {module:model/CreateMediaRequestData}
     */
    CreateMediaRequestData,

    /**
     * The CreateMediaRequestDataAttributes model constructor.
     * @property {module:model/CreateMediaRequestDataAttributes}
     */
    CreateMediaRequestDataAttributes,

    /**
     * The CreateWebhookSubscriptionRequest model constructor.
     * @property {module:model/CreateWebhookSubscriptionRequest}
     */
    CreateWebhookSubscriptionRequest,

    /**
     * The CreateWebhookSubscriptionRequestData model constructor.
     * @property {module:model/CreateWebhookSubscriptionRequestData}
     */
    CreateWebhookSubscriptionRequestData,

    /**
     * The CreateWebhookSubscriptionRequestDataAttributes model constructor.
     * @property {module:model/CreateWebhookSubscriptionRequestDataAttributes}
     */
    CreateWebhookSubscriptionRequestDataAttributes,

    /**
     * The DirectUploadResponseObject model constructor.
     * @property {module:model/DirectUploadResponseObject}
     */
    DirectUploadResponseObject,

    /**
     * The DirectUploadResponseObjectData model constructor.
     * @property {module:model/DirectUploadResponseObjectData}
     */
    DirectUploadResponseObjectData,

    /**
     * The DirectUploadResponseObjectDataAttributes model constructor.
     * @property {module:model/DirectUploadResponseObjectDataAttributes}
     */
    DirectUploadResponseObjectDataAttributes,

    /**
     * The LinksObjectData model constructor.
     * @property {module:model/LinksObjectData}
     */
    LinksObjectData,

    /**
     * The MediaResponseObject model constructor.
     * @property {module:model/MediaResponseObject}
     */
    MediaResponseObject,

    /**
     * The MediaResponseObjectData model constructor.
     * @property {module:model/MediaResponseObjectData}
     */
    MediaResponseObjectData,

    /**
     * The MediaResponseObjectDataAttributes model constructor.
     * @property {module:model/MediaResponseObjectDataAttributes}
     */
    MediaResponseObjectDataAttributes,

    /**
     * The MediaResponseObjectDataRelationships model constructor.
     * @property {module:model/MediaResponseObjectDataRelationships}
     */
    MediaResponseObjectDataRelationships,

    /**
     * The MediaResponseObjectDataRelationshipsClips model constructor.
     * @property {module:model/MediaResponseObjectDataRelationshipsClips}
     */
    MediaResponseObjectDataRelationshipsClips,

    /**
     * The MediasPostRequest model constructor.
     * @property {module:model/MediasPostRequest}
     */
    MediasPostRequest,

    /**
     * The MediasPostRequestPayload model constructor.
     * @property {module:model/MediasPostRequestPayload}
     */
    MediasPostRequestPayload,

    /**
     * The MediasPostRequestPayloadData model constructor.
     * @property {module:model/MediasPostRequestPayloadData}
     */
    MediasPostRequestPayloadData,

    /**
     * The MediasPostRequestPayloadDataAttributes model constructor.
     * @property {module:model/MediasPostRequestPayloadDataAttributes}
     */
    MediasPostRequestPayloadDataAttributes,

    /**
     * The MediasPostRequestPayloadDataRelationships model constructor.
     * @property {module:model/MediasPostRequestPayloadDataRelationships}
     */
    MediasPostRequestPayloadDataRelationships,

    /**
     * The MediasPostRequestPayloadDataRelationshipsClips model constructor.
     * @property {module:model/MediasPostRequestPayloadDataRelationshipsClips}
     */
    MediasPostRequestPayloadDataRelationshipsClips,

    /**
     * The MediasPostRequestPayloadDataRelationshipsClipsDataInner model constructor.
     * @property {module:model/MediasPostRequestPayloadDataRelationshipsClipsDataInner}
     */
    MediasPostRequestPayloadDataRelationshipsClipsDataInner,

    /**
     * The MediasPostRequestPayloadDataTranscription model constructor.
     * @property {module:model/MediasPostRequestPayloadDataTranscription}
     */
    MediasPostRequestPayloadDataTranscription,

    /**
     * The MediasPostRequestPayloadDataTranscriptionData model constructor.
     * @property {module:model/MediasPostRequestPayloadDataTranscriptionData}
     */
    MediasPostRequestPayloadDataTranscriptionData,

    /**
     * The MediasPostRequestPayloadIncludedInner model constructor.
     * @property {module:model/MediasPostRequestPayloadIncludedInner}
     */
    MediasPostRequestPayloadIncludedInner,

    /**
     * The MediasPostRequestPayloadIncludedInnerOneOf model constructor.
     * @property {module:model/MediasPostRequestPayloadIncludedInnerOneOf}
     */
    MediasPostRequestPayloadIncludedInnerOneOf,

    /**
     * The MediasPostRequestPayloadIncludedInnerOneOf1 model constructor.
     * @property {module:model/MediasPostRequestPayloadIncludedInnerOneOf1}
     */
    MediasPostRequestPayloadIncludedInnerOneOf1,

    /**
     * The MediasPostRequestPayloadIncludedInnerOneOf1Attributes model constructor.
     * @property {module:model/MediasPostRequestPayloadIncludedInnerOneOf1Attributes}
     */
    MediasPostRequestPayloadIncludedInnerOneOf1Attributes,

    /**
     * The MediasPostRequestPayloadIncludedInnerOneOfAttributes model constructor.
     * @property {module:model/MediasPostRequestPayloadIncludedInnerOneOfAttributes}
     */
    MediasPostRequestPayloadIncludedInnerOneOfAttributes,

    /**
     * The MediasPostRequestPayloadIncludedInnerOneOfRelationships model constructor.
     * @property {module:model/MediasPostRequestPayloadIncludedInnerOneOfRelationships}
     */
    MediasPostRequestPayloadIncludedInnerOneOfRelationships,

    /**
     * The MediasPostRequestPayloadIncludedInnerOneOfRelationshipsMedia model constructor.
     * @property {module:model/MediasPostRequestPayloadIncludedInnerOneOfRelationshipsMedia}
     */
    MediasPostRequestPayloadIncludedInnerOneOfRelationshipsMedia,

    /**
     * The MediasPostRequestPayloadIncludedInnerOneOfRelationshipsMediaData model constructor.
     * @property {module:model/MediasPostRequestPayloadIncludedInnerOneOfRelationshipsMediaData}
     */
    MediasPostRequestPayloadIncludedInnerOneOfRelationshipsMediaData,

    /**
     * The MediasResponseObject model constructor.
     * @property {module:model/MediasResponseObject}
     */
    MediasResponseObject,

    /**
     * The PaymentRequiredErrorResponseObject model constructor.
     * @property {module:model/PaymentRequiredErrorResponseObject}
     */
    PaymentRequiredErrorResponseObject,

    /**
     * The PaymentRequiredErrorResponseObjectErrorsInner model constructor.
     * @property {module:model/PaymentRequiredErrorResponseObjectErrorsInner}
     */
    PaymentRequiredErrorResponseObjectErrorsInner,

    /**
     * The PaymentRequiredErrorResponseObjectErrorsInnerSource model constructor.
     * @property {module:model/PaymentRequiredErrorResponseObjectErrorsInnerSource}
     */
    PaymentRequiredErrorResponseObjectErrorsInnerSource,

    /**
     * The TooManyRequestsErrorResponseObject model constructor.
     * @property {module:model/TooManyRequestsErrorResponseObject}
     */
    TooManyRequestsErrorResponseObject,

    /**
     * The TooManyRequestsErrorResponseObjectErrorsInner model constructor.
     * @property {module:model/TooManyRequestsErrorResponseObjectErrorsInner}
     */
    TooManyRequestsErrorResponseObjectErrorsInner,

    /**
     * The UnauthorizedErrorResponseObject model constructor.
     * @property {module:model/UnauthorizedErrorResponseObject}
     */
    UnauthorizedErrorResponseObject,

    /**
     * The UnauthorizedErrorResponseObjectErrorsInner model constructor.
     * @property {module:model/UnauthorizedErrorResponseObjectErrorsInner}
     */
    UnauthorizedErrorResponseObjectErrorsInner,

    /**
     * The UpdateClipByIdRequest model constructor.
     * @property {module:model/UpdateClipByIdRequest}
     */
    UpdateClipByIdRequest,

    /**
     * The UpdateClipByIdRequestData model constructor.
     * @property {module:model/UpdateClipByIdRequestData}
     */
    UpdateClipByIdRequestData,

    /**
     * The UpdateClipByIdRequestDataAttributes model constructor.
     * @property {module:model/UpdateClipByIdRequestDataAttributes}
     */
    UpdateClipByIdRequestDataAttributes,

    /**
     * The UpdateMediaByIdRequest model constructor.
     * @property {module:model/UpdateMediaByIdRequest}
     */
    UpdateMediaByIdRequest,

    /**
     * The UpdateMediaByIdRequestData model constructor.
     * @property {module:model/UpdateMediaByIdRequestData}
     */
    UpdateMediaByIdRequestData,

    /**
     * The UpdateMediaByIdRequestDataAttributes model constructor.
     * @property {module:model/UpdateMediaByIdRequestDataAttributes}
     */
    UpdateMediaByIdRequestDataAttributes,

    /**
     * The WebhookSubscriptionResponseObject model constructor.
     * @property {module:model/WebhookSubscriptionResponseObject}
     */
    WebhookSubscriptionResponseObject,

    /**
     * The WebhookSubscriptionResponseObjectData model constructor.
     * @property {module:model/WebhookSubscriptionResponseObjectData}
     */
    WebhookSubscriptionResponseObjectData,

    /**
     * The WebhookSubscriptionResponseObjectDataAttributes model constructor.
     * @property {module:model/WebhookSubscriptionResponseObjectDataAttributes}
     */
    WebhookSubscriptionResponseObjectDataAttributes,

    /**
     * The WebhookSubscriptionResponseObjectDataRelationships model constructor.
     * @property {module:model/WebhookSubscriptionResponseObjectDataRelationships}
     */
    WebhookSubscriptionResponseObjectDataRelationships,

    /**
     * The WebhookSubscriptionsResponseObject model constructor.
     * @property {module:model/WebhookSubscriptionsResponseObject}
     */
    WebhookSubscriptionsResponseObject,

    /**
    * The DefaultApi service constructor.
    * @property {module:api/DefaultApi}
    */
    DefaultApi
};
