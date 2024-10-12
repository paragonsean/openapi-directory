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


import ApiClient from "../ApiClient";
import ClipResponseObject from '../model/ClipResponseObject';
import ClipsResponseObject from '../model/ClipsResponseObject';
import CreateClipRequest from '../model/CreateClipRequest';
import CreateMediaRequest from '../model/CreateMediaRequest';
import CreateWebhookSubscriptionRequest from '../model/CreateWebhookSubscriptionRequest';
import DirectUploadResponseObject from '../model/DirectUploadResponseObject';
import MediaResponseObject from '../model/MediaResponseObject';
import MediasResponseObject from '../model/MediasResponseObject';
import PaymentRequiredErrorResponseObject from '../model/PaymentRequiredErrorResponseObject';
import TooManyRequestsErrorResponseObject from '../model/TooManyRequestsErrorResponseObject';
import UnauthorizedErrorResponseObject from '../model/UnauthorizedErrorResponseObject';
import UpdateClipByIdRequest from '../model/UpdateClipByIdRequest';
import UpdateMediaByIdRequest from '../model/UpdateMediaByIdRequest';
import WebhookSubscriptionResponseObject from '../model/WebhookSubscriptionResponseObject';
import WebhookSubscriptionsResponseObject from '../model/WebhookSubscriptionsResponseObject';

/**
* Default service.
* @module api/DefaultApi
* @version 1.0.0
*/
export default class DefaultApi {

    /**
    * Constructs a new DefaultApi. 
    * @alias module:api/DefaultApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createClip operation.
     * @callback module:api/DefaultApi~createClipCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClipResponseObject} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * create clip
     * @param {module:model/CreateClipRequest} createClipRequest 
     * @param {module:api/DefaultApi~createClipCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClipResponseObject}
     */
    createClip(createClipRequest, callback) {
      let postBody = createClipRequest;
      // verify the required parameter 'createClipRequest' is set
      if (createClipRequest === undefined || createClipRequest === null) {
        throw new Error("Missing the required parameter 'createClipRequest' when calling createClip");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['BearerHeader'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ClipResponseObject;
      return this.apiClient.callApi(
        '/clips', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createMedia operation.
     * @callback module:api/DefaultApi~createMediaCallback
     * @param {String} error Error message, if any.
     * @param {module:model/MediaResponseObject} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * create media
     * @param {module:model/CreateMediaRequest} createMediaRequest 
     * @param {module:api/DefaultApi~createMediaCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/MediaResponseObject}
     */
    createMedia(createMediaRequest, callback) {
      let postBody = createMediaRequest;
      // verify the required parameter 'createMediaRequest' is set
      if (createMediaRequest === undefined || createMediaRequest === null) {
        throw new Error("Missing the required parameter 'createMediaRequest' when calling createMedia");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['BearerHeader'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = MediaResponseObject;
      return this.apiClient.callApi(
        '/medias', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createWebhookSubscription operation.
     * @callback module:api/DefaultApi~createWebhookSubscriptionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/WebhookSubscriptionResponseObject} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * create webhook subscription
     * @param {module:model/CreateWebhookSubscriptionRequest} createWebhookSubscriptionRequest 
     * @param {module:api/DefaultApi~createWebhookSubscriptionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/WebhookSubscriptionResponseObject}
     */
    createWebhookSubscription(createWebhookSubscriptionRequest, callback) {
      let postBody = createWebhookSubscriptionRequest;
      // verify the required parameter 'createWebhookSubscriptionRequest' is set
      if (createWebhookSubscriptionRequest === undefined || createWebhookSubscriptionRequest === null) {
        throw new Error("Missing the required parameter 'createWebhookSubscriptionRequest' when calling createWebhookSubscription");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['BearerHeader'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = WebhookSubscriptionResponseObject;
      return this.apiClient.callApi(
        '/webhook_subscriptions', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteClipById operation.
     * @callback module:api/DefaultApi~deleteClipByIdCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * delete clip
     * @param {String} id The id of the clip to be retrieved
     * @param {module:api/DefaultApi~deleteClipByIdCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteClipById(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling deleteClipById");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['BearerHeader'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/clips/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteMediaById operation.
     * @callback module:api/DefaultApi~deleteMediaByIdCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * delete media
     * @param {String} id id
     * @param {module:api/DefaultApi~deleteMediaByIdCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteMediaById(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling deleteMediaById");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['BearerHeader'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/medias/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteWebhookSubscriptionById operation.
     * @callback module:api/DefaultApi~deleteWebhookSubscriptionByIdCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * delete webhook subscription
     * @param {String} id The id of the webhook subscription to be retrieved
     * @param {module:api/DefaultApi~deleteWebhookSubscriptionByIdCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteWebhookSubscriptionById(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling deleteWebhookSubscriptionById");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['BearerHeader'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/webhook_subscriptions/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getClipById operation.
     * @callback module:api/DefaultApi~getClipByIdCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClipResponseObject} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * show clip
     * @param {String} id The id of the clip to be retrieved
     * @param {module:api/DefaultApi~getClipByIdCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClipResponseObject}
     */
    getClipById(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getClipById");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['BearerHeader'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ClipResponseObject;
      return this.apiClient.callApi(
        '/clips/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getClips operation.
     * @callback module:api/DefaultApi~getClipsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClipsResponseObject} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * list clips
     * @param {Object} opts Optional parameters
     * @param {Object.<String, Object>} [filter] Filters to be applied to the query.  Query params in the url must look like this: \"filter[attributeName_*matcher*]\"  (i.e. filter[name_eq]=chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/  
     * @param {Object.<String, Object>} [page] Specify page number and page size for the query
     * @param {module:model/String} [sort] Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting
     * @param {module:api/DefaultApi~getClipsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClipsResponseObject}
     */
    getClips(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'filter': opts['filter'],
        'page': opts['page'],
        'sort': opts['sort']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['BearerHeader'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ClipsResponseObject;
      return this.apiClient.callApi(
        '/clips', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getMediaById operation.
     * @callback module:api/DefaultApi~getMediaByIdCallback
     * @param {String} error Error message, if any.
     * @param {module:model/MediaResponseObject} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * show media
     * @param {String} id id
     * @param {module:api/DefaultApi~getMediaByIdCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/MediaResponseObject}
     */
    getMediaById(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getMediaById");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['BearerHeader'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = MediaResponseObject;
      return this.apiClient.callApi(
        '/medias/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getMedias operation.
     * @callback module:api/DefaultApi~getMediasCallback
     * @param {String} error Error message, if any.
     * @param {module:model/MediasResponseObject} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * list medias
     * @param {Object} opts Optional parameters
     * @param {Object.<String, Object>} [filter] Filters to be applied to the query.  Query params in the url must look like this: \"filter[attributeName_*matcher*]\"  (i.e. filter[name_eq]=chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/  
     * @param {Object.<String, Object>} [page] Specify page number and page size for the query
     * @param {module:model/String} [sort] Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting
     * @param {module:api/DefaultApi~getMediasCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/MediasResponseObject}
     */
    getMedias(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'filter': opts['filter'],
        'page': opts['page'],
        'sort': opts['sort']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['BearerHeader'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = MediasResponseObject;
      return this.apiClient.callApi(
        '/medias', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getUploadUrl operation.
     * @callback module:api/DefaultApi~getUploadUrlCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DirectUploadResponseObject} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * prepare presigned upload url
     * @param {module:api/DefaultApi~getUploadUrlCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DirectUploadResponseObject}
     */
    getUploadUrl(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['BearerHeader'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DirectUploadResponseObject;
      return this.apiClient.callApi(
        '/direct_uploads', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getWebhookSubscriptionById operation.
     * @callback module:api/DefaultApi~getWebhookSubscriptionByIdCallback
     * @param {String} error Error message, if any.
     * @param {module:model/WebhookSubscriptionResponseObject} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * show webhook subscription
     * @param {String} id The id of the webhook subscription to be retrieved
     * @param {module:api/DefaultApi~getWebhookSubscriptionByIdCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/WebhookSubscriptionResponseObject}
     */
    getWebhookSubscriptionById(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getWebhookSubscriptionById");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['BearerHeader'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = WebhookSubscriptionResponseObject;
      return this.apiClient.callApi(
        '/webhook_subscriptions/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getWebhookSubscriptions operation.
     * @callback module:api/DefaultApi~getWebhookSubscriptionsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/WebhookSubscriptionsResponseObject} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * list webhook subscriptions
     * @param {Object} opts Optional parameters
     * @param {Object.<String, Object>} [filter] Filters to be applied to the query.  Query params in the url must look like this: \"filter[attributeName_*matcher*]\"  (i.e. filter[name_eq]=chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/  
     * @param {module:model/String} [sort] Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting
     * @param {module:api/DefaultApi~getWebhookSubscriptionsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/WebhookSubscriptionsResponseObject}
     */
    getWebhookSubscriptions(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'filter': opts['filter'],
        'sort': opts['sort']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['BearerHeader'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = WebhookSubscriptionsResponseObject;
      return this.apiClient.callApi(
        '/webhook_subscriptions', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateClipById operation.
     * @callback module:api/DefaultApi~updateClipByIdCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClipResponseObject} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * update clip
     * @param {String} id The id of the clip to be retrieved
     * @param {module:model/UpdateClipByIdRequest} updateClipByIdRequest 
     * @param {module:api/DefaultApi~updateClipByIdCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClipResponseObject}
     */
    updateClipById(id, updateClipByIdRequest, callback) {
      let postBody = updateClipByIdRequest;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling updateClipById");
      }
      // verify the required parameter 'updateClipByIdRequest' is set
      if (updateClipByIdRequest === undefined || updateClipByIdRequest === null) {
        throw new Error("Missing the required parameter 'updateClipByIdRequest' when calling updateClipById");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['BearerHeader'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ClipResponseObject;
      return this.apiClient.callApi(
        '/clips/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateMediaById operation.
     * @callback module:api/DefaultApi~updateMediaByIdCallback
     * @param {String} error Error message, if any.
     * @param {module:model/MediaResponseObject} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * update media
     * @param {String} id id
     * @param {module:model/UpdateMediaByIdRequest} updateMediaByIdRequest 
     * @param {module:api/DefaultApi~updateMediaByIdCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/MediaResponseObject}
     */
    updateMediaById(id, updateMediaByIdRequest, callback) {
      let postBody = updateMediaByIdRequest;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling updateMediaById");
      }
      // verify the required parameter 'updateMediaByIdRequest' is set
      if (updateMediaByIdRequest === undefined || updateMediaByIdRequest === null) {
        throw new Error("Missing the required parameter 'updateMediaByIdRequest' when calling updateMediaById");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['BearerHeader'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = MediaResponseObject;
      return this.apiClient.callApi(
        '/medias/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
