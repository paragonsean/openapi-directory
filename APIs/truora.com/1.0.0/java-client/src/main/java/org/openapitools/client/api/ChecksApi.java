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


import org.openapitools.client.model.CheckDetailsOutput;
import org.openapitools.client.model.CheckOutput;
import org.openapitools.client.model.ChecksOutput;
import org.openapitools.client.model.Database;
import org.openapitools.client.model.Error;
import java.time.LocalDate;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ChecksApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ChecksApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ChecksApi(ApiClient apiClient) {
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
     * Build call for createCheck
     * @param country Document country (required)
     * @param type Background check type (required)
     * @param truoraPriority Describes the background check priority. The amount of high priority checks is limited by country. Medium priority is used by default (optional)
     * @param birthCertificate Person birth certificate (optional)
     * @param companyName Company name \\\&quot;Don&#39;t forget this required field to complete background checks in Brazil\\\&quot; (optional)
     * @param dateOfBirth Person birthdate. This date is used to get some additional information about a person and to filter homonyms in some cases. YYYY-MM-DD format, Required for complete background checks in Brazil (optional)
     * @param diplomaticId Diplomatic ID (optional)
     * @param driverLicense Driver&#39;s license number (optional)
     * @param escrow Colombian escrow (optional)
     * @param firstName Person or entity first name. If the document type and number are not provided, the report might include homonyms. Required when searching by first name, Required in order to get complete background checks in Brazil (optional)
     * @param forceCreation Forces a new background check creation when true. Reuses recently created background checks otherwise (optional)
     * @param foreignId Person foreign ID (optional)
     * @param issueDate Person document issue date in \\\&quot;YYYY-mm-dd\\\&quot; format (e.g. 2008-12-31) . This date is used to get some additional information about a person in some cases (optional)
     * @param lastName Person or entity last name. If the document type and number are not provided, the report might include homonyms. Required when searching by last name. Required in order to get complete background checks in Brazil (optional)
     * @param licensePlate Vehicle license plate (optional)
     * @param nationalId National ID (optional)
     * @param nativeCountry Country of birth (optional)
     * @param ownerDocumentId National ID of the vehicle owner (optional)
     * @param ownerDocumentType National ID, foreign ID, or tax ID (optional)
     * @param passport Person passport (optional)
     * @param paymentDate Payment day of a vehicle circulation permit (Chile only) (optional)
     * @param pep ID for Venezuelans working in Colombia (optional)
     * @param phoneNumber Person phone number. Required by law to notify the person their background is being checked (optional)
     * @param professionalCard Professional ID card (optional)
     * @param ptp ID for Venezuelans working in Peru (optional)
     * @param region Region where the background is to be checked in addition to the region where the person is from. By default, background checks in Brazil are performed in the region where the person is from. Required for Brazil only. Allowed values are: DF: Distrito Federal, AC: Acre, AL: Alagoas, AP: Amapá, AM: Amazonas, BA: Bahía, CE: Ceará, ES: Espírito Santo, GO: Goiás, MA: Maranhão, MT: Mato Grosso, MS: Mato Grosso do Sul, MG: Minas Gerais, PA: Pará, PB: Paraíba, PR: Paraná, PE: Pernambuco, PI: Piauí, RJ: Río de Janeiro, RN: Río Grande do Norte, RS: Río Grande do Sul, RO: Rondônia, RR: Roraima, SC: Santa Catarina, SP: São Paulo, SE: Sergipe, TO : Tocantins. (optional)
     * @param reportId Report ID the background check will be inserted into (optional)
     * @param stateId  Used for the RG (Registro Geral) identification in Brazil. This identification has different formats according to the state that issues the document. It can have numbers and letters but other characters (- * , . ) are omitted, Required in order to get complete background checks in Brazil (optional)
     * @param taxId Company ID used for tax payments (optional)
     * @param userAuthorized Indicates whether the person subject to the validation authorized the validation. Must be true in order to proceed [Required for API key V1 or later] (optional)
     * @param vehicleId Vehicle license plate (optional)
     * @param verificationCode Verification code registered for criminal records in Peru only (optional)
     * @param watch Indicates whether the check score is to be periodically revised and its frequency. It can be daily, weekly, monthly, yearly or have a custom frequency written as a number accompanied by d: day, w: week, m: month, y: year for instance: 3d: every three days, 2w: every two weeks. Ignore this field if the check is only to be performed once (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Click to view/hide response structure </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Validation error, at least one of the parameters was invalid. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> There are too many high priority background checks being processed. Please try again later. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createCheckCall(String country, String type, String truoraPriority, String birthCertificate, String companyName, LocalDate dateOfBirth, String diplomaticId, String driverLicense, String escrow, String firstName, Boolean forceCreation, String foreignId, LocalDate issueDate, String lastName, String licensePlate, String nationalId, String nativeCountry, String ownerDocumentId, String ownerDocumentType, String passport, LocalDate paymentDate, String pep, String phoneNumber, String professionalCard, String ptp, String region, String reportId, String stateId, String taxId, Boolean userAuthorized, String vehicleId, String verificationCode, String watch, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/checks";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (birthCertificate != null) {
            localVarFormParams.put("birth_certificate", birthCertificate);
        }

        if (companyName != null) {
            localVarFormParams.put("company_name", companyName);
        }

        if (country != null) {
            localVarFormParams.put("country", country);
        }

        if (dateOfBirth != null) {
            localVarFormParams.put("date_of_birth", dateOfBirth);
        }

        if (diplomaticId != null) {
            localVarFormParams.put("diplomatic_id", diplomaticId);
        }

        if (driverLicense != null) {
            localVarFormParams.put("driver_license", driverLicense);
        }

        if (escrow != null) {
            localVarFormParams.put("escrow", escrow);
        }

        if (firstName != null) {
            localVarFormParams.put("first_name", firstName);
        }

        if (forceCreation != null) {
            localVarFormParams.put("force_creation", forceCreation);
        }

        if (foreignId != null) {
            localVarFormParams.put("foreign_id", foreignId);
        }

        if (issueDate != null) {
            localVarFormParams.put("issue_date", issueDate);
        }

        if (lastName != null) {
            localVarFormParams.put("last_name", lastName);
        }

        if (licensePlate != null) {
            localVarFormParams.put("license_plate", licensePlate);
        }

        if (nationalId != null) {
            localVarFormParams.put("national_id", nationalId);
        }

        if (nativeCountry != null) {
            localVarFormParams.put("native_country", nativeCountry);
        }

        if (ownerDocumentId != null) {
            localVarFormParams.put("owner_document_id", ownerDocumentId);
        }

        if (ownerDocumentType != null) {
            localVarFormParams.put("owner_document_type", ownerDocumentType);
        }

        if (passport != null) {
            localVarFormParams.put("passport", passport);
        }

        if (paymentDate != null) {
            localVarFormParams.put("payment_date", paymentDate);
        }

        if (pep != null) {
            localVarFormParams.put("pep", pep);
        }

        if (phoneNumber != null) {
            localVarFormParams.put("phone_number", phoneNumber);
        }

        if (professionalCard != null) {
            localVarFormParams.put("professional_card", professionalCard);
        }

        if (ptp != null) {
            localVarFormParams.put("ptp", ptp);
        }

        if (region != null) {
            localVarFormParams.put("region", region);
        }

        if (reportId != null) {
            localVarFormParams.put("report_id", reportId);
        }

        if (stateId != null) {
            localVarFormParams.put("state_id", stateId);
        }

        if (taxId != null) {
            localVarFormParams.put("tax_id", taxId);
        }

        if (type != null) {
            localVarFormParams.put("type", type);
        }

        if (userAuthorized != null) {
            localVarFormParams.put("user_authorized", userAuthorized);
        }

        if (vehicleId != null) {
            localVarFormParams.put("vehicle_id", vehicleId);
        }

        if (verificationCode != null) {
            localVarFormParams.put("verification_code", verificationCode);
        }

        if (watch != null) {
            localVarFormParams.put("watch", watch);
        }

        if (truoraPriority != null) {
            localVarHeaderParams.put("Truora-Priority", localVarApiClient.parameterToString(truoraPriority));
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
    private okhttp3.Call createCheckValidateBeforeCall(String country, String type, String truoraPriority, String birthCertificate, String companyName, LocalDate dateOfBirth, String diplomaticId, String driverLicense, String escrow, String firstName, Boolean forceCreation, String foreignId, LocalDate issueDate, String lastName, String licensePlate, String nationalId, String nativeCountry, String ownerDocumentId, String ownerDocumentType, String passport, LocalDate paymentDate, String pep, String phoneNumber, String professionalCard, String ptp, String region, String reportId, String stateId, String taxId, Boolean userAuthorized, String vehicleId, String verificationCode, String watch, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'country' is set
        if (country == null) {
            throw new ApiException("Missing the required parameter 'country' when calling createCheck(Async)");
        }

        // verify the required parameter 'type' is set
        if (type == null) {
            throw new ApiException("Missing the required parameter 'type' when calling createCheck(Async)");
        }

        return createCheckCall(country, type, truoraPriority, birthCertificate, companyName, dateOfBirth, diplomaticId, driverLicense, escrow, firstName, forceCreation, foreignId, issueDate, lastName, licensePlate, nationalId, nativeCountry, ownerDocumentId, ownerDocumentType, passport, paymentDate, pep, phoneNumber, professionalCard, ptp, region, reportId, stateId, taxId, userAuthorized, vehicleId, verificationCode, watch, _callback);

    }

    /**
     * Create a background check
     * Creates a background check and queues it to start collecting information. The full details of background checks can be retrieved with their respective Check IDs using getCheck endpoint. Keep in mind that, depending on the check type, input document, and country of a search, certain inputs are required. You should always provide as many inputs as possible in order to get the highest accuracy.  If your check type is not referenced in the following table, please reach out to find out the fields that apply for you.  | Country | Person-National | PersonForeigner | Company | Vehicle-National | Vehicle-Foreigner | |:-------:|:---------------:|:---------------:|:-------:|:----------------:|:-----------------:| | Chile&lt;br&gt;CL | national_id*&lt;br&gt;date_of_birth&lt;br&gt;phone_number | foreign_id*&lt;br&gt;date_of_birth*&lt;br&gt;phone_number&lt;br&gt;first_name*&lt;br&gt;last_name*&lt;br&gt;native_country* | N/A | national_id*&lt;br&gt;license_plate*&lt;br&gt;payment_date (Santiago only)&lt;br&gt;driver_license (Santiago only) | foreign_id*&lt;br&gt;first_name*&lt;br&gt;last_name*&lt;br&gt;date_of_birth*&lt;br&gt;native_country*&lt;br&gt;license_plate*&lt;br&gt;payment_date (Santiago only)&lt;br&gt;driver_license (Santiago only) | | Colombia&lt;br&gt;CO | national_id*&lt;br&gt;date_of_birth&lt;br&gt;issue_date&lt;br&gt;phone_number | foreign_id* or PEP*&lt;br&gt;date_of_birth&lt;br&gt;phone_number&lt;br&gt;issue_date* | tax_id*&lt;br&gt;national_id | national_id*&lt;br&gt;date_of_birth&lt;br&gt;phone_number&lt;br&gt;license_plate*&lt;br&gt;owner_document_type&lt;br&gt;owner_document_id | foreign_id*&lt;br&gt;date_of_birth&lt;br&gt;phone_number&lt;br&gt;license_plate*&lt;br&gt;issue_date* | | Mexico&lt;br&gt;MX | national_id*&lt;br&gt;phone_number | foreign_id* | tax_id* | license_plate*&lt;br&gt;national_id&lt;br&gt;vehicle_id&lt;br&gt;driver_license(Estado de Mexico only) | N/A | | Brazil&lt;br&gt;BR | national_id*&lt;br&gt;date_of_birth*&lt;br&gt;region*&lt;br&gt;phone_number | N/A | tax_id* | license_plate* | N/A | | Costa Rica&lt;br&gt;CR | national_id*&lt;br&gt;phone_number | foreign_id* | N/A | license_plate* | N/A | | Ecuador&lt;br&gt;EC | national_id*&lt;br&gt;phone_number | foreign_id* | tax_id* | license_plate* | N/A | | Peru&lt;br&gt;PE | national_id*&lt;br&gt;date_of_birth&lt;br&gt;phone_number | foreign_id*&lt;br&gt;ptp&lt;br&gt;date_of_birth*&lt;br&gt;phone_number | N/A | national_id*&lt;br&gt;date_of_birth&lt;br&gt;license_plate* | foreign_id*&lt;br&gt;ptp&lt;br&gt;date_of_birth*&lt;br&gt;license_plate* | | Argentina&lt;br&gt;AR | national_id* | N/A | N/A | national_id* | N/A | | International&lt;br&gt;ALL | name* | name* | company_name* | N/A | N/A |  (*) Required field
     * @param country Document country (required)
     * @param type Background check type (required)
     * @param truoraPriority Describes the background check priority. The amount of high priority checks is limited by country. Medium priority is used by default (optional)
     * @param birthCertificate Person birth certificate (optional)
     * @param companyName Company name \\\&quot;Don&#39;t forget this required field to complete background checks in Brazil\\\&quot; (optional)
     * @param dateOfBirth Person birthdate. This date is used to get some additional information about a person and to filter homonyms in some cases. YYYY-MM-DD format, Required for complete background checks in Brazil (optional)
     * @param diplomaticId Diplomatic ID (optional)
     * @param driverLicense Driver&#39;s license number (optional)
     * @param escrow Colombian escrow (optional)
     * @param firstName Person or entity first name. If the document type and number are not provided, the report might include homonyms. Required when searching by first name, Required in order to get complete background checks in Brazil (optional)
     * @param forceCreation Forces a new background check creation when true. Reuses recently created background checks otherwise (optional)
     * @param foreignId Person foreign ID (optional)
     * @param issueDate Person document issue date in \\\&quot;YYYY-mm-dd\\\&quot; format (e.g. 2008-12-31) . This date is used to get some additional information about a person in some cases (optional)
     * @param lastName Person or entity last name. If the document type and number are not provided, the report might include homonyms. Required when searching by last name. Required in order to get complete background checks in Brazil (optional)
     * @param licensePlate Vehicle license plate (optional)
     * @param nationalId National ID (optional)
     * @param nativeCountry Country of birth (optional)
     * @param ownerDocumentId National ID of the vehicle owner (optional)
     * @param ownerDocumentType National ID, foreign ID, or tax ID (optional)
     * @param passport Person passport (optional)
     * @param paymentDate Payment day of a vehicle circulation permit (Chile only) (optional)
     * @param pep ID for Venezuelans working in Colombia (optional)
     * @param phoneNumber Person phone number. Required by law to notify the person their background is being checked (optional)
     * @param professionalCard Professional ID card (optional)
     * @param ptp ID for Venezuelans working in Peru (optional)
     * @param region Region where the background is to be checked in addition to the region where the person is from. By default, background checks in Brazil are performed in the region where the person is from. Required for Brazil only. Allowed values are: DF: Distrito Federal, AC: Acre, AL: Alagoas, AP: Amapá, AM: Amazonas, BA: Bahía, CE: Ceará, ES: Espírito Santo, GO: Goiás, MA: Maranhão, MT: Mato Grosso, MS: Mato Grosso do Sul, MG: Minas Gerais, PA: Pará, PB: Paraíba, PR: Paraná, PE: Pernambuco, PI: Piauí, RJ: Río de Janeiro, RN: Río Grande do Norte, RS: Río Grande do Sul, RO: Rondônia, RR: Roraima, SC: Santa Catarina, SP: São Paulo, SE: Sergipe, TO : Tocantins. (optional)
     * @param reportId Report ID the background check will be inserted into (optional)
     * @param stateId  Used for the RG (Registro Geral) identification in Brazil. This identification has different formats according to the state that issues the document. It can have numbers and letters but other characters (- * , . ) are omitted, Required in order to get complete background checks in Brazil (optional)
     * @param taxId Company ID used for tax payments (optional)
     * @param userAuthorized Indicates whether the person subject to the validation authorized the validation. Must be true in order to proceed [Required for API key V1 or later] (optional)
     * @param vehicleId Vehicle license plate (optional)
     * @param verificationCode Verification code registered for criminal records in Peru only (optional)
     * @param watch Indicates whether the check score is to be periodically revised and its frequency. It can be daily, weekly, monthly, yearly or have a custom frequency written as a number accompanied by d: day, w: week, m: month, y: year for instance: 3d: every three days, 2w: every two weeks. Ignore this field if the check is only to be performed once (optional)
     * @return CheckOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Click to view/hide response structure </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Validation error, at least one of the parameters was invalid. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> There are too many high priority background checks being processed. Please try again later. </td><td>  -  </td></tr>
     </table>
     */
    public CheckOutput createCheck(String country, String type, String truoraPriority, String birthCertificate, String companyName, LocalDate dateOfBirth, String diplomaticId, String driverLicense, String escrow, String firstName, Boolean forceCreation, String foreignId, LocalDate issueDate, String lastName, String licensePlate, String nationalId, String nativeCountry, String ownerDocumentId, String ownerDocumentType, String passport, LocalDate paymentDate, String pep, String phoneNumber, String professionalCard, String ptp, String region, String reportId, String stateId, String taxId, Boolean userAuthorized, String vehicleId, String verificationCode, String watch) throws ApiException {
        ApiResponse<CheckOutput> localVarResp = createCheckWithHttpInfo(country, type, truoraPriority, birthCertificate, companyName, dateOfBirth, diplomaticId, driverLicense, escrow, firstName, forceCreation, foreignId, issueDate, lastName, licensePlate, nationalId, nativeCountry, ownerDocumentId, ownerDocumentType, passport, paymentDate, pep, phoneNumber, professionalCard, ptp, region, reportId, stateId, taxId, userAuthorized, vehicleId, verificationCode, watch);
        return localVarResp.getData();
    }

    /**
     * Create a background check
     * Creates a background check and queues it to start collecting information. The full details of background checks can be retrieved with their respective Check IDs using getCheck endpoint. Keep in mind that, depending on the check type, input document, and country of a search, certain inputs are required. You should always provide as many inputs as possible in order to get the highest accuracy.  If your check type is not referenced in the following table, please reach out to find out the fields that apply for you.  | Country | Person-National | PersonForeigner | Company | Vehicle-National | Vehicle-Foreigner | |:-------:|:---------------:|:---------------:|:-------:|:----------------:|:-----------------:| | Chile&lt;br&gt;CL | national_id*&lt;br&gt;date_of_birth&lt;br&gt;phone_number | foreign_id*&lt;br&gt;date_of_birth*&lt;br&gt;phone_number&lt;br&gt;first_name*&lt;br&gt;last_name*&lt;br&gt;native_country* | N/A | national_id*&lt;br&gt;license_plate*&lt;br&gt;payment_date (Santiago only)&lt;br&gt;driver_license (Santiago only) | foreign_id*&lt;br&gt;first_name*&lt;br&gt;last_name*&lt;br&gt;date_of_birth*&lt;br&gt;native_country*&lt;br&gt;license_plate*&lt;br&gt;payment_date (Santiago only)&lt;br&gt;driver_license (Santiago only) | | Colombia&lt;br&gt;CO | national_id*&lt;br&gt;date_of_birth&lt;br&gt;issue_date&lt;br&gt;phone_number | foreign_id* or PEP*&lt;br&gt;date_of_birth&lt;br&gt;phone_number&lt;br&gt;issue_date* | tax_id*&lt;br&gt;national_id | national_id*&lt;br&gt;date_of_birth&lt;br&gt;phone_number&lt;br&gt;license_plate*&lt;br&gt;owner_document_type&lt;br&gt;owner_document_id | foreign_id*&lt;br&gt;date_of_birth&lt;br&gt;phone_number&lt;br&gt;license_plate*&lt;br&gt;issue_date* | | Mexico&lt;br&gt;MX | national_id*&lt;br&gt;phone_number | foreign_id* | tax_id* | license_plate*&lt;br&gt;national_id&lt;br&gt;vehicle_id&lt;br&gt;driver_license(Estado de Mexico only) | N/A | | Brazil&lt;br&gt;BR | national_id*&lt;br&gt;date_of_birth*&lt;br&gt;region*&lt;br&gt;phone_number | N/A | tax_id* | license_plate* | N/A | | Costa Rica&lt;br&gt;CR | national_id*&lt;br&gt;phone_number | foreign_id* | N/A | license_plate* | N/A | | Ecuador&lt;br&gt;EC | national_id*&lt;br&gt;phone_number | foreign_id* | tax_id* | license_plate* | N/A | | Peru&lt;br&gt;PE | national_id*&lt;br&gt;date_of_birth&lt;br&gt;phone_number | foreign_id*&lt;br&gt;ptp&lt;br&gt;date_of_birth*&lt;br&gt;phone_number | N/A | national_id*&lt;br&gt;date_of_birth&lt;br&gt;license_plate* | foreign_id*&lt;br&gt;ptp&lt;br&gt;date_of_birth*&lt;br&gt;license_plate* | | Argentina&lt;br&gt;AR | national_id* | N/A | N/A | national_id* | N/A | | International&lt;br&gt;ALL | name* | name* | company_name* | N/A | N/A |  (*) Required field
     * @param country Document country (required)
     * @param type Background check type (required)
     * @param truoraPriority Describes the background check priority. The amount of high priority checks is limited by country. Medium priority is used by default (optional)
     * @param birthCertificate Person birth certificate (optional)
     * @param companyName Company name \\\&quot;Don&#39;t forget this required field to complete background checks in Brazil\\\&quot; (optional)
     * @param dateOfBirth Person birthdate. This date is used to get some additional information about a person and to filter homonyms in some cases. YYYY-MM-DD format, Required for complete background checks in Brazil (optional)
     * @param diplomaticId Diplomatic ID (optional)
     * @param driverLicense Driver&#39;s license number (optional)
     * @param escrow Colombian escrow (optional)
     * @param firstName Person or entity first name. If the document type and number are not provided, the report might include homonyms. Required when searching by first name, Required in order to get complete background checks in Brazil (optional)
     * @param forceCreation Forces a new background check creation when true. Reuses recently created background checks otherwise (optional)
     * @param foreignId Person foreign ID (optional)
     * @param issueDate Person document issue date in \\\&quot;YYYY-mm-dd\\\&quot; format (e.g. 2008-12-31) . This date is used to get some additional information about a person in some cases (optional)
     * @param lastName Person or entity last name. If the document type and number are not provided, the report might include homonyms. Required when searching by last name. Required in order to get complete background checks in Brazil (optional)
     * @param licensePlate Vehicle license plate (optional)
     * @param nationalId National ID (optional)
     * @param nativeCountry Country of birth (optional)
     * @param ownerDocumentId National ID of the vehicle owner (optional)
     * @param ownerDocumentType National ID, foreign ID, or tax ID (optional)
     * @param passport Person passport (optional)
     * @param paymentDate Payment day of a vehicle circulation permit (Chile only) (optional)
     * @param pep ID for Venezuelans working in Colombia (optional)
     * @param phoneNumber Person phone number. Required by law to notify the person their background is being checked (optional)
     * @param professionalCard Professional ID card (optional)
     * @param ptp ID for Venezuelans working in Peru (optional)
     * @param region Region where the background is to be checked in addition to the region where the person is from. By default, background checks in Brazil are performed in the region where the person is from. Required for Brazil only. Allowed values are: DF: Distrito Federal, AC: Acre, AL: Alagoas, AP: Amapá, AM: Amazonas, BA: Bahía, CE: Ceará, ES: Espírito Santo, GO: Goiás, MA: Maranhão, MT: Mato Grosso, MS: Mato Grosso do Sul, MG: Minas Gerais, PA: Pará, PB: Paraíba, PR: Paraná, PE: Pernambuco, PI: Piauí, RJ: Río de Janeiro, RN: Río Grande do Norte, RS: Río Grande do Sul, RO: Rondônia, RR: Roraima, SC: Santa Catarina, SP: São Paulo, SE: Sergipe, TO : Tocantins. (optional)
     * @param reportId Report ID the background check will be inserted into (optional)
     * @param stateId  Used for the RG (Registro Geral) identification in Brazil. This identification has different formats according to the state that issues the document. It can have numbers and letters but other characters (- * , . ) are omitted, Required in order to get complete background checks in Brazil (optional)
     * @param taxId Company ID used for tax payments (optional)
     * @param userAuthorized Indicates whether the person subject to the validation authorized the validation. Must be true in order to proceed [Required for API key V1 or later] (optional)
     * @param vehicleId Vehicle license plate (optional)
     * @param verificationCode Verification code registered for criminal records in Peru only (optional)
     * @param watch Indicates whether the check score is to be periodically revised and its frequency. It can be daily, weekly, monthly, yearly or have a custom frequency written as a number accompanied by d: day, w: week, m: month, y: year for instance: 3d: every three days, 2w: every two weeks. Ignore this field if the check is only to be performed once (optional)
     * @return ApiResponse&lt;CheckOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Click to view/hide response structure </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Validation error, at least one of the parameters was invalid. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> There are too many high priority background checks being processed. Please try again later. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CheckOutput> createCheckWithHttpInfo(String country, String type, String truoraPriority, String birthCertificate, String companyName, LocalDate dateOfBirth, String diplomaticId, String driverLicense, String escrow, String firstName, Boolean forceCreation, String foreignId, LocalDate issueDate, String lastName, String licensePlate, String nationalId, String nativeCountry, String ownerDocumentId, String ownerDocumentType, String passport, LocalDate paymentDate, String pep, String phoneNumber, String professionalCard, String ptp, String region, String reportId, String stateId, String taxId, Boolean userAuthorized, String vehicleId, String verificationCode, String watch) throws ApiException {
        okhttp3.Call localVarCall = createCheckValidateBeforeCall(country, type, truoraPriority, birthCertificate, companyName, dateOfBirth, diplomaticId, driverLicense, escrow, firstName, forceCreation, foreignId, issueDate, lastName, licensePlate, nationalId, nativeCountry, ownerDocumentId, ownerDocumentType, passport, paymentDate, pep, phoneNumber, professionalCard, ptp, region, reportId, stateId, taxId, userAuthorized, vehicleId, verificationCode, watch, null);
        Type localVarReturnType = new TypeToken<CheckOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create a background check (asynchronously)
     * Creates a background check and queues it to start collecting information. The full details of background checks can be retrieved with their respective Check IDs using getCheck endpoint. Keep in mind that, depending on the check type, input document, and country of a search, certain inputs are required. You should always provide as many inputs as possible in order to get the highest accuracy.  If your check type is not referenced in the following table, please reach out to find out the fields that apply for you.  | Country | Person-National | PersonForeigner | Company | Vehicle-National | Vehicle-Foreigner | |:-------:|:---------------:|:---------------:|:-------:|:----------------:|:-----------------:| | Chile&lt;br&gt;CL | national_id*&lt;br&gt;date_of_birth&lt;br&gt;phone_number | foreign_id*&lt;br&gt;date_of_birth*&lt;br&gt;phone_number&lt;br&gt;first_name*&lt;br&gt;last_name*&lt;br&gt;native_country* | N/A | national_id*&lt;br&gt;license_plate*&lt;br&gt;payment_date (Santiago only)&lt;br&gt;driver_license (Santiago only) | foreign_id*&lt;br&gt;first_name*&lt;br&gt;last_name*&lt;br&gt;date_of_birth*&lt;br&gt;native_country*&lt;br&gt;license_plate*&lt;br&gt;payment_date (Santiago only)&lt;br&gt;driver_license (Santiago only) | | Colombia&lt;br&gt;CO | national_id*&lt;br&gt;date_of_birth&lt;br&gt;issue_date&lt;br&gt;phone_number | foreign_id* or PEP*&lt;br&gt;date_of_birth&lt;br&gt;phone_number&lt;br&gt;issue_date* | tax_id*&lt;br&gt;national_id | national_id*&lt;br&gt;date_of_birth&lt;br&gt;phone_number&lt;br&gt;license_plate*&lt;br&gt;owner_document_type&lt;br&gt;owner_document_id | foreign_id*&lt;br&gt;date_of_birth&lt;br&gt;phone_number&lt;br&gt;license_plate*&lt;br&gt;issue_date* | | Mexico&lt;br&gt;MX | national_id*&lt;br&gt;phone_number | foreign_id* | tax_id* | license_plate*&lt;br&gt;national_id&lt;br&gt;vehicle_id&lt;br&gt;driver_license(Estado de Mexico only) | N/A | | Brazil&lt;br&gt;BR | national_id*&lt;br&gt;date_of_birth*&lt;br&gt;region*&lt;br&gt;phone_number | N/A | tax_id* | license_plate* | N/A | | Costa Rica&lt;br&gt;CR | national_id*&lt;br&gt;phone_number | foreign_id* | N/A | license_plate* | N/A | | Ecuador&lt;br&gt;EC | national_id*&lt;br&gt;phone_number | foreign_id* | tax_id* | license_plate* | N/A | | Peru&lt;br&gt;PE | national_id*&lt;br&gt;date_of_birth&lt;br&gt;phone_number | foreign_id*&lt;br&gt;ptp&lt;br&gt;date_of_birth*&lt;br&gt;phone_number | N/A | national_id*&lt;br&gt;date_of_birth&lt;br&gt;license_plate* | foreign_id*&lt;br&gt;ptp&lt;br&gt;date_of_birth*&lt;br&gt;license_plate* | | Argentina&lt;br&gt;AR | national_id* | N/A | N/A | national_id* | N/A | | International&lt;br&gt;ALL | name* | name* | company_name* | N/A | N/A |  (*) Required field
     * @param country Document country (required)
     * @param type Background check type (required)
     * @param truoraPriority Describes the background check priority. The amount of high priority checks is limited by country. Medium priority is used by default (optional)
     * @param birthCertificate Person birth certificate (optional)
     * @param companyName Company name \\\&quot;Don&#39;t forget this required field to complete background checks in Brazil\\\&quot; (optional)
     * @param dateOfBirth Person birthdate. This date is used to get some additional information about a person and to filter homonyms in some cases. YYYY-MM-DD format, Required for complete background checks in Brazil (optional)
     * @param diplomaticId Diplomatic ID (optional)
     * @param driverLicense Driver&#39;s license number (optional)
     * @param escrow Colombian escrow (optional)
     * @param firstName Person or entity first name. If the document type and number are not provided, the report might include homonyms. Required when searching by first name, Required in order to get complete background checks in Brazil (optional)
     * @param forceCreation Forces a new background check creation when true. Reuses recently created background checks otherwise (optional)
     * @param foreignId Person foreign ID (optional)
     * @param issueDate Person document issue date in \\\&quot;YYYY-mm-dd\\\&quot; format (e.g. 2008-12-31) . This date is used to get some additional information about a person in some cases (optional)
     * @param lastName Person or entity last name. If the document type and number are not provided, the report might include homonyms. Required when searching by last name. Required in order to get complete background checks in Brazil (optional)
     * @param licensePlate Vehicle license plate (optional)
     * @param nationalId National ID (optional)
     * @param nativeCountry Country of birth (optional)
     * @param ownerDocumentId National ID of the vehicle owner (optional)
     * @param ownerDocumentType National ID, foreign ID, or tax ID (optional)
     * @param passport Person passport (optional)
     * @param paymentDate Payment day of a vehicle circulation permit (Chile only) (optional)
     * @param pep ID for Venezuelans working in Colombia (optional)
     * @param phoneNumber Person phone number. Required by law to notify the person their background is being checked (optional)
     * @param professionalCard Professional ID card (optional)
     * @param ptp ID for Venezuelans working in Peru (optional)
     * @param region Region where the background is to be checked in addition to the region where the person is from. By default, background checks in Brazil are performed in the region where the person is from. Required for Brazil only. Allowed values are: DF: Distrito Federal, AC: Acre, AL: Alagoas, AP: Amapá, AM: Amazonas, BA: Bahía, CE: Ceará, ES: Espírito Santo, GO: Goiás, MA: Maranhão, MT: Mato Grosso, MS: Mato Grosso do Sul, MG: Minas Gerais, PA: Pará, PB: Paraíba, PR: Paraná, PE: Pernambuco, PI: Piauí, RJ: Río de Janeiro, RN: Río Grande do Norte, RS: Río Grande do Sul, RO: Rondônia, RR: Roraima, SC: Santa Catarina, SP: São Paulo, SE: Sergipe, TO : Tocantins. (optional)
     * @param reportId Report ID the background check will be inserted into (optional)
     * @param stateId  Used for the RG (Registro Geral) identification in Brazil. This identification has different formats according to the state that issues the document. It can have numbers and letters but other characters (- * , . ) are omitted, Required in order to get complete background checks in Brazil (optional)
     * @param taxId Company ID used for tax payments (optional)
     * @param userAuthorized Indicates whether the person subject to the validation authorized the validation. Must be true in order to proceed [Required for API key V1 or later] (optional)
     * @param vehicleId Vehicle license plate (optional)
     * @param verificationCode Verification code registered for criminal records in Peru only (optional)
     * @param watch Indicates whether the check score is to be periodically revised and its frequency. It can be daily, weekly, monthly, yearly or have a custom frequency written as a number accompanied by d: day, w: week, m: month, y: year for instance: 3d: every three days, 2w: every two weeks. Ignore this field if the check is only to be performed once (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Click to view/hide response structure </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Validation error, at least one of the parameters was invalid. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> There are too many high priority background checks being processed. Please try again later. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createCheckAsync(String country, String type, String truoraPriority, String birthCertificate, String companyName, LocalDate dateOfBirth, String diplomaticId, String driverLicense, String escrow, String firstName, Boolean forceCreation, String foreignId, LocalDate issueDate, String lastName, String licensePlate, String nationalId, String nativeCountry, String ownerDocumentId, String ownerDocumentType, String passport, LocalDate paymentDate, String pep, String phoneNumber, String professionalCard, String ptp, String region, String reportId, String stateId, String taxId, Boolean userAuthorized, String vehicleId, String verificationCode, String watch, final ApiCallback<CheckOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = createCheckValidateBeforeCall(country, type, truoraPriority, birthCertificate, companyName, dateOfBirth, diplomaticId, driverLicense, escrow, firstName, forceCreation, foreignId, issueDate, lastName, licensePlate, nationalId, nativeCountry, ownerDocumentId, ownerDocumentType, passport, paymentDate, pep, phoneNumber, professionalCard, ptp, region, reportId, stateId, taxId, userAuthorized, vehicleId, verificationCode, watch, _callback);
        Type localVarReturnType = new TypeToken<CheckOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getCheck
     * @param checkId Check ID (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The Check was not found with the given ID </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getCheckCall(String checkId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/checks/{check_id}"
            .replace("{" + "check_id" + "}", localVarApiClient.escapeString(checkId.toString()));

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
    private okhttp3.Call getCheckValidateBeforeCall(String checkId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'checkId' is set
        if (checkId == null) {
            throw new ApiException("Missing the required parameter 'checkId' when calling getCheck(Async)");
        }

        return getCheckCall(checkId, _callback);

    }

    /**
     * Get Background Check
     * Returns the results of the check that matches the ID provided, complete with a set of scores explained below.  ### Scores:   - **Global Score**: Average risk associated with a person, company or vehicle, according to  the background check results. The global score considers results that are validated with the  ID number provided. The score ranges from 0 to 1, where 0 represents high risk and 1 low risk.   - **ID Score**: Average risk associated with a person according to the background check  results. The ID score considers the results that are validated with a person identity  document. The score ranges from 0 to 1, where 0 represents high risk and 1 low risk.    - **Homonym Score**: Average risk associated with a person according to the background check  results. The homonym score considers results that are validated against the name of a person and could not be validated with their ID number. These results might have homonyms associated with them. The score ranges from 0 to 1, where 0 represents high risk and 1 low risk.   In order to calculate these scores, a weighted average is considered with different weights allocated to each dataset. Scores can be customized using the config endpoints by assigning a weight to each dataset according to its relevance.  Keep in mind that results from the API vary depending on the country, check type and the inputs entered on check creation.
     * @param checkId Check ID (required)
     * @return CheckOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The Check was not found with the given ID </td><td>  -  </td></tr>
     </table>
     */
    public CheckOutput getCheck(String checkId) throws ApiException {
        ApiResponse<CheckOutput> localVarResp = getCheckWithHttpInfo(checkId);
        return localVarResp.getData();
    }

    /**
     * Get Background Check
     * Returns the results of the check that matches the ID provided, complete with a set of scores explained below.  ### Scores:   - **Global Score**: Average risk associated with a person, company or vehicle, according to  the background check results. The global score considers results that are validated with the  ID number provided. The score ranges from 0 to 1, where 0 represents high risk and 1 low risk.   - **ID Score**: Average risk associated with a person according to the background check  results. The ID score considers the results that are validated with a person identity  document. The score ranges from 0 to 1, where 0 represents high risk and 1 low risk.    - **Homonym Score**: Average risk associated with a person according to the background check  results. The homonym score considers results that are validated against the name of a person and could not be validated with their ID number. These results might have homonyms associated with them. The score ranges from 0 to 1, where 0 represents high risk and 1 low risk.   In order to calculate these scores, a weighted average is considered with different weights allocated to each dataset. Scores can be customized using the config endpoints by assigning a weight to each dataset according to its relevance.  Keep in mind that results from the API vary depending on the country, check type and the inputs entered on check creation.
     * @param checkId Check ID (required)
     * @return ApiResponse&lt;CheckOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The Check was not found with the given ID </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CheckOutput> getCheckWithHttpInfo(String checkId) throws ApiException {
        okhttp3.Call localVarCall = getCheckValidateBeforeCall(checkId, null);
        Type localVarReturnType = new TypeToken<CheckOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Background Check (asynchronously)
     * Returns the results of the check that matches the ID provided, complete with a set of scores explained below.  ### Scores:   - **Global Score**: Average risk associated with a person, company or vehicle, according to  the background check results. The global score considers results that are validated with the  ID number provided. The score ranges from 0 to 1, where 0 represents high risk and 1 low risk.   - **ID Score**: Average risk associated with a person according to the background check  results. The ID score considers the results that are validated with a person identity  document. The score ranges from 0 to 1, where 0 represents high risk and 1 low risk.    - **Homonym Score**: Average risk associated with a person according to the background check  results. The homonym score considers results that are validated against the name of a person and could not be validated with their ID number. These results might have homonyms associated with them. The score ranges from 0 to 1, where 0 represents high risk and 1 low risk.   In order to calculate these scores, a weighted average is considered with different weights allocated to each dataset. Scores can be customized using the config endpoints by assigning a weight to each dataset according to its relevance.  Keep in mind that results from the API vary depending on the country, check type and the inputs entered on check creation.
     * @param checkId Check ID (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The Check was not found with the given ID </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getCheckAsync(String checkId, final ApiCallback<CheckOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = getCheckValidateBeforeCall(checkId, _callback);
        Type localVarReturnType = new TypeToken<CheckOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getHealthDashboard
     * @param country Country in ISO 3166, uppercase (optional)
     * @param unixTimestampSeconds Unix timestamp in seconds. Send a day timestamp to view the database hourly status for that day or send the current time to know the current database status (optional)
     * @param unixtimezoneOffsetSeconds Offset between the local time and the UTC time in seconds. (e.g., Colombia is at UTC -18000 seconds)   (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getHealthDashboardCall(String country, String unixTimestampSeconds, String unixtimezoneOffsetSeconds, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/checks/health";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (country != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("country", country));
        }

        if (unixTimestampSeconds != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("unixTimestampSeconds", unixTimestampSeconds));
        }

        if (unixtimezoneOffsetSeconds != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("unixtimezoneOffsetSeconds", unixtimezoneOffsetSeconds));
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
    private okhttp3.Call getHealthDashboardValidateBeforeCall(String country, String unixTimestampSeconds, String unixtimezoneOffsetSeconds, final ApiCallback _callback) throws ApiException {
        return getHealthDashboardCall(country, unixTimestampSeconds, unixtimezoneOffsetSeconds, _callback);

    }

    /**
     * Get Health Dashboard
     * Get the status of a database
     * @param country Country in ISO 3166, uppercase (optional)
     * @param unixTimestampSeconds Unix timestamp in seconds. Send a day timestamp to view the database hourly status for that day or send the current time to know the current database status (optional)
     * @param unixtimezoneOffsetSeconds Offset between the local time and the UTC time in seconds. (e.g., Colombia is at UTC -18000 seconds)   (optional)
     * @return List&lt;Database&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public List<Database> getHealthDashboard(String country, String unixTimestampSeconds, String unixtimezoneOffsetSeconds) throws ApiException {
        ApiResponse<List<Database>> localVarResp = getHealthDashboardWithHttpInfo(country, unixTimestampSeconds, unixtimezoneOffsetSeconds);
        return localVarResp.getData();
    }

    /**
     * Get Health Dashboard
     * Get the status of a database
     * @param country Country in ISO 3166, uppercase (optional)
     * @param unixTimestampSeconds Unix timestamp in seconds. Send a day timestamp to view the database hourly status for that day or send the current time to know the current database status (optional)
     * @param unixtimezoneOffsetSeconds Offset between the local time and the UTC time in seconds. (e.g., Colombia is at UTC -18000 seconds)   (optional)
     * @return ApiResponse&lt;List&lt;Database&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<Database>> getHealthDashboardWithHttpInfo(String country, String unixTimestampSeconds, String unixtimezoneOffsetSeconds) throws ApiException {
        okhttp3.Call localVarCall = getHealthDashboardValidateBeforeCall(country, unixTimestampSeconds, unixtimezoneOffsetSeconds, null);
        Type localVarReturnType = new TypeToken<List<Database>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Health Dashboard (asynchronously)
     * Get the status of a database
     * @param country Country in ISO 3166, uppercase (optional)
     * @param unixTimestampSeconds Unix timestamp in seconds. Send a day timestamp to view the database hourly status for that day or send the current time to know the current database status (optional)
     * @param unixtimezoneOffsetSeconds Offset between the local time and the UTC time in seconds. (e.g., Colombia is at UTC -18000 seconds)   (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getHealthDashboardAsync(String country, String unixTimestampSeconds, String unixtimezoneOffsetSeconds, final ApiCallback<List<Database>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getHealthDashboardValidateBeforeCall(country, unixTimestampSeconds, unixtimezoneOffsetSeconds, _callback);
        Type localVarReturnType = new TypeToken<List<Database>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listCheckDetails
     * @param checkId ID of the Check (required)
     * @param startKey Start key value for the pagination (optional)
     * @param lang This parameter is used to specify the language wanted for details, if not specified details will come in their original language. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listCheckDetailsCall(String checkId, String startKey, String lang, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/checks/{check_id}/details"
            .replace("{" + "check_id" + "}", localVarApiClient.escapeString(checkId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (startKey != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("start_key", startKey));
        }

        if (lang != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("lang", lang));
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
    private okhttp3.Call listCheckDetailsValidateBeforeCall(String checkId, String startKey, String lang, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'checkId' is set
        if (checkId == null) {
            throw new ApiException("Missing the required parameter 'checkId' when calling listCheckDetails(Async)");
        }

        return listCheckDetailsCall(checkId, startKey, lang, _callback);

    }

    /**
     * List Check Details
     * Lists all details associated with a Check. It can be paginated.
     * @param checkId ID of the Check (required)
     * @param startKey Start key value for the pagination (optional)
     * @param lang This parameter is used to specify the language wanted for details, if not specified details will come in their original language. (optional)
     * @return CheckDetailsOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public CheckDetailsOutput listCheckDetails(String checkId, String startKey, String lang) throws ApiException {
        ApiResponse<CheckDetailsOutput> localVarResp = listCheckDetailsWithHttpInfo(checkId, startKey, lang);
        return localVarResp.getData();
    }

    /**
     * List Check Details
     * Lists all details associated with a Check. It can be paginated.
     * @param checkId ID of the Check (required)
     * @param startKey Start key value for the pagination (optional)
     * @param lang This parameter is used to specify the language wanted for details, if not specified details will come in their original language. (optional)
     * @return ApiResponse&lt;CheckDetailsOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CheckDetailsOutput> listCheckDetailsWithHttpInfo(String checkId, String startKey, String lang) throws ApiException {
        okhttp3.Call localVarCall = listCheckDetailsValidateBeforeCall(checkId, startKey, lang, null);
        Type localVarReturnType = new TypeToken<CheckDetailsOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List Check Details (asynchronously)
     * Lists all details associated with a Check. It can be paginated.
     * @param checkId ID of the Check (required)
     * @param startKey Start key value for the pagination (optional)
     * @param lang This parameter is used to specify the language wanted for details, if not specified details will come in their original language. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listCheckDetailsAsync(String checkId, String startKey, String lang, final ApiCallback<CheckDetailsOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = listCheckDetailsValidateBeforeCall(checkId, startKey, lang, _callback);
        Type localVarReturnType = new TypeToken<CheckDetailsOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listChecks
     * @param startKey Start key value for the pagination (optional)
     * @param reportId Report id checks to be returned (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listChecksCall(String startKey, String reportId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/checks";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (startKey != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("start_key", startKey));
        }

        if (reportId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("report_id", reportId));
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
    private okhttp3.Call listChecksValidateBeforeCall(String startKey, String reportId, final ApiCallback _callback) throws ApiException {
        return listChecksCall(startKey, reportId, _callback);

    }

    /**
     * List Checks
     * Lists the existing checks in the account or in a specified report.
     * @param startKey Start key value for the pagination (optional)
     * @param reportId Report id checks to be returned (optional)
     * @return ChecksOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ChecksOutput listChecks(String startKey, String reportId) throws ApiException {
        ApiResponse<ChecksOutput> localVarResp = listChecksWithHttpInfo(startKey, reportId);
        return localVarResp.getData();
    }

    /**
     * List Checks
     * Lists the existing checks in the account or in a specified report.
     * @param startKey Start key value for the pagination (optional)
     * @param reportId Report id checks to be returned (optional)
     * @return ApiResponse&lt;ChecksOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ChecksOutput> listChecksWithHttpInfo(String startKey, String reportId) throws ApiException {
        okhttp3.Call localVarCall = listChecksValidateBeforeCall(startKey, reportId, null);
        Type localVarReturnType = new TypeToken<ChecksOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List Checks (asynchronously)
     * Lists the existing checks in the account or in a specified report.
     * @param startKey Start key value for the pagination (optional)
     * @param reportId Report id checks to be returned (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listChecksAsync(String startKey, String reportId, final ApiCallback<ChecksOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = listChecksValidateBeforeCall(startKey, reportId, _callback);
        Type localVarReturnType = new TypeToken<ChecksOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
