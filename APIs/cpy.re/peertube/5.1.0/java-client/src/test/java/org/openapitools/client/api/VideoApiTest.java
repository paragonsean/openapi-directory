/*
 * PeerTube
 * The PeerTube API is built on HTTP(S) and is RESTful. You can use your favorite HTTP/REST library for your programming language to use PeerTube. The spec API is fully compatible with [openapi-generator](https://github.com/OpenAPITools/openapi-generator/wiki/API-client-generator-HOWTO) which generates a client SDK in the language of your choice - we generate some client SDKs automatically:  - [Python](https://framagit.org/framasoft/peertube/clients/python) - [Go](https://framagit.org/framasoft/peertube/clients/go) - [Kotlin](https://framagit.org/framasoft/peertube/clients/kotlin)  See the [REST API quick start](https://docs.joinpeertube.org/api/rest-getting-started) for a few examples of using the PeerTube API.  # Authentication  When you sign up for an account on a PeerTube instance, you are given the possibility to generate sessions on it, and authenticate there using an access token. Only __one access token can currently be used at a time__.  ## Roles  Accounts are given permissions based on their role. There are three roles on PeerTube: Administrator, Moderator, and User. See the [roles guide](https://docs.joinpeertube.org/admin/managing-users#roles) for a detail of their permissions.  # Errors  The API uses standard HTTP status codes to indicate the success or failure of the API call, completed by a [RFC7807-compliant](https://tools.ietf.org/html/rfc7807) response body.  ``` HTTP 1.1 404 Not Found Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Video not found\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 404,   \"title\": \"Not Found\",   \"type\": \"about:blank\" } ```  We provide error `type` values for [a growing number of cases](https://github.com/Chocobozzz/PeerTube/blob/develop/shared/models/server/server-error-code.enum.ts), but it is still optional. Types are used to disambiguate errors that bear the same status code and are non-obvious:  ``` HTTP 1.1 403 Forbidden Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Cannot get this video regarding follow constraints\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 403,   \"title\": \"Forbidden\",   \"type\": \"https://docs.joinpeertube.org/api/rest-reference.html#section/Errors/does_not_respect_follow_constraints\" } ```  Here a 403 error could otherwise mean that the video is private or blocklisted.  ### Validation errors  Each parameter is evaluated on its own against a set of rules before the route validator proceeds with potential testing involving parameter combinations. Errors coming from validation errors appear earlier and benefit from a more detailed error description:  ``` HTTP 1.1 400 Bad Request Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Incorrect request parameters: id\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"instance\": \"/api/v1/videos/9c9de5e8-0a1e-484a-b099-e80766180\",   \"invalid-params\": {     \"id\": {       \"location\": \"params\",       \"msg\": \"Invalid value\",       \"param\": \"id\",       \"value\": \"9c9de5e8-0a1e-484a-b099-e80766180\"     }   },   \"status\": 400,   \"title\": \"Bad Request\",   \"type\": \"about:blank\" } ```  Where `id` is the name of the field concerned by the error, within the route definition. `invalid-params.<field>.location` can be either 'params', 'body', 'header', 'query' or 'cookies', and `invalid-params.<field>.value` reports the value that didn't pass validation whose `invalid-params.<field>.msg` is about.  ### Deprecated error fields  Some fields could be included with previous versions. They are still included but their use is deprecated: - `error`: superseded by `detail` - `code`: superseded by `type` (which is now an URI)  # Rate limits  We are rate-limiting all endpoints of PeerTube's API. Custom values can be set by administrators:  | Endpoint (prefix: `/api/v1`) | Calls         | Time frame   | |------------------------------|---------------|--------------| | `/_*`                         | 50            | 10 seconds   | | `POST /users/token`          | 15            | 5 minutes    | | `POST /users/register`       | 2<sup>*</sup> | 5 minutes    | | `POST /users/ask-send-verify-email` | 3      | 5 minutes    |  Depending on the endpoint, <sup>*</sup>failed requests are not taken into account. A service limit is announced by a `429 Too Many Requests` status code.  You can get details about the current state of your rate limit by reading the following headers:  | Header                  | Description                                                | |-------------------------|------------------------------------------------------------| | `X-RateLimit-Limit`     | Number of max requests allowed in the current time period  | | `X-RateLimit-Remaining` | Number of remaining requests in the current time period    | | `X-RateLimit-Reset`     | Timestamp of end of current time period as UNIX timestamp  | | `Retry-After`           | Seconds to delay after the first `429` is received         |  # CORS  This API features [Cross-Origin Resource Sharing (CORS)](https://fetch.spec.whatwg.org/), allowing cross-domain communication from the browser for some routes:  | Endpoint                    | |------------------------- ---| | `/api/_*`                    | | `/download/_*`               | | `/lazy-static/_*`            | | `/.well-known/webfinger`    |  In addition, all routes serving ActivityPub are CORS-enabled for all origins. 
 *
 * The version of the OpenAPI document: 5.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import java.math.BigDecimal;
import java.io.File;
import org.openapitools.client.model.GetAccountVideosCategoryOneOfParameter;
import org.openapitools.client.model.GetAccountVideosLanguageOneOfParameter;
import org.openapitools.client.model.GetAccountVideosLicenceOneOfParameter;
import org.openapitools.client.model.GetAccountVideosTagsAllOfParameter;
import org.openapitools.client.model.GetAccountVideosTagsOneOfParameter;
import org.openapitools.client.model.GetLiveIdIdParameter;
import org.openapitools.client.model.LiveVideoLatencyMode;
import org.openapitools.client.model.LiveVideoReplaySettings;
import org.openapitools.client.model.LiveVideoResponse;
import org.openapitools.client.model.LiveVideoUpdate;
import java.time.OffsetDateTime;
import org.openapitools.client.model.UserViewingVideo;
import org.openapitools.client.model.VideoDetails;
import org.openapitools.client.model.VideoListResponse;
import org.openapitools.client.model.VideoPrivacySet;
import org.openapitools.client.model.VideoScheduledUpdate;
import org.openapitools.client.model.VideoSource;
import org.openapitools.client.model.VideoTokenResponse;
import org.openapitools.client.model.VideoUploadRequestResumable;
import org.openapitools.client.model.VideoUploadResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for VideoApi
 */
@Disabled
public class VideoApiTest {

    private final VideoApi api = new VideoApi();

    /**
     * Create a live
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addLive_0Test() throws ApiException {
        Integer channelId = null;
        String name = null;
        Integer category = null;
        Boolean commentsEnabled = null;
        String description = null;
        Boolean downloadEnabled = null;
        String language = null;
        LiveVideoLatencyMode latencyMode = null;
        Integer licence = null;
        Boolean nsfw = null;
        Boolean permanentLive = null;
        File previewfile = null;
        VideoPrivacySet privacy = null;
        LiveVideoReplaySettings replaySettings = null;
        Boolean saveReplay = null;
        String support = null;
        List<String> tags = null;
        File thumbnailfile = null;
        VideoUploadResponse response = api.addLive_0(channelId, name, category, commentsEnabled, description, downloadEnabled, language, latencyMode, licence, nsfw, permanentLive, previewfile, privacy, replaySettings, saveReplay, support, tags, thumbnailfile);
        // TODO: test validations
    }

    /**
     * Notify user is watching a video
     *
     * Call this endpoint regularly (every 5-10 seconds for example) to notify the server the user is watching the video. After a while, PeerTube will increase video&#39;s viewers counter. If the user is authenticated, PeerTube will also store the current player time.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addViewTest() throws ApiException {
        GetLiveIdIdParameter id = null;
        UserViewingVideo userViewingVideo = null;
        api.addView(id, userViewingVideo);
        // TODO: test validations
    }

    /**
     * Create a studio task
     *
     * Create a task to edit a video  (cut, add intro/outro etc)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV1VideosIdStudioEditPost_0Test() throws ApiException {
        GetLiveIdIdParameter id = null;
        api.apiV1VideosIdStudioEditPost_0(id);
        // TODO: test validations
    }

    /**
     * Set watching progress of a video
     *
     * This endpoint has been deprecated. Use &#x60;/videos/{id}/views&#x60; instead
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV1VideosIdWatchingPutTest() throws ApiException {
        GetLiveIdIdParameter id = null;
        UserViewingVideo userViewingVideo = null;
        api.apiV1VideosIdWatchingPut(id, userViewingVideo);
        // TODO: test validations
    }

    /**
     * Delete a video
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void delVideoTest() throws ApiException {
        GetLiveIdIdParameter id = null;
        api.delVideo(id);
        // TODO: test validations
    }

    /**
     * List videos of an account
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAccountVideos_0Test() throws ApiException {
        String name = null;
        GetAccountVideosCategoryOneOfParameter categoryOneOf = null;
        Boolean isLive = null;
        GetAccountVideosTagsOneOfParameter tagsOneOf = null;
        GetAccountVideosTagsAllOfParameter tagsAllOf = null;
        GetAccountVideosLicenceOneOfParameter licenceOneOf = null;
        GetAccountVideosLanguageOneOfParameter languageOneOf = null;
        String nsfw = null;
        Boolean isLocal = null;
        Integer include = null;
        VideoPrivacySet privacyOneOf = null;
        Boolean hasHLSFiles = null;
        Boolean hasWebtorrentFiles = null;
        String skipCount = null;
        Integer start = null;
        Integer count = null;
        String sort = null;
        Boolean excludeAlreadyWatched = null;
        VideoListResponse response = api.getAccountVideos_0(name, categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched);
        // TODO: test validations
    }

    /**
     * List available video categories
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getCategoriesTest() throws ApiException {
        List<String> response = api.getCategories();
        // TODO: test validations
    }

    /**
     * List available video languages
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLanguagesTest() throws ApiException {
        List<String> response = api.getLanguages();
        // TODO: test validations
    }

    /**
     * List available video licences
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLicencesTest() throws ApiException {
        List<String> response = api.getLicences();
        // TODO: test validations
    }

    /**
     * Get information about a live
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLiveId_0Test() throws ApiException {
        GetLiveIdIdParameter id = null;
        LiveVideoResponse response = api.getLiveId_0(id);
        // TODO: test validations
    }

    /**
     * Get a video
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getVideoTest() throws ApiException {
        GetLiveIdIdParameter id = null;
        VideoDetails response = api.getVideo(id);
        // TODO: test validations
    }

    /**
     * List videos of a video channel
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getVideoChannelVideosTest() throws ApiException {
        String channelHandle = null;
        GetAccountVideosCategoryOneOfParameter categoryOneOf = null;
        Boolean isLive = null;
        GetAccountVideosTagsOneOfParameter tagsOneOf = null;
        GetAccountVideosTagsAllOfParameter tagsAllOf = null;
        GetAccountVideosLicenceOneOfParameter licenceOneOf = null;
        GetAccountVideosLanguageOneOfParameter languageOneOf = null;
        String nsfw = null;
        Boolean isLocal = null;
        Integer include = null;
        VideoPrivacySet privacyOneOf = null;
        Boolean hasHLSFiles = null;
        Boolean hasWebtorrentFiles = null;
        String skipCount = null;
        Integer start = null;
        Integer count = null;
        String sort = null;
        Boolean excludeAlreadyWatched = null;
        VideoListResponse response = api.getVideoChannelVideos(channelHandle, categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched);
        // TODO: test validations
    }

    /**
     * Get complete video description
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getVideoDescTest() throws ApiException {
        GetLiveIdIdParameter id = null;
        String response = api.getVideoDesc(id);
        // TODO: test validations
    }

    /**
     * List available video privacy policies
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getVideoPrivacyPoliciesTest() throws ApiException {
        List<String> response = api.getVideoPrivacyPolicies();
        // TODO: test validations
    }

    /**
     * Get video source file metadata
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getVideoSourceTest() throws ApiException {
        GetLiveIdIdParameter id = null;
        VideoSource response = api.getVideoSource(id);
        // TODO: test validations
    }

    /**
     * List videos
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getVideosTest() throws ApiException {
        GetAccountVideosCategoryOneOfParameter categoryOneOf = null;
        Boolean isLive = null;
        GetAccountVideosTagsOneOfParameter tagsOneOf = null;
        GetAccountVideosTagsAllOfParameter tagsAllOf = null;
        GetAccountVideosLicenceOneOfParameter licenceOneOf = null;
        GetAccountVideosLanguageOneOfParameter languageOneOf = null;
        String nsfw = null;
        Boolean isLocal = null;
        Integer include = null;
        VideoPrivacySet privacyOneOf = null;
        Boolean hasHLSFiles = null;
        Boolean hasWebtorrentFiles = null;
        String skipCount = null;
        Integer start = null;
        Integer count = null;
        String sort = null;
        Boolean excludeAlreadyWatched = null;
        VideoListResponse response = api.getVideos(categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched);
        // TODO: test validations
    }

    /**
     * Update a video
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putVideoTest() throws ApiException {
        GetLiveIdIdParameter id = null;
        Integer category = null;
        Boolean commentsEnabled = null;
        String description = null;
        Boolean downloadEnabled = null;
        String language = null;
        Integer licence = null;
        String name = null;
        Boolean nsfw = null;
        OffsetDateTime originallyPublishedAt = null;
        File previewfile = null;
        VideoPrivacySet privacy = null;
        VideoScheduledUpdate scheduleUpdate = null;
        String support = null;
        List<String> tags = null;
        File thumbnailfile = null;
        String waitTranscoding = null;
        api.putVideo(id, category, commentsEnabled, description, downloadEnabled, language, licence, name, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding);
        // TODO: test validations
    }

    /**
     * Request video token
     *
     * Request special tokens that expire quickly to use them in some context (like accessing private static files)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void requestVideoTokenTest() throws ApiException {
        GetLiveIdIdParameter id = null;
        VideoTokenResponse response = api.requestVideoToken(id);
        // TODO: test validations
    }

    /**
     * Update information about a live
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateLiveId_0Test() throws ApiException {
        GetLiveIdIdParameter id = null;
        LiveVideoUpdate liveVideoUpdate = null;
        api.updateLiveId_0(id, liveVideoUpdate);
        // TODO: test validations
    }

    /**
     * Upload a video
     *
     * Uses a single request to upload a video.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void uploadLegacyTest() throws ApiException {
        Integer channelId = null;
        String name = null;
        File videofile = null;
        Integer category = null;
        Boolean commentsEnabled = null;
        String description = null;
        Boolean downloadEnabled = null;
        String language = null;
        Integer licence = null;
        Boolean nsfw = null;
        OffsetDateTime originallyPublishedAt = null;
        File previewfile = null;
        VideoPrivacySet privacy = null;
        VideoScheduledUpdate scheduleUpdate = null;
        String support = null;
        Set<String> tags = null;
        File thumbnailfile = null;
        Boolean waitTranscoding = null;
        VideoUploadResponse response = api.uploadLegacy(channelId, name, videofile, category, commentsEnabled, description, downloadEnabled, language, licence, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding);
        // TODO: test validations
    }

    /**
     * Send chunk for the resumable upload of a video
     *
     * Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to continue, pause or resume the upload of a video
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void uploadResumableTest() throws ApiException {
        String uploadId = null;
        String contentRange = null;
        BigDecimal contentLength = null;
        File body = null;
        VideoUploadResponse response = api.uploadResumable(uploadId, contentRange, contentLength, body);
        // TODO: test validations
    }

    /**
     * Cancel the resumable upload of a video, deleting any data uploaded so far
     *
     * Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to cancel the upload of a video
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void uploadResumableCancelTest() throws ApiException {
        String uploadId = null;
        BigDecimal contentLength = null;
        api.uploadResumableCancel(uploadId, contentLength);
        // TODO: test validations
    }

    /**
     * Initialize the resumable upload of a video
     *
     * Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to initialize the upload of a video
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void uploadResumableInitTest() throws ApiException {
        BigDecimal xUploadContentLength = null;
        String xUploadContentType = null;
        VideoUploadRequestResumable videoUploadRequestResumable = null;
        api.uploadResumableInit(xUploadContentLength, xUploadContentType, videoUploadRequestResumable);
        // TODO: test validations
    }

}
