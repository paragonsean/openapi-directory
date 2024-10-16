/*
 * Mon-voyage-pas-cher.com Public API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.1
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


import org.openapitools.client.model.DistanceResponse;
import org.openapitools.client.model.ElevationResponse;
import org.openapitools.client.model.ErrorResponse;
import java.time.LocalDate;
import org.openapitools.client.model.SunPositionResponse;
import org.openapitools.client.model.TimezoneResponse;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ServicesApisApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ServicesApisApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ServicesApisApi(ApiClient apiClient) {
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
     * Build call for getDistance
     * @param locationA The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) of location point A (required)
     * @param locationB The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) of location point B (required)
     * @param unit The unit of length you want the elevation returned either meters or feet returned (optional, default to kms)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> The error message object </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDistanceCall(String locationA, String locationB, String unit, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/distance";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (locationA != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("locationA", locationA));
        }

        if (locationB != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("locationB", locationB));
        }

        if (unit != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("unit", unit));
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

        String[] localVarAuthNames = new String[] { "x-api-key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getDistanceValidateBeforeCall(String locationA, String locationB, String unit, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'locationA' is set
        if (locationA == null) {
            throw new ApiException("Missing the required parameter 'locationA' when calling getDistance(Async)");
        }

        // verify the required parameter 'locationB' is set
        if (locationB == null) {
            throw new ApiException("Missing the required parameter 'locationB' when calling getDistance(Async)");
        }

        return getDistanceCall(locationA, locationB, unit, _callback);

    }

    /**
     * Calculate distance between lats/longs
     * This webservice is providing you the ability to calculate the distance between 2 lat/long points, it returns you the value in km or miles
     * @param locationA The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) of location point A (required)
     * @param locationB The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) of location point B (required)
     * @param unit The unit of length you want the elevation returned either meters or feet returned (optional, default to kms)
     * @return DistanceResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> The error message object </td><td>  -  </td></tr>
     </table>
     */
    public DistanceResponse getDistance(String locationA, String locationB, String unit) throws ApiException {
        ApiResponse<DistanceResponse> localVarResp = getDistanceWithHttpInfo(locationA, locationB, unit);
        return localVarResp.getData();
    }

    /**
     * Calculate distance between lats/longs
     * This webservice is providing you the ability to calculate the distance between 2 lat/long points, it returns you the value in km or miles
     * @param locationA The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) of location point A (required)
     * @param locationB The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) of location point B (required)
     * @param unit The unit of length you want the elevation returned either meters or feet returned (optional, default to kms)
     * @return ApiResponse&lt;DistanceResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> The error message object </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DistanceResponse> getDistanceWithHttpInfo(String locationA, String locationB, String unit) throws ApiException {
        okhttp3.Call localVarCall = getDistanceValidateBeforeCall(locationA, locationB, unit, null);
        Type localVarReturnType = new TypeToken<DistanceResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Calculate distance between lats/longs (asynchronously)
     * This webservice is providing you the ability to calculate the distance between 2 lat/long points, it returns you the value in km or miles
     * @param locationA The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) of location point A (required)
     * @param locationB The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) of location point B (required)
     * @param unit The unit of length you want the elevation returned either meters or feet returned (optional, default to kms)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> The error message object </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDistanceAsync(String locationA, String locationB, String unit, final ApiCallback<DistanceResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDistanceValidateBeforeCall(locationA, locationB, unit, _callback);
        Type localVarReturnType = new TypeToken<DistanceResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getElevation
     * @param locations The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) or a list of coordinates separated using the pipe (&#39;|&#39;) character. The maximum number of coordinates you can send at one time is 20 ( ex. 67.85572,20.22513|27.85572,20.22513 ) (required)
     * @param unit The unit of length you want the elevation returned either meters or feet returned (optional, default to meters)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> The error message object </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getElevationCall(String locations, String unit, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/elevation";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (locations != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("locations", locations));
        }

        if (unit != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("unit", unit));
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

        String[] localVarAuthNames = new String[] { "x-api-key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getElevationValidateBeforeCall(String locations, String unit, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'locations' is set
        if (locations == null) {
            throw new ApiException("Missing the required parameter 'locations' when calling getElevation(Async)");
        }

        return getElevationCall(locations, unit, _callback);

    }

    /**
     * Search elevation informations from lat/long
     * This webservice is providing you the ability to retrieve the elevation in meters or feet of ONE or MULTIPLE given latitude/longitude point(s). &lt;br /&gt;If you use MULTIPLE lat/long point, the maximum number of point you can send in one request is 256. Be aware that if MULTIPLE mode, the results are de-deplicated if you are sending the same latitude/longitude point multiple times.&lt;br /&gt;If your workload is a batch of millions of lat/long point, You will also get better throughput if you send around 100 lat/long points in one request than the maximum. This maximum is mostly allowed for people trying to graph altitudes.
     * @param locations The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) or a list of coordinates separated using the pipe (&#39;|&#39;) character. The maximum number of coordinates you can send at one time is 20 ( ex. 67.85572,20.22513|27.85572,20.22513 ) (required)
     * @param unit The unit of length you want the elevation returned either meters or feet returned (optional, default to meters)
     * @return ElevationResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> The error message object </td><td>  -  </td></tr>
     </table>
     */
    public ElevationResponse getElevation(String locations, String unit) throws ApiException {
        ApiResponse<ElevationResponse> localVarResp = getElevationWithHttpInfo(locations, unit);
        return localVarResp.getData();
    }

    /**
     * Search elevation informations from lat/long
     * This webservice is providing you the ability to retrieve the elevation in meters or feet of ONE or MULTIPLE given latitude/longitude point(s). &lt;br /&gt;If you use MULTIPLE lat/long point, the maximum number of point you can send in one request is 256. Be aware that if MULTIPLE mode, the results are de-deplicated if you are sending the same latitude/longitude point multiple times.&lt;br /&gt;If your workload is a batch of millions of lat/long point, You will also get better throughput if you send around 100 lat/long points in one request than the maximum. This maximum is mostly allowed for people trying to graph altitudes.
     * @param locations The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) or a list of coordinates separated using the pipe (&#39;|&#39;) character. The maximum number of coordinates you can send at one time is 20 ( ex. 67.85572,20.22513|27.85572,20.22513 ) (required)
     * @param unit The unit of length you want the elevation returned either meters or feet returned (optional, default to meters)
     * @return ApiResponse&lt;ElevationResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> The error message object </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ElevationResponse> getElevationWithHttpInfo(String locations, String unit) throws ApiException {
        okhttp3.Call localVarCall = getElevationValidateBeforeCall(locations, unit, null);
        Type localVarReturnType = new TypeToken<ElevationResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Search elevation informations from lat/long (asynchronously)
     * This webservice is providing you the ability to retrieve the elevation in meters or feet of ONE or MULTIPLE given latitude/longitude point(s). &lt;br /&gt;If you use MULTIPLE lat/long point, the maximum number of point you can send in one request is 256. Be aware that if MULTIPLE mode, the results are de-deplicated if you are sending the same latitude/longitude point multiple times.&lt;br /&gt;If your workload is a batch of millions of lat/long point, You will also get better throughput if you send around 100 lat/long points in one request than the maximum. This maximum is mostly allowed for people trying to graph altitudes.
     * @param locations The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) or a list of coordinates separated using the pipe (&#39;|&#39;) character. The maximum number of coordinates you can send at one time is 20 ( ex. 67.85572,20.22513|27.85572,20.22513 ) (required)
     * @param unit The unit of length you want the elevation returned either meters or feet returned (optional, default to meters)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> The error message object </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getElevationAsync(String locations, String unit, final ApiCallback<ElevationResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getElevationValidateBeforeCall(locations, unit, _callback);
        Type localVarReturnType = new TypeToken<ElevationResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getSun
     * @param location Here you can send either a latitude / longitude (required)
     * @param date The date for what you will get the data ( full-date notation as defined by RFC 3339, section 5.6, for example, 2017-07-21 ), if not provided as parameter, today is going to be used (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> The error message object </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSunCall(String location, LocalDate date, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/sun_positions";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (location != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("location", location));
        }

        if (date != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("date", date));
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

        String[] localVarAuthNames = new String[] { "x-api-key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getSunValidateBeforeCall(String location, LocalDate date, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'location' is set
        if (location == null) {
            throw new ApiException("Missing the required parameter 'location' when calling getSun(Async)");
        }

        return getSunCall(location, date, _callback);

    }

    /**
     * Search position of sun from lat/long and date
     * This webservice is providing you the ability to retrieve the time of each phases of the sunlight cycle. Sunset, sunrise, sunriseEnd, golden hour, solarNoon, dawn, dusk and more for a given location and date. If the date if not provided, the response provided return informations for today at UTC time.
     * @param location Here you can send either a latitude / longitude (required)
     * @param date The date for what you will get the data ( full-date notation as defined by RFC 3339, section 5.6, for example, 2017-07-21 ), if not provided as parameter, today is going to be used (optional)
     * @return SunPositionResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> The error message object </td><td>  -  </td></tr>
     </table>
     */
    public SunPositionResponse getSun(String location, LocalDate date) throws ApiException {
        ApiResponse<SunPositionResponse> localVarResp = getSunWithHttpInfo(location, date);
        return localVarResp.getData();
    }

    /**
     * Search position of sun from lat/long and date
     * This webservice is providing you the ability to retrieve the time of each phases of the sunlight cycle. Sunset, sunrise, sunriseEnd, golden hour, solarNoon, dawn, dusk and more for a given location and date. If the date if not provided, the response provided return informations for today at UTC time.
     * @param location Here you can send either a latitude / longitude (required)
     * @param date The date for what you will get the data ( full-date notation as defined by RFC 3339, section 5.6, for example, 2017-07-21 ), if not provided as parameter, today is going to be used (optional)
     * @return ApiResponse&lt;SunPositionResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> The error message object </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<SunPositionResponse> getSunWithHttpInfo(String location, LocalDate date) throws ApiException {
        okhttp3.Call localVarCall = getSunValidateBeforeCall(location, date, null);
        Type localVarReturnType = new TypeToken<SunPositionResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Search position of sun from lat/long and date (asynchronously)
     * This webservice is providing you the ability to retrieve the time of each phases of the sunlight cycle. Sunset, sunrise, sunriseEnd, golden hour, solarNoon, dawn, dusk and more for a given location and date. If the date if not provided, the response provided return informations for today at UTC time.
     * @param location Here you can send either a latitude / longitude (required)
     * @param date The date for what you will get the data ( full-date notation as defined by RFC 3339, section 5.6, for example, 2017-07-21 ), if not provided as parameter, today is going to be used (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> The error message object </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSunAsync(String location, LocalDate date, final ApiCallback<SunPositionResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getSunValidateBeforeCall(location, date, _callback);
        Type localVarReturnType = new TypeToken<SunPositionResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getTimezone
     * @param location Here you can send either a latitude / longitude ( ex. 67.85572,20.22513 ) or a IATA Code ( ex. LHR for London Heathrow) (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> The error message object </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getTimezoneCall(String location, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/timezone";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (location != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("location", location));
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

        String[] localVarAuthNames = new String[] { "x-api-key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getTimezoneValidateBeforeCall(String location, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'location' is set
        if (location == null) {
            throw new ApiException("Missing the required parameter 'location' when calling getTimezone(Async)");
        }

        return getTimezoneCall(location, _callback);

    }

    /**
     * Search timezone and time informations from lat/long
     * This webservice is providing you the ability to retrieve the tz database time zones ( https://en.wikipedia.org/wiki/List_of_tz_database_time_zones )  from a given location ( )latitude and longitude or IATA code ). It also returns you the current time at the provided location.
     * @param location Here you can send either a latitude / longitude ( ex. 67.85572,20.22513 ) or a IATA Code ( ex. LHR for London Heathrow) (required)
     * @return TimezoneResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> The error message object </td><td>  -  </td></tr>
     </table>
     */
    public TimezoneResponse getTimezone(String location) throws ApiException {
        ApiResponse<TimezoneResponse> localVarResp = getTimezoneWithHttpInfo(location);
        return localVarResp.getData();
    }

    /**
     * Search timezone and time informations from lat/long
     * This webservice is providing you the ability to retrieve the tz database time zones ( https://en.wikipedia.org/wiki/List_of_tz_database_time_zones )  from a given location ( )latitude and longitude or IATA code ). It also returns you the current time at the provided location.
     * @param location Here you can send either a latitude / longitude ( ex. 67.85572,20.22513 ) or a IATA Code ( ex. LHR for London Heathrow) (required)
     * @return ApiResponse&lt;TimezoneResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> The error message object </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<TimezoneResponse> getTimezoneWithHttpInfo(String location) throws ApiException {
        okhttp3.Call localVarCall = getTimezoneValidateBeforeCall(location, null);
        Type localVarReturnType = new TypeToken<TimezoneResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Search timezone and time informations from lat/long (asynchronously)
     * This webservice is providing you the ability to retrieve the tz database time zones ( https://en.wikipedia.org/wiki/List_of_tz_database_time_zones )  from a given location ( )latitude and longitude or IATA code ). It also returns you the current time at the provided location.
     * @param location Here you can send either a latitude / longitude ( ex. 67.85572,20.22513 ) or a IATA Code ( ex. LHR for London Heathrow) (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> The error message object </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getTimezoneAsync(String location, final ApiCallback<TimezoneResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getTimezoneValidateBeforeCall(location, _callback);
        Type localVarReturnType = new TypeToken<TimezoneResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
