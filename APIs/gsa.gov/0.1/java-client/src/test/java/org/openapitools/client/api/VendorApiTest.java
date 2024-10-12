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
 * API tests for VendorApi
 */
@Disabled
public class VendorApiTest {

    private final VendorApi api = new VendorApi();

    /**
     * This endpoint returns a single vendor by their 9 digit DUNS number
     *
     * &lt;p&gt;This endpoint returns a single vendor by their 9 digit DUNS number. DUNS numbers can be looked up in the &lt;a href&#x3D;\&quot;https://www.sam.gov\&quot;&gt;System for Award Management&lt;/a&gt; by vendor name.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getVendorGETTest() throws ApiException {
        String duns = null;
        Object response = api.getVendorGET(duns);
        // TODO: test validations
    }

}
