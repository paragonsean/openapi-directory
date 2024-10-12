/*
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.0
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


import java.io.File;
import org.openapitools.client.model.ImagePrediction;
import org.openapitools.client.model.ImageUrl;
import org.openapitools.client.model.PredictionQueryResult;
import org.openapitools.client.model.PredictionQueryToken;
import java.util.UUID;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class PredictionsApiApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public PredictionsApiApi() {
        this(Configuration.getDefaultApiClient());
    }

    public PredictionsApiApi(ApiClient apiClient) {
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
     * Build call for deletePrediction
     * @param projectId The project id (required)
     * @param ids The prediction ids. Limited to 64 (required)
     * @param trainingKey  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deletePredictionCall(UUID projectId, List<String> ids, String trainingKey, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/projects/{projectId}/predictions"
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (ids != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("csv", "ids", ids));
        }

        if (trainingKey != null) {
            localVarHeaderParams.put("Training-Key", localVarApiClient.parameterToString(trainingKey));
        }

        final String[] localVarAccepts = {
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
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deletePredictionValidateBeforeCall(UUID projectId, List<String> ids, String trainingKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling deletePrediction(Async)");
        }

        // verify the required parameter 'ids' is set
        if (ids == null) {
            throw new ApiException("Missing the required parameter 'ids' when calling deletePrediction(Async)");
        }

        // verify the required parameter 'trainingKey' is set
        if (trainingKey == null) {
            throw new ApiException("Missing the required parameter 'trainingKey' when calling deletePrediction(Async)");
        }

        return deletePredictionCall(projectId, ids, trainingKey, _callback);

    }

    /**
     * Delete a set of predicted images and their associated prediction results
     * 
     * @param projectId The project id (required)
     * @param ids The prediction ids. Limited to 64 (required)
     * @param trainingKey  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public void deletePrediction(UUID projectId, List<String> ids, String trainingKey) throws ApiException {
        deletePredictionWithHttpInfo(projectId, ids, trainingKey);
    }

    /**
     * Delete a set of predicted images and their associated prediction results
     * 
     * @param projectId The project id (required)
     * @param ids The prediction ids. Limited to 64 (required)
     * @param trainingKey  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deletePredictionWithHttpInfo(UUID projectId, List<String> ids, String trainingKey) throws ApiException {
        okhttp3.Call localVarCall = deletePredictionValidateBeforeCall(projectId, ids, trainingKey, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a set of predicted images and their associated prediction results (asynchronously)
     * 
     * @param projectId The project id (required)
     * @param ids The prediction ids. Limited to 64 (required)
     * @param trainingKey  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deletePredictionAsync(UUID projectId, List<String> ids, String trainingKey, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deletePredictionValidateBeforeCall(projectId, ids, trainingKey, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for queryPredictions
     * @param projectId The project id (required)
     * @param trainingKey  (required)
     * @param predictionQueryToken Parameters used to query the predictions. Limited to combining 2 tags (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call queryPredictionsCall(UUID projectId, String trainingKey, PredictionQueryToken predictionQueryToken, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = predictionQueryToken;

        // create path and map variables
        String localVarPath = "/projects/{projectId}/predictions/query"
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()));

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
            "application/xml",
            "text/json",
            "text/xml"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json",
            "application/x-www-form-urlencoded",
            "application/xml",
            "text/json",
            "text/xml"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call queryPredictionsValidateBeforeCall(UUID projectId, String trainingKey, PredictionQueryToken predictionQueryToken, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling queryPredictions(Async)");
        }

        // verify the required parameter 'trainingKey' is set
        if (trainingKey == null) {
            throw new ApiException("Missing the required parameter 'trainingKey' when calling queryPredictions(Async)");
        }

        // verify the required parameter 'predictionQueryToken' is set
        if (predictionQueryToken == null) {
            throw new ApiException("Missing the required parameter 'predictionQueryToken' when calling queryPredictions(Async)");
        }

        return queryPredictionsCall(projectId, trainingKey, predictionQueryToken, _callback);

    }

    /**
     * Get images that were sent to your prediction endpoint
     * 
     * @param projectId The project id (required)
     * @param trainingKey  (required)
     * @param predictionQueryToken Parameters used to query the predictions. Limited to combining 2 tags (required)
     * @return PredictionQueryResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public PredictionQueryResult queryPredictions(UUID projectId, String trainingKey, PredictionQueryToken predictionQueryToken) throws ApiException {
        ApiResponse<PredictionQueryResult> localVarResp = queryPredictionsWithHttpInfo(projectId, trainingKey, predictionQueryToken);
        return localVarResp.getData();
    }

    /**
     * Get images that were sent to your prediction endpoint
     * 
     * @param projectId The project id (required)
     * @param trainingKey  (required)
     * @param predictionQueryToken Parameters used to query the predictions. Limited to combining 2 tags (required)
     * @return ApiResponse&lt;PredictionQueryResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PredictionQueryResult> queryPredictionsWithHttpInfo(UUID projectId, String trainingKey, PredictionQueryToken predictionQueryToken) throws ApiException {
        okhttp3.Call localVarCall = queryPredictionsValidateBeforeCall(projectId, trainingKey, predictionQueryToken, null);
        Type localVarReturnType = new TypeToken<PredictionQueryResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get images that were sent to your prediction endpoint (asynchronously)
     * 
     * @param projectId The project id (required)
     * @param trainingKey  (required)
     * @param predictionQueryToken Parameters used to query the predictions. Limited to combining 2 tags (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call queryPredictionsAsync(UUID projectId, String trainingKey, PredictionQueryToken predictionQueryToken, final ApiCallback<PredictionQueryResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = queryPredictionsValidateBeforeCall(projectId, trainingKey, predictionQueryToken, _callback);
        Type localVarReturnType = new TypeToken<PredictionQueryResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for quickTestImage
     * @param projectId The project id (required)
     * @param trainingKey  (required)
     * @param imageData  (required)
     * @param iterationId Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call quickTestImageCall(UUID projectId, String trainingKey, File imageData, UUID iterationId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/projects/{projectId}/quicktest/image"
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (imageData != null) {
            localVarFormParams.put("imageData", imageData);
        }

        if (iterationId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("iterationId", iterationId));
        }

        if (trainingKey != null) {
            localVarHeaderParams.put("Training-Key", localVarApiClient.parameterToString(trainingKey));
        }

        final String[] localVarAccepts = {
            "application/json",
            "application/xml",
            "text/json",
            "text/xml"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "multipart/form-data"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call quickTestImageValidateBeforeCall(UUID projectId, String trainingKey, File imageData, UUID iterationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling quickTestImage(Async)");
        }

        // verify the required parameter 'trainingKey' is set
        if (trainingKey == null) {
            throw new ApiException("Missing the required parameter 'trainingKey' when calling quickTestImage(Async)");
        }

        // verify the required parameter 'imageData' is set
        if (imageData == null) {
            throw new ApiException("Missing the required parameter 'imageData' when calling quickTestImage(Async)");
        }

        return quickTestImageCall(projectId, trainingKey, imageData, iterationId, _callback);

    }

    /**
     * Quick test an image
     * 
     * @param projectId The project id (required)
     * @param trainingKey  (required)
     * @param imageData  (required)
     * @param iterationId Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified. (optional)
     * @return ImagePrediction
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ImagePrediction quickTestImage(UUID projectId, String trainingKey, File imageData, UUID iterationId) throws ApiException {
        ApiResponse<ImagePrediction> localVarResp = quickTestImageWithHttpInfo(projectId, trainingKey, imageData, iterationId);
        return localVarResp.getData();
    }

    /**
     * Quick test an image
     * 
     * @param projectId The project id (required)
     * @param trainingKey  (required)
     * @param imageData  (required)
     * @param iterationId Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified. (optional)
     * @return ApiResponse&lt;ImagePrediction&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ImagePrediction> quickTestImageWithHttpInfo(UUID projectId, String trainingKey, File imageData, UUID iterationId) throws ApiException {
        okhttp3.Call localVarCall = quickTestImageValidateBeforeCall(projectId, trainingKey, imageData, iterationId, null);
        Type localVarReturnType = new TypeToken<ImagePrediction>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Quick test an image (asynchronously)
     * 
     * @param projectId The project id (required)
     * @param trainingKey  (required)
     * @param imageData  (required)
     * @param iterationId Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call quickTestImageAsync(UUID projectId, String trainingKey, File imageData, UUID iterationId, final ApiCallback<ImagePrediction> _callback) throws ApiException {

        okhttp3.Call localVarCall = quickTestImageValidateBeforeCall(projectId, trainingKey, imageData, iterationId, _callback);
        Type localVarReturnType = new TypeToken<ImagePrediction>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for quickTestImageUrl
     * @param projectId The project to evaluate against (required)
     * @param trainingKey  (required)
     * @param imageUrl An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated (required)
     * @param iterationId Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call quickTestImageUrlCall(UUID projectId, String trainingKey, ImageUrl imageUrl, UUID iterationId, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = imageUrl;

        // create path and map variables
        String localVarPath = "/projects/{projectId}/quicktest/url"
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (iterationId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("iterationId", iterationId));
        }

        if (trainingKey != null) {
            localVarHeaderParams.put("Training-Key", localVarApiClient.parameterToString(trainingKey));
        }

        final String[] localVarAccepts = {
            "application/json",
            "application/xml",
            "text/json",
            "text/xml"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json",
            "application/x-www-form-urlencoded",
            "application/xml",
            "text/json",
            "text/xml"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call quickTestImageUrlValidateBeforeCall(UUID projectId, String trainingKey, ImageUrl imageUrl, UUID iterationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling quickTestImageUrl(Async)");
        }

        // verify the required parameter 'trainingKey' is set
        if (trainingKey == null) {
            throw new ApiException("Missing the required parameter 'trainingKey' when calling quickTestImageUrl(Async)");
        }

        // verify the required parameter 'imageUrl' is set
        if (imageUrl == null) {
            throw new ApiException("Missing the required parameter 'imageUrl' when calling quickTestImageUrl(Async)");
        }

        return quickTestImageUrlCall(projectId, trainingKey, imageUrl, iterationId, _callback);

    }

    /**
     * Quick test an image url
     * 
     * @param projectId The project to evaluate against (required)
     * @param trainingKey  (required)
     * @param imageUrl An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated (required)
     * @param iterationId Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified. (optional)
     * @return ImagePrediction
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ImagePrediction quickTestImageUrl(UUID projectId, String trainingKey, ImageUrl imageUrl, UUID iterationId) throws ApiException {
        ApiResponse<ImagePrediction> localVarResp = quickTestImageUrlWithHttpInfo(projectId, trainingKey, imageUrl, iterationId);
        return localVarResp.getData();
    }

    /**
     * Quick test an image url
     * 
     * @param projectId The project to evaluate against (required)
     * @param trainingKey  (required)
     * @param imageUrl An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated (required)
     * @param iterationId Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified. (optional)
     * @return ApiResponse&lt;ImagePrediction&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ImagePrediction> quickTestImageUrlWithHttpInfo(UUID projectId, String trainingKey, ImageUrl imageUrl, UUID iterationId) throws ApiException {
        okhttp3.Call localVarCall = quickTestImageUrlValidateBeforeCall(projectId, trainingKey, imageUrl, iterationId, null);
        Type localVarReturnType = new TypeToken<ImagePrediction>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Quick test an image url (asynchronously)
     * 
     * @param projectId The project to evaluate against (required)
     * @param trainingKey  (required)
     * @param imageUrl An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated (required)
     * @param iterationId Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call quickTestImageUrlAsync(UUID projectId, String trainingKey, ImageUrl imageUrl, UUID iterationId, final ApiCallback<ImagePrediction> _callback) throws ApiException {

        okhttp3.Call localVarCall = quickTestImageUrlValidateBeforeCall(projectId, trainingKey, imageUrl, iterationId, _callback);
        Type localVarReturnType = new TypeToken<ImagePrediction>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
