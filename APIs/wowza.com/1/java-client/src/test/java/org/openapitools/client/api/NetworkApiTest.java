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
import org.openapitools.client.model.Error401;
import java.time.OffsetDateTime;
import org.openapitools.client.model.UsageNetworkStreamSources;
import org.openapitools.client.model.UsageNetworkStreamTargets;
import org.openapitools.client.model.UsageNetworkTranscoders;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for NetworkApi
 */
@Disabled
public class NetworkApiTest {

    private final NetworkApi api = new NetworkApi();

    /**
     * Fetch network usage for all stream sources
     *
     * This operation shows the amount of network usage for all stream sources in the account. The default time frame is &lt;em&gt;from&lt;/em&gt; the last billing date &lt;em&gt;to&lt;/em&gt; the end of the current day.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void usageNetworkStreamSourcesIndexTest() throws ApiException {
        OffsetDateTime from = null;
        OffsetDateTime to = null;
        UsageNetworkStreamSources response = api.usageNetworkStreamSourcesIndex(from, to);
        // TODO: test validations
    }

    /**
     * Fetch network usage for all stream targets
     *
     * This operation shows the amount of network usage for all stream targets in the account cumulatively and individually. The default time frame is &lt;em&gt;from&lt;/em&gt; the last billing date &lt;em&gt;to&lt;/em&gt; the end of the current day.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void usageNetworkStreamTargetsIndexTest() throws ApiException {
        OffsetDateTime from = null;
        OffsetDateTime to = null;
        UsageNetworkStreamTargets response = api.usageNetworkStreamTargetsIndex(from, to);
        // TODO: test validations
    }

    /**
     * Fetch network usage for all transcoders
     *
     * This operation shows the amount of network usage (egress) for all transcoders in the account. The default time frame is &lt;em&gt;from&lt;/em&gt; the last billing date &lt;em&gt;to&lt;/em&gt; the end of the current day.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void usageNetworkTranscodersIndexTest() throws ApiException {
        OffsetDateTime from = null;
        OffsetDateTime to = null;
        String transcoderType = null;
        String billingMode = null;
        UsageNetworkTranscoders response = api.usageNetworkTranscodersIndex(from, to, transcoderType, billingMode);
        // TODO: test validations
    }

}
