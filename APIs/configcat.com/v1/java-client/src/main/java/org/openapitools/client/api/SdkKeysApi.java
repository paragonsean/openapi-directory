/*
 * ConfigCat Public Management API
 * **Base API URL**: https://api.configcat.com  If you prefer the swagger documentation, you can find it here: [Swagger UI](https://api.configcat.com/swagger).  The purpose of this API is to access the ConfigCat platform programmatically.  You can **Create**, **Read**, **Update** and **Delete** any entities like **Feature Flags, Configs, Environments** or **Products** within ConfigCat.   The API is based on HTTP REST, uses resource-oriented URLs, status codes and supports JSON  and JSON+HAL format. Do not use this API for accessing and evaluating feature flag values. Use the [SDKs instead](https://configcat.com/docs/sdk-reference/overview).   # OpenAPI Specification  The complete specification is publicly available here: [swagger.json](v1/swagger.json).  You can use it to generate client libraries in various languages with [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) or [Swagger Codegen](https://swagger.io/tools/swagger-codegen/) to interact with this API.  # Authentication This API uses the [Basic HTTP Authentication Scheme](https://en.wikipedia.org/wiki/Basic_access_authentication).   <!-- ReDoc-Inject: <security-definitions> -->  # Throttling and rate limits All the rate limited API calls are returning information about the current rate limit period in the following HTTP headers:  | Header | Description | | :- | :- | | X-Rate-Limit-Remaining | The maximum number of requests remaining in the current rate limit period. | | X-Rate-Limit-Reset     | The time when the current rate limit period resets.        |  When the rate limit is exceeded by a request, the API returns with a `HTTP 429 - Too many requests` status along with a `Retry-After` HTTP header. 
 *
 * The version of the OpenAPI document: v1
 * Contact: support@configcat.com
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


import org.openapitools.client.model.SdkKeysModel;
import java.util.UUID;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SdkKeysApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public SdkKeysApi() {
        this(Configuration.getDefaultApiClient());
    }

    public SdkKeysApi(ApiClient apiClient) {
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
     * Build call for getSdkKeys
     * @param configId The identifier of the Config. (required)
     * @param environmentId The identifier of the Environment. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized. In case of the Public Management API credentials are invalid. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests. In case of the request rate exceeds the rate limits. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSdkKeysCall(UUID configId, UUID environmentId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/configs/{configId}/environments/{environmentId}"
            .replace("{" + "configId" + "}", localVarApiClient.escapeString(configId.toString()))
            .replace("{" + "environmentId" + "}", localVarApiClient.escapeString(environmentId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/hal+json",
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

        String[] localVarAuthNames = new String[] { "Basic" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getSdkKeysValidateBeforeCall(UUID configId, UUID environmentId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'configId' is set
        if (configId == null) {
            throw new ApiException("Missing the required parameter 'configId' when calling getSdkKeys(Async)");
        }

        // verify the required parameter 'environmentId' is set
        if (environmentId == null) {
            throw new ApiException("Missing the required parameter 'environmentId' when calling getSdkKeys(Async)");
        }

        return getSdkKeysCall(configId, environmentId, _callback);

    }

    /**
     * Get SDK Key
     * This endpoint returns the SDK Key for your Config in a specified Environment.
     * @param configId The identifier of the Config. (required)
     * @param environmentId The identifier of the Environment. (required)
     * @return SdkKeysModel
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized. In case of the Public Management API credentials are invalid. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests. In case of the request rate exceeds the rate limits. </td><td>  -  </td></tr>
     </table>
     */
    public SdkKeysModel getSdkKeys(UUID configId, UUID environmentId) throws ApiException {
        ApiResponse<SdkKeysModel> localVarResp = getSdkKeysWithHttpInfo(configId, environmentId);
        return localVarResp.getData();
    }

    /**
     * Get SDK Key
     * This endpoint returns the SDK Key for your Config in a specified Environment.
     * @param configId The identifier of the Config. (required)
     * @param environmentId The identifier of the Environment. (required)
     * @return ApiResponse&lt;SdkKeysModel&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized. In case of the Public Management API credentials are invalid. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests. In case of the request rate exceeds the rate limits. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<SdkKeysModel> getSdkKeysWithHttpInfo(UUID configId, UUID environmentId) throws ApiException {
        okhttp3.Call localVarCall = getSdkKeysValidateBeforeCall(configId, environmentId, null);
        Type localVarReturnType = new TypeToken<SdkKeysModel>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get SDK Key (asynchronously)
     * This endpoint returns the SDK Key for your Config in a specified Environment.
     * @param configId The identifier of the Config. (required)
     * @param environmentId The identifier of the Environment. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized. In case of the Public Management API credentials are invalid. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> Too many requests. In case of the request rate exceeds the rate limits. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSdkKeysAsync(UUID configId, UUID environmentId, final ApiCallback<SdkKeysModel> _callback) throws ApiException {

        okhttp3.Call localVarCall = getSdkKeysValidateBeforeCall(configId, environmentId, _callback);
        Type localVarReturnType = new TypeToken<SdkKeysModel>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
