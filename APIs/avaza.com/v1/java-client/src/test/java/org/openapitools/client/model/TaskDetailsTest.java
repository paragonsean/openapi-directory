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
import org.openapitools.client.model.AssignedToUser;
import org.openapitools.client.model.TagItem;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for TaskDetails
 */
public class TaskDetailsTest {
    private final TaskDetails model = new TaskDetails();

    /**
     * Model tests for TaskDetails
     */
    @Test
    public void testTaskDetails() {
        // TODO: test TaskDetails
    }

    /**
     * Test the property 'accountTaskTypeIDFK'
     */
    @Test
    public void accountTaskTypeIDFKTest() {
        // TODO: test accountTaskTypeIDFK
    }

    /**
     * Test the property 'actualTime'
     */
    @Test
    public void actualTimeTest() {
        // TODO: test actualTime
    }

    /**
     * Test the property 'assignedToUsers'
     */
    @Test
    public void assignedToUsersTest() {
        // TODO: test assignedToUsers
    }

    /**
     * Test the property 'dateCompleted'
     */
    @Test
    public void dateCompletedTest() {
        // TODO: test dateCompleted
    }

    /**
     * Test the property 'dateCreated'
     */
    @Test
    public void dateCreatedTest() {
        // TODO: test dateCreated
    }

    /**
     * Test the property 'dateDue'
     */
    @Test
    public void dateDueTest() {
        // TODO: test dateDue
    }

    /**
     * Test the property 'dateStart'
     */
    @Test
    public void dateStartTest() {
        // TODO: test dateStart
    }

    /**
     * Test the property 'dateUpdated'
     */
    @Test
    public void dateUpdatedTest() {
        // TODO: test dateUpdated
    }

    /**
     * Test the property 'description'
     */
    @Test
    public void descriptionTest() {
        // TODO: test description
    }

    /**
     * Test the property 'descriptionNoHTML'
     */
    @Test
    public void descriptionNoHTMLTest() {
        // TODO: test descriptionNoHTML
    }

    /**
     * Test the property 'estimatedEffort'
     */
    @Test
    public void estimatedEffortTest() {
        // TODO: test estimatedEffort
    }

    /**
     * Test the property 'percentComplete'
     */
    @Test
    public void percentCompleteTest() {
        // TODO: test percentComplete
    }

    /**
     * Test the property 'projectCode'
     */
    @Test
    public void projectCodeTest() {
        // TODO: test projectCode
    }

    /**
     * Test the property 'projectIDFK'
     */
    @Test
    public void projectIDFKTest() {
        // TODO: test projectIDFK
    }

    /**
     * Test the property 'projectTitle'
     */
    @Test
    public void projectTitleTest() {
        // TODO: test projectTitle
    }

    /**
     * Test the property 'sectionIDFK'
     */
    @Test
    public void sectionIDFKTest() {
        // TODO: test sectionIDFK
    }

    /**
     * Test the property 'sectionTitle'
     */
    @Test
    public void sectionTitleTest() {
        // TODO: test sectionTitle
    }

    /**
     * Test the property 'tags'
     */
    @Test
    public void tagsTest() {
        // TODO: test tags
    }

    /**
     * Test the property 'taskID'
     */
    @Test
    public void taskIDTest() {
        // TODO: test taskID
    }

    /**
     * Test the property 'taskPriorityCode'
     */
    @Test
    public void taskPriorityCodeTest() {
        // TODO: test taskPriorityCode
    }

    /**
     * Test the property 'taskPriorityName'
     */
    @Test
    public void taskPriorityNameTest() {
        // TODO: test taskPriorityName
    }

    /**
     * Test the property 'taskStatusCode'
     */
    @Test
    public void taskStatusCodeTest() {
        // TODO: test taskStatusCode
    }

    /**
     * Test the property 'taskStatusName'
     */
    @Test
    public void taskStatusNameTest() {
        // TODO: test taskStatusName
    }

    /**
     * Test the property 'title'
     */
    @Test
    public void titleTest() {
        // TODO: test title
    }

    /**
     * Test the property 'isCompleteStatus'
     */
    @Test
    public void isCompleteStatusTest() {
        // TODO: test isCompleteStatus
    }

}
