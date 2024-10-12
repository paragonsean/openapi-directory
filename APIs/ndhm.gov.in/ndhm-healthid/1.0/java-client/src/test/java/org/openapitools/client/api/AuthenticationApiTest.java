/*
 * Health ID Service
 * It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent.  In order to issue a Health ID to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily.
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.AuthAccountAadhaarBioRequest;
import org.openapitools.client.model.AuthAccountAadhaarOTPRequest;
import org.openapitools.client.model.AuthAccountMobileOTPRequest;
import org.openapitools.client.model.AuthAccountWithDemographicsRequest;
import org.openapitools.client.model.AuthInitRequest;
import org.openapitools.client.model.AuthMobileOTPRequest;
import org.openapitools.client.model.AuthWithMobileTxnAndUserData;
import org.openapitools.client.model.AuthWithPasswordRequest;
import org.openapitools.client.model.JwtRequest;
import org.openapitools.client.model.JwtResponse;
import org.openapitools.client.model.ResendOTPRequest;
import org.openapitools.client.model.TxnResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for AuthenticationApi
 */
@Disabled
public class AuthenticationApiTest {

    private final AuthenticationApi api = new AuthenticationApi();

    /**
     * Authentication with PASSWORD based auth transaction.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void authAccountPasswordRequestUsingPOSTTest() throws ApiException {
        AuthWithPasswordRequest authenticationRequest = null;
        String acceptLanguage = null;
        JwtResponse response = api.authAccountPasswordRequestUsingPOST(authenticationRequest, acceptLanguage);
        // TODO: test validations
    }

    /**
     * Authenticate using verified Mobile Number and user data
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void authWithMobileTokenUsingPOSTTest() throws ApiException {
        AuthWithMobileTxnAndUserData authRequest = null;
        String acceptLanguage = null;
        JwtResponse response = api.authWithMobileTokenUsingPOST(authRequest, acceptLanguage);
        // TODO: test validations
    }

    /**
     * Authenticate request to generate Mobile OTP using Health ID number / Health ID
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void authenticateUserUsingPOSTTest() throws ApiException {
        AuthMobileOTPRequest authRequest = null;
        String acceptLanguage = null;
        TxnResponse response = api.authenticateUserUsingPOST(authRequest, acceptLanguage);
        // TODO: test validations
    }

    /**
     * Authenticate using Health ID number / Health ID and password
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void authenticateWithPasswordUsingPOSTTest() throws ApiException {
        JwtRequest authenticationRequest = null;
        String acceptLanguage = null;
        JwtResponse response = api.authenticateWithPasswordUsingPOST(authenticationRequest, acceptLanguage);
        // TODO: test validations
    }

    /**
     * Auth token public key.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void certUsingGETTest() throws ApiException {
        String acceptLanguage = null;
        String response = api.certUsingGET(acceptLanguage);
        // TODO: test validations
    }

    /**
     * Authentication with Aadhaar Biometric based auth transaction.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void confirmWithAadhaarBioUsingPOSTTest() throws ApiException {
        AuthAccountAadhaarBioRequest authenticationRequest = null;
        String acceptLanguage = null;
        JwtResponse response = api.confirmWithAadhaarBioUsingPOST(authenticationRequest, acceptLanguage);
        // TODO: test validations
    }

    /**
     * Authentication with Aadhaar OTP based auth transaction.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void confirmWithAadhaarOtpUsingPOSTTest() throws ApiException {
        AuthAccountAadhaarOTPRequest authenticationRequest = null;
        String acceptLanguage = null;
        JwtResponse response = api.confirmWithAadhaarOtpUsingPOST(authenticationRequest, acceptLanguage);
        // TODO: test validations
    }

    /**
     * Authenticate using demographic data of user.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void confirmWithDemographicsUsingPOSTTest() throws ApiException {
        AuthAccountWithDemographicsRequest authenticationRequest = null;
        String acceptLanguage = null;
        String response = api.confirmWithDemographicsUsingPOST(authenticationRequest, acceptLanguage);
        // TODO: test validations
    }

    /**
     * Authentication with Mobile OTP based auth transaction.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void confirmWithMobileUsingPOSTTest() throws ApiException {
        AuthAccountMobileOTPRequest authenticationRequest = null;
        String acceptLanguage = null;
        JwtResponse response = api.confirmWithMobileUsingPOST(authenticationRequest, acceptLanguage);
        // TODO: test validations
    }

    /**
     * Initiate authentication process for given Health ID
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void initiateAuthUsingPOSTTest() throws ApiException {
        AuthInitRequest authRequest = null;
        String acceptLanguage = null;
        TxnResponse response = api.initiateAuthUsingPOST(authRequest, acceptLanguage);
        // TODO: test validations
    }

    /**
     * Resend Aadhaar/Mobile OTP for Authentication Transaction.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void resendAuthMobileOTPUsingPOSTTest() throws ApiException {
        ResendOTPRequest resendOtpRequest = null;
        String acceptLanguage = null;
        Boolean response = api.resendAuthMobileOTPUsingPOST(resendOtpRequest, acceptLanguage);
        // TODO: test validations
    }

}
