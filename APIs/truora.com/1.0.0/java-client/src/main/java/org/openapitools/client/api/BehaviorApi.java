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


import org.openapitools.client.model.BehaviourOutput;
import org.openapitools.client.model.Error;
import java.time.OffsetDateTime;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BehaviorApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public BehaviorApi() {
        this(Configuration.getDefaultApiClient());
    }

    public BehaviorApi(ApiClient apiClient) {
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
     * Build call for reportBehavior
     * @param birthDate Birth date of reported person (required)
     * @param country Document country (required)
     * @param documentId Person document ID (required)
     * @param documentType Document type associated with the background check (required)
     * @param email Reported person e-mail (required)
     * @param feedbackDate Behavior report date (required)
     * @param firstName Person first name (required)
     * @param lastName Person last name (required)
     * @param reason Report reason (required)
     * @param phoneNumber Phone number of the reported person (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td>  </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Error uploading the items </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call reportBehaviorCall(OffsetDateTime birthDate, String country, String documentId, String documentType, String email, OffsetDateTime feedbackDate, String firstName, String lastName, String reason, String phoneNumber, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/behavior";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (birthDate != null) {
            localVarFormParams.put("birth_date", birthDate);
        }

        if (country != null) {
            localVarFormParams.put("country", country);
        }

        if (documentId != null) {
            localVarFormParams.put("document_id", documentId);
        }

        if (documentType != null) {
            localVarFormParams.put("document_type", documentType);
        }

        if (email != null) {
            localVarFormParams.put("email", email);
        }

        if (feedbackDate != null) {
            localVarFormParams.put("feedback_date", feedbackDate);
        }

        if (firstName != null) {
            localVarFormParams.put("first_name", firstName);
        }

        if (lastName != null) {
            localVarFormParams.put("last_name", lastName);
        }

        if (phoneNumber != null) {
            localVarFormParams.put("phone_number", phoneNumber);
        }

        if (reason != null) {
            localVarFormParams.put("reason", reason);
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
    private okhttp3.Call reportBehaviorValidateBeforeCall(OffsetDateTime birthDate, String country, String documentId, String documentType, String email, OffsetDateTime feedbackDate, String firstName, String lastName, String reason, String phoneNumber, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'birthDate' is set
        if (birthDate == null) {
            throw new ApiException("Missing the required parameter 'birthDate' when calling reportBehavior(Async)");
        }

        // verify the required parameter 'country' is set
        if (country == null) {
            throw new ApiException("Missing the required parameter 'country' when calling reportBehavior(Async)");
        }

        // verify the required parameter 'documentId' is set
        if (documentId == null) {
            throw new ApiException("Missing the required parameter 'documentId' when calling reportBehavior(Async)");
        }

        // verify the required parameter 'documentType' is set
        if (documentType == null) {
            throw new ApiException("Missing the required parameter 'documentType' when calling reportBehavior(Async)");
        }

        // verify the required parameter 'email' is set
        if (email == null) {
            throw new ApiException("Missing the required parameter 'email' when calling reportBehavior(Async)");
        }

        // verify the required parameter 'feedbackDate' is set
        if (feedbackDate == null) {
            throw new ApiException("Missing the required parameter 'feedbackDate' when calling reportBehavior(Async)");
        }

        // verify the required parameter 'firstName' is set
        if (firstName == null) {
            throw new ApiException("Missing the required parameter 'firstName' when calling reportBehavior(Async)");
        }

        // verify the required parameter 'lastName' is set
        if (lastName == null) {
            throw new ApiException("Missing the required parameter 'lastName' when calling reportBehavior(Async)");
        }

        // verify the required parameter 'reason' is set
        if (reason == null) {
            throw new ApiException("Missing the required parameter 'reason' when calling reportBehavior(Async)");
        }

        return reportBehaviorCall(birthDate, country, documentId, documentType, email, feedbackDate, firstName, lastName, reason, phoneNumber, _callback);

    }

    /**
     * Report Behavior
     * Creates a behavior item to report employee conducts that do not or might not be included in their background check. This report includes both possitive and negative behaviors and sorts them by severity.  ### Reasons to report a person  &lt;table&gt;   &lt;tr&gt;     &lt;td style&#x3D;\&quot;width: 100px\&quot;&gt;&lt;center&gt;&lt;b&gt;Very High&lt;/b&gt;&lt;br&gt;(Score: 1)&lt;/td&gt;     &lt;td&gt;Rape, Drug Dealing, Sexual Harassment&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;High&lt;/b&gt;&lt;br&gt;(Score: 0.8)&lt;/td&gt;     &lt;td&gt;Theft, Fights, Aggressive Behaviour, Identity Fraud, Drunk, Drug Possession&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;Medium&lt;/b&gt;&lt;br&gt;(Score: 0.6)&lt;/td&gt;     &lt;td&gt;Absences&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;Low&lt;/b&gt;&lt;br&gt;(Score: 0.4)&lt;/td&gt;     &lt;td&gt;Tardiness, Confidentiality Breach&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;None&lt;/b&gt;&lt;br&gt;(Score: 0)&lt;/td&gt;     &lt;td&gt;Good Reputation&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;Unknown&lt;/b&gt;&lt;/td&gt;     &lt;td&gt;No information&lt;/td&gt;   &lt;/tr&gt; &lt;/table&gt;  **NOTE:** If the reason of your report is not here, please contact Truora support team. 
     * @param birthDate Birth date of reported person (required)
     * @param country Document country (required)
     * @param documentId Person document ID (required)
     * @param documentType Document type associated with the background check (required)
     * @param email Reported person e-mail (required)
     * @param feedbackDate Behavior report date (required)
     * @param firstName Person first name (required)
     * @param lastName Person last name (required)
     * @param reason Report reason (required)
     * @param phoneNumber Phone number of the reported person (optional)
     * @return BehaviourOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td>  </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Error uploading the items </td><td>  -  </td></tr>
     </table>
     */
    public BehaviourOutput reportBehavior(OffsetDateTime birthDate, String country, String documentId, String documentType, String email, OffsetDateTime feedbackDate, String firstName, String lastName, String reason, String phoneNumber) throws ApiException {
        ApiResponse<BehaviourOutput> localVarResp = reportBehaviorWithHttpInfo(birthDate, country, documentId, documentType, email, feedbackDate, firstName, lastName, reason, phoneNumber);
        return localVarResp.getData();
    }

    /**
     * Report Behavior
     * Creates a behavior item to report employee conducts that do not or might not be included in their background check. This report includes both possitive and negative behaviors and sorts them by severity.  ### Reasons to report a person  &lt;table&gt;   &lt;tr&gt;     &lt;td style&#x3D;\&quot;width: 100px\&quot;&gt;&lt;center&gt;&lt;b&gt;Very High&lt;/b&gt;&lt;br&gt;(Score: 1)&lt;/td&gt;     &lt;td&gt;Rape, Drug Dealing, Sexual Harassment&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;High&lt;/b&gt;&lt;br&gt;(Score: 0.8)&lt;/td&gt;     &lt;td&gt;Theft, Fights, Aggressive Behaviour, Identity Fraud, Drunk, Drug Possession&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;Medium&lt;/b&gt;&lt;br&gt;(Score: 0.6)&lt;/td&gt;     &lt;td&gt;Absences&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;Low&lt;/b&gt;&lt;br&gt;(Score: 0.4)&lt;/td&gt;     &lt;td&gt;Tardiness, Confidentiality Breach&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;None&lt;/b&gt;&lt;br&gt;(Score: 0)&lt;/td&gt;     &lt;td&gt;Good Reputation&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;Unknown&lt;/b&gt;&lt;/td&gt;     &lt;td&gt;No information&lt;/td&gt;   &lt;/tr&gt; &lt;/table&gt;  **NOTE:** If the reason of your report is not here, please contact Truora support team. 
     * @param birthDate Birth date of reported person (required)
     * @param country Document country (required)
     * @param documentId Person document ID (required)
     * @param documentType Document type associated with the background check (required)
     * @param email Reported person e-mail (required)
     * @param feedbackDate Behavior report date (required)
     * @param firstName Person first name (required)
     * @param lastName Person last name (required)
     * @param reason Report reason (required)
     * @param phoneNumber Phone number of the reported person (optional)
     * @return ApiResponse&lt;BehaviourOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td>  </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Error uploading the items </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<BehaviourOutput> reportBehaviorWithHttpInfo(OffsetDateTime birthDate, String country, String documentId, String documentType, String email, OffsetDateTime feedbackDate, String firstName, String lastName, String reason, String phoneNumber) throws ApiException {
        okhttp3.Call localVarCall = reportBehaviorValidateBeforeCall(birthDate, country, documentId, documentType, email, feedbackDate, firstName, lastName, reason, phoneNumber, null);
        Type localVarReturnType = new TypeToken<BehaviourOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Report Behavior (asynchronously)
     * Creates a behavior item to report employee conducts that do not or might not be included in their background check. This report includes both possitive and negative behaviors and sorts them by severity.  ### Reasons to report a person  &lt;table&gt;   &lt;tr&gt;     &lt;td style&#x3D;\&quot;width: 100px\&quot;&gt;&lt;center&gt;&lt;b&gt;Very High&lt;/b&gt;&lt;br&gt;(Score: 1)&lt;/td&gt;     &lt;td&gt;Rape, Drug Dealing, Sexual Harassment&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;High&lt;/b&gt;&lt;br&gt;(Score: 0.8)&lt;/td&gt;     &lt;td&gt;Theft, Fights, Aggressive Behaviour, Identity Fraud, Drunk, Drug Possession&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;Medium&lt;/b&gt;&lt;br&gt;(Score: 0.6)&lt;/td&gt;     &lt;td&gt;Absences&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;Low&lt;/b&gt;&lt;br&gt;(Score: 0.4)&lt;/td&gt;     &lt;td&gt;Tardiness, Confidentiality Breach&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;None&lt;/b&gt;&lt;br&gt;(Score: 0)&lt;/td&gt;     &lt;td&gt;Good Reputation&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;Unknown&lt;/b&gt;&lt;/td&gt;     &lt;td&gt;No information&lt;/td&gt;   &lt;/tr&gt; &lt;/table&gt;  **NOTE:** If the reason of your report is not here, please contact Truora support team. 
     * @param birthDate Birth date of reported person (required)
     * @param country Document country (required)
     * @param documentId Person document ID (required)
     * @param documentType Document type associated with the background check (required)
     * @param email Reported person e-mail (required)
     * @param feedbackDate Behavior report date (required)
     * @param firstName Person first name (required)
     * @param lastName Person last name (required)
     * @param reason Report reason (required)
     * @param phoneNumber Phone number of the reported person (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td>  </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Error uploading the items </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call reportBehaviorAsync(OffsetDateTime birthDate, String country, String documentId, String documentType, String email, OffsetDateTime feedbackDate, String firstName, String lastName, String reason, String phoneNumber, final ApiCallback<BehaviourOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = reportBehaviorValidateBeforeCall(birthDate, country, documentId, documentType, email, feedbackDate, firstName, lastName, reason, phoneNumber, _callback);
        Type localVarReturnType = new TypeToken<BehaviourOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
