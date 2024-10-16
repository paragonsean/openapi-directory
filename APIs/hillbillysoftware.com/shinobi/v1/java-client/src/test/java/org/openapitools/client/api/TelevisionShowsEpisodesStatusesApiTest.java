/*
 * shinobiapi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.Episode;
import org.openapitools.client.model.LastAvailableSeason;
import org.openapitools.client.model.PostResult;
import org.openapitools.client.model.ShowStatus;
import org.openapitools.client.model.TVInformation;
import org.openapitools.client.model.TVInformationPost;
import org.openapitools.client.model.TVShowSeasons;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for TelevisionShowsEpisodesStatusesApi
 */
@Disabled
public class TelevisionShowsEpisodesStatusesApiTest {

    private final TelevisionShowsEpisodesStatusesApi api = new TelevisionShowsEpisodesStatusesApi();

    /**
     * Add new show to database
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addTVShowPostTest() throws ApiException {
        TVInformationPost value = null;
        PostResult response = api.addTVShowPost(value);
        // TODO: test validations
    }

    /**
     * Gets all episodes for selected ID
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void episodesByIDGetTest() throws ApiException {
        String accessToken = null;
        String ID = null;
        List<Episode> response = api.episodesByIDGet(accessToken, ID);
        // TODO: test validations
    }

    /**
     * Gets list of episodes for specified imdbID and Season number
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void episodesBySeasonGetTest() throws ApiException {
        String accessToken = null;
        String ID = null;
        String season = null;
        List<Episode> response = api.episodesBySeasonGet(accessToken, ID, season);
        // TODO: test validations
    }

    /**
     * Gets all episodes for selected show
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void episodesGetTest() throws ApiException {
        String accessToken = null;
        String showname = null;
        List<Episode> response = api.episodesGet(accessToken, showname);
        // TODO: test validations
    }

    /**
     * Returns last available season number in database, based on passed imdbID
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void episodesLastAvailableSeasonGetTest() throws ApiException {
        String accessToken = null;
        String ID = null;
        LastAvailableSeason response = api.episodesLastAvailableSeasonGet(accessToken, ID);
        // TODO: test validations
    }

    /**
     * Gets latest season number based on show name
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void episodesLastAvailableSeasonbyNameGetTest() throws ApiException {
        String accessToken = null;
        String name = null;
        LastAvailableSeason response = api.episodesLastAvailableSeasonbyNameGet(accessToken, name);
        // TODO: test validations
    }

    /**
     * Returns number of available seasons and episodes
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void episodesSeasonCountGetTest() throws ApiException {
        String accessToken = null;
        String ID = null;
        TVShowSeasons response = api.episodesSeasonCountGet(accessToken, ID);
        // TODO: test validations
    }

    /**
     * Returns status of queried show (query can be IMDB, TVDB, or showname)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void showStatusGetTest() throws ApiException {
        String accessToken = null;
        String query = null;
        List<ShowStatus> response = api.showStatusGet(accessToken, query);
        // TODO: test validations
    }

    /**
     * Returns results based on query, result set limited to 5 records
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void tVShowByNameGetTest() throws ApiException {
        String accessToken = null;
        String query = null;
        List<TVInformation> response = api.tVShowByNameGet(accessToken, query);
        // TODO: test validations
    }

    /**
     * Returns TVShow information based on IMDBid
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void tVShowIDGetTest() throws ApiException {
        String accesstoken = null;
        String id = null;
        String imdbID = null;
        TVInformation response = api.tVShowIDGet(accesstoken, id, imdbID);
        // TODO: test validations
    }

}
