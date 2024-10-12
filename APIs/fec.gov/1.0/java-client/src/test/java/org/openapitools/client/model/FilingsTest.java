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
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.jackson.nullable.JsonNullable;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for Filings
 */
public class FilingsTest {
    private final Filings model = new Filings();

    /**
     * Model tests for Filings
     */
    @Test
    public void testFilings() {
        // TODO: test Filings
    }

    /**
     * Test the property 'additionalBankNames'
     */
    @Test
    public void additionalBankNamesTest() {
        // TODO: test additionalBankNames
    }

    /**
     * Test the property 'amendmentChain'
     */
    @Test
    public void amendmentChainTest() {
        // TODO: test amendmentChain
    }

    /**
     * Test the property 'amendmentIndicator'
     */
    @Test
    public void amendmentIndicatorTest() {
        // TODO: test amendmentIndicator
    }

    /**
     * Test the property 'amendmentVersion'
     */
    @Test
    public void amendmentVersionTest() {
        // TODO: test amendmentVersion
    }

    /**
     * Test the property 'bankDepositoryCity'
     */
    @Test
    public void bankDepositoryCityTest() {
        // TODO: test bankDepositoryCity
    }

    /**
     * Test the property 'bankDepositoryName'
     */
    @Test
    public void bankDepositoryNameTest() {
        // TODO: test bankDepositoryName
    }

    /**
     * Test the property 'bankDepositoryState'
     */
    @Test
    public void bankDepositoryStateTest() {
        // TODO: test bankDepositoryState
    }

    /**
     * Test the property 'bankDepositoryStreet1'
     */
    @Test
    public void bankDepositoryStreet1Test() {
        // TODO: test bankDepositoryStreet1
    }

    /**
     * Test the property 'bankDepositoryStreet2'
     */
    @Test
    public void bankDepositoryStreet2Test() {
        // TODO: test bankDepositoryStreet2
    }

    /**
     * Test the property 'bankDepositoryZip'
     */
    @Test
    public void bankDepositoryZipTest() {
        // TODO: test bankDepositoryZip
    }

    /**
     * Test the property 'beginningImageNumber'
     */
    @Test
    public void beginningImageNumberTest() {
        // TODO: test beginningImageNumber
    }

    /**
     * Test the property 'candidateId'
     */
    @Test
    public void candidateIdTest() {
        // TODO: test candidateId
    }

    /**
     * Test the property 'candidateName'
     */
    @Test
    public void candidateNameTest() {
        // TODO: test candidateName
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
     * Test the property 'cycle'
     */
    @Test
    public void cycleTest() {
        // TODO: test cycle
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
     * Test the property 'documentType'
     */
    @Test
    public void documentTypeTest() {
        // TODO: test documentType
    }

    /**
     * Test the property 'documentTypeFull'
     */
    @Test
    public void documentTypeFullTest() {
        // TODO: test documentTypeFull
    }

    /**
     * Test the property 'electionYear'
     */
    @Test
    public void electionYearTest() {
        // TODO: test electionYear
    }

    /**
     * Test the property 'endingImageNumber'
     */
    @Test
    public void endingImageNumberTest() {
        // TODO: test endingImageNumber
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
     * Test the property 'formCategory'
     */
    @Test
    public void formCategoryTest() {
        // TODO: test formCategory
    }

    /**
     * Test the property 'formType'
     */
    @Test
    public void formTypeTest() {
        // TODO: test formType
    }

    /**
     * Test the property 'housePersonalFunds'
     */
    @Test
    public void housePersonalFundsTest() {
        // TODO: test housePersonalFunds
    }

    /**
     * Test the property 'htmlUrl'
     */
    @Test
    public void htmlUrlTest() {
        // TODO: test htmlUrl
    }

    /**
     * Test the property 'isAmended'
     */
    @Test
    public void isAmendedTest() {
        // TODO: test isAmended
    }

    /**
     * Test the property 'meansFiled'
     */
    @Test
    public void meansFiledTest() {
        // TODO: test meansFiled
    }

    /**
     * Test the property 'mostRecent'
     */
    @Test
    public void mostRecentTest() {
        // TODO: test mostRecent
    }

    /**
     * Test the property 'mostRecentFileNumber'
     */
    @Test
    public void mostRecentFileNumberTest() {
        // TODO: test mostRecentFileNumber
    }

    /**
     * Test the property 'netDonations'
     */
    @Test
    public void netDonationsTest() {
        // TODO: test netDonations
    }

    /**
     * Test the property 'office'
     */
    @Test
    public void officeTest() {
        // TODO: test office
    }

    /**
     * Test the property 'oppositionPersonalFunds'
     */
    @Test
    public void oppositionPersonalFundsTest() {
        // TODO: test oppositionPersonalFunds
    }

    /**
     * Test the property 'pages'
     */
    @Test
    public void pagesTest() {
        // TODO: test pages
    }

    /**
     * Test the property 'party'
     */
    @Test
    public void partyTest() {
        // TODO: test party
    }

    /**
     * Test the property 'pdfUrl'
     */
    @Test
    public void pdfUrlTest() {
        // TODO: test pdfUrl
    }

    /**
     * Test the property 'previousFileNumber'
     */
    @Test
    public void previousFileNumberTest() {
        // TODO: test previousFileNumber
    }

    /**
     * Test the property 'primaryGeneralIndicator'
     */
    @Test
    public void primaryGeneralIndicatorTest() {
        // TODO: test primaryGeneralIndicator
    }

    /**
     * Test the property 'receiptDate'
     */
    @Test
    public void receiptDateTest() {
        // TODO: test receiptDate
    }

    /**
     * Test the property 'reportType'
     */
    @Test
    public void reportTypeTest() {
        // TODO: test reportType
    }

    /**
     * Test the property 'reportTypeFull'
     */
    @Test
    public void reportTypeFullTest() {
        // TODO: test reportTypeFull
    }

    /**
     * Test the property 'reportYear'
     */
    @Test
    public void reportYearTest() {
        // TODO: test reportYear
    }

    /**
     * Test the property 'requestType'
     */
    @Test
    public void requestTypeTest() {
        // TODO: test requestType
    }

    /**
     * Test the property 'senatePersonalFunds'
     */
    @Test
    public void senatePersonalFundsTest() {
        // TODO: test senatePersonalFunds
    }

    /**
     * Test the property 'state'
     */
    @Test
    public void stateTest() {
        // TODO: test state
    }

    /**
     * Test the property 'subId'
     */
    @Test
    public void subIdTest() {
        // TODO: test subId
    }

    /**
     * Test the property 'totalCommunicationCost'
     */
    @Test
    public void totalCommunicationCostTest() {
        // TODO: test totalCommunicationCost
    }

    /**
     * Test the property 'totalDisbursements'
     */
    @Test
    public void totalDisbursementsTest() {
        // TODO: test totalDisbursements
    }

    /**
     * Test the property 'totalIndependentExpenditures'
     */
    @Test
    public void totalIndependentExpendituresTest() {
        // TODO: test totalIndependentExpenditures
    }

    /**
     * Test the property 'totalIndividualContributions'
     */
    @Test
    public void totalIndividualContributionsTest() {
        // TODO: test totalIndividualContributions
    }

    /**
     * Test the property 'totalReceipts'
     */
    @Test
    public void totalReceiptsTest() {
        // TODO: test totalReceipts
    }

    /**
     * Test the property 'treasurerName'
     */
    @Test
    public void treasurerNameTest() {
        // TODO: test treasurerName
    }

    /**
     * Test the property 'updateDate'
     */
    @Test
    public void updateDateTest() {
        // TODO: test updateDate
    }

}
