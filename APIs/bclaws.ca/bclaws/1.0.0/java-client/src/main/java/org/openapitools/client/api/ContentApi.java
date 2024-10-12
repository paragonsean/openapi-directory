/*
 * BC Laws
 * BC Laws is an electronic library providing free public access to the laws of British Columbia. BC Laws is hosted by the Queen's Printer of British Columbia and published in partnership with the Ministry of Justice and the Law Clerk of the Legislative Assembly.BC Laws contains a comprehensive collection of BC legislation and related materials. It is available on the internet in two forms:First: The library is available as a web site in which users can browse and search the laws of British Columbia.Second: The library is available as a portal to legislation in raw XML data format, accessible via the BC Laws API2. This direct access to raw data is intended to enable third parties to build or add their own custom applications based on the structure of the data and all the associated search functionality inherent in that structure. The BC Laws website itself is an example of one such application.   Please note that you may experience issues when submitting requests to the delivery or test environment if using this [OpenAPI specification](https://github.com/bcgov/api-specs) in other API console viewers.
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

public class ContentApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ContentApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ContentApi(ApiClient apiClient) {
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
     * Build call for contentAspectIdCivixDocumentIdGet
     * @param aspectId The identifier of the &#39;aspect&#39; (content group) to search (required)
     * @param civixDocumentId The document identification code for an index or directory (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List documents and directories within the aspect. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call contentAspectIdCivixDocumentIdGetCall(String aspectId, String civixDocumentId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/content/{aspectId}/{civixDocumentId}"
            .replace("{" + "aspectId" + "}", localVarApiClient.escapeString(aspectId.toString()))
            .replace("{" + "civixDocumentId" + "}", localVarApiClient.escapeString(civixDocumentId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

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
    private okhttp3.Call contentAspectIdCivixDocumentIdGetValidateBeforeCall(String aspectId, String civixDocumentId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'aspectId' is set
        if (aspectId == null) {
            throw new ApiException("Missing the required parameter 'aspectId' when calling contentAspectIdCivixDocumentIdGet(Async)");
        }

        // verify the required parameter 'civixDocumentId' is set
        if (civixDocumentId == null) {
            throw new ApiException("Missing the required parameter 'civixDocumentId' when calling contentAspectIdCivixDocumentIdGet(Async)");
        }

        return contentAspectIdCivixDocumentIdGetCall(aspectId, civixDocumentId, _callback);

    }

    /**
     * Lists the metadata available for the specified index or directory from the BCLaws legislative respository
     * 
     * @param aspectId The identifier of the &#39;aspect&#39; (content group) to search (required)
     * @param civixDocumentId The document identification code for an index or directory (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List documents and directories within the aspect. </td><td>  -  </td></tr>
     </table>
     */
    public void contentAspectIdCivixDocumentIdGet(String aspectId, String civixDocumentId) throws ApiException {
        contentAspectIdCivixDocumentIdGetWithHttpInfo(aspectId, civixDocumentId);
    }

    /**
     * Lists the metadata available for the specified index or directory from the BCLaws legislative respository
     * 
     * @param aspectId The identifier of the &#39;aspect&#39; (content group) to search (required)
     * @param civixDocumentId The document identification code for an index or directory (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List documents and directories within the aspect. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> contentAspectIdCivixDocumentIdGetWithHttpInfo(String aspectId, String civixDocumentId) throws ApiException {
        okhttp3.Call localVarCall = contentAspectIdCivixDocumentIdGetValidateBeforeCall(aspectId, civixDocumentId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Lists the metadata available for the specified index or directory from the BCLaws legislative respository (asynchronously)
     * 
     * @param aspectId The identifier of the &#39;aspect&#39; (content group) to search (required)
     * @param civixDocumentId The document identification code for an index or directory (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List documents and directories within the aspect. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call contentAspectIdCivixDocumentIdGetAsync(String aspectId, String civixDocumentId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = contentAspectIdCivixDocumentIdGetValidateBeforeCall(aspectId, civixDocumentId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for contentAspectIdGet
     * @param aspectId The identifier of the &#39;aspect&#39; (content group) to search (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List documents and directories within the aspect. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call contentAspectIdGetCall(String aspectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/content/{aspectId}"
            .replace("{" + "aspectId" + "}", localVarApiClient.escapeString(aspectId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

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
    private okhttp3.Call contentAspectIdGetValidateBeforeCall(String aspectId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'aspectId' is set
        if (aspectId == null) {
            throw new ApiException("Missing the required parameter 'aspectId' when calling contentAspectIdGet(Async)");
        }

        return contentAspectIdGetCall(aspectId, _callback);

    }

    /**
     * Describes the documents and directories available within a specific &#39;aspect&#39; (content group) of the BCLaws library
     * 
     * @param aspectId The identifier of the &#39;aspect&#39; (content group) to search (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List documents and directories within the aspect. </td><td>  -  </td></tr>
     </table>
     */
    public void contentAspectIdGet(String aspectId) throws ApiException {
        contentAspectIdGetWithHttpInfo(aspectId);
    }

    /**
     * Describes the documents and directories available within a specific &#39;aspect&#39; (content group) of the BCLaws library
     * 
     * @param aspectId The identifier of the &#39;aspect&#39; (content group) to search (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List documents and directories within the aspect. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> contentAspectIdGetWithHttpInfo(String aspectId) throws ApiException {
        okhttp3.Call localVarCall = contentAspectIdGetValidateBeforeCall(aspectId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Describes the documents and directories available within a specific &#39;aspect&#39; (content group) of the BCLaws library (asynchronously)
     * 
     * @param aspectId The identifier of the &#39;aspect&#39; (content group) to search (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List documents and directories within the aspect. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call contentAspectIdGetAsync(String aspectId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = contentAspectIdGetValidateBeforeCall(aspectId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
