/*
 * IdealSpot GeoData
 * Hyperlocal Demographics, Vehicle Traffic, Economic, Market Signals, and More. Use this API to request IdealSpot hyperlocal geospatial market insight and geometry data.   ## Detailed Description  Use this API as your **local economy microscope** by querying [IdealSpot](https://www.idealspot.com) hyperlocal market insight and geometry data. We offer the most precise, extensive, and frequently-updated local market data in the US. Our data is available across the entire US and can be queried at geographic scales ranging from the micro (Census block) through the macro (nation).  Better data and analysis leads to a better understanding of local market opportunities and risks. Integrate with your commercial real estate and marketing applications, machine learning workflows, and other investment analytics.  Our goal is to offer the most complete snapshot of the geographically distributed consumer and retail economy. We start with the fundamentals of consumers and business establishments. To connect retailers with consumers, we provide mobility data like vehicle traffic and mobile device data. To describe consumer intent, we provide geolocated digital marketing data.   We believe that accurate capital allocation through reliable local market data is foundational to creating robust, healthy, and livable communities for all. We hope you and your clients find tremendous value in this service.  ## Features  Query data and GeoJSON geometries at these scales for any US latitude and longitude:  * Rings (0.5 km+) * Drive time (1-60 minutes) * Bike time (3-60 minutes) * Walk time (5-60 minutes) * Public transit time (5-60 minutes) * Administrative region (US, states, core-based statistical areas, counties, Census-designated places, Census tracts, zipcodes, Census block groups, opportunity zones)  | Data Feature | Description | | ------- | ------------------------------| | Demographics, Housing, Spending | *Updated Quarterly*.  Current and historical market data including population, spending, and housing. Vendor (PopStats) is relied upon by Walgreens, Ulta Beauty, Blackstone, etc | | Labor, Business Establishments, Economic Conditions | *Updated Quarterly*.  Traditional market data including workforce, business establishment counts, and economic conditions like local GDP, unemployment rates. Vendor (PopStats) is relied upon by Walgreens, Ulta Beauty, Blackstone, etc | | Consumer segmentation | *Updated Annually*. Demographics grouped into narrative-oriented segments. | | Vehicle Traffic | *Updated semi-annually*. Gold standard in vehicle traffic data from INRIX. Counts by day of week, time of day and side of street. | | Rings and Travel time polygons | *Estimate in Real-time*. Rings alongside drive time, walk time, bike time, and public transit time polygons. Request as GeoJSON geometries for mapping or use with data queries | | Administrative region polygons | *Updated Annually*. GeoJSON administrative regions from US Census Bureau: block groups, tracts, counties, CBSAs, states, opportunity zones, USPS zipcodes | | Internet Search Volumes | 30 day rolling averages for geolocated advertising potential across 450 business categories from major search engines | | Social Media Interest | 30 day rolling average for geolocated advertising potential across 450 business categories from major social networks |  ### Coming Soon!  This API powers our local market research platform at [IdealSpot.com](https://www.idealspot.com). The functionality exposed so far is only a portion of our current capabilities. We will be exposing additional API features in time so watch this space!  | Data Feature | Description | | ------- | ------------------------------| Mobile device visit counts, points of interest, brands | Fresh point of interest data across 3000+ brands, millions of POI, and historical foot traffic counts using mobile data for those points of interest Origin/destination trips from mobile devices | Map origins and destinations of devices visiting an arbitrary catchment area Competition search | Search all major point-of-interest aggregators in one query Environment/climate | Expected weather patterns like temperature and precipitation Filter search API | Query data for all counties in state, all tracts in MSA, etc Road segment tiles | Plot road segments on maps in interactive applications  ## Developer Website  For more detail see https://developer.idealspot.com/
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


import org.openapitools.client.model.Describetheregionwithin5minutedriveTimeofageographicpoint;
import org.openapitools.client.model.FetchAdministrativeRegionsusingLatLng;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class GeometriesApiApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public GeometriesApiApi() {
        this(Configuration.getDefaultApiClient());
    }

    public GeometriesApiApi(ApiClient apiClient) {
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
     * Build call for fetchAdministrativeRegionsusingLatLng
     * @param latitude (Required) Search coordinate latitude (required)
     * @param longitude (Required) Search coordinate longitude (required)
     * @param xRapidAPIKey (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata (required)
     * @param xRapidAPIHost  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Server -  <br>  * Vary -  <br>  * Via -  <br>  * X-RapidAPI-Region -  <br>  * X-RapidAPI-Version -  <br>  * access-control-allow-credentials -  <br>  * access-control-allow-origin -  <br>  * access-control-expose-headers -  <br>  * cache-control -  <br>  * transfer-encoding -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call fetchAdministrativeRegionsusingLatLngCall(Double latitude, Double longitude, String xRapidAPIKey, String xRapidAPIHost, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/geometries/regions/intersecting/{latitude}/{longitude}"
            .replace("{" + "latitude" + "}", localVarApiClient.escapeString(latitude.toString()))
            .replace("{" + "longitude" + "}", localVarApiClient.escapeString(longitude.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xRapidAPIKey != null) {
            localVarHeaderParams.put("X-RapidAPI-Key", localVarApiClient.parameterToString(xRapidAPIKey));
        }

        if (xRapidAPIHost != null) {
            localVarHeaderParams.put("X-RapidAPI-Host", localVarApiClient.parameterToString(xRapidAPIHost));
        }

        final String[] localVarAccepts = {
            "application/json; charset=utf-8"
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
    private okhttp3.Call fetchAdministrativeRegionsusingLatLngValidateBeforeCall(Double latitude, Double longitude, String xRapidAPIKey, String xRapidAPIHost, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'latitude' is set
        if (latitude == null) {
            throw new ApiException("Missing the required parameter 'latitude' when calling fetchAdministrativeRegionsusingLatLng(Async)");
        }

        // verify the required parameter 'longitude' is set
        if (longitude == null) {
            throw new ApiException("Missing the required parameter 'longitude' when calling fetchAdministrativeRegionsusingLatLng(Async)");
        }

        // verify the required parameter 'xRapidAPIKey' is set
        if (xRapidAPIKey == null) {
            throw new ApiException("Missing the required parameter 'xRapidAPIKey' when calling fetchAdministrativeRegionsusingLatLng(Async)");
        }

        // verify the required parameter 'xRapidAPIHost' is set
        if (xRapidAPIHost == null) {
            throw new ApiException("Missing the required parameter 'xRapidAPIHost' when calling fetchAdministrativeRegionsusingLatLng(Async)");
        }

        return fetchAdministrativeRegionsusingLatLngCall(latitude, longitude, xRapidAPIKey, xRapidAPIHost, _callback);

    }

    /**
     * Fetch Administrative Regions using Lat/Lng
     * For given latitude and longitude, find intersecting administrative regions. Region polygons are simplified for web mapping.
     * @param latitude (Required) Search coordinate latitude (required)
     * @param longitude (Required) Search coordinate longitude (required)
     * @param xRapidAPIKey (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata (required)
     * @param xRapidAPIHost  (required)
     * @return FetchAdministrativeRegionsusingLatLng
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Server -  <br>  * Vary -  <br>  * Via -  <br>  * X-RapidAPI-Region -  <br>  * X-RapidAPI-Version -  <br>  * access-control-allow-credentials -  <br>  * access-control-allow-origin -  <br>  * access-control-expose-headers -  <br>  * cache-control -  <br>  * transfer-encoding -  <br>  </td></tr>
     </table>
     */
    public FetchAdministrativeRegionsusingLatLng fetchAdministrativeRegionsusingLatLng(Double latitude, Double longitude, String xRapidAPIKey, String xRapidAPIHost) throws ApiException {
        ApiResponse<FetchAdministrativeRegionsusingLatLng> localVarResp = fetchAdministrativeRegionsusingLatLngWithHttpInfo(latitude, longitude, xRapidAPIKey, xRapidAPIHost);
        return localVarResp.getData();
    }

    /**
     * Fetch Administrative Regions using Lat/Lng
     * For given latitude and longitude, find intersecting administrative regions. Region polygons are simplified for web mapping.
     * @param latitude (Required) Search coordinate latitude (required)
     * @param longitude (Required) Search coordinate longitude (required)
     * @param xRapidAPIKey (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata (required)
     * @param xRapidAPIHost  (required)
     * @return ApiResponse&lt;FetchAdministrativeRegionsusingLatLng&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Server -  <br>  * Vary -  <br>  * Via -  <br>  * X-RapidAPI-Region -  <br>  * X-RapidAPI-Version -  <br>  * access-control-allow-credentials -  <br>  * access-control-allow-origin -  <br>  * access-control-expose-headers -  <br>  * cache-control -  <br>  * transfer-encoding -  <br>  </td></tr>
     </table>
     */
    public ApiResponse<FetchAdministrativeRegionsusingLatLng> fetchAdministrativeRegionsusingLatLngWithHttpInfo(Double latitude, Double longitude, String xRapidAPIKey, String xRapidAPIHost) throws ApiException {
        okhttp3.Call localVarCall = fetchAdministrativeRegionsusingLatLngValidateBeforeCall(latitude, longitude, xRapidAPIKey, xRapidAPIHost, null);
        Type localVarReturnType = new TypeToken<FetchAdministrativeRegionsusingLatLng>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Fetch Administrative Regions using Lat/Lng (asynchronously)
     * For given latitude and longitude, find intersecting administrative regions. Region polygons are simplified for web mapping.
     * @param latitude (Required) Search coordinate latitude (required)
     * @param longitude (Required) Search coordinate longitude (required)
     * @param xRapidAPIKey (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata (required)
     * @param xRapidAPIHost  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Server -  <br>  * Vary -  <br>  * Via -  <br>  * X-RapidAPI-Region -  <br>  * X-RapidAPI-Version -  <br>  * access-control-allow-credentials -  <br>  * access-control-allow-origin -  <br>  * access-control-expose-headers -  <br>  * cache-control -  <br>  * transfer-encoding -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call fetchAdministrativeRegionsusingLatLngAsync(Double latitude, Double longitude, String xRapidAPIKey, String xRapidAPIHost, final ApiCallback<FetchAdministrativeRegionsusingLatLng> _callback) throws ApiException {

        okhttp3.Call localVarCall = fetchAdministrativeRegionsusingLatLngValidateBeforeCall(latitude, longitude, xRapidAPIKey, xRapidAPIHost, _callback);
        Type localVarReturnType = new TypeToken<FetchAdministrativeRegionsusingLatLng>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for fetchGeometries
     * @param location (Required) Represents a buffer, region, or custom polygon specification. Accepts the &#x60;Location&#x60; model (as a &#x60;Buffer&#x60;, &#x60;Region&#x60;, or &#x60;Custom Polygon&#x60;) formatted as a JSON string. Multiple &#x60;location&#x60; query parameters are allowed. NOTE: When requesting multiple locations, you must include brackets(i.e. &#x60;?location[]&#x3D;...&amp;location[]&#x3D;...&#x60;). If not included, only the last location will be used. (required)
     * @param xRapidAPIKey (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata (required)
     * @param xRapidAPIHost  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * Vary -  <br>  * Via -  <br>  * X-RapidAPI-Region -  <br>  * X-RapidAPI-Version -  <br>  * access-control-allow-credentials -  <br>  * access-control-allow-origin -  <br>  * access-control-expose-headers -  <br>  * cache-control -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call fetchGeometriesCall(String location, String xRapidAPIKey, String xRapidAPIHost, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/geometries/geometry";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (location != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("location[]", location));
        }

        if (xRapidAPIKey != null) {
            localVarHeaderParams.put("X-RapidAPI-Key", localVarApiClient.parameterToString(xRapidAPIKey));
        }

        if (xRapidAPIHost != null) {
            localVarHeaderParams.put("X-RapidAPI-Host", localVarApiClient.parameterToString(xRapidAPIHost));
        }

        final String[] localVarAccepts = {
            "application/json; charset=utf-8"
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
    private okhttp3.Call fetchGeometriesValidateBeforeCall(String location, String xRapidAPIKey, String xRapidAPIHost, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'location' is set
        if (location == null) {
            throw new ApiException("Missing the required parameter 'location' when calling fetchGeometries(Async)");
        }

        // verify the required parameter 'xRapidAPIKey' is set
        if (xRapidAPIKey == null) {
            throw new ApiException("Missing the required parameter 'xRapidAPIKey' when calling fetchGeometries(Async)");
        }

        // verify the required parameter 'xRapidAPIHost' is set
        if (xRapidAPIHost == null) {
            throw new ApiException("Missing the required parameter 'xRapidAPIHost' when calling fetchGeometries(Async)");
        }

        return fetchGeometriesCall(location, xRapidAPIKey, xRapidAPIHost, _callback);

    }

    /**
     * Fetch Geometries
     * Fetch location GeoJSON
     * @param location (Required) Represents a buffer, region, or custom polygon specification. Accepts the &#x60;Location&#x60; model (as a &#x60;Buffer&#x60;, &#x60;Region&#x60;, or &#x60;Custom Polygon&#x60;) formatted as a JSON string. Multiple &#x60;location&#x60; query parameters are allowed. NOTE: When requesting multiple locations, you must include brackets(i.e. &#x60;?location[]&#x3D;...&amp;location[]&#x3D;...&#x60;). If not included, only the last location will be used. (required)
     * @param xRapidAPIKey (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata (required)
     * @param xRapidAPIHost  (required)
     * @return Describetheregionwithin5minutedriveTimeofageographicpoint
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * Vary -  <br>  * Via -  <br>  * X-RapidAPI-Region -  <br>  * X-RapidAPI-Version -  <br>  * access-control-allow-credentials -  <br>  * access-control-allow-origin -  <br>  * access-control-expose-headers -  <br>  * cache-control -  <br>  </td></tr>
     </table>
     */
    public Describetheregionwithin5minutedriveTimeofageographicpoint fetchGeometries(String location, String xRapidAPIKey, String xRapidAPIHost) throws ApiException {
        ApiResponse<Describetheregionwithin5minutedriveTimeofageographicpoint> localVarResp = fetchGeometriesWithHttpInfo(location, xRapidAPIKey, xRapidAPIHost);
        return localVarResp.getData();
    }

    /**
     * Fetch Geometries
     * Fetch location GeoJSON
     * @param location (Required) Represents a buffer, region, or custom polygon specification. Accepts the &#x60;Location&#x60; model (as a &#x60;Buffer&#x60;, &#x60;Region&#x60;, or &#x60;Custom Polygon&#x60;) formatted as a JSON string. Multiple &#x60;location&#x60; query parameters are allowed. NOTE: When requesting multiple locations, you must include brackets(i.e. &#x60;?location[]&#x3D;...&amp;location[]&#x3D;...&#x60;). If not included, only the last location will be used. (required)
     * @param xRapidAPIKey (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata (required)
     * @param xRapidAPIHost  (required)
     * @return ApiResponse&lt;Describetheregionwithin5minutedriveTimeofageographicpoint&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * Vary -  <br>  * Via -  <br>  * X-RapidAPI-Region -  <br>  * X-RapidAPI-Version -  <br>  * access-control-allow-credentials -  <br>  * access-control-allow-origin -  <br>  * access-control-expose-headers -  <br>  * cache-control -  <br>  </td></tr>
     </table>
     */
    public ApiResponse<Describetheregionwithin5minutedriveTimeofageographicpoint> fetchGeometriesWithHttpInfo(String location, String xRapidAPIKey, String xRapidAPIHost) throws ApiException {
        okhttp3.Call localVarCall = fetchGeometriesValidateBeforeCall(location, xRapidAPIKey, xRapidAPIHost, null);
        Type localVarReturnType = new TypeToken<Describetheregionwithin5minutedriveTimeofageographicpoint>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Fetch Geometries (asynchronously)
     * Fetch location GeoJSON
     * @param location (Required) Represents a buffer, region, or custom polygon specification. Accepts the &#x60;Location&#x60; model (as a &#x60;Buffer&#x60;, &#x60;Region&#x60;, or &#x60;Custom Polygon&#x60;) formatted as a JSON string. Multiple &#x60;location&#x60; query parameters are allowed. NOTE: When requesting multiple locations, you must include brackets(i.e. &#x60;?location[]&#x3D;...&amp;location[]&#x3D;...&#x60;). If not included, only the last location will be used. (required)
     * @param xRapidAPIKey (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata (required)
     * @param xRapidAPIHost  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * Vary -  <br>  * Via -  <br>  * X-RapidAPI-Region -  <br>  * X-RapidAPI-Version -  <br>  * access-control-allow-credentials -  <br>  * access-control-allow-origin -  <br>  * access-control-expose-headers -  <br>  * cache-control -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call fetchGeometriesAsync(String location, String xRapidAPIKey, String xRapidAPIHost, final ApiCallback<Describetheregionwithin5minutedriveTimeofageographicpoint> _callback) throws ApiException {

        okhttp3.Call localVarCall = fetchGeometriesValidateBeforeCall(location, xRapidAPIKey, xRapidAPIHost, _callback);
        Type localVarReturnType = new TypeToken<Describetheregionwithin5minutedriveTimeofageographicpoint>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
