/*
 * OpenUV - Global Real-Time UV Index Forecast API
 * The missing minimalistic JSON real-time UV Index API for awesome Developers, Innovators and Smart Home Enthusiasts
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


import java.math.BigDecimal;
import org.openapitools.client.model.Forecast;
import java.time.OffsetDateTime;
import org.openapitools.client.model.ProtectionResult;
import java.util.Set;
import org.openapitools.client.model.UvIndexResult;

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
     * Build call for forecastGet
     * @param lat latitude, from -90.00 to 90.00 (required)
     * @param lng longitude, from -180.00 to 180.00 (required)
     * @param xAccessToken This header is used to send data that contains your OpenUV API key (required)
     * @param alt Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value. (optional)
     * @param ozone Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default. (optional)
     * @param dt UTC datetime in ISO-8601 format, now by default. Use that parameter to get UV Index Forecast for any point in time. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call forecastGetCall(BigDecimal lat, BigDecimal lng, String xAccessToken, BigDecimal alt, BigDecimal ozone, OffsetDateTime dt, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/forecast";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (lat != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("lat", lat));
        }

        if (lng != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("lng", lng));
        }

        if (alt != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("alt", alt));
        }

        if (ozone != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("ozone", ozone));
        }

        if (dt != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("dt", dt));
        }

        if (xAccessToken != null) {
            localVarHeaderParams.put("x-access-token", localVarApiClient.parameterToString(xAccessToken));
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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call forecastGetValidateBeforeCall(BigDecimal lat, BigDecimal lng, String xAccessToken, BigDecimal alt, BigDecimal ozone, OffsetDateTime dt, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'lat' is set
        if (lat == null) {
            throw new ApiException("Missing the required parameter 'lat' when calling forecastGet(Async)");
        }

        // verify the required parameter 'lng' is set
        if (lng == null) {
            throw new ApiException("Missing the required parameter 'lng' when calling forecastGet(Async)");
        }

        // verify the required parameter 'xAccessToken' is set
        if (xAccessToken == null) {
            throw new ApiException("Missing the required parameter 'xAccessToken' when calling forecastGet(Async)");
        }

        return forecastGetCall(lat, lng, xAccessToken, alt, ozone, dt, _callback);

    }

    /**
     * 
     * Get hourly UV Index Forecast by location and date. Optional altitude, ozone level and datetime could be provided.
     * @param lat latitude, from -90.00 to 90.00 (required)
     * @param lng longitude, from -180.00 to 180.00 (required)
     * @param xAccessToken This header is used to send data that contains your OpenUV API key (required)
     * @param alt Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value. (optional)
     * @param ozone Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default. (optional)
     * @param dt UTC datetime in ISO-8601 format, now by default. Use that parameter to get UV Index Forecast for any point in time. (optional)
     * @return List&lt;Set&lt;Forecast&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public List<Set<Forecast>> forecastGet(BigDecimal lat, BigDecimal lng, String xAccessToken, BigDecimal alt, BigDecimal ozone, OffsetDateTime dt) throws ApiException {
        ApiResponse<List<Set<Forecast>>> localVarResp = forecastGetWithHttpInfo(lat, lng, xAccessToken, alt, ozone, dt);
        return localVarResp.getData();
    }

    /**
     * 
     * Get hourly UV Index Forecast by location and date. Optional altitude, ozone level and datetime could be provided.
     * @param lat latitude, from -90.00 to 90.00 (required)
     * @param lng longitude, from -180.00 to 180.00 (required)
     * @param xAccessToken This header is used to send data that contains your OpenUV API key (required)
     * @param alt Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value. (optional)
     * @param ozone Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default. (optional)
     * @param dt UTC datetime in ISO-8601 format, now by default. Use that parameter to get UV Index Forecast for any point in time. (optional)
     * @return ApiResponse&lt;List&lt;Set&lt;Forecast&gt;&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<Set<Forecast>>> forecastGetWithHttpInfo(BigDecimal lat, BigDecimal lng, String xAccessToken, BigDecimal alt, BigDecimal ozone, OffsetDateTime dt) throws ApiException {
        okhttp3.Call localVarCall = forecastGetValidateBeforeCall(lat, lng, xAccessToken, alt, ozone, dt, null);
        Type localVarReturnType = new TypeToken<List<Set<Forecast>>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Get hourly UV Index Forecast by location and date. Optional altitude, ozone level and datetime could be provided.
     * @param lat latitude, from -90.00 to 90.00 (required)
     * @param lng longitude, from -180.00 to 180.00 (required)
     * @param xAccessToken This header is used to send data that contains your OpenUV API key (required)
     * @param alt Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value. (optional)
     * @param ozone Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default. (optional)
     * @param dt UTC datetime in ISO-8601 format, now by default. Use that parameter to get UV Index Forecast for any point in time. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call forecastGetAsync(BigDecimal lat, BigDecimal lng, String xAccessToken, BigDecimal alt, BigDecimal ozone, OffsetDateTime dt, final ApiCallback<List<Set<Forecast>>> _callback) throws ApiException {

        okhttp3.Call localVarCall = forecastGetValidateBeforeCall(lat, lng, xAccessToken, alt, ozone, dt, _callback);
        Type localVarReturnType = new TypeToken<List<Set<Forecast>>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for protectionGet
     * @param lat latitude, from -90.00 to 90.00 (required)
     * @param lng longitude, from -180.00 to 180.00 (required)
     * @param from UV Index from value for protection datetime lookup. From 0 to 40. (required)
     * @param to UV Index to value for protection datetime lookup. From 0 to 40. (required)
     * @param xAccessToken This header is used to send data that contains your OpenUV API key (required)
     * @param alt Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value. (optional)
     * @param ozone Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call protectionGetCall(BigDecimal lat, BigDecimal lng, BigDecimal from, BigDecimal to, String xAccessToken, BigDecimal alt, BigDecimal ozone, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/protection";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (lat != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("lat", lat));
        }

        if (lng != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("lng", lng));
        }

        if (from != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("from", from));
        }

        if (to != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("to", to));
        }

        if (alt != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("alt", alt));
        }

        if (ozone != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("ozone", ozone));
        }

        if (xAccessToken != null) {
            localVarHeaderParams.put("x-access-token", localVarApiClient.parameterToString(xAccessToken));
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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call protectionGetValidateBeforeCall(BigDecimal lat, BigDecimal lng, BigDecimal from, BigDecimal to, String xAccessToken, BigDecimal alt, BigDecimal ozone, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'lat' is set
        if (lat == null) {
            throw new ApiException("Missing the required parameter 'lat' when calling protectionGet(Async)");
        }

        // verify the required parameter 'lng' is set
        if (lng == null) {
            throw new ApiException("Missing the required parameter 'lng' when calling protectionGet(Async)");
        }

        // verify the required parameter 'from' is set
        if (from == null) {
            throw new ApiException("Missing the required parameter 'from' when calling protectionGet(Async)");
        }

        // verify the required parameter 'to' is set
        if (to == null) {
            throw new ApiException("Missing the required parameter 'to' when calling protectionGet(Async)");
        }

        // verify the required parameter 'xAccessToken' is set
        if (xAccessToken == null) {
            throw new ApiException("Missing the required parameter 'xAccessToken' when calling protectionGet(Async)");
        }

        return protectionGetCall(lat, lng, from, to, xAccessToken, alt, ozone, _callback);

    }

    /**
     * 
     * Get daily protection time by location, UV Index from and UV Index to with 10 minutes accuracy. Optional altitide and ozone level could be provided.
     * @param lat latitude, from -90.00 to 90.00 (required)
     * @param lng longitude, from -180.00 to 180.00 (required)
     * @param from UV Index from value for protection datetime lookup. From 0 to 40. (required)
     * @param to UV Index to value for protection datetime lookup. From 0 to 40. (required)
     * @param xAccessToken This header is used to send data that contains your OpenUV API key (required)
     * @param alt Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value. (optional)
     * @param ozone Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default. (optional)
     * @return ProtectionResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ProtectionResult protectionGet(BigDecimal lat, BigDecimal lng, BigDecimal from, BigDecimal to, String xAccessToken, BigDecimal alt, BigDecimal ozone) throws ApiException {
        ApiResponse<ProtectionResult> localVarResp = protectionGetWithHttpInfo(lat, lng, from, to, xAccessToken, alt, ozone);
        return localVarResp.getData();
    }

    /**
     * 
     * Get daily protection time by location, UV Index from and UV Index to with 10 minutes accuracy. Optional altitide and ozone level could be provided.
     * @param lat latitude, from -90.00 to 90.00 (required)
     * @param lng longitude, from -180.00 to 180.00 (required)
     * @param from UV Index from value for protection datetime lookup. From 0 to 40. (required)
     * @param to UV Index to value for protection datetime lookup. From 0 to 40. (required)
     * @param xAccessToken This header is used to send data that contains your OpenUV API key (required)
     * @param alt Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value. (optional)
     * @param ozone Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default. (optional)
     * @return ApiResponse&lt;ProtectionResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ProtectionResult> protectionGetWithHttpInfo(BigDecimal lat, BigDecimal lng, BigDecimal from, BigDecimal to, String xAccessToken, BigDecimal alt, BigDecimal ozone) throws ApiException {
        okhttp3.Call localVarCall = protectionGetValidateBeforeCall(lat, lng, from, to, xAccessToken, alt, ozone, null);
        Type localVarReturnType = new TypeToken<ProtectionResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Get daily protection time by location, UV Index from and UV Index to with 10 minutes accuracy. Optional altitide and ozone level could be provided.
     * @param lat latitude, from -90.00 to 90.00 (required)
     * @param lng longitude, from -180.00 to 180.00 (required)
     * @param from UV Index from value for protection datetime lookup. From 0 to 40. (required)
     * @param to UV Index to value for protection datetime lookup. From 0 to 40. (required)
     * @param xAccessToken This header is used to send data that contains your OpenUV API key (required)
     * @param alt Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value. (optional)
     * @param ozone Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call protectionGetAsync(BigDecimal lat, BigDecimal lng, BigDecimal from, BigDecimal to, String xAccessToken, BigDecimal alt, BigDecimal ozone, final ApiCallback<ProtectionResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = protectionGetValidateBeforeCall(lat, lng, from, to, xAccessToken, alt, ozone, _callback);
        Type localVarReturnType = new TypeToken<ProtectionResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for uvGet
     * @param lat latitude, from -90.00 to 90.00 (required)
     * @param lng longitude, from -180.00 to 180.00 (required)
     * @param xAccessToken This header is used to send data that contains your OpenUV API key (required)
     * @param alt Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value. (optional)
     * @param ozone Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default. (optional)
     * @param dt UTC datetime in ISO-8601 format, now by default. Use that parameter to get UV Index Forecast for any point in time. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call uvGetCall(BigDecimal lat, BigDecimal lng, String xAccessToken, BigDecimal alt, BigDecimal ozone, OffsetDateTime dt, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/uv";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (lat != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("lat", lat));
        }

        if (lng != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("lng", lng));
        }

        if (alt != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("alt", alt));
        }

        if (ozone != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("ozone", ozone));
        }

        if (dt != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("dt", dt));
        }

        if (xAccessToken != null) {
            localVarHeaderParams.put("x-access-token", localVarApiClient.parameterToString(xAccessToken));
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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call uvGetValidateBeforeCall(BigDecimal lat, BigDecimal lng, String xAccessToken, BigDecimal alt, BigDecimal ozone, OffsetDateTime dt, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'lat' is set
        if (lat == null) {
            throw new ApiException("Missing the required parameter 'lat' when calling uvGet(Async)");
        }

        // verify the required parameter 'lng' is set
        if (lng == null) {
            throw new ApiException("Missing the required parameter 'lng' when calling uvGet(Async)");
        }

        // verify the required parameter 'xAccessToken' is set
        if (xAccessToken == null) {
            throw new ApiException("Missing the required parameter 'xAccessToken' when calling uvGet(Async)");
        }

        return uvGetCall(lat, lng, xAccessToken, alt, ozone, dt, _callback);

    }

    /**
     * 
     * Get real-time UV Index by location. Optional altitude, ozone level and datetime could be provided.
     * @param lat latitude, from -90.00 to 90.00 (required)
     * @param lng longitude, from -180.00 to 180.00 (required)
     * @param xAccessToken This header is used to send data that contains your OpenUV API key (required)
     * @param alt Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value. (optional)
     * @param ozone Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default. (optional)
     * @param dt UTC datetime in ISO-8601 format, now by default. Use that parameter to get UV Index Forecast for any point in time. (optional)
     * @return UvIndexResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public UvIndexResult uvGet(BigDecimal lat, BigDecimal lng, String xAccessToken, BigDecimal alt, BigDecimal ozone, OffsetDateTime dt) throws ApiException {
        ApiResponse<UvIndexResult> localVarResp = uvGetWithHttpInfo(lat, lng, xAccessToken, alt, ozone, dt);
        return localVarResp.getData();
    }

    /**
     * 
     * Get real-time UV Index by location. Optional altitude, ozone level and datetime could be provided.
     * @param lat latitude, from -90.00 to 90.00 (required)
     * @param lng longitude, from -180.00 to 180.00 (required)
     * @param xAccessToken This header is used to send data that contains your OpenUV API key (required)
     * @param alt Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value. (optional)
     * @param ozone Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default. (optional)
     * @param dt UTC datetime in ISO-8601 format, now by default. Use that parameter to get UV Index Forecast for any point in time. (optional)
     * @return ApiResponse&lt;UvIndexResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UvIndexResult> uvGetWithHttpInfo(BigDecimal lat, BigDecimal lng, String xAccessToken, BigDecimal alt, BigDecimal ozone, OffsetDateTime dt) throws ApiException {
        okhttp3.Call localVarCall = uvGetValidateBeforeCall(lat, lng, xAccessToken, alt, ozone, dt, null);
        Type localVarReturnType = new TypeToken<UvIndexResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Get real-time UV Index by location. Optional altitude, ozone level and datetime could be provided.
     * @param lat latitude, from -90.00 to 90.00 (required)
     * @param lng longitude, from -180.00 to 180.00 (required)
     * @param xAccessToken This header is used to send data that contains your OpenUV API key (required)
     * @param alt Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value. (optional)
     * @param ozone Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default. (optional)
     * @param dt UTC datetime in ISO-8601 format, now by default. Use that parameter to get UV Index Forecast for any point in time. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call uvGetAsync(BigDecimal lat, BigDecimal lng, String xAccessToken, BigDecimal alt, BigDecimal ozone, OffsetDateTime dt, final ApiCallback<UvIndexResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = uvGetValidateBeforeCall(lat, lng, xAccessToken, alt, ozone, dt, _callback);
        Type localVarReturnType = new TypeToken<UvIndexResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
