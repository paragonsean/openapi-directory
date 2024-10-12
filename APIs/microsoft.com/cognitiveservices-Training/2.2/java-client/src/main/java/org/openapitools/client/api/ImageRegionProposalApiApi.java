/*
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.2
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


import org.openapitools.client.model.ImageRegionProposal;
import java.util.UUID;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ImageRegionProposalApiApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ImageRegionProposalApiApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ImageRegionProposalApiApi(ApiClient apiClient) {
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
     * Build call for getImageRegionProposals
     * @param projectId The project id. (required)
     * @param imageId The image id. (required)
     * @param trainingKey  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getImageRegionProposalsCall(UUID projectId, UUID imageId, String trainingKey, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/{projectId}/images/{imageId}/regionproposals"
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()))
            .replace("{" + "imageId" + "}", localVarApiClient.escapeString(imageId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (trainingKey != null) {
            localVarHeaderParams.put("Training-Key", localVarApiClient.parameterToString(trainingKey));
        }

        final String[] localVarAccepts = {
            "application/json",
            "text/json"
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getImageRegionProposalsValidateBeforeCall(UUID projectId, UUID imageId, String trainingKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling getImageRegionProposals(Async)");
        }

        // verify the required parameter 'imageId' is set
        if (imageId == null) {
            throw new ApiException("Missing the required parameter 'imageId' when calling getImageRegionProposals(Async)");
        }

        // verify the required parameter 'trainingKey' is set
        if (trainingKey == null) {
            throw new ApiException("Missing the required parameter 'trainingKey' when calling getImageRegionProposals(Async)");
        }

        return getImageRegionProposalsCall(projectId, imageId, trainingKey, _callback);

    }

    /**
     * Get region proposals for an image. Returns empty array if no proposals are found.
     * This API will get region proposals for an image along with confidences for the region. It returns an empty array if no proposals are found.
     * @param projectId The project id. (required)
     * @param imageId The image id. (required)
     * @param trainingKey  (required)
     * @return ImageRegionProposal
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ImageRegionProposal getImageRegionProposals(UUID projectId, UUID imageId, String trainingKey) throws ApiException {
        ApiResponse<ImageRegionProposal> localVarResp = getImageRegionProposalsWithHttpInfo(projectId, imageId, trainingKey);
        return localVarResp.getData();
    }

    /**
     * Get region proposals for an image. Returns empty array if no proposals are found.
     * This API will get region proposals for an image along with confidences for the region. It returns an empty array if no proposals are found.
     * @param projectId The project id. (required)
     * @param imageId The image id. (required)
     * @param trainingKey  (required)
     * @return ApiResponse&lt;ImageRegionProposal&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ImageRegionProposal> getImageRegionProposalsWithHttpInfo(UUID projectId, UUID imageId, String trainingKey) throws ApiException {
        okhttp3.Call localVarCall = getImageRegionProposalsValidateBeforeCall(projectId, imageId, trainingKey, null);
        Type localVarReturnType = new TypeToken<ImageRegionProposal>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get region proposals for an image. Returns empty array if no proposals are found. (asynchronously)
     * This API will get region proposals for an image along with confidences for the region. It returns an empty array if no proposals are found.
     * @param projectId The project id. (required)
     * @param imageId The image id. (required)
     * @param trainingKey  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getImageRegionProposalsAsync(UUID projectId, UUID imageId, String trainingKey, final ApiCallback<ImageRegionProposal> _callback) throws ApiException {

        okhttp3.Call localVarCall = getImageRegionProposalsValidateBeforeCall(projectId, imageId, trainingKey, _callback);
        Type localVarReturnType = new TypeToken<ImageRegionProposal>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
