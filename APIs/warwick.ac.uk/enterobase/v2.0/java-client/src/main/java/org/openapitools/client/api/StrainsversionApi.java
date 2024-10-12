/*
 * Enterobase-API
 *  API for EnteroBase (https://enterobase.warwick.ac.uk)   EnteroBase is a user-friendly online resource, where users can upload their  own sequencing data for de novo assembly by a stream-lined pipeline. The assemblies  are used for calling MLST and wgMLST patterns, allowing users to compare their strains  to publically available genotyping data from other EnteroBase users, GenBank and classical MLST databases.  Click here to find how to get and use an API token: http://bit.ly/1TKlaOU 
 *
 * The version of the OpenAPI document: v2.0
 * Contact: enterobase@warwick.ac.uk
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

public class StrainsversionApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public StrainsversionApi() {
        this(Configuration.getDefaultApiClient());
    }

    public StrainsversionApi(ApiClient apiClient) {
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
     * Build call for apiV20DatabaseStrainsversionGet
     * @param database Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively (required)
     * @param continent  (optional)
     * @param offset Cursor position in results (optional, default to 0)
     * @param sampleAccession  (optional)
     * @param latitude  (optional)
     * @param collectionMonth  (optional)
     * @param antigenicFormulas  (optional)
     * @param strainName  (optional)
     * @param labContact  (optional)
     * @param sortorder Order of search results: asc or desc (optional, default to asc)
     * @param limit Number of results per page (optional, default to 50)
     * @param serotype  (optional)
     * @param region  (optional)
     * @param country  (optional)
     * @param collectionDate  (optional)
     * @param returnAll  (optional)
     * @param onlyFields  (optional)
     * @param sourceNiche  (optional)
     * @param collectionYear  (optional)
     * @param secondarySampleAccession  (optional)
     * @param sourceDetails  (optional)
     * @param substrains  (optional)
     * @param version  (optional)
     * @param sourceType  (optional)
     * @param orderby Field to order by. Default: barcode (optional, default to barcode)
     * @param myStrains  (optional)
     * @param collectionTime  (optional)
     * @param county  (optional)
     * @param uberstrain  (optional)
     * @param comment  (optional)
     * @param longitude  (optional)
     * @param reldate  (optional)
     * @param assemblyBarcode  (optional)
     * @param barcode Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA (optional)
     * @param postcode  (optional)
     * @param city  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List of strainsversion objects </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Unauthorised access for this specific resource </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV20DatabaseStrainsversionGetCall(String database, String continent, Integer offset, String sampleAccession, Float latitude, Integer collectionMonth, String antigenicFormulas, String strainName, String labContact, String sortorder, Integer limit, String serotype, String region, String country, Integer collectionDate, Boolean returnAll, List<String> onlyFields, String sourceNiche, Integer collectionYear, String secondarySampleAccession, String sourceDetails, Boolean substrains, Integer version, String sourceType, String orderby, Boolean myStrains, String collectionTime, String county, String uberstrain, String comment, Float longitude, Integer reldate, String assemblyBarcode, List<String> barcode, String postcode, String city, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v2.0/{database}/strainsversion"
            .replace("{" + "database" + "}", localVarApiClient.escapeString(database.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (continent != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("continent", continent));
        }

        if (offset != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("offset", offset));
        }

        if (sampleAccession != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sample_accession", sampleAccession));
        }

        if (latitude != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("latitude", latitude));
        }

        if (collectionMonth != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("collection_month", collectionMonth));
        }

        if (antigenicFormulas != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("antigenic_formulas", antigenicFormulas));
        }

        if (strainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("strain_name", strainName));
        }

        if (labContact != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("lab_contact", labContact));
        }

        if (sortorder != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sortorder", sortorder));
        }

        if (limit != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("limit", limit));
        }

        if (serotype != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("serotype", serotype));
        }

        if (region != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("region", region));
        }

        if (country != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("country", country));
        }

        if (collectionDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("collection_date", collectionDate));
        }

        if (returnAll != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("return_all", returnAll));
        }

        if (onlyFields != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("multi", "only_fields", onlyFields));
        }

        if (sourceNiche != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("source_niche", sourceNiche));
        }

        if (collectionYear != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("collection_year", collectionYear));
        }

        if (secondarySampleAccession != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("secondary_sample_accession", secondarySampleAccession));
        }

        if (sourceDetails != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("source_details", sourceDetails));
        }

        if (substrains != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("substrains", substrains));
        }

        if (version != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("version", version));
        }

        if (sourceType != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("source_type", sourceType));
        }

        if (orderby != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("orderby", orderby));
        }

        if (myStrains != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("my_strains", myStrains));
        }

        if (collectionTime != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("collection_time", collectionTime));
        }

        if (county != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("county", county));
        }

        if (uberstrain != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("uberstrain", uberstrain));
        }

        if (comment != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("comment", comment));
        }

        if (longitude != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("longitude", longitude));
        }

        if (reldate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("reldate", reldate));
        }

        if (assemblyBarcode != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("assembly_barcode", assemblyBarcode));
        }

        if (barcode != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("multi", "barcode", barcode));
        }

        if (postcode != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("postcode", postcode));
        }

        if (city != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("city", city));
        }

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
    private okhttp3.Call apiV20DatabaseStrainsversionGetValidateBeforeCall(String database, String continent, Integer offset, String sampleAccession, Float latitude, Integer collectionMonth, String antigenicFormulas, String strainName, String labContact, String sortorder, Integer limit, String serotype, String region, String country, Integer collectionDate, Boolean returnAll, List<String> onlyFields, String sourceNiche, Integer collectionYear, String secondarySampleAccession, String sourceDetails, Boolean substrains, Integer version, String sourceType, String orderby, Boolean myStrains, String collectionTime, String county, String uberstrain, String comment, Float longitude, Integer reldate, String assemblyBarcode, List<String> barcode, String postcode, String city, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'database' is set
        if (database == null) {
            throw new ApiException("Missing the required parameter 'database' when calling apiV20DatabaseStrainsversionGet(Async)");
        }

        return apiV20DatabaseStrainsversionGetCall(database, continent, offset, sampleAccession, latitude, collectionMonth, antigenicFormulas, strainName, labContact, sortorder, limit, serotype, region, country, collectionDate, returnAll, onlyFields, sourceNiche, collectionYear, secondarySampleAccession, sourceDetails, substrains, version, sourceType, orderby, myStrains, collectionTime, county, uberstrain, comment, longitude, reldate, assemblyBarcode, barcode, postcode, city, _callback);

    }

    /**
     * 
     * Strain previous metadata
     * @param database Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively (required)
     * @param continent  (optional)
     * @param offset Cursor position in results (optional, default to 0)
     * @param sampleAccession  (optional)
     * @param latitude  (optional)
     * @param collectionMonth  (optional)
     * @param antigenicFormulas  (optional)
     * @param strainName  (optional)
     * @param labContact  (optional)
     * @param sortorder Order of search results: asc or desc (optional, default to asc)
     * @param limit Number of results per page (optional, default to 50)
     * @param serotype  (optional)
     * @param region  (optional)
     * @param country  (optional)
     * @param collectionDate  (optional)
     * @param returnAll  (optional)
     * @param onlyFields  (optional)
     * @param sourceNiche  (optional)
     * @param collectionYear  (optional)
     * @param secondarySampleAccession  (optional)
     * @param sourceDetails  (optional)
     * @param substrains  (optional)
     * @param version  (optional)
     * @param sourceType  (optional)
     * @param orderby Field to order by. Default: barcode (optional, default to barcode)
     * @param myStrains  (optional)
     * @param collectionTime  (optional)
     * @param county  (optional)
     * @param uberstrain  (optional)
     * @param comment  (optional)
     * @param longitude  (optional)
     * @param reldate  (optional)
     * @param assemblyBarcode  (optional)
     * @param barcode Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA (optional)
     * @param postcode  (optional)
     * @param city  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List of strainsversion objects </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Unauthorised access for this specific resource </td><td>  -  </td></tr>
     </table>
     */
    public void apiV20DatabaseStrainsversionGet(String database, String continent, Integer offset, String sampleAccession, Float latitude, Integer collectionMonth, String antigenicFormulas, String strainName, String labContact, String sortorder, Integer limit, String serotype, String region, String country, Integer collectionDate, Boolean returnAll, List<String> onlyFields, String sourceNiche, Integer collectionYear, String secondarySampleAccession, String sourceDetails, Boolean substrains, Integer version, String sourceType, String orderby, Boolean myStrains, String collectionTime, String county, String uberstrain, String comment, Float longitude, Integer reldate, String assemblyBarcode, List<String> barcode, String postcode, String city) throws ApiException {
        apiV20DatabaseStrainsversionGetWithHttpInfo(database, continent, offset, sampleAccession, latitude, collectionMonth, antigenicFormulas, strainName, labContact, sortorder, limit, serotype, region, country, collectionDate, returnAll, onlyFields, sourceNiche, collectionYear, secondarySampleAccession, sourceDetails, substrains, version, sourceType, orderby, myStrains, collectionTime, county, uberstrain, comment, longitude, reldate, assemblyBarcode, barcode, postcode, city);
    }

    /**
     * 
     * Strain previous metadata
     * @param database Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively (required)
     * @param continent  (optional)
     * @param offset Cursor position in results (optional, default to 0)
     * @param sampleAccession  (optional)
     * @param latitude  (optional)
     * @param collectionMonth  (optional)
     * @param antigenicFormulas  (optional)
     * @param strainName  (optional)
     * @param labContact  (optional)
     * @param sortorder Order of search results: asc or desc (optional, default to asc)
     * @param limit Number of results per page (optional, default to 50)
     * @param serotype  (optional)
     * @param region  (optional)
     * @param country  (optional)
     * @param collectionDate  (optional)
     * @param returnAll  (optional)
     * @param onlyFields  (optional)
     * @param sourceNiche  (optional)
     * @param collectionYear  (optional)
     * @param secondarySampleAccession  (optional)
     * @param sourceDetails  (optional)
     * @param substrains  (optional)
     * @param version  (optional)
     * @param sourceType  (optional)
     * @param orderby Field to order by. Default: barcode (optional, default to barcode)
     * @param myStrains  (optional)
     * @param collectionTime  (optional)
     * @param county  (optional)
     * @param uberstrain  (optional)
     * @param comment  (optional)
     * @param longitude  (optional)
     * @param reldate  (optional)
     * @param assemblyBarcode  (optional)
     * @param barcode Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA (optional)
     * @param postcode  (optional)
     * @param city  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List of strainsversion objects </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Unauthorised access for this specific resource </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiV20DatabaseStrainsversionGetWithHttpInfo(String database, String continent, Integer offset, String sampleAccession, Float latitude, Integer collectionMonth, String antigenicFormulas, String strainName, String labContact, String sortorder, Integer limit, String serotype, String region, String country, Integer collectionDate, Boolean returnAll, List<String> onlyFields, String sourceNiche, Integer collectionYear, String secondarySampleAccession, String sourceDetails, Boolean substrains, Integer version, String sourceType, String orderby, Boolean myStrains, String collectionTime, String county, String uberstrain, String comment, Float longitude, Integer reldate, String assemblyBarcode, List<String> barcode, String postcode, String city) throws ApiException {
        okhttp3.Call localVarCall = apiV20DatabaseStrainsversionGetValidateBeforeCall(database, continent, offset, sampleAccession, latitude, collectionMonth, antigenicFormulas, strainName, labContact, sortorder, limit, serotype, region, country, collectionDate, returnAll, onlyFields, sourceNiche, collectionYear, secondarySampleAccession, sourceDetails, substrains, version, sourceType, orderby, myStrains, collectionTime, county, uberstrain, comment, longitude, reldate, assemblyBarcode, barcode, postcode, city, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * Strain previous metadata
     * @param database Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively (required)
     * @param continent  (optional)
     * @param offset Cursor position in results (optional, default to 0)
     * @param sampleAccession  (optional)
     * @param latitude  (optional)
     * @param collectionMonth  (optional)
     * @param antigenicFormulas  (optional)
     * @param strainName  (optional)
     * @param labContact  (optional)
     * @param sortorder Order of search results: asc or desc (optional, default to asc)
     * @param limit Number of results per page (optional, default to 50)
     * @param serotype  (optional)
     * @param region  (optional)
     * @param country  (optional)
     * @param collectionDate  (optional)
     * @param returnAll  (optional)
     * @param onlyFields  (optional)
     * @param sourceNiche  (optional)
     * @param collectionYear  (optional)
     * @param secondarySampleAccession  (optional)
     * @param sourceDetails  (optional)
     * @param substrains  (optional)
     * @param version  (optional)
     * @param sourceType  (optional)
     * @param orderby Field to order by. Default: barcode (optional, default to barcode)
     * @param myStrains  (optional)
     * @param collectionTime  (optional)
     * @param county  (optional)
     * @param uberstrain  (optional)
     * @param comment  (optional)
     * @param longitude  (optional)
     * @param reldate  (optional)
     * @param assemblyBarcode  (optional)
     * @param barcode Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA (optional)
     * @param postcode  (optional)
     * @param city  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List of strainsversion objects </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Unauthorised access for this specific resource </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV20DatabaseStrainsversionGetAsync(String database, String continent, Integer offset, String sampleAccession, Float latitude, Integer collectionMonth, String antigenicFormulas, String strainName, String labContact, String sortorder, Integer limit, String serotype, String region, String country, Integer collectionDate, Boolean returnAll, List<String> onlyFields, String sourceNiche, Integer collectionYear, String secondarySampleAccession, String sourceDetails, Boolean substrains, Integer version, String sourceType, String orderby, Boolean myStrains, String collectionTime, String county, String uberstrain, String comment, Float longitude, Integer reldate, String assemblyBarcode, List<String> barcode, String postcode, String city, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV20DatabaseStrainsversionGetValidateBeforeCall(database, continent, offset, sampleAccession, latitude, collectionMonth, antigenicFormulas, strainName, labContact, sortorder, limit, serotype, region, country, collectionDate, returnAll, onlyFields, sourceNiche, collectionYear, secondarySampleAccession, sourceDetails, substrains, version, sourceType, orderby, myStrains, collectionTime, county, uberstrain, comment, longitude, reldate, assemblyBarcode, barcode, postcode, city, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
