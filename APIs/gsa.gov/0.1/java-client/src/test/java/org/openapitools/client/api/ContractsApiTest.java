/*
 * Discovery Market Research
 * <p>This API drives the <a href=\"https://discovery.gsa.gov\">Discovery Market Research Tool</a>. It contains information on the vendors that are part of the OASIS and OASIS Small Business contracting vehicles, such as their contracting history, their elligibility for contract awards, and their small business designations. To learn more about the tool, please visit <a href=\"https://discovery.gsa.gov\">Discovery</a> or see the README on our <a href=\"https://github.com/PSHCDevOps/discovery\">GitHub repository</a>.</p> <p><strong>Please note that the base path for this API is <code>https://api.data.gov/gsa/discovery/</code></strong></p> <p>It requires an API key, obtainable at <a href=\"http://api.data.gov/\">api.data.gov</a>. It must be passed in the <code>api_key</code> parameter with each request.</p>
 *
 * The version of the OpenAPI document: 0.1
 * Contact: discovery-18f@gsa.gov
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ContractsApi
 */
@Disabled
public class ContractsApiTest {

    private final ContractsApi api = new ContractsApi();

    /**
     * This endpoint returns contract history from FPDS for a specific vendor
     *
     * &lt;p&gt;This endpoint returns contract history from FPDS for a specific vendor. The vendor&#39;s DUNS number is a required parameter. You can also filter contracts by their NAICS code to find contracts relevant to a particular category.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listContractsGETTest() throws ApiException {
        String duns = null;
        String naics = null;
        String sort = null;
        String direction = null;
        String page = null;
        Object response = api.listContractsGET(duns, naics, sort, direction, page);
        // TODO: test validations
    }

}
