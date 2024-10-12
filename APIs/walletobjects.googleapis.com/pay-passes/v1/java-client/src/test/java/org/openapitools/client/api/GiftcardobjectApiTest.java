/*
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
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
import org.openapitools.client.model.AddMessageRequest;
import org.openapitools.client.model.GiftCardObject;
import org.openapitools.client.model.GiftCardObjectAddMessageResponse;
import org.openapitools.client.model.GiftCardObjectListResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for GiftcardobjectApi
 */
@Disabled
public class GiftcardobjectApiTest {

    private final GiftcardobjectApi api = new GiftcardobjectApi();

    /**
     * Adds a message to the gift card object referenced by the given object ID.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void walletobjectsGiftcardobjectAddmessageTest() throws ApiException {
        String resourceId = null;
        String $xgafv = null;
        String accessToken = null;
        String alt = null;
        String paramCallback = null;
        String fields = null;
        String key = null;
        String oauthToken = null;
        Boolean prettyPrint = null;
        String quotaUser = null;
        String uploadProtocol = null;
        String uploadType = null;
        AddMessageRequest addMessageRequest = null;
        GiftCardObjectAddMessageResponse response = api.walletobjectsGiftcardobjectAddmessage(resourceId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, addMessageRequest);
        // TODO: test validations
    }

    /**
     * Returns the gift card object with the given object ID.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void walletobjectsGiftcardobjectGetTest() throws ApiException {
        String resourceId = null;
        String $xgafv = null;
        String accessToken = null;
        String alt = null;
        String paramCallback = null;
        String fields = null;
        String key = null;
        String oauthToken = null;
        Boolean prettyPrint = null;
        String quotaUser = null;
        String uploadProtocol = null;
        String uploadType = null;
        GiftCardObject response = api.walletobjectsGiftcardobjectGet(resourceId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
        // TODO: test validations
    }

    /**
     * Inserts an gift card object with the given ID and properties.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void walletobjectsGiftcardobjectInsertTest() throws ApiException {
        String $xgafv = null;
        String accessToken = null;
        String alt = null;
        String paramCallback = null;
        String fields = null;
        String key = null;
        String oauthToken = null;
        Boolean prettyPrint = null;
        String quotaUser = null;
        String uploadProtocol = null;
        String uploadType = null;
        GiftCardObject giftCardObject = null;
        GiftCardObject response = api.walletobjectsGiftcardobjectInsert($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, giftCardObject);
        // TODO: test validations
    }

    /**
     * Returns a list of all gift card objects for a given issuer ID.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void walletobjectsGiftcardobjectListTest() throws ApiException {
        String $xgafv = null;
        String accessToken = null;
        String alt = null;
        String paramCallback = null;
        String fields = null;
        String key = null;
        String oauthToken = null;
        Boolean prettyPrint = null;
        String quotaUser = null;
        String uploadProtocol = null;
        String uploadType = null;
        String classId = null;
        Integer maxResults = null;
        String token = null;
        GiftCardObjectListResponse response = api.walletobjectsGiftcardobjectList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, classId, maxResults, token);
        // TODO: test validations
    }

    /**
     * Updates the gift card object referenced by the given object ID. This method supports patch semantics.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void walletobjectsGiftcardobjectPatchTest() throws ApiException {
        String resourceId = null;
        String $xgafv = null;
        String accessToken = null;
        String alt = null;
        String paramCallback = null;
        String fields = null;
        String key = null;
        String oauthToken = null;
        Boolean prettyPrint = null;
        String quotaUser = null;
        String uploadProtocol = null;
        String uploadType = null;
        GiftCardObject giftCardObject = null;
        GiftCardObject response = api.walletobjectsGiftcardobjectPatch(resourceId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, giftCardObject);
        // TODO: test validations
    }

    /**
     * Updates the gift card object referenced by the given object ID.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void walletobjectsGiftcardobjectUpdateTest() throws ApiException {
        String resourceId = null;
        String $xgafv = null;
        String accessToken = null;
        String alt = null;
        String paramCallback = null;
        String fields = null;
        String key = null;
        String oauthToken = null;
        Boolean prettyPrint = null;
        String quotaUser = null;
        String uploadProtocol = null;
        String uploadType = null;
        GiftCardObject giftCardObject = null;
        GiftCardObject response = api.walletobjectsGiftcardobjectUpdate(resourceId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, giftCardObject);
        // TODO: test validations
    }

}
