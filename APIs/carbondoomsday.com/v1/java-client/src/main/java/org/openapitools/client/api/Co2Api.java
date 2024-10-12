/*
 * CarbonDoomsDay
 * A real-time RESTish web API for worldwide carbon dioxide levels.
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
import org.openapitools.client.model.CO2;
import org.openapitools.client.model.Co2List200Response;
import java.time.LocalDate;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Co2Api {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public Co2Api() {
        this(Configuration.getDefaultApiClient());
    }

    public Co2Api(ApiClient apiClient) {
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
     * Build call for co2List
     * @param ppm  (optional)
     * @param date  (optional)
     * @param dateRange Multiple values may be separated by commas. (optional)
     * @param ordering Which field to use when ordering the results. (optional)
     * @param page A page number within the paginated result set. (optional)
     * @param limit Number of results to return per page. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call co2ListCall(BigDecimal ppm, String date, String dateRange, String ordering, Integer page, Integer limit, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/co2/";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (ppm != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("ppm", ppm));
        }

        if (date != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("date", date));
        }

        if (dateRange != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("date__range", dateRange));
        }

        if (ordering != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("ordering", ordering));
        }

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
        }

        if (limit != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("limit", limit));
        }

        final String[] localVarAccepts = {
            "application/json",
            "text/csv"
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

        String[] localVarAuthNames = new String[] { "basic" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call co2ListValidateBeforeCall(BigDecimal ppm, String date, String dateRange, String ordering, Integer page, Integer limit, final ApiCallback _callback) throws ApiException {
        return co2ListCall(ppm, date, dateRange, ordering, page, limit, _callback);

    }

    /**
     * 
     * CO2 measurements from the Mauna Loa observatory.  This data is made available through the good work of the people at the Mauna Loa observatory. Their release notes say:      These data are made freely available to the public and the scientific     community in the belief that their wide dissemination will lead to greater     understanding and new scientific insights.  We currently scrape the following sources:    * [co2_mlo_weekly.csv]   * [co2_mlo_surface-insitu_1_ccgg_DailyData.txt]   * [weekly_mlo.csv]  We have daily CO2 measurements as far back as 1958.  Learn about using pagination via [the 3rd party documentation].  [co2_mlo_weekly.csv]: https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2_mlo_weekly.csv [co2_mlo_surface-insitu_1_ccgg_DailyData.txt]: ftp://aftp.cmdl.noaa.gov/data/trace_gases/co2/in-situ/surface/mlo/co2_mlo_surface-insitu_1_ccgg_DailyData.txt [weekly_mlo.csv]: http://scrippsco2.ucsd.edu/sites/default/files/data/in_situ_co2/weekly_mlo.csv [the 3rd party documentation]: http://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination
     * @param ppm  (optional)
     * @param date  (optional)
     * @param dateRange Multiple values may be separated by commas. (optional)
     * @param ordering Which field to use when ordering the results. (optional)
     * @param page A page number within the paginated result set. (optional)
     * @param limit Number of results to return per page. (optional)
     * @return Co2List200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public Co2List200Response co2List(BigDecimal ppm, String date, String dateRange, String ordering, Integer page, Integer limit) throws ApiException {
        ApiResponse<Co2List200Response> localVarResp = co2ListWithHttpInfo(ppm, date, dateRange, ordering, page, limit);
        return localVarResp.getData();
    }

    /**
     * 
     * CO2 measurements from the Mauna Loa observatory.  This data is made available through the good work of the people at the Mauna Loa observatory. Their release notes say:      These data are made freely available to the public and the scientific     community in the belief that their wide dissemination will lead to greater     understanding and new scientific insights.  We currently scrape the following sources:    * [co2_mlo_weekly.csv]   * [co2_mlo_surface-insitu_1_ccgg_DailyData.txt]   * [weekly_mlo.csv]  We have daily CO2 measurements as far back as 1958.  Learn about using pagination via [the 3rd party documentation].  [co2_mlo_weekly.csv]: https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2_mlo_weekly.csv [co2_mlo_surface-insitu_1_ccgg_DailyData.txt]: ftp://aftp.cmdl.noaa.gov/data/trace_gases/co2/in-situ/surface/mlo/co2_mlo_surface-insitu_1_ccgg_DailyData.txt [weekly_mlo.csv]: http://scrippsco2.ucsd.edu/sites/default/files/data/in_situ_co2/weekly_mlo.csv [the 3rd party documentation]: http://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination
     * @param ppm  (optional)
     * @param date  (optional)
     * @param dateRange Multiple values may be separated by commas. (optional)
     * @param ordering Which field to use when ordering the results. (optional)
     * @param page A page number within the paginated result set. (optional)
     * @param limit Number of results to return per page. (optional)
     * @return ApiResponse&lt;Co2List200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Co2List200Response> co2ListWithHttpInfo(BigDecimal ppm, String date, String dateRange, String ordering, Integer page, Integer limit) throws ApiException {
        okhttp3.Call localVarCall = co2ListValidateBeforeCall(ppm, date, dateRange, ordering, page, limit, null);
        Type localVarReturnType = new TypeToken<Co2List200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * CO2 measurements from the Mauna Loa observatory.  This data is made available through the good work of the people at the Mauna Loa observatory. Their release notes say:      These data are made freely available to the public and the scientific     community in the belief that their wide dissemination will lead to greater     understanding and new scientific insights.  We currently scrape the following sources:    * [co2_mlo_weekly.csv]   * [co2_mlo_surface-insitu_1_ccgg_DailyData.txt]   * [weekly_mlo.csv]  We have daily CO2 measurements as far back as 1958.  Learn about using pagination via [the 3rd party documentation].  [co2_mlo_weekly.csv]: https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2_mlo_weekly.csv [co2_mlo_surface-insitu_1_ccgg_DailyData.txt]: ftp://aftp.cmdl.noaa.gov/data/trace_gases/co2/in-situ/surface/mlo/co2_mlo_surface-insitu_1_ccgg_DailyData.txt [weekly_mlo.csv]: http://scrippsco2.ucsd.edu/sites/default/files/data/in_situ_co2/weekly_mlo.csv [the 3rd party documentation]: http://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination
     * @param ppm  (optional)
     * @param date  (optional)
     * @param dateRange Multiple values may be separated by commas. (optional)
     * @param ordering Which field to use when ordering the results. (optional)
     * @param page A page number within the paginated result set. (optional)
     * @param limit Number of results to return per page. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call co2ListAsync(BigDecimal ppm, String date, String dateRange, String ordering, Integer page, Integer limit, final ApiCallback<Co2List200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = co2ListValidateBeforeCall(ppm, date, dateRange, ordering, page, limit, _callback);
        Type localVarReturnType = new TypeToken<Co2List200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for co2Read
     * @param date  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call co2ReadCall(LocalDate date, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/co2/{date}/"
            .replace("{" + "date" + "}", localVarApiClient.escapeString(date.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json",
            "text/csv"
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

        String[] localVarAuthNames = new String[] { "basic" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call co2ReadValidateBeforeCall(LocalDate date, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'date' is set
        if (date == null) {
            throw new ApiException("Missing the required parameter 'date' when calling co2Read(Async)");
        }

        return co2ReadCall(date, _callback);

    }

    /**
     * 
     * CO2 measurements from the Mauna Loa observatory.  This data is made available through the good work of the people at the Mauna Loa observatory. Their release notes say:      These data are made freely available to the public and the scientific     community in the belief that their wide dissemination will lead to greater     understanding and new scientific insights.  We currently scrape the following sources:    * [co2_mlo_weekly.csv]   * [co2_mlo_surface-insitu_1_ccgg_DailyData.txt]   * [weekly_mlo.csv]  We have daily CO2 measurements as far back as 1958.  Learn about using pagination via [the 3rd party documentation].  [co2_mlo_weekly.csv]: https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2_mlo_weekly.csv [co2_mlo_surface-insitu_1_ccgg_DailyData.txt]: ftp://aftp.cmdl.noaa.gov/data/trace_gases/co2/in-situ/surface/mlo/co2_mlo_surface-insitu_1_ccgg_DailyData.txt [weekly_mlo.csv]: http://scrippsco2.ucsd.edu/sites/default/files/data/in_situ_co2/weekly_mlo.csv [the 3rd party documentation]: http://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination
     * @param date  (required)
     * @return CO2
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public CO2 co2Read(LocalDate date) throws ApiException {
        ApiResponse<CO2> localVarResp = co2ReadWithHttpInfo(date);
        return localVarResp.getData();
    }

    /**
     * 
     * CO2 measurements from the Mauna Loa observatory.  This data is made available through the good work of the people at the Mauna Loa observatory. Their release notes say:      These data are made freely available to the public and the scientific     community in the belief that their wide dissemination will lead to greater     understanding and new scientific insights.  We currently scrape the following sources:    * [co2_mlo_weekly.csv]   * [co2_mlo_surface-insitu_1_ccgg_DailyData.txt]   * [weekly_mlo.csv]  We have daily CO2 measurements as far back as 1958.  Learn about using pagination via [the 3rd party documentation].  [co2_mlo_weekly.csv]: https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2_mlo_weekly.csv [co2_mlo_surface-insitu_1_ccgg_DailyData.txt]: ftp://aftp.cmdl.noaa.gov/data/trace_gases/co2/in-situ/surface/mlo/co2_mlo_surface-insitu_1_ccgg_DailyData.txt [weekly_mlo.csv]: http://scrippsco2.ucsd.edu/sites/default/files/data/in_situ_co2/weekly_mlo.csv [the 3rd party documentation]: http://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination
     * @param date  (required)
     * @return ApiResponse&lt;CO2&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CO2> co2ReadWithHttpInfo(LocalDate date) throws ApiException {
        okhttp3.Call localVarCall = co2ReadValidateBeforeCall(date, null);
        Type localVarReturnType = new TypeToken<CO2>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * CO2 measurements from the Mauna Loa observatory.  This data is made available through the good work of the people at the Mauna Loa observatory. Their release notes say:      These data are made freely available to the public and the scientific     community in the belief that their wide dissemination will lead to greater     understanding and new scientific insights.  We currently scrape the following sources:    * [co2_mlo_weekly.csv]   * [co2_mlo_surface-insitu_1_ccgg_DailyData.txt]   * [weekly_mlo.csv]  We have daily CO2 measurements as far back as 1958.  Learn about using pagination via [the 3rd party documentation].  [co2_mlo_weekly.csv]: https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2_mlo_weekly.csv [co2_mlo_surface-insitu_1_ccgg_DailyData.txt]: ftp://aftp.cmdl.noaa.gov/data/trace_gases/co2/in-situ/surface/mlo/co2_mlo_surface-insitu_1_ccgg_DailyData.txt [weekly_mlo.csv]: http://scrippsco2.ucsd.edu/sites/default/files/data/in_situ_co2/weekly_mlo.csv [the 3rd party documentation]: http://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination
     * @param date  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call co2ReadAsync(LocalDate date, final ApiCallback<CO2> _callback) throws ApiException {

        okhttp3.Call localVarCall = co2ReadValidateBeforeCall(date, _callback);
        Type localVarReturnType = new TypeToken<CO2>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
