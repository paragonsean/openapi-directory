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
import org.openapitools.client.model.Filter;
import org.openapitools.client.model.SourceTagFilter;
import org.openapitools.client.model.TagPathTag;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for FilteringApi
 */
@Disabled
public class FilteringApiTest {

    private final FilteringApi api = new FilteringApi();

    /**
     * Get a list of source to filter associations.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void filteringAssociationsGetTest() throws ApiException {
        Long startindex = null;
        Long count = null;
        List<SourceTagFilter> response = api.filteringAssociationsGet(startindex, count);
        // TODO: test validations
    }

    /**
     * remove the source &lt;-&gt; filter association corresponding to the supplied ID
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void filteringAssociationsIdDeleteTest() throws ApiException {
        Long id = null;
        api.filteringAssociationsIdDelete(id);
        // TODO: test validations
    }

    /**
     * Inserts or updates a source &lt;-&gt; filter associations. If the specified Source already  has an association this is updated, otherwise a new is inserted.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void filteringAssociationsPostTest() throws ApiException {
        SourceTagFilter sourcetagfilter = null;
        api.filteringAssociationsPost(sourcetagfilter);
        // TODO: test validations
    }

    /**
     * List defined filters
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void filteringFiltersGetTest() throws ApiException {
        Long startindex = null;
        Long count = null;
        List<Filter> response = api.filteringFiltersGet(startindex, count);
        // TODO: test validations
    }

    /**
     * remove the filter corresponding to the supplied ID
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void filteringFiltersIdDeleteTest() throws ApiException {
        Long id = null;
        api.filteringFiltersIdDelete(id);
        // TODO: test validations
    }

    /**
     * List tagpaths for the selected filter
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void filteringFiltersIdTagpathsGetTest() throws ApiException {
        Long id = null;
        List<TagPathTag> response = api.filteringFiltersIdTagpathsGet(id);
        // TODO: test validations
    }

    /**
     * add a tagpath to a filter
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void filteringFiltersIdTagpathsPostTest() throws ApiException {
        Long id = null;
        TagPathTag tagpath = null;
        api.filteringFiltersIdTagpathsPost(id, tagpath);
        // TODO: test validations
    }

    /**
     * remove the tagpath corresponding to the supplied ID
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void filteringFiltersIdTagpathsTagpathidDeleteTest() throws ApiException {
        Long id = null;
        Long tagpathid = null;
        api.filteringFiltersIdTagpathsTagpathidDelete(id, tagpathid);
        // TODO: test validations
    }

    /**
     * Inserts or updates a filter. If a filter with same name as supplied filter exists this filter is updated, otherwise a new filter is inserted.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void filteringFiltersPostTest() throws ApiException {
        Filter tagFilter = null;
        api.filteringFiltersPost(tagFilter);
        // TODO: test validations
    }

}
