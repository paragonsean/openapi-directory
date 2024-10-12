/*
 * SubscriptionClient
 * The User Subscription Management Client.
 *
 * The version of the OpenAPI document: 2015-11-01
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


import org.openapitools.client.model.Offer;
import org.openapitools.client.model.OfferList;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DelegatedProviderOffersApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public DelegatedProviderOffersApi() {
        this(Configuration.getDefaultApiClient());
    }

    public DelegatedProviderOffersApi(ApiClient apiClient) {
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
     * Build call for delegatedProviderOffersGet
     * @param delegatedProviderId Id of the delegated provider. (required)
     * @param offerName Name of the offer. (required)
     * @param apiVersion Client Api Version. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call delegatedProviderOffersGetCall(String delegatedProviderId, String offerName, String apiVersion, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/delegatedProviders/{delegatedProviderId}/offers/{offerName}"
            .replace("{" + "delegatedProviderId" + "}", localVarApiClient.escapeString(delegatedProviderId.toString()))
            .replace("{" + "offerName" + "}", localVarApiClient.escapeString(offerName.toString()));

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
    private okhttp3.Call delegatedProviderOffersGetValidateBeforeCall(String delegatedProviderId, String offerName, String apiVersion, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'delegatedProviderId' is set
        if (delegatedProviderId == null) {
            throw new ApiException("Missing the required parameter 'delegatedProviderId' when calling delegatedProviderOffersGet(Async)");
        }

        // verify the required parameter 'offerName' is set
        if (offerName == null) {
            throw new ApiException("Missing the required parameter 'offerName' when calling delegatedProviderOffersGet(Async)");
        }

        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling delegatedProviderOffersGet(Async)");
        }

        return delegatedProviderOffersGetCall(delegatedProviderId, offerName, apiVersion, _callback);

    }

    /**
     * 
     * Get the specified offer for the delegated provider.
     * @param delegatedProviderId Id of the delegated provider. (required)
     * @param offerName Name of the offer. (required)
     * @param apiVersion Client Api Version. (required)
     * @return Offer
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Offer delegatedProviderOffersGet(String delegatedProviderId, String offerName, String apiVersion) throws ApiException {
        ApiResponse<Offer> localVarResp = delegatedProviderOffersGetWithHttpInfo(delegatedProviderId, offerName, apiVersion);
        return localVarResp.getData();
    }

    /**
     * 
     * Get the specified offer for the delegated provider.
     * @param delegatedProviderId Id of the delegated provider. (required)
     * @param offerName Name of the offer. (required)
     * @param apiVersion Client Api Version. (required)
     * @return ApiResponse&lt;Offer&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Offer> delegatedProviderOffersGetWithHttpInfo(String delegatedProviderId, String offerName, String apiVersion) throws ApiException {
        okhttp3.Call localVarCall = delegatedProviderOffersGetValidateBeforeCall(delegatedProviderId, offerName, apiVersion, null);
        Type localVarReturnType = new TypeToken<Offer>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Get the specified offer for the delegated provider.
     * @param delegatedProviderId Id of the delegated provider. (required)
     * @param offerName Name of the offer. (required)
     * @param apiVersion Client Api Version. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call delegatedProviderOffersGetAsync(String delegatedProviderId, String offerName, String apiVersion, final ApiCallback<Offer> _callback) throws ApiException {

        okhttp3.Call localVarCall = delegatedProviderOffersGetValidateBeforeCall(delegatedProviderId, offerName, apiVersion, _callback);
        Type localVarReturnType = new TypeToken<Offer>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for delegatedProviderOffersList
     * @param delegatedProviderId Id of the delegated provider. (required)
     * @param apiVersion Client Api Version. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call delegatedProviderOffersListCall(String delegatedProviderId, String apiVersion, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/delegatedProviders/{delegatedProviderId}/offers"
            .replace("{" + "delegatedProviderId" + "}", localVarApiClient.escapeString(delegatedProviderId.toString()));

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
    private okhttp3.Call delegatedProviderOffersListValidateBeforeCall(String delegatedProviderId, String apiVersion, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'delegatedProviderId' is set
        if (delegatedProviderId == null) {
            throw new ApiException("Missing the required parameter 'delegatedProviderId' when calling delegatedProviderOffersList(Async)");
        }

        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling delegatedProviderOffersList(Async)");
        }

        return delegatedProviderOffersListCall(delegatedProviderId, apiVersion, _callback);

    }

    /**
     * 
     * Get the list of offers for the specified delegated provider.
     * @param delegatedProviderId Id of the delegated provider. (required)
     * @param apiVersion Client Api Version. (required)
     * @return OfferList
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public OfferList delegatedProviderOffersList(String delegatedProviderId, String apiVersion) throws ApiException {
        ApiResponse<OfferList> localVarResp = delegatedProviderOffersListWithHttpInfo(delegatedProviderId, apiVersion);
        return localVarResp.getData();
    }

    /**
     * 
     * Get the list of offers for the specified delegated provider.
     * @param delegatedProviderId Id of the delegated provider. (required)
     * @param apiVersion Client Api Version. (required)
     * @return ApiResponse&lt;OfferList&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<OfferList> delegatedProviderOffersListWithHttpInfo(String delegatedProviderId, String apiVersion) throws ApiException {
        okhttp3.Call localVarCall = delegatedProviderOffersListValidateBeforeCall(delegatedProviderId, apiVersion, null);
        Type localVarReturnType = new TypeToken<OfferList>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Get the list of offers for the specified delegated provider.
     * @param delegatedProviderId Id of the delegated provider. (required)
     * @param apiVersion Client Api Version. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call delegatedProviderOffersListAsync(String delegatedProviderId, String apiVersion, final ApiCallback<OfferList> _callback) throws ApiException {

        okhttp3.Call localVarCall = delegatedProviderOffersListValidateBeforeCall(delegatedProviderId, apiVersion, _callback);
        Type localVarReturnType = new TypeToken<OfferList>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
