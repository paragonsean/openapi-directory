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


import org.openapitools.client.model.Trailer;
import org.openapitools.client.model.TrailerCount;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TrailersMovieTelevisionShowTrailersApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public TrailersMovieTelevisionShowTrailersApi() {
        this(Configuration.getDefaultApiClient());
    }

    public TrailersMovieTelevisionShowTrailersApi(ApiClient apiClient) {
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
     * Build call for trailerCountByIDGet
     * @param accessToken  (required)
     * @param imdbID  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Count of trailers available for imdbID </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call trailerCountByIDGetCall(String accessToken, String imdbID, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/Trailers/CountByID/{AccessToken}/{imdbID}"
            .replace("{" + "AccessToken" + "}", localVarApiClient.escapeString(accessToken.toString()))
            .replace("{" + "imdbID" + "}", localVarApiClient.escapeString(imdbID.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json",
            "text/json",
            "application/xml",
            "text/xml"
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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call trailerCountByIDGetValidateBeforeCall(String accessToken, String imdbID, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'accessToken' is set
        if (accessToken == null) {
            throw new ApiException("Missing the required parameter 'accessToken' when calling trailerCountByIDGet(Async)");
        }

        // verify the required parameter 'imdbID' is set
        if (imdbID == null) {
            throw new ApiException("Missing the required parameter 'imdbID' when calling trailerCountByIDGet(Async)");
        }

        return trailerCountByIDGetCall(accessToken, imdbID, _callback);

    }

    /**
     * Get trailer count for passed ID
     * 
     * @param accessToken  (required)
     * @param imdbID  (required)
     * @return TrailerCount
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Count of trailers available for imdbID </td><td>  -  </td></tr>
     </table>
     */
    public TrailerCount trailerCountByIDGet(String accessToken, String imdbID) throws ApiException {
        ApiResponse<TrailerCount> localVarResp = trailerCountByIDGetWithHttpInfo(accessToken, imdbID);
        return localVarResp.getData();
    }

    /**
     * Get trailer count for passed ID
     * 
     * @param accessToken  (required)
     * @param imdbID  (required)
     * @return ApiResponse&lt;TrailerCount&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Count of trailers available for imdbID </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<TrailerCount> trailerCountByIDGetWithHttpInfo(String accessToken, String imdbID) throws ApiException {
        okhttp3.Call localVarCall = trailerCountByIDGetValidateBeforeCall(accessToken, imdbID, null);
        Type localVarReturnType = new TypeToken<TrailerCount>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get trailer count for passed ID (asynchronously)
     * 
     * @param accessToken  (required)
     * @param imdbID  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Count of trailers available for imdbID </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call trailerCountByIDGetAsync(String accessToken, String imdbID, final ApiCallback<TrailerCount> _callback) throws ApiException {

        okhttp3.Call localVarCall = trailerCountByIDGetValidateBeforeCall(accessToken, imdbID, _callback);
        Type localVarReturnType = new TypeToken<TrailerCount>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for trailerCountByNameGet
     * @param accessToken  (required)
     * @param name  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Count of trailers available for passed name </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call trailerCountByNameGetCall(String accessToken, String name, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/Trailers/CountByName/{AccessToken}/{Name}"
            .replace("{" + "AccessToken" + "}", localVarApiClient.escapeString(accessToken.toString()))
            .replace("{" + "Name" + "}", localVarApiClient.escapeString(name.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json",
            "text/json",
            "application/xml",
            "text/xml"
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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call trailerCountByNameGetValidateBeforeCall(String accessToken, String name, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'accessToken' is set
        if (accessToken == null) {
            throw new ApiException("Missing the required parameter 'accessToken' when calling trailerCountByNameGet(Async)");
        }

        // verify the required parameter 'name' is set
        if (name == null) {
            throw new ApiException("Missing the required parameter 'name' when calling trailerCountByNameGet(Async)");
        }

        return trailerCountByNameGetCall(accessToken, name, _callback);

    }

    /**
     * Get trailer count for passed name (Movie title or TVShow name)
     * 
     * @param accessToken  (required)
     * @param name  (required)
     * @return TrailerCount
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Count of trailers available for passed name </td><td>  -  </td></tr>
     </table>
     */
    public TrailerCount trailerCountByNameGet(String accessToken, String name) throws ApiException {
        ApiResponse<TrailerCount> localVarResp = trailerCountByNameGetWithHttpInfo(accessToken, name);
        return localVarResp.getData();
    }

    /**
     * Get trailer count for passed name (Movie title or TVShow name)
     * 
     * @param accessToken  (required)
     * @param name  (required)
     * @return ApiResponse&lt;TrailerCount&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Count of trailers available for passed name </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<TrailerCount> trailerCountByNameGetWithHttpInfo(String accessToken, String name) throws ApiException {
        okhttp3.Call localVarCall = trailerCountByNameGetValidateBeforeCall(accessToken, name, null);
        Type localVarReturnType = new TypeToken<TrailerCount>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get trailer count for passed name (Movie title or TVShow name) (asynchronously)
     * 
     * @param accessToken  (required)
     * @param name  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Count of trailers available for passed name </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call trailerCountByNameGetAsync(String accessToken, String name, final ApiCallback<TrailerCount> _callback) throws ApiException {

        okhttp3.Call localVarCall = trailerCountByNameGetValidateBeforeCall(accessToken, name, _callback);
        Type localVarReturnType = new TypeToken<TrailerCount>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for trailerSearchGet
     * @param accessToken  (required)
     * @param phrase Trailer you like to search for (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List of trailers </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call trailerSearchGetCall(String accessToken, String phrase, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/Trailers/Search/{AccessToken}/{Phrase}"
            .replace("{" + "AccessToken" + "}", localVarApiClient.escapeString(accessToken.toString()))
            .replace("{" + "Phrase" + "}", localVarApiClient.escapeString(phrase.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json",
            "text/json",
            "application/xml",
            "text/xml"
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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call trailerSearchGetValidateBeforeCall(String accessToken, String phrase, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'accessToken' is set
        if (accessToken == null) {
            throw new ApiException("Missing the required parameter 'accessToken' when calling trailerSearchGet(Async)");
        }

        // verify the required parameter 'phrase' is set
        if (phrase == null) {
            throw new ApiException("Missing the required parameter 'phrase' when calling trailerSearchGet(Async)");
        }

        return trailerSearchGetCall(accessToken, phrase, _callback);

    }

    /**
     * Gets trailers by search phrase (limited to 10 records)
     * 
     * @param accessToken  (required)
     * @param phrase Trailer you like to search for (required)
     * @return List&lt;Trailer&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List of trailers </td><td>  -  </td></tr>
     </table>
     */
    public List<Trailer> trailerSearchGet(String accessToken, String phrase) throws ApiException {
        ApiResponse<List<Trailer>> localVarResp = trailerSearchGetWithHttpInfo(accessToken, phrase);
        return localVarResp.getData();
    }

    /**
     * Gets trailers by search phrase (limited to 10 records)
     * 
     * @param accessToken  (required)
     * @param phrase Trailer you like to search for (required)
     * @return ApiResponse&lt;List&lt;Trailer&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List of trailers </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<Trailer>> trailerSearchGetWithHttpInfo(String accessToken, String phrase) throws ApiException {
        okhttp3.Call localVarCall = trailerSearchGetValidateBeforeCall(accessToken, phrase, null);
        Type localVarReturnType = new TypeToken<List<Trailer>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Gets trailers by search phrase (limited to 10 records) (asynchronously)
     * 
     * @param accessToken  (required)
     * @param phrase Trailer you like to search for (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List of trailers </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call trailerSearchGetAsync(String accessToken, String phrase, final ApiCallback<List<Trailer>> _callback) throws ApiException {

        okhttp3.Call localVarCall = trailerSearchGetValidateBeforeCall(accessToken, phrase, _callback);
        Type localVarReturnType = new TypeToken<List<Trailer>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for trailersbyIDGet
     * @param accessToken  (required)
     * @param imdbID  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List of trailers </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call trailersbyIDGetCall(String accessToken, String imdbID, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/Trailers/ByID/{AccessToken}/{imdbID}"
            .replace("{" + "AccessToken" + "}", localVarApiClient.escapeString(accessToken.toString()))
            .replace("{" + "imdbID" + "}", localVarApiClient.escapeString(imdbID.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json",
            "text/json",
            "application/xml",
            "text/xml"
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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call trailersbyIDGetValidateBeforeCall(String accessToken, String imdbID, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'accessToken' is set
        if (accessToken == null) {
            throw new ApiException("Missing the required parameter 'accessToken' when calling trailersbyIDGet(Async)");
        }

        // verify the required parameter 'imdbID' is set
        if (imdbID == null) {
            throw new ApiException("Missing the required parameter 'imdbID' when calling trailersbyIDGet(Async)");
        }

        return trailersbyIDGetCall(accessToken, imdbID, _callback);

    }

    /**
     * Get Trailers for passed imdbID
     * 
     * @param accessToken  (required)
     * @param imdbID  (required)
     * @return List&lt;Trailer&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List of trailers </td><td>  -  </td></tr>
     </table>
     */
    public List<Trailer> trailersbyIDGet(String accessToken, String imdbID) throws ApiException {
        ApiResponse<List<Trailer>> localVarResp = trailersbyIDGetWithHttpInfo(accessToken, imdbID);
        return localVarResp.getData();
    }

    /**
     * Get Trailers for passed imdbID
     * 
     * @param accessToken  (required)
     * @param imdbID  (required)
     * @return ApiResponse&lt;List&lt;Trailer&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List of trailers </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<Trailer>> trailersbyIDGetWithHttpInfo(String accessToken, String imdbID) throws ApiException {
        okhttp3.Call localVarCall = trailersbyIDGetValidateBeforeCall(accessToken, imdbID, null);
        Type localVarReturnType = new TypeToken<List<Trailer>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Trailers for passed imdbID (asynchronously)
     * 
     * @param accessToken  (required)
     * @param imdbID  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List of trailers </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call trailersbyIDGetAsync(String accessToken, String imdbID, final ApiCallback<List<Trailer>> _callback) throws ApiException {

        okhttp3.Call localVarCall = trailersbyIDGetValidateBeforeCall(accessToken, imdbID, _callback);
        Type localVarReturnType = new TypeToken<List<Trailer>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
