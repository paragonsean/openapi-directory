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

public class TrafficApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public TrafficApi() {
        this(Configuration.getDefaultApiClient());
    }

    public TrafficApi(ApiClient apiClient) {
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
     * Build call for getNetworkTraffic_1
     * @param networkId  (required)
     * @param t0 The beginning of the timespan for the data. The maximum lookback period is 30 days from today. (optional)
     * @param timespan The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 30 days. (optional)
     * @param deviceType Filter the data by device type: &#39;combined&#39;, &#39;wireless&#39;, &#39;switch&#39; or &#39;appliance&#39;. Defaults to &#39;combined&#39;. When using &#39;combined&#39;, for each rule the data will come from the device type with the most usage. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNetworkTraffic_1Call(String networkId, String t0, Float timespan, String deviceType, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/networks/{networkId}/traffic"
            .replace("{" + "networkId" + "}", localVarApiClient.escapeString(networkId.toString()));

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

        if (deviceType != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("deviceType", deviceType));
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
    private okhttp3.Call getNetworkTraffic_1ValidateBeforeCall(String networkId, String t0, Float timespan, String deviceType, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling getNetworkTraffic_1(Async)");
        }

        return getNetworkTraffic_1Call(networkId, t0, timespan, deviceType, _callback);

    }

    /**
     * Return the traffic analysis data for this network
     * Return the traffic analysis data for this network. Traffic analysis with hostname visibility must be enabled on the network.
     * @param networkId  (required)
     * @param t0 The beginning of the timespan for the data. The maximum lookback period is 30 days from today. (optional)
     * @param timespan The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 30 days. (optional)
     * @param deviceType Filter the data by device type: &#39;combined&#39;, &#39;wireless&#39;, &#39;switch&#39; or &#39;appliance&#39;. Defaults to &#39;combined&#39;. When using &#39;combined&#39;, for each rule the data will come from the device type with the most usage. (optional)
     * @return List&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public List<Object> getNetworkTraffic_1(String networkId, String t0, Float timespan, String deviceType) throws ApiException {
        ApiResponse<List<Object>> localVarResp = getNetworkTraffic_1WithHttpInfo(networkId, t0, timespan, deviceType);
        return localVarResp.getData();
    }

    /**
     * Return the traffic analysis data for this network
     * Return the traffic analysis data for this network. Traffic analysis with hostname visibility must be enabled on the network.
     * @param networkId  (required)
     * @param t0 The beginning of the timespan for the data. The maximum lookback period is 30 days from today. (optional)
     * @param timespan The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 30 days. (optional)
     * @param deviceType Filter the data by device type: &#39;combined&#39;, &#39;wireless&#39;, &#39;switch&#39; or &#39;appliance&#39;. Defaults to &#39;combined&#39;. When using &#39;combined&#39;, for each rule the data will come from the device type with the most usage. (optional)
     * @return ApiResponse&lt;List&lt;Object&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<Object>> getNetworkTraffic_1WithHttpInfo(String networkId, String t0, Float timespan, String deviceType) throws ApiException {
        okhttp3.Call localVarCall = getNetworkTraffic_1ValidateBeforeCall(networkId, t0, timespan, deviceType, null);
        Type localVarReturnType = new TypeToken<List<Object>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Return the traffic analysis data for this network (asynchronously)
     * Return the traffic analysis data for this network. Traffic analysis with hostname visibility must be enabled on the network.
     * @param networkId  (required)
     * @param t0 The beginning of the timespan for the data. The maximum lookback period is 30 days from today. (optional)
     * @param timespan The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 30 days. (optional)
     * @param deviceType Filter the data by device type: &#39;combined&#39;, &#39;wireless&#39;, &#39;switch&#39; or &#39;appliance&#39;. Defaults to &#39;combined&#39;. When using &#39;combined&#39;, for each rule the data will come from the device type with the most usage. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNetworkTraffic_1Async(String networkId, String t0, Float timespan, String deviceType, final ApiCallback<List<Object>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getNetworkTraffic_1ValidateBeforeCall(networkId, t0, timespan, deviceType, _callback);
        Type localVarReturnType = new TypeToken<List<Object>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
