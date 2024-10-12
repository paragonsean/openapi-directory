/*
 * LH Public API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
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



import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CargoApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public CargoApi() {
        this(Configuration.getDefaultApiClient());
    }

    public CargoApi(ApiClient apiClient) {
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
     * Build call for cargoGetRouteFromDateProductCodeByOriginAndDestinationGet
     * @param origin Departure Airport : 3-letter IATA airport code, e.g. FRA. (required)
     * @param destination Arrival airport : 3-letter IATA airport code, e.g. HKG. (required)
     * @param fromDate Departure date in the local time of the departure airport. Based on LAT (Latest Acceptance Time). format : yyyy-MM-dd eg : 2017-07-15 (required)
     * @param productCode Product code for requested service and specials : 3-letter eg: YNZ (required)
     * @param accept http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call cargoGetRouteFromDateProductCodeByOriginAndDestinationGetCall(String origin, String destination, String fromDate, String productCode, String accept, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/cargo/getRoute/{origin}-{destination}/{fromDate}/{productCode}"
            .replace("{" + "origin" + "}", localVarApiClient.escapeString(origin.toString()))
            .replace("{" + "destination" + "}", localVarApiClient.escapeString(destination.toString()))
            .replace("{" + "fromDate" + "}", localVarApiClient.escapeString(fromDate.toString()))
            .replace("{" + "productCode" + "}", localVarApiClient.escapeString(productCode.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (accept != null) {
            localVarHeaderParams.put("Accept", localVarApiClient.parameterToString(accept));
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

        String[] localVarAuthNames = new String[] { "auth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call cargoGetRouteFromDateProductCodeByOriginAndDestinationGetValidateBeforeCall(String origin, String destination, String fromDate, String productCode, String accept, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'origin' is set
        if (origin == null) {
            throw new ApiException("Missing the required parameter 'origin' when calling cargoGetRouteFromDateProductCodeByOriginAndDestinationGet(Async)");
        }

        // verify the required parameter 'destination' is set
        if (destination == null) {
            throw new ApiException("Missing the required parameter 'destination' when calling cargoGetRouteFromDateProductCodeByOriginAndDestinationGet(Async)");
        }

        // verify the required parameter 'fromDate' is set
        if (fromDate == null) {
            throw new ApiException("Missing the required parameter 'fromDate' when calling cargoGetRouteFromDateProductCodeByOriginAndDestinationGet(Async)");
        }

        // verify the required parameter 'productCode' is set
        if (productCode == null) {
            throw new ApiException("Missing the required parameter 'productCode' when calling cargoGetRouteFromDateProductCodeByOriginAndDestinationGet(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling cargoGetRouteFromDateProductCodeByOriginAndDestinationGet(Async)");
        }

        return cargoGetRouteFromDateProductCodeByOriginAndDestinationGetCall(origin, destination, fromDate, productCode, accept, _callback);

    }

    /**
     * Retrieve all flights
     * Retrieve a list of all possible flights (both direct and connecting) between two airports on a given date. Routes are available for today and up to days in the future.
     * @param origin Departure Airport : 3-letter IATA airport code, e.g. FRA. (required)
     * @param destination Arrival airport : 3-letter IATA airport code, e.g. HKG. (required)
     * @param fromDate Departure date in the local time of the departure airport. Based on LAT (Latest Acceptance Time). format : yyyy-MM-dd eg : 2017-07-15 (required)
     * @param productCode Product code for requested service and specials : 3-letter eg: YNZ (required)
     * @param accept http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public Object cargoGetRouteFromDateProductCodeByOriginAndDestinationGet(String origin, String destination, String fromDate, String productCode, String accept) throws ApiException {
        ApiResponse<Object> localVarResp = cargoGetRouteFromDateProductCodeByOriginAndDestinationGetWithHttpInfo(origin, destination, fromDate, productCode, accept);
        return localVarResp.getData();
    }

    /**
     * Retrieve all flights
     * Retrieve a list of all possible flights (both direct and connecting) between two airports on a given date. Routes are available for today and up to days in the future.
     * @param origin Departure Airport : 3-letter IATA airport code, e.g. FRA. (required)
     * @param destination Arrival airport : 3-letter IATA airport code, e.g. HKG. (required)
     * @param fromDate Departure date in the local time of the departure airport. Based on LAT (Latest Acceptance Time). format : yyyy-MM-dd eg : 2017-07-15 (required)
     * @param productCode Product code for requested service and specials : 3-letter eg: YNZ (required)
     * @param accept http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> cargoGetRouteFromDateProductCodeByOriginAndDestinationGetWithHttpInfo(String origin, String destination, String fromDate, String productCode, String accept) throws ApiException {
        okhttp3.Call localVarCall = cargoGetRouteFromDateProductCodeByOriginAndDestinationGetValidateBeforeCall(origin, destination, fromDate, productCode, accept, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve all flights (asynchronously)
     * Retrieve a list of all possible flights (both direct and connecting) between two airports on a given date. Routes are available for today and up to days in the future.
     * @param origin Departure Airport : 3-letter IATA airport code, e.g. FRA. (required)
     * @param destination Arrival airport : 3-letter IATA airport code, e.g. HKG. (required)
     * @param fromDate Departure date in the local time of the departure airport. Based on LAT (Latest Acceptance Time). format : yyyy-MM-dd eg : 2017-07-15 (required)
     * @param productCode Product code for requested service and specials : 3-letter eg: YNZ (required)
     * @param accept http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call cargoGetRouteFromDateProductCodeByOriginAndDestinationGetAsync(String origin, String destination, String fromDate, String productCode, String accept, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = cargoGetRouteFromDateProductCodeByOriginAndDestinationGetValidateBeforeCall(origin, destination, fromDate, productCode, accept, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for cargoShipmentTrackingByAWBPrefixAndAWBNumberGet
     * @param aWBPrefix aWBPrefix : Represents the airline that is the owner of this AWB, i.e. \&quot;020\&quot; &#x3D; Lufthansa Cargo, format : [0-9]{3} e.g. 020 (required)
     * @param aWBNumber aWBNumber : The Air Waybill Number , format : [0-9]{8} e.g. 08002050 (required)
     * @param accept http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call cargoShipmentTrackingByAWBPrefixAndAWBNumberGetCall(String aWBPrefix, String aWBNumber, String accept, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/cargo/shipmentTracking/{aWBPrefix}-{aWBNumber}"
            .replace("{" + "aWBPrefix" + "}", localVarApiClient.escapeString(aWBPrefix.toString()))
            .replace("{" + "aWBNumber" + "}", localVarApiClient.escapeString(aWBNumber.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (accept != null) {
            localVarHeaderParams.put("Accept", localVarApiClient.parameterToString(accept));
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

        String[] localVarAuthNames = new String[] { "auth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call cargoShipmentTrackingByAWBPrefixAndAWBNumberGetValidateBeforeCall(String aWBPrefix, String aWBNumber, String accept, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'aWBPrefix' is set
        if (aWBPrefix == null) {
            throw new ApiException("Missing the required parameter 'aWBPrefix' when calling cargoShipmentTrackingByAWBPrefixAndAWBNumberGet(Async)");
        }

        // verify the required parameter 'aWBNumber' is set
        if (aWBNumber == null) {
            throw new ApiException("Missing the required parameter 'aWBNumber' when calling cargoShipmentTrackingByAWBPrefixAndAWBNumberGet(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling cargoShipmentTrackingByAWBPrefixAndAWBNumberGet(Async)");
        }

        return cargoShipmentTrackingByAWBPrefixAndAWBNumberGetCall(aWBPrefix, aWBNumber, accept, _callback);

    }

    /**
     * Shipment Tracking
     * With this tracking service you can easily retrieve your shipment or flight status information.
     * @param aWBPrefix aWBPrefix : Represents the airline that is the owner of this AWB, i.e. \&quot;020\&quot; &#x3D; Lufthansa Cargo, format : [0-9]{3} e.g. 020 (required)
     * @param aWBNumber aWBNumber : The Air Waybill Number , format : [0-9]{8} e.g. 08002050 (required)
     * @param accept http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public Object cargoShipmentTrackingByAWBPrefixAndAWBNumberGet(String aWBPrefix, String aWBNumber, String accept) throws ApiException {
        ApiResponse<Object> localVarResp = cargoShipmentTrackingByAWBPrefixAndAWBNumberGetWithHttpInfo(aWBPrefix, aWBNumber, accept);
        return localVarResp.getData();
    }

    /**
     * Shipment Tracking
     * With this tracking service you can easily retrieve your shipment or flight status information.
     * @param aWBPrefix aWBPrefix : Represents the airline that is the owner of this AWB, i.e. \&quot;020\&quot; &#x3D; Lufthansa Cargo, format : [0-9]{3} e.g. 020 (required)
     * @param aWBNumber aWBNumber : The Air Waybill Number , format : [0-9]{8} e.g. 08002050 (required)
     * @param accept http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> cargoShipmentTrackingByAWBPrefixAndAWBNumberGetWithHttpInfo(String aWBPrefix, String aWBNumber, String accept) throws ApiException {
        okhttp3.Call localVarCall = cargoShipmentTrackingByAWBPrefixAndAWBNumberGetValidateBeforeCall(aWBPrefix, aWBNumber, accept, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Shipment Tracking (asynchronously)
     * With this tracking service you can easily retrieve your shipment or flight status information.
     * @param aWBPrefix aWBPrefix : Represents the airline that is the owner of this AWB, i.e. \&quot;020\&quot; &#x3D; Lufthansa Cargo, format : [0-9]{3} e.g. 020 (required)
     * @param aWBNumber aWBNumber : The Air Waybill Number , format : [0-9]{8} e.g. 08002050 (required)
     * @param accept http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call cargoShipmentTrackingByAWBPrefixAndAWBNumberGetAsync(String aWBPrefix, String aWBNumber, String accept, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = cargoShipmentTrackingByAWBPrefixAndAWBNumberGetValidateBeforeCall(aWBPrefix, aWBNumber, accept, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
