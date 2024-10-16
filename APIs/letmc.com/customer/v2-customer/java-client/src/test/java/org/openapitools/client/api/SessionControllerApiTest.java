/*
 * agentOS Api V2, Customer Login Call Group
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-customer
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for SessionControllerApi
 */
@Disabled
public class SessionControllerApiTest {

    private final SessionControllerApi api = new SessionControllerApi();

    /**
     * Change the password of a customer given their existing and new password.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void sessionControllerChangePasswordTest() throws ApiException {
        String shortName = null;
        String token = null;
        String oldPassword = null;
        String newPassword = null;
        api.sessionControllerChangePassword(shortName, token, oldPassword, newPassword);
        // TODO: test validations
    }

    /**
     * Send a request to the in-tray to create a landlord login.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void sessionControllerCreateLandlordLoginTest() throws ApiException {
        String shortName = null;
        String email = null;
        String title = null;
        String forename = null;
        String surname = null;
        String propertyAddress = null;
        String contactDetails = null;
        String branchID = null;
        api.sessionControllerCreateLandlordLogin(shortName, email, title, forename, surname, propertyAddress, contactDetails, branchID);
        // TODO: test validations
    }

    /**
     * Gets information about the currently logged on customer.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void sessionControllerGetSessionInfoTest() throws ApiException {
        String shortName = null;
        String token = null;
        String response = api.sessionControllerGetSessionInfo(shortName, token);
        // TODO: test validations
    }

    /**
     * Login as a customer given their username and password.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void sessionControllerLoginTest() throws ApiException {
        String shortName = null;
        String username = null;
        String password = null;
        String response = api.sessionControllerLogin(shortName, username, password);
        // TODO: test validations
    }

    /**
     * Logout a customer previously logged in via the Login endpoint.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void sessionControllerLogoutTest() throws ApiException {
        String shortName = null;
        String token = null;
        api.sessionControllerLogout(shortName, token);
        // TODO: test validations
    }

    /**
     * Reset the customer&#39;s password. An email will be sent out to reset.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void sessionControllerResetPasswordTest() throws ApiException {
        String shortName = null;
        String email = null;
        api.sessionControllerResetPassword(shortName, email);
        // TODO: test validations
    }

}
