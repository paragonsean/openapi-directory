/*
 * TruAnon Private API
 * Welcome to TruAnon! Thank you for helping make the Internet a safer place to be.  Adopting TruAnon is simple. There is no setup or dependencies, nothing to store or process. Making identity part of your service is fun, and you’ll be up and running in a matter of minutes.  TruAnon Private Token is used anytime you request information from TruAnon and you must edit this into the Variables section for this collection.  This API contains two endpoints and both require these same two arguments, also found in the Variables section of this collection.  These two arguments are:  TruAnon Service Identifier  and  Your Member Name  Your TruAnon Service Identifier was provided by TruAnon and is likely the root domain of your site or service. Your Member Name is the unique member ID on your system that you would like to query.  Information is continuously updated for display purposes and aside from performance considerations, there should be no need to capture or save anything from TruAnon.
 *
 * The version of the OpenAPI document: 1.0.0
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

public class DefaultApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public DefaultApi() {
        this(Configuration.getDefaultApiClient());
    }

    public DefaultApi(ApiClient apiClient) {
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
     * Build call for getProfile
     * @param id This is your unique username or member ID (optional)
     * @param service The service name given to you by TruAnon (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getProfileCall(String id, String service, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/get_profile";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (id != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("id", id));
        }

        if (service != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("service", service));
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
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getProfileValidateBeforeCall(String id, String service, final ApiCallback _callback) throws ApiException {
        return getProfileCall(id, service, _callback);

    }

    /**
     * Get Profile
     * get_profile Private API: Request confirmed profile data for your unique member ID
     * @param id This is your unique username or member ID (optional)
     * @param service The service name given to you by TruAnon (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public void getProfile(String id, String service) throws ApiException {
        getProfileWithHttpInfo(id, service);
    }

    /**
     * Get Profile
     * get_profile Private API: Request confirmed profile data for your unique member ID
     * @param id This is your unique username or member ID (optional)
     * @param service The service name given to you by TruAnon (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> getProfileWithHttpInfo(String id, String service) throws ApiException {
        okhttp3.Call localVarCall = getProfileValidateBeforeCall(id, service, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Get Profile (asynchronously)
     * get_profile Private API: Request confirmed profile data for your unique member ID
     * @param id This is your unique username or member ID (optional)
     * @param service The service name given to you by TruAnon (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getProfileAsync(String id, String service, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = getProfileValidateBeforeCall(id, service, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getToken
     * @param id This is your unique username or member ID (optional)
     * @param service The service name given to you by TruAnon (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getTokenCall(String id, String service, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/request_token";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (id != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("id", id));
        }

        if (service != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("service", service));
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
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getTokenValidateBeforeCall(String id, String service, final ApiCallback _callback) throws ApiException {
        return getTokenCall(id, service, _callback);

    }

    /**
     * Get Token
     * request_token Private API: Request a Proof token to let the member confirm in a popup interface          {\&quot;id\&quot;:\&quot;qjgblv72bzzio\&quot;,\&quot;type\&quot;:\&quot;Proof\&quot;,\&quot;active\&quot;:true,\&quot;name\&quot;:\&quot;New Proof\&quot;}  Step 2. Create a verifyProfile Public Web link: Use the Proof token id as the token argument in your public URL used to open a new target popup. This activity is where members may confirm immediately.              https://staging.truanon.com/verifyProfile?id&#x3D;john_doe&amp;service&#x3D;securecannabisalliance&amp;token&#x3D;qjgblv72bzzio
     * @param id This is your unique username or member ID (optional)
     * @param service The service name given to you by TruAnon (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public void getToken(String id, String service) throws ApiException {
        getTokenWithHttpInfo(id, service);
    }

    /**
     * Get Token
     * request_token Private API: Request a Proof token to let the member confirm in a popup interface          {\&quot;id\&quot;:\&quot;qjgblv72bzzio\&quot;,\&quot;type\&quot;:\&quot;Proof\&quot;,\&quot;active\&quot;:true,\&quot;name\&quot;:\&quot;New Proof\&quot;}  Step 2. Create a verifyProfile Public Web link: Use the Proof token id as the token argument in your public URL used to open a new target popup. This activity is where members may confirm immediately.              https://staging.truanon.com/verifyProfile?id&#x3D;john_doe&amp;service&#x3D;securecannabisalliance&amp;token&#x3D;qjgblv72bzzio
     * @param id This is your unique username or member ID (optional)
     * @param service The service name given to you by TruAnon (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> getTokenWithHttpInfo(String id, String service) throws ApiException {
        okhttp3.Call localVarCall = getTokenValidateBeforeCall(id, service, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Get Token (asynchronously)
     * request_token Private API: Request a Proof token to let the member confirm in a popup interface          {\&quot;id\&quot;:\&quot;qjgblv72bzzio\&quot;,\&quot;type\&quot;:\&quot;Proof\&quot;,\&quot;active\&quot;:true,\&quot;name\&quot;:\&quot;New Proof\&quot;}  Step 2. Create a verifyProfile Public Web link: Use the Proof token id as the token argument in your public URL used to open a new target popup. This activity is where members may confirm immediately.              https://staging.truanon.com/verifyProfile?id&#x3D;john_doe&amp;service&#x3D;securecannabisalliance&amp;token&#x3D;qjgblv72bzzio
     * @param id This is your unique username or member ID (optional)
     * @param service The service name given to you by TruAnon (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getTokenAsync(String id, String service, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = getTokenValidateBeforeCall(id, service, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
