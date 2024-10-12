/*
 * City Context
 * City Context provides a straightforward API to access UK Open Data: crime statistics, schools, demographics and more.
 *
 * The version of the OpenAPI document: 1.0.0
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


import org.openapitools.client.model.PointInfo;
import org.openapitools.client.model.Usage;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CitycontextApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public CitycontextApi() {
        this(Configuration.getDefaultApiClient());
    }

    public CitycontextApi(ApiClient apiClient) {
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
     * Build call for byPoint
     * @param lat Latitude (required)
     * @param lon Longitude (required)
     * @param schoolSearchRadius Search radius for schools, in metres, between 100 and 4000 (optional)
     * @param parkSearchRadius Search radius for parks, in metres, between 100 and 2000 (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call byPointCall(Float lat, Float lon, Integer schoolSearchRadius, Integer parkSearchRadius, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/@{lat},{lon}"
            .replace("{" + "lat" + "}", localVarApiClient.escapeString(lat.toString()))
            .replace("{" + "lon" + "}", localVarApiClient.escapeString(lon.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (schoolSearchRadius != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("school_search_radius", schoolSearchRadius));
        }

        if (parkSearchRadius != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("park_search_radius", parkSearchRadius));
        }

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

        String[] localVarAuthNames = new String[] { "user_key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call byPointValidateBeforeCall(Float lat, Float lon, Integer schoolSearchRadius, Integer parkSearchRadius, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'lat' is set
        if (lat == null) {
            throw new ApiException("Missing the required parameter 'lat' when calling byPoint(Async)");
        }

        // verify the required parameter 'lon' is set
        if (lon == null) {
            throw new ApiException("Missing the required parameter 'lon' when calling byPoint(Async)");
        }

        return byPointCall(lat, lon, schoolSearchRadius, parkSearchRadius, _callback);

    }

    /**
     * Query by coordinates (SRID 4326 - decimal degrees)
     * 
     * @param lat Latitude (required)
     * @param lon Longitude (required)
     * @param schoolSearchRadius Search radius for schools, in metres, between 100 and 4000 (optional)
     * @param parkSearchRadius Search radius for parks, in metres, between 100 and 2000 (optional)
     * @return PointInfo
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public PointInfo byPoint(Float lat, Float lon, Integer schoolSearchRadius, Integer parkSearchRadius) throws ApiException {
        ApiResponse<PointInfo> localVarResp = byPointWithHttpInfo(lat, lon, schoolSearchRadius, parkSearchRadius);
        return localVarResp.getData();
    }

    /**
     * Query by coordinates (SRID 4326 - decimal degrees)
     * 
     * @param lat Latitude (required)
     * @param lon Longitude (required)
     * @param schoolSearchRadius Search radius for schools, in metres, between 100 and 4000 (optional)
     * @param parkSearchRadius Search radius for parks, in metres, between 100 and 2000 (optional)
     * @return ApiResponse&lt;PointInfo&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PointInfo> byPointWithHttpInfo(Float lat, Float lon, Integer schoolSearchRadius, Integer parkSearchRadius) throws ApiException {
        okhttp3.Call localVarCall = byPointValidateBeforeCall(lat, lon, schoolSearchRadius, parkSearchRadius, null);
        Type localVarReturnType = new TypeToken<PointInfo>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Query by coordinates (SRID 4326 - decimal degrees) (asynchronously)
     * 
     * @param lat Latitude (required)
     * @param lon Longitude (required)
     * @param schoolSearchRadius Search radius for schools, in metres, between 100 and 4000 (optional)
     * @param parkSearchRadius Search radius for parks, in metres, between 100 and 2000 (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call byPointAsync(Float lat, Float lon, Integer schoolSearchRadius, Integer parkSearchRadius, final ApiCallback<PointInfo> _callback) throws ApiException {

        okhttp3.Call localVarCall = byPointValidateBeforeCall(lat, lon, schoolSearchRadius, parkSearchRadius, _callback);
        Type localVarReturnType = new TypeToken<PointInfo>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for byPostcode
     * @param postcode Postcode (required)
     * @param schoolSearchRadius Search radius for schools, in metres, between 100 and 4000 (optional)
     * @param parkSearchRadius Search radius for parks, in metres, between 100 and 2000 (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call byPostcodeCall(String postcode, Integer schoolSearchRadius, Integer parkSearchRadius, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/postcodes/{postcode}"
            .replace("{" + "postcode" + "}", localVarApiClient.escapeString(postcode.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (schoolSearchRadius != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("school_search_radius", schoolSearchRadius));
        }

        if (parkSearchRadius != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("park_search_radius", parkSearchRadius));
        }

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

        String[] localVarAuthNames = new String[] { "user_key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call byPostcodeValidateBeforeCall(String postcode, Integer schoolSearchRadius, Integer parkSearchRadius, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'postcode' is set
        if (postcode == null) {
            throw new ApiException("Missing the required parameter 'postcode' when calling byPostcode(Async)");
        }

        return byPostcodeCall(postcode, schoolSearchRadius, parkSearchRadius, _callback);

    }

    /**
     * Query by postcode
     * 
     * @param postcode Postcode (required)
     * @param schoolSearchRadius Search radius for schools, in metres, between 100 and 4000 (optional)
     * @param parkSearchRadius Search radius for parks, in metres, between 100 and 2000 (optional)
     * @return PointInfo
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public PointInfo byPostcode(String postcode, Integer schoolSearchRadius, Integer parkSearchRadius) throws ApiException {
        ApiResponse<PointInfo> localVarResp = byPostcodeWithHttpInfo(postcode, schoolSearchRadius, parkSearchRadius);
        return localVarResp.getData();
    }

    /**
     * Query by postcode
     * 
     * @param postcode Postcode (required)
     * @param schoolSearchRadius Search radius for schools, in metres, between 100 and 4000 (optional)
     * @param parkSearchRadius Search radius for parks, in metres, between 100 and 2000 (optional)
     * @return ApiResponse&lt;PointInfo&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PointInfo> byPostcodeWithHttpInfo(String postcode, Integer schoolSearchRadius, Integer parkSearchRadius) throws ApiException {
        okhttp3.Call localVarCall = byPostcodeValidateBeforeCall(postcode, schoolSearchRadius, parkSearchRadius, null);
        Type localVarReturnType = new TypeToken<PointInfo>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Query by postcode (asynchronously)
     * 
     * @param postcode Postcode (required)
     * @param schoolSearchRadius Search radius for schools, in metres, between 100 and 4000 (optional)
     * @param parkSearchRadius Search radius for parks, in metres, between 100 and 2000 (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call byPostcodeAsync(String postcode, Integer schoolSearchRadius, Integer parkSearchRadius, final ApiCallback<PointInfo> _callback) throws ApiException {

        okhttp3.Call localVarCall = byPostcodeValidateBeforeCall(postcode, schoolSearchRadius, parkSearchRadius, _callback);
        Type localVarReturnType = new TypeToken<PointInfo>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for usage
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usageCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/usage";

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

        String[] localVarAuthNames = new String[] { "user_key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call usageValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return usageCall(_callback);

    }

    /**
     * Get usage in current month
     * 
     * @return Usage
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public Usage usage() throws ApiException {
        ApiResponse<Usage> localVarResp = usageWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Get usage in current month
     * 
     * @return ApiResponse&lt;Usage&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Usage> usageWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = usageValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<Usage>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get usage in current month (asynchronously)
     * 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usageAsync(final ApiCallback<Usage> _callback) throws ApiException {

        okhttp3.Call localVarCall = usageValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<Usage>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
