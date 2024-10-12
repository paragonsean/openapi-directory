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
import org.openapitools.client.model.AddStreamTargetToTranscoderOutput200Response;
import org.openapitools.client.model.CreateTranscoder200Response;
import org.openapitools.client.model.CreateTranscoderOutput200Response;
import org.openapitools.client.model.CreateTranscoderProperty200Response;
import org.openapitools.client.model.DisableAllStreamTargetsTranscoder200Response;
import org.openapitools.client.model.DisableTranscoderOutputOutputStreamTarget200Response;
import org.openapitools.client.model.EnableTranscoderOutputOutputStreamTarget200Response;
import org.openapitools.client.model.Error401;
import org.openapitools.client.model.Error403;
import org.openapitools.client.model.Error404;
import org.openapitools.client.model.Error410;
import org.openapitools.client.model.Error422;
import org.openapitools.client.model.ListTranscoderRecordings200Response;
import org.openapitools.client.model.ListTranscoderSchedules200Response;
import org.openapitools.client.model.OutputAddStreamTargetInput;
import org.openapitools.client.model.OutputCreateInput;
import org.openapitools.client.model.OutputRemoveStreamTargetInput;
import org.openapitools.client.model.OutputStreamTarget;
import org.openapitools.client.model.OutputStreamTargetCreateInput;
import org.openapitools.client.model.OutputStreamTargetUpdateInput;
import org.openapitools.client.model.OutputUpdateInput;
import org.openapitools.client.model.Outputs;
import org.openapitools.client.model.ResetTranscoder200Response;
import org.openapitools.client.model.RestartTranscoderOutputOutputStreamTarget200Response;
import org.openapitools.client.model.ShowTranscoderState200Response;
import org.openapitools.client.model.ShowTranscoderStats200Response;
import org.openapitools.client.model.ShowTranscoderThumbnailUrl200Response;
import org.openapitools.client.model.ShowUptimeMetricsCurrent200Response;
import org.openapitools.client.model.ShowUptimeMetricsHistoric200Response;
import org.openapitools.client.model.StartTranscoder200Response;
import org.openapitools.client.model.TranscoderCreateInput;
import org.openapitools.client.model.TranscoderProperties;
import org.openapitools.client.model.TranscoderPropertyCreateInput;
import org.openapitools.client.model.TranscoderUpdateInput;
import org.openapitools.client.model.Transcoders;
import org.openapitools.client.model.Uptime;
import org.openapitools.client.model.Uptimes;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for TranscodersApi
 */
@Disabled
public class TranscodersApiTest {

    private final TranscodersApi api = new TranscodersApi();

    /**
     * Deprecated operation
     *
     * The operation POST /transcoders/{transcoder_id}/outputs/{id}/add_stream_target is deprecated. Use POST /transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets to add an existing stream target to an output.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addStreamTargetToTranscoderOutputTest() throws ApiException {
        String transcoderId = null;
        String id = null;
        OutputAddStreamTargetInput outputStreamTarget = null;
        AddStreamTargetToTranscoderOutput200Response response = api.addStreamTargetToTranscoderOutput(transcoderId, id, outputStreamTarget);
        // TODO: test validations
    }

    /**
     * Create a transcoder
     *
     * This operation creates a transcoder.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createTranscoderTest() throws ApiException {
        TranscoderCreateInput transcoder = null;
        CreateTranscoder200Response response = api.createTranscoder(transcoder);
        // TODO: test validations
    }

    /**
     * Create an output
     *
     * This operation creates an output rendition for a specific transcoder.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createTranscoderOutputTest() throws ApiException {
        String transcoderId = null;
        OutputCreateInput output = null;
        CreateTranscoderOutput200Response response = api.createTranscoderOutput(transcoderId, output);
        // TODO: test validations
    }

    /**
     * Create an output stream target
     *
     * This operation creates an output stream target. Targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt; can&#39;t be added to output renditions.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createTranscoderOutputOutputStreamTargetTest() throws ApiException {
        String transcoderId = null;
        String outputId = null;
        OutputStreamTargetCreateInput outputStreamTarget = null;
        AddStreamTargetToTranscoderOutput200Response response = api.createTranscoderOutputOutputStreamTarget(transcoderId, outputId, outputStreamTarget);
        // TODO: test validations
    }

    /**
     * Create a property for a transcoder
     *
     * This operation creates a property for a transcoder. For more information see the technical article [How to set advanced properties by using the Wowza Streaming Cloud REST API](https://www.wowza.com/docs/how-to-set-advanced-properties-by-using-the-wowza-streaming-cloud-rest-api).
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createTranscoderPropertyTest() throws ApiException {
        String transcoderId = null;
        TranscoderPropertyCreateInput property = null;
        CreateTranscoderProperty200Response response = api.createTranscoderProperty(transcoderId, property);
        // TODO: test validations
    }

    /**
     * Delete a transcoder
     *
     * This operation deletes a transcoder, including all of its assigned output renditions and stream targets.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteTranscoderTest() throws ApiException {
        String id = null;
        api.deleteTranscoder(id);
        // TODO: test validations
    }

    /**
     * Delete an output
     *
     * This operation deletes an output, including all of its assigned targets.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteTranscoderOutputTest() throws ApiException {
        String transcoderId = null;
        String id = null;
        api.deleteTranscoderOutput(transcoderId, id);
        // TODO: test validations
    }

    /**
     * Delete an output stream target
     *
     * This operation deletes an output stream target, including all of its assigned targets.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteTranscoderOutputOutputStreamTargetTest() throws ApiException {
        String transcoderId = null;
        String outputId = null;
        String streamTargetId = null;
        api.deleteTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId);
        // TODO: test validations
    }

    /**
     * Delete a transcoder&#39;s property
     *
     * This operation deletes a specific property from a specific transcoder.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteTranscoderPropertyTest() throws ApiException {
        String transcoderId = null;
        String id = null;
        api.deleteTranscoderProperty(transcoderId, id);
        // TODO: test validations
    }

    /**
     * Disable a transcoder&#39;s stream targets
     *
     * This operation disables all of the stream targets assigned to a specific transcoder.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void disableAllStreamTargetsTranscoderTest() throws ApiException {
        String id = null;
        DisableAllStreamTargetsTranscoder200Response response = api.disableAllStreamTargetsTranscoder(id);
        // TODO: test validations
    }

    /**
     * Disable an output stream target
     *
     * This operation disables an output stream target.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void disableTranscoderOutputOutputStreamTargetTest() throws ApiException {
        String transcoderId = null;
        String outputId = null;
        String streamTargetId = null;
        DisableTranscoderOutputOutputStreamTarget200Response response = api.disableTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId);
        // TODO: test validations
    }

    /**
     * Enable a transcoder&#39;s stream targets
     *
     * This operation enables all of the stream targets assigned to a specific transcoder.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void enableAllStreamTargetsTranscoderTest() throws ApiException {
        String id = null;
        DisableAllStreamTargetsTranscoder200Response response = api.enableAllStreamTargetsTranscoder(id);
        // TODO: test validations
    }

    /**
     * Enable an output stream target
     *
     * This operation enables an output stream target.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void enableTranscoderOutputOutputStreamTargetTest() throws ApiException {
        String transcoderId = null;
        String outputId = null;
        String streamTargetId = null;
        EnableTranscoderOutputOutputStreamTarget200Response response = api.enableTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId);
        // TODO: test validations
    }

    /**
     * Fetch all uptime records for a transcoder
     *
     * This operation shows all of the uptime records for a specific transcoder. An &lt;em&gt;uptime record&lt;/em&gt; identifies a specific transcoding session.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void indexUptimesTest() throws ApiException {
        String transcoderId = null;
        Integer page = null;
        Integer perPage = null;
        Uptimes response = api.indexUptimes(transcoderId, page, perPage);
        // TODO: test validations
    }

    /**
     * Fetch all output stream targets of an output of a transcoder
     *
     * This operation shows the details of all of the output stream targets of an output of a transcoder.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listTranscoderOutputOutputStreamTargetsTest() throws ApiException {
        String transcoderId = null;
        String outputId = null;
        OutputStreamTarget response = api.listTranscoderOutputOutputStreamTargets(transcoderId, outputId);
        // TODO: test validations
    }

    /**
     * Fetch all outputs of a transcoder
     *
     * This operation shows the details of all of the output renditions of a specific transcoder.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listTranscoderOutputsTest() throws ApiException {
        String transcoderId = null;
        Outputs response = api.listTranscoderOutputs(transcoderId);
        // TODO: test validations
    }

    /**
     * Fetch a transcoder&#39;s properties
     *
     * This operation shows all of the properties of a specific transcoder.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listTranscoderPropertiesTest() throws ApiException {
        String transcoderId = null;
        TranscoderProperties response = api.listTranscoderProperties(transcoderId);
        // TODO: test validations
    }

    /**
     * Fetch a transcoder&#39;s recordings
     *
     * This operation shows the details of all of the recordings for a specific transcoder.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listTranscoderRecordingsTest() throws ApiException {
        String id = null;
        ListTranscoderRecordings200Response response = api.listTranscoderRecordings(id);
        // TODO: test validations
    }

    /**
     * Fetch transcoder&#39;s schedules
     *
     * This operation shows the details of all of the schedules for a specific transcoder.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listTranscoderSchedulesTest() throws ApiException {
        String id = null;
        ListTranscoderSchedules200Response response = api.listTranscoderSchedules(id);
        // TODO: test validations
    }

    /**
     * Fetch all transcoders
     *
     * This operation shows the details of all of your transcoders.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listTranscodersTest() throws ApiException {
        Integer page = null;
        Integer perPage = null;
        Transcoders response = api.listTranscoders(page, perPage);
        // TODO: test validations
    }

    /**
     * Deprecated operation
     *
     * The operation DELETE /transcoders/{transcoder_id}/outputs/{id}/remove_stream_target is deprecated. Use DELETE /transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets/{id} to remove a stream target from an output.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void removeStreamTargetToTranscoderOutputTest() throws ApiException {
        String transcoderId = null;
        String id = null;
        OutputRemoveStreamTargetInput outputStreamTarget = null;
        api.removeStreamTargetToTranscoderOutput(transcoderId, id, outputStreamTarget);
        // TODO: test validations
    }

    /**
     * Reset a transcoder
     *
     * This operation resets a transcoder.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void resetTranscoderTest() throws ApiException {
        String id = null;
        ResetTranscoder200Response response = api.resetTranscoder(id);
        // TODO: test validations
    }

    /**
     * Restart an output stream target
     *
     * This operation restarts an output stream target.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void restartTranscoderOutputOutputStreamTargetTest() throws ApiException {
        String transcoderId = null;
        String outputId = null;
        String streamTargetId = null;
        RestartTranscoderOutputOutputStreamTarget200Response response = api.restartTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId);
        // TODO: test validations
    }

    /**
     * Fetch a transcoder
     *
     * This operation shows the details of a specific transcoder.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void showTranscoderTest() throws ApiException {
        String id = null;
        CreateTranscoder200Response response = api.showTranscoder(id);
        // TODO: test validations
    }

    /**
     * Fetch an output
     *
     * This operation shows the details of a specific output rendition for a specific transcoder.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void showTranscoderOutputTest() throws ApiException {
        String transcoderId = null;
        String id = null;
        CreateTranscoderOutput200Response response = api.showTranscoderOutput(transcoderId, id);
        // TODO: test validations
    }

    /**
     * Fetch an output stream target
     *
     * This operation shows the details of an output stream target.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void showTranscoderOutputOutputStreamTargetTest() throws ApiException {
        String transcoderId = null;
        String outputId = null;
        String streamTargetId = null;
        AddStreamTargetToTranscoderOutput200Response response = api.showTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId);
        // TODO: test validations
    }

    /**
     * Fetch a property for a transcoder
     *
     * This operation shows the details of a specific property for a specific transcoder.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void showTranscoderPropertyTest() throws ApiException {
        String transcoderId = null;
        String id = null;
        CreateTranscoderProperty200Response response = api.showTranscoderProperty(transcoderId, id);
        // TODO: test validations
    }

    /**
     * Fetch the state and uptime ID of a transcoder
     *
     * This operation shows the current state and uptime ID of a transcoder.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void showTranscoderStateTest() throws ApiException {
        String id = null;
        ShowTranscoderState200Response response = api.showTranscoderState(id);
        // TODO: test validations
    }

    /**
     * Fetch statistics for a current transcoder
     *
     * This operation responds with a hash of metrics (keys) for a currently running transcoder. Each key has a &lt;strong&gt;status&lt;/strong&gt;, &lt;strong&gt;text&lt;/strong&gt; (description), &lt;strong&gt;units&lt;/strong&gt;, and &lt;strong&gt;value&lt;/strong&gt;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void showTranscoderStatsTest() throws ApiException {
        String id = null;
        ShowTranscoderStats200Response response = api.showTranscoderStats(id);
        // TODO: test validations
    }

    /**
     * Fetch the thumbnail URL of a transcoder
     *
     * This operation shows the thumbnail URL of a started transcoder.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void showTranscoderThumbnailUrlTest() throws ApiException {
        String id = null;
        ShowTranscoderThumbnailUrl200Response response = api.showTranscoderThumbnailUrl(id);
        // TODO: test validations
    }

    /**
     * Fetch an uptime record
     *
     * This operation shows the details of a specific uptime record for a specific transcoder. An &lt;em&gt;uptime record&lt;/em&gt; identifies a transcoding session.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void showUptimeTest() throws ApiException {
        String transcoderId = null;
        String id = null;
        Uptime response = api.showUptime(transcoderId, id);
        // TODO: test validations
    }

    /**
     * Fetch current stream health metrics for an active transcoder
     *
     * This operation returns a snapshot of the current source connection and processing details of an active (running) transcoder.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void showUptimeMetricsCurrentTest() throws ApiException {
        String transcoderId = null;
        String id = null;
        String fields = null;
        ShowUptimeMetricsCurrent200Response response = api.showUptimeMetricsCurrent(transcoderId, id, fields);
        // TODO: test validations
    }

    /**
     * Fetch historic stream health metrics for a transcoder
     *
     * This operation shows the historic source connection and processing details for a transcoding session (uptime record). The transcoder can be running or stopped. Metrics are recorded every 20 seconds.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void showUptimeMetricsHistoricTest() throws ApiException {
        String transcoderId = null;
        String id = null;
        String fields = null;
        String from = null;
        String to = null;
        ShowUptimeMetricsHistoric200Response response = api.showUptimeMetricsHistoric(transcoderId, id, fields, from, to);
        // TODO: test validations
    }

    /**
     * Start a transcoder
     *
     * This operation starts a transcoder.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void startTranscoderTest() throws ApiException {
        String id = null;
        StartTranscoder200Response response = api.startTranscoder(id);
        // TODO: test validations
    }

    /**
     * Stop a transcoder
     *
     * This operation stops a transcoder.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void stopTranscoderTest() throws ApiException {
        String id = null;
        StartTranscoder200Response response = api.stopTranscoder(id);
        // TODO: test validations
    }

    /**
     * Update a transcoder
     *
     * This operation updates a transcoder.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateTranscoderTest() throws ApiException {
        String id = null;
        TranscoderUpdateInput transcoder = null;
        CreateTranscoder200Response response = api.updateTranscoder(id, transcoder);
        // TODO: test validations
    }

    /**
     * Update an output
     *
     * This operation updates an output rendition.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateTranscoderOutputTest() throws ApiException {
        String transcoderId = null;
        String id = null;
        OutputUpdateInput output = null;
        CreateTranscoderOutput200Response response = api.updateTranscoderOutput(transcoderId, id, output);
        // TODO: test validations
    }

    /**
     * Update an output stream target
     *
     * This operation updates an output stream target.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateTranscoderOutputOutputStreamTargetTest() throws ApiException {
        String transcoderId = null;
        String outputId = null;
        String streamTargetId = null;
        OutputStreamTargetUpdateInput outputStreamTarget = null;
        AddStreamTargetToTranscoderOutput200Response response = api.updateTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId, outputStreamTarget);
        // TODO: test validations
    }

}
