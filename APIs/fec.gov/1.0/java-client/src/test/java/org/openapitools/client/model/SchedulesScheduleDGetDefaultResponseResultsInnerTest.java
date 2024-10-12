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
import java.util.Arrays;
import org.openapitools.client.model.CommitteeHistory;
import org.openapitools.jackson.nullable.JsonNullable;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for SchedulesScheduleDGetDefaultResponseResultsInner
 */
public class SchedulesScheduleDGetDefaultResponseResultsInnerTest {
    private final SchedulesScheduleDGetDefaultResponseResultsInner model = new SchedulesScheduleDGetDefaultResponseResultsInner();

    /**
     * Model tests for SchedulesScheduleDGetDefaultResponseResultsInner
     */
    @Test
    public void testSchedulesScheduleDGetDefaultResponseResultsInner() {
        // TODO: test SchedulesScheduleDGetDefaultResponseResultsInner
    }

    /**
     * Test the property 'actionCode'
     */
    @Test
    public void actionCodeTest() {
        // TODO: test actionCode
    }

    /**
     * Test the property 'actionCodeFull'
     */
    @Test
    public void actionCodeFullTest() {
        // TODO: test actionCodeFull
    }

    /**
     * Test the property 'amountIncurredPeriod'
     */
    @Test
    public void amountIncurredPeriodTest() {
        // TODO: test amountIncurredPeriod
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
     * Test the property 'committeeName'
     */
    @Test
    public void committeeNameTest() {
        // TODO: test committeeName
    }

    /**
     * Test the property 'conduitCommitteeCity'
     */
    @Test
    public void conduitCommitteeCityTest() {
        // TODO: test conduitCommitteeCity
    }

    /**
     * Test the property 'conduitCommitteeId'
     */
    @Test
    public void conduitCommitteeIdTest() {
        // TODO: test conduitCommitteeId
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
     * Test the property 'creditorDebtorCity'
     */
    @Test
    public void creditorDebtorCityTest() {
        // TODO: test creditorDebtorCity
    }

    /**
     * Test the property 'creditorDebtorFirstName'
     */
    @Test
    public void creditorDebtorFirstNameTest() {
        // TODO: test creditorDebtorFirstName
    }

    /**
     * Test the property 'creditorDebtorId'
     */
    @Test
    public void creditorDebtorIdTest() {
        // TODO: test creditorDebtorId
    }

    /**
     * Test the property 'creditorDebtorLastName'
     */
    @Test
    public void creditorDebtorLastNameTest() {
        // TODO: test creditorDebtorLastName
    }

    /**
     * Test the property 'creditorDebtorMiddleName'
     */
    @Test
    public void creditorDebtorMiddleNameTest() {
        // TODO: test creditorDebtorMiddleName
    }

    /**
     * Test the property 'creditorDebtorName'
     */
    @Test
    public void creditorDebtorNameTest() {
        // TODO: test creditorDebtorName
    }

    /**
     * Test the property 'creditorDebtorPrefix'
     */
    @Test
    public void creditorDebtorPrefixTest() {
        // TODO: test creditorDebtorPrefix
    }

    /**
     * Test the property 'creditorDebtorState'
     */
    @Test
    public void creditorDebtorStateTest() {
        // TODO: test creditorDebtorState
    }

    /**
     * Test the property 'creditorDebtorStreet1'
     */
    @Test
    public void creditorDebtorStreet1Test() {
        // TODO: test creditorDebtorStreet1
    }

    /**
     * Test the property 'creditorDebtorStreet2'
     */
    @Test
    public void creditorDebtorStreet2Test() {
        // TODO: test creditorDebtorStreet2
    }

    /**
     * Test the property 'creditorDebtorSuffix'
     */
    @Test
    public void creditorDebtorSuffixTest() {
        // TODO: test creditorDebtorSuffix
    }

    /**
     * Test the property 'electionCycle'
     */
    @Test
    public void electionCycleTest() {
        // TODO: test electionCycle
    }

    /**
     * Test the property 'entityType'
     */
    @Test
    public void entityTypeTest() {
        // TODO: test entityType
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
     * Test the property 'natureOfDebt'
     */
    @Test
    public void natureOfDebtTest() {
        // TODO: test natureOfDebt
    }

    /**
     * Test the property 'originalSubId'
     */
    @Test
    public void originalSubIdTest() {
        // TODO: test originalSubId
    }

    /**
     * Test the property 'outstandingBalanceBeginningOfPeriod'
     */
    @Test
    public void outstandingBalanceBeginningOfPeriodTest() {
        // TODO: test outstandingBalanceBeginningOfPeriod
    }

    /**
     * Test the property 'outstandingBalanceCloseOfPeriod'
     */
    @Test
    public void outstandingBalanceCloseOfPeriodTest() {
        // TODO: test outstandingBalanceCloseOfPeriod
    }

    /**
     * Test the property 'paymentPeriod'
     */
    @Test
    public void paymentPeriodTest() {
        // TODO: test paymentPeriod
    }

    /**
     * Test the property 'pdfUrl'
     */
    @Test
    public void pdfUrlTest() {
        // TODO: test pdfUrl
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

}
