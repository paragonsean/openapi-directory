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
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.jackson.nullable.JsonNullable;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for CommitteeReportsPresidential
 */
public class CommitteeReportsPresidentialTest {
    private final CommitteeReportsPresidential model = new CommitteeReportsPresidential();

    /**
     * Model tests for CommitteeReportsPresidential
     */
    @Test
    public void testCommitteeReportsPresidential() {
        // TODO: test CommitteeReportsPresidential
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
     * Test the property 'amendmentIndicatorFull'
     */
    @Test
    public void amendmentIndicatorFullTest() {
        // TODO: test amendmentIndicatorFull
    }

    /**
     * Test the property 'beginningImageNumber'
     */
    @Test
    public void beginningImageNumberTest() {
        // TODO: test beginningImageNumber
    }

    /**
     * Test the property 'candidateContributionPeriod'
     */
    @Test
    public void candidateContributionPeriodTest() {
        // TODO: test candidateContributionPeriod
    }

    /**
     * Test the property 'candidateContributionYtd'
     */
    @Test
    public void candidateContributionYtdTest() {
        // TODO: test candidateContributionYtd
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
     * Test the property 'endImageNumber'
     */
    @Test
    public void endImageNumberTest() {
        // TODO: test endImageNumber
    }

    /**
     * Test the property 'exemptLegalAccountingDisbursementPeriod'
     */
    @Test
    public void exemptLegalAccountingDisbursementPeriodTest() {
        // TODO: test exemptLegalAccountingDisbursementPeriod
    }

    /**
     * Test the property 'exemptLegalAccountingDisbursementYtd'
     */
    @Test
    public void exemptLegalAccountingDisbursementYtdTest() {
        // TODO: test exemptLegalAccountingDisbursementYtd
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
     * Test the property 'federalFundsPeriod'
     */
    @Test
    public void federalFundsPeriodTest() {
        // TODO: test federalFundsPeriod
    }

    /**
     * Test the property 'federalFundsYtd'
     */
    @Test
    public void federalFundsYtdTest() {
        // TODO: test federalFundsYtd
    }

    /**
     * Test the property 'fileNumber'
     */
    @Test
    public void fileNumberTest() {
        // TODO: test fileNumber
    }

    /**
     * Test the property 'fundraisingDisbursementsPeriod'
     */
    @Test
    public void fundraisingDisbursementsPeriodTest() {
        // TODO: test fundraisingDisbursementsPeriod
    }

    /**
     * Test the property 'fundraisingDisbursementsYtd'
     */
    @Test
    public void fundraisingDisbursementsYtdTest() {
        // TODO: test fundraisingDisbursementsYtd
    }

    /**
     * Test the property 'htmlUrl'
     */
    @Test
    public void htmlUrlTest() {
        // TODO: test htmlUrl
    }

    /**
     * Test the property 'individualItemizedContributionsPeriod'
     */
    @Test
    public void individualItemizedContributionsPeriodTest() {
        // TODO: test individualItemizedContributionsPeriod
    }

    /**
     * Test the property 'individualItemizedContributionsYtd'
     */
    @Test
    public void individualItemizedContributionsYtdTest() {
        // TODO: test individualItemizedContributionsYtd
    }

    /**
     * Test the property 'individualUnitemizedContributionsPeriod'
     */
    @Test
    public void individualUnitemizedContributionsPeriodTest() {
        // TODO: test individualUnitemizedContributionsPeriod
    }

    /**
     * Test the property 'individualUnitemizedContributionsYtd'
     */
    @Test
    public void individualUnitemizedContributionsYtdTest() {
        // TODO: test individualUnitemizedContributionsYtd
    }

    /**
     * Test the property 'isAmended'
     */
    @Test
    public void isAmendedTest() {
        // TODO: test isAmended
    }

    /**
     * Test the property 'itemsOnHandLiquidated'
     */
    @Test
    public void itemsOnHandLiquidatedTest() {
        // TODO: test itemsOnHandLiquidated
    }

    /**
     * Test the property 'loansReceivedFromCandidatePeriod'
     */
    @Test
    public void loansReceivedFromCandidatePeriodTest() {
        // TODO: test loansReceivedFromCandidatePeriod
    }

    /**
     * Test the property 'loansReceivedFromCandidateYtd'
     */
    @Test
    public void loansReceivedFromCandidateYtdTest() {
        // TODO: test loansReceivedFromCandidateYtd
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
     * Test the property 'offsetsToFundraisingExpendituresPeriod'
     */
    @Test
    public void offsetsToFundraisingExpendituresPeriodTest() {
        // TODO: test offsetsToFundraisingExpendituresPeriod
    }

    /**
     * Test the property 'offsetsToFundraisingExpendituresYtd'
     */
    @Test
    public void offsetsToFundraisingExpendituresYtdTest() {
        // TODO: test offsetsToFundraisingExpendituresYtd
    }

    /**
     * Test the property 'offsetsToLegalAccountingPeriod'
     */
    @Test
    public void offsetsToLegalAccountingPeriodTest() {
        // TODO: test offsetsToLegalAccountingPeriod
    }

    /**
     * Test the property 'offsetsToLegalAccountingYtd'
     */
    @Test
    public void offsetsToLegalAccountingYtdTest() {
        // TODO: test offsetsToLegalAccountingYtd
    }

    /**
     * Test the property 'offsetsToOperatingExpendituresPeriod'
     */
    @Test
    public void offsetsToOperatingExpendituresPeriodTest() {
        // TODO: test offsetsToOperatingExpendituresPeriod
    }

    /**
     * Test the property 'offsetsToOperatingExpendituresYtd'
     */
    @Test
    public void offsetsToOperatingExpendituresYtdTest() {
        // TODO: test offsetsToOperatingExpendituresYtd
    }

    /**
     * Test the property 'operatingExpendituresPeriod'
     */
    @Test
    public void operatingExpendituresPeriodTest() {
        // TODO: test operatingExpendituresPeriod
    }

    /**
     * Test the property 'operatingExpendituresYtd'
     */
    @Test
    public void operatingExpendituresYtdTest() {
        // TODO: test operatingExpendituresYtd
    }

    /**
     * Test the property 'otherDisbursementsPeriod'
     */
    @Test
    public void otherDisbursementsPeriodTest() {
        // TODO: test otherDisbursementsPeriod
    }

    /**
     * Test the property 'otherDisbursementsYtd'
     */
    @Test
    public void otherDisbursementsYtdTest() {
        // TODO: test otherDisbursementsYtd
    }

    /**
     * Test the property 'otherLoansReceivedPeriod'
     */
    @Test
    public void otherLoansReceivedPeriodTest() {
        // TODO: test otherLoansReceivedPeriod
    }

    /**
     * Test the property 'otherLoansReceivedYtd'
     */
    @Test
    public void otherLoansReceivedYtdTest() {
        // TODO: test otherLoansReceivedYtd
    }

    /**
     * Test the property 'otherPoliticalCommitteeContributionsPeriod'
     */
    @Test
    public void otherPoliticalCommitteeContributionsPeriodTest() {
        // TODO: test otherPoliticalCommitteeContributionsPeriod
    }

    /**
     * Test the property 'otherPoliticalCommitteeContributionsYtd'
     */
    @Test
    public void otherPoliticalCommitteeContributionsYtdTest() {
        // TODO: test otherPoliticalCommitteeContributionsYtd
    }

    /**
     * Test the property 'otherReceiptsPeriod'
     */
    @Test
    public void otherReceiptsPeriodTest() {
        // TODO: test otherReceiptsPeriod
    }

    /**
     * Test the property 'otherReceiptsYtd'
     */
    @Test
    public void otherReceiptsYtdTest() {
        // TODO: test otherReceiptsYtd
    }

    /**
     * Test the property 'pdfUrl'
     */
    @Test
    public void pdfUrlTest() {
        // TODO: test pdfUrl
    }

    /**
     * Test the property 'politicalPartyCommitteeContributionsPeriod'
     */
    @Test
    public void politicalPartyCommitteeContributionsPeriodTest() {
        // TODO: test politicalPartyCommitteeContributionsPeriod
    }

    /**
     * Test the property 'politicalPartyCommitteeContributionsYtd'
     */
    @Test
    public void politicalPartyCommitteeContributionsYtdTest() {
        // TODO: test politicalPartyCommitteeContributionsYtd
    }

    /**
     * Test the property 'previousFileNumber'
     */
    @Test
    public void previousFileNumberTest() {
        // TODO: test previousFileNumber
    }

    /**
     * Test the property 'receiptDate'
     */
    @Test
    public void receiptDateTest() {
        // TODO: test receiptDate
    }

    /**
     * Test the property 'refundedIndividualContributionsPeriod'
     */
    @Test
    public void refundedIndividualContributionsPeriodTest() {
        // TODO: test refundedIndividualContributionsPeriod
    }

    /**
     * Test the property 'refundedIndividualContributionsYtd'
     */
    @Test
    public void refundedIndividualContributionsYtdTest() {
        // TODO: test refundedIndividualContributionsYtd
    }

    /**
     * Test the property 'refundedOtherPoliticalCommitteeContributionsPeriod'
     */
    @Test
    public void refundedOtherPoliticalCommitteeContributionsPeriodTest() {
        // TODO: test refundedOtherPoliticalCommitteeContributionsPeriod
    }

    /**
     * Test the property 'refundedOtherPoliticalCommitteeContributionsYtd'
     */
    @Test
    public void refundedOtherPoliticalCommitteeContributionsYtdTest() {
        // TODO: test refundedOtherPoliticalCommitteeContributionsYtd
    }

    /**
     * Test the property 'refundedPoliticalPartyCommitteeContributionsPeriod'
     */
    @Test
    public void refundedPoliticalPartyCommitteeContributionsPeriodTest() {
        // TODO: test refundedPoliticalPartyCommitteeContributionsPeriod
    }

    /**
     * Test the property 'refundedPoliticalPartyCommitteeContributionsYtd'
     */
    @Test
    public void refundedPoliticalPartyCommitteeContributionsYtdTest() {
        // TODO: test refundedPoliticalPartyCommitteeContributionsYtd
    }

    /**
     * Test the property 'repaymentsLoansMadeByCandidatePeriod'
     */
    @Test
    public void repaymentsLoansMadeByCandidatePeriodTest() {
        // TODO: test repaymentsLoansMadeByCandidatePeriod
    }

    /**
     * Test the property 'repaymentsLoansMadeCandidateYtd'
     */
    @Test
    public void repaymentsLoansMadeCandidateYtdTest() {
        // TODO: test repaymentsLoansMadeCandidateYtd
    }

    /**
     * Test the property 'repaymentsOtherLoansPeriod'
     */
    @Test
    public void repaymentsOtherLoansPeriodTest() {
        // TODO: test repaymentsOtherLoansPeriod
    }

    /**
     * Test the property 'repaymentsOtherLoansYtd'
     */
    @Test
    public void repaymentsOtherLoansYtdTest() {
        // TODO: test repaymentsOtherLoansYtd
    }

    /**
     * Test the property 'reportForm'
     */
    @Test
    public void reportFormTest() {
        // TODO: test reportForm
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
     * Test the property 'subtotalSummaryPeriod'
     */
    @Test
    public void subtotalSummaryPeriodTest() {
        // TODO: test subtotalSummaryPeriod
    }

    /**
     * Test the property 'totalContributionRefundsPeriod'
     */
    @Test
    public void totalContributionRefundsPeriodTest() {
        // TODO: test totalContributionRefundsPeriod
    }

    /**
     * Test the property 'totalContributionRefundsYtd'
     */
    @Test
    public void totalContributionRefundsYtdTest() {
        // TODO: test totalContributionRefundsYtd
    }

    /**
     * Test the property 'totalContributionsPeriod'
     */
    @Test
    public void totalContributionsPeriodTest() {
        // TODO: test totalContributionsPeriod
    }

    /**
     * Test the property 'totalContributionsYtd'
     */
    @Test
    public void totalContributionsYtdTest() {
        // TODO: test totalContributionsYtd
    }

    /**
     * Test the property 'totalDisbursementsPeriod'
     */
    @Test
    public void totalDisbursementsPeriodTest() {
        // TODO: test totalDisbursementsPeriod
    }

    /**
     * Test the property 'totalDisbursementsYtd'
     */
    @Test
    public void totalDisbursementsYtdTest() {
        // TODO: test totalDisbursementsYtd
    }

    /**
     * Test the property 'totalIndividualContributionsPeriod'
     */
    @Test
    public void totalIndividualContributionsPeriodTest() {
        // TODO: test totalIndividualContributionsPeriod
    }

    /**
     * Test the property 'totalIndividualContributionsYtd'
     */
    @Test
    public void totalIndividualContributionsYtdTest() {
        // TODO: test totalIndividualContributionsYtd
    }

    /**
     * Test the property 'totalLoanRepaymentsMadePeriod'
     */
    @Test
    public void totalLoanRepaymentsMadePeriodTest() {
        // TODO: test totalLoanRepaymentsMadePeriod
    }

    /**
     * Test the property 'totalLoanRepaymentsMadeYtd'
     */
    @Test
    public void totalLoanRepaymentsMadeYtdTest() {
        // TODO: test totalLoanRepaymentsMadeYtd
    }

    /**
     * Test the property 'totalLoansReceivedPeriod'
     */
    @Test
    public void totalLoansReceivedPeriodTest() {
        // TODO: test totalLoansReceivedPeriod
    }

    /**
     * Test the property 'totalLoansReceivedYtd'
     */
    @Test
    public void totalLoansReceivedYtdTest() {
        // TODO: test totalLoansReceivedYtd
    }

    /**
     * Test the property 'totalOffsetsToOperatingExpendituresPeriod'
     */
    @Test
    public void totalOffsetsToOperatingExpendituresPeriodTest() {
        // TODO: test totalOffsetsToOperatingExpendituresPeriod
    }

    /**
     * Test the property 'totalOffsetsToOperatingExpendituresYtd'
     */
    @Test
    public void totalOffsetsToOperatingExpendituresYtdTest() {
        // TODO: test totalOffsetsToOperatingExpendituresYtd
    }

    /**
     * Test the property 'totalPeriod'
     */
    @Test
    public void totalPeriodTest() {
        // TODO: test totalPeriod
    }

    /**
     * Test the property 'totalReceiptsPeriod'
     */
    @Test
    public void totalReceiptsPeriodTest() {
        // TODO: test totalReceiptsPeriod
    }

    /**
     * Test the property 'totalReceiptsYtd'
     */
    @Test
    public void totalReceiptsYtdTest() {
        // TODO: test totalReceiptsYtd
    }

    /**
     * Test the property 'totalYtd'
     */
    @Test
    public void totalYtdTest() {
        // TODO: test totalYtd
    }

    /**
     * Test the property 'transfersFromAffiliatedCommitteePeriod'
     */
    @Test
    public void transfersFromAffiliatedCommitteePeriodTest() {
        // TODO: test transfersFromAffiliatedCommitteePeriod
    }

    /**
     * Test the property 'transfersFromAffiliatedCommitteeYtd'
     */
    @Test
    public void transfersFromAffiliatedCommitteeYtdTest() {
        // TODO: test transfersFromAffiliatedCommitteeYtd
    }

    /**
     * Test the property 'transfersToOtherAuthorizedCommitteePeriod'
     */
    @Test
    public void transfersToOtherAuthorizedCommitteePeriodTest() {
        // TODO: test transfersToOtherAuthorizedCommitteePeriod
    }

    /**
     * Test the property 'transfersToOtherAuthorizedCommitteeYtd'
     */
    @Test
    public void transfersToOtherAuthorizedCommitteeYtdTest() {
        // TODO: test transfersToOtherAuthorizedCommitteeYtd
    }

}
