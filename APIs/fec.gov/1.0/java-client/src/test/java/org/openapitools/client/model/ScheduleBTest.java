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
import java.util.Arrays;
import org.openapitools.client.model.CommitteeHistory;
import org.openapitools.jackson.nullable.JsonNullable;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for ScheduleB
 */
public class ScheduleBTest {
    private final ScheduleB model = new ScheduleB();

    /**
     * Model tests for ScheduleB
     */
    @Test
    public void testScheduleB() {
        // TODO: test ScheduleB
    }

    /**
     * Test the property 'amendmentIndicator'
     */
    @Test
    public void amendmentIndicatorTest() {
        // TODO: test amendmentIndicator
    }

    /**
     * Test the property 'amendmentIndicatorDesc'
     */
    @Test
    public void amendmentIndicatorDescTest() {
        // TODO: test amendmentIndicatorDesc
    }

    /**
     * Test the property 'backReferenceScheduleId'
     */
    @Test
    public void backReferenceScheduleIdTest() {
        // TODO: test backReferenceScheduleId
    }

    /**
     * Test the property 'backReferenceTransactionId'
     */
    @Test
    public void backReferenceTransactionIdTest() {
        // TODO: test backReferenceTransactionId
    }

    /**
     * Test the property 'beneficiaryCommitteeName'
     */
    @Test
    public void beneficiaryCommitteeNameTest() {
        // TODO: test beneficiaryCommitteeName
    }

    /**
     * Test the property 'candidateFirstName'
     */
    @Test
    public void candidateFirstNameTest() {
        // TODO: test candidateFirstName
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
     * Test the property 'candidateMiddleName'
     */
    @Test
    public void candidateMiddleNameTest() {
        // TODO: test candidateMiddleName
    }

    /**
     * Test the property 'candidateName'
     */
    @Test
    public void candidateNameTest() {
        // TODO: test candidateName
    }

    /**
     * Test the property 'candidateOffice'
     */
    @Test
    public void candidateOfficeTest() {
        // TODO: test candidateOffice
    }

    /**
     * Test the property 'candidateOfficeDescription'
     */
    @Test
    public void candidateOfficeDescriptionTest() {
        // TODO: test candidateOfficeDescription
    }

    /**
     * Test the property 'candidateOfficeDistrict'
     */
    @Test
    public void candidateOfficeDistrictTest() {
        // TODO: test candidateOfficeDistrict
    }

    /**
     * Test the property 'candidateOfficeState'
     */
    @Test
    public void candidateOfficeStateTest() {
        // TODO: test candidateOfficeState
    }

    /**
     * Test the property 'candidateOfficeStateFull'
     */
    @Test
    public void candidateOfficeStateFullTest() {
        // TODO: test candidateOfficeStateFull
    }

    /**
     * Test the property 'candidatePrefix'
     */
    @Test
    public void candidatePrefixTest() {
        // TODO: test candidatePrefix
    }

    /**
     * Test the property 'candidateSuffix'
     */
    @Test
    public void candidateSuffixTest() {
        // TODO: test candidateSuffix
    }

    /**
     * Test the property 'categoryCode'
     */
    @Test
    public void categoryCodeTest() {
        // TODO: test categoryCode
    }

    /**
     * Test the property 'categoryCodeFull'
     */
    @Test
    public void categoryCodeFullTest() {
        // TODO: test categoryCodeFull
    }

    /**
     * Test the property 'commDt'
     */
    @Test
    public void commDtTest() {
        // TODO: test commDt
    }

    /**
     * Test the property 'committee'
     */
    @Test
    public void committeeTest() {
        // TODO: test committee
    }

    /**
     * Test the property 'committeeId'
     */
    @Test
    public void committeeIdTest() {
        // TODO: test committeeId
    }

    /**
     * Test the property 'conduitCommitteeCity'
     */
    @Test
    public void conduitCommitteeCityTest() {
        // TODO: test conduitCommitteeCity
    }

    /**
     * Test the property 'conduitCommitteeName'
     */
    @Test
    public void conduitCommitteeNameTest() {
        // TODO: test conduitCommitteeName
    }

    /**
     * Test the property 'conduitCommitteeState'
     */
    @Test
    public void conduitCommitteeStateTest() {
        // TODO: test conduitCommitteeState
    }

    /**
     * Test the property 'conduitCommitteeStreet1'
     */
    @Test
    public void conduitCommitteeStreet1Test() {
        // TODO: test conduitCommitteeStreet1
    }

    /**
     * Test the property 'conduitCommitteeStreet2'
     */
    @Test
    public void conduitCommitteeStreet2Test() {
        // TODO: test conduitCommitteeStreet2
    }

    /**
     * Test the property 'conduitCommitteeZip'
     */
    @Test
    public void conduitCommitteeZipTest() {
        // TODO: test conduitCommitteeZip
    }

    /**
     * Test the property 'disbursementAmount'
     */
    @Test
    public void disbursementAmountTest() {
        // TODO: test disbursementAmount
    }

    /**
     * Test the property 'disbursementDate'
     */
    @Test
    public void disbursementDateTest() {
        // TODO: test disbursementDate
    }

    /**
     * Test the property 'disbursementDescription'
     */
    @Test
    public void disbursementDescriptionTest() {
        // TODO: test disbursementDescription
    }

    /**
     * Test the property 'disbursementPurposeCategory'
     */
    @Test
    public void disbursementPurposeCategoryTest() {
        // TODO: test disbursementPurposeCategory
    }

    /**
     * Test the property 'disbursementType'
     */
    @Test
    public void disbursementTypeTest() {
        // TODO: test disbursementType
    }

    /**
     * Test the property 'disbursementTypeDescription'
     */
    @Test
    public void disbursementTypeDescriptionTest() {
        // TODO: test disbursementTypeDescription
    }

    /**
     * Test the property 'electionType'
     */
    @Test
    public void electionTypeTest() {
        // TODO: test electionType
    }

    /**
     * Test the property 'electionTypeFull'
     */
    @Test
    public void electionTypeFullTest() {
        // TODO: test electionTypeFull
    }

    /**
     * Test the property 'entityType'
     */
    @Test
    public void entityTypeTest() {
        // TODO: test entityType
    }

    /**
     * Test the property 'entityTypeDesc'
     */
    @Test
    public void entityTypeDescTest() {
        // TODO: test entityTypeDesc
    }

    /**
     * Test the property 'fecElectionTypeDesc'
     */
    @Test
    public void fecElectionTypeDescTest() {
        // TODO: test fecElectionTypeDesc
    }

    /**
     * Test the property 'fecElectionYear'
     */
    @Test
    public void fecElectionYearTest() {
        // TODO: test fecElectionYear
    }

    /**
     * Test the property 'fileNumber'
     */
    @Test
    public void fileNumberTest() {
        // TODO: test fileNumber
    }

    /**
     * Test the property 'filingForm'
     */
    @Test
    public void filingFormTest() {
        // TODO: test filingForm
    }

    /**
     * Test the property 'imageNumber'
     */
    @Test
    public void imageNumberTest() {
        // TODO: test imageNumber
    }

    /**
     * Test the property 'lineNumber'
     */
    @Test
    public void lineNumberTest() {
        // TODO: test lineNumber
    }

    /**
     * Test the property 'lineNumberLabel'
     */
    @Test
    public void lineNumberLabelTest() {
        // TODO: test lineNumberLabel
    }

    /**
     * Test the property 'linkId'
     */
    @Test
    public void linkIdTest() {
        // TODO: test linkId
    }

    /**
     * Test the property 'loadDate'
     */
    @Test
    public void loadDateTest() {
        // TODO: test loadDate
    }

    /**
     * Test the property 'memoCode'
     */
    @Test
    public void memoCodeTest() {
        // TODO: test memoCode
    }

    /**
     * Test the property 'memoCodeFull'
     */
    @Test
    public void memoCodeFullTest() {
        // TODO: test memoCodeFull
    }

    /**
     * Test the property 'memoText'
     */
    @Test
    public void memoTextTest() {
        // TODO: test memoText
    }

    /**
     * Test the property 'memoedSubtotal'
     */
    @Test
    public void memoedSubtotalTest() {
        // TODO: test memoedSubtotal
    }

    /**
     * Test the property 'nationalCommitteeNonfederalAccount'
     */
    @Test
    public void nationalCommitteeNonfederalAccountTest() {
        // TODO: test nationalCommitteeNonfederalAccount
    }

    /**
     * Test the property 'originalSubId'
     */
    @Test
    public void originalSubIdTest() {
        // TODO: test originalSubId
    }

    /**
     * Test the property 'payeeEmployer'
     */
    @Test
    public void payeeEmployerTest() {
        // TODO: test payeeEmployer
    }

    /**
     * Test the property 'payeeFirstName'
     */
    @Test
    public void payeeFirstNameTest() {
        // TODO: test payeeFirstName
    }

    /**
     * Test the property 'payeeLastName'
     */
    @Test
    public void payeeLastNameTest() {
        // TODO: test payeeLastName
    }

    /**
     * Test the property 'payeeMiddleName'
     */
    @Test
    public void payeeMiddleNameTest() {
        // TODO: test payeeMiddleName
    }

    /**
     * Test the property 'payeeOccupation'
     */
    @Test
    public void payeeOccupationTest() {
        // TODO: test payeeOccupation
    }

    /**
     * Test the property 'payeePrefix'
     */
    @Test
    public void payeePrefixTest() {
        // TODO: test payeePrefix
    }

    /**
     * Test the property 'payeeSuffix'
     */
    @Test
    public void payeeSuffixTest() {
        // TODO: test payeeSuffix
    }

    /**
     * Test the property 'pdfUrl'
     */
    @Test
    public void pdfUrlTest() {
        // TODO: test pdfUrl
    }

    /**
     * Test the property 'recipientCity'
     */
    @Test
    public void recipientCityTest() {
        // TODO: test recipientCity
    }

    /**
     * Test the property 'recipientCommittee'
     */
    @Test
    public void recipientCommitteeTest() {
        // TODO: test recipientCommittee
    }

    /**
     * Test the property 'recipientCommitteeId'
     */
    @Test
    public void recipientCommitteeIdTest() {
        // TODO: test recipientCommitteeId
    }

    /**
     * Test the property 'recipientName'
     */
    @Test
    public void recipientNameTest() {
        // TODO: test recipientName
    }

    /**
     * Test the property 'recipientState'
     */
    @Test
    public void recipientStateTest() {
        // TODO: test recipientState
    }

    /**
     * Test the property 'recipientZip'
     */
    @Test
    public void recipientZipTest() {
        // TODO: test recipientZip
    }

    /**
     * Test the property 'refDispExcessFlg'
     */
    @Test
    public void refDispExcessFlgTest() {
        // TODO: test refDispExcessFlg
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
     * Test the property 'scheduleType'
     */
    @Test
    public void scheduleTypeTest() {
        // TODO: test scheduleType
    }

    /**
     * Test the property 'scheduleTypeFull'
     */
    @Test
    public void scheduleTypeFullTest() {
        // TODO: test scheduleTypeFull
    }

    /**
     * Test the property 'semiAnnualBundledRefund'
     */
    @Test
    public void semiAnnualBundledRefundTest() {
        // TODO: test semiAnnualBundledRefund
    }

    /**
     * Test the property 'spenderCommitteeDesignation'
     */
    @Test
    public void spenderCommitteeDesignationTest() {
        // TODO: test spenderCommitteeDesignation
    }

    /**
     * Test the property 'spenderCommitteeOrgType'
     */
    @Test
    public void spenderCommitteeOrgTypeTest() {
        // TODO: test spenderCommitteeOrgType
    }

    /**
     * Test the property 'spenderCommitteeType'
     */
    @Test
    public void spenderCommitteeTypeTest() {
        // TODO: test spenderCommitteeType
    }

    /**
     * Test the property 'subId'
     */
    @Test
    public void subIdTest() {
        // TODO: test subId
    }

    /**
     * Test the property 'transactionId'
     */
    @Test
    public void transactionIdTest() {
        // TODO: test transactionId
    }

    /**
     * Test the property 'twoYearTransactionPeriod'
     */
    @Test
    public void twoYearTransactionPeriodTest() {
        // TODO: test twoYearTransactionPeriod
    }

    /**
     * Test the property 'unusedRecipientCommitteeId'
     */
    @Test
    public void unusedRecipientCommitteeIdTest() {
        // TODO: test unusedRecipientCommitteeId
    }

}
