/*
 * Rebilly REST API
 * # Introduction The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable resource URLs.  It returns HTTP response codes to indicate errors.  It also accepts and returns JSON in the HTTP body.  You can use your favorite HTTP/REST library for your programming language to use Rebilly's API, or you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php) and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).  We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com) is supported by an API which is documented and available for use so that you may automate any workflows necessary.  This document contains the most commonly integrated resources.  # Authentication  When you sign up for an account, you are given your first secret API key. You can generate additional API keys, and delete API keys (as you may need to rotate your keys in the future). You authenticate to the Rebilly API by providing your secret key in the request header.  Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key. - [Secret API key](#section/Authentication/SecretApiKey): used for requests made   from the server side. Never share these keys. Keep them guarded and secure. - [Publishable API key](#section/Authentication/PublishableApiKey): used for    requests from the client side. For now can only be used to create    a [Payment Token](#operation/PostToken) and    a [File token](#operation/PostFile). - [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.  Never share your secret keys. Keep them guarded and secure.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  # Errors Rebilly follow's the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Forbidden &lt;RedocResponse pointer={\"#/components/responses/Forbidden\"} /&gt;  ## Conflict &lt;RedocResponse pointer={\"#/components/responses/Conflict\"} /&gt;  ## NotFound &lt;RedocResponse pointer={\"#/components/responses/NotFound\"} /&gt;  ## Unauthorized &lt;RedocResponse pointer={\"#/components/responses/Unauthorized\"} /&gt;  ## ValidationError &lt;RedocResponse pointer={\"#/components/responses/ValidationError\"} /&gt;  # SDKs  Rebilly offers a Javascript SDK and a PHP SDK to help interact with the API.  However, no SDK is required to use the API.  Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),  a client-side iFrame-based solution to help create payment tokens while minimizing PCI DSS compliance burdens and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is interacting with the [payment tokens creation operation](#operation/PostToken).  ## Javascript SDK  Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks). SDK code examples are included in these docs.  ## PHP SDK For all PHP SDK examples provided in these docs you will need to configure the `$client`. You may do it like this:  ```php $client = new Rebilly\\Client([     'apiKey' =&gt; 'YourApiKeyHere',     'baseUrl' =&gt; 'https://api.rebilly.com', ]); ```  # Using filter with collections Rebilly provides collections filtering. You can use `?filter` param on collections to define which records should be shown in the response.  Here is filter format description:  - Fields and values in filter are separated with `:`: `?filter=firstName:John`.  - Sub-fields are separated with `.`: `?filter=billingAddress.country:US`.  - Multiple filters are separated with `;`: `?filter=firstName:John;lastName:Doe`. They will be joined with `AND` logic. In this example: `firstName:John` AND `lastName:Doe`.  - You can use multiple values using `,` as values separator: `?filter=firstName:John,Bob`. Multiple values specified for a field will be joined with `OR` logic. In this example: `firstName:John` OR `firstName:Bob`.  - To negate the filter use `!`: `?filter=firstName:!John`. Note that you can negate multiple values like this: `?filter=firstName:!John,!Bob`. This filter rule will exclude all Johns and Bobs from the response.  - You can use range filters like this: `?filter=amount:1..10`.  - You can use gte (greater than or equals) filter like this: `?filter=amount:1..`, or lte (less than or equals) than filter like this: `?filter=amount:..10`. This also works for datetime-based fields.  - You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: `?filter=firstName:@yourListName`. You can also exclude list values: `?filter=firstName:!@yourListName`.  - Datetime-based fields accept values formatted using RFC 3339 like this: `?filter=createdTime:2021-02-14T13:30:00Z`.   # Expand to include embedded objects Rebilly provides the ability to pre-load additional  objects with a request.   You can use `?expand` param on most requests to expand and include embedded objects within the `_embedded` property of the response.  The `_embedded` property contains an array of  objects keyed by the expand parameter value(s).  You may expand multiple objects by passing them as comma-separated to the expand value like so:  ``` ?expand=recentInvoice,customer ```  And in the response, you would see:  ``` \"_embedded\": [     \"recentInvoice\": {...},     \"customer\": {...} ] ``` Expand may be utilitized not only on `GET` requests but also on `PATCH`, `POST`, `PUT` requests too.   # Getting started guide  Rebilly's API has over 300 operations.  That's more than you'll  need to implement your use cases.  If you have a use  case you would like to implement, please consult us for feedback on the best API operations for the task.  Our getting started guide will demonstrate a basic order form use case.  It will allow us to highlight core resources in Rebilly that will be helpful for many other use cases too.  Within 25 minutes, you'll have sent API requests (via our console) to create a subscription order. 
 *
 * The version of the OpenAPI document: 2.1
 * Contact: integrations@rebilly.com
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


import org.openapitools.client.model.Attachment;
import org.openapitools.client.model.Error;
import org.openapitools.client.model.InvalidError;
import org.openapitools.client.model.ModelFile;
import org.openapitools.client.model.PostFileRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class FilesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public FilesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public FilesApi(ApiClient apiClient) {
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
     * Build call for deleteAttachment
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Attachment was deleted. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteAttachmentCall(String id, String organizationId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/attachments/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (organizationId != null) {
            localVarHeaderParams.put("Organization-Id", localVarApiClient.parameterToString(organizationId));
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

        String[] localVarAuthNames = new String[] { "SecretApiKey", "JWT" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteAttachmentValidateBeforeCall(String id, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling deleteAttachment(Async)");
        }

        return deleteAttachmentCall(id, organizationId, _callback);

    }

    /**
     * Delete an Attachment
     * Delete the Attachment with predefined identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Attachment was deleted. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public void deleteAttachment(String id, String organizationId) throws ApiException {
        deleteAttachmentWithHttpInfo(id, organizationId);
    }

    /**
     * Delete an Attachment
     * Delete the Attachment with predefined identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Attachment was deleted. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteAttachmentWithHttpInfo(String id, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = deleteAttachmentValidateBeforeCall(id, organizationId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete an Attachment (asynchronously)
     * Delete the Attachment with predefined identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Attachment was deleted. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteAttachmentAsync(String id, String organizationId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteAttachmentValidateBeforeCall(id, organizationId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteFile
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> File was deleted. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteFileCall(String id, String organizationId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/files/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (organizationId != null) {
            localVarHeaderParams.put("Organization-Id", localVarApiClient.parameterToString(organizationId));
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

        String[] localVarAuthNames = new String[] { "SecretApiKey", "JWT" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteFileValidateBeforeCall(String id, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling deleteFile(Async)");
        }

        return deleteFileCall(id, organizationId, _callback);

    }

    /**
     * Delete a File
     * Delete the File with predefined identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> File was deleted. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public void deleteFile(String id, String organizationId) throws ApiException {
        deleteFileWithHttpInfo(id, organizationId);
    }

    /**
     * Delete a File
     * Delete the File with predefined identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> File was deleted. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteFileWithHttpInfo(String id, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = deleteFileValidateBeforeCall(id, organizationId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a File (asynchronously)
     * Delete the File with predefined identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> File was deleted. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteFileAsync(String id, String organizationId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteFileValidateBeforeCall(id, organizationId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getAttachment
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Attachment was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAttachmentCall(String id, String organizationId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/attachments/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (organizationId != null) {
            localVarHeaderParams.put("Organization-Id", localVarApiClient.parameterToString(organizationId));
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

        String[] localVarAuthNames = new String[] { "SecretApiKey", "JWT" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getAttachmentValidateBeforeCall(String id, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getAttachment(Async)");
        }

        return getAttachmentCall(id, organizationId, _callback);

    }

    /**
     * Retrieve an Attachment
     * Retrieve a Attachment with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return Attachment
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Attachment was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public Attachment getAttachment(String id, String organizationId) throws ApiException {
        ApiResponse<Attachment> localVarResp = getAttachmentWithHttpInfo(id, organizationId);
        return localVarResp.getData();
    }

    /**
     * Retrieve an Attachment
     * Retrieve a Attachment with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;Attachment&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Attachment was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Attachment> getAttachmentWithHttpInfo(String id, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = getAttachmentValidateBeforeCall(id, organizationId, null);
        Type localVarReturnType = new TypeToken<Attachment>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve an Attachment (asynchronously)
     * Retrieve a Attachment with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Attachment was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAttachmentAsync(String id, String organizationId, final ApiCallback<Attachment> _callback) throws ApiException {

        okhttp3.Call localVarCall = getAttachmentValidateBeforeCall(id, organizationId, _callback);
        Type localVarReturnType = new TypeToken<Attachment>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getAttachmentCollection
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param q The partial search of the text fields. (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @param fields Limit the returned fields to the list specified, separated by comma. Note that id is always returned. (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of Attachments was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAttachmentCollectionCall(String organizationId, Integer limit, Integer offset, String filter, String q, String expand, String fields, List<String> sort, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/attachments";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (limit != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("limit", limit));
        }

        if (offset != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("offset", offset));
        }

        if (filter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("filter", filter));
        }

        if (q != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("q", q));
        }

        if (expand != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("expand", expand));
        }

        if (fields != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("fields", fields));
        }

        if (sort != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("csv", "sort", sort));
        }

        if (organizationId != null) {
            localVarHeaderParams.put("Organization-Id", localVarApiClient.parameterToString(organizationId));
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

        String[] localVarAuthNames = new String[] { "SecretApiKey", "JWT" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getAttachmentCollectionValidateBeforeCall(String organizationId, Integer limit, Integer offset, String filter, String q, String expand, String fields, List<String> sort, final ApiCallback _callback) throws ApiException {
        return getAttachmentCollectionCall(organizationId, limit, offset, filter, q, expand, fields, sort, _callback);

    }

    /**
     * Retrieve a list of Attachments
     * Retrieve a list of attachments. You may sort by the id, name, relatedId, relatedType, fileId, createdTime, and updatedTime. 
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param q The partial search of the text fields. (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @param fields Limit the returned fields to the list specified, separated by comma. Note that id is always returned. (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @return List&lt;Attachment&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of Attachments was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public List<Attachment> getAttachmentCollection(String organizationId, Integer limit, Integer offset, String filter, String q, String expand, String fields, List<String> sort) throws ApiException {
        ApiResponse<List<Attachment>> localVarResp = getAttachmentCollectionWithHttpInfo(organizationId, limit, offset, filter, q, expand, fields, sort);
        return localVarResp.getData();
    }

    /**
     * Retrieve a list of Attachments
     * Retrieve a list of attachments. You may sort by the id, name, relatedId, relatedType, fileId, createdTime, and updatedTime. 
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param q The partial search of the text fields. (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @param fields Limit the returned fields to the list specified, separated by comma. Note that id is always returned. (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @return ApiResponse&lt;List&lt;Attachment&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of Attachments was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<Attachment>> getAttachmentCollectionWithHttpInfo(String organizationId, Integer limit, Integer offset, String filter, String q, String expand, String fields, List<String> sort) throws ApiException {
        okhttp3.Call localVarCall = getAttachmentCollectionValidateBeforeCall(organizationId, limit, offset, filter, q, expand, fields, sort, null);
        Type localVarReturnType = new TypeToken<List<Attachment>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve a list of Attachments (asynchronously)
     * Retrieve a list of attachments. You may sort by the id, name, relatedId, relatedType, fileId, createdTime, and updatedTime. 
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param q The partial search of the text fields. (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @param fields Limit the returned fields to the list specified, separated by comma. Note that id is always returned. (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of Attachments was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAttachmentCollectionAsync(String organizationId, Integer limit, Integer offset, String filter, String q, String expand, String fields, List<String> sort, final ApiCallback<List<Attachment>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getAttachmentCollectionValidateBeforeCall(organizationId, limit, offset, filter, q, expand, fields, sort, _callback);
        Type localVarReturnType = new TypeToken<List<Attachment>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getFile
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> File was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getFileCall(String id, String organizationId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/files/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (organizationId != null) {
            localVarHeaderParams.put("Organization-Id", localVarApiClient.parameterToString(organizationId));
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

        String[] localVarAuthNames = new String[] { "SecretApiKey", "JWT" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getFileValidateBeforeCall(String id, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getFile(Async)");
        }

        return getFileCall(id, organizationId, _callback);

    }

    /**
     * Retrieve a File Record
     * Retrieve a File with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ModelFile
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> File was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public ModelFile getFile(String id, String organizationId) throws ApiException {
        ApiResponse<ModelFile> localVarResp = getFileWithHttpInfo(id, organizationId);
        return localVarResp.getData();
    }

    /**
     * Retrieve a File Record
     * Retrieve a File with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;ModelFile&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> File was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ModelFile> getFileWithHttpInfo(String id, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = getFileValidateBeforeCall(id, organizationId, null);
        Type localVarReturnType = new TypeToken<ModelFile>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve a File Record (asynchronously)
     * Retrieve a File with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> File was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getFileAsync(String id, String organizationId, final ApiCallback<ModelFile> _callback) throws ApiException {

        okhttp3.Call localVarCall = getFileValidateBeforeCall(id, organizationId, _callback);
        Type localVarReturnType = new TypeToken<ModelFile>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getFileCollection
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param q The partial search of the text fields. (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @param fields Limit the returned fields to the list specified, separated by comma. Note that id is always returned. (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of Files was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getFileCollectionCall(String organizationId, Integer limit, Integer offset, String filter, String q, String expand, String fields, List<String> sort, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/files";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (limit != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("limit", limit));
        }

        if (offset != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("offset", offset));
        }

        if (filter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("filter", filter));
        }

        if (q != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("q", q));
        }

        if (expand != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("expand", expand));
        }

        if (fields != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("fields", fields));
        }

        if (sort != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("csv", "sort", sort));
        }

        if (organizationId != null) {
            localVarHeaderParams.put("Organization-Id", localVarApiClient.parameterToString(organizationId));
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

        String[] localVarAuthNames = new String[] { "SecretApiKey", "JWT" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getFileCollectionValidateBeforeCall(String organizationId, Integer limit, Integer offset, String filter, String q, String expand, String fields, List<String> sort, final ApiCallback _callback) throws ApiException {
        return getFileCollectionCall(organizationId, limit, offset, filter, q, expand, fields, sort, _callback);

    }

    /**
     * Retrieve a list of files
     * Retrieve a list of files. 
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param q The partial search of the text fields. (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @param fields Limit the returned fields to the list specified, separated by comma. Note that id is always returned. (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @return List&lt;ModelFile&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of Files was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public List<ModelFile> getFileCollection(String organizationId, Integer limit, Integer offset, String filter, String q, String expand, String fields, List<String> sort) throws ApiException {
        ApiResponse<List<ModelFile>> localVarResp = getFileCollectionWithHttpInfo(organizationId, limit, offset, filter, q, expand, fields, sort);
        return localVarResp.getData();
    }

    /**
     * Retrieve a list of files
     * Retrieve a list of files. 
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param q The partial search of the text fields. (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @param fields Limit the returned fields to the list specified, separated by comma. Note that id is always returned. (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @return ApiResponse&lt;List&lt;ModelFile&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of Files was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<ModelFile>> getFileCollectionWithHttpInfo(String organizationId, Integer limit, Integer offset, String filter, String q, String expand, String fields, List<String> sort) throws ApiException {
        okhttp3.Call localVarCall = getFileCollectionValidateBeforeCall(organizationId, limit, offset, filter, q, expand, fields, sort, null);
        Type localVarReturnType = new TypeToken<List<ModelFile>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve a list of files (asynchronously)
     * Retrieve a list of files. 
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param q The partial search of the text fields. (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @param fields Limit the returned fields to the list specified, separated by comma. Note that id is always returned. (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of Files was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getFileCollectionAsync(String organizationId, Integer limit, Integer offset, String filter, String q, String expand, String fields, List<String> sort, final ApiCallback<List<ModelFile>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getFileCollectionValidateBeforeCall(organizationId, limit, offset, filter, q, expand, fields, sort, _callback);
        Type localVarReturnType = new TypeToken<List<ModelFile>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getFileDownload
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param imageSize Resize image to specified size. Supports any sizes from 10x10 to 2000x2000 (format &#x60;{width}x{height}&#x60;). The image will be returned in the original size if the value is invalid. This parameter will be ignored for non-image files. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The file was retrieved successfully. </td><td>  * Content-Length - The number of bytes in the file. <br>  * Content-Type - The MIME type of the file. <br>  </td></tr>
        <tr><td> 302 </td><td> Resource was moved. </td><td>  * Location -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getFileDownloadCall(String id, String organizationId, String imageSize, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/files/{id}/download"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (imageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("imageSize", imageSize));
        }

        if (organizationId != null) {
            localVarHeaderParams.put("Organization-Id", localVarApiClient.parameterToString(organizationId));
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

        String[] localVarAuthNames = new String[] { "SecretApiKey", "JWT" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getFileDownloadValidateBeforeCall(String id, String organizationId, String imageSize, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getFileDownload(Async)");
        }

        return getFileDownloadCall(id, organizationId, imageSize, _callback);

    }

    /**
     * Download a file
     * Download a file. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param imageSize Resize image to specified size. Supports any sizes from 10x10 to 2000x2000 (format &#x60;{width}x{height}&#x60;). The image will be returned in the original size if the value is invalid. This parameter will be ignored for non-image files. (optional)
     * @return String
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The file was retrieved successfully. </td><td>  * Content-Length - The number of bytes in the file. <br>  * Content-Type - The MIME type of the file. <br>  </td></tr>
        <tr><td> 302 </td><td> Resource was moved. </td><td>  * Location -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public String getFileDownload(String id, String organizationId, String imageSize) throws ApiException {
        ApiResponse<String> localVarResp = getFileDownloadWithHttpInfo(id, organizationId, imageSize);
        return localVarResp.getData();
    }

    /**
     * Download a file
     * Download a file. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param imageSize Resize image to specified size. Supports any sizes from 10x10 to 2000x2000 (format &#x60;{width}x{height}&#x60;). The image will be returned in the original size if the value is invalid. This parameter will be ignored for non-image files. (optional)
     * @return ApiResponse&lt;String&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The file was retrieved successfully. </td><td>  * Content-Length - The number of bytes in the file. <br>  * Content-Type - The MIME type of the file. <br>  </td></tr>
        <tr><td> 302 </td><td> Resource was moved. </td><td>  * Location -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<String> getFileDownloadWithHttpInfo(String id, String organizationId, String imageSize) throws ApiException {
        okhttp3.Call localVarCall = getFileDownloadValidateBeforeCall(id, organizationId, imageSize, null);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Download a file (asynchronously)
     * Download a file. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param imageSize Resize image to specified size. Supports any sizes from 10x10 to 2000x2000 (format &#x60;{width}x{height}&#x60;). The image will be returned in the original size if the value is invalid. This parameter will be ignored for non-image files. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The file was retrieved successfully. </td><td>  * Content-Length - The number of bytes in the file. <br>  * Content-Type - The MIME type of the file. <br>  </td></tr>
        <tr><td> 302 </td><td> Resource was moved. </td><td>  * Location -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getFileDownloadAsync(String id, String organizationId, String imageSize, final ApiCallback<String> _callback) throws ApiException {

        okhttp3.Call localVarCall = getFileDownloadValidateBeforeCall(id, organizationId, imageSize, _callback);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getFileDownloadExtension
     * @param id The resource identifier string. (required)
     * @param extension File extension which also indicates the desired file format. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The file was retrieved successfully. </td><td>  * Content-Length - The number of bytes in the file. <br>  * Content-Type - The MIME type of the file. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getFileDownloadExtensionCall(String id, String extension, String organizationId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/files/{id}/download{extension}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()))
            .replace("{" + "extension" + "}", localVarApiClient.escapeString(extension.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (organizationId != null) {
            localVarHeaderParams.put("Organization-Id", localVarApiClient.parameterToString(organizationId));
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

        String[] localVarAuthNames = new String[] { "SecretApiKey", "JWT" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getFileDownloadExtensionValidateBeforeCall(String id, String extension, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getFileDownloadExtension(Async)");
        }

        // verify the required parameter 'extension' is set
        if (extension == null) {
            throw new ApiException("Missing the required parameter 'extension' when calling getFileDownloadExtension(Async)");
        }

        return getFileDownloadExtensionCall(id, extension, organizationId, _callback);

    }

    /**
     * Download image in specific format
     * Download image in specific format. Images are converted server-side. 
     * @param id The resource identifier string. (required)
     * @param extension File extension which also indicates the desired file format. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return String
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The file was retrieved successfully. </td><td>  * Content-Length - The number of bytes in the file. <br>  * Content-Type - The MIME type of the file. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public String getFileDownloadExtension(String id, String extension, String organizationId) throws ApiException {
        ApiResponse<String> localVarResp = getFileDownloadExtensionWithHttpInfo(id, extension, organizationId);
        return localVarResp.getData();
    }

    /**
     * Download image in specific format
     * Download image in specific format. Images are converted server-side. 
     * @param id The resource identifier string. (required)
     * @param extension File extension which also indicates the desired file format. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;String&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The file was retrieved successfully. </td><td>  * Content-Length - The number of bytes in the file. <br>  * Content-Type - The MIME type of the file. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<String> getFileDownloadExtensionWithHttpInfo(String id, String extension, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = getFileDownloadExtensionValidateBeforeCall(id, extension, organizationId, null);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Download image in specific format (asynchronously)
     * Download image in specific format. Images are converted server-side. 
     * @param id The resource identifier string. (required)
     * @param extension File extension which also indicates the desired file format. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The file was retrieved successfully. </td><td>  * Content-Length - The number of bytes in the file. <br>  * Content-Type - The MIME type of the file. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getFileDownloadExtensionAsync(String id, String extension, String organizationId, final ApiCallback<String> _callback) throws ApiException {

        okhttp3.Call localVarCall = getFileDownloadExtensionValidateBeforeCall(id, extension, organizationId, _callback);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postAttachment
     * @param attachment Attachment resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Attachment was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postAttachmentCall(Attachment attachment, String organizationId, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = attachment;

        // create path and map variables
        String localVarPath = "/attachments";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (organizationId != null) {
            localVarHeaderParams.put("Organization-Id", localVarApiClient.parameterToString(organizationId));
        }

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

        String[] localVarAuthNames = new String[] { "SecretApiKey", "JWT" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postAttachmentValidateBeforeCall(Attachment attachment, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'attachment' is set
        if (attachment == null) {
            throw new ApiException("Missing the required parameter 'attachment' when calling postAttachment(Async)");
        }

        return postAttachmentCall(attachment, organizationId, _callback);

    }

    /**
     * Create an Attachment
     * Create an Attachment. 
     * @param attachment Attachment resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return Attachment
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Attachment was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public Attachment postAttachment(Attachment attachment, String organizationId) throws ApiException {
        ApiResponse<Attachment> localVarResp = postAttachmentWithHttpInfo(attachment, organizationId);
        return localVarResp.getData();
    }

    /**
     * Create an Attachment
     * Create an Attachment. 
     * @param attachment Attachment resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;Attachment&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Attachment was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Attachment> postAttachmentWithHttpInfo(Attachment attachment, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = postAttachmentValidateBeforeCall(attachment, organizationId, null);
        Type localVarReturnType = new TypeToken<Attachment>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create an Attachment (asynchronously)
     * Create an Attachment. 
     * @param attachment Attachment resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Attachment was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postAttachmentAsync(Attachment attachment, String organizationId, final ApiCallback<Attachment> _callback) throws ApiException {

        okhttp3.Call localVarCall = postAttachmentValidateBeforeCall(attachment, organizationId, _callback);
        Type localVarReturnType = new TypeToken<Attachment>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postFile
     * @param postFileRequest  (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> File was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postFileCall(PostFileRequest postFileRequest, String organizationId, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = postFileRequest;

        // create path and map variables
        String localVarPath = "/files";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (organizationId != null) {
            localVarHeaderParams.put("Organization-Id", localVarApiClient.parameterToString(organizationId));
        }

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

        String[] localVarAuthNames = new String[] { "SecretApiKey", "JWT", "PublishableApiKey" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postFileValidateBeforeCall(PostFileRequest postFileRequest, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'postFileRequest' is set
        if (postFileRequest == null) {
            throw new ApiException("Missing the required parameter 'postFileRequest' when calling postFile(Async)");
        }

        return postFileCall(postFileRequest, organizationId, _callback);

    }

    /**
     * Create a file
     * Additionally, a file can be sent with:.  - multipart/form-data POST request: in this case all property names are the same as the JSON ones (&#x60;file&#x60; is an uploaded file)  - file body request: the file body is sent as the request body, with the appropriate &#x60;Content-Type&#x60;. No additional  properties can be set along the request data  The following file types only are allowed:  - jpg  - png  - gif  - pdf  - mp3   If using a Publishable Api Key, only private files can be created. The files can later on be modified or used using  a secret API key. 
     * @param postFileRequest  (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ModelFile
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> File was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public ModelFile postFile(PostFileRequest postFileRequest, String organizationId) throws ApiException {
        ApiResponse<ModelFile> localVarResp = postFileWithHttpInfo(postFileRequest, organizationId);
        return localVarResp.getData();
    }

    /**
     * Create a file
     * Additionally, a file can be sent with:.  - multipart/form-data POST request: in this case all property names are the same as the JSON ones (&#x60;file&#x60; is an uploaded file)  - file body request: the file body is sent as the request body, with the appropriate &#x60;Content-Type&#x60;. No additional  properties can be set along the request data  The following file types only are allowed:  - jpg  - png  - gif  - pdf  - mp3   If using a Publishable Api Key, only private files can be created. The files can later on be modified or used using  a secret API key. 
     * @param postFileRequest  (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;ModelFile&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> File was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ModelFile> postFileWithHttpInfo(PostFileRequest postFileRequest, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = postFileValidateBeforeCall(postFileRequest, organizationId, null);
        Type localVarReturnType = new TypeToken<ModelFile>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create a file (asynchronously)
     * Additionally, a file can be sent with:.  - multipart/form-data POST request: in this case all property names are the same as the JSON ones (&#x60;file&#x60; is an uploaded file)  - file body request: the file body is sent as the request body, with the appropriate &#x60;Content-Type&#x60;. No additional  properties can be set along the request data  The following file types only are allowed:  - jpg  - png  - gif  - pdf  - mp3   If using a Publishable Api Key, only private files can be created. The files can later on be modified or used using  a secret API key. 
     * @param postFileRequest  (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> File was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postFileAsync(PostFileRequest postFileRequest, String organizationId, final ApiCallback<ModelFile> _callback) throws ApiException {

        okhttp3.Call localVarCall = postFileValidateBeforeCall(postFileRequest, organizationId, _callback);
        Type localVarReturnType = new TypeToken<ModelFile>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for putAttachment
     * @param id The resource identifier string. (required)
     * @param attachment Attachment resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Attachment was updated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 201 </td><td> Attachment was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putAttachmentCall(String id, Attachment attachment, String organizationId, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = attachment;

        // create path and map variables
        String localVarPath = "/attachments/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (organizationId != null) {
            localVarHeaderParams.put("Organization-Id", localVarApiClient.parameterToString(organizationId));
        }

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

        String[] localVarAuthNames = new String[] { "SecretApiKey", "JWT" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call putAttachmentValidateBeforeCall(String id, Attachment attachment, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling putAttachment(Async)");
        }

        // verify the required parameter 'attachment' is set
        if (attachment == null) {
            throw new ApiException("Missing the required parameter 'attachment' when calling putAttachment(Async)");
        }

        return putAttachmentCall(id, attachment, organizationId, _callback);

    }

    /**
     * Update the Attachment with predefined ID
     * Update the Attachment with predefined ID. 
     * @param id The resource identifier string. (required)
     * @param attachment Attachment resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return Attachment
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Attachment was updated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 201 </td><td> Attachment was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public Attachment putAttachment(String id, Attachment attachment, String organizationId) throws ApiException {
        ApiResponse<Attachment> localVarResp = putAttachmentWithHttpInfo(id, attachment, organizationId);
        return localVarResp.getData();
    }

    /**
     * Update the Attachment with predefined ID
     * Update the Attachment with predefined ID. 
     * @param id The resource identifier string. (required)
     * @param attachment Attachment resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;Attachment&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Attachment was updated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 201 </td><td> Attachment was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Attachment> putAttachmentWithHttpInfo(String id, Attachment attachment, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = putAttachmentValidateBeforeCall(id, attachment, organizationId, null);
        Type localVarReturnType = new TypeToken<Attachment>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update the Attachment with predefined ID (asynchronously)
     * Update the Attachment with predefined ID. 
     * @param id The resource identifier string. (required)
     * @param attachment Attachment resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Attachment was updated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 201 </td><td> Attachment was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putAttachmentAsync(String id, Attachment attachment, String organizationId, final ApiCallback<Attachment> _callback) throws ApiException {

        okhttp3.Call localVarCall = putAttachmentValidateBeforeCall(id, attachment, organizationId, _callback);
        Type localVarReturnType = new TypeToken<Attachment>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for putFile
     * @param id The resource identifier string. (required)
     * @param modelFile File resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> File was updated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putFileCall(String id, ModelFile modelFile, String organizationId, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = modelFile;

        // create path and map variables
        String localVarPath = "/files/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (organizationId != null) {
            localVarHeaderParams.put("Organization-Id", localVarApiClient.parameterToString(organizationId));
        }

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

        String[] localVarAuthNames = new String[] { "SecretApiKey", "JWT" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call putFileValidateBeforeCall(String id, ModelFile modelFile, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling putFile(Async)");
        }

        // verify the required parameter 'modelFile' is set
        if (modelFile == null) {
            throw new ApiException("Missing the required parameter 'modelFile' when calling putFile(Async)");
        }

        return putFileCall(id, modelFile, organizationId, _callback);

    }

    /**
     * Update the File with predefined ID
     * Update the File with predefined ID. Note that file can be uploaded with POST. only. 
     * @param id The resource identifier string. (required)
     * @param modelFile File resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ModelFile
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> File was updated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public ModelFile putFile(String id, ModelFile modelFile, String organizationId) throws ApiException {
        ApiResponse<ModelFile> localVarResp = putFileWithHttpInfo(id, modelFile, organizationId);
        return localVarResp.getData();
    }

    /**
     * Update the File with predefined ID
     * Update the File with predefined ID. Note that file can be uploaded with POST. only. 
     * @param id The resource identifier string. (required)
     * @param modelFile File resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;ModelFile&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> File was updated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ModelFile> putFileWithHttpInfo(String id, ModelFile modelFile, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = putFileValidateBeforeCall(id, modelFile, organizationId, null);
        Type localVarReturnType = new TypeToken<ModelFile>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update the File with predefined ID (asynchronously)
     * Update the File with predefined ID. Note that file can be uploaded with POST. only. 
     * @param id The resource identifier string. (required)
     * @param modelFile File resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> File was updated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putFileAsync(String id, ModelFile modelFile, String organizationId, final ApiCallback<ModelFile> _callback) throws ApiException {

        okhttp3.Call localVarCall = putFileValidateBeforeCall(id, modelFile, organizationId, _callback);
        Type localVarReturnType = new TypeToken<ModelFile>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
