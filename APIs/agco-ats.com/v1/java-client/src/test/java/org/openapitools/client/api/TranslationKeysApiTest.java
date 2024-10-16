/*
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.APIIPagedResponseOASSupportSharedModelsTranslationKey;
import org.openapitools.client.model.APIModelsApiError;
import org.openapitools.client.model.OASSupportSharedModelsTranslationKey;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for TranslationKeysApi
 */
@Disabled
public class TranslationKeysApiTest {

    private final TranslationKeysApi api = new TranslationKeysApi();

    /**
     * Create a translationKey object.
     *
     * No Documentation Found.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void translationKeysCreateTranslationKeyTest() throws ApiException {
        OASSupportSharedModelsTranslationKey oaSSupportSharedModelsTranslationKey = null;
        Integer response = api.translationKeysCreateTranslationKey(oaSSupportSharedModelsTranslationKey);
        // TODO: test validations
    }

    /**
     * Get a paged response of TranslationKeys.
     *
     * 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void translationKeysGetTest() throws ApiException {
        Integer limit = null;
        Integer offset = null;
        String keyNames = null;
        APIIPagedResponseOASSupportSharedModelsTranslationKey response = api.translationKeysGet(limit, offset, keyNames);
        // TODO: test validations
    }

    /**
     * Get TranslationKey by ID
     *
     * No Documentation Found.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void translationKeysGetTranslationKeyTest() throws ApiException {
        Integer ID = null;
        OASSupportSharedModelsTranslationKey response = api.translationKeysGetTranslationKey(ID);
        // TODO: test validations
    }

    /**
     * Update the StringID of the translationKey object.
     *
     * No Documentation Found.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void translationKeysUpdateTranslationKeyTest() throws ApiException {
        Integer ID = null;
        OASSupportSharedModelsTranslationKey oaSSupportSharedModelsTranslationKey = null;
        api.translationKeysUpdateTranslationKey(ID, oaSSupportSharedModelsTranslationKey);
        // TODO: test validations
    }

}
