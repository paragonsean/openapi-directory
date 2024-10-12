/*
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ErrorResponse;
import org.openapitools.client.model.SalesCreditmemoRepositoryV1SavePostRequest;
import org.openapitools.client.model.SalesDataCreditmemoInterface;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CreditmemoApi
 */
@Disabled
public class CreditmemoApiTest {

    private final CreditmemoApi api = new CreditmemoApi();

    /**
     * creditmemo
     *
     * Performs persist operations for a specified credit memo.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void salesCreditmemoRepositoryV1SavePostTest() throws ApiException {
        SalesCreditmemoRepositoryV1SavePostRequest salesCreditmemoRepositoryV1SavePostRequest = null;
        SalesDataCreditmemoInterface response = api.salesCreditmemoRepositoryV1SavePost(salesCreditmemoRepositoryV1SavePostRequest);
        // TODO: test validations
    }

}
