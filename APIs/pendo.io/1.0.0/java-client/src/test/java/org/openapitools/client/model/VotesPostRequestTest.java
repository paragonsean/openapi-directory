/*
 * Pendo Feedback API
 * ## Who is this for?  This documentation is for developers creating their own integration with [Feedback's](https://www.pendo.io/product/feedback/) API. If you are doing a standard integration, there's a really easy [Javascript integration](https://help.receptive.io/hc/en-us/articles/209221969-How-to-integrate-Receptive-with-your-app) that you should know about before you go to the effort of building your own integration.  ## Authentication  API calls generally need to be authenticated. Generate an API Key at https://feedback.pendo.io/app/#/vendor/settings?section=integrate. This key should then be added to every request as a request header named 'auth-token' (preferred), or as a query parameter named 'auth-token'.  ## Endpoint  API endpoint is https://api.feedback.eu.pendo.io / https://api.feedback.us.pendo.io depending where your datacenter is located.  ## Notes  API endpoints are being added to this documentation as needed by customers. If you don't see an endpoint you need please contact support and if it exists we'll publish the docs here. The 'try it out' feature on this documentation page will probably be blocked by your browser because the Access-Control-Allow-Origin header has its value set by the Feedback server depending on your hostname.  ## Generating client code  This documentation is automatically generated from an OpenAPI spec available [here](http://apidoc.receptive.io/receptive.swagger.json). You can use Swagger to auto-generate API client code in many languages using the [Swagger Editor](http://editor.swagger.io/#/)
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@receptive.io
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.FeatureVote;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for VotesPostRequest
 */
public class VotesPostRequestTest {
    private final VotesPostRequest model = new VotesPostRequest();

    /**
     * Model tests for VotesPostRequest
     */
    @Test
    public void testVotesPostRequest() {
        // TODO: test VotesPostRequest
    }

    /**
     * Test the property 'userId'
     */
    @Test
    public void userIdTest() {
        // TODO: test userId
    }

    /**
     * Test the property 'votes'
     */
    @Test
    public void votesTest() {
        // TODO: test votes
    }

}
