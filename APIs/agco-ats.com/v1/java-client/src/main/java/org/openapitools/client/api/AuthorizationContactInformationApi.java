/*
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
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


import org.openapitools.client.model.APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation;
import org.openapitools.client.model.APIModelsApiError;
import org.openapitools.client.model.AuthorizationCodesSharedModelsAuthorizationContactInformation;
import java.time.OffsetDateTime;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class AuthorizationContactInformationApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public AuthorizationContactInformationApi() {
        this(Configuration.getDefaultApiClient());
    }

    public AuthorizationContactInformationApi(ApiClient apiClient) {
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
     * Build call for authorizationContactInformationGet
     * @param limit Optional. The page limit.  If not specified, the default page limit is 10. (optional)
     * @param offset Optional. The page offset.  If not specified, the default page offset is 0. (optional)
     * @param authorizationCode Optional. Search by authorization code. (optional)
     * @param afterDate Optional. Include only data for authorization codes created after a provided date. (optional)
     * @param beforeDate Optional. Include only data for authorization codes created before a provided date. (optional)
     * @param dealerCode Optional. Search by dealer code. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call authorizationContactInformationGetCall(Integer limit, Integer offset, String authorizationCode, OffsetDateTime afterDate, OffsetDateTime beforeDate, String dealerCode, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v2/AuthorizationContactInformation";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (limit != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("limit", limit));
        }

        if (offset != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("offset", offset));
        }

        if (authorizationCode != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("authorizationCode", authorizationCode));
        }

        if (afterDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("afterDate", afterDate));
        }

        if (beforeDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("beforeDate", beforeDate));
        }

        if (dealerCode != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("dealerCode", dealerCode));
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
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call authorizationContactInformationGetValidateBeforeCall(Integer limit, Integer offset, String authorizationCode, OffsetDateTime afterDate, OffsetDateTime beforeDate, String dealerCode, final ApiCallback _callback) throws ApiException {
        return authorizationContactInformationGetCall(limit, offset, authorizationCode, afterDate, beforeDate, dealerCode, _callback);

    }

    /**
     * Get contact information for authorization codes.
     * No Documentation Found.
     * @param limit Optional. The page limit.  If not specified, the default page limit is 10. (optional)
     * @param offset Optional. The page offset.  If not specified, the default page offset is 0. (optional)
     * @param authorizationCode Optional. Search by authorization code. (optional)
     * @param afterDate Optional. Include only data for authorization codes created after a provided date. (optional)
     * @param beforeDate Optional. Include only data for authorization codes created before a provided date. (optional)
     * @param dealerCode Optional. Search by dealer code. (optional)
     * @return APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation authorizationContactInformationGet(Integer limit, Integer offset, String authorizationCode, OffsetDateTime afterDate, OffsetDateTime beforeDate, String dealerCode) throws ApiException {
        ApiResponse<APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation> localVarResp = authorizationContactInformationGetWithHttpInfo(limit, offset, authorizationCode, afterDate, beforeDate, dealerCode);
        return localVarResp.getData();
    }

    /**
     * Get contact information for authorization codes.
     * No Documentation Found.
     * @param limit Optional. The page limit.  If not specified, the default page limit is 10. (optional)
     * @param offset Optional. The page offset.  If not specified, the default page offset is 0. (optional)
     * @param authorizationCode Optional. Search by authorization code. (optional)
     * @param afterDate Optional. Include only data for authorization codes created after a provided date. (optional)
     * @param beforeDate Optional. Include only data for authorization codes created before a provided date. (optional)
     * @param dealerCode Optional. Search by dealer code. (optional)
     * @return ApiResponse&lt;APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation> authorizationContactInformationGetWithHttpInfo(Integer limit, Integer offset, String authorizationCode, OffsetDateTime afterDate, OffsetDateTime beforeDate, String dealerCode) throws ApiException {
        okhttp3.Call localVarCall = authorizationContactInformationGetValidateBeforeCall(limit, offset, authorizationCode, afterDate, beforeDate, dealerCode, null);
        Type localVarReturnType = new TypeToken<APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get contact information for authorization codes. (asynchronously)
     * No Documentation Found.
     * @param limit Optional. The page limit.  If not specified, the default page limit is 10. (optional)
     * @param offset Optional. The page offset.  If not specified, the default page offset is 0. (optional)
     * @param authorizationCode Optional. Search by authorization code. (optional)
     * @param afterDate Optional. Include only data for authorization codes created after a provided date. (optional)
     * @param beforeDate Optional. Include only data for authorization codes created before a provided date. (optional)
     * @param dealerCode Optional. Search by dealer code. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call authorizationContactInformationGetAsync(Integer limit, Integer offset, String authorizationCode, OffsetDateTime afterDate, OffsetDateTime beforeDate, String dealerCode, final ApiCallback<APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation> _callback) throws ApiException {

        okhttp3.Call localVarCall = authorizationContactInformationGetValidateBeforeCall(limit, offset, authorizationCode, afterDate, beforeDate, dealerCode, _callback);
        Type localVarReturnType = new TypeToken<APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for authorizationContactInformationPost
     * @param authorizationCodesSharedModelsAuthorizationContactInformation A contact information. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call authorizationContactInformationPostCall(AuthorizationCodesSharedModelsAuthorizationContactInformation authorizationCodesSharedModelsAuthorizationContactInformation, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = authorizationCodesSharedModelsAuthorizationContactInformation;

        // create path and map variables
        String localVarPath = "/api/v2/AuthorizationContactInformation";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

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
    private okhttp3.Call authorizationContactInformationPostValidateBeforeCall(AuthorizationCodesSharedModelsAuthorizationContactInformation authorizationCodesSharedModelsAuthorizationContactInformation, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'authorizationCodesSharedModelsAuthorizationContactInformation' is set
        if (authorizationCodesSharedModelsAuthorizationContactInformation == null) {
            throw new ApiException("Missing the required parameter 'authorizationCodesSharedModelsAuthorizationContactInformation' when calling authorizationContactInformationPost(Async)");
        }

        return authorizationContactInformationPostCall(authorizationCodesSharedModelsAuthorizationContactInformation, _callback);

    }

    /**
     * Add contact information for authorization code.
     * No Documentation Found.
     * @param authorizationCodesSharedModelsAuthorizationContactInformation A contact information. (required)
     * @return Integer
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public Integer authorizationContactInformationPost(AuthorizationCodesSharedModelsAuthorizationContactInformation authorizationCodesSharedModelsAuthorizationContactInformation) throws ApiException {
        ApiResponse<Integer> localVarResp = authorizationContactInformationPostWithHttpInfo(authorizationCodesSharedModelsAuthorizationContactInformation);
        return localVarResp.getData();
    }

    /**
     * Add contact information for authorization code.
     * No Documentation Found.
     * @param authorizationCodesSharedModelsAuthorizationContactInformation A contact information. (required)
     * @return ApiResponse&lt;Integer&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Integer> authorizationContactInformationPostWithHttpInfo(AuthorizationCodesSharedModelsAuthorizationContactInformation authorizationCodesSharedModelsAuthorizationContactInformation) throws ApiException {
        okhttp3.Call localVarCall = authorizationContactInformationPostValidateBeforeCall(authorizationCodesSharedModelsAuthorizationContactInformation, null);
        Type localVarReturnType = new TypeToken<Integer>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add contact information for authorization code. (asynchronously)
     * No Documentation Found.
     * @param authorizationCodesSharedModelsAuthorizationContactInformation A contact information. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call authorizationContactInformationPostAsync(AuthorizationCodesSharedModelsAuthorizationContactInformation authorizationCodesSharedModelsAuthorizationContactInformation, final ApiCallback<Integer> _callback) throws ApiException {

        okhttp3.Call localVarCall = authorizationContactInformationPostValidateBeforeCall(authorizationCodesSharedModelsAuthorizationContactInformation, _callback);
        Type localVarReturnType = new TypeToken<Integer>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
