/*
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
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

public class PacketsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public PacketsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public PacketsApi(ApiClient apiClient) {
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
     * Build call for getDeviceSwitchPortsStatusesPackets_3
     * @param serial  (required)
     * @param t0 The beginning of the timespan for the data. The maximum lookback period is 1 day from today. (optional)
     * @param timespan The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 1 day. The default is 1 day. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDeviceSwitchPortsStatusesPackets_3Call(String serial, String t0, Float timespan, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/devices/{serial}/switch/ports/statuses/packets"
            .replace("{" + "serial" + "}", localVarApiClient.escapeString(serial.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (t0 != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("t0", t0));
        }

        if (timespan != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("timespan", timespan));
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

        String[] localVarAuthNames = new String[] { "meraki_api_key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getDeviceSwitchPortsStatusesPackets_3ValidateBeforeCall(String serial, String t0, Float timespan, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'serial' is set
        if (serial == null) {
            throw new ApiException("Missing the required parameter 'serial' when calling getDeviceSwitchPortsStatusesPackets_3(Async)");
        }

        return getDeviceSwitchPortsStatusesPackets_3Call(serial, t0, timespan, _callback);

    }

    /**
     * Return the packet counters for all the ports of a switch
     * Return the packet counters for all the ports of a switch
     * @param serial  (required)
     * @param t0 The beginning of the timespan for the data. The maximum lookback period is 1 day from today. (optional)
     * @param timespan The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 1 day. The default is 1 day. (optional)
     * @return List&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public List<Object> getDeviceSwitchPortsStatusesPackets_3(String serial, String t0, Float timespan) throws ApiException {
        ApiResponse<List<Object>> localVarResp = getDeviceSwitchPortsStatusesPackets_3WithHttpInfo(serial, t0, timespan);
        return localVarResp.getData();
    }

    /**
     * Return the packet counters for all the ports of a switch
     * Return the packet counters for all the ports of a switch
     * @param serial  (required)
     * @param t0 The beginning of the timespan for the data. The maximum lookback period is 1 day from today. (optional)
     * @param timespan The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 1 day. The default is 1 day. (optional)
     * @return ApiResponse&lt;List&lt;Object&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<Object>> getDeviceSwitchPortsStatusesPackets_3WithHttpInfo(String serial, String t0, Float timespan) throws ApiException {
        okhttp3.Call localVarCall = getDeviceSwitchPortsStatusesPackets_3ValidateBeforeCall(serial, t0, timespan, null);
        Type localVarReturnType = new TypeToken<List<Object>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Return the packet counters for all the ports of a switch (asynchronously)
     * Return the packet counters for all the ports of a switch
     * @param serial  (required)
     * @param t0 The beginning of the timespan for the data. The maximum lookback period is 1 day from today. (optional)
     * @param timespan The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 1 day. The default is 1 day. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDeviceSwitchPortsStatusesPackets_3Async(String serial, String t0, Float timespan, final ApiCallback<List<Object>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDeviceSwitchPortsStatusesPackets_3ValidateBeforeCall(serial, t0, timespan, _callback);
        Type localVarReturnType = new TypeToken<List<Object>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
