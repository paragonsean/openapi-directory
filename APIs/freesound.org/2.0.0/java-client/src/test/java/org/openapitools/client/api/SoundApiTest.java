/*
 * Freesound
 * With the Freesound APIv2 you can browse, search, and retrieve information about Freesound users, packs, and the sounds themselves of course. You can find similar sounds to a given target (based on content analysis) and retrieve automatically extracted features from audio files, as well as perform advanced queries combining content analysis features and other metadata (tags, etc...). With the Freesound APIv2, you can also upload, comment, rate and bookmark sounds!
 *
 * The version of the OpenAPI document: 2.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.Sound;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for SoundApi
 */
@Disabled
public class SoundApiTest {

    private final SoundApi api = new SoundApi();

    /**
     * Details of a sound
     *
     * This resource allows the retrieval of detailed information about a sound.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getSoundByIdTest() throws ApiException {
        Long soundId = null;
        Sound response = api.getSoundById(soundId);
        // TODO: test validations
    }

}
