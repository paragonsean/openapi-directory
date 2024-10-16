/*
 * NFL v3 Play-by-Play
 * NFL play-by-play API.
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiCallback;
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.Pair;
import org.openapitools.client.ProgressRequestBody;
import org.openapitools.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


import org.openapitools.client.model.PlayByPlay;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DefaultApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public DefaultApi() {
        this(Configuration.getDefaultApiClient());
    }

    public DefaultApi(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return localVarApiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public int getHostIndex() {
        return localHostIndex;
    }

    public void setHostIndex(int hostIndex) {
        this.localHostIndex = hostIndex;
    }

    public String getCustomBaseUrl() {
        return localCustomBaseUrl;
    }

    public void setCustomBaseUrl(String customBaseUrl) {
        this.localCustomBaseUrl = customBaseUrl;
    }

    /**
     * Build call for playByPlay
     * @param format Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. (required)
     * @param season Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          (required)
     * @param week Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          (required)
     * @param hometeam Abbreviation of the home team. Example: &lt;code&gt;WAS&lt;/code&gt;. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call playByPlayCall(String format, String season, String week, String hometeam, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/{format}/PlayByPlay/{season}/{week}/{hometeam}"
            .replace("{" + "format" + "}", localVarApiClient.escapeString(format.toString()))
            .replace("{" + "season" + "}", localVarApiClient.escapeString(season.toString()))
            .replace("{" + "week" + "}", localVarApiClient.escapeString(week.toString()))
            .replace("{" + "hometeam" + "}", localVarApiClient.escapeString(hometeam.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "apiKeyQuery", "apiKeyHeader" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call playByPlayValidateBeforeCall(String format, String season, String week, String hometeam, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'format' is set
        if (format == null) {
            throw new ApiException("Missing the required parameter 'format' when calling playByPlay(Async)");
        }

        // verify the required parameter 'season' is set
        if (season == null) {
            throw new ApiException("Missing the required parameter 'season' when calling playByPlay(Async)");
        }

        // verify the required parameter 'week' is set
        if (week == null) {
            throw new ApiException("Missing the required parameter 'week' when calling playByPlay(Async)");
        }

        // verify the required parameter 'hometeam' is set
        if (hometeam == null) {
            throw new ApiException("Missing the required parameter 'hometeam' when calling playByPlay(Async)");
        }

        return playByPlayCall(format, season, week, hometeam, _callback);

    }

    /**
     * Play By Play
     * 
     * @param format Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. (required)
     * @param season Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          (required)
     * @param week Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          (required)
     * @param hometeam Abbreviation of the home team. Example: &lt;code&gt;WAS&lt;/code&gt;. (required)
     * @return PlayByPlay
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public PlayByPlay playByPlay(String format, String season, String week, String hometeam) throws ApiException {
        ApiResponse<PlayByPlay> localVarResp = playByPlayWithHttpInfo(format, season, week, hometeam);
        return localVarResp.getData();
    }

    /**
     * Play By Play
     * 
     * @param format Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. (required)
     * @param season Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          (required)
     * @param week Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          (required)
     * @param hometeam Abbreviation of the home team. Example: &lt;code&gt;WAS&lt;/code&gt;. (required)
     * @return ApiResponse&lt;PlayByPlay&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PlayByPlay> playByPlayWithHttpInfo(String format, String season, String week, String hometeam) throws ApiException {
        okhttp3.Call localVarCall = playByPlayValidateBeforeCall(format, season, week, hometeam, null);
        Type localVarReturnType = new TypeToken<PlayByPlay>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Play By Play (asynchronously)
     * 
     * @param format Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. (required)
     * @param season Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          (required)
     * @param week Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          (required)
     * @param hometeam Abbreviation of the home team. Example: &lt;code&gt;WAS&lt;/code&gt;. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call playByPlayAsync(String format, String season, String week, String hometeam, final ApiCallback<PlayByPlay> _callback) throws ApiException {

        okhttp3.Call localVarCall = playByPlayValidateBeforeCall(format, season, week, hometeam, _callback);
        Type localVarReturnType = new TypeToken<PlayByPlay>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for playByPlayDelta
     * @param format Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. (required)
     * @param season Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          (required)
     * @param week Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          (required)
     * @param minutes Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:&lt;br&gt;           &lt;code&gt;1&lt;/code&gt; or &lt;code&gt;2&lt;/code&gt;.          (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call playByPlayDeltaCall(String format, String season, String week, String minutes, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/{format}/PlayByPlayDelta/{season}/{week}/{minutes}"
            .replace("{" + "format" + "}", localVarApiClient.escapeString(format.toString()))
            .replace("{" + "season" + "}", localVarApiClient.escapeString(season.toString()))
            .replace("{" + "week" + "}", localVarApiClient.escapeString(week.toString()))
            .replace("{" + "minutes" + "}", localVarApiClient.escapeString(minutes.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "apiKeyQuery", "apiKeyHeader" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call playByPlayDeltaValidateBeforeCall(String format, String season, String week, String minutes, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'format' is set
        if (format == null) {
            throw new ApiException("Missing the required parameter 'format' when calling playByPlayDelta(Async)");
        }

        // verify the required parameter 'season' is set
        if (season == null) {
            throw new ApiException("Missing the required parameter 'season' when calling playByPlayDelta(Async)");
        }

        // verify the required parameter 'week' is set
        if (week == null) {
            throw new ApiException("Missing the required parameter 'week' when calling playByPlayDelta(Async)");
        }

        // verify the required parameter 'minutes' is set
        if (minutes == null) {
            throw new ApiException("Missing the required parameter 'minutes' when calling playByPlayDelta(Async)");
        }

        return playByPlayDeltaCall(format, season, week, minutes, _callback);

    }

    /**
     * Play By Play Delta
     * 
     * @param format Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. (required)
     * @param season Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          (required)
     * @param week Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          (required)
     * @param minutes Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:&lt;br&gt;           &lt;code&gt;1&lt;/code&gt; or &lt;code&gt;2&lt;/code&gt;.          (required)
     * @return List&lt;PlayByPlay&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public List<PlayByPlay> playByPlayDelta(String format, String season, String week, String minutes) throws ApiException {
        ApiResponse<List<PlayByPlay>> localVarResp = playByPlayDeltaWithHttpInfo(format, season, week, minutes);
        return localVarResp.getData();
    }

    /**
     * Play By Play Delta
     * 
     * @param format Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. (required)
     * @param season Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          (required)
     * @param week Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          (required)
     * @param minutes Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:&lt;br&gt;           &lt;code&gt;1&lt;/code&gt; or &lt;code&gt;2&lt;/code&gt;.          (required)
     * @return ApiResponse&lt;List&lt;PlayByPlay&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<PlayByPlay>> playByPlayDeltaWithHttpInfo(String format, String season, String week, String minutes) throws ApiException {
        okhttp3.Call localVarCall = playByPlayDeltaValidateBeforeCall(format, season, week, minutes, null);
        Type localVarReturnType = new TypeToken<List<PlayByPlay>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Play By Play Delta (asynchronously)
     * 
     * @param format Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. (required)
     * @param season Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          (required)
     * @param week Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          (required)
     * @param minutes Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:&lt;br&gt;           &lt;code&gt;1&lt;/code&gt; or &lt;code&gt;2&lt;/code&gt;.          (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call playByPlayDeltaAsync(String format, String season, String week, String minutes, final ApiCallback<List<PlayByPlay>> _callback) throws ApiException {

        okhttp3.Call localVarCall = playByPlayDeltaValidateBeforeCall(format, season, week, minutes, _callback);
        Type localVarReturnType = new TypeToken<List<PlayByPlay>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for playByPlaySimulation
     * @param format Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. (required)
     * @param numberofplays The number of plays to progress in this NFL live game simulation. Example entries are &lt;code&gt;0&lt;/code&gt;, &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, &lt;code&gt;150&lt;/code&gt;, &lt;code&gt;200&lt;/code&gt;, etc. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call playByPlaySimulationCall(String format, String numberofplays, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/{format}/SimulatedPlayByPlay/{numberofplays}"
            .replace("{" + "format" + "}", localVarApiClient.escapeString(format.toString()))
            .replace("{" + "numberofplays" + "}", localVarApiClient.escapeString(numberofplays.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "apiKeyQuery", "apiKeyHeader" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call playByPlaySimulationValidateBeforeCall(String format, String numberofplays, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'format' is set
        if (format == null) {
            throw new ApiException("Missing the required parameter 'format' when calling playByPlaySimulation(Async)");
        }

        // verify the required parameter 'numberofplays' is set
        if (numberofplays == null) {
            throw new ApiException("Missing the required parameter 'numberofplays' when calling playByPlaySimulation(Async)");
        }

        return playByPlaySimulationCall(format, numberofplays, _callback);

    }

    /**
     * Play By Play Simulation
     * Gets simulated live play-by-play of NFL games, covering the Conference Championship games on January 21, 2018.
     * @param format Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. (required)
     * @param numberofplays The number of plays to progress in this NFL live game simulation. Example entries are &lt;code&gt;0&lt;/code&gt;, &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, &lt;code&gt;150&lt;/code&gt;, &lt;code&gt;200&lt;/code&gt;, etc. (required)
     * @return List&lt;PlayByPlay&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public List<PlayByPlay> playByPlaySimulation(String format, String numberofplays) throws ApiException {
        ApiResponse<List<PlayByPlay>> localVarResp = playByPlaySimulationWithHttpInfo(format, numberofplays);
        return localVarResp.getData();
    }

    /**
     * Play By Play Simulation
     * Gets simulated live play-by-play of NFL games, covering the Conference Championship games on January 21, 2018.
     * @param format Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. (required)
     * @param numberofplays The number of plays to progress in this NFL live game simulation. Example entries are &lt;code&gt;0&lt;/code&gt;, &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, &lt;code&gt;150&lt;/code&gt;, &lt;code&gt;200&lt;/code&gt;, etc. (required)
     * @return ApiResponse&lt;List&lt;PlayByPlay&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<PlayByPlay>> playByPlaySimulationWithHttpInfo(String format, String numberofplays) throws ApiException {
        okhttp3.Call localVarCall = playByPlaySimulationValidateBeforeCall(format, numberofplays, null);
        Type localVarReturnType = new TypeToken<List<PlayByPlay>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Play By Play Simulation (asynchronously)
     * Gets simulated live play-by-play of NFL games, covering the Conference Championship games on January 21, 2018.
     * @param format Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. (required)
     * @param numberofplays The number of plays to progress in this NFL live game simulation. Example entries are &lt;code&gt;0&lt;/code&gt;, &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, &lt;code&gt;150&lt;/code&gt;, &lt;code&gt;200&lt;/code&gt;, etc. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call playByPlaySimulationAsync(String format, String numberofplays, final ApiCallback<List<PlayByPlay>> _callback) throws ApiException {

        okhttp3.Call localVarCall = playByPlaySimulationValidateBeforeCall(format, numberofplays, _callback);
        Type localVarReturnType = new TypeToken<List<PlayByPlay>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
