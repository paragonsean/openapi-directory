/*
 * PowerTools Developer
 * Apptigent PowerTools Developer Edition is a powerful suite of API endpoints for custom applications running on any stack. Manipulate text, modify collections, format dates and times, convert currency, perform advanced mathematical calculations, shorten URL's, encode strings, convert text to speech, translate content into multiple languages, process images, and more. PowerTools is the ultimate developer toolkit.
 *
 * The version of the OpenAPI document: 2021.1.01
 * Contact: support@apptigent.com
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


import org.openapitools.client.model.InputDateTimeConversion;
import org.openapitools.client.model.InputDateTimeDifference;
import org.openapitools.client.model.InputDateTimeFormat;
import org.openapitools.client.model.InputDateTimeInfo;
import org.openapitools.client.model.OutputDateDifference;
import org.openapitools.client.model.OutputDateInfo;
import org.openapitools.client.model.OutputString;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DateTimeApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public DateTimeApi() {
        this(Configuration.getDefaultApiClient());
    }

    public DateTimeApi(ApiClient apiClient) {
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
     * Build call for dateTimeDifference
     * @param dateTimeDifference  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> ERROR </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call dateTimeDifferenceCall(InputDateTimeDifference dateTimeDifference, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = dateTimeDifference;

        // create path and map variables
        String localVarPath = "/DateTimeDifference";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "apiKeyHeader" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call dateTimeDifferenceValidateBeforeCall(InputDateTimeDifference dateTimeDifference, final ApiCallback _callback) throws ApiException {
        return dateTimeDifferenceCall(dateTimeDifference, _callback);

    }

    /**
     * DateTime - DateTime difference
     * Calculate the difference between two dates
     * @param dateTimeDifference  (optional)
     * @return OutputDateDifference
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> ERROR </td><td>  -  </td></tr>
     </table>
     */
    public OutputDateDifference dateTimeDifference(InputDateTimeDifference dateTimeDifference) throws ApiException {
        ApiResponse<OutputDateDifference> localVarResp = dateTimeDifferenceWithHttpInfo(dateTimeDifference);
        return localVarResp.getData();
    }

    /**
     * DateTime - DateTime difference
     * Calculate the difference between two dates
     * @param dateTimeDifference  (optional)
     * @return ApiResponse&lt;OutputDateDifference&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> ERROR </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<OutputDateDifference> dateTimeDifferenceWithHttpInfo(InputDateTimeDifference dateTimeDifference) throws ApiException {
        okhttp3.Call localVarCall = dateTimeDifferenceValidateBeforeCall(dateTimeDifference, null);
        Type localVarReturnType = new TypeToken<OutputDateDifference>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * DateTime - DateTime difference (asynchronously)
     * Calculate the difference between two dates
     * @param dateTimeDifference  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> ERROR </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call dateTimeDifferenceAsync(InputDateTimeDifference dateTimeDifference, final ApiCallback<OutputDateDifference> _callback) throws ApiException {

        okhttp3.Call localVarCall = dateTimeDifferenceValidateBeforeCall(dateTimeDifference, _callback);
        Type localVarReturnType = new TypeToken<OutputDateDifference>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for dateTimeInfo
     * @param dateTimeInfo  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> ERROR </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call dateTimeInfoCall(InputDateTimeInfo dateTimeInfo, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = dateTimeInfo;

        // create path and map variables
        String localVarPath = "/DateTimeInfo";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "apiKeyHeader" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call dateTimeInfoValidateBeforeCall(InputDateTimeInfo dateTimeInfo, final ApiCallback _callback) throws ApiException {
        return dateTimeInfoCall(dateTimeInfo, _callback);

    }

    /**
     * DateTime - Get date and time information
     * Retrieve useful date and time information, such as day of year, total seconds and ticks
     * @param dateTimeInfo  (optional)
     * @return OutputDateInfo
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> ERROR </td><td>  -  </td></tr>
     </table>
     */
    public OutputDateInfo dateTimeInfo(InputDateTimeInfo dateTimeInfo) throws ApiException {
        ApiResponse<OutputDateInfo> localVarResp = dateTimeInfoWithHttpInfo(dateTimeInfo);
        return localVarResp.getData();
    }

    /**
     * DateTime - Get date and time information
     * Retrieve useful date and time information, such as day of year, total seconds and ticks
     * @param dateTimeInfo  (optional)
     * @return ApiResponse&lt;OutputDateInfo&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> ERROR </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<OutputDateInfo> dateTimeInfoWithHttpInfo(InputDateTimeInfo dateTimeInfo) throws ApiException {
        okhttp3.Call localVarCall = dateTimeInfoValidateBeforeCall(dateTimeInfo, null);
        Type localVarReturnType = new TypeToken<OutputDateInfo>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * DateTime - Get date and time information (asynchronously)
     * Retrieve useful date and time information, such as day of year, total seconds and ticks
     * @param dateTimeInfo  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> ERROR </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call dateTimeInfoAsync(InputDateTimeInfo dateTimeInfo, final ApiCallback<OutputDateInfo> _callback) throws ApiException {

        okhttp3.Call localVarCall = dateTimeInfoValidateBeforeCall(dateTimeInfo, _callback);
        Type localVarReturnType = new TypeToken<OutputDateInfo>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for formatDateTime
     * @param dateTimeFormat  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> ERROR </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call formatDateTimeCall(InputDateTimeFormat dateTimeFormat, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = dateTimeFormat;

        // create path and map variables
        String localVarPath = "/FormatDateTime";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "apiKeyHeader" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call formatDateTimeValidateBeforeCall(InputDateTimeFormat dateTimeFormat, final ApiCallback _callback) throws ApiException {
        return formatDateTimeCall(dateTimeFormat, _callback);

    }

    /**
     * DateTime - Format date and time
     * Create a date/time string in a specific format
     * @param dateTimeFormat  (optional)
     * @return OutputString
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> ERROR </td><td>  -  </td></tr>
     </table>
     */
    public OutputString formatDateTime(InputDateTimeFormat dateTimeFormat) throws ApiException {
        ApiResponse<OutputString> localVarResp = formatDateTimeWithHttpInfo(dateTimeFormat);
        return localVarResp.getData();
    }

    /**
     * DateTime - Format date and time
     * Create a date/time string in a specific format
     * @param dateTimeFormat  (optional)
     * @return ApiResponse&lt;OutputString&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> ERROR </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<OutputString> formatDateTimeWithHttpInfo(InputDateTimeFormat dateTimeFormat) throws ApiException {
        okhttp3.Call localVarCall = formatDateTimeValidateBeforeCall(dateTimeFormat, null);
        Type localVarReturnType = new TypeToken<OutputString>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * DateTime - Format date and time (asynchronously)
     * Create a date/time string in a specific format
     * @param dateTimeFormat  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> ERROR </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call formatDateTimeAsync(InputDateTimeFormat dateTimeFormat, final ApiCallback<OutputString> _callback) throws ApiException {

        okhttp3.Call localVarCall = formatDateTimeValidateBeforeCall(dateTimeFormat, _callback);
        Type localVarReturnType = new TypeToken<OutputString>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for worldTime
     * @param dateTimeConversion  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> ERROR </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call worldTimeCall(InputDateTimeConversion dateTimeConversion, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = dateTimeConversion;

        // create path and map variables
        String localVarPath = "/WorldTime";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "apiKeyHeader" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call worldTimeValidateBeforeCall(InputDateTimeConversion dateTimeConversion, final ApiCallback _callback) throws ApiException {
        return worldTimeCall(dateTimeConversion, _callback);

    }

    /**
     * DateTime - Get world time
     * Convert date and time from one time zone to another
     * @param dateTimeConversion  (optional)
     * @return OutputString
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> ERROR </td><td>  -  </td></tr>
     </table>
     */
    public OutputString worldTime(InputDateTimeConversion dateTimeConversion) throws ApiException {
        ApiResponse<OutputString> localVarResp = worldTimeWithHttpInfo(dateTimeConversion);
        return localVarResp.getData();
    }

    /**
     * DateTime - Get world time
     * Convert date and time from one time zone to another
     * @param dateTimeConversion  (optional)
     * @return ApiResponse&lt;OutputString&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> ERROR </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<OutputString> worldTimeWithHttpInfo(InputDateTimeConversion dateTimeConversion) throws ApiException {
        okhttp3.Call localVarCall = worldTimeValidateBeforeCall(dateTimeConversion, null);
        Type localVarReturnType = new TypeToken<OutputString>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * DateTime - Get world time (asynchronously)
     * Convert date and time from one time zone to another
     * @param dateTimeConversion  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> ERROR </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call worldTimeAsync(InputDateTimeConversion dateTimeConversion, final ApiCallback<OutputString> _callback) throws ApiException {

        okhttp3.Call localVarCall = worldTimeValidateBeforeCall(dateTimeConversion, _callback);
        Type localVarReturnType = new TypeToken<OutputString>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
