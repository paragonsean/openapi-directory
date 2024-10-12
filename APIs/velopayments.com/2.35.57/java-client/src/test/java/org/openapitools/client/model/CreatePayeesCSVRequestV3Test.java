/*
 * Velo Payments APIs
 * ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response. 
 *
 * The version of the OpenAPI document: 2.35.57
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.time.LocalDate;
import java.util.Arrays;
import org.openapitools.client.model.PayeeTypeEnum;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for CreatePayeesCSVRequestV3
 */
public class CreatePayeesCSVRequestV3Test {
    private final CreatePayeesCSVRequestV3 model = new CreatePayeesCSVRequestV3();

    /**
     * Model tests for CreatePayeesCSVRequestV3
     */
    @Test
    public void testCreatePayeesCSVRequestV3() {
        // TODO: test CreatePayeesCSVRequestV3
    }

    /**
     * Test the property 'addressCity'
     */
    @Test
    public void addressCityTest() {
        // TODO: test addressCity
    }

    /**
     * Test the property 'addressCountry'
     */
    @Test
    public void addressCountryTest() {
        // TODO: test addressCountry
    }

    /**
     * Test the property 'addressCountyOrProvince'
     */
    @Test
    public void addressCountyOrProvinceTest() {
        // TODO: test addressCountyOrProvince
    }

    /**
     * Test the property 'addressLine1'
     */
    @Test
    public void addressLine1Test() {
        // TODO: test addressLine1
    }

    /**
     * Test the property 'addressLine2'
     */
    @Test
    public void addressLine2Test() {
        // TODO: test addressLine2
    }

    /**
     * Test the property 'addressLine3'
     */
    @Test
    public void addressLine3Test() {
        // TODO: test addressLine3
    }

    /**
     * Test the property 'addressLine4'
     */
    @Test
    public void addressLine4Test() {
        // TODO: test addressLine4
    }

    /**
     * Test the property 'addressZipOrPostcode'
     */
    @Test
    public void addressZipOrPostcodeTest() {
        // TODO: test addressZipOrPostcode
    }

    /**
     * Test the property 'challengeDescription'
     */
    @Test
    public void challengeDescriptionTest() {
        // TODO: test challengeDescription
    }

    /**
     * Test the property 'challengeValue'
     */
    @Test
    public void challengeValueTest() {
        // TODO: test challengeValue
    }

    /**
     * Test the property 'companyEIN'
     */
    @Test
    public void companyEINTest() {
        // TODO: test companyEIN
    }

    /**
     * Test the property 'companyName'
     */
    @Test
    public void companyNameTest() {
        // TODO: test companyName
    }

    /**
     * Test the property 'companyOperatingName'
     */
    @Test
    public void companyOperatingNameTest() {
        // TODO: test companyOperatingName
    }

    /**
     * Test the property 'email'
     */
    @Test
    public void emailTest() {
        // TODO: test email
    }

    /**
     * Test the property 'individualDateOfBirth'
     */
    @Test
    public void individualDateOfBirthTest() {
        // TODO: test individualDateOfBirth
    }

    /**
     * Test the property 'individualFirstName'
     */
    @Test
    public void individualFirstNameTest() {
        // TODO: test individualFirstName
    }

    /**
     * Test the property 'individualLastName'
     */
    @Test
    public void individualLastNameTest() {
        // TODO: test individualLastName
    }

    /**
     * Test the property 'individualNationalIdentification'
     */
    @Test
    public void individualNationalIdentificationTest() {
        // TODO: test individualNationalIdentification
    }

    /**
     * Test the property 'individualOtherNames'
     */
    @Test
    public void individualOtherNamesTest() {
        // TODO: test individualOtherNames
    }

    /**
     * Test the property 'individualTitle'
     */
    @Test
    public void individualTitleTest() {
        // TODO: test individualTitle
    }

    /**
     * Test the property 'payeeLanguage'
     */
    @Test
    public void payeeLanguageTest() {
        // TODO: test payeeLanguage
    }

    /**
     * Test the property 'paymentChannelAccountName'
     */
    @Test
    public void paymentChannelAccountNameTest() {
        // TODO: test paymentChannelAccountName
    }

    /**
     * Test the property 'paymentChannelAccountNumber'
     */
    @Test
    public void paymentChannelAccountNumberTest() {
        // TODO: test paymentChannelAccountNumber
    }

    /**
     * Test the property 'paymentChannelCountryCode'
     */
    @Test
    public void paymentChannelCountryCodeTest() {
        // TODO: test paymentChannelCountryCode
    }

    /**
     * Test the property 'paymentChannelCurrency'
     */
    @Test
    public void paymentChannelCurrencyTest() {
        // TODO: test paymentChannelCurrency
    }

    /**
     * Test the property 'paymentChannelIban'
     */
    @Test
    public void paymentChannelIbanTest() {
        // TODO: test paymentChannelIban
    }

    /**
     * Test the property 'paymentChannelRoutingNumber'
     */
    @Test
    public void paymentChannelRoutingNumberTest() {
        // TODO: test paymentChannelRoutingNumber
    }

    /**
     * Test the property 'remoteId'
     */
    @Test
    public void remoteIdTest() {
        // TODO: test remoteId
    }

    /**
     * Test the property 'type'
     */
    @Test
    public void typeTest() {
        // TODO: test type
    }

}
