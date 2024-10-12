/*
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
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
import org.openapitools.client.model.ContentLanguagePreference;
import org.openapitools.client.model.EntryForApiContractPartialFindResult;
import org.openapitools.client.model.EntryOptionalFields;
import org.openapitools.client.model.EntrySortRule;
import org.openapitools.client.model.EntryStatus;
import org.openapitools.client.model.EntryTypes;
import org.openapitools.client.model.NameMatchMode;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for EntryApiApi
 */
@Disabled
public class EntryApiApiTest {

    private final EntryApiApi api = new EntryApiApi();

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiEntriesGetTest() throws ApiException {
        String query = null;
        List<String> tagName = null;
        List<Integer> tagId = null;
        Boolean childTags = null;
        EntryTypes entryTypes = null;
        EntryStatus status = null;
        Integer start = null;
        Integer maxResults = null;
        Boolean getTotalCount = null;
        EntrySortRule sort = null;
        NameMatchMode nameMatchMode = null;
        EntryOptionalFields fields = null;
        ContentLanguagePreference lang = null;
        EntryForApiContractPartialFindResult response = api.apiEntriesGet(query, tagName, tagId, childTags, entryTypes, status, start, maxResults, getTotalCount, sort, nameMatchMode, fields, lang);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiEntriesNamesGetTest() throws ApiException {
        String query = null;
        NameMatchMode nameMatchMode = null;
        Integer maxResults = null;
        List<String> response = api.apiEntriesNamesGet(query, nameMatchMode, maxResults);
        // TODO: test validations
    }

}
