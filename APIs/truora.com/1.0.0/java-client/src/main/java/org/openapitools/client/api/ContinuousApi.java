/*
 * Checks API
 * **NOTE:** This is a preview of the API and it is not considered stable since refinements are still being made.  # Introduction  Welcome to the  **Truora Check** [**RESTful API**](https://en.wikipedia.org/wiki/Representational_state_transfer) reference. You may also want to check out our [**Validations API docs**](https://docs.validations.truora.com/) or our [**Signals API docs**](https://docs.signals.truora.com/).  Truora Check API allows performing full background checks on people, vehicles and companies. There are three main types of background checks:  - **Personal background check**: Verifies national IDs in multiple databases of public and legal entities in the LATAM region. For every national ID, returns information on: personal identity, criminal records, international background check, and professional background.  - **Vehicle background check**: Verifies the vehicle documents and the owner identity in multiple databases of public and legal entities in the LATAM region. For every vehicle and owner type, returns information on: personal identity, driving records, criminal records, and vehicle information.    - **Company background check**: Verifies the tax ID or a company name in multiple databases of public and legal entities in the LATAM region. For every company, returns the associated: business status, legal and criminal records, and media reports.  # API Key V1 is live!  API key version 1 is now live. Users with version 0 API keys are not immediately required to upgrade to V1 but should plan to do so at their earliest convenience. The changes for integration with API keys v1 are as follows:  - The field ``user_authorized`` is now required to perform person checks. This field indicates the API user has authorization to perform the check in compliance with data protection law. - The field ``homonym_scores`` is no longer included in our person check response as its results are already included in the body of the check and keeping them duplicated is generating unnecessary confusion.   # API composition  ## Endpoints  - **Check endpoints**: Provide an easy way to create and search for a background check. They also allow inserting groups of checks into reports. Each check contains scores, datasets and databases.   ```plain https://api.truora.com/v1/checks ```  - **Report endpoints**: Support batch uploads and grouping multiple checks together. Excel and .csv files are supported for batch uploads.   ```plain https://api.truora.com/v1/reports ```  - **Configuration endpoints**: Allows personalizing data sets and scores for customized background checks.  ```plain https://api.truora.com/v1/config ```  - **Continuous check endpoints**: Allows creating recurring checks and get notified whenever a change in the check score occurs.  ```plain https://api.truora.com/v1/continuous_checks ```  - **Behavior endpoints**: Allows sharing anonymous feedback about a person behavior when interacting with the company.  ```plain https://api.truora.com/v1/behaviour ```  - **Hooks endpoints**: Allows sending notifications via requests to your service or another third-party service whenever certain events occur.  ```plain https://api.truora.com/v1/hooks ```  ## Datasets  Categories that group the resulting information for background checks from databases are called datasets. Datasets are divided in:  - **Personal identity**: Corroborates the existence and validates personal identity documents.   - **Criminal record**: Checks for crimes according to each country penal code or criminal code. Keep in mind that data aged less than 10 years is usually more consistent.  - **Legal background**: Checks for lawsuits filed. Keep in mind that data aged less than 10 years is usually more consistent.  - **International background**: Checks international lists for crimes related to identity theft, money laundering, terrorist financing, and high crimes.  - **Professional background**: Checks professional regulatory entities for relevant information.  - **Affiliations and insurances**: Checks the history and status of social security affiliations.  - **Alert in media**: Checks major media agencies for relevant news related to violent actions.      - **Vehicle information**: Checks for the physical characteristics of the vehicle, technical status, insurance history, and other relevant information.  - **Traffic fines**: Checks for outstanding traffic fines.  - **Driving licenses**: Shows information relevant to the driver. Such as license status and driver certificates.  - **Business background**: Checks for business status, legal and criminal history, and other relevant information.  - **Taxes and Finances**: Checks for the information related to personal finances, liabilities, and taxes.  ## Requests Format  The POST requests receive a body that must be encoded in `www-x-form-urlencoded`, for instance:  ```plain type=person&national_id=123456&country=CO ```  The responses are always encoded in `JSON` format.  ## Errors  Whenever there is an error, a JSON with the following format is returned:  ```json {     \"code\": <Truora error code>,     \"http_code\": <The HTTP status of the response>,     \"message\": <The error message> } ```  for instance:  ```json {     \"code\": 10404,     \"http_code\": 404,     \"message\": \"The Check was not found\" } ```  ## SDKs  If your favorite language was not on the next list, You can use our [OpenAPI 3 spec](https://docs.truora.com/openapi.json) to generate it using the [Open API Generator](https://openapi-generator.tech/docs/installation).  To download the SDK click on the desired programming language:  - [C# .Net Core](https://truora-sdk.s3.amazonaws.com/checks/checks_csharp-netcore_latest.zip)  - [Elixir](https://truora-sdk.s3.amazonaws.com/checks/checks_elixir_latest.zip)  - [Go](https://truora-sdk.s3.amazonaws.com/checks/checks_go_latest.zip)  - [Java](https://truora-sdk.s3.amazonaws.com/checks/checks_java_latest.zip)  - [JavaScript](https://truora-sdk.s3.amazonaws.com/checks/checks_javascript_latest.zip)  - [Objc](https://truora-sdk.s3.amazonaws.com/checks/checks_objc_latest.zip)  - [Php](https://truora-sdk.s3.amazonaws.com/checks/checks_php_latest.zip)  - [Python](https://truora-sdk.s3.amazonaws.com/checks/checks_python_latest.zip)  - [Ruby](https://truora-sdk.s3.amazonaws.com/checks/checks_ruby_latest.zip)  You can see the full list of supported platforms here:  https://openapi-generator.tech/docs/generators   
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: api@truora.com
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
import org.openapitools.client.model.ContinuousCheck;
import org.openapitools.client.model.Error;
import org.openapitools.client.model.GetContiuousCheckHistoryOutput;
import org.openapitools.client.model.ListContinuousChecksOutput;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ContinuousApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ContinuousApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ContinuousApi(ApiClient apiClient) {
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
     * Build call for createContinuousCheck
     * @param checkId Background checks to be processed recurrently (optional)
     * @param frequency Time between background checks. It can be daily, weekly, monthly, yearly or have a custom frequency written as a number accompanied by d: day, w: week, m: month, y: year for instance: 3d: every three days, 2w: every two weeks (optional)
     * @param status Indicates whether the background checks must be processed recurrently (enabled | disabled) (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createContinuousCheckCall(String checkId, String frequency, String status, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/continuous-checks";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (checkId != null) {
            localVarFormParams.put("check_id", checkId);
        }

        if (frequency != null) {
            localVarFormParams.put("frequency", frequency);
        }

        if (status != null) {
            localVarFormParams.put("status", status);
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/x-www-form-urlencoded"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "api-key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call createContinuousCheckValidateBeforeCall(String checkId, String frequency, String status, final ApiCallback _callback) throws ApiException {
        return createContinuousCheckCall(checkId, frequency, status, _callback);

    }

    /**
     * 
     * Creates a continuous check that will run background checks recurrently according to the frequency provided.
     * @param checkId Background checks to be processed recurrently (optional)
     * @param frequency Time between background checks. It can be daily, weekly, monthly, yearly or have a custom frequency written as a number accompanied by d: day, w: week, m: month, y: year for instance: 3d: every three days, 2w: every two weeks (optional)
     * @param status Indicates whether the background checks must be processed recurrently (enabled | disabled) (optional)
     * @return ContinuousCheck
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public ContinuousCheck createContinuousCheck(String checkId, String frequency, String status) throws ApiException {
        ApiResponse<ContinuousCheck> localVarResp = createContinuousCheckWithHttpInfo(checkId, frequency, status);
        return localVarResp.getData();
    }

    /**
     * 
     * Creates a continuous check that will run background checks recurrently according to the frequency provided.
     * @param checkId Background checks to be processed recurrently (optional)
     * @param frequency Time between background checks. It can be daily, weekly, monthly, yearly or have a custom frequency written as a number accompanied by d: day, w: week, m: month, y: year for instance: 3d: every three days, 2w: every two weeks (optional)
     * @param status Indicates whether the background checks must be processed recurrently (enabled | disabled) (optional)
     * @return ApiResponse&lt;ContinuousCheck&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ContinuousCheck> createContinuousCheckWithHttpInfo(String checkId, String frequency, String status) throws ApiException {
        okhttp3.Call localVarCall = createContinuousCheckValidateBeforeCall(checkId, frequency, status, null);
        Type localVarReturnType = new TypeToken<ContinuousCheck>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Creates a continuous check that will run background checks recurrently according to the frequency provided.
     * @param checkId Background checks to be processed recurrently (optional)
     * @param frequency Time between background checks. It can be daily, weekly, monthly, yearly or have a custom frequency written as a number accompanied by d: day, w: week, m: month, y: year for instance: 3d: every three days, 2w: every two weeks (optional)
     * @param status Indicates whether the background checks must be processed recurrently (enabled | disabled) (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createContinuousCheckAsync(String checkId, String frequency, String status, final ApiCallback<ContinuousCheck> _callback) throws ApiException {

        okhttp3.Call localVarCall = createContinuousCheckValidateBeforeCall(checkId, frequency, status, _callback);
        Type localVarReturnType = new TypeToken<ContinuousCheck>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getContinuousCheck
     * @param continuousCheckId ID resulting from calling CreateContinuousCheck (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getContinuousCheckCall(BigDecimal continuousCheckId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/continuous-checks/{continuous_check_id}"
            .replace("{" + "continuous_check_id" + "}", localVarApiClient.escapeString(continuousCheckId.toString()));

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

        String[] localVarAuthNames = new String[] { "api-key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getContinuousCheckValidateBeforeCall(BigDecimal continuousCheckId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'continuousCheckId' is set
        if (continuousCheckId == null) {
            throw new ApiException("Missing the required parameter 'continuousCheckId' when calling getContinuousCheck(Async)");
        }

        return getContinuousCheckCall(continuousCheckId, _callback);

    }

    /**
     * 
     * Lists history associated with a Check. It can be paginated
     * @param continuousCheckId ID resulting from calling CreateContinuousCheck (required)
     * @return ContinuousCheck
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ContinuousCheck getContinuousCheck(BigDecimal continuousCheckId) throws ApiException {
        ApiResponse<ContinuousCheck> localVarResp = getContinuousCheckWithHttpInfo(continuousCheckId);
        return localVarResp.getData();
    }

    /**
     * 
     * Lists history associated with a Check. It can be paginated
     * @param continuousCheckId ID resulting from calling CreateContinuousCheck (required)
     * @return ApiResponse&lt;ContinuousCheck&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ContinuousCheck> getContinuousCheckWithHttpInfo(BigDecimal continuousCheckId) throws ApiException {
        okhttp3.Call localVarCall = getContinuousCheckValidateBeforeCall(continuousCheckId, null);
        Type localVarReturnType = new TypeToken<ContinuousCheck>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Lists history associated with a Check. It can be paginated
     * @param continuousCheckId ID resulting from calling CreateContinuousCheck (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getContinuousCheckAsync(BigDecimal continuousCheckId, final ApiCallback<ContinuousCheck> _callback) throws ApiException {

        okhttp3.Call localVarCall = getContinuousCheckValidateBeforeCall(continuousCheckId, _callback);
        Type localVarReturnType = new TypeToken<ContinuousCheck>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listContinuousChecks
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listContinuousChecksCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/continuous-checks";

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

        String[] localVarAuthNames = new String[] { "api-key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listContinuousChecksValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return listContinuousChecksCall(_callback);

    }

    /**
     * 
     * Lists all continuous checks
     * @return ListContinuousChecksOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ListContinuousChecksOutput listContinuousChecks() throws ApiException {
        ApiResponse<ListContinuousChecksOutput> localVarResp = listContinuousChecksWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * 
     * Lists all continuous checks
     * @return ApiResponse&lt;ListContinuousChecksOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListContinuousChecksOutput> listContinuousChecksWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = listContinuousChecksValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<ListContinuousChecksOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Lists all continuous checks
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listContinuousChecksAsync(final ApiCallback<ListContinuousChecksOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = listContinuousChecksValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<ListContinuousChecksOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateContinuousCheck
     * @param continuousCheckId ID resulting from calling CreateContinuousCheck (required)
     * @param frequency Time between background checks (required)
     * @param status Indicates whether the background checks must be processed recurrently (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateContinuousCheckCall(BigDecimal continuousCheckId, String frequency, String status, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/continuous-checks/{continuous_check_id}"
            .replace("{" + "continuous_check_id" + "}", localVarApiClient.escapeString(continuousCheckId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (frequency != null) {
            localVarFormParams.put("frequency", frequency);
        }

        if (status != null) {
            localVarFormParams.put("status", status);
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/x-www-form-urlencoded"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "api-key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updateContinuousCheckValidateBeforeCall(BigDecimal continuousCheckId, String frequency, String status, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'continuousCheckId' is set
        if (continuousCheckId == null) {
            throw new ApiException("Missing the required parameter 'continuousCheckId' when calling updateContinuousCheck(Async)");
        }

        // verify the required parameter 'frequency' is set
        if (frequency == null) {
            throw new ApiException("Missing the required parameter 'frequency' when calling updateContinuousCheck(Async)");
        }

        // verify the required parameter 'status' is set
        if (status == null) {
            throw new ApiException("Missing the required parameter 'status' when calling updateContinuousCheck(Async)");
        }

        return updateContinuousCheckCall(continuousCheckId, frequency, status, _callback);

    }

    /**
     * 
     * Updates a continuous check
     * @param continuousCheckId ID resulting from calling CreateContinuousCheck (required)
     * @param frequency Time between background checks (required)
     * @param status Indicates whether the background checks must be processed recurrently (required)
     * @return ContinuousCheck
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ContinuousCheck updateContinuousCheck(BigDecimal continuousCheckId, String frequency, String status) throws ApiException {
        ApiResponse<ContinuousCheck> localVarResp = updateContinuousCheckWithHttpInfo(continuousCheckId, frequency, status);
        return localVarResp.getData();
    }

    /**
     * 
     * Updates a continuous check
     * @param continuousCheckId ID resulting from calling CreateContinuousCheck (required)
     * @param frequency Time between background checks (required)
     * @param status Indicates whether the background checks must be processed recurrently (required)
     * @return ApiResponse&lt;ContinuousCheck&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ContinuousCheck> updateContinuousCheckWithHttpInfo(BigDecimal continuousCheckId, String frequency, String status) throws ApiException {
        okhttp3.Call localVarCall = updateContinuousCheckValidateBeforeCall(continuousCheckId, frequency, status, null);
        Type localVarReturnType = new TypeToken<ContinuousCheck>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Updates a continuous check
     * @param continuousCheckId ID resulting from calling CreateContinuousCheck (required)
     * @param frequency Time between background checks (required)
     * @param status Indicates whether the background checks must be processed recurrently (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateContinuousCheckAsync(BigDecimal continuousCheckId, String frequency, String status, final ApiCallback<ContinuousCheck> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateContinuousCheckValidateBeforeCall(continuousCheckId, frequency, status, _callback);
        Type localVarReturnType = new TypeToken<ContinuousCheck>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for v1ContinuousChecksContinuousCheckIdHistoryGet
     * @param continuousCheckId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> ok </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call v1ContinuousChecksContinuousCheckIdHistoryGetCall(String continuousCheckId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/continuous-checks/{continuous_check_id}/history"
            .replace("{" + "continuous_check_id" + "}", localVarApiClient.escapeString(continuousCheckId.toString()));

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

        String[] localVarAuthNames = new String[] { "api-key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call v1ContinuousChecksContinuousCheckIdHistoryGetValidateBeforeCall(String continuousCheckId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'continuousCheckId' is set
        if (continuousCheckId == null) {
            throw new ApiException("Missing the required parameter 'continuousCheckId' when calling v1ContinuousChecksContinuousCheckIdHistoryGet(Async)");
        }

        return v1ContinuousChecksContinuousCheckIdHistoryGetCall(continuousCheckId, _callback);

    }

    /**
     * 
     * Lists background check logs. It can be paginated  
     * @param continuousCheckId  (required)
     * @return GetContiuousCheckHistoryOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> ok </td><td>  -  </td></tr>
     </table>
     */
    public GetContiuousCheckHistoryOutput v1ContinuousChecksContinuousCheckIdHistoryGet(String continuousCheckId) throws ApiException {
        ApiResponse<GetContiuousCheckHistoryOutput> localVarResp = v1ContinuousChecksContinuousCheckIdHistoryGetWithHttpInfo(continuousCheckId);
        return localVarResp.getData();
    }

    /**
     * 
     * Lists background check logs. It can be paginated  
     * @param continuousCheckId  (required)
     * @return ApiResponse&lt;GetContiuousCheckHistoryOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> ok </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetContiuousCheckHistoryOutput> v1ContinuousChecksContinuousCheckIdHistoryGetWithHttpInfo(String continuousCheckId) throws ApiException {
        okhttp3.Call localVarCall = v1ContinuousChecksContinuousCheckIdHistoryGetValidateBeforeCall(continuousCheckId, null);
        Type localVarReturnType = new TypeToken<GetContiuousCheckHistoryOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Lists background check logs. It can be paginated  
     * @param continuousCheckId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> ok </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call v1ContinuousChecksContinuousCheckIdHistoryGetAsync(String continuousCheckId, final ApiCallback<GetContiuousCheckHistoryOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = v1ContinuousChecksContinuousCheckIdHistoryGetValidateBeforeCall(continuousCheckId, _callback);
        Type localVarReturnType = new TypeToken<GetContiuousCheckHistoryOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
