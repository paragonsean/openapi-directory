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
import org.openapitools.client.model.ProjectMemberDetails;
import org.openapitools.client.model.ProjectSectionDetails;
import org.openapitools.client.model.ProjectTagItem;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for ProjectDetails
 */
public class ProjectDetailsTest {
    private final ProjectDetails model = new ProjectDetails();

    /**
     * Model tests for ProjectDetails
     */
    @Test
    public void testProjectDetails() {
        // TODO: test ProjectDetails
    }

    /**
     * Test the property 'budgetAmount'
     */
    @Test
    public void budgetAmountTest() {
        // TODO: test budgetAmount
    }

    /**
     * Test the property 'budgetHours'
     */
    @Test
    public void budgetHoursTest() {
        // TODO: test budgetHours
    }

    /**
     * Test the property 'companyIDFK'
     */
    @Test
    public void companyIDFKTest() {
        // TODO: test companyIDFK
    }

    /**
     * Test the property 'companyName'
     */
    @Test
    public void companyNameTest() {
        // TODO: test companyName
    }

    /**
     * Test the property 'dateCreated'
     */
    @Test
    public void dateCreatedTest() {
        // TODO: test dateCreated
    }

    /**
     * Test the property 'dateUpdated'
     */
    @Test
    public void dateUpdatedTest() {
        // TODO: test dateUpdated
    }

    /**
     * Test the property 'defaultAccountTaskTypeIDFK'
     */
    @Test
    public void defaultAccountTaskTypeIDFKTest() {
        // TODO: test defaultAccountTaskTypeIDFK
    }

    /**
     * Test the property 'defaultAccountTaskTypeName'
     */
    @Test
    public void defaultAccountTaskTypeNameTest() {
        // TODO: test defaultAccountTaskTypeName
    }

    /**
     * Test the property 'endDate'
     */
    @Test
    public void endDateTest() {
        // TODO: test endDate
    }

    /**
     * Test the property 'members'
     */
    @Test
    public void membersTest() {
        // TODO: test members
    }

    /**
     * Test the property 'notes'
     */
    @Test
    public void notesTest() {
        // TODO: test notes
    }

    /**
     * Test the property 'projectBillableTypeCode'
     */
    @Test
    public void projectBillableTypeCodeTest() {
        // TODO: test projectBillableTypeCode
    }

    /**
     * Test the property 'projectBudgetTypeCode'
     */
    @Test
    public void projectBudgetTypeCodeTest() {
        // TODO: test projectBudgetTypeCode
    }

    /**
     * Test the property 'projectCategoryColor'
     */
    @Test
    public void projectCategoryColorTest() {
        // TODO: test projectCategoryColor
    }

    /**
     * Test the property 'projectCategoryIDFK'
     */
    @Test
    public void projectCategoryIDFKTest() {
        // TODO: test projectCategoryIDFK
    }

    /**
     * Test the property 'projectCategoryName'
     */
    @Test
    public void projectCategoryNameTest() {
        // TODO: test projectCategoryName
    }

    /**
     * Test the property 'projectCode'
     */
    @Test
    public void projectCodeTest() {
        // TODO: test projectCode
    }

    /**
     * Test the property 'projectHourlyRate'
     */
    @Test
    public void projectHourlyRateTest() {
        // TODO: test projectHourlyRate
    }

    /**
     * Test the property 'projectID'
     */
    @Test
    public void projectIDTest() {
        // TODO: test projectID
    }

    /**
     * Test the property 'projectOwnerUserIDFK'
     */
    @Test
    public void projectOwnerUserIDFKTest() {
        // TODO: test projectOwnerUserIDFK
    }

    /**
     * Test the property 'projectStatusCode'
     */
    @Test
    public void projectStatusCodeTest() {
        // TODO: test projectStatusCode
    }

    /**
     * Test the property 'projectTags'
     */
    @Test
    public void projectTagsTest() {
        // TODO: test projectTags
    }

    /**
     * Test the property 'sections'
     */
    @Test
    public void sectionsTest() {
        // TODO: test sections
    }

    /**
     * Test the property 'startDate'
     */
    @Test
    public void startDateTest() {
        // TODO: test startDate
    }

    /**
     * Test the property 'title'
     */
    @Test
    public void titleTest() {
        // TODO: test title
    }

    /**
     * Test the property 'isArchived'
     */
    @Test
    public void isArchivedTest() {
        // TODO: test isArchived
    }

    /**
     * Test the property 'isTaskRequiredOnTimesheet'
     */
    @Test
    public void isTaskRequiredOnTimesheetTest() {
        // TODO: test isTaskRequiredOnTimesheet
    }

}
