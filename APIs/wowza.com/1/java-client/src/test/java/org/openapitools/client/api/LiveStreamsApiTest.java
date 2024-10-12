/*
 * Wowza Streaming Cloud REST API Reference Documentation
 *  # About the REST API  The Wowza Streaming Cloud<sup>TM</sup> REST API (application programming interface) offers complete programmatic control over live streams, transcoders, stream sources, and stream targets. Anything you can do in the Wowza Streaming Cloud UI can also be achieved by making HTTP-based requests to cloud-based servers through the REST API.  The Wowza Streaming Cloud REST API features *cross-origin resource sharing*, or CORS. CORS is a [W3C specification](https://www.w3.org/TR/cors/) that provides headers in HTTP requests to enable a web server to safely make a network request to another domain.  In order to protect shared resources, the Wowza Streaming Cloud REST API is subject to limits. For details, see [Wowza Streaming Cloud REST API limits](https://www.wowza.com/docs/wowza-streaming-cloud-rest-api-limits). # About this documentation This reference documentation is based on the open-source [Swagger framework](http://swagger.io/specification/). It allows you to view the operations, parameters, and request and reponse schemas for every resource. Request samples are presented in cURL (Shell) and JavaScript; some samples also include just the JSON object. Response samples are all JSON.  For more information and examples on using the Wowza Streaming Cloud REST API, see our [library of Wowza Streaming Cloud REST API technical articles](https://www.wowza.com/docs/wowza-streaming-cloud-rest-api).  # Query requirements The Wowza Streaming Cloud REST API uses HTTP requests to retrieve data from cloud-based servers. Requests must contain proper JSON, two authentication keys, and the correct version number in the base path.  ## JSON The Wowza Streaming Cloud REST API uses the [JSON API specification](http://jsonapi.org/format/) to request and return data. This means requests must include the header `Content-Type: application/json` and must include a single resource object in JSON format as primary data.  Responses include HTTP status codes that indicate whether the query was successful. If there was an error, a description explains the problem so that you can fix it and try again.  ## Authentication Requests to the Wowza Streaming Cloud REST API must be authenticated with two keys: an API key and an access key. Each key is a 64-character alphanumeric string that you can find on the **API Access** page in Wowza Streaming Cloud.  Use the `wsc-api-key` and `wsc-access-key` headers to authenticate requests, like this (in cURL):  ```bash curl -H 'wsc-api-key: [64-character-api-key-goes-here]' -H 'wsc-access-key: [64-character-access-key-goes-here]' ```  <!-- ReDoc-Inject: <security-definitions> -->  ## Version The Wowza Streaming Cloud API is currently at version 1.0.0. Use `v1` in your base path in every request, like this path to the live_streams endpoint: ``` https://api.cloud.wowza.com/api/v1/live_streams ``` ## Example query Here is a complete example POST request, in cURL, with proper JSON syntax, headers, authentication, and version information: ```bash curl -H 'wsc-api-key: [64-character-api-key-goes-here]' -H 'wsc-access-key: [64-character-access-key-goes-here]'   -H 'Content-Type: application/json' -X POST -d '{     \"live_stream\": {       \"name\": \"My live Stream\",       \"...\": \"...\"     }   }' https://api.cloud.wowza.com/api/v1/live_streams ``` 
 *
 * The version of the OpenAPI document: 1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.CreateLiveStream200Response;
import org.openapitools.client.model.Error401;
import org.openapitools.client.model.Error403;
import org.openapitools.client.model.Error404;
import org.openapitools.client.model.Error410;
import org.openapitools.client.model.Error422;
import org.openapitools.client.model.LiveStreamCreateInput;
import org.openapitools.client.model.LiveStreamUpdateInput;
import org.openapitools.client.model.LiveStreams;
import org.openapitools.client.model.RegenerateConnectionCodeLiveStream200Response;
import org.openapitools.client.model.ResetLiveStream200Response;
import org.openapitools.client.model.ShowLiveStreamState200Response;
import org.openapitools.client.model.ShowLiveStreamStats200Response;
import org.openapitools.client.model.ShowLiveStreamThumbnailUrl200Response;
import org.openapitools.client.model.StartLiveStream200Response;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for LiveStreamsApi
 */
@Disabled
public class LiveStreamsApiTest {

    private final LiveStreamsApi api = new LiveStreamsApi();

    /**
     * Create a live stream
     *
     * This operation creates a live stream.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createLiveStreamTest() throws ApiException {
        LiveStreamCreateInput liveStream = null;
        CreateLiveStream200Response response = api.createLiveStream(liveStream);
        // TODO: test validations
    }

    /**
     * Delete a live stream
     *
     * This operation deletes a live stream, including all assigned outputs and targets.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteLiveStreamTest() throws ApiException {
        String id = null;
        api.deleteLiveStream(id);
        // TODO: test validations
    }

    /**
     * Fetch all live streams
     *
     * This operation shows the details of all of your live streams.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listLiveStreamsTest() throws ApiException {
        Integer page = null;
        Integer perPage = null;
        LiveStreams response = api.listLiveStreams(page, perPage);
        // TODO: test validations
    }

    /**
     * Regenerate the connection code for a live stream
     *
     * This operation regenerates the connection code of a live stream.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void regenerateConnectionCodeLiveStreamTest() throws ApiException {
        String id = null;
        RegenerateConnectionCodeLiveStream200Response response = api.regenerateConnectionCodeLiveStream(id);
        // TODO: test validations
    }

    /**
     * Reset a live stream
     *
     * This operation resets a live stream.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void resetLiveStreamTest() throws ApiException {
        String id = null;
        ResetLiveStream200Response response = api.resetLiveStream(id);
        // TODO: test validations
    }

    /**
     * Fetch a live stream
     *
     * This operation shows the details of a specific live stream.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void showLiveStreamTest() throws ApiException {
        String id = null;
        CreateLiveStream200Response response = api.showLiveStream(id);
        // TODO: test validations
    }

    /**
     * Fetch the state of a live stream
     *
     * This operation shows the current state of a live stream.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void showLiveStreamStateTest() throws ApiException {
        String id = null;
        ShowLiveStreamState200Response response = api.showLiveStreamState(id);
        // TODO: test validations
    }

    /**
     * Fetch metrics for an active live stream
     *
     * This operation returns a hash of metrics keys, each of which identifies a status, text description, unit, and value.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void showLiveStreamStatsTest() throws ApiException {
        String id = null;
        ShowLiveStreamStats200Response response = api.showLiveStreamStats(id);
        // TODO: test validations
    }

    /**
     * Fetch the thumbnail URL of a live stream
     *
     * This operation shows the thumbnail URL of a started live stream.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void showLiveStreamThumbnailUrlTest() throws ApiException {
        String id = null;
        ShowLiveStreamThumbnailUrl200Response response = api.showLiveStreamThumbnailUrl(id);
        // TODO: test validations
    }

    /**
     * Start a live stream
     *
     * This operation starts a live stream.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void startLiveStreamTest() throws ApiException {
        String id = null;
        StartLiveStream200Response response = api.startLiveStream(id);
        // TODO: test validations
    }

    /**
     * Stop a live stream
     *
     * This operation stops a live stream.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void stopLiveStreamTest() throws ApiException {
        String id = null;
        ShowLiveStreamState200Response response = api.stopLiveStream(id);
        // TODO: test validations
    }

    /**
     * Update a live stream
     *
     * This operation updates a live stream.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateLiveStreamTest() throws ApiException {
        String id = null;
        LiveStreamUpdateInput liveStream = null;
        CreateLiveStream200Response response = api.updateLiveStream(id, liveStream);
        // TODO: test validations
    }

}
