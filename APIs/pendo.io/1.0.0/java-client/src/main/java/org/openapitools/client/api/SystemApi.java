/*
 * Pendo Feedback API
 * ## Who is this for?  This documentation is for developers creating their own integration with [Feedback's](https://www.pendo.io/product/feedback/) API. If you are doing a standard integration, there's a really easy [Javascript integration](https://help.receptive.io/hc/en-us/articles/209221969-How-to-integrate-Receptive-with-your-app) that you should know about before you go to the effort of building your own integration.  ## Authentication  API calls generally need to be authenticated. Generate an API Key at https://feedback.pendo.io/app/#/vendor/settings?section=integrate. This key should then be added to every request as a request header named 'auth-token' (preferred), or as a query parameter named 'auth-token'.  ## Endpoint  API endpoint is https://api.feedback.eu.pendo.io / https://api.feedback.us.pendo.io depending where your datacenter is located.  ## Notes  API endpoints are being added to this documentation as needed by customers. If you don't see an endpoint you need please contact support and if it exists we'll publish the docs here. The 'try it out' feature on this documentation page will probably be blocked by your browser because the Access-Control-Allow-Origin header has its value set by the Feedback server depending on your hostname.  ## Generating client code  This documentation is automatically generated from an OpenAPI spec available [here](http://apidoc.receptive.io/receptive.swagger.json). You can use Swagger to auto-generate API client code in many languages using the [Swagger Editor](http://editor.swagger.io/#/)
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@receptive.io
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

public class SystemApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public SystemApi() {
        this(Configuration.getDefaultApiClient());
    }

    public SystemApi(ApiClient apiClient) {
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
     * Build call for healthCheckPingGet
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> API is healthy </td><td>  -  </td></tr>
        <tr><td> 503 </td><td> Load balancers cannot route a request to a healthy API server </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call healthCheckPingGetCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/health-check/ping";

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
    private okhttp3.Call healthCheckPingGetValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return healthCheckPingGetCall(_callback);

    }

    /**
     * Health check for API
     * Provides a response for automatic checks that the API and load balancers are healthy
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> API is healthy </td><td>  -  </td></tr>
        <tr><td> 503 </td><td> Load balancers cannot route a request to a healthy API server </td><td>  -  </td></tr>
     </table>
     */
    public void healthCheckPingGet() throws ApiException {
        healthCheckPingGetWithHttpInfo();
    }

    /**
     * Health check for API
     * Provides a response for automatic checks that the API and load balancers are healthy
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> API is healthy </td><td>  -  </td></tr>
        <tr><td> 503 </td><td> Load balancers cannot route a request to a healthy API server </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> healthCheckPingGetWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = healthCheckPingGetValidateBeforeCall(null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Health check for API (asynchronously)
     * Provides a response for automatic checks that the API and load balancers are healthy
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> API is healthy </td><td>  -  </td></tr>
        <tr><td> 503 </td><td> Load balancers cannot route a request to a healthy API server </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call healthCheckPingGetAsync(final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = healthCheckPingGetValidateBeforeCall(_callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
