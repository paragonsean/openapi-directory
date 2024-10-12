/*
 * NBA v3 Play-by-Play
 * NBA play-by-play API.
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.PlayByPlay;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DefaultApi
 */
@Disabled
public class DefaultApiTest {

    private final DefaultApi api = new DefaultApi();

    /**
     * Play By Play
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void playByPlayTest() throws ApiException {
        String format = null;
        String gameid = null;
        PlayByPlay response = api.playByPlay(format, gameid);
        // TODO: test validations
    }

    /**
     * Play By Play Delta
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void playByPlayDeltaTest() throws ApiException {
        String format = null;
        String date = null;
        String minutes = null;
        List<PlayByPlay> response = api.playByPlayDelta(format, date, minutes);
        // TODO: test validations
    }

}
