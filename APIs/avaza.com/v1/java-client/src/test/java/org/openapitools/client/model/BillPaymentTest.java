/*
 * Avaza API Documentation
 * Welcome to the autogenerated documentation & test tool for Avaza's API. <br/><br/><strong>API Security & Authentication</strong><br/>Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS <br/><br/>You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).<br/><br/> OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  <br/>OAuth2 Token endpoint: https://any.avaza.com/oauth2/token<br/>Base URL for subsequent API Requests: https://api.avaza.com/ <br/><br/>Blogpost about authenticating with Avaza's API:  https://www.avaza.com/avaza-api-oauth2-authentication/ <br/>Blogpost on using Avaza's webhooks: https://www.avaza.com/avaza-api-webhook-notifications/<br/>The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days<br/>The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. <br/><br><strong>Support</strong><br/>For API Support, and to request access please contact Avaza Support Team via our support chat. <br/><br/><strong>User Contributed Libraries:</strong><br/>Graciously contributed by 3rd party users like you. <br/>Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.<br/> <ul><li> - <a target='blank' href='https://packagist.org/packages/debiprasad/oauth2-avaza'>PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)</a></li></ul>
 *
 * The version of the OpenAPI document: v1
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
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.BillPaymentAllocation;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for BillPayment
 */
public class BillPaymentTest {
    private final BillPayment model = new BillPayment();

    /**
     * Model tests for BillPayment
     */
    @Test
    public void testBillPayment() {
        // TODO: test BillPayment
    }

    /**
     * Test the property 'accountIDFK'
     */
    @Test
    public void accountIDFKTest() {
        // TODO: test accountIDFK
    }

    /**
     * Test the property 'balance'
     */
    @Test
    public void balanceTest() {
        // TODO: test balance
    }

    /**
     * Test the property 'currencyCode'
     */
    @Test
    public void currencyCodeTest() {
        // TODO: test currencyCode
    }

    /**
     * Test the property 'dateCreated'
     */
    @Test
    public void dateCreatedTest() {
        // TODO: test dateCreated
    }

    /**
     * Test the property 'dateIssued'
     */
    @Test
    public void dateIssuedTest() {
        // TODO: test dateIssued
    }

    /**
     * Test the property 'dateUpdated'
     */
    @Test
    public void dateUpdatedTest() {
        // TODO: test dateUpdated
    }

    /**
     * Test the property 'exchangeRate'
     */
    @Test
    public void exchangeRateTest() {
        // TODO: test exchangeRate
    }

    /**
     * Test the property 'notes'
     */
    @Test
    public void notesTest() {
        // TODO: test notes
    }

    /**
     * Test the property 'paymentAllocations'
     */
    @Test
    public void paymentAllocationsTest() {
        // TODO: test paymentAllocations
    }

    /**
     * Test the property 'paymentNumber'
     */
    @Test
    public void paymentNumberTest() {
        // TODO: test paymentNumber
    }

    /**
     * Test the property 'paymentProviderCode'
     */
    @Test
    public void paymentProviderCodeTest() {
        // TODO: test paymentProviderCode
    }

    /**
     * Test the property 'supplierIDFK'
     */
    @Test
    public void supplierIDFKTest() {
        // TODO: test supplierIDFK
    }

    /**
     * Test the property 'totalAmount'
     */
    @Test
    public void totalAmountTest() {
        // TODO: test totalAmount
    }

    /**
     * Test the property 'transactionID'
     */
    @Test
    public void transactionIDTest() {
        // TODO: test transactionID
    }

    /**
     * Test the property 'transactionPrefix'
     */
    @Test
    public void transactionPrefixTest() {
        // TODO: test transactionPrefix
    }

    /**
     * Test the property 'transactionReference'
     */
    @Test
    public void transactionReferenceTest() {
        // TODO: test transactionReference
    }

    /**
     * Test the property 'transactionStatusCode'
     */
    @Test
    public void transactionStatusCodeTest() {
        // TODO: test transactionStatusCode
    }

}
