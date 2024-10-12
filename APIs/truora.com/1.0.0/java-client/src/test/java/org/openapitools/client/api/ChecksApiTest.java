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

import org.openapitools.client.ApiException;
import org.openapitools.client.model.CheckDetailsOutput;
import org.openapitools.client.model.CheckOutput;
import org.openapitools.client.model.ChecksOutput;
import org.openapitools.client.model.Database;
import org.openapitools.client.model.Error;
import java.time.LocalDate;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ChecksApi
 */
@Disabled
public class ChecksApiTest {

    private final ChecksApi api = new ChecksApi();

    /**
     * Create a background check
     *
     * Creates a background check and queues it to start collecting information. The full details of background checks can be retrieved with their respective Check IDs using getCheck endpoint. Keep in mind that, depending on the check type, input document, and country of a search, certain inputs are required. You should always provide as many inputs as possible in order to get the highest accuracy.  If your check type is not referenced in the following table, please reach out to find out the fields that apply for you.  | Country | Person-National | PersonForeigner | Company | Vehicle-National | Vehicle-Foreigner | |:-------:|:---------------:|:---------------:|:-------:|:----------------:|:-----------------:| | Chile&lt;br&gt;CL | national_id*&lt;br&gt;date_of_birth&lt;br&gt;phone_number | foreign_id*&lt;br&gt;date_of_birth*&lt;br&gt;phone_number&lt;br&gt;first_name*&lt;br&gt;last_name*&lt;br&gt;native_country* | N/A | national_id*&lt;br&gt;license_plate*&lt;br&gt;payment_date (Santiago only)&lt;br&gt;driver_license (Santiago only) | foreign_id*&lt;br&gt;first_name*&lt;br&gt;last_name*&lt;br&gt;date_of_birth*&lt;br&gt;native_country*&lt;br&gt;license_plate*&lt;br&gt;payment_date (Santiago only)&lt;br&gt;driver_license (Santiago only) | | Colombia&lt;br&gt;CO | national_id*&lt;br&gt;date_of_birth&lt;br&gt;issue_date&lt;br&gt;phone_number | foreign_id* or PEP*&lt;br&gt;date_of_birth&lt;br&gt;phone_number&lt;br&gt;issue_date* | tax_id*&lt;br&gt;national_id | national_id*&lt;br&gt;date_of_birth&lt;br&gt;phone_number&lt;br&gt;license_plate*&lt;br&gt;owner_document_type&lt;br&gt;owner_document_id | foreign_id*&lt;br&gt;date_of_birth&lt;br&gt;phone_number&lt;br&gt;license_plate*&lt;br&gt;issue_date* | | Mexico&lt;br&gt;MX | national_id*&lt;br&gt;phone_number | foreign_id* | tax_id* | license_plate*&lt;br&gt;national_id&lt;br&gt;vehicle_id&lt;br&gt;driver_license(Estado de Mexico only) | N/A | | Brazil&lt;br&gt;BR | national_id*&lt;br&gt;date_of_birth*&lt;br&gt;region*&lt;br&gt;phone_number | N/A | tax_id* | license_plate* | N/A | | Costa Rica&lt;br&gt;CR | national_id*&lt;br&gt;phone_number | foreign_id* | N/A | license_plate* | N/A | | Ecuador&lt;br&gt;EC | national_id*&lt;br&gt;phone_number | foreign_id* | tax_id* | license_plate* | N/A | | Peru&lt;br&gt;PE | national_id*&lt;br&gt;date_of_birth&lt;br&gt;phone_number | foreign_id*&lt;br&gt;ptp&lt;br&gt;date_of_birth*&lt;br&gt;phone_number | N/A | national_id*&lt;br&gt;date_of_birth&lt;br&gt;license_plate* | foreign_id*&lt;br&gt;ptp&lt;br&gt;date_of_birth*&lt;br&gt;license_plate* | | Argentina&lt;br&gt;AR | national_id* | N/A | N/A | national_id* | N/A | | International&lt;br&gt;ALL | name* | name* | company_name* | N/A | N/A |  (*) Required field
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createCheckTest() throws ApiException {
        String country = null;
        String type = null;
        String truoraPriority = null;
        String birthCertificate = null;
        String companyName = null;
        LocalDate dateOfBirth = null;
        String diplomaticId = null;
        String driverLicense = null;
        String escrow = null;
        String firstName = null;
        Boolean forceCreation = null;
        String foreignId = null;
        LocalDate issueDate = null;
        String lastName = null;
        String licensePlate = null;
        String nationalId = null;
        String nativeCountry = null;
        String ownerDocumentId = null;
        String ownerDocumentType = null;
        String passport = null;
        LocalDate paymentDate = null;
        String pep = null;
        String phoneNumber = null;
        String professionalCard = null;
        String ptp = null;
        String region = null;
        String reportId = null;
        String stateId = null;
        String taxId = null;
        Boolean userAuthorized = null;
        String vehicleId = null;
        String verificationCode = null;
        String watch = null;
        CheckOutput response = api.createCheck(country, type, truoraPriority, birthCertificate, companyName, dateOfBirth, diplomaticId, driverLicense, escrow, firstName, forceCreation, foreignId, issueDate, lastName, licensePlate, nationalId, nativeCountry, ownerDocumentId, ownerDocumentType, passport, paymentDate, pep, phoneNumber, professionalCard, ptp, region, reportId, stateId, taxId, userAuthorized, vehicleId, verificationCode, watch);
        // TODO: test validations
    }

    /**
     * Get Background Check
     *
     * Returns the results of the check that matches the ID provided, complete with a set of scores explained below.  ### Scores:   - **Global Score**: Average risk associated with a person, company or vehicle, according to  the background check results. The global score considers results that are validated with the  ID number provided. The score ranges from 0 to 1, where 0 represents high risk and 1 low risk.   - **ID Score**: Average risk associated with a person according to the background check  results. The ID score considers the results that are validated with a person identity  document. The score ranges from 0 to 1, where 0 represents high risk and 1 low risk.    - **Homonym Score**: Average risk associated with a person according to the background check  results. The homonym score considers results that are validated against the name of a person and could not be validated with their ID number. These results might have homonyms associated with them. The score ranges from 0 to 1, where 0 represents high risk and 1 low risk.   In order to calculate these scores, a weighted average is considered with different weights allocated to each dataset. Scores can be customized using the config endpoints by assigning a weight to each dataset according to its relevance.  Keep in mind that results from the API vary depending on the country, check type and the inputs entered on check creation.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getCheckTest() throws ApiException {
        String checkId = null;
        CheckOutput response = api.getCheck(checkId);
        // TODO: test validations
    }

    /**
     * Get Health Dashboard
     *
     * Get the status of a database
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getHealthDashboardTest() throws ApiException {
        String country = null;
        String unixTimestampSeconds = null;
        String unixtimezoneOffsetSeconds = null;
        List<Database> response = api.getHealthDashboard(country, unixTimestampSeconds, unixtimezoneOffsetSeconds);
        // TODO: test validations
    }

    /**
     * List Check Details
     *
     * Lists all details associated with a Check. It can be paginated.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listCheckDetailsTest() throws ApiException {
        String checkId = null;
        String startKey = null;
        String lang = null;
        CheckDetailsOutput response = api.listCheckDetails(checkId, startKey, lang);
        // TODO: test validations
    }

    /**
     * List Checks
     *
     * Lists the existing checks in the account or in a specified report.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listChecksTest() throws ApiException {
        String startKey = null;
        String reportId = null;
        ChecksOutput response = api.listChecks(startKey, reportId);
        // TODO: test validations
    }

}
