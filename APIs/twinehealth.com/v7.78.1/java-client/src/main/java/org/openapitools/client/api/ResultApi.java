/*
 * Fitbit Plus API
 * # Overview The Fitbit Plus API is a RESTful API. The requests and responses are formated according to the [JSON API](http://jsonapi.org/format/1.0/) specification.  In addition to this documentation, we also provide an [OpenAPI](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md) \"yaml\" file describing the API: [Fitbit Plus API Specification](swagger.yaml).  # Authentication Authentication for the Fitbit Plus API is based on the [OAuth 2.0 Authorization Framework](https://tools.ietf.org/html/rfc6749). Fitbit Plus currently supports grant types of **client_credentials** and **refresh_token**.  See [POST /oauth/token](#operation/createToken) for details on the request and response formats. <!-- ReDoc-Inject: <security-definitions> -->  ## Building Integrations We will provide customers with unique client credentials for each application/integration they build, allowing us to enforce appropriate access controls and monitor API usage. The client credentials will be scoped to the organization, and allow full access to all patients and related data within that organization.  These credentials are appropriate for creating an integration that does one of the following:  - background reporting/analysis  - synchronizing data with another system (such as an EMR)  The API credentials and oauth flows we currently support are **not** well suited for creating a user-facing application that allows a user (patient, coach, or admin) to login and have access to data which is appropriate to that specific user. It is possible to build such an application, but it is not possible to use Fitbit Plus as a federated identity provider. You would need to have a separate means of verifying a user's identity. We do not currently support the required password-based oauth flow to make this possible.  # Paging The Fitbit Plus API supports two different pagination strategies for GET collection endpoints.  #### Skip-based paging  Skip-based paging uses the query parameters `page[size]` and `page[number]` to specify the max number of resources returned and the page number. We default to skip-based paging if there are no page parameters. The response will include a `links` object containing links to the first, last, prev, and next pages of data.  If the contents of the collection change while you are iterating through the collection, you will see duplicate or missing documents. For example, if you are iterating through the `calender_event` resource via `GET /pub/calendar_event?sort=start_at&page[size]=50&page[number]=1`, and a new `calendar_event` is created that has a `start_at` value before the first `calendar_event`, when you fetch the next page at `GET /pub/calendar_event?sort=start_at&page[size]=50&page[number]=2`, the first entry in the second response will be a duplicate of the last entry in the first response.  #### Cursor-based paging Cursor-based paging uses the query parameters `page[limit]` and `page[after]` to specify the max number of entries returned and identify where to begin the next page. Add `page[limit]` to the parameters to use cursor-based paging. The response will include a `links` object containing a link to the next page of data, if the next page exists.  Cursor-based paging is not subject to duplication if new resources are added to the collection. For example, if you are iterating through the `calender_event` resource via `GET /pub/calendar_event?sort=start_at&page[limit]=50`, and a new `calendar_event` is created that has a `start_at` value before the first `calendar_event`, you will not see a duplicate entry when you fetch the next page at `GET /pub/calendar_event?sort=start_at&page[limit]=50&page[after]=<cursor>`.  We encourage the use of cursor-based paging for performance reasons.  In either form of paging, you can determine whether any resources were missed by comparing the number of fetched resources against `meta.count`. Set `page[size]` or `page[limit]` to 0 to get only the count.  It is not valid to mix the two strategies. 
 *
 * The version of the OpenAPI document: v7.78.1
 * Contact: apiteam@twinehealth.com
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


import org.openapitools.client.model.FetchErrorResponse;
import org.openapitools.client.model.FetchPatientHealthResultResponse;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ResultApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ResultApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ResultApi(ApiClient apiClient) {
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
     * Build call for fetchPatientHealthResult
     * @param id Patient health result identifier (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call fetchPatientHealthResultCall(String id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/result/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/vnd.api+json"
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
    private okhttp3.Call fetchPatientHealthResultValidateBeforeCall(String id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling fetchPatientHealthResult(Async)");
        }

        return fetchPatientHealthResultCall(id, _callback);

    }

    /**
     * Get a patient health result
     * Get patient health result by id.
     * @param id Patient health result identifier (required)
     * @return FetchPatientHealthResultResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
     </table>
     */
    public FetchPatientHealthResultResponse fetchPatientHealthResult(String id) throws ApiException {
        ApiResponse<FetchPatientHealthResultResponse> localVarResp = fetchPatientHealthResultWithHttpInfo(id);
        return localVarResp.getData();
    }

    /**
     * Get a patient health result
     * Get patient health result by id.
     * @param id Patient health result identifier (required)
     * @return ApiResponse&lt;FetchPatientHealthResultResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<FetchPatientHealthResultResponse> fetchPatientHealthResultWithHttpInfo(String id) throws ApiException {
        okhttp3.Call localVarCall = fetchPatientHealthResultValidateBeforeCall(id, null);
        Type localVarReturnType = new TypeToken<FetchPatientHealthResultResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a patient health result (asynchronously)
     * Get patient health result by id.
     * @param id Patient health result identifier (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call fetchPatientHealthResultAsync(String id, final ApiCallback<FetchPatientHealthResultResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = fetchPatientHealthResultValidateBeforeCall(id, _callback);
        Type localVarReturnType = new TypeToken<FetchPatientHealthResultResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for fetchPatientHealthResults
     * @param filterPatient Filter the patient health results for a specified patient (required)
     * @param filterActions A comma-separated list of action identifiers (optional)
     * @param filterStartAt Filter results that occurred after the passed ISO date and time string (optional)
     * @param filterEndAt Filter results that occurred before the passed ISO date and time string (optional)
     * @param filterThreads A comma-separated list of thread identifiers (optional)
     * @param filterCreatedAt The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for results created in November 2017 (America/New_York): &#x60;filter[created_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60;  (optional)
     * @param filterUpdatedAt The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for results updated in November 2017 (America/New_York): &#x60;filter[updated_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60;  (optional)
     * @param pageNumber Page number (optional, default to 1)
     * @param pageSize Page size (optional, default to 10)
     * @param pageLimit Page limit (optional, default to 50)
     * @param pageAfter Page cursor (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Invalid Request </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call fetchPatientHealthResultsCall(String filterPatient, String filterActions, String filterStartAt, String filterEndAt, String filterThreads, String filterCreatedAt, String filterUpdatedAt, Integer pageNumber, Integer pageSize, Integer pageLimit, String pageAfter, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/result";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (filterPatient != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("filter[patient]", filterPatient));
        }

        if (filterActions != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("filter[actions]", filterActions));
        }

        if (filterStartAt != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("filter[start_at]", filterStartAt));
        }

        if (filterEndAt != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("filter[end_at]", filterEndAt));
        }

        if (filterThreads != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("filter[threads]", filterThreads));
        }

        if (filterCreatedAt != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("filter[created_at]", filterCreatedAt));
        }

        if (filterUpdatedAt != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("filter[updated_at]", filterUpdatedAt));
        }

        if (pageNumber != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page[number]", pageNumber));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page[size]", pageSize));
        }

        if (pageLimit != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page[limit]", pageLimit));
        }

        if (pageAfter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page[after]", pageAfter));
        }

        final String[] localVarAccepts = {
            "application/vnd.api+json"
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
    private okhttp3.Call fetchPatientHealthResultsValidateBeforeCall(String filterPatient, String filterActions, String filterStartAt, String filterEndAt, String filterThreads, String filterCreatedAt, String filterUpdatedAt, Integer pageNumber, Integer pageSize, Integer pageLimit, String pageAfter, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'filterPatient' is set
        if (filterPatient == null) {
            throw new ApiException("Missing the required parameter 'filterPatient' when calling fetchPatientHealthResults(Async)");
        }

        return fetchPatientHealthResultsCall(filterPatient, filterActions, filterStartAt, filterEndAt, filterThreads, filterCreatedAt, filterUpdatedAt, pageNumber, pageSize, pageLimit, pageAfter, _callback);

    }

    /**
     * List patient health results
     * Get a list of patient health results.
     * @param filterPatient Filter the patient health results for a specified patient (required)
     * @param filterActions A comma-separated list of action identifiers (optional)
     * @param filterStartAt Filter results that occurred after the passed ISO date and time string (optional)
     * @param filterEndAt Filter results that occurred before the passed ISO date and time string (optional)
     * @param filterThreads A comma-separated list of thread identifiers (optional)
     * @param filterCreatedAt The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for results created in November 2017 (America/New_York): &#x60;filter[created_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60;  (optional)
     * @param filterUpdatedAt The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for results updated in November 2017 (America/New_York): &#x60;filter[updated_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60;  (optional)
     * @param pageNumber Page number (optional, default to 1)
     * @param pageSize Page size (optional, default to 10)
     * @param pageLimit Page limit (optional, default to 50)
     * @param pageAfter Page cursor (optional)
     * @return FetchPatientHealthResultResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Invalid Request </td><td>  -  </td></tr>
     </table>
     */
    public FetchPatientHealthResultResponse fetchPatientHealthResults(String filterPatient, String filterActions, String filterStartAt, String filterEndAt, String filterThreads, String filterCreatedAt, String filterUpdatedAt, Integer pageNumber, Integer pageSize, Integer pageLimit, String pageAfter) throws ApiException {
        ApiResponse<FetchPatientHealthResultResponse> localVarResp = fetchPatientHealthResultsWithHttpInfo(filterPatient, filterActions, filterStartAt, filterEndAt, filterThreads, filterCreatedAt, filterUpdatedAt, pageNumber, pageSize, pageLimit, pageAfter);
        return localVarResp.getData();
    }

    /**
     * List patient health results
     * Get a list of patient health results.
     * @param filterPatient Filter the patient health results for a specified patient (required)
     * @param filterActions A comma-separated list of action identifiers (optional)
     * @param filterStartAt Filter results that occurred after the passed ISO date and time string (optional)
     * @param filterEndAt Filter results that occurred before the passed ISO date and time string (optional)
     * @param filterThreads A comma-separated list of thread identifiers (optional)
     * @param filterCreatedAt The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for results created in November 2017 (America/New_York): &#x60;filter[created_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60;  (optional)
     * @param filterUpdatedAt The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for results updated in November 2017 (America/New_York): &#x60;filter[updated_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60;  (optional)
     * @param pageNumber Page number (optional, default to 1)
     * @param pageSize Page size (optional, default to 10)
     * @param pageLimit Page limit (optional, default to 50)
     * @param pageAfter Page cursor (optional)
     * @return ApiResponse&lt;FetchPatientHealthResultResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Invalid Request </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<FetchPatientHealthResultResponse> fetchPatientHealthResultsWithHttpInfo(String filterPatient, String filterActions, String filterStartAt, String filterEndAt, String filterThreads, String filterCreatedAt, String filterUpdatedAt, Integer pageNumber, Integer pageSize, Integer pageLimit, String pageAfter) throws ApiException {
        okhttp3.Call localVarCall = fetchPatientHealthResultsValidateBeforeCall(filterPatient, filterActions, filterStartAt, filterEndAt, filterThreads, filterCreatedAt, filterUpdatedAt, pageNumber, pageSize, pageLimit, pageAfter, null);
        Type localVarReturnType = new TypeToken<FetchPatientHealthResultResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List patient health results (asynchronously)
     * Get a list of patient health results.
     * @param filterPatient Filter the patient health results for a specified patient (required)
     * @param filterActions A comma-separated list of action identifiers (optional)
     * @param filterStartAt Filter results that occurred after the passed ISO date and time string (optional)
     * @param filterEndAt Filter results that occurred before the passed ISO date and time string (optional)
     * @param filterThreads A comma-separated list of thread identifiers (optional)
     * @param filterCreatedAt The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for results created in November 2017 (America/New_York): &#x60;filter[created_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60;  (optional)
     * @param filterUpdatedAt The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for results updated in November 2017 (America/New_York): &#x60;filter[updated_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60;  (optional)
     * @param pageNumber Page number (optional, default to 1)
     * @param pageSize Page size (optional, default to 10)
     * @param pageLimit Page limit (optional, default to 50)
     * @param pageAfter Page cursor (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Invalid Request </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call fetchPatientHealthResultsAsync(String filterPatient, String filterActions, String filterStartAt, String filterEndAt, String filterThreads, String filterCreatedAt, String filterUpdatedAt, Integer pageNumber, Integer pageSize, Integer pageLimit, String pageAfter, final ApiCallback<FetchPatientHealthResultResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = fetchPatientHealthResultsValidateBeforeCall(filterPatient, filterActions, filterStartAt, filterEndAt, filterThreads, filterCreatedAt, filterUpdatedAt, pageNumber, pageSize, pageLimit, pageAfter, _callback);
        Type localVarReturnType = new TypeToken<FetchPatientHealthResultResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
