/*
 * Mailscript
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.4.0
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


import org.openapitools.client.model.AddAddressRequest;
import org.openapitools.client.model.ErrorResponse;
import org.openapitools.client.model.GetAllAddressesResponse;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class AddressesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public AddressesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public AddressesApi(ApiClient apiClient) {
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
     * Build call for addAddress
     * @param addAddressRequest Address body (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Internal error </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Bad credentials </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Invalid input </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addAddressCall(AddAddressRequest addAddressRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = addAddressRequest;

        // create path and map variables
        String localVarPath = "/addresses";

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

        String[] localVarAuthNames = new String[] { "bearerAuth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call addAddressValidateBeforeCall(AddAddressRequest addAddressRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'addAddressRequest' is set
        if (addAddressRequest == null) {
            throw new ApiException("Missing the required parameter 'addAddressRequest' when calling addAddress(Async)");
        }

        return addAddressCall(addAddressRequest, _callback);

    }

    /**
     * Claim a new Mailscript address
     * 
     * @param addAddressRequest Address body (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Internal error </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Bad credentials </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Invalid input </td><td>  -  </td></tr>
     </table>
     */
    public void addAddress(AddAddressRequest addAddressRequest) throws ApiException {
        addAddressWithHttpInfo(addAddressRequest);
    }

    /**
     * Claim a new Mailscript address
     * 
     * @param addAddressRequest Address body (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Internal error </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Bad credentials </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Invalid input </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> addAddressWithHttpInfo(AddAddressRequest addAddressRequest) throws ApiException {
        okhttp3.Call localVarCall = addAddressValidateBeforeCall(addAddressRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Claim a new Mailscript address (asynchronously)
     * 
     * @param addAddressRequest Address body (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Internal error </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Bad credentials </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Invalid input </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addAddressAsync(AddAddressRequest addAddressRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = addAddressValidateBeforeCall(addAddressRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteAddress
     * @param address ID of address (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful delete operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Bad credentials </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Invalid input </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteAddressCall(String address, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/addresses/{address}"
            .replace("{" + "address" + "}", localVarApiClient.escapeString(address.toString()));

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

        String[] localVarAuthNames = new String[] { "bearerAuth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteAddressValidateBeforeCall(String address, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'address' is set
        if (address == null) {
            throw new ApiException("Missing the required parameter 'address' when calling deleteAddress(Async)");
        }

        return deleteAddressCall(address, _callback);

    }

    /**
     * Delete a mailscript address
     * 
     * @param address ID of address (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful delete operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Bad credentials </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Invalid input </td><td>  -  </td></tr>
     </table>
     */
    public void deleteAddress(String address) throws ApiException {
        deleteAddressWithHttpInfo(address);
    }

    /**
     * Delete a mailscript address
     * 
     * @param address ID of address (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful delete operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Bad credentials </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Invalid input </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteAddressWithHttpInfo(String address) throws ApiException {
        okhttp3.Call localVarCall = deleteAddressValidateBeforeCall(address, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a mailscript address (asynchronously)
     * 
     * @param address ID of address (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful delete operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Bad credentials </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Invalid input </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteAddressAsync(String address, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteAddressValidateBeforeCall(address, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getAllAddresses
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Bad credentials </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Invalid input </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAllAddressesCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/addresses";

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

        String[] localVarAuthNames = new String[] { "bearerAuth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getAllAddressesValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return getAllAddressesCall(_callback);

    }

    /**
     * Get all addresses you have access to
     * 
     * @return GetAllAddressesResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Bad credentials </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Invalid input </td><td>  -  </td></tr>
     </table>
     */
    public GetAllAddressesResponse getAllAddresses() throws ApiException {
        ApiResponse<GetAllAddressesResponse> localVarResp = getAllAddressesWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Get all addresses you have access to
     * 
     * @return ApiResponse&lt;GetAllAddressesResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Bad credentials </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Invalid input </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetAllAddressesResponse> getAllAddressesWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getAllAddressesValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<GetAllAddressesResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get all addresses you have access to (asynchronously)
     * 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Bad credentials </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Invalid input </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAllAddressesAsync(final ApiCallback<GetAllAddressesResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getAllAddressesValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<GetAllAddressesResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
