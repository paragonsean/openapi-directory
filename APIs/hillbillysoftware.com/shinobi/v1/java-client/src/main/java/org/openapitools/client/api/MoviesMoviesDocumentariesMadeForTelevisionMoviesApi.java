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


import org.openapitools.client.model.MovieInformation;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MoviesMoviesDocumentariesMadeForTelevisionMoviesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public MoviesMoviesDocumentariesMadeForTelevisionMoviesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public MoviesMoviesDocumentariesMadeForTelevisionMoviesApi(ApiClient apiClient) {
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
     * Build call for movieIDGet
     * @param accesstoken  (required)
     * @param imdbID  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Movie information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call movieIDGetCall(String accesstoken, String imdbID, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/Movie/ByID/{accesstoken}/{imdbID}"
            .replace("{" + "accesstoken" + "}", localVarApiClient.escapeString(accesstoken.toString()))
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
    private okhttp3.Call movieIDGetValidateBeforeCall(String accesstoken, String imdbID, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'accesstoken' is set
        if (accesstoken == null) {
            throw new ApiException("Missing the required parameter 'accesstoken' when calling movieIDGet(Async)");
        }

        // verify the required parameter 'imdbID' is set
        if (imdbID == null) {
            throw new ApiException("Missing the required parameter 'imdbID' when calling movieIDGet(Async)");
        }

        return movieIDGetCall(accesstoken, imdbID, _callback);

    }

    /**
     * 
     * 
     * @param accesstoken  (required)
     * @param imdbID  (required)
     * @return MovieInformation
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Movie information </td><td>  -  </td></tr>
     </table>
     */
    public MovieInformation movieIDGet(String accesstoken, String imdbID) throws ApiException {
        ApiResponse<MovieInformation> localVarResp = movieIDGetWithHttpInfo(accesstoken, imdbID);
        return localVarResp.getData();
    }

    /**
     * 
     * 
     * @param accesstoken  (required)
     * @param imdbID  (required)
     * @return ApiResponse&lt;MovieInformation&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Movie information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<MovieInformation> movieIDGetWithHttpInfo(String accesstoken, String imdbID) throws ApiException {
        okhttp3.Call localVarCall = movieIDGetValidateBeforeCall(accesstoken, imdbID, null);
        Type localVarReturnType = new TypeToken<MovieInformation>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * 
     * @param accesstoken  (required)
     * @param imdbID  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Movie information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call movieIDGetAsync(String accesstoken, String imdbID, final ApiCallback<MovieInformation> _callback) throws ApiException {

        okhttp3.Call localVarCall = movieIDGetValidateBeforeCall(accesstoken, imdbID, _callback);
        Type localVarReturnType = new TypeToken<MovieInformation>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for movieSearchGetAsync
     * @param accessToken  (required)
     * @param query  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List of information about queried movie(s) </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call movieSearchGetAsyncCall(String accessToken, String query, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/Movie/Search/{AccessToken}/{Query}"
            .replace("{" + "AccessToken" + "}", localVarApiClient.escapeString(accessToken.toString()))
            .replace("{" + "Query" + "}", localVarApiClient.escapeString(query.toString()));

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
    private okhttp3.Call movieSearchGetAsyncValidateBeforeCall(String accessToken, String query, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'accessToken' is set
        if (accessToken == null) {
            throw new ApiException("Missing the required parameter 'accessToken' when calling movieSearchGetAsync(Async)");
        }

        // verify the required parameter 'query' is set
        if (query == null) {
            throw new ApiException("Missing the required parameter 'query' when calling movieSearchGetAsync(Async)");
        }

        return movieSearchGetAsyncCall(accessToken, query, _callback);

    }

    /**
     * Searches for movies, result set limited to 5 records
     * 
     * @param accessToken  (required)
     * @param query  (required)
     * @return List&lt;MovieInformation&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List of information about queried movie(s) </td><td>  -  </td></tr>
     </table>
     */
    public List<MovieInformation> movieSearchGetAsync(String accessToken, String query) throws ApiException {
        ApiResponse<List<MovieInformation>> localVarResp = movieSearchGetAsyncWithHttpInfo(accessToken, query);
        return localVarResp.getData();
    }

    /**
     * Searches for movies, result set limited to 5 records
     * 
     * @param accessToken  (required)
     * @param query  (required)
     * @return ApiResponse&lt;List&lt;MovieInformation&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List of information about queried movie(s) </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<MovieInformation>> movieSearchGetAsyncWithHttpInfo(String accessToken, String query) throws ApiException {
        okhttp3.Call localVarCall = movieSearchGetAsyncValidateBeforeCall(accessToken, query, null);
        Type localVarReturnType = new TypeToken<List<MovieInformation>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Searches for movies, result set limited to 5 records (asynchronously)
     * 
     * @param accessToken  (required)
     * @param query  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List of information about queried movie(s) </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call movieSearchGetAsyncAsync(String accessToken, String query, final ApiCallback<List<MovieInformation>> _callback) throws ApiException {

        okhttp3.Call localVarCall = movieSearchGetAsyncValidateBeforeCall(accessToken, query, _callback);
        Type localVarReturnType = new TypeToken<List<MovieInformation>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
