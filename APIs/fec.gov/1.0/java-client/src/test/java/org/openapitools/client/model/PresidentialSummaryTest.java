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
import java.math.BigDecimal;
import java.util.Arrays;
import org.openapitools.jackson.nullable.JsonNullable;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for PresidentialSummary
 */
public class PresidentialSummaryTest {
    private final PresidentialSummary model = new PresidentialSummary();

    /**
     * Model tests for PresidentialSummary
     */
    @Test
    public void testPresidentialSummary() {
        // TODO: test PresidentialSummary
    }

    /**
     * Test the property 'candidateContributionsLessRepayments'
     */
    @Test
    public void candidateContributionsLessRepaymentsTest() {
        // TODO: test candidateContributionsLessRepayments
    }

    /**
     * Test the property 'candidateId'
     */
    @Test
    public void candidateIdTest() {
        // TODO: test candidateId
    }

    /**
     * Test the property 'candidateLastName'
     */
    @Test
    public void candidateLastNameTest() {
        // TODO: test candidateLastName
    }

    /**
     * Test the property 'candidateName'
     */
    @Test
    public void candidateNameTest() {
        // TODO: test candidateName
    }

    /**
     * Test the property 'candidatePartyAffiliation'
     */
    @Test
    public void candidatePartyAffiliationTest() {
        // TODO: test candidatePartyAffiliation
    }

    /**
     * Test the property 'cashOnHandEnd'
     */
    @Test
    public void cashOnHandEndTest() {
        // TODO: test cashOnHandEnd
    }

    /**
     * Test the property 'committeeDesignation'
     */
    @Test
    public void committeeDesignationTest() {
        // TODO: test committeeDesignation
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
     * Test the property 'committeeType'
     */
    @Test
    public void committeeTypeTest() {
        // TODO: test committeeType
    }

    /**
     * Test the property 'debtsOwedByCommittee'
     */
    @Test
    public void debtsOwedByCommitteeTest() {
        // TODO: test debtsOwedByCommittee
    }

    /**
     * Test the property 'disbursementsLessOffsets'
     */
    @Test
    public void disbursementsLessOffsetsTest() {
        // TODO: test disbursementsLessOffsets
    }

    /**
     * Test the property 'electionYear'
     */
    @Test
    public void electionYearTest() {
        // TODO: test electionYear
    }

    /**
     * Test the property 'exemptLegalAccountingDisbursement'
     */
    @Test
    public void exemptLegalAccountingDisbursementTest() {
        // TODO: test exemptLegalAccountingDisbursement
    }

    /**
     * Test the property 'federalFunds'
     */
    @Test
    public void federalFundsTest() {
        // TODO: test federalFunds
    }

    /**
     * Test the property 'fundraisingDisbursements'
     */
    @Test
    public void fundraisingDisbursementsTest() {
        // TODO: test fundraisingDisbursements
    }

    /**
     * Test the property 'individualContributionsLessRefunds'
     */
    @Test
    public void individualContributionsLessRefundsTest() {
        // TODO: test individualContributionsLessRefunds
    }

    /**
     * Test the property 'netReceipts'
     */
    @Test
    public void netReceiptsTest() {
        // TODO: test netReceipts
    }

    /**
     * Test the property 'offsetsToOperatingExpenditures'
     */
    @Test
    public void offsetsToOperatingExpendituresTest() {
        // TODO: test offsetsToOperatingExpenditures
    }

    /**
     * Test the property 'operatingExpenditures'
     */
    @Test
    public void operatingExpendituresTest() {
        // TODO: test operatingExpenditures
    }

    /**
     * Test the property 'otherDisbursements'
     */
    @Test
    public void otherDisbursementsTest() {
        // TODO: test otherDisbursements
    }

    /**
     * Test the property 'pacContributionsLessRefunds'
     */
    @Test
    public void pacContributionsLessRefundsTest() {
        // TODO: test pacContributionsLessRefunds
    }

    /**
     * Test the property 'partyContributionsLessRefunds'
     */
    @Test
    public void partyContributionsLessRefundsTest() {
        // TODO: test partyContributionsLessRefunds
    }

    /**
     * Test the property 'repaymentsLoansMadeByCandidate'
     */
    @Test
    public void repaymentsLoansMadeByCandidateTest() {
        // TODO: test repaymentsLoansMadeByCandidate
    }

    /**
     * Test the property 'repaymentsOtherLoans'
     */
    @Test
    public void repaymentsOtherLoansTest() {
        // TODO: test repaymentsOtherLoans
    }

    /**
     * Test the property 'roundedNetReceipts'
     */
    @Test
    public void roundedNetReceiptsTest() {
        // TODO: test roundedNetReceipts
    }

    /**
     * Test the property 'totalContributionRefunds'
     */
    @Test
    public void totalContributionRefundsTest() {
        // TODO: test totalContributionRefunds
    }

    /**
     * Test the property 'totalLoanRepaymentsMade'
     */
    @Test
    public void totalLoanRepaymentsMadeTest() {
        // TODO: test totalLoanRepaymentsMade
    }

    /**
     * Test the property 'transfersFromAffiliatedCommittees'
     */
    @Test
    public void transfersFromAffiliatedCommitteesTest() {
        // TODO: test transfersFromAffiliatedCommittees
    }

    /**
     * Test the property 'transfersToOtherAuthorizedCommittees'
     */
    @Test
    public void transfersToOtherAuthorizedCommitteesTest() {
        // TODO: test transfersToOtherAuthorizedCommittees
    }

}
