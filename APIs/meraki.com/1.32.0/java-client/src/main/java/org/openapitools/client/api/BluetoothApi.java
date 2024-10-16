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


import org.openapitools.client.model.GetDeviceWirelessBluetoothSettings200Response;
import org.openapitools.client.model.GetNetworkWirelessBluetoothSettings200Response;
import org.openapitools.client.model.UpdateDeviceWirelessBluetoothSettingsRequest;
import org.openapitools.client.model.UpdateNetworkWirelessBluetoothSettingsRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BluetoothApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public BluetoothApi() {
        this(Configuration.getDefaultApiClient());
    }

    public BluetoothApi(ApiClient apiClient) {
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
     * Build call for getDeviceWirelessBluetoothSettings_1
     * @param serial  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDeviceWirelessBluetoothSettings_1Call(String serial, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/devices/{serial}/wireless/bluetooth/settings"
            .replace("{" + "serial" + "}", localVarApiClient.escapeString(serial.toString()));

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

        String[] localVarAuthNames = new String[] { "meraki_api_key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getDeviceWirelessBluetoothSettings_1ValidateBeforeCall(String serial, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'serial' is set
        if (serial == null) {
            throw new ApiException("Missing the required parameter 'serial' when calling getDeviceWirelessBluetoothSettings_1(Async)");
        }

        return getDeviceWirelessBluetoothSettings_1Call(serial, _callback);

    }

    /**
     * Return the bluetooth settings for a wireless device
     * Return the bluetooth settings for a wireless device
     * @param serial  (required)
     * @return GetDeviceWirelessBluetoothSettings200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public GetDeviceWirelessBluetoothSettings200Response getDeviceWirelessBluetoothSettings_1(String serial) throws ApiException {
        ApiResponse<GetDeviceWirelessBluetoothSettings200Response> localVarResp = getDeviceWirelessBluetoothSettings_1WithHttpInfo(serial);
        return localVarResp.getData();
    }

    /**
     * Return the bluetooth settings for a wireless device
     * Return the bluetooth settings for a wireless device
     * @param serial  (required)
     * @return ApiResponse&lt;GetDeviceWirelessBluetoothSettings200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetDeviceWirelessBluetoothSettings200Response> getDeviceWirelessBluetoothSettings_1WithHttpInfo(String serial) throws ApiException {
        okhttp3.Call localVarCall = getDeviceWirelessBluetoothSettings_1ValidateBeforeCall(serial, null);
        Type localVarReturnType = new TypeToken<GetDeviceWirelessBluetoothSettings200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Return the bluetooth settings for a wireless device (asynchronously)
     * Return the bluetooth settings for a wireless device
     * @param serial  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDeviceWirelessBluetoothSettings_1Async(String serial, final ApiCallback<GetDeviceWirelessBluetoothSettings200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDeviceWirelessBluetoothSettings_1ValidateBeforeCall(serial, _callback);
        Type localVarReturnType = new TypeToken<GetDeviceWirelessBluetoothSettings200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getNetworkWirelessBluetoothSettings_1
     * @param networkId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNetworkWirelessBluetoothSettings_1Call(String networkId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/networks/{networkId}/wireless/bluetooth/settings"
            .replace("{" + "networkId" + "}", localVarApiClient.escapeString(networkId.toString()));

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

        String[] localVarAuthNames = new String[] { "meraki_api_key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getNetworkWirelessBluetoothSettings_1ValidateBeforeCall(String networkId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling getNetworkWirelessBluetoothSettings_1(Async)");
        }

        return getNetworkWirelessBluetoothSettings_1Call(networkId, _callback);

    }

    /**
     * Return the Bluetooth settings for a network. &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt; must be enabled on the network.
     * Return the Bluetooth settings for a network. &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt; must be enabled on the network.
     * @param networkId  (required)
     * @return GetNetworkWirelessBluetoothSettings200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public GetNetworkWirelessBluetoothSettings200Response getNetworkWirelessBluetoothSettings_1(String networkId) throws ApiException {
        ApiResponse<GetNetworkWirelessBluetoothSettings200Response> localVarResp = getNetworkWirelessBluetoothSettings_1WithHttpInfo(networkId);
        return localVarResp.getData();
    }

    /**
     * Return the Bluetooth settings for a network. &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt; must be enabled on the network.
     * Return the Bluetooth settings for a network. &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt; must be enabled on the network.
     * @param networkId  (required)
     * @return ApiResponse&lt;GetNetworkWirelessBluetoothSettings200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetNetworkWirelessBluetoothSettings200Response> getNetworkWirelessBluetoothSettings_1WithHttpInfo(String networkId) throws ApiException {
        okhttp3.Call localVarCall = getNetworkWirelessBluetoothSettings_1ValidateBeforeCall(networkId, null);
        Type localVarReturnType = new TypeToken<GetNetworkWirelessBluetoothSettings200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Return the Bluetooth settings for a network. &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt; must be enabled on the network. (asynchronously)
     * Return the Bluetooth settings for a network. &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt; must be enabled on the network.
     * @param networkId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNetworkWirelessBluetoothSettings_1Async(String networkId, final ApiCallback<GetNetworkWirelessBluetoothSettings200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getNetworkWirelessBluetoothSettings_1ValidateBeforeCall(networkId, _callback);
        Type localVarReturnType = new TypeToken<GetNetworkWirelessBluetoothSettings200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateDeviceWirelessBluetoothSettings_1
     * @param serial  (required)
     * @param updateDeviceWirelessBluetoothSettingsRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateDeviceWirelessBluetoothSettings_1Call(String serial, UpdateDeviceWirelessBluetoothSettingsRequest updateDeviceWirelessBluetoothSettingsRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateDeviceWirelessBluetoothSettingsRequest;

        // create path and map variables
        String localVarPath = "/devices/{serial}/wireless/bluetooth/settings"
            .replace("{" + "serial" + "}", localVarApiClient.escapeString(serial.toString()));

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
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "meraki_api_key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updateDeviceWirelessBluetoothSettings_1ValidateBeforeCall(String serial, UpdateDeviceWirelessBluetoothSettingsRequest updateDeviceWirelessBluetoothSettingsRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'serial' is set
        if (serial == null) {
            throw new ApiException("Missing the required parameter 'serial' when calling updateDeviceWirelessBluetoothSettings_1(Async)");
        }

        return updateDeviceWirelessBluetoothSettings_1Call(serial, updateDeviceWirelessBluetoothSettingsRequest, _callback);

    }

    /**
     * Update the bluetooth settings for a wireless device
     * Update the bluetooth settings for a wireless device
     * @param serial  (required)
     * @param updateDeviceWirelessBluetoothSettingsRequest  (optional)
     * @return GetDeviceWirelessBluetoothSettings200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public GetDeviceWirelessBluetoothSettings200Response updateDeviceWirelessBluetoothSettings_1(String serial, UpdateDeviceWirelessBluetoothSettingsRequest updateDeviceWirelessBluetoothSettingsRequest) throws ApiException {
        ApiResponse<GetDeviceWirelessBluetoothSettings200Response> localVarResp = updateDeviceWirelessBluetoothSettings_1WithHttpInfo(serial, updateDeviceWirelessBluetoothSettingsRequest);
        return localVarResp.getData();
    }

    /**
     * Update the bluetooth settings for a wireless device
     * Update the bluetooth settings for a wireless device
     * @param serial  (required)
     * @param updateDeviceWirelessBluetoothSettingsRequest  (optional)
     * @return ApiResponse&lt;GetDeviceWirelessBluetoothSettings200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetDeviceWirelessBluetoothSettings200Response> updateDeviceWirelessBluetoothSettings_1WithHttpInfo(String serial, UpdateDeviceWirelessBluetoothSettingsRequest updateDeviceWirelessBluetoothSettingsRequest) throws ApiException {
        okhttp3.Call localVarCall = updateDeviceWirelessBluetoothSettings_1ValidateBeforeCall(serial, updateDeviceWirelessBluetoothSettingsRequest, null);
        Type localVarReturnType = new TypeToken<GetDeviceWirelessBluetoothSettings200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update the bluetooth settings for a wireless device (asynchronously)
     * Update the bluetooth settings for a wireless device
     * @param serial  (required)
     * @param updateDeviceWirelessBluetoothSettingsRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateDeviceWirelessBluetoothSettings_1Async(String serial, UpdateDeviceWirelessBluetoothSettingsRequest updateDeviceWirelessBluetoothSettingsRequest, final ApiCallback<GetDeviceWirelessBluetoothSettings200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateDeviceWirelessBluetoothSettings_1ValidateBeforeCall(serial, updateDeviceWirelessBluetoothSettingsRequest, _callback);
        Type localVarReturnType = new TypeToken<GetDeviceWirelessBluetoothSettings200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateNetworkWirelessBluetoothSettings_1
     * @param networkId  (required)
     * @param updateNetworkWirelessBluetoothSettingsRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateNetworkWirelessBluetoothSettings_1Call(String networkId, UpdateNetworkWirelessBluetoothSettingsRequest updateNetworkWirelessBluetoothSettingsRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateNetworkWirelessBluetoothSettingsRequest;

        // create path and map variables
        String localVarPath = "/networks/{networkId}/wireless/bluetooth/settings"
            .replace("{" + "networkId" + "}", localVarApiClient.escapeString(networkId.toString()));

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
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "meraki_api_key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updateNetworkWirelessBluetoothSettings_1ValidateBeforeCall(String networkId, UpdateNetworkWirelessBluetoothSettingsRequest updateNetworkWirelessBluetoothSettingsRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling updateNetworkWirelessBluetoothSettings_1(Async)");
        }

        return updateNetworkWirelessBluetoothSettings_1Call(networkId, updateNetworkWirelessBluetoothSettingsRequest, _callback);

    }

    /**
     * Update the Bluetooth settings for a network
     * Update the Bluetooth settings for a network. See the docs page for &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt;.
     * @param networkId  (required)
     * @param updateNetworkWirelessBluetoothSettingsRequest  (optional)
     * @return GetNetworkWirelessBluetoothSettings200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public GetNetworkWirelessBluetoothSettings200Response updateNetworkWirelessBluetoothSettings_1(String networkId, UpdateNetworkWirelessBluetoothSettingsRequest updateNetworkWirelessBluetoothSettingsRequest) throws ApiException {
        ApiResponse<GetNetworkWirelessBluetoothSettings200Response> localVarResp = updateNetworkWirelessBluetoothSettings_1WithHttpInfo(networkId, updateNetworkWirelessBluetoothSettingsRequest);
        return localVarResp.getData();
    }

    /**
     * Update the Bluetooth settings for a network
     * Update the Bluetooth settings for a network. See the docs page for &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt;.
     * @param networkId  (required)
     * @param updateNetworkWirelessBluetoothSettingsRequest  (optional)
     * @return ApiResponse&lt;GetNetworkWirelessBluetoothSettings200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetNetworkWirelessBluetoothSettings200Response> updateNetworkWirelessBluetoothSettings_1WithHttpInfo(String networkId, UpdateNetworkWirelessBluetoothSettingsRequest updateNetworkWirelessBluetoothSettingsRequest) throws ApiException {
        okhttp3.Call localVarCall = updateNetworkWirelessBluetoothSettings_1ValidateBeforeCall(networkId, updateNetworkWirelessBluetoothSettingsRequest, null);
        Type localVarReturnType = new TypeToken<GetNetworkWirelessBluetoothSettings200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update the Bluetooth settings for a network (asynchronously)
     * Update the Bluetooth settings for a network. See the docs page for &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt;.
     * @param networkId  (required)
     * @param updateNetworkWirelessBluetoothSettingsRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateNetworkWirelessBluetoothSettings_1Async(String networkId, UpdateNetworkWirelessBluetoothSettingsRequest updateNetworkWirelessBluetoothSettingsRequest, final ApiCallback<GetNetworkWirelessBluetoothSettings200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateNetworkWirelessBluetoothSettings_1ValidateBeforeCall(networkId, updateNetworkWirelessBluetoothSettingsRequest, _callback);
        Type localVarReturnType = new TypeToken<GetNetworkWirelessBluetoothSettings200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
