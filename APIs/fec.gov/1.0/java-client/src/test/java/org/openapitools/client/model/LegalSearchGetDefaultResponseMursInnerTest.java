/*
 * OpenFEC
 * This application programming interface (API) allows you to explore the way candidates and committees fund their campaigns.    The Federal Election Commission (FEC) API is a RESTful web service supporting full-text and field-specific searches on FEC data. [Bulk downloads](https://www.fec.gov/data/advanced/?tab=bulk-data) are available on the current site. Information is tied to the underlying forms by file ID and image ID. Data is updated nightly.    There are a lot of data, and a good place to start is to use search to find interesting candidates and committees. Then, you can use their IDs to find report or line item details with the other endpoints. If you are interested in individual donors, check out contributor information in the `/schedule_a/` endpoints.    <b class=\"body\" id=\"getting_started_head\">Getting started with the openFEC API</b><br>    If you would like to use the FEC's API programmatically, you can sign up for your own API key using our form. Alternatively, you can still try out our API without an API key by using the web interface and using DEMO_KEY. Note that when you use the openFEC API you are subject to the [Terms of Service](https://github.com/fecgov/FEC/blob/master/TERMS-OF-SERVICE.md) and [Acceptable Use policy](https://github.com/fecgov/FEC/blob/master/ACCEPTABLE-USE-POLICY.md).    Signing up for an API key will enable you to place up to 1,000 calls an hour. Each call is limited to 100 results per page. You can email questions, comments or a request to get a key for 7,200 calls an hour (120 calls per minute) to <a href=\"mailto:APIinfo@fec.gov\">APIinfo@fec.gov</a>. You can also ask questions and discuss the data in a community led [group](https://groups.google.com/forum/#!forum/fec-data).    The model definitions and schema are available at [/swagger](/swagger/). This is useful for making wrappers and exploring the data.    A few restrictions limit the way you can use FEC data. For example, you can’t use contributor lists for commercial purposes or to solicit donations. [Learn more here](https://www.fec.gov/updates/sale-or-use-contributor-information/).    [Inspect our source code](https://github.com/fecgov/openFEC). We welcome issues and pull requests!    <p><br></p> <h2 class=\"title\" id=\"signup_head\">Sign up for an API key</h2> <div id=\"apidatagov_signup\">Loading signup form...</div>
 *
 * The version of the OpenAPI document: 1.0
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.LegalSearchGetDefaultResponseAdminFinesInnerCommissionVotesInner;
import org.openapitools.client.model.LegalSearchGetDefaultResponseAdminFinesInnerDocumentsInner;
import org.openapitools.client.model.LegalSearchGetDefaultResponseAdrsInnerDispositionsInner;
import org.openapitools.client.model.LegalSearchGetDefaultResponseAdrsInnerParticipantsInner;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for LegalSearchGetDefaultResponseMursInner
 */
public class LegalSearchGetDefaultResponseMursInnerTest {
    private final LegalSearchGetDefaultResponseMursInner model = new LegalSearchGetDefaultResponseMursInner();

    /**
     * Model tests for LegalSearchGetDefaultResponseMursInner
     */
    @Test
    public void testLegalSearchGetDefaultResponseMursInner() {
        // TODO: test LegalSearchGetDefaultResponseMursInner
    }

    /**
     * Test the property 'closeDate'
     */
    @Test
    public void closeDateTest() {
        // TODO: test closeDate
    }

    /**
     * Test the property 'commissionVotes'
     */
    @Test
    public void commissionVotesTest() {
        // TODO: test commissionVotes
    }

    /**
     * Test the property 'dispositions'
     */
    @Test
    public void dispositionsTest() {
        // TODO: test dispositions
    }

    /**
     * Test the property 'docId'
     */
    @Test
    public void docIdTest() {
        // TODO: test docId
    }

    /**
     * Test the property 'documentHighlights'
     */
    @Test
    public void documentHighlightsTest() {
        // TODO: test documentHighlights
    }

    /**
     * Test the property 'documents'
     */
    @Test
    public void documentsTest() {
        // TODO: test documents
    }

    /**
     * Test the property 'electionCycles'
     */
    @Test
    public void electionCyclesTest() {
        // TODO: test electionCycles
    }

    /**
     * Test the property 'highlights'
     */
    @Test
    public void highlightsTest() {
        // TODO: test highlights
    }

    /**
     * Test the property 'murType'
     */
    @Test
    public void murTypeTest() {
        // TODO: test murType
    }

    /**
     * Test the property 'name'
     */
    @Test
    public void nameTest() {
        // TODO: test name
    }

    /**
     * Test the property 'false'
     */
    @Test
    public void falseTest() {
        // TODO: test false
    }

    /**
     * Test the property 'openDate'
     */
    @Test
    public void openDateTest() {
        // TODO: test openDate
    }

    /**
     * Test the property 'participants'
     */
    @Test
    public void participantsTest() {
        // TODO: test participants
    }

    /**
     * Test the property 'respondents'
     */
    @Test
    public void respondentsTest() {
        // TODO: test respondents
    }

    /**
     * Test the property 'subjects'
     */
    @Test
    public void subjectsTest() {
        // TODO: test subjects
    }

    /**
     * Test the property 'url'
     */
    @Test
    public void urlTest() {
        // TODO: test url
    }

}
