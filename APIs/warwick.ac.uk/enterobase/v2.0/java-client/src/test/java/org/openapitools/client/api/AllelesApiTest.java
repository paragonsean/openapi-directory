/*
 * Enterobase-API
 *  API for EnteroBase (https://enterobase.warwick.ac.uk)   EnteroBase is a user-friendly online resource, where users can upload their  own sequencing data for de novo assembly by a stream-lined pipeline. The assemblies  are used for calling MLST and wgMLST patterns, allowing users to compare their strains  to publically available genotyping data from other EnteroBase users, GenBank and classical MLST databases.  Click here to find how to get and use an API token: http://bit.ly/1TKlaOU 
 *
 * The version of the OpenAPI document: v2.0
 * Contact: enterobase@warwick.ac.uk
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
 * API tests for AllelesApi
 */
@Disabled
public class AllelesApiTest {

    private final AllelesApi api = new AllelesApi();

    /**
     * Alleles  data 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV20DatabaseSchemeAllelesGetTest() throws ApiException {
        String locus = null;
        String database = null;
        String scheme = null;
        List<String> barcode = null;
        Integer offset = null;
        String alleleId = null;
        List<String> onlyFields = null;
        String seq = null;
        Integer reldate = null;
        Integer limit = null;
        api.apiV20DatabaseSchemeAllelesGet(locus, database, scheme, barcode, offset, alleleId, onlyFields, seq, reldate, limit);
        // TODO: test validations
    }

}
