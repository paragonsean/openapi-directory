/*
 * Test the ExhibitDay API with Swagger
 * This API can be used to programmatically pull data out of ExhibitDay or push data into ExhibitDay -- allowing for automation between ExhibitDay and your internal systems (or other third-party software). To use the API, you'll need working knowledge of consuming REST APIs.<br /><br />Docs: https://api.exhibitday.com/swagger/docs/v1
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


import java.math.BigDecimal;
import java.time.LocalDate;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class FinancialsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public FinancialsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public FinancialsApi(ApiClient apiClient) {
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
     * Build call for financialsEventCosts0Get
     * @param apiKey  (required)
     * @param filterByEventId Id of a specific event that you would like to retrieve costs for. (optional)
     * @param filterByEventStartDateGreaterThanOrEqualTo Only include costs for events that have their start date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD (optional)
     * @param filterByEventStartDateSmallerThanOrEqualTo Only include costs for events that have their start date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD (optional)
     * @param filterByEventEndDateGreaterThanOrEqualTo Only include costs for events that have their end date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD (optional)
     * @param filterByEventEndDateSmallerThanOrEqualTo Only include costs for events that have their end date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call financialsEventCosts0GetCall(String apiKey, BigDecimal filterByEventId, LocalDate filterByEventStartDateGreaterThanOrEqualTo, LocalDate filterByEventStartDateSmallerThanOrEqualTo, LocalDate filterByEventEndDateGreaterThanOrEqualTo, LocalDate filterByEventEndDateSmallerThanOrEqualTo, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/financials/event_costs";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (apiKey != null) {
            localVarHeaderParams.put("api_key", localVarApiClient.parameterToString(apiKey));
        }

        if (filterByEventId != null) {
            localVarHeaderParams.put("filter_by_event_id", localVarApiClient.parameterToString(filterByEventId));
        }

        if (filterByEventStartDateGreaterThanOrEqualTo != null) {
            localVarHeaderParams.put("filter_by_event_start_date_greater_than_or_equal_to", localVarApiClient.parameterToString(filterByEventStartDateGreaterThanOrEqualTo));
        }

        if (filterByEventStartDateSmallerThanOrEqualTo != null) {
            localVarHeaderParams.put("filter_by_event_start_date_smaller_than_or_equal_to", localVarApiClient.parameterToString(filterByEventStartDateSmallerThanOrEqualTo));
        }

        if (filterByEventEndDateGreaterThanOrEqualTo != null) {
            localVarHeaderParams.put("filter_by_event_end_date_greater_than_or_equal_to", localVarApiClient.parameterToString(filterByEventEndDateGreaterThanOrEqualTo));
        }

        if (filterByEventEndDateSmallerThanOrEqualTo != null) {
            localVarHeaderParams.put("filter_by_event_end_date_smaller_than_or_equal_to", localVarApiClient.parameterToString(filterByEventEndDateSmallerThanOrEqualTo));
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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call financialsEventCosts0GetValidateBeforeCall(String apiKey, BigDecimal filterByEventId, LocalDate filterByEventStartDateGreaterThanOrEqualTo, LocalDate filterByEventStartDateSmallerThanOrEqualTo, LocalDate filterByEventEndDateGreaterThanOrEqualTo, LocalDate filterByEventEndDateSmallerThanOrEqualTo, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'apiKey' is set
        if (apiKey == null) {
            throw new ApiException("Missing the required parameter 'apiKey' when calling financialsEventCosts0Get(Async)");
        }

        return financialsEventCosts0GetCall(apiKey, filterByEventId, filterByEventStartDateGreaterThanOrEqualTo, filterByEventStartDateSmallerThanOrEqualTo, filterByEventEndDateGreaterThanOrEqualTo, filterByEventEndDateSmallerThanOrEqualTo, _callback);

    }

    /**
     * 
     * Retrieve event costs
     * @param apiKey  (required)
     * @param filterByEventId Id of a specific event that you would like to retrieve costs for. (optional)
     * @param filterByEventStartDateGreaterThanOrEqualTo Only include costs for events that have their start date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD (optional)
     * @param filterByEventStartDateSmallerThanOrEqualTo Only include costs for events that have their start date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD (optional)
     * @param filterByEventEndDateGreaterThanOrEqualTo Only include costs for events that have their end date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD (optional)
     * @param filterByEventEndDateSmallerThanOrEqualTo Only include costs for events that have their end date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD (optional)
     * @return String
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public String financialsEventCosts0Get(String apiKey, BigDecimal filterByEventId, LocalDate filterByEventStartDateGreaterThanOrEqualTo, LocalDate filterByEventStartDateSmallerThanOrEqualTo, LocalDate filterByEventEndDateGreaterThanOrEqualTo, LocalDate filterByEventEndDateSmallerThanOrEqualTo) throws ApiException {
        ApiResponse<String> localVarResp = financialsEventCosts0GetWithHttpInfo(apiKey, filterByEventId, filterByEventStartDateGreaterThanOrEqualTo, filterByEventStartDateSmallerThanOrEqualTo, filterByEventEndDateGreaterThanOrEqualTo, filterByEventEndDateSmallerThanOrEqualTo);
        return localVarResp.getData();
    }

    /**
     * 
     * Retrieve event costs
     * @param apiKey  (required)
     * @param filterByEventId Id of a specific event that you would like to retrieve costs for. (optional)
     * @param filterByEventStartDateGreaterThanOrEqualTo Only include costs for events that have their start date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD (optional)
     * @param filterByEventStartDateSmallerThanOrEqualTo Only include costs for events that have their start date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD (optional)
     * @param filterByEventEndDateGreaterThanOrEqualTo Only include costs for events that have their end date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD (optional)
     * @param filterByEventEndDateSmallerThanOrEqualTo Only include costs for events that have their end date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD (optional)
     * @return ApiResponse&lt;String&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<String> financialsEventCosts0GetWithHttpInfo(String apiKey, BigDecimal filterByEventId, LocalDate filterByEventStartDateGreaterThanOrEqualTo, LocalDate filterByEventStartDateSmallerThanOrEqualTo, LocalDate filterByEventEndDateGreaterThanOrEqualTo, LocalDate filterByEventEndDateSmallerThanOrEqualTo) throws ApiException {
        okhttp3.Call localVarCall = financialsEventCosts0GetValidateBeforeCall(apiKey, filterByEventId, filterByEventStartDateGreaterThanOrEqualTo, filterByEventStartDateSmallerThanOrEqualTo, filterByEventEndDateGreaterThanOrEqualTo, filterByEventEndDateSmallerThanOrEqualTo, null);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Retrieve event costs
     * @param apiKey  (required)
     * @param filterByEventId Id of a specific event that you would like to retrieve costs for. (optional)
     * @param filterByEventStartDateGreaterThanOrEqualTo Only include costs for events that have their start date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD (optional)
     * @param filterByEventStartDateSmallerThanOrEqualTo Only include costs for events that have their start date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD (optional)
     * @param filterByEventEndDateGreaterThanOrEqualTo Only include costs for events that have their end date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD (optional)
     * @param filterByEventEndDateSmallerThanOrEqualTo Only include costs for events that have their end date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call financialsEventCosts0GetAsync(String apiKey, BigDecimal filterByEventId, LocalDate filterByEventStartDateGreaterThanOrEqualTo, LocalDate filterByEventStartDateSmallerThanOrEqualTo, LocalDate filterByEventEndDateGreaterThanOrEqualTo, LocalDate filterByEventEndDateSmallerThanOrEqualTo, final ApiCallback<String> _callback) throws ApiException {

        okhttp3.Call localVarCall = financialsEventCosts0GetValidateBeforeCall(apiKey, filterByEventId, filterByEventStartDateGreaterThanOrEqualTo, filterByEventStartDateSmallerThanOrEqualTo, filterByEventEndDateGreaterThanOrEqualTo, filterByEventEndDateSmallerThanOrEqualTo, _callback);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for financialsMiscAnnualExpenseCosts0Get
     * @param apiKey  (required)
     * @param budgetYear The specific budget year that you would like to retrieve miscellaneous annual expense costs for (e.g., 2023). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call financialsMiscAnnualExpenseCosts0GetCall(String apiKey, BigDecimal budgetYear, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/financials/misc_annual_expense_costs";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (apiKey != null) {
            localVarHeaderParams.put("api_key", localVarApiClient.parameterToString(apiKey));
        }

        if (budgetYear != null) {
            localVarHeaderParams.put("budget_year", localVarApiClient.parameterToString(budgetYear));
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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call financialsMiscAnnualExpenseCosts0GetValidateBeforeCall(String apiKey, BigDecimal budgetYear, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'apiKey' is set
        if (apiKey == null) {
            throw new ApiException("Missing the required parameter 'apiKey' when calling financialsMiscAnnualExpenseCosts0Get(Async)");
        }

        return financialsMiscAnnualExpenseCosts0GetCall(apiKey, budgetYear, _callback);

    }

    /**
     * 
     * Retrieve Miscellaneous Annual Expense Costs
     * @param apiKey  (required)
     * @param budgetYear The specific budget year that you would like to retrieve miscellaneous annual expense costs for (e.g., 2023). (optional)
     * @return String
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public String financialsMiscAnnualExpenseCosts0Get(String apiKey, BigDecimal budgetYear) throws ApiException {
        ApiResponse<String> localVarResp = financialsMiscAnnualExpenseCosts0GetWithHttpInfo(apiKey, budgetYear);
        return localVarResp.getData();
    }

    /**
     * 
     * Retrieve Miscellaneous Annual Expense Costs
     * @param apiKey  (required)
     * @param budgetYear The specific budget year that you would like to retrieve miscellaneous annual expense costs for (e.g., 2023). (optional)
     * @return ApiResponse&lt;String&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<String> financialsMiscAnnualExpenseCosts0GetWithHttpInfo(String apiKey, BigDecimal budgetYear) throws ApiException {
        okhttp3.Call localVarCall = financialsMiscAnnualExpenseCosts0GetValidateBeforeCall(apiKey, budgetYear, null);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Retrieve Miscellaneous Annual Expense Costs
     * @param apiKey  (required)
     * @param budgetYear The specific budget year that you would like to retrieve miscellaneous annual expense costs for (e.g., 2023). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call financialsMiscAnnualExpenseCosts0GetAsync(String apiKey, BigDecimal budgetYear, final ApiCallback<String> _callback) throws ApiException {

        okhttp3.Call localVarCall = financialsMiscAnnualExpenseCosts0GetValidateBeforeCall(apiKey, budgetYear, _callback);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
