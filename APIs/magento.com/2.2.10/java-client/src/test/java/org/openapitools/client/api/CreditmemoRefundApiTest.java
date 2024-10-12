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
import org.openapitools.client.model.SalesCreditmemoManagementV1RefundPostRequest;
import org.openapitools.client.model.SalesDataCreditmemoInterface;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CreditmemoRefundApi
 */
@Disabled
public class CreditmemoRefundApiTest {

    private final CreditmemoRefundApi api = new CreditmemoRefundApi();

    /**
     * creditmemo/refund
     *
     * Prepare creditmemo to refund and save it.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void salesCreditmemoManagementV1RefundPostTest() throws ApiException {
        SalesCreditmemoManagementV1RefundPostRequest salesCreditmemoManagementV1RefundPostRequest = null;
        SalesDataCreditmemoInterface response = api.salesCreditmemoManagementV1RefundPost(salesCreditmemoManagementV1RefundPostRequest);
        // TODO: test validations
    }

}
