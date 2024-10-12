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
import org.openapitools.client.model.AddVideoChannel200Response;
import org.openapitools.client.model.ApiV1AccountsNameVideoPlaylistsGet200Response;
import org.openapitools.client.model.ApiV1UsersMeAvatarPickPost200Response;
import org.openapitools.client.model.ApiV1VideoChannelsChannelHandleBannerPickPost200Response;
import java.io.File;
import org.openapitools.client.model.GetAccountFollowers200Response;
import org.openapitools.client.model.GetAccountVideosCategoryOneOfParameter;
import org.openapitools.client.model.GetAccountVideosLanguageOneOfParameter;
import org.openapitools.client.model.GetAccountVideosLicenceOneOfParameter;
import org.openapitools.client.model.GetAccountVideosTagsAllOfParameter;
import org.openapitools.client.model.GetAccountVideosTagsOneOfParameter;
import org.openapitools.client.model.ImportVideosInChannelCreate;
import org.openapitools.client.model.VideoChannel;
import org.openapitools.client.model.VideoChannelCreate;
import org.openapitools.client.model.VideoChannelList;
import org.openapitools.client.model.VideoChannelSyncList;
import org.openapitools.client.model.VideoChannelUpdate;
import org.openapitools.client.model.VideoListResponse;
import org.openapitools.client.model.VideoPlaylistTypeSet;
import org.openapitools.client.model.VideoPrivacySet;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for VideoChannelsApi
 */
@Disabled
public class VideoChannelsApiTest {

    private final VideoChannelsApi api = new VideoChannelsApi();

    /**
     * Create a video channel
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addVideoChannelTest() throws ApiException {
        VideoChannelCreate videoChannelCreate = null;
        AddVideoChannel200Response response = api.addVideoChannel(videoChannelCreate);
        // TODO: test validations
    }

    /**
     * List the synchronizations of video channels of an account
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV1AccountsNameVideoChannelSyncsGetTest() throws ApiException {
        String name = null;
        Integer start = null;
        Integer count = null;
        String sort = null;
        VideoChannelSyncList response = api.apiV1AccountsNameVideoChannelSyncsGet(name, start, count, sort);
        // TODO: test validations
    }

    /**
     * List video channels of an account
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV1AccountsNameVideoChannelsGetTest() throws ApiException {
        String name = null;
        Boolean withStats = null;
        Integer start = null;
        Integer count = null;
        String sort = null;
        VideoChannelList response = api.apiV1AccountsNameVideoChannelsGet(name, withStats, start, count, sort);
        // TODO: test validations
    }

    /**
     * Delete channel avatar
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV1VideoChannelsChannelHandleAvatarDeleteTest() throws ApiException {
        String channelHandle = null;
        api.apiV1VideoChannelsChannelHandleAvatarDelete(channelHandle);
        // TODO: test validations
    }

    /**
     * Update channel avatar
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV1VideoChannelsChannelHandleAvatarPickPostTest() throws ApiException {
        String channelHandle = null;
        File avatarfile = null;
        ApiV1UsersMeAvatarPickPost200Response response = api.apiV1VideoChannelsChannelHandleAvatarPickPost(channelHandle, avatarfile);
        // TODO: test validations
    }

    /**
     * Delete channel banner
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV1VideoChannelsChannelHandleBannerDeleteTest() throws ApiException {
        String channelHandle = null;
        api.apiV1VideoChannelsChannelHandleBannerDelete(channelHandle);
        // TODO: test validations
    }

    /**
     * Update channel banner
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV1VideoChannelsChannelHandleBannerPickPostTest() throws ApiException {
        String channelHandle = null;
        File bannerfile = null;
        ApiV1VideoChannelsChannelHandleBannerPickPost200Response response = api.apiV1VideoChannelsChannelHandleBannerPickPost(channelHandle, bannerfile);
        // TODO: test validations
    }

    /**
     * Import videos in channel
     *
     * Import a remote channel/playlist videos into a channel
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV1VideoChannelsChannelHandleImportVideosPostTest() throws ApiException {
        String channelHandle = null;
        ImportVideosInChannelCreate importVideosInChannelCreate = null;
        api.apiV1VideoChannelsChannelHandleImportVideosPost(channelHandle, importVideosInChannelCreate);
        // TODO: test validations
    }

    /**
     * List playlists of a channel
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV1VideoChannelsChannelHandleVideoPlaylistsGet_0Test() throws ApiException {
        String channelHandle = null;
        Integer start = null;
        Integer count = null;
        String sort = null;
        VideoPlaylistTypeSet playlistType = null;
        ApiV1AccountsNameVideoPlaylistsGet200Response response = api.apiV1VideoChannelsChannelHandleVideoPlaylistsGet_0(channelHandle, start, count, sort, playlistType);
        // TODO: test validations
    }

    /**
     * Delete a video channel
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void delVideoChannelTest() throws ApiException {
        String channelHandle = null;
        api.delVideoChannel(channelHandle);
        // TODO: test validations
    }

    /**
     * Get a video channel
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getVideoChannelTest() throws ApiException {
        String channelHandle = null;
        VideoChannel response = api.getVideoChannel(channelHandle);
        // TODO: test validations
    }

    /**
     * List followers of a video channel
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getVideoChannelFollowersTest() throws ApiException {
        String channelHandle = null;
        Integer start = null;
        Integer count = null;
        String sort = null;
        String search = null;
        GetAccountFollowers200Response response = api.getVideoChannelFollowers(channelHandle, start, count, sort, search);
        // TODO: test validations
    }

    /**
     * List videos of a video channel
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getVideoChannelVideos_0Test() throws ApiException {
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
        VideoListResponse response = api.getVideoChannelVideos_0(channelHandle, categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched);
        // TODO: test validations
    }

    /**
     * List video channels
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getVideoChannelsTest() throws ApiException {
        Integer start = null;
        Integer count = null;
        String sort = null;
        VideoChannelList response = api.getVideoChannels(start, count, sort);
        // TODO: test validations
    }

    /**
     * Update a video channel
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putVideoChannelTest() throws ApiException {
        String channelHandle = null;
        VideoChannelUpdate videoChannelUpdate = null;
        api.putVideoChannel(channelHandle, videoChannelUpdate);
        // TODO: test validations
    }

}
