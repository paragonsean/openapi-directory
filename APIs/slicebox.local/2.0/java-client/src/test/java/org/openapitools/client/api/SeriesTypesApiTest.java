/*
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.Seriestype;
import org.openapitools.client.model.Seriestyperule;
import org.openapitools.client.model.Seriestyperuleattribute;
import org.openapitools.client.model.Seriestypeupdatestatus;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for SeriesTypesApi
 */
@Disabled
public class SeriesTypesApiTest {

    private final SeriesTypesApi api = new SeriesTypesApi();

    /**
     * get a list of all added series types. By filtering search results for certain series types, it is easier for applications to ensure that they read images of applicable types.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void seriestypesGetTest() throws ApiException {
        Long startindex = null;
        Long count = null;
        List<Seriestype> response = api.seriestypesGet(startindex, count);
        // TODO: test validations
    }

    /**
     * remove the series type corresponding to the supplied ID
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void seriestypesIdDeleteTest() throws ApiException {
        Long id = null;
        api.seriestypesIdDelete(id);
        // TODO: test validations
    }

    /**
     * request an asynchronous update of all series, labelling appropriate series with the series type corresponding to the supplied ID.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void seriestypesIdPutTest() throws ApiException {
        Long id = null;
        api.seriestypesIdPut(id);
        // TODO: test validations
    }

    /**
     * add a new series type
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void seriestypesPostTest() throws ApiException {
        Seriestype seriesType = null;
        Seriestype response = api.seriestypesPost(seriesType);
        // TODO: test validations
    }

    /**
     * get a list of rules for assigning series types to series. A rule connects to a series of attributes with values and a resulting series type. If a series has the required values of the listed attributes, it is assigned to the series type of the rule.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void seriestypesRulesGetTest() throws ApiException {
        Long seriestypeid = null;
        List<Seriestyperule> response = api.seriestypesRulesGet(seriestypeid);
        // TODO: test validations
    }

    /**
     * get the list of attributes for the series type rule with the supplied ID.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void seriestypesRulesIdAttributesGetTest() throws ApiException {
        Long id = null;
        List<Seriestyperuleattribute> response = api.seriestypesRulesIdAttributesGet(id);
        // TODO: test validations
    }

    /**
     * add a new series type rule attribute
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void seriestypesRulesIdAttributesPostTest() throws ApiException {
        Long id = null;
        Seriestyperuleattribute seriesTypeRuleAttribute = null;
        Seriestyperuleattribute response = api.seriestypesRulesIdAttributesPost(id, seriesTypeRuleAttribute);
        // TODO: test validations
    }

    /**
     * remove the series type rule corresponding to the supplied ID
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void seriestypesRulesIdDeleteTest() throws ApiException {
        Long id = null;
        api.seriestypesRulesIdDelete(id);
        // TODO: test validations
    }

    /**
     * add a new series type rule
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void seriestypesRulesPostTest() throws ApiException {
        Seriestyperule seriesTypeRule = null;
        Seriestyperule response = api.seriestypesRulesPost(seriesTypeRule);
        // TODO: test validations
    }

    /**
     * remove the series type rule attribute corresponding to the supplied series type and attribute IDs
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void seriestypesRulesRuleIdAttributesAttributeIdDeleteTest() throws ApiException {
        Long ruleId = null;
        Long attributeId = null;
        api.seriestypesRulesRuleIdAttributesAttributeIdDelete(ruleId, attributeId);
        // TODO: test validations
    }

    /**
     * get the status of the internal process of updating series types for series following a change of series types, rules or attributes.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void seriestypesRulesUpdatestatusGetTest() throws ApiException {
        Seriestypeupdatestatus response = api.seriestypesRulesUpdatestatusGet();
        // TODO: test validations
    }

}
