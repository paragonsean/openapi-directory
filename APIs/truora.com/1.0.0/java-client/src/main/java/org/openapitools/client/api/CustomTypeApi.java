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


import org.openapitools.client.model.Error;
import org.openapitools.client.model.ScoreConfigOutput;
import org.openapitools.client.model.ScoreConfigsOutput;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CustomTypeApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public CustomTypeApi() {
        this(Configuration.getDefaultApiClient());
    }

    public CustomTypeApi(ApiClient apiClient) {
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
     * Build call for createScoreConfig
     * @param country Country where this set of rules applies. Use \\\&quot;all\\\&quot; if the check type searches by name by relying on international databases (required)
     * @param type Score configuration name. It cannot be person, vehicle, or company (required)
     * @param datasetAffiliationsAndInsurances Affiliation and insurance weight for score calculation. From 0 to 1 (optional)
     * @param datasetAlertInMedia Alert in media weight for score calculation. From 0 to 1 (optional)
     * @param datasetBusinessBackground Business background weight for score calculation. From 0 to 1 (optional)
     * @param datasetCriminalRecord Criminal record weight for score calculation. From 0 to 1 (optional)
     * @param datasetDrivingLicenses Driving license weight for score calculation. From 0 to 1 (optional)
     * @param datasetInternationalBackground International background weight for score calculation. From 0 to 1 (optional)
     * @param datasetLegalBackground Legal background weight for score calculation. From 0 to 1 (optional)
     * @param datasetPersonalIdentity Personal identity weight for score calculation. From 0 to 1 (optional)
     * @param datasetProfessionalBackground Professional background weight for score calculation. From 0 to 1 (optional)
     * @param datasetTaxesAndFinances Taxes and financial background weight for score calculation. From 0 to 1 (optional)
     * @param datasetTrafficFines Traffic fines weight for score calculation. From 0 to 1 (optional)
     * @param datasetVehicleInformation Vehicle information weight for score calculation. From 0 to 1 (optional)
     * @param datasetVehiclePermits Vehicle certificate background weight for score calculation. From 0 to 1 (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td>  </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Validation error when creating the ScoreConfig </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createScoreConfigCall(String country, String type, Float datasetAffiliationsAndInsurances, Float datasetAlertInMedia, Float datasetBusinessBackground, Float datasetCriminalRecord, Float datasetDrivingLicenses, Float datasetInternationalBackground, Float datasetLegalBackground, Float datasetPersonalIdentity, Float datasetProfessionalBackground, Float datasetTaxesAndFinances, Float datasetTrafficFines, Float datasetVehicleInformation, Float datasetVehiclePermits, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/config";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (country != null) {
            localVarFormParams.put("country", country);
        }

        if (datasetAffiliationsAndInsurances != null) {
            localVarFormParams.put("dataset_affiliations_and_insurances", datasetAffiliationsAndInsurances);
        }

        if (datasetAlertInMedia != null) {
            localVarFormParams.put("dataset_alert_in_media", datasetAlertInMedia);
        }

        if (datasetBusinessBackground != null) {
            localVarFormParams.put("dataset_business_background", datasetBusinessBackground);
        }

        if (datasetCriminalRecord != null) {
            localVarFormParams.put("dataset_criminal_record", datasetCriminalRecord);
        }

        if (datasetDrivingLicenses != null) {
            localVarFormParams.put("dataset_driving_licenses", datasetDrivingLicenses);
        }

        if (datasetInternationalBackground != null) {
            localVarFormParams.put("dataset_international_background", datasetInternationalBackground);
        }

        if (datasetLegalBackground != null) {
            localVarFormParams.put("dataset_legal_background", datasetLegalBackground);
        }

        if (datasetPersonalIdentity != null) {
            localVarFormParams.put("dataset_personal_identity", datasetPersonalIdentity);
        }

        if (datasetProfessionalBackground != null) {
            localVarFormParams.put("dataset_professional_background", datasetProfessionalBackground);
        }

        if (datasetTaxesAndFinances != null) {
            localVarFormParams.put("dataset_taxes_and_finances", datasetTaxesAndFinances);
        }

        if (datasetTrafficFines != null) {
            localVarFormParams.put("dataset_traffic_fines", datasetTrafficFines);
        }

        if (datasetVehicleInformation != null) {
            localVarFormParams.put("dataset_vehicle_information", datasetVehicleInformation);
        }

        if (datasetVehiclePermits != null) {
            localVarFormParams.put("dataset_vehicle_permits", datasetVehiclePermits);
        }

        if (type != null) {
            localVarFormParams.put("type", type);
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
    private okhttp3.Call createScoreConfigValidateBeforeCall(String country, String type, Float datasetAffiliationsAndInsurances, Float datasetAlertInMedia, Float datasetBusinessBackground, Float datasetCriminalRecord, Float datasetDrivingLicenses, Float datasetInternationalBackground, Float datasetLegalBackground, Float datasetPersonalIdentity, Float datasetProfessionalBackground, Float datasetTaxesAndFinances, Float datasetTrafficFines, Float datasetVehicleInformation, Float datasetVehiclePermits, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'country' is set
        if (country == null) {
            throw new ApiException("Missing the required parameter 'country' when calling createScoreConfig(Async)");
        }

        // verify the required parameter 'type' is set
        if (type == null) {
            throw new ApiException("Missing the required parameter 'type' when calling createScoreConfig(Async)");
        }

        return createScoreConfigCall(country, type, datasetAffiliationsAndInsurances, datasetAlertInMedia, datasetBusinessBackground, datasetCriminalRecord, datasetDrivingLicenses, datasetInternationalBackground, datasetLegalBackground, datasetPersonalIdentity, datasetProfessionalBackground, datasetTaxesAndFinances, datasetTrafficFines, datasetVehicleInformation, datasetVehiclePermits, _callback);

    }

    /**
     * Create Score Configurations
     * Create a custom score configuration selecting the weight for each background check dataset and the country where it applies. Weights are numbers between 0 and 1 that represent how impactful the dataset is for the score. Keep in mind that the sum of all weights must equal 1.
     * @param country Country where this set of rules applies. Use \\\&quot;all\\\&quot; if the check type searches by name by relying on international databases (required)
     * @param type Score configuration name. It cannot be person, vehicle, or company (required)
     * @param datasetAffiliationsAndInsurances Affiliation and insurance weight for score calculation. From 0 to 1 (optional)
     * @param datasetAlertInMedia Alert in media weight for score calculation. From 0 to 1 (optional)
     * @param datasetBusinessBackground Business background weight for score calculation. From 0 to 1 (optional)
     * @param datasetCriminalRecord Criminal record weight for score calculation. From 0 to 1 (optional)
     * @param datasetDrivingLicenses Driving license weight for score calculation. From 0 to 1 (optional)
     * @param datasetInternationalBackground International background weight for score calculation. From 0 to 1 (optional)
     * @param datasetLegalBackground Legal background weight for score calculation. From 0 to 1 (optional)
     * @param datasetPersonalIdentity Personal identity weight for score calculation. From 0 to 1 (optional)
     * @param datasetProfessionalBackground Professional background weight for score calculation. From 0 to 1 (optional)
     * @param datasetTaxesAndFinances Taxes and financial background weight for score calculation. From 0 to 1 (optional)
     * @param datasetTrafficFines Traffic fines weight for score calculation. From 0 to 1 (optional)
     * @param datasetVehicleInformation Vehicle information weight for score calculation. From 0 to 1 (optional)
     * @param datasetVehiclePermits Vehicle certificate background weight for score calculation. From 0 to 1 (optional)
     * @return ScoreConfigOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td>  </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Validation error when creating the ScoreConfig </td><td>  -  </td></tr>
     </table>
     */
    public ScoreConfigOutput createScoreConfig(String country, String type, Float datasetAffiliationsAndInsurances, Float datasetAlertInMedia, Float datasetBusinessBackground, Float datasetCriminalRecord, Float datasetDrivingLicenses, Float datasetInternationalBackground, Float datasetLegalBackground, Float datasetPersonalIdentity, Float datasetProfessionalBackground, Float datasetTaxesAndFinances, Float datasetTrafficFines, Float datasetVehicleInformation, Float datasetVehiclePermits) throws ApiException {
        ApiResponse<ScoreConfigOutput> localVarResp = createScoreConfigWithHttpInfo(country, type, datasetAffiliationsAndInsurances, datasetAlertInMedia, datasetBusinessBackground, datasetCriminalRecord, datasetDrivingLicenses, datasetInternationalBackground, datasetLegalBackground, datasetPersonalIdentity, datasetProfessionalBackground, datasetTaxesAndFinances, datasetTrafficFines, datasetVehicleInformation, datasetVehiclePermits);
        return localVarResp.getData();
    }

    /**
     * Create Score Configurations
     * Create a custom score configuration selecting the weight for each background check dataset and the country where it applies. Weights are numbers between 0 and 1 that represent how impactful the dataset is for the score. Keep in mind that the sum of all weights must equal 1.
     * @param country Country where this set of rules applies. Use \\\&quot;all\\\&quot; if the check type searches by name by relying on international databases (required)
     * @param type Score configuration name. It cannot be person, vehicle, or company (required)
     * @param datasetAffiliationsAndInsurances Affiliation and insurance weight for score calculation. From 0 to 1 (optional)
     * @param datasetAlertInMedia Alert in media weight for score calculation. From 0 to 1 (optional)
     * @param datasetBusinessBackground Business background weight for score calculation. From 0 to 1 (optional)
     * @param datasetCriminalRecord Criminal record weight for score calculation. From 0 to 1 (optional)
     * @param datasetDrivingLicenses Driving license weight for score calculation. From 0 to 1 (optional)
     * @param datasetInternationalBackground International background weight for score calculation. From 0 to 1 (optional)
     * @param datasetLegalBackground Legal background weight for score calculation. From 0 to 1 (optional)
     * @param datasetPersonalIdentity Personal identity weight for score calculation. From 0 to 1 (optional)
     * @param datasetProfessionalBackground Professional background weight for score calculation. From 0 to 1 (optional)
     * @param datasetTaxesAndFinances Taxes and financial background weight for score calculation. From 0 to 1 (optional)
     * @param datasetTrafficFines Traffic fines weight for score calculation. From 0 to 1 (optional)
     * @param datasetVehicleInformation Vehicle information weight for score calculation. From 0 to 1 (optional)
     * @param datasetVehiclePermits Vehicle certificate background weight for score calculation. From 0 to 1 (optional)
     * @return ApiResponse&lt;ScoreConfigOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td>  </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Validation error when creating the ScoreConfig </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ScoreConfigOutput> createScoreConfigWithHttpInfo(String country, String type, Float datasetAffiliationsAndInsurances, Float datasetAlertInMedia, Float datasetBusinessBackground, Float datasetCriminalRecord, Float datasetDrivingLicenses, Float datasetInternationalBackground, Float datasetLegalBackground, Float datasetPersonalIdentity, Float datasetProfessionalBackground, Float datasetTaxesAndFinances, Float datasetTrafficFines, Float datasetVehicleInformation, Float datasetVehiclePermits) throws ApiException {
        okhttp3.Call localVarCall = createScoreConfigValidateBeforeCall(country, type, datasetAffiliationsAndInsurances, datasetAlertInMedia, datasetBusinessBackground, datasetCriminalRecord, datasetDrivingLicenses, datasetInternationalBackground, datasetLegalBackground, datasetPersonalIdentity, datasetProfessionalBackground, datasetTaxesAndFinances, datasetTrafficFines, datasetVehicleInformation, datasetVehiclePermits, null);
        Type localVarReturnType = new TypeToken<ScoreConfigOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create Score Configurations (asynchronously)
     * Create a custom score configuration selecting the weight for each background check dataset and the country where it applies. Weights are numbers between 0 and 1 that represent how impactful the dataset is for the score. Keep in mind that the sum of all weights must equal 1.
     * @param country Country where this set of rules applies. Use \\\&quot;all\\\&quot; if the check type searches by name by relying on international databases (required)
     * @param type Score configuration name. It cannot be person, vehicle, or company (required)
     * @param datasetAffiliationsAndInsurances Affiliation and insurance weight for score calculation. From 0 to 1 (optional)
     * @param datasetAlertInMedia Alert in media weight for score calculation. From 0 to 1 (optional)
     * @param datasetBusinessBackground Business background weight for score calculation. From 0 to 1 (optional)
     * @param datasetCriminalRecord Criminal record weight for score calculation. From 0 to 1 (optional)
     * @param datasetDrivingLicenses Driving license weight for score calculation. From 0 to 1 (optional)
     * @param datasetInternationalBackground International background weight for score calculation. From 0 to 1 (optional)
     * @param datasetLegalBackground Legal background weight for score calculation. From 0 to 1 (optional)
     * @param datasetPersonalIdentity Personal identity weight for score calculation. From 0 to 1 (optional)
     * @param datasetProfessionalBackground Professional background weight for score calculation. From 0 to 1 (optional)
     * @param datasetTaxesAndFinances Taxes and financial background weight for score calculation. From 0 to 1 (optional)
     * @param datasetTrafficFines Traffic fines weight for score calculation. From 0 to 1 (optional)
     * @param datasetVehicleInformation Vehicle information weight for score calculation. From 0 to 1 (optional)
     * @param datasetVehiclePermits Vehicle certificate background weight for score calculation. From 0 to 1 (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td>  </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Validation error when creating the ScoreConfig </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createScoreConfigAsync(String country, String type, Float datasetAffiliationsAndInsurances, Float datasetAlertInMedia, Float datasetBusinessBackground, Float datasetCriminalRecord, Float datasetDrivingLicenses, Float datasetInternationalBackground, Float datasetLegalBackground, Float datasetPersonalIdentity, Float datasetProfessionalBackground, Float datasetTaxesAndFinances, Float datasetTrafficFines, Float datasetVehicleInformation, Float datasetVehiclePermits, final ApiCallback<ScoreConfigOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = createScoreConfigValidateBeforeCall(country, type, datasetAffiliationsAndInsurances, datasetAlertInMedia, datasetBusinessBackground, datasetCriminalRecord, datasetDrivingLicenses, datasetInternationalBackground, datasetLegalBackground, datasetPersonalIdentity, datasetProfessionalBackground, datasetTaxesAndFinances, datasetTrafficFines, datasetVehicleInformation, datasetVehiclePermits, _callback);
        Type localVarReturnType = new TypeToken<ScoreConfigOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteCustomType
     * @param type Name of the custom type to be deleted (required)
     * @param country Country where the custom type is valid (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteCustomTypeCall(String type, String country, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/config";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (type != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("type", type));
        }

        if (country != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("country", country));
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

        String[] localVarAuthNames = new String[] { "api-key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteCustomTypeValidateBeforeCall(String type, String country, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'type' is set
        if (type == null) {
            throw new ApiException("Missing the required parameter 'type' when calling deleteCustomType(Async)");
        }

        return deleteCustomTypeCall(type, country, _callback);

    }

    /**
     * Delete Custom Type
     * Allows deleting a custom type. Person, vehicle, and company types cannot be deleted
     * @param type Name of the custom type to be deleted (required)
     * @param country Country where the custom type is valid (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void deleteCustomType(String type, String country) throws ApiException {
        deleteCustomTypeWithHttpInfo(type, country);
    }

    /**
     * Delete Custom Type
     * Allows deleting a custom type. Person, vehicle, and company types cannot be deleted
     * @param type Name of the custom type to be deleted (required)
     * @param country Country where the custom type is valid (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteCustomTypeWithHttpInfo(String type, String country) throws ApiException {
        okhttp3.Call localVarCall = deleteCustomTypeValidateBeforeCall(type, country, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete Custom Type (asynchronously)
     * Allows deleting a custom type. Person, vehicle, and company types cannot be deleted
     * @param type Name of the custom type to be deleted (required)
     * @param country Country where the custom type is valid (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteCustomTypeAsync(String type, String country, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteCustomTypeValidateBeforeCall(type, country, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for listScoreConfigs
     * @param startKey The key to start the pagination (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listScoreConfigsCall(String startKey, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/config";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (startKey != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("start_key", startKey));
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

        String[] localVarAuthNames = new String[] { "api-key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listScoreConfigsValidateBeforeCall(String startKey, final ApiCallback _callback) throws ApiException {
        return listScoreConfigsCall(startKey, _callback);

    }

    /**
     * List Score Configurations
     * Lists the custom score configurations of the associated account.
     * @param startKey The key to start the pagination (optional)
     * @return ScoreConfigsOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ScoreConfigsOutput listScoreConfigs(String startKey) throws ApiException {
        ApiResponse<ScoreConfigsOutput> localVarResp = listScoreConfigsWithHttpInfo(startKey);
        return localVarResp.getData();
    }

    /**
     * List Score Configurations
     * Lists the custom score configurations of the associated account.
     * @param startKey The key to start the pagination (optional)
     * @return ApiResponse&lt;ScoreConfigsOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ScoreConfigsOutput> listScoreConfigsWithHttpInfo(String startKey) throws ApiException {
        okhttp3.Call localVarCall = listScoreConfigsValidateBeforeCall(startKey, null);
        Type localVarReturnType = new TypeToken<ScoreConfigsOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List Score Configurations (asynchronously)
     * Lists the custom score configurations of the associated account.
     * @param startKey The key to start the pagination (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listScoreConfigsAsync(String startKey, final ApiCallback<ScoreConfigsOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = listScoreConfigsValidateBeforeCall(startKey, _callback);
        Type localVarReturnType = new TypeToken<ScoreConfigsOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateCustomType
     * @param country Country where this set of rules applies. Use \\\&quot;all\\\&quot; if the check type searches by name by relying on international databases (required)
     * @param type Score configuration name. It cannot be person, vehicle, or company (required)
     * @param datasetAffiliationsAndInsurances Affiliation and insurance weight for score calculation. From 0 to 1 (optional)
     * @param datasetAlertInMedia Alert in media weight for score calculation. From 0 to 1 (optional)
     * @param datasetBusinessBackground Business background weight for score calculation. From 0 to 1 (optional)
     * @param datasetCriminalRecord Criminal record weight for score calculation. From 0 to 1 (optional)
     * @param datasetDrivingLicenses Driving license weight for score calculation. From 0 to 1 (optional)
     * @param datasetInternationalBackground International background weight for score calculation. From 0 to 1 (optional)
     * @param datasetLegalBackground Legal background weight for score calculation. From 0 to 1 (optional)
     * @param datasetPersonalIdentity Personal identity weight for score calculation. From 0 to 1 (optional)
     * @param datasetProfessionalBackground Professional background weight for score calculation. From 0 to 1 (optional)
     * @param datasetTaxesAndFinances Taxes and financial background weight for score calculation. From 0 to 1 (optional)
     * @param datasetTrafficFines Traffic fines weight for score calculation. From 0 to 1 (optional)
     * @param datasetVehicleInformation Vehicle information weight for score calculation. From 0 to 1 (optional)
     * @param datasetVehiclePermits Vehicle certificate background weight for score calculation. From 0 to 1 (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateCustomTypeCall(String country, String type, Float datasetAffiliationsAndInsurances, Float datasetAlertInMedia, Float datasetBusinessBackground, Float datasetCriminalRecord, Float datasetDrivingLicenses, Float datasetInternationalBackground, Float datasetLegalBackground, Float datasetPersonalIdentity, Float datasetProfessionalBackground, Float datasetTaxesAndFinances, Float datasetTrafficFines, Float datasetVehicleInformation, Float datasetVehiclePermits, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/config";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (country != null) {
            localVarFormParams.put("country", country);
        }

        if (datasetAffiliationsAndInsurances != null) {
            localVarFormParams.put("dataset_affiliations_and_insurances", datasetAffiliationsAndInsurances);
        }

        if (datasetAlertInMedia != null) {
            localVarFormParams.put("dataset_alert_in_media", datasetAlertInMedia);
        }

        if (datasetBusinessBackground != null) {
            localVarFormParams.put("dataset_business_background", datasetBusinessBackground);
        }

        if (datasetCriminalRecord != null) {
            localVarFormParams.put("dataset_criminal_record", datasetCriminalRecord);
        }

        if (datasetDrivingLicenses != null) {
            localVarFormParams.put("dataset_driving_licenses", datasetDrivingLicenses);
        }

        if (datasetInternationalBackground != null) {
            localVarFormParams.put("dataset_international_background", datasetInternationalBackground);
        }

        if (datasetLegalBackground != null) {
            localVarFormParams.put("dataset_legal_background", datasetLegalBackground);
        }

        if (datasetPersonalIdentity != null) {
            localVarFormParams.put("dataset_personal_identity", datasetPersonalIdentity);
        }

        if (datasetProfessionalBackground != null) {
            localVarFormParams.put("dataset_professional_background", datasetProfessionalBackground);
        }

        if (datasetTaxesAndFinances != null) {
            localVarFormParams.put("dataset_taxes_and_finances", datasetTaxesAndFinances);
        }

        if (datasetTrafficFines != null) {
            localVarFormParams.put("dataset_traffic_fines", datasetTrafficFines);
        }

        if (datasetVehicleInformation != null) {
            localVarFormParams.put("dataset_vehicle_information", datasetVehicleInformation);
        }

        if (datasetVehiclePermits != null) {
            localVarFormParams.put("dataset_vehicle_permits", datasetVehiclePermits);
        }

        if (type != null) {
            localVarFormParams.put("type", type);
        }

        final String[] localVarAccepts = {
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
    private okhttp3.Call updateCustomTypeValidateBeforeCall(String country, String type, Float datasetAffiliationsAndInsurances, Float datasetAlertInMedia, Float datasetBusinessBackground, Float datasetCriminalRecord, Float datasetDrivingLicenses, Float datasetInternationalBackground, Float datasetLegalBackground, Float datasetPersonalIdentity, Float datasetProfessionalBackground, Float datasetTaxesAndFinances, Float datasetTrafficFines, Float datasetVehicleInformation, Float datasetVehiclePermits, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'country' is set
        if (country == null) {
            throw new ApiException("Missing the required parameter 'country' when calling updateCustomType(Async)");
        }

        // verify the required parameter 'type' is set
        if (type == null) {
            throw new ApiException("Missing the required parameter 'type' when calling updateCustomType(Async)");
        }

        return updateCustomTypeCall(country, type, datasetAffiliationsAndInsurances, datasetAlertInMedia, datasetBusinessBackground, datasetCriminalRecord, datasetDrivingLicenses, datasetInternationalBackground, datasetLegalBackground, datasetPersonalIdentity, datasetProfessionalBackground, datasetTaxesAndFinances, datasetTrafficFines, datasetVehicleInformation, datasetVehiclePermits, _callback);

    }

    /**
     * Update Custom Type
     * Allows updating a custom type. Person, vehicle, and company types are not modifiable
     * @param country Country where this set of rules applies. Use \\\&quot;all\\\&quot; if the check type searches by name by relying on international databases (required)
     * @param type Score configuration name. It cannot be person, vehicle, or company (required)
     * @param datasetAffiliationsAndInsurances Affiliation and insurance weight for score calculation. From 0 to 1 (optional)
     * @param datasetAlertInMedia Alert in media weight for score calculation. From 0 to 1 (optional)
     * @param datasetBusinessBackground Business background weight for score calculation. From 0 to 1 (optional)
     * @param datasetCriminalRecord Criminal record weight for score calculation. From 0 to 1 (optional)
     * @param datasetDrivingLicenses Driving license weight for score calculation. From 0 to 1 (optional)
     * @param datasetInternationalBackground International background weight for score calculation. From 0 to 1 (optional)
     * @param datasetLegalBackground Legal background weight for score calculation. From 0 to 1 (optional)
     * @param datasetPersonalIdentity Personal identity weight for score calculation. From 0 to 1 (optional)
     * @param datasetProfessionalBackground Professional background weight for score calculation. From 0 to 1 (optional)
     * @param datasetTaxesAndFinances Taxes and financial background weight for score calculation. From 0 to 1 (optional)
     * @param datasetTrafficFines Traffic fines weight for score calculation. From 0 to 1 (optional)
     * @param datasetVehicleInformation Vehicle information weight for score calculation. From 0 to 1 (optional)
     * @param datasetVehiclePermits Vehicle certificate background weight for score calculation. From 0 to 1 (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void updateCustomType(String country, String type, Float datasetAffiliationsAndInsurances, Float datasetAlertInMedia, Float datasetBusinessBackground, Float datasetCriminalRecord, Float datasetDrivingLicenses, Float datasetInternationalBackground, Float datasetLegalBackground, Float datasetPersonalIdentity, Float datasetProfessionalBackground, Float datasetTaxesAndFinances, Float datasetTrafficFines, Float datasetVehicleInformation, Float datasetVehiclePermits) throws ApiException {
        updateCustomTypeWithHttpInfo(country, type, datasetAffiliationsAndInsurances, datasetAlertInMedia, datasetBusinessBackground, datasetCriminalRecord, datasetDrivingLicenses, datasetInternationalBackground, datasetLegalBackground, datasetPersonalIdentity, datasetProfessionalBackground, datasetTaxesAndFinances, datasetTrafficFines, datasetVehicleInformation, datasetVehiclePermits);
    }

    /**
     * Update Custom Type
     * Allows updating a custom type. Person, vehicle, and company types are not modifiable
     * @param country Country where this set of rules applies. Use \\\&quot;all\\\&quot; if the check type searches by name by relying on international databases (required)
     * @param type Score configuration name. It cannot be person, vehicle, or company (required)
     * @param datasetAffiliationsAndInsurances Affiliation and insurance weight for score calculation. From 0 to 1 (optional)
     * @param datasetAlertInMedia Alert in media weight for score calculation. From 0 to 1 (optional)
     * @param datasetBusinessBackground Business background weight for score calculation. From 0 to 1 (optional)
     * @param datasetCriminalRecord Criminal record weight for score calculation. From 0 to 1 (optional)
     * @param datasetDrivingLicenses Driving license weight for score calculation. From 0 to 1 (optional)
     * @param datasetInternationalBackground International background weight for score calculation. From 0 to 1 (optional)
     * @param datasetLegalBackground Legal background weight for score calculation. From 0 to 1 (optional)
     * @param datasetPersonalIdentity Personal identity weight for score calculation. From 0 to 1 (optional)
     * @param datasetProfessionalBackground Professional background weight for score calculation. From 0 to 1 (optional)
     * @param datasetTaxesAndFinances Taxes and financial background weight for score calculation. From 0 to 1 (optional)
     * @param datasetTrafficFines Traffic fines weight for score calculation. From 0 to 1 (optional)
     * @param datasetVehicleInformation Vehicle information weight for score calculation. From 0 to 1 (optional)
     * @param datasetVehiclePermits Vehicle certificate background weight for score calculation. From 0 to 1 (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> updateCustomTypeWithHttpInfo(String country, String type, Float datasetAffiliationsAndInsurances, Float datasetAlertInMedia, Float datasetBusinessBackground, Float datasetCriminalRecord, Float datasetDrivingLicenses, Float datasetInternationalBackground, Float datasetLegalBackground, Float datasetPersonalIdentity, Float datasetProfessionalBackground, Float datasetTaxesAndFinances, Float datasetTrafficFines, Float datasetVehicleInformation, Float datasetVehiclePermits) throws ApiException {
        okhttp3.Call localVarCall = updateCustomTypeValidateBeforeCall(country, type, datasetAffiliationsAndInsurances, datasetAlertInMedia, datasetBusinessBackground, datasetCriminalRecord, datasetDrivingLicenses, datasetInternationalBackground, datasetLegalBackground, datasetPersonalIdentity, datasetProfessionalBackground, datasetTaxesAndFinances, datasetTrafficFines, datasetVehicleInformation, datasetVehiclePermits, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Update Custom Type (asynchronously)
     * Allows updating a custom type. Person, vehicle, and company types are not modifiable
     * @param country Country where this set of rules applies. Use \\\&quot;all\\\&quot; if the check type searches by name by relying on international databases (required)
     * @param type Score configuration name. It cannot be person, vehicle, or company (required)
     * @param datasetAffiliationsAndInsurances Affiliation and insurance weight for score calculation. From 0 to 1 (optional)
     * @param datasetAlertInMedia Alert in media weight for score calculation. From 0 to 1 (optional)
     * @param datasetBusinessBackground Business background weight for score calculation. From 0 to 1 (optional)
     * @param datasetCriminalRecord Criminal record weight for score calculation. From 0 to 1 (optional)
     * @param datasetDrivingLicenses Driving license weight for score calculation. From 0 to 1 (optional)
     * @param datasetInternationalBackground International background weight for score calculation. From 0 to 1 (optional)
     * @param datasetLegalBackground Legal background weight for score calculation. From 0 to 1 (optional)
     * @param datasetPersonalIdentity Personal identity weight for score calculation. From 0 to 1 (optional)
     * @param datasetProfessionalBackground Professional background weight for score calculation. From 0 to 1 (optional)
     * @param datasetTaxesAndFinances Taxes and financial background weight for score calculation. From 0 to 1 (optional)
     * @param datasetTrafficFines Traffic fines weight for score calculation. From 0 to 1 (optional)
     * @param datasetVehicleInformation Vehicle information weight for score calculation. From 0 to 1 (optional)
     * @param datasetVehiclePermits Vehicle certificate background weight for score calculation. From 0 to 1 (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateCustomTypeAsync(String country, String type, Float datasetAffiliationsAndInsurances, Float datasetAlertInMedia, Float datasetBusinessBackground, Float datasetCriminalRecord, Float datasetDrivingLicenses, Float datasetInternationalBackground, Float datasetLegalBackground, Float datasetPersonalIdentity, Float datasetProfessionalBackground, Float datasetTaxesAndFinances, Float datasetTrafficFines, Float datasetVehicleInformation, Float datasetVehiclePermits, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateCustomTypeValidateBeforeCall(country, type, datasetAffiliationsAndInsurances, datasetAlertInMedia, datasetBusinessBackground, datasetCriminalRecord, datasetDrivingLicenses, datasetInternationalBackground, datasetLegalBackground, datasetPersonalIdentity, datasetProfessionalBackground, datasetTaxesAndFinances, datasetTrafficFines, datasetVehicleInformation, datasetVehiclePermits, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
