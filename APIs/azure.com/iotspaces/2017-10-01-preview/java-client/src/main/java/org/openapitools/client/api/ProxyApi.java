/*
 * IoTSpacesClient
 * Use this API to manage the IoTSpaces service instances in your Azure subscription.
 *
 * The version of the OpenAPI document: 2017-10-01-preview
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


import org.openapitools.client.model.ErrorDetails;
import org.openapitools.client.model.IoTSpacesNameAvailabilityInfo;
import org.openapitools.client.model.OperationInputs;
import org.openapitools.client.model.OperationListResult;
import java.util.UUID;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ProxyApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ProxyApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ProxyApi(ApiClient apiClient) {
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
     * Build call for ioTSpacesCheckNameAvailability
     * @param apiVersion The version of the API. (required)
     * @param subscriptionId The subscription identifier. (required)
     * @param operationInputs Set the name parameter in the OperationInputs structure to the name of the IoTSpaces instance to check. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> This is a synchronous operation. The body contains a JSON-serialized response that specifies whether the IoTSpaces service name is available. If the name is not available, the body contains the reason. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> DefaultErrorResponse </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call ioTSpacesCheckNameAvailabilityCall(String apiVersion, UUID subscriptionId, OperationInputs operationInputs, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = operationInputs;

        // create path and map variables
        String localVarPath = "/subscriptions/{subscriptionId}/providers/Microsoft.IoTSpaces/checkNameAvailability"
            .replace("{" + "subscriptionId" + "}", localVarApiClient.escapeString(subscriptionId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (apiVersion != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("api-version", apiVersion));
        }

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

        String[] localVarAuthNames = new String[] { "azure_auth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call ioTSpacesCheckNameAvailabilityValidateBeforeCall(String apiVersion, UUID subscriptionId, OperationInputs operationInputs, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling ioTSpacesCheckNameAvailability(Async)");
        }

        // verify the required parameter 'subscriptionId' is set
        if (subscriptionId == null) {
            throw new ApiException("Missing the required parameter 'subscriptionId' when calling ioTSpacesCheckNameAvailability(Async)");
        }

        // verify the required parameter 'operationInputs' is set
        if (operationInputs == null) {
            throw new ApiException("Missing the required parameter 'operationInputs' when calling ioTSpacesCheckNameAvailability(Async)");
        }

        return ioTSpacesCheckNameAvailabilityCall(apiVersion, subscriptionId, operationInputs, _callback);

    }

    /**
     * 
     * Check if an IoTSpaces instance name is available.
     * @param apiVersion The version of the API. (required)
     * @param subscriptionId The subscription identifier. (required)
     * @param operationInputs Set the name parameter in the OperationInputs structure to the name of the IoTSpaces instance to check. (required)
     * @return IoTSpacesNameAvailabilityInfo
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> This is a synchronous operation. The body contains a JSON-serialized response that specifies whether the IoTSpaces service name is available. If the name is not available, the body contains the reason. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> DefaultErrorResponse </td><td>  -  </td></tr>
     </table>
     */
    public IoTSpacesNameAvailabilityInfo ioTSpacesCheckNameAvailability(String apiVersion, UUID subscriptionId, OperationInputs operationInputs) throws ApiException {
        ApiResponse<IoTSpacesNameAvailabilityInfo> localVarResp = ioTSpacesCheckNameAvailabilityWithHttpInfo(apiVersion, subscriptionId, operationInputs);
        return localVarResp.getData();
    }

    /**
     * 
     * Check if an IoTSpaces instance name is available.
     * @param apiVersion The version of the API. (required)
     * @param subscriptionId The subscription identifier. (required)
     * @param operationInputs Set the name parameter in the OperationInputs structure to the name of the IoTSpaces instance to check. (required)
     * @return ApiResponse&lt;IoTSpacesNameAvailabilityInfo&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> This is a synchronous operation. The body contains a JSON-serialized response that specifies whether the IoTSpaces service name is available. If the name is not available, the body contains the reason. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> DefaultErrorResponse </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<IoTSpacesNameAvailabilityInfo> ioTSpacesCheckNameAvailabilityWithHttpInfo(String apiVersion, UUID subscriptionId, OperationInputs operationInputs) throws ApiException {
        okhttp3.Call localVarCall = ioTSpacesCheckNameAvailabilityValidateBeforeCall(apiVersion, subscriptionId, operationInputs, null);
        Type localVarReturnType = new TypeToken<IoTSpacesNameAvailabilityInfo>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Check if an IoTSpaces instance name is available.
     * @param apiVersion The version of the API. (required)
     * @param subscriptionId The subscription identifier. (required)
     * @param operationInputs Set the name parameter in the OperationInputs structure to the name of the IoTSpaces instance to check. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> This is a synchronous operation. The body contains a JSON-serialized response that specifies whether the IoTSpaces service name is available. If the name is not available, the body contains the reason. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> DefaultErrorResponse </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call ioTSpacesCheckNameAvailabilityAsync(String apiVersion, UUID subscriptionId, OperationInputs operationInputs, final ApiCallback<IoTSpacesNameAvailabilityInfo> _callback) throws ApiException {

        okhttp3.Call localVarCall = ioTSpacesCheckNameAvailabilityValidateBeforeCall(apiVersion, subscriptionId, operationInputs, _callback);
        Type localVarReturnType = new TypeToken<IoTSpacesNameAvailabilityInfo>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for operationsList
     * @param apiVersion The version of the API. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK. The request has succeeded. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> DefaultErrorResponse </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call operationsListCall(String apiVersion, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/providers/Microsoft.IoTSpaces/operations";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (apiVersion != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("api-version", apiVersion));
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

        String[] localVarAuthNames = new String[] { "azure_auth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call operationsListValidateBeforeCall(String apiVersion, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling operationsList(Async)");
        }

        return operationsListCall(apiVersion, _callback);

    }

    /**
     * 
     * Lists all of the available IoTSpaces service REST API operations.
     * @param apiVersion The version of the API. (required)
     * @return OperationListResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK. The request has succeeded. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> DefaultErrorResponse </td><td>  -  </td></tr>
     </table>
     */
    public OperationListResult operationsList(String apiVersion) throws ApiException {
        ApiResponse<OperationListResult> localVarResp = operationsListWithHttpInfo(apiVersion);
        return localVarResp.getData();
    }

    /**
     * 
     * Lists all of the available IoTSpaces service REST API operations.
     * @param apiVersion The version of the API. (required)
     * @return ApiResponse&lt;OperationListResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK. The request has succeeded. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> DefaultErrorResponse </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<OperationListResult> operationsListWithHttpInfo(String apiVersion) throws ApiException {
        okhttp3.Call localVarCall = operationsListValidateBeforeCall(apiVersion, null);
        Type localVarReturnType = new TypeToken<OperationListResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Lists all of the available IoTSpaces service REST API operations.
     * @param apiVersion The version of the API. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK. The request has succeeded. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> DefaultErrorResponse </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call operationsListAsync(String apiVersion, final ApiCallback<OperationListResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = operationsListValidateBeforeCall(apiVersion, _callback);
        Type localVarReturnType = new TypeToken<OperationListResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
