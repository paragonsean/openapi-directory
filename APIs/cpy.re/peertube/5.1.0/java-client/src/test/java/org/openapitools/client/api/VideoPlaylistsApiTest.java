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
import org.openapitools.client.model.AddPlaylist200Response;
import org.openapitools.client.model.AddVideoPlaylistVideo200Response;
import org.openapitools.client.model.AddVideoPlaylistVideoRequest;
import org.openapitools.client.model.ApiV1AccountsNameVideoPlaylistsGet200Response;
import org.openapitools.client.model.ApiV1UsersMeVideoPlaylistsVideosExistGet200Response;
import java.io.File;
import org.openapitools.client.model.PutVideoPlaylistVideoRequest;
import org.openapitools.client.model.ReorderVideoPlaylistRequest;
import org.openapitools.client.model.VideoListResponse;
import org.openapitools.client.model.VideoPlaylist;
import org.openapitools.client.model.VideoPlaylistPrivacySet;
import org.openapitools.client.model.VideoPlaylistTypeSet;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for VideoPlaylistsApi
 */
@Disabled
public class VideoPlaylistsApiTest {

    private final VideoPlaylistsApi api = new VideoPlaylistsApi();

    /**
     * Create a video playlist
     *
     * If the video playlist is set as public, &#x60;videoChannelId&#x60; is mandatory.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addPlaylistTest() throws ApiException {
        String displayName = null;
        String description = null;
        VideoPlaylistPrivacySet privacy = null;
        File thumbnailfile = null;
        Integer videoChannelId = null;
        AddPlaylist200Response response = api.addPlaylist(displayName, description, privacy, thumbnailfile, videoChannelId);
        // TODO: test validations
    }

    /**
     * Add a video in a playlist
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addVideoPlaylistVideo_0Test() throws ApiException {
        Integer playlistId = null;
        AddVideoPlaylistVideoRequest addVideoPlaylistVideoRequest = null;
        AddVideoPlaylistVideo200Response response = api.addVideoPlaylistVideo_0(playlistId, addVideoPlaylistVideoRequest);
        // TODO: test validations
    }

    /**
     * List playlists of an account
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV1AccountsNameVideoPlaylistsGetTest() throws ApiException {
        String name = null;
        Integer start = null;
        Integer count = null;
        String sort = null;
        String search = null;
        VideoPlaylistTypeSet playlistType = null;
        ApiV1AccountsNameVideoPlaylistsGet200Response response = api.apiV1AccountsNameVideoPlaylistsGet(name, start, count, sort, search, playlistType);
        // TODO: test validations
    }

    /**
     * Check video exists in my playlists
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV1UsersMeVideoPlaylistsVideosExistGetTest() throws ApiException {
        List<Integer> videoIds = null;
        ApiV1UsersMeVideoPlaylistsVideosExistGet200Response response = api.apiV1UsersMeVideoPlaylistsVideosExistGet(videoIds);
        // TODO: test validations
    }

    /**
     * List playlists of a channel
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV1VideoChannelsChannelHandleVideoPlaylistsGetTest() throws ApiException {
        String channelHandle = null;
        Integer start = null;
        Integer count = null;
        String sort = null;
        VideoPlaylistTypeSet playlistType = null;
        ApiV1AccountsNameVideoPlaylistsGet200Response response = api.apiV1VideoChannelsChannelHandleVideoPlaylistsGet(channelHandle, start, count, sort, playlistType);
        // TODO: test validations
    }

    /**
     * Delete a video playlist
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV1VideoPlaylistsPlaylistIdDeleteTest() throws ApiException {
        Integer playlistId = null;
        api.apiV1VideoPlaylistsPlaylistIdDelete(playlistId);
        // TODO: test validations
    }

    /**
     * Get a video playlist
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV1VideoPlaylistsPlaylistIdGetTest() throws ApiException {
        Integer playlistId = null;
        VideoPlaylist response = api.apiV1VideoPlaylistsPlaylistIdGet(playlistId);
        // TODO: test validations
    }

    /**
     * Update a video playlist
     *
     * If the video playlist is set as public, the playlist must have a assigned channel.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV1VideoPlaylistsPlaylistIdPutTest() throws ApiException {
        Integer playlistId = null;
        String description = null;
        String displayName = null;
        VideoPlaylistPrivacySet privacy = null;
        File thumbnailfile = null;
        Integer videoChannelId = null;
        api.apiV1VideoPlaylistsPlaylistIdPut(playlistId, description, displayName, privacy, thumbnailfile, videoChannelId);
        // TODO: test validations
    }

    /**
     * Delete an element from a playlist
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void delVideoPlaylistVideoTest() throws ApiException {
        Integer playlistId = null;
        Integer playlistElementId = null;
        api.delVideoPlaylistVideo(playlistId, playlistElementId);
        // TODO: test validations
    }

    /**
     * List available playlist privacy policies
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPlaylistPrivacyPoliciesTest() throws ApiException {
        List<String> response = api.getPlaylistPrivacyPolicies();
        // TODO: test validations
    }

    /**
     * List video playlists
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPlaylistsTest() throws ApiException {
        Integer start = null;
        Integer count = null;
        String sort = null;
        VideoPlaylistTypeSet playlistType = null;
        ApiV1AccountsNameVideoPlaylistsGet200Response response = api.getPlaylists(start, count, sort, playlistType);
        // TODO: test validations
    }

    /**
     * List videos of a playlist
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getVideoPlaylistVideos_0Test() throws ApiException {
        Integer playlistId = null;
        Integer start = null;
        Integer count = null;
        VideoListResponse response = api.getVideoPlaylistVideos_0(playlistId, start, count);
        // TODO: test validations
    }

    /**
     * Update a playlist element
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putVideoPlaylistVideoTest() throws ApiException {
        Integer playlistId = null;
        Integer playlistElementId = null;
        PutVideoPlaylistVideoRequest putVideoPlaylistVideoRequest = null;
        api.putVideoPlaylistVideo(playlistId, playlistElementId, putVideoPlaylistVideoRequest);
        // TODO: test validations
    }

    /**
     * Reorder a playlist
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void reorderVideoPlaylistTest() throws ApiException {
        Integer playlistId = null;
        ReorderVideoPlaylistRequest reorderVideoPlaylistRequest = null;
        api.reorderVideoPlaylist(playlistId, reorderVideoPlaylistRequest);
        // TODO: test validations
    }

}
