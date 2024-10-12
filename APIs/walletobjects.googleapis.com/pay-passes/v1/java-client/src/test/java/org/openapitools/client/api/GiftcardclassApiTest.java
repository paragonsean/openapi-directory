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
import org.openapitools.client.model.GiftCardClass;
import org.openapitools.client.model.GiftCardClassAddMessageResponse;
import org.openapitools.client.model.GiftCardClassListResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for GiftcardclassApi
 */
@Disabled
public class GiftcardclassApiTest {

    private final GiftcardclassApi api = new GiftcardclassApi();

    /**
     * Adds a message to the gift card class referenced by the given class ID.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void walletobjectsGiftcardclassAddmessageTest() throws ApiException {
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
        GiftCardClassAddMessageResponse response = api.walletobjectsGiftcardclassAddmessage(resourceId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, addMessageRequest);
        // TODO: test validations
    }

    /**
     * Returns the gift card class with the given class ID.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void walletobjectsGiftcardclassGetTest() throws ApiException {
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
        GiftCardClass response = api.walletobjectsGiftcardclassGet(resourceId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
        // TODO: test validations
    }

    /**
     * Inserts an gift card class with the given ID and properties.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void walletobjectsGiftcardclassInsertTest() throws ApiException {
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
        GiftCardClass giftCardClass = null;
        GiftCardClass response = api.walletobjectsGiftcardclassInsert($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, giftCardClass);
        // TODO: test validations
    }

    /**
     * Returns a list of all gift card classes for a given issuer ID.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void walletobjectsGiftcardclassListTest() throws ApiException {
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
        String issuerId = null;
        Integer maxResults = null;
        String token = null;
        GiftCardClassListResponse response = api.walletobjectsGiftcardclassList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, issuerId, maxResults, token);
        // TODO: test validations
    }

    /**
     * Updates the gift card class referenced by the given class ID. This method supports patch semantics.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void walletobjectsGiftcardclassPatchTest() throws ApiException {
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
        GiftCardClass giftCardClass = null;
        GiftCardClass response = api.walletobjectsGiftcardclassPatch(resourceId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, giftCardClass);
        // TODO: test validations
    }

    /**
     * Updates the gift card class referenced by the given class ID.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void walletobjectsGiftcardclassUpdateTest() throws ApiException {
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
        GiftCardClass giftCardClass = null;
        GiftCardClass response = api.walletobjectsGiftcardclassUpdate(resourceId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, giftCardClass);
        // TODO: test validations
    }

}
