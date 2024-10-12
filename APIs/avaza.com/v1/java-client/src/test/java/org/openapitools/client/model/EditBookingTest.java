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
import java.util.Arrays;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for EditBooking
 */
public class EditBookingTest {
    private final EditBooking model = new EditBooking();

    /**
     * Model tests for EditBooking
     */
    @Test
    public void testEditBooking() {
        // TODO: test EditBooking
    }

    /**
     * Test the property 'categoryIDFK'
     */
    @Test
    public void categoryIDFKTest() {
        // TODO: test categoryIDFK
    }

    /**
     * Test the property 'durationType'
     */
    @Test
    public void durationTypeTest() {
        // TODO: test durationType
    }

    /**
     * Test the property 'endDate'
     */
    @Test
    public void endDateTest() {
        // TODO: test endDate
    }

    /**
     * Test the property 'hoursPerDay'
     */
    @Test
    public void hoursPerDayTest() {
        // TODO: test hoursPerDay
    }

    /**
     * Test the property 'notes'
     */
    @Test
    public void notesTest() {
        // TODO: test notes
    }

    /**
     * Test the property 'projectIDFK'
     */
    @Test
    public void projectIDFKTest() {
        // TODO: test projectIDFK
    }

    /**
     * Test the property 'scheduleOnDaysOff'
     */
    @Test
    public void scheduleOnDaysOffTest() {
        // TODO: test scheduleOnDaysOff
    }

    /**
     * Test the property 'scheduleSeriesID'
     */
    @Test
    public void scheduleSeriesIDTest() {
        // TODO: test scheduleSeriesID
    }

    /**
     * Test the property 'startDate'
     */
    @Test
    public void startDateTest() {
        // TODO: test startDate
    }

    /**
     * Test the property 'taskIDFK'
     */
    @Test
    public void taskIDFKTest() {
        // TODO: test taskIDFK
    }

    /**
     * Test the property 'totalDuration'
     */
    @Test
    public void totalDurationTest() {
        // TODO: test totalDuration
    }

    /**
     * Test the property 'userIDFK'
     */
    @Test
    public void userIDFKTest() {
        // TODO: test userIDFK
    }

}
