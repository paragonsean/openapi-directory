/*
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
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


import org.openapitools.client.model.CompanyCreditDataCreditLimitSearchResultsInterface;
import org.openapitools.client.model.ErrorResponse;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CompanyCreditsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public CompanyCreditsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public CompanyCreditsApi(ApiClient apiClient) {
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
     * Build call for companyCreditCreditLimitRepositoryV1GetListGet
     * @param searchCriteriaFilterGroups0Filters0Field Field (optional)
     * @param searchCriteriaFilterGroups0Filters0Value Value (optional)
     * @param searchCriteriaFilterGroups0Filters0ConditionType Condition type (optional)
     * @param searchCriteriaSortOrders0Field Sorting field. (optional)
     * @param searchCriteriaSortOrders0Direction Sorting direction. (optional)
     * @param searchCriteriaPageSize Page size. (optional)
     * @param searchCriteriaCurrentPage Current page. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 Success. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> 401 Unauthorized </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server error </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companyCreditCreditLimitRepositoryV1GetListGetCall(String searchCriteriaFilterGroups0Filters0Field, String searchCriteriaFilterGroups0Filters0Value, String searchCriteriaFilterGroups0Filters0ConditionType, String searchCriteriaSortOrders0Field, String searchCriteriaSortOrders0Direction, Integer searchCriteriaPageSize, Integer searchCriteriaCurrentPage, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/V1/companyCredits/";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (searchCriteriaFilterGroups0Filters0Field != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("searchCriteria[filterGroups][0][filters][0][field]", searchCriteriaFilterGroups0Filters0Field));
        }

        if (searchCriteriaFilterGroups0Filters0Value != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("searchCriteria[filterGroups][0][filters][0][value]", searchCriteriaFilterGroups0Filters0Value));
        }

        if (searchCriteriaFilterGroups0Filters0ConditionType != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("searchCriteria[filterGroups][0][filters][0][conditionType]", searchCriteriaFilterGroups0Filters0ConditionType));
        }

        if (searchCriteriaSortOrders0Field != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("searchCriteria[sortOrders][0][field]", searchCriteriaSortOrders0Field));
        }

        if (searchCriteriaSortOrders0Direction != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("searchCriteria[sortOrders][0][direction]", searchCriteriaSortOrders0Direction));
        }

        if (searchCriteriaPageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("searchCriteria[pageSize]", searchCriteriaPageSize));
        }

        if (searchCriteriaCurrentPage != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("searchCriteria[currentPage]", searchCriteriaCurrentPage));
        }

        final String[] localVarAccepts = {
            "application/json",
            "application/xml"
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
    private okhttp3.Call companyCreditCreditLimitRepositoryV1GetListGetValidateBeforeCall(String searchCriteriaFilterGroups0Filters0Field, String searchCriteriaFilterGroups0Filters0Value, String searchCriteriaFilterGroups0Filters0ConditionType, String searchCriteriaSortOrders0Field, String searchCriteriaSortOrders0Direction, Integer searchCriteriaPageSize, Integer searchCriteriaCurrentPage, final ApiCallback _callback) throws ApiException {
        return companyCreditCreditLimitRepositoryV1GetListGetCall(searchCriteriaFilterGroups0Filters0Field, searchCriteriaFilterGroups0Filters0Value, searchCriteriaFilterGroups0Filters0ConditionType, searchCriteriaSortOrders0Field, searchCriteriaSortOrders0Direction, searchCriteriaPageSize, searchCriteriaCurrentPage, _callback);

    }

    /**
     * companyCredits/
     * Returns the list of credits for specified companies.
     * @param searchCriteriaFilterGroups0Filters0Field Field (optional)
     * @param searchCriteriaFilterGroups0Filters0Value Value (optional)
     * @param searchCriteriaFilterGroups0Filters0ConditionType Condition type (optional)
     * @param searchCriteriaSortOrders0Field Sorting field. (optional)
     * @param searchCriteriaSortOrders0Direction Sorting direction. (optional)
     * @param searchCriteriaPageSize Page size. (optional)
     * @param searchCriteriaCurrentPage Current page. (optional)
     * @return CompanyCreditDataCreditLimitSearchResultsInterface
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 Success. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> 401 Unauthorized </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server error </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public CompanyCreditDataCreditLimitSearchResultsInterface companyCreditCreditLimitRepositoryV1GetListGet(String searchCriteriaFilterGroups0Filters0Field, String searchCriteriaFilterGroups0Filters0Value, String searchCriteriaFilterGroups0Filters0ConditionType, String searchCriteriaSortOrders0Field, String searchCriteriaSortOrders0Direction, Integer searchCriteriaPageSize, Integer searchCriteriaCurrentPage) throws ApiException {
        ApiResponse<CompanyCreditDataCreditLimitSearchResultsInterface> localVarResp = companyCreditCreditLimitRepositoryV1GetListGetWithHttpInfo(searchCriteriaFilterGroups0Filters0Field, searchCriteriaFilterGroups0Filters0Value, searchCriteriaFilterGroups0Filters0ConditionType, searchCriteriaSortOrders0Field, searchCriteriaSortOrders0Direction, searchCriteriaPageSize, searchCriteriaCurrentPage);
        return localVarResp.getData();
    }

    /**
     * companyCredits/
     * Returns the list of credits for specified companies.
     * @param searchCriteriaFilterGroups0Filters0Field Field (optional)
     * @param searchCriteriaFilterGroups0Filters0Value Value (optional)
     * @param searchCriteriaFilterGroups0Filters0ConditionType Condition type (optional)
     * @param searchCriteriaSortOrders0Field Sorting field. (optional)
     * @param searchCriteriaSortOrders0Direction Sorting direction. (optional)
     * @param searchCriteriaPageSize Page size. (optional)
     * @param searchCriteriaCurrentPage Current page. (optional)
     * @return ApiResponse&lt;CompanyCreditDataCreditLimitSearchResultsInterface&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 Success. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> 401 Unauthorized </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server error </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CompanyCreditDataCreditLimitSearchResultsInterface> companyCreditCreditLimitRepositoryV1GetListGetWithHttpInfo(String searchCriteriaFilterGroups0Filters0Field, String searchCriteriaFilterGroups0Filters0Value, String searchCriteriaFilterGroups0Filters0ConditionType, String searchCriteriaSortOrders0Field, String searchCriteriaSortOrders0Direction, Integer searchCriteriaPageSize, Integer searchCriteriaCurrentPage) throws ApiException {
        okhttp3.Call localVarCall = companyCreditCreditLimitRepositoryV1GetListGetValidateBeforeCall(searchCriteriaFilterGroups0Filters0Field, searchCriteriaFilterGroups0Filters0Value, searchCriteriaFilterGroups0Filters0ConditionType, searchCriteriaSortOrders0Field, searchCriteriaSortOrders0Direction, searchCriteriaPageSize, searchCriteriaCurrentPage, null);
        Type localVarReturnType = new TypeToken<CompanyCreditDataCreditLimitSearchResultsInterface>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * companyCredits/ (asynchronously)
     * Returns the list of credits for specified companies.
     * @param searchCriteriaFilterGroups0Filters0Field Field (optional)
     * @param searchCriteriaFilterGroups0Filters0Value Value (optional)
     * @param searchCriteriaFilterGroups0Filters0ConditionType Condition type (optional)
     * @param searchCriteriaSortOrders0Field Sorting field. (optional)
     * @param searchCriteriaSortOrders0Direction Sorting direction. (optional)
     * @param searchCriteriaPageSize Page size. (optional)
     * @param searchCriteriaCurrentPage Current page. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 Success. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> 401 Unauthorized </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server error </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companyCreditCreditLimitRepositoryV1GetListGetAsync(String searchCriteriaFilterGroups0Filters0Field, String searchCriteriaFilterGroups0Filters0Value, String searchCriteriaFilterGroups0Filters0ConditionType, String searchCriteriaSortOrders0Field, String searchCriteriaSortOrders0Direction, Integer searchCriteriaPageSize, Integer searchCriteriaCurrentPage, final ApiCallback<CompanyCreditDataCreditLimitSearchResultsInterface> _callback) throws ApiException {

        okhttp3.Call localVarCall = companyCreditCreditLimitRepositoryV1GetListGetValidateBeforeCall(searchCriteriaFilterGroups0Filters0Field, searchCriteriaFilterGroups0Filters0Value, searchCriteriaFilterGroups0Filters0ConditionType, searchCriteriaSortOrders0Field, searchCriteriaSortOrders0Direction, searchCriteriaPageSize, searchCriteriaCurrentPage, _callback);
        Type localVarReturnType = new TypeToken<CompanyCreditDataCreditLimitSearchResultsInterface>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
