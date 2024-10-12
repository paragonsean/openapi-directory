/*
 * Musixmatch API
 * Musixmatch lyrics API is a robust service that permits you to search and retrieve lyrics in the simplest possible way. It just works.  Include millions of licensed lyrics on your website or in your application legally.  The fastest, most powerful and legal way to display lyrics on your website or in your application.  #### Read musixmatch API Terms & Conditions and the Privacy Policy: Before getting started, you must take a look at the [API Terms & Conditions](http://musixmatch.com/apiterms/) and the [Privacy Policy](https://developer.musixmatch.com/privacy). We’ve worked hard to make this service completely legal so that we are all protected from any foreseeable liability. Take the time to read this stuff.  #### Register for an API key: All you need to do is [register](https://developer.musixmatch.com/signup) in order to get your API key, a mandatory parameter for most of our API calls. It’s your personal identifier and should be kept secret:  ```   https://api.musixmatch.com/ws/v1.1/track.get?apikey=YOUR_API_KEY ``` #### Integrate the musixmatch service with your web site or application In the most common scenario you only need to implement two API calls:  The first call is to match your catalog to ours using the [track.search](#!/Track/get_track_search) function and the second is to get the lyrics using the [track.lyrics.get](#!/Lyrics/get_track_lyrics_get) api. That’s it!  ## API Methods What does the musiXmatch API do?  The musiXmatch API allows you to read objects from our huge 100% licensed lyrics database.  To make your life easier we are providing you with one or more examples to show you how it could work in the wild. You’ll find both the API request and API response in all the available output formats for each API call. Follow the links below for the details.  The current API version is 1.1, the root URL is located at https://api.musixmatch.com/ws/1.1/  Supported input parameters can be found on the page [Input Parameters](https://developer.musixmatch.com/documentation/input-parameters). Use UTF-8 to encode arguments when calling API methods.  Every response includes a status_code. A list of all status codes can be consulted at [Status Codes](https://developer.musixmatch.com/documentation/status-codes).  ## Music meta data The musiXmatch api is built around lyrics, but there are many other data we provide through the api that can be used to improve every existent music service.  ## Track Inside the track object you can get the following extra information:  ### TRACK RATING  The track rating is a score 0-100 identifying how popular is a song in musixmatch.  You can use this information to sort search results, like the most popular songs of an artist, of a music genre, of a lyrics language.  ### INSTRUMENTAL AND EXPLICIT FLAGS  The instrumental flag identifies songs with music only, no lyrics.  The explicit flag identifies songs with explicit lyrics or explicit title. We're able to identify explicit words and set the flag for the most common languages.  ### FAVOURITES  How many users have this song in their list of favourites.  Can be used to sort tracks by num favourite to identify more popular tracks within a set.  ### MUSIC GENRE  The music genere of the song.  Can be used to group songs by genre, as input for similarity alghorithms, artist genre identification, navigate songs by genere, etc.  ### SONG TITLES TRANSLATIONS  The track title, as translated in different lanauages, can be used to display the right writing for a given user, example:  LIES (Bigbang) becomes 在光化門 in chinese HALLELUJAH (Bigbang) becomes ハレルヤ in japanese   ## Artist Inside the artist object you can get the following nice extra information:  ### COMMENTS AND COUNTRY  An artist comment is a short snippet of text which can be mainly used for disambiguation.  The artist country is the born country of the artist/group  There are two perfect search result if you search by artist with the keyword \"U2\". Indeed there are two distinct music groups with this same name, one is the most known irish group of Bono Vox, the other is a less popular (world wide speaking) group from Japan.  Here's how you can made use of the artist comment in your search result page:  U2 (Irish rock band) U2 (あきやまうに) You can also show the artist country for even better disambiguation:  U2 (Irish rock band) from Ireland U2 (あきやまうに) from Japan ARTIST TRANSLATIONS  When you create a world wide music related service you have to take into consideration to display the artist name in the user's local language. These translation are also used as aliases to improve the search results.  Let's use PSY for this example.  Western people know him as PSY but korean want to see the original name 싸이.  Using the name translations provided by our api you can show to every user the writing they expect to see.  Furthermore, when you search for \"psy gangnam style\" or \"싸이 gangnam style\" with our search/match api you will still be able to find the song.  ### ARTIST RATING  The artist rating is a score 0-100 identifying how popular is an artist in musixmatch.  You can use this information to build charts, for suggestions, to sort search results. In the example above about U2, we use the artist rating to show the irish band before the japanese one in our serp.  ### ARTIST MUSIC GENRE  We provide one or more main artist genre, this information can be used to calculate similar artist, suggestions, or the filter a search by artist genre.    ## Album Inside the album object you can get the following nice extra information:  ### ALBUM RATING  The album rating is a score 0-100 identifying how popular is an album in musixmatch.  You can use this information to sort search results, like the most popular albums of an artist.  ### ALBUM RATING  The album rating is a score 0-100 identifying how popular is an album in musixmatch.  You can use this information to sort search results, like the most popular albums of an artist.  ### ALBUM COPYRIGHT AND LABEL  For most of our albums we can provide extra information like for example:  Label: Universal-Island Records Ltd. Copyright: (P) 2013 Rubyworks, under license to Columbia Records, a Division of Sony Music Entertainment. ALBUM TYPE AND RELEASE DATE  The album official release date can be used to sort an artist's albums view starting by the most recent one.  Album can also be filtered or grouped by type: Single, Album, Compilation, Remix, Live. This can help to build an artist page with a more organized structure.  ### ALBUM MUSIC GENRE  For most of the albums we provide two groups of music genres. Primary and secondary. This information can be used to help user navigate albums by genre.  An example could be:  Primary genere: POP Secondary genre: K-POP or Mandopop 
 *
 * The version of the OpenAPI document: 1.1.0
 * Contact: info@musixmatch.com
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


import org.openapitools.client.model.ArtistGetGet200Response;
import org.openapitools.client.model.ArtistRelatedGetGet200Response;
import java.math.BigDecimal;
import org.openapitools.client.model.ChartArtistsGetGet200Response;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ArtistApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ArtistApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ArtistApi(ApiClient apiClient) {
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
     * Build call for artistGetGet
     * @param artistId  The musiXmatch artist id (required)
     * @param format output format: json, jsonp, xml. (optional, default to json)
     * @param paramCallback jsonp callback (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The request was successful. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call artistGetGetCall(String artistId, String format, String paramCallback, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/artist.get";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (format != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("format", format));
        }

        if (paramCallback != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("callback", paramCallback));
        }

        if (artistId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("artist_id", artistId));
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

        String[] localVarAuthNames = new String[] { "key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call artistGetGetValidateBeforeCall(String artistId, String format, String paramCallback, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'artistId' is set
        if (artistId == null) {
            throw new ApiException("Missing the required parameter 'artistId' when calling artistGetGet(Async)");
        }

        return artistGetGetCall(artistId, format, paramCallback, _callback);

    }

    /**
     * 
     * 
     * @param artistId  The musiXmatch artist id (required)
     * @param format output format: json, jsonp, xml. (optional, default to json)
     * @param paramCallback jsonp callback (optional)
     * @return ArtistGetGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The request was successful. </td><td>  -  </td></tr>
     </table>
     */
    public ArtistGetGet200Response artistGetGet(String artistId, String format, String paramCallback) throws ApiException {
        ApiResponse<ArtistGetGet200Response> localVarResp = artistGetGetWithHttpInfo(artistId, format, paramCallback);
        return localVarResp.getData();
    }

    /**
     * 
     * 
     * @param artistId  The musiXmatch artist id (required)
     * @param format output format: json, jsonp, xml. (optional, default to json)
     * @param paramCallback jsonp callback (optional)
     * @return ApiResponse&lt;ArtistGetGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The request was successful. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ArtistGetGet200Response> artistGetGetWithHttpInfo(String artistId, String format, String paramCallback) throws ApiException {
        okhttp3.Call localVarCall = artistGetGetValidateBeforeCall(artistId, format, paramCallback, null);
        Type localVarReturnType = new TypeToken<ArtistGetGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * 
     * @param artistId  The musiXmatch artist id (required)
     * @param format output format: json, jsonp, xml. (optional, default to json)
     * @param paramCallback jsonp callback (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The request was successful. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call artistGetGetAsync(String artistId, String format, String paramCallback, final ApiCallback<ArtistGetGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = artistGetGetValidateBeforeCall(artistId, format, paramCallback, _callback);
        Type localVarReturnType = new TypeToken<ArtistGetGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for artistRelatedGetGet
     * @param artistId The musiXmatch artist id (required)
     * @param format output format: json, jsonp, xml. (optional, default to json)
     * @param paramCallback jsonp callback (optional)
     * @param pageSize Define the page size for paginated results.Range is 1 to 100. (optional)
     * @param page Define the page number for paginated results (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The request was successful. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call artistRelatedGetGetCall(String artistId, String format, String paramCallback, BigDecimal pageSize, BigDecimal page, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/artist.related.get";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (format != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("format", format));
        }

        if (paramCallback != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("callback", paramCallback));
        }

        if (artistId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("artist_id", artistId));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page_size", pageSize));
        }

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
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

        String[] localVarAuthNames = new String[] { "key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call artistRelatedGetGetValidateBeforeCall(String artistId, String format, String paramCallback, BigDecimal pageSize, BigDecimal page, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'artistId' is set
        if (artistId == null) {
            throw new ApiException("Missing the required parameter 'artistId' when calling artistRelatedGetGet(Async)");
        }

        return artistRelatedGetGetCall(artistId, format, paramCallback, pageSize, page, _callback);

    }

    /**
     * 
     * 
     * @param artistId The musiXmatch artist id (required)
     * @param format output format: json, jsonp, xml. (optional, default to json)
     * @param paramCallback jsonp callback (optional)
     * @param pageSize Define the page size for paginated results.Range is 1 to 100. (optional)
     * @param page Define the page number for paginated results (optional)
     * @return ArtistRelatedGetGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The request was successful. </td><td>  -  </td></tr>
     </table>
     */
    public ArtistRelatedGetGet200Response artistRelatedGetGet(String artistId, String format, String paramCallback, BigDecimal pageSize, BigDecimal page) throws ApiException {
        ApiResponse<ArtistRelatedGetGet200Response> localVarResp = artistRelatedGetGetWithHttpInfo(artistId, format, paramCallback, pageSize, page);
        return localVarResp.getData();
    }

    /**
     * 
     * 
     * @param artistId The musiXmatch artist id (required)
     * @param format output format: json, jsonp, xml. (optional, default to json)
     * @param paramCallback jsonp callback (optional)
     * @param pageSize Define the page size for paginated results.Range is 1 to 100. (optional)
     * @param page Define the page number for paginated results (optional)
     * @return ApiResponse&lt;ArtistRelatedGetGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The request was successful. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ArtistRelatedGetGet200Response> artistRelatedGetGetWithHttpInfo(String artistId, String format, String paramCallback, BigDecimal pageSize, BigDecimal page) throws ApiException {
        okhttp3.Call localVarCall = artistRelatedGetGetValidateBeforeCall(artistId, format, paramCallback, pageSize, page, null);
        Type localVarReturnType = new TypeToken<ArtistRelatedGetGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * 
     * @param artistId The musiXmatch artist id (required)
     * @param format output format: json, jsonp, xml. (optional, default to json)
     * @param paramCallback jsonp callback (optional)
     * @param pageSize Define the page size for paginated results.Range is 1 to 100. (optional)
     * @param page Define the page number for paginated results (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The request was successful. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call artistRelatedGetGetAsync(String artistId, String format, String paramCallback, BigDecimal pageSize, BigDecimal page, final ApiCallback<ArtistRelatedGetGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = artistRelatedGetGetValidateBeforeCall(artistId, format, paramCallback, pageSize, page, _callback);
        Type localVarReturnType = new TypeToken<ArtistRelatedGetGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for artistSearchGet
     * @param format output format: json, jsonp, xml. (optional, default to json)
     * @param paramCallback jsonp callback (optional)
     * @param qArtist The song artist (optional)
     * @param fArtistId When set, filter by this artist id (optional)
     * @param page Define the page number for paginated results (optional)
     * @param pageSize Define the page size for paginated results.Range is 1 to 100. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The request was successful. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call artistSearchGetCall(String format, String paramCallback, String qArtist, BigDecimal fArtistId, BigDecimal page, BigDecimal pageSize, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/artist.search";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (format != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("format", format));
        }

        if (paramCallback != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("callback", paramCallback));
        }

        if (qArtist != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("q_artist", qArtist));
        }

        if (fArtistId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("f_artist_id", fArtistId));
        }

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page_size", pageSize));
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

        String[] localVarAuthNames = new String[] { "key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call artistSearchGetValidateBeforeCall(String format, String paramCallback, String qArtist, BigDecimal fArtistId, BigDecimal page, BigDecimal pageSize, final ApiCallback _callback) throws ApiException {
        return artistSearchGetCall(format, paramCallback, qArtist, fArtistId, page, pageSize, _callback);

    }

    /**
     * 
     * 
     * @param format output format: json, jsonp, xml. (optional, default to json)
     * @param paramCallback jsonp callback (optional)
     * @param qArtist The song artist (optional)
     * @param fArtistId When set, filter by this artist id (optional)
     * @param page Define the page number for paginated results (optional)
     * @param pageSize Define the page size for paginated results.Range is 1 to 100. (optional)
     * @return ArtistRelatedGetGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The request was successful. </td><td>  -  </td></tr>
     </table>
     */
    public ArtistRelatedGetGet200Response artistSearchGet(String format, String paramCallback, String qArtist, BigDecimal fArtistId, BigDecimal page, BigDecimal pageSize) throws ApiException {
        ApiResponse<ArtistRelatedGetGet200Response> localVarResp = artistSearchGetWithHttpInfo(format, paramCallback, qArtist, fArtistId, page, pageSize);
        return localVarResp.getData();
    }

    /**
     * 
     * 
     * @param format output format: json, jsonp, xml. (optional, default to json)
     * @param paramCallback jsonp callback (optional)
     * @param qArtist The song artist (optional)
     * @param fArtistId When set, filter by this artist id (optional)
     * @param page Define the page number for paginated results (optional)
     * @param pageSize Define the page size for paginated results.Range is 1 to 100. (optional)
     * @return ApiResponse&lt;ArtistRelatedGetGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The request was successful. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ArtistRelatedGetGet200Response> artistSearchGetWithHttpInfo(String format, String paramCallback, String qArtist, BigDecimal fArtistId, BigDecimal page, BigDecimal pageSize) throws ApiException {
        okhttp3.Call localVarCall = artistSearchGetValidateBeforeCall(format, paramCallback, qArtist, fArtistId, page, pageSize, null);
        Type localVarReturnType = new TypeToken<ArtistRelatedGetGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * 
     * @param format output format: json, jsonp, xml. (optional, default to json)
     * @param paramCallback jsonp callback (optional)
     * @param qArtist The song artist (optional)
     * @param fArtistId When set, filter by this artist id (optional)
     * @param page Define the page number for paginated results (optional)
     * @param pageSize Define the page size for paginated results.Range is 1 to 100. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The request was successful. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call artistSearchGetAsync(String format, String paramCallback, String qArtist, BigDecimal fArtistId, BigDecimal page, BigDecimal pageSize, final ApiCallback<ArtistRelatedGetGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = artistSearchGetValidateBeforeCall(format, paramCallback, qArtist, fArtistId, page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<ArtistRelatedGetGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for chartArtistsGetGet
     * @param format output format: json, jsonp, xml. (optional, default to json)
     * @param paramCallback jsonp callback (optional)
     * @param page Define the page number for paginated results (optional)
     * @param pageSize Define the page size for paginated results.Range is 1 to 100. (optional)
     * @param country A valid ISO 3166 country code (optional, default to us)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The request was successful. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call chartArtistsGetGetCall(String format, String paramCallback, BigDecimal page, BigDecimal pageSize, String country, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/chart.artists.get";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (format != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("format", format));
        }

        if (paramCallback != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("callback", paramCallback));
        }

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page_size", pageSize));
        }

        if (country != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("country", country));
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

        String[] localVarAuthNames = new String[] { "key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call chartArtistsGetGetValidateBeforeCall(String format, String paramCallback, BigDecimal page, BigDecimal pageSize, String country, final ApiCallback _callback) throws ApiException {
        return chartArtistsGetGetCall(format, paramCallback, page, pageSize, country, _callback);

    }

    /**
     * 
     * 
     * @param format output format: json, jsonp, xml. (optional, default to json)
     * @param paramCallback jsonp callback (optional)
     * @param page Define the page number for paginated results (optional)
     * @param pageSize Define the page size for paginated results.Range is 1 to 100. (optional)
     * @param country A valid ISO 3166 country code (optional, default to us)
     * @return ChartArtistsGetGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The request was successful. </td><td>  -  </td></tr>
     </table>
     */
    public ChartArtistsGetGet200Response chartArtistsGetGet(String format, String paramCallback, BigDecimal page, BigDecimal pageSize, String country) throws ApiException {
        ApiResponse<ChartArtistsGetGet200Response> localVarResp = chartArtistsGetGetWithHttpInfo(format, paramCallback, page, pageSize, country);
        return localVarResp.getData();
    }

    /**
     * 
     * 
     * @param format output format: json, jsonp, xml. (optional, default to json)
     * @param paramCallback jsonp callback (optional)
     * @param page Define the page number for paginated results (optional)
     * @param pageSize Define the page size for paginated results.Range is 1 to 100. (optional)
     * @param country A valid ISO 3166 country code (optional, default to us)
     * @return ApiResponse&lt;ChartArtistsGetGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The request was successful. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ChartArtistsGetGet200Response> chartArtistsGetGetWithHttpInfo(String format, String paramCallback, BigDecimal page, BigDecimal pageSize, String country) throws ApiException {
        okhttp3.Call localVarCall = chartArtistsGetGetValidateBeforeCall(format, paramCallback, page, pageSize, country, null);
        Type localVarReturnType = new TypeToken<ChartArtistsGetGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * 
     * @param format output format: json, jsonp, xml. (optional, default to json)
     * @param paramCallback jsonp callback (optional)
     * @param page Define the page number for paginated results (optional)
     * @param pageSize Define the page size for paginated results.Range is 1 to 100. (optional)
     * @param country A valid ISO 3166 country code (optional, default to us)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The request was successful. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call chartArtistsGetGetAsync(String format, String paramCallback, BigDecimal page, BigDecimal pageSize, String country, final ApiCallback<ChartArtistsGetGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = chartArtistsGetGetValidateBeforeCall(format, paramCallback, page, pageSize, country, _callback);
        Type localVarReturnType = new TypeToken<ChartArtistsGetGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
