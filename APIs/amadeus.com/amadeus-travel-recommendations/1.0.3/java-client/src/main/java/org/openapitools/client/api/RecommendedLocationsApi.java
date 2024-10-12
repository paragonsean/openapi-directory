/*
 * Travel Recommendations API
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 1.0.3
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


import org.openapitools.client.model.Error400;
import org.openapitools.client.model.Error500;
import org.openapitools.client.model.GetRecommendedLocation200Response;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class RecommendedLocationsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public RecommendedLocationsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public RecommendedLocationsApi(ApiClient apiClient) {
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
     * Build call for getRecommendedLocation
     * @param cityCodes City used by the algorythm to recommend new destination. Several cities can be specified using comma.  City codes follow [IATA standard](http://www.iata.org/publications/Pages/code-search.aspx) (required)
     * @param travelerCountryCode Origin country of the traveler following [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code format (e.g. US) (optional, default to FR)
     * @param destinationCountryCodes List of country the traveler want to visit, separated with comma.  Country codes follow [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code format (e.g. US) (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful reply </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> code    | title                                  ------- | -------------------------------------  477     | INVALID FORMAT 572     | INVALID OPTION                             32171   | MANDATORY DATA MISSING  </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getRecommendedLocationCall(String cityCodes, String travelerCountryCode, String destinationCountryCodes, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/reference-data/recommended-locations";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (cityCodes != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("cityCodes", cityCodes));
        }

        if (travelerCountryCode != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("travelerCountryCode", travelerCountryCode));
        }

        if (destinationCountryCodes != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("destinationCountryCodes", destinationCountryCodes));
        }

        final String[] localVarAccepts = {
            "application/vnd.amadeus+json"
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
    private okhttp3.Call getRecommendedLocationValidateBeforeCall(String cityCodes, String travelerCountryCode, String destinationCountryCodes, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'cityCodes' is set
        if (cityCodes == null) {
            throw new ApiException("Missing the required parameter 'cityCodes' when calling getRecommendedLocation(Async)");
        }

        return getRecommendedLocationCall(cityCodes, travelerCountryCode, destinationCountryCodes, _callback);

    }

    /**
     * GET recommended destinations
     * 
     * @param cityCodes City used by the algorythm to recommend new destination. Several cities can be specified using comma.  City codes follow [IATA standard](http://www.iata.org/publications/Pages/code-search.aspx) (required)
     * @param travelerCountryCode Origin country of the traveler following [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code format (e.g. US) (optional, default to FR)
     * @param destinationCountryCodes List of country the traveler want to visit, separated with comma.  Country codes follow [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code format (e.g. US) (optional)
     * @return GetRecommendedLocation200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful reply </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> code    | title                                  ------- | -------------------------------------  477     | INVALID FORMAT 572     | INVALID OPTION                             32171   | MANDATORY DATA MISSING  </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public GetRecommendedLocation200Response getRecommendedLocation(String cityCodes, String travelerCountryCode, String destinationCountryCodes) throws ApiException {
        ApiResponse<GetRecommendedLocation200Response> localVarResp = getRecommendedLocationWithHttpInfo(cityCodes, travelerCountryCode, destinationCountryCodes);
        return localVarResp.getData();
    }

    /**
     * GET recommended destinations
     * 
     * @param cityCodes City used by the algorythm to recommend new destination. Several cities can be specified using comma.  City codes follow [IATA standard](http://www.iata.org/publications/Pages/code-search.aspx) (required)
     * @param travelerCountryCode Origin country of the traveler following [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code format (e.g. US) (optional, default to FR)
     * @param destinationCountryCodes List of country the traveler want to visit, separated with comma.  Country codes follow [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code format (e.g. US) (optional)
     * @return ApiResponse&lt;GetRecommendedLocation200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful reply </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> code    | title                                  ------- | -------------------------------------  477     | INVALID FORMAT 572     | INVALID OPTION                             32171   | MANDATORY DATA MISSING  </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetRecommendedLocation200Response> getRecommendedLocationWithHttpInfo(String cityCodes, String travelerCountryCode, String destinationCountryCodes) throws ApiException {
        okhttp3.Call localVarCall = getRecommendedLocationValidateBeforeCall(cityCodes, travelerCountryCode, destinationCountryCodes, null);
        Type localVarReturnType = new TypeToken<GetRecommendedLocation200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * GET recommended destinations (asynchronously)
     * 
     * @param cityCodes City used by the algorythm to recommend new destination. Several cities can be specified using comma.  City codes follow [IATA standard](http://www.iata.org/publications/Pages/code-search.aspx) (required)
     * @param travelerCountryCode Origin country of the traveler following [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code format (e.g. US) (optional, default to FR)
     * @param destinationCountryCodes List of country the traveler want to visit, separated with comma.  Country codes follow [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code format (e.g. US) (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful reply </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> code    | title                                  ------- | -------------------------------------  477     | INVALID FORMAT 572     | INVALID OPTION                             32171   | MANDATORY DATA MISSING  </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getRecommendedLocationAsync(String cityCodes, String travelerCountryCode, String destinationCountryCodes, final ApiCallback<GetRecommendedLocation200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getRecommendedLocationValidateBeforeCall(cityCodes, travelerCountryCode, destinationCountryCodes, _callback);
        Type localVarReturnType = new TypeToken<GetRecommendedLocation200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
