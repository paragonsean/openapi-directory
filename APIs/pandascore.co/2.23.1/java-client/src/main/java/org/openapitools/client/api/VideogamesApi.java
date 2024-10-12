/*
 * PandaScore REST API for All Videogames
 *  # Introduction  Whether you're looking to build an official Pandascore integration for your service, or you just want to build something awesome, [we can help you get started](/home).  The API works over the HTTPS protocol, and is accessed from the `api.pandascore.co` domain.  - The current endpoint is [https://api.pandascore.co](https://api.pandascore.co). - All data is sent and received as JSON by default. - Blank fields are included with `null` values instead of being omitted. - All timestamps are returned in ISO-8601 format  ### About this documentation  Clicking on a query parameter like `filter` or `search` will show you the available options: ![filter](/doc/images/query_param_details.jpg)  You can also click on a response to see the detailed response schema: ![response](/doc/images/response_schema.jpg)  ## Events hierarchy  The PandaScore API allows you to access data about eSports events by using a certain structure detailed below.  **Leagues**  Leagues are the top level events. They don't have a date and represent a regular competition. A League is composed of one or several series.   Some League of Legends leagues are: _EU LCS, NA LCS, LCK, etc._   Some Dota 2 leagues are: _ESL One, GESC, The International, PGL, etc._  **Series**  A Serie represents an occurrence of a league event.   The EU LCS league has two series per year: _spring 2017, summer 2017, spring 2016, summer 2016 etc._   Some Dota2 Series examples would be: _Changsha Major, Open Bucharest, Frankfurt, i-League Invitational etc._  **Tournaments**  Tournaments groups all the matches of a serie under \"stages\" and \"groups\".   The tournaments of the EU LCS of summer 2017 are: _Group A, Group B, Playoffs, etc._   Some Dota 2 tournaments are: _Group A, Group B, Playoffs, etc._  **Matches**  Finally we have matches which have two players or teams (depending on the played videogame) and several games (the rounds of the match).   Matches of the group A in the EU LCS of summer 2017 are: _G2 vs FNC, MSF vs NIP, etc._   Matches of the group A in the ESL One, Genting tournamnet are: _Lower Round 1, Quarterfinal, Upper Final, etc._    **Please note that some matches may be listed as \"TBD vs TBD\" if the matchup is not announced yet, for example the date of the Final match is known but the quarterfinal is still being played.**   ![Structure](/doc/images/structure.png)  ## Formats  &lt;!-- The API currently supports the JSON format by default, as well as the XML format. Add the desired extension to your request URL in order to get that format. --&gt; The API currently supports the JSON format by default.  Other formats may be added depending on user needs.  ## Pagination  The Pandascore API paginates all resources on the index method.  Requests that return multiple items will be paginated to 50 items by default. You can specify further pages with the `page[number]` parameter. You can also set a custom page size (up to 100) with the `page[size]` parameter.  The `Link` HTTP response header contains pagination data with `first`, `previous`, `next` and `last` raw page links when available, under the format  ``` Link: &lt;https://api.pandascore.co/{Resource}?page=X+1&gt;; rel=\"next\", &lt;https://api.pandascore.co/{Resource}?page=X-1&gt;; rel=\"prev\", &lt;https://api.pandascore.co/{Resource}?page=1&gt;; rel=\"first\", &lt;https://api.pandascore.co/{Resource}?page=X+n&gt;; rel=\"last\" ```  There is also:  * A `X-Page` header field, which contains the current page. * A `X-Per-Page` header field, which contains the current pagination length. * A `X-Total` header field, which contains the total count of items across all pages.  ## Filtering  The `filter` query parameter can be used to filter a collection by one or several fields for one or several values. The `filter` parameter takes the field to filter as a key, and the values to filter as the value. Multiples values must be comma-separated (`,`).  For example, the following is a request for all the champions with a name matching Twitch or Brand exactly, but only with 21 armor:  ``` GET /lol/champions?filter[name]=Brand,Twitch&amp;filter[armor]=21&amp;token=YOUR_ACCESS_TOKEN ```  ## Range  The `range` parameter is a hash that allows filtering fields by an interval. Only values between the given two comma-separated bounds will be returned. The bounds are inclusive.  For example, the following is a request for all the champions with `hp` within 500 and 1000:  ``` GET /lol/champions?range[hp]=500,1000&amp;token=YOUR_ACCESS_TOKEN ```  ## Search  The `search` parameter is a bit like the `filter` parameter, but it will return all results where the values **contain** the given parameter.  Note: this only works on strings. Searching with integer values is not supported and `filter` or `range` parameters may be better suited for your needs here.  For example, to get all the champions with a name containing `\"twi\"`:  ``` $ curl -sg -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' 'https://api.pandascore.co/lol/champions?search[name]=twi' | jq -S '.[].name' \"Twitch\" \"Twisted Fate\" ```  ## Sorting  All index endpoints support multiple sort fields with comma-separation (`,`); the fields are applied in the order specified.  The sort order for each field is ascending unless it is prefixed with a minus (U+002D HYPHEN-MINUS, “-“), in which case it is descending.  For example, `GET /lol/champions?sort=attackdamage,-name&amp;token=YOUR_ACCESS_TOKEN` will return all the champions sorted by attack damage. Any champions with the same attack damage will then be sorted by their names in descending alphabetical order.  ## Rate limiting  Depending on your current plan, you will have a different rate limit. Your plan and your current request count [are available on your dashboard](https://pandascore.co/settings).  With the **free plan**, you have a limit of 1000 requests per hour, others plans have a limit of 4000 requests per hour. The number of remaining requests is available in the `X-Rate-Limit-Remaining` response header.  Your API key is included in all the examples on this page, so you can test any example right away. **Only you can see this value.**  # Authentication  The authentication on the Pandascore API works with access tokens.  All developers need to [create an account](https://pandascore.co/users/sign_in) before getting started, in order to get an access token. The access token should not be shared.  **Your token can be found and regenerated from [your dashboard](https://pandascore.co/settings).**  The access token can be passed in the URL with the `token` query string parameter, or in the `Authorization: Bearer` header field.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt; 
 *
 * The version of the OpenAPI document: 2.23.1
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


import org.openapitools.client.model.FilterOverLeagues;
import org.openapitools.client.model.FilterOverSeries;
import org.openapitools.client.model.FilterOverShortTournaments;
import org.openapitools.client.model.FilterOverShortVideogameVersions;
import org.openapitools.client.model.GetAdditions400Response;
import org.openapitools.client.model.GetAdditionsPageParameter;
import org.openapitools.client.model.League;
import org.openapitools.client.model.RangeOverLeagues;
import org.openapitools.client.model.RangeOverSeries;
import org.openapitools.client.model.RangeOverShortTournaments;
import org.openapitools.client.model.RangeOverShortVideogameVersions;
import org.openapitools.client.model.SearchOverLeagues;
import org.openapitools.client.model.SearchOverSeries;
import org.openapitools.client.model.SearchOverShortTournaments;
import org.openapitools.client.model.SearchOverShortVideogameVersions;
import org.openapitools.client.model.Serie;
import org.openapitools.client.model.ShortTournament;
import org.openapitools.client.model.ShortVideogameVersion;
import org.openapitools.client.model.Videogame;
import org.openapitools.client.model.VideogameIDOrSlug;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class VideogamesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public VideogamesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public VideogamesApi(ApiClient apiClient) {
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
     * Build call for getVideogames
     * @param page Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; (optional)
     * @param perPage Equivalent to &#x60;page[size]&#x60; (optional, default to 50)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of videogames </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVideogamesCall(GetAdditionsPageParameter page, Integer perPage, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/videogames";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
        }

        if (perPage != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("per_page", perPage));
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

        String[] localVarAuthNames = new String[] { "BearerToken", "QueryToken" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getVideogamesValidateBeforeCall(GetAdditionsPageParameter page, Integer perPage, final ApiCallback _callback) throws ApiException {
        return getVideogamesCall(page, perPage, _callback);

    }

    /**
     * List videogames
     * List videogames
     * @param page Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; (optional)
     * @param perPage Equivalent to &#x60;page[size]&#x60; (optional, default to 50)
     * @return List&lt;Videogame&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of videogames </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
     </table>
     */
    public List<Videogame> getVideogames(GetAdditionsPageParameter page, Integer perPage) throws ApiException {
        ApiResponse<List<Videogame>> localVarResp = getVideogamesWithHttpInfo(page, perPage);
        return localVarResp.getData();
    }

    /**
     * List videogames
     * List videogames
     * @param page Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; (optional)
     * @param perPage Equivalent to &#x60;page[size]&#x60; (optional, default to 50)
     * @return ApiResponse&lt;List&lt;Videogame&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of videogames </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<Videogame>> getVideogamesWithHttpInfo(GetAdditionsPageParameter page, Integer perPage) throws ApiException {
        okhttp3.Call localVarCall = getVideogamesValidateBeforeCall(page, perPage, null);
        Type localVarReturnType = new TypeToken<List<Videogame>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List videogames (asynchronously)
     * List videogames
     * @param page Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; (optional)
     * @param perPage Equivalent to &#x60;page[size]&#x60; (optional, default to 50)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of videogames </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVideogamesAsync(GetAdditionsPageParameter page, Integer perPage, final ApiCallback<List<Videogame>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getVideogamesValidateBeforeCall(page, perPage, _callback);
        Type localVarReturnType = new TypeToken<List<Videogame>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getVideogamesVideogameIdOrSlug
     * @param videogameIdOrSlug A videogame ID or slug (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A videogame </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVideogamesVideogameIdOrSlugCall(VideogameIDOrSlug videogameIdOrSlug, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/videogames/{videogame_id_or_slug}"
            .replace("{" + "videogame_id_or_slug" + "}", localVarApiClient.escapeString(videogameIdOrSlug.toString()));

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
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "BearerToken", "QueryToken" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getVideogamesVideogameIdOrSlugValidateBeforeCall(VideogameIDOrSlug videogameIdOrSlug, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'videogameIdOrSlug' is set
        if (videogameIdOrSlug == null) {
            throw new ApiException("Missing the required parameter 'videogameIdOrSlug' when calling getVideogamesVideogameIdOrSlug(Async)");
        }

        return getVideogamesVideogameIdOrSlugCall(videogameIdOrSlug, _callback);

    }

    /**
     * Get a videogame
     * Get a single videogame by ID or by slug
     * @param videogameIdOrSlug A videogame ID or slug (required)
     * @return Videogame
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A videogame </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
     </table>
     */
    public Videogame getVideogamesVideogameIdOrSlug(VideogameIDOrSlug videogameIdOrSlug) throws ApiException {
        ApiResponse<Videogame> localVarResp = getVideogamesVideogameIdOrSlugWithHttpInfo(videogameIdOrSlug);
        return localVarResp.getData();
    }

    /**
     * Get a videogame
     * Get a single videogame by ID or by slug
     * @param videogameIdOrSlug A videogame ID or slug (required)
     * @return ApiResponse&lt;Videogame&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A videogame </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Videogame> getVideogamesVideogameIdOrSlugWithHttpInfo(VideogameIDOrSlug videogameIdOrSlug) throws ApiException {
        okhttp3.Call localVarCall = getVideogamesVideogameIdOrSlugValidateBeforeCall(videogameIdOrSlug, null);
        Type localVarReturnType = new TypeToken<Videogame>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a videogame (asynchronously)
     * Get a single videogame by ID or by slug
     * @param videogameIdOrSlug A videogame ID or slug (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A videogame </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVideogamesVideogameIdOrSlugAsync(VideogameIDOrSlug videogameIdOrSlug, final ApiCallback<Videogame> _callback) throws ApiException {

        okhttp3.Call localVarCall = getVideogamesVideogameIdOrSlugValidateBeforeCall(videogameIdOrSlug, _callback);
        Type localVarReturnType = new TypeToken<Videogame>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getVideogamesVideogameIdOrSlugLeagues
     * @param videogameIdOrSlug A videogame ID or slug (required)
     * @param search Options to search results (optional)
     * @param sort Options to sort results (optional)
     * @param range Options to select results within ranges (optional)
     * @param filter Options to filter results. String fields are case sensitive (optional)
     * @param page Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; (optional)
     * @param perPage Equivalent to &#x60;page[size]&#x60; (optional, default to 50)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of leagues </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVideogamesVideogameIdOrSlugLeaguesCall(VideogameIDOrSlug videogameIdOrSlug, SearchOverLeagues search, List<String> sort, RangeOverLeagues range, FilterOverLeagues filter, GetAdditionsPageParameter page, Integer perPage, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/videogames/{videogame_id_or_slug}/leagues"
            .replace("{" + "videogame_id_or_slug" + "}", localVarApiClient.escapeString(videogameIdOrSlug.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (search != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("search", search));
        }

        if (sort != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("multi", "sort", sort));
        }

        if (range != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("range", range));
        }

        if (filter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("filter", filter));
        }

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
        }

        if (perPage != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("per_page", perPage));
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

        String[] localVarAuthNames = new String[] { "BearerToken", "QueryToken" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getVideogamesVideogameIdOrSlugLeaguesValidateBeforeCall(VideogameIDOrSlug videogameIdOrSlug, SearchOverLeagues search, List<String> sort, RangeOverLeagues range, FilterOverLeagues filter, GetAdditionsPageParameter page, Integer perPage, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'videogameIdOrSlug' is set
        if (videogameIdOrSlug == null) {
            throw new ApiException("Missing the required parameter 'videogameIdOrSlug' when calling getVideogamesVideogameIdOrSlugLeagues(Async)");
        }

        return getVideogamesVideogameIdOrSlugLeaguesCall(videogameIdOrSlug, search, sort, range, filter, page, perPage, _callback);

    }

    /**
     * 
     * 
     * @param videogameIdOrSlug A videogame ID or slug (required)
     * @param search Options to search results (optional)
     * @param sort Options to sort results (optional)
     * @param range Options to select results within ranges (optional)
     * @param filter Options to filter results. String fields are case sensitive (optional)
     * @param page Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; (optional)
     * @param perPage Equivalent to &#x60;page[size]&#x60; (optional, default to 50)
     * @return List&lt;League&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of leagues </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
     </table>
     */
    public List<League> getVideogamesVideogameIdOrSlugLeagues(VideogameIDOrSlug videogameIdOrSlug, SearchOverLeagues search, List<String> sort, RangeOverLeagues range, FilterOverLeagues filter, GetAdditionsPageParameter page, Integer perPage) throws ApiException {
        ApiResponse<List<League>> localVarResp = getVideogamesVideogameIdOrSlugLeaguesWithHttpInfo(videogameIdOrSlug, search, sort, range, filter, page, perPage);
        return localVarResp.getData();
    }

    /**
     * 
     * 
     * @param videogameIdOrSlug A videogame ID or slug (required)
     * @param search Options to search results (optional)
     * @param sort Options to sort results (optional)
     * @param range Options to select results within ranges (optional)
     * @param filter Options to filter results. String fields are case sensitive (optional)
     * @param page Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; (optional)
     * @param perPage Equivalent to &#x60;page[size]&#x60; (optional, default to 50)
     * @return ApiResponse&lt;List&lt;League&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of leagues </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<League>> getVideogamesVideogameIdOrSlugLeaguesWithHttpInfo(VideogameIDOrSlug videogameIdOrSlug, SearchOverLeagues search, List<String> sort, RangeOverLeagues range, FilterOverLeagues filter, GetAdditionsPageParameter page, Integer perPage) throws ApiException {
        okhttp3.Call localVarCall = getVideogamesVideogameIdOrSlugLeaguesValidateBeforeCall(videogameIdOrSlug, search, sort, range, filter, page, perPage, null);
        Type localVarReturnType = new TypeToken<List<League>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * 
     * @param videogameIdOrSlug A videogame ID or slug (required)
     * @param search Options to search results (optional)
     * @param sort Options to sort results (optional)
     * @param range Options to select results within ranges (optional)
     * @param filter Options to filter results. String fields are case sensitive (optional)
     * @param page Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; (optional)
     * @param perPage Equivalent to &#x60;page[size]&#x60; (optional, default to 50)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of leagues </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVideogamesVideogameIdOrSlugLeaguesAsync(VideogameIDOrSlug videogameIdOrSlug, SearchOverLeagues search, List<String> sort, RangeOverLeagues range, FilterOverLeagues filter, GetAdditionsPageParameter page, Integer perPage, final ApiCallback<List<League>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getVideogamesVideogameIdOrSlugLeaguesValidateBeforeCall(videogameIdOrSlug, search, sort, range, filter, page, perPage, _callback);
        Type localVarReturnType = new TypeToken<List<League>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getVideogamesVideogameIdOrSlugSeries
     * @param videogameIdOrSlug A videogame ID or slug (required)
     * @param filter Options to filter results. String fields are case sensitive (optional)
     * @param search Options to search results (optional)
     * @param sort Options to sort results (optional)
     * @param range Options to select results within ranges (optional)
     * @param page Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; (optional)
     * @param perPage Equivalent to &#x60;page[size]&#x60; (optional, default to 50)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of series </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVideogamesVideogameIdOrSlugSeriesCall(VideogameIDOrSlug videogameIdOrSlug, FilterOverSeries filter, SearchOverSeries search, List<String> sort, RangeOverSeries range, GetAdditionsPageParameter page, Integer perPage, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/videogames/{videogame_id_or_slug}/series"
            .replace("{" + "videogame_id_or_slug" + "}", localVarApiClient.escapeString(videogameIdOrSlug.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (filter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("filter", filter));
        }

        if (search != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("search", search));
        }

        if (sort != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("multi", "sort", sort));
        }

        if (range != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("range", range));
        }

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
        }

        if (perPage != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("per_page", perPage));
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

        String[] localVarAuthNames = new String[] { "BearerToken", "QueryToken" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getVideogamesVideogameIdOrSlugSeriesValidateBeforeCall(VideogameIDOrSlug videogameIdOrSlug, FilterOverSeries filter, SearchOverSeries search, List<String> sort, RangeOverSeries range, GetAdditionsPageParameter page, Integer perPage, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'videogameIdOrSlug' is set
        if (videogameIdOrSlug == null) {
            throw new ApiException("Missing the required parameter 'videogameIdOrSlug' when calling getVideogamesVideogameIdOrSlugSeries(Async)");
        }

        return getVideogamesVideogameIdOrSlugSeriesCall(videogameIdOrSlug, filter, search, sort, range, page, perPage, _callback);

    }

    /**
     * List series for a videogame
     * List series for the given videogame
     * @param videogameIdOrSlug A videogame ID or slug (required)
     * @param filter Options to filter results. String fields are case sensitive (optional)
     * @param search Options to search results (optional)
     * @param sort Options to sort results (optional)
     * @param range Options to select results within ranges (optional)
     * @param page Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; (optional)
     * @param perPage Equivalent to &#x60;page[size]&#x60; (optional, default to 50)
     * @return List&lt;Serie&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of series </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
     </table>
     */
    public List<Serie> getVideogamesVideogameIdOrSlugSeries(VideogameIDOrSlug videogameIdOrSlug, FilterOverSeries filter, SearchOverSeries search, List<String> sort, RangeOverSeries range, GetAdditionsPageParameter page, Integer perPage) throws ApiException {
        ApiResponse<List<Serie>> localVarResp = getVideogamesVideogameIdOrSlugSeriesWithHttpInfo(videogameIdOrSlug, filter, search, sort, range, page, perPage);
        return localVarResp.getData();
    }

    /**
     * List series for a videogame
     * List series for the given videogame
     * @param videogameIdOrSlug A videogame ID or slug (required)
     * @param filter Options to filter results. String fields are case sensitive (optional)
     * @param search Options to search results (optional)
     * @param sort Options to sort results (optional)
     * @param range Options to select results within ranges (optional)
     * @param page Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; (optional)
     * @param perPage Equivalent to &#x60;page[size]&#x60; (optional, default to 50)
     * @return ApiResponse&lt;List&lt;Serie&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of series </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<Serie>> getVideogamesVideogameIdOrSlugSeriesWithHttpInfo(VideogameIDOrSlug videogameIdOrSlug, FilterOverSeries filter, SearchOverSeries search, List<String> sort, RangeOverSeries range, GetAdditionsPageParameter page, Integer perPage) throws ApiException {
        okhttp3.Call localVarCall = getVideogamesVideogameIdOrSlugSeriesValidateBeforeCall(videogameIdOrSlug, filter, search, sort, range, page, perPage, null);
        Type localVarReturnType = new TypeToken<List<Serie>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List series for a videogame (asynchronously)
     * List series for the given videogame
     * @param videogameIdOrSlug A videogame ID or slug (required)
     * @param filter Options to filter results. String fields are case sensitive (optional)
     * @param search Options to search results (optional)
     * @param sort Options to sort results (optional)
     * @param range Options to select results within ranges (optional)
     * @param page Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; (optional)
     * @param perPage Equivalent to &#x60;page[size]&#x60; (optional, default to 50)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of series </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVideogamesVideogameIdOrSlugSeriesAsync(VideogameIDOrSlug videogameIdOrSlug, FilterOverSeries filter, SearchOverSeries search, List<String> sort, RangeOverSeries range, GetAdditionsPageParameter page, Integer perPage, final ApiCallback<List<Serie>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getVideogamesVideogameIdOrSlugSeriesValidateBeforeCall(videogameIdOrSlug, filter, search, sort, range, page, perPage, _callback);
        Type localVarReturnType = new TypeToken<List<Serie>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getVideogamesVideogameIdOrSlugTournaments
     * @param videogameIdOrSlug A videogame ID or slug (required)
     * @param filter Options to filter results. String fields are case sensitive (optional)
     * @param range Options to select results within ranges (optional)
     * @param sort Options to sort results (optional)
     * @param search Options to search results (optional)
     * @param page Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; (optional)
     * @param perPage Equivalent to &#x60;page[size]&#x60; (optional, default to 50)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of tournaments </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVideogamesVideogameIdOrSlugTournamentsCall(VideogameIDOrSlug videogameIdOrSlug, FilterOverShortTournaments filter, RangeOverShortTournaments range, List<String> sort, SearchOverShortTournaments search, GetAdditionsPageParameter page, Integer perPage, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/videogames/{videogame_id_or_slug}/tournaments"
            .replace("{" + "videogame_id_or_slug" + "}", localVarApiClient.escapeString(videogameIdOrSlug.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (filter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("filter", filter));
        }

        if (range != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("range", range));
        }

        if (sort != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("multi", "sort", sort));
        }

        if (search != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("search", search));
        }

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
        }

        if (perPage != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("per_page", perPage));
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

        String[] localVarAuthNames = new String[] { "BearerToken", "QueryToken" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getVideogamesVideogameIdOrSlugTournamentsValidateBeforeCall(VideogameIDOrSlug videogameIdOrSlug, FilterOverShortTournaments filter, RangeOverShortTournaments range, List<String> sort, SearchOverShortTournaments search, GetAdditionsPageParameter page, Integer perPage, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'videogameIdOrSlug' is set
        if (videogameIdOrSlug == null) {
            throw new ApiException("Missing the required parameter 'videogameIdOrSlug' when calling getVideogamesVideogameIdOrSlugTournaments(Async)");
        }

        return getVideogamesVideogameIdOrSlugTournamentsCall(videogameIdOrSlug, filter, range, sort, search, page, perPage, _callback);

    }

    /**
     * Get tournaments for a videogame
     * List tournaments of the given videogame
     * @param videogameIdOrSlug A videogame ID or slug (required)
     * @param filter Options to filter results. String fields are case sensitive (optional)
     * @param range Options to select results within ranges (optional)
     * @param sort Options to sort results (optional)
     * @param search Options to search results (optional)
     * @param page Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; (optional)
     * @param perPage Equivalent to &#x60;page[size]&#x60; (optional, default to 50)
     * @return List&lt;ShortTournament&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of tournaments </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
     </table>
     */
    public List<ShortTournament> getVideogamesVideogameIdOrSlugTournaments(VideogameIDOrSlug videogameIdOrSlug, FilterOverShortTournaments filter, RangeOverShortTournaments range, List<String> sort, SearchOverShortTournaments search, GetAdditionsPageParameter page, Integer perPage) throws ApiException {
        ApiResponse<List<ShortTournament>> localVarResp = getVideogamesVideogameIdOrSlugTournamentsWithHttpInfo(videogameIdOrSlug, filter, range, sort, search, page, perPage);
        return localVarResp.getData();
    }

    /**
     * Get tournaments for a videogame
     * List tournaments of the given videogame
     * @param videogameIdOrSlug A videogame ID or slug (required)
     * @param filter Options to filter results. String fields are case sensitive (optional)
     * @param range Options to select results within ranges (optional)
     * @param sort Options to sort results (optional)
     * @param search Options to search results (optional)
     * @param page Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; (optional)
     * @param perPage Equivalent to &#x60;page[size]&#x60; (optional, default to 50)
     * @return ApiResponse&lt;List&lt;ShortTournament&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of tournaments </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<ShortTournament>> getVideogamesVideogameIdOrSlugTournamentsWithHttpInfo(VideogameIDOrSlug videogameIdOrSlug, FilterOverShortTournaments filter, RangeOverShortTournaments range, List<String> sort, SearchOverShortTournaments search, GetAdditionsPageParameter page, Integer perPage) throws ApiException {
        okhttp3.Call localVarCall = getVideogamesVideogameIdOrSlugTournamentsValidateBeforeCall(videogameIdOrSlug, filter, range, sort, search, page, perPage, null);
        Type localVarReturnType = new TypeToken<List<ShortTournament>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get tournaments for a videogame (asynchronously)
     * List tournaments of the given videogame
     * @param videogameIdOrSlug A videogame ID or slug (required)
     * @param filter Options to filter results. String fields are case sensitive (optional)
     * @param range Options to select results within ranges (optional)
     * @param sort Options to sort results (optional)
     * @param search Options to search results (optional)
     * @param page Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; (optional)
     * @param perPage Equivalent to &#x60;page[size]&#x60; (optional, default to 50)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of tournaments </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVideogamesVideogameIdOrSlugTournamentsAsync(VideogameIDOrSlug videogameIdOrSlug, FilterOverShortTournaments filter, RangeOverShortTournaments range, List<String> sort, SearchOverShortTournaments search, GetAdditionsPageParameter page, Integer perPage, final ApiCallback<List<ShortTournament>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getVideogamesVideogameIdOrSlugTournamentsValidateBeforeCall(videogameIdOrSlug, filter, range, sort, search, page, perPage, _callback);
        Type localVarReturnType = new TypeToken<List<ShortTournament>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getVideogamesVideogameIdOrSlugVersions
     * @param videogameIdOrSlug A videogame ID or slug (required)
     * @param filter Options to filter results. String fields are case sensitive (optional)
     * @param range Options to select results within ranges (optional)
     * @param sort Options to sort results (optional)
     * @param search Options to search results (optional)
     * @param page Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; (optional)
     * @param perPage Equivalent to &#x60;page[size]&#x60; (optional, default to 50)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of a videogame&#39;s versions </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVideogamesVideogameIdOrSlugVersionsCall(VideogameIDOrSlug videogameIdOrSlug, FilterOverShortVideogameVersions filter, RangeOverShortVideogameVersions range, List<String> sort, SearchOverShortVideogameVersions search, GetAdditionsPageParameter page, Integer perPage, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/videogames/{videogame_id_or_slug}/versions"
            .replace("{" + "videogame_id_or_slug" + "}", localVarApiClient.escapeString(videogameIdOrSlug.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (filter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("filter", filter));
        }

        if (range != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("range", range));
        }

        if (sort != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("multi", "sort", sort));
        }

        if (search != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("search", search));
        }

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
        }

        if (perPage != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("per_page", perPage));
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

        String[] localVarAuthNames = new String[] { "BearerToken", "QueryToken" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getVideogamesVideogameIdOrSlugVersionsValidateBeforeCall(VideogameIDOrSlug videogameIdOrSlug, FilterOverShortVideogameVersions filter, RangeOverShortVideogameVersions range, List<String> sort, SearchOverShortVideogameVersions search, GetAdditionsPageParameter page, Integer perPage, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'videogameIdOrSlug' is set
        if (videogameIdOrSlug == null) {
            throw new ApiException("Missing the required parameter 'videogameIdOrSlug' when calling getVideogamesVideogameIdOrSlugVersions(Async)");
        }

        return getVideogamesVideogameIdOrSlugVersionsCall(videogameIdOrSlug, filter, range, sort, search, page, perPage, _callback);

    }

    /**
     * List videogame versions
     * List available versions for a given videogame
     * @param videogameIdOrSlug A videogame ID or slug (required)
     * @param filter Options to filter results. String fields are case sensitive (optional)
     * @param range Options to select results within ranges (optional)
     * @param sort Options to sort results (optional)
     * @param search Options to search results (optional)
     * @param page Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; (optional)
     * @param perPage Equivalent to &#x60;page[size]&#x60; (optional, default to 50)
     * @return List&lt;ShortVideogameVersion&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of a videogame&#39;s versions </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
     </table>
     */
    public List<ShortVideogameVersion> getVideogamesVideogameIdOrSlugVersions(VideogameIDOrSlug videogameIdOrSlug, FilterOverShortVideogameVersions filter, RangeOverShortVideogameVersions range, List<String> sort, SearchOverShortVideogameVersions search, GetAdditionsPageParameter page, Integer perPage) throws ApiException {
        ApiResponse<List<ShortVideogameVersion>> localVarResp = getVideogamesVideogameIdOrSlugVersionsWithHttpInfo(videogameIdOrSlug, filter, range, sort, search, page, perPage);
        return localVarResp.getData();
    }

    /**
     * List videogame versions
     * List available versions for a given videogame
     * @param videogameIdOrSlug A videogame ID or slug (required)
     * @param filter Options to filter results. String fields are case sensitive (optional)
     * @param range Options to select results within ranges (optional)
     * @param sort Options to sort results (optional)
     * @param search Options to search results (optional)
     * @param page Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; (optional)
     * @param perPage Equivalent to &#x60;page[size]&#x60; (optional, default to 50)
     * @return ApiResponse&lt;List&lt;ShortVideogameVersion&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of a videogame&#39;s versions </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<ShortVideogameVersion>> getVideogamesVideogameIdOrSlugVersionsWithHttpInfo(VideogameIDOrSlug videogameIdOrSlug, FilterOverShortVideogameVersions filter, RangeOverShortVideogameVersions range, List<String> sort, SearchOverShortVideogameVersions search, GetAdditionsPageParameter page, Integer perPage) throws ApiException {
        okhttp3.Call localVarCall = getVideogamesVideogameIdOrSlugVersionsValidateBeforeCall(videogameIdOrSlug, filter, range, sort, search, page, perPage, null);
        Type localVarReturnType = new TypeToken<List<ShortVideogameVersion>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List videogame versions (asynchronously)
     * List available versions for a given videogame
     * @param videogameIdOrSlug A videogame ID or slug (required)
     * @param filter Options to filter results. String fields are case sensitive (optional)
     * @param range Options to select results within ranges (optional)
     * @param sort Options to sort results (optional)
     * @param search Options to search results (optional)
     * @param page Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; (optional)
     * @param perPage Equivalent to &#x60;page[size]&#x60; (optional, default to 50)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of a videogame&#39;s versions </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVideogamesVideogameIdOrSlugVersionsAsync(VideogameIDOrSlug videogameIdOrSlug, FilterOverShortVideogameVersions filter, RangeOverShortVideogameVersions range, List<String> sort, SearchOverShortVideogameVersions search, GetAdditionsPageParameter page, Integer perPage, final ApiCallback<List<ShortVideogameVersion>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getVideogamesVideogameIdOrSlugVersionsValidateBeforeCall(videogameIdOrSlug, filter, range, sort, search, page, perPage, _callback);
        Type localVarReturnType = new TypeToken<List<ShortVideogameVersion>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
