/*
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
 *
 * The version of the OpenAPI document: v1
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


import org.openapitools.client.model.AssetsFundingGoalModel;
import org.openapitools.client.model.NeedsVsAbilitiesModel;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ProjectedGoalsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ProjectedGoalsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ProjectedGoalsApi(ApiClient apiClient) {
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
     * Build call for projectedGoalsGetAssetsFundingGoalsByPlanid
     * @param planId Id of the plan to retrieve data from (e.g. 1001-11-3). (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 202 </td><td> Plan migration is processing </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Invalid request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized for plan data access </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectedGoalsGetAssetsFundingGoalsByPlanidCall(String planId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/ProjectedGoals/AssetsFundingGoals";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (planId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("planId", planId));
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
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call projectedGoalsGetAssetsFundingGoalsByPlanidValidateBeforeCall(String planId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'planId' is set
        if (planId == null) {
            throw new ApiException("Missing the required parameter 'planId' when calling projectedGoalsGetAssetsFundingGoalsByPlanid(Async)");
        }

        return projectedGoalsGetAssetsFundingGoalsByPlanidCall(planId, _callback);

    }

    /**
     * Retrieve assets funding goals over time
     * This operation retrieves the assets funding each goal throughout the plan years
     * @param planId Id of the plan to retrieve data from (e.g. 1001-11-3). (required)
     * @return AssetsFundingGoalModel
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 202 </td><td> Plan migration is processing </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Invalid request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized for plan data access </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public AssetsFundingGoalModel projectedGoalsGetAssetsFundingGoalsByPlanid(String planId) throws ApiException {
        ApiResponse<AssetsFundingGoalModel> localVarResp = projectedGoalsGetAssetsFundingGoalsByPlanidWithHttpInfo(planId);
        return localVarResp.getData();
    }

    /**
     * Retrieve assets funding goals over time
     * This operation retrieves the assets funding each goal throughout the plan years
     * @param planId Id of the plan to retrieve data from (e.g. 1001-11-3). (required)
     * @return ApiResponse&lt;AssetsFundingGoalModel&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 202 </td><td> Plan migration is processing </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Invalid request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized for plan data access </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<AssetsFundingGoalModel> projectedGoalsGetAssetsFundingGoalsByPlanidWithHttpInfo(String planId) throws ApiException {
        okhttp3.Call localVarCall = projectedGoalsGetAssetsFundingGoalsByPlanidValidateBeforeCall(planId, null);
        Type localVarReturnType = new TypeToken<AssetsFundingGoalModel>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve assets funding goals over time (asynchronously)
     * This operation retrieves the assets funding each goal throughout the plan years
     * @param planId Id of the plan to retrieve data from (e.g. 1001-11-3). (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 202 </td><td> Plan migration is processing </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Invalid request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized for plan data access </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectedGoalsGetAssetsFundingGoalsByPlanidAsync(String planId, final ApiCallback<AssetsFundingGoalModel> _callback) throws ApiException {

        okhttp3.Call localVarCall = projectedGoalsGetAssetsFundingGoalsByPlanidValidateBeforeCall(planId, _callback);
        Type localVarReturnType = new TypeToken<AssetsFundingGoalModel>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for projectedGoalsGetNeedsVsAbilitiesByPlanid
     * @param planId Id of the plan to retrieve data from (e.g. 1001-11-3). (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 202 </td><td> Plan migration is processing </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Invalid request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized for plan data access </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectedGoalsGetNeedsVsAbilitiesByPlanidCall(String planId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/ProjectedGoals/NeedsVsAbilities";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (planId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("planId", planId));
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
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call projectedGoalsGetNeedsVsAbilitiesByPlanidValidateBeforeCall(String planId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'planId' is set
        if (planId == null) {
            throw new ApiException("Missing the required parameter 'planId' when calling projectedGoalsGetNeedsVsAbilitiesByPlanid(Async)");
        }

        return projectedGoalsGetNeedsVsAbilitiesByPlanidCall(planId, _callback);

    }

    /**
     * Retrieve needs vs abilities data
     * This operation retrieves a needs and abilities data for all goals throughout                the plan years.
     * @param planId Id of the plan to retrieve data from (e.g. 1001-11-3). (required)
     * @return NeedsVsAbilitiesModel
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 202 </td><td> Plan migration is processing </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Invalid request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized for plan data access </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public NeedsVsAbilitiesModel projectedGoalsGetNeedsVsAbilitiesByPlanid(String planId) throws ApiException {
        ApiResponse<NeedsVsAbilitiesModel> localVarResp = projectedGoalsGetNeedsVsAbilitiesByPlanidWithHttpInfo(planId);
        return localVarResp.getData();
    }

    /**
     * Retrieve needs vs abilities data
     * This operation retrieves a needs and abilities data for all goals throughout                the plan years.
     * @param planId Id of the plan to retrieve data from (e.g. 1001-11-3). (required)
     * @return ApiResponse&lt;NeedsVsAbilitiesModel&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 202 </td><td> Plan migration is processing </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Invalid request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized for plan data access </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<NeedsVsAbilitiesModel> projectedGoalsGetNeedsVsAbilitiesByPlanidWithHttpInfo(String planId) throws ApiException {
        okhttp3.Call localVarCall = projectedGoalsGetNeedsVsAbilitiesByPlanidValidateBeforeCall(planId, null);
        Type localVarReturnType = new TypeToken<NeedsVsAbilitiesModel>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve needs vs abilities data (asynchronously)
     * This operation retrieves a needs and abilities data for all goals throughout                the plan years.
     * @param planId Id of the plan to retrieve data from (e.g. 1001-11-3). (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 202 </td><td> Plan migration is processing </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Invalid request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized for plan data access </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectedGoalsGetNeedsVsAbilitiesByPlanidAsync(String planId, final ApiCallback<NeedsVsAbilitiesModel> _callback) throws ApiException {

        okhttp3.Call localVarCall = projectedGoalsGetNeedsVsAbilitiesByPlanidValidateBeforeCall(planId, _callback);
        Type localVarReturnType = new TypeToken<NeedsVsAbilitiesModel>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
