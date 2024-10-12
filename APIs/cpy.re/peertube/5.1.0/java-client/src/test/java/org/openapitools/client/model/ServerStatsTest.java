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


package org.openapitools.client.model;

import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.ServerStatsVideosRedundancyInner;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for ServerStats
 */
public class ServerStatsTest {
    private final ServerStats model = new ServerStats();

    /**
     * Model tests for ServerStats
     */
    @Test
    public void testServerStats() {
        // TODO: test ServerStats
    }

    /**
     * Test the property 'activityPubMessagesProcessedPerSecond'
     */
    @Test
    public void activityPubMessagesProcessedPerSecondTest() {
        // TODO: test activityPubMessagesProcessedPerSecond
    }

    /**
     * Test the property 'totalActivityPubMessagesErrors'
     */
    @Test
    public void totalActivityPubMessagesErrorsTest() {
        // TODO: test totalActivityPubMessagesErrors
    }

    /**
     * Test the property 'totalActivityPubMessagesProcessed'
     */
    @Test
    public void totalActivityPubMessagesProcessedTest() {
        // TODO: test totalActivityPubMessagesProcessed
    }

    /**
     * Test the property 'totalActivityPubMessagesSuccesses'
     */
    @Test
    public void totalActivityPubMessagesSuccessesTest() {
        // TODO: test totalActivityPubMessagesSuccesses
    }

    /**
     * Test the property 'totalActivityPubMessagesWaiting'
     */
    @Test
    public void totalActivityPubMessagesWaitingTest() {
        // TODO: test totalActivityPubMessagesWaiting
    }

    /**
     * Test the property 'totalDailyActiveUsers'
     */
    @Test
    public void totalDailyActiveUsersTest() {
        // TODO: test totalDailyActiveUsers
    }

    /**
     * Test the property 'totalInstanceFollowers'
     */
    @Test
    public void totalInstanceFollowersTest() {
        // TODO: test totalInstanceFollowers
    }

    /**
     * Test the property 'totalInstanceFollowing'
     */
    @Test
    public void totalInstanceFollowingTest() {
        // TODO: test totalInstanceFollowing
    }

    /**
     * Test the property 'totalLocalDailyActiveVideoChannels'
     */
    @Test
    public void totalLocalDailyActiveVideoChannelsTest() {
        // TODO: test totalLocalDailyActiveVideoChannels
    }

    /**
     * Test the property 'totalLocalMonthlyActiveVideoChannels'
     */
    @Test
    public void totalLocalMonthlyActiveVideoChannelsTest() {
        // TODO: test totalLocalMonthlyActiveVideoChannels
    }

    /**
     * Test the property 'totalLocalPlaylists'
     */
    @Test
    public void totalLocalPlaylistsTest() {
        // TODO: test totalLocalPlaylists
    }

    /**
     * Test the property 'totalLocalVideoChannels'
     */
    @Test
    public void totalLocalVideoChannelsTest() {
        // TODO: test totalLocalVideoChannels
    }

    /**
     * Test the property 'totalLocalVideoComments'
     */
    @Test
    public void totalLocalVideoCommentsTest() {
        // TODO: test totalLocalVideoComments
    }

    /**
     * Test the property 'totalLocalVideoFilesSize'
     */
    @Test
    public void totalLocalVideoFilesSizeTest() {
        // TODO: test totalLocalVideoFilesSize
    }

    /**
     * Test the property 'totalLocalVideoViews'
     */
    @Test
    public void totalLocalVideoViewsTest() {
        // TODO: test totalLocalVideoViews
    }

    /**
     * Test the property 'totalLocalVideos'
     */
    @Test
    public void totalLocalVideosTest() {
        // TODO: test totalLocalVideos
    }

    /**
     * Test the property 'totalLocalWeeklyActiveVideoChannels'
     */
    @Test
    public void totalLocalWeeklyActiveVideoChannelsTest() {
        // TODO: test totalLocalWeeklyActiveVideoChannels
    }

    /**
     * Test the property 'totalMonthlyActiveUsers'
     */
    @Test
    public void totalMonthlyActiveUsersTest() {
        // TODO: test totalMonthlyActiveUsers
    }

    /**
     * Test the property 'totalUsers'
     */
    @Test
    public void totalUsersTest() {
        // TODO: test totalUsers
    }

    /**
     * Test the property 'totalVideoComments'
     */
    @Test
    public void totalVideoCommentsTest() {
        // TODO: test totalVideoComments
    }

    /**
     * Test the property 'totalVideos'
     */
    @Test
    public void totalVideosTest() {
        // TODO: test totalVideos
    }

    /**
     * Test the property 'totalWeeklyActiveUsers'
     */
    @Test
    public void totalWeeklyActiveUsersTest() {
        // TODO: test totalWeeklyActiveUsers
    }

    /**
     * Test the property 'videosRedundancy'
     */
    @Test
    public void videosRedundancyTest() {
        // TODO: test videosRedundancy
    }

}
