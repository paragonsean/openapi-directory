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


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import java.time.LocalDate;
import org.openapitools.client.model.RadAnalystPage;
import org.openapitools.client.model.StateElectionOfficeInfoPage;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for FilerResourcesApi
 */
@Disabled
public class FilerResourcesApiTest {

    private final FilerResourcesApi api = new FilerResourcesApi();

    /**
     *  Use this endpoint to look up the RAD Analyst for a committee.  The mission of the Reports Analysis Division (RAD) is to ensure that campaigns and political committees file timely and accurate reports that fully disclose their financial activities.  RAD is responsible for reviewing statements and financial reports filed by political committees participating in federal elections, providing assistance and guidance to the committees to properly file their reports, and for taking appropriate action to ensure compliance with the Federal Election Campaign Act (FECA). 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void radAnalystGetTest() throws ApiException {
        String apiKey = null;
        LocalDate minAssignmentUpdateDate = null;
        List<Integer> telephoneExt = null;
        List<Integer> analystId = null;
        Boolean sortNullOnly = null;
        Integer page = null;
        List<String> committeeId = null;
        Boolean sortNullsLast = null;
        Boolean sortHideNull = null;
        List<String> name = null;
        Integer perPage = null;
        List<String> email = null;
        List<String> title = null;
        String sort = null;
        LocalDate maxAssignmentUpdateDate = null;
        List<Integer> analystShortId = null;
        RadAnalystPage response = api.radAnalystGet(apiKey, minAssignmentUpdateDate, telephoneExt, analystId, sortNullOnly, page, committeeId, sortNullsLast, sortHideNull, name, perPage, email, title, sort, maxAssignmentUpdateDate, analystShortId);
        // TODO: test validations
    }

    /**
     *  State laws and procedures govern elections for state or local offices as well as how candidates appear on election ballots. Contact the appropriate state election office for more information. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void stateElectionOfficeGetTest() throws ApiException {
        String state = null;
        String apiKey = null;
        Integer page = null;
        Boolean sortHideNull = null;
        Integer perPage = null;
        Boolean sortNullOnly = null;
        String sort = null;
        Boolean sortNullsLast = null;
        StateElectionOfficeInfoPage response = api.stateElectionOfficeGet(state, apiKey, page, sortHideNull, perPage, sortNullOnly, sort, sortNullsLast);
        // TODO: test validations
    }

}
