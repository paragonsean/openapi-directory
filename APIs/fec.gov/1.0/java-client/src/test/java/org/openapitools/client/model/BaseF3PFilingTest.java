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
import org.openapitools.jackson.nullable.JsonNullable;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for BaseF3PFiling
 */
public class BaseF3PFilingTest {
    private final BaseF3PFiling model = new BaseF3PFiling();

    /**
     * Model tests for BaseF3PFiling
     */
    @Test
    public void testBaseF3PFiling() {
        // TODO: test BaseF3PFiling
    }

    /**
     * Test the property 'amendedBy'
     */
    @Test
    public void amendedByTest() {
        // TODO: test amendedBy
    }

    /**
     * Test the property 'amendment'
     */
    @Test
    public void amendmentTest() {
        // TODO: test amendment
    }

    /**
     * Test the property 'amendmentChain'
     */
    @Test
    public void amendmentChainTest() {
        // TODO: test amendmentChain
    }

    /**
     * Test the property 'beginningImageNumber'
     */
    @Test
    public void beginningImageNumberTest() {
        // TODO: test beginningImageNumber
    }

    /**
     * Test the property 'cashOnHandBeginningPeriod'
     */
    @Test
    public void cashOnHandBeginningPeriodTest() {
        // TODO: test cashOnHandBeginningPeriod
    }

    /**
     * Test the property 'cashOnHandEndPeriod'
     */
    @Test
    public void cashOnHandEndPeriodTest() {
        // TODO: test cashOnHandEndPeriod
    }

    /**
     * Test the property 'city'
     */
    @Test
    public void cityTest() {
        // TODO: test city
    }

    /**
     * Test the property 'committeeId'
     */
    @Test
    public void committeeIdTest() {
        // TODO: test committeeId
    }

    /**
     * Test the property 'committeeName'
     */
    @Test
    public void committeeNameTest() {
        // TODO: test committeeName
    }

    /**
     * Test the property 'coverageEndDate'
     */
    @Test
    public void coverageEndDateTest() {
        // TODO: test coverageEndDate
    }

    /**
     * Test the property 'coverageStartDate'
     */
    @Test
    public void coverageStartDateTest() {
        // TODO: test coverageStartDate
    }

    /**
     * Test the property 'csvUrl'
     */
    @Test
    public void csvUrlTest() {
        // TODO: test csvUrl
    }

    /**
     * Test the property 'debtsOwedByCommittee'
     */
    @Test
    public void debtsOwedByCommitteeTest() {
        // TODO: test debtsOwedByCommittee
    }

    /**
     * Test the property 'debtsOwedToCommittee'
     */
    @Test
    public void debtsOwedToCommitteeTest() {
        // TODO: test debtsOwedToCommittee
    }

    /**
     * Test the property 'documentDescription'
     */
    @Test
    public void documentDescriptionTest() {
        // TODO: test documentDescription
    }

    /**
     * Test the property 'electionDate'
     */
    @Test
    public void electionDateTest() {
        // TODO: test electionDate
    }

    /**
     * Test the property 'electionState'
     */
    @Test
    public void electionStateTest() {
        // TODO: test electionState
    }

    /**
     * Test the property 'expenditureSubjectToLimits'
     */
    @Test
    public void expenditureSubjectToLimitsTest() {
        // TODO: test expenditureSubjectToLimits
    }

    /**
     * Test the property 'fecFileId'
     */
    @Test
    public void fecFileIdTest() {
        // TODO: test fecFileId
    }

    /**
     * Test the property 'fecUrl'
     */
    @Test
    public void fecUrlTest() {
        // TODO: test fecUrl
    }

    /**
     * Test the property 'fileNumber'
     */
    @Test
    public void fileNumberTest() {
        // TODO: test fileNumber
    }

    /**
     * Test the property 'generalElection'
     */
    @Test
    public void generalElectionTest() {
        // TODO: test generalElection
    }

    /**
     * Test the property 'isAmended'
     */
    @Test
    public void isAmendedTest() {
        // TODO: test isAmended
    }

    /**
     * Test the property 'mostRecent'
     */
    @Test
    public void mostRecentTest() {
        // TODO: test mostRecent
    }

    /**
     * Test the property 'mostRecentFiling'
     */
    @Test
    public void mostRecentFilingTest() {
        // TODO: test mostRecentFiling
    }

    /**
     * Test the property 'netContributionsCycleToDate'
     */
    @Test
    public void netContributionsCycleToDateTest() {
        // TODO: test netContributionsCycleToDate
    }

    /**
     * Test the property 'netOperatingExpendituresCycleToDate'
     */
    @Test
    public void netOperatingExpendituresCycleToDateTest() {
        // TODO: test netOperatingExpendituresCycleToDate
    }

    /**
     * Test the property 'pdfUrl'
     */
    @Test
    public void pdfUrlTest() {
        // TODO: test pdfUrl
    }

    /**
     * Test the property 'prefix'
     */
    @Test
    public void prefixTest() {
        // TODO: test prefix
    }

    /**
     * Test the property 'primaryElection'
     */
    @Test
    public void primaryElectionTest() {
        // TODO: test primaryElection
    }

    /**
     * Test the property 'receiptDate'
     */
    @Test
    public void receiptDateTest() {
        // TODO: test receiptDate
    }

    /**
     * Test the property 'report'
     */
    @Test
    public void reportTest() {
        // TODO: test report
    }

    /**
     * Test the property 'reportType'
     */
    @Test
    public void reportTypeTest() {
        // TODO: test reportType
    }

    /**
     * Test the property 'reportYear'
     */
    @Test
    public void reportYearTest() {
        // TODO: test reportYear
    }

    /**
     * Test the property 'rptPgi'
     */
    @Test
    public void rptPgiTest() {
        // TODO: test rptPgi
    }

    /**
     * Test the property 'signDate'
     */
    @Test
    public void signDateTest() {
        // TODO: test signDate
    }

    /**
     * Test the property 'state'
     */
    @Test
    public void stateTest() {
        // TODO: test state
    }

    /**
     * Test the property 'street1'
     */
    @Test
    public void street1Test() {
        // TODO: test street1
    }

    /**
     * Test the property 'street2'
     */
    @Test
    public void street2Test() {
        // TODO: test street2
    }

    /**
     * Test the property 'subtotalSummaryPeriod'
     */
    @Test
    public void subtotalSummaryPeriodTest() {
        // TODO: test subtotalSummaryPeriod
    }

    /**
     * Test the property 'suffix'
     */
    @Test
    public void suffixTest() {
        // TODO: test suffix
    }

    /**
     * Test the property 'summaryLines'
     */
    @Test
    public void summaryLinesTest() {
        // TODO: test summaryLines
    }

    /**
     * Test the property 'treasurerFirstName'
     */
    @Test
    public void treasurerFirstNameTest() {
        // TODO: test treasurerFirstName
    }

    /**
     * Test the property 'treasurerLastName'
     */
    @Test
    public void treasurerLastNameTest() {
        // TODO: test treasurerLastName
    }

    /**
     * Test the property 'treasurerMiddleName'
     */
    @Test
    public void treasurerMiddleNameTest() {
        // TODO: test treasurerMiddleName
    }

    /**
     * Test the property 'treasurerName'
     */
    @Test
    public void treasurerNameTest() {
        // TODO: test treasurerName
    }

    /**
     * Test the property 'zip'
     */
    @Test
    public void zipTest() {
        // TODO: test zip
    }

}
