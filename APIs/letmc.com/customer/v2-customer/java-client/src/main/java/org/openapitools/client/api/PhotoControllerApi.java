/*
 * agentOS Api V2, Customer Login Call Group
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-customer
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

public class PhotoControllerApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public PhotoControllerApi() {
        this(Configuration.getDefaultApiClient());
    }

    public PhotoControllerApi(ApiClient apiClient) {
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
     * Build call for photoControllerGetPhotoDownload
     * @param shortName The unique client short-name (required)
     * @param token The login token returned from the /session POST call (required)
     * @param photoID The unique ID of the photo on the property (required)
     * @param width An optional parameter specifying the image width (optional)
     * @param height An optional parameter specifying the image height (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call photoControllerGetPhotoDownloadCall(String shortName, String token, String photoID, Integer width, Integer height, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v2/customer/{shortName}/photo/download"
            .replace("{" + "shortName" + "}", localVarApiClient.escapeString(shortName.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (token != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("token", token));
        }

        if (photoID != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("photoID", photoID));
        }

        if (width != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("width", width));
        }

        if (height != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("height", height));
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
    private okhttp3.Call photoControllerGetPhotoDownloadValidateBeforeCall(String shortName, String token, String photoID, Integer width, Integer height, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'shortName' is set
        if (shortName == null) {
            throw new ApiException("Missing the required parameter 'shortName' when calling photoControllerGetPhotoDownload(Async)");
        }

        // verify the required parameter 'token' is set
        if (token == null) {
            throw new ApiException("Missing the required parameter 'token' when calling photoControllerGetPhotoDownload(Async)");
        }

        // verify the required parameter 'photoID' is set
        if (photoID == null) {
            throw new ApiException("Missing the required parameter 'photoID' when calling photoControllerGetPhotoDownload(Async)");
        }

        return photoControllerGetPhotoDownloadCall(shortName, token, photoID, width, height, _callback);

    }

    /**
     * Downloads the photo of a property given the photo ID.
     * 
     * @param shortName The unique client short-name (required)
     * @param token The login token returned from the /session POST call (required)
     * @param photoID The unique ID of the photo on the property (required)
     * @param width An optional parameter specifying the image width (optional)
     * @param height An optional parameter specifying the image height (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Object photoControllerGetPhotoDownload(String shortName, String token, String photoID, Integer width, Integer height) throws ApiException {
        ApiResponse<Object> localVarResp = photoControllerGetPhotoDownloadWithHttpInfo(shortName, token, photoID, width, height);
        return localVarResp.getData();
    }

    /**
     * Downloads the photo of a property given the photo ID.
     * 
     * @param shortName The unique client short-name (required)
     * @param token The login token returned from the /session POST call (required)
     * @param photoID The unique ID of the photo on the property (required)
     * @param width An optional parameter specifying the image width (optional)
     * @param height An optional parameter specifying the image height (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> photoControllerGetPhotoDownloadWithHttpInfo(String shortName, String token, String photoID, Integer width, Integer height) throws ApiException {
        okhttp3.Call localVarCall = photoControllerGetPhotoDownloadValidateBeforeCall(shortName, token, photoID, width, height, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Downloads the photo of a property given the photo ID. (asynchronously)
     * 
     * @param shortName The unique client short-name (required)
     * @param token The login token returned from the /session POST call (required)
     * @param photoID The unique ID of the photo on the property (required)
     * @param width An optional parameter specifying the image width (optional)
     * @param height An optional parameter specifying the image height (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call photoControllerGetPhotoDownloadAsync(String shortName, String token, String photoID, Integer width, Integer height, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = photoControllerGetPhotoDownloadValidateBeforeCall(shortName, token, photoID, width, height, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
