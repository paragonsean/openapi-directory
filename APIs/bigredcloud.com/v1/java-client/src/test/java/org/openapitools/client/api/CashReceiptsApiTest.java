/*
 * Big Red Cloud API
 *   <div style='line-height: 30px;'>      <strong>Welcome to the Big Red Cloud API</strong><br/>      This API enables programmatic access to Big Red Cloud data.<br/>      We have used Swagger to auto generate the API documentation on this page, and it also enables direct interaction with the API in this page. <br/>      To get started, you will require an API Key - check out our guide at <a target='_blank' href='https://www.bigredcloud.com/support/generating-api-key-guide/'>https://www.bigredcloud.com/support/generating-api-key-guide/</a> for information on how to get one. <br/>      Use the  'Enter API Key' button below to enter your API key and start interacting with your Big Red Cloud data right on this page. <br/>      The API key will be stored in your browsers local storage for convenience, but you will be able to delete it at any time if you wish. <br/>      For additional information on the API, check out our support article at <a target='_blank' href='https://www.bigredcloud.com/support/api/'>https://www.bigredcloud.com/support/api/</a><br/>  </div>
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
import org.openapitools.client.model.BatchItemCashReceiptDto;
import org.openapitools.client.model.CashReceiptDto;
import org.openapitools.client.model.PageResultCashReceiptQueryDto;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CashReceiptsApi
 */
@Disabled
public class CashReceiptsApiTest {

    private final CashReceiptsApi api = new CashReceiptsApi();

    /**
     * Removes an existing Cash Receipt.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void cashReceiptsDeleteTest() throws ApiException {
        Long id = null;
        String timestamp = null;
        Object response = api.cashReceiptsDelete(id, timestamp);
        // TODO: test validations
    }

    /**
     * Returns a list of company&#39;s Cash Receipts. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void cashReceiptsGetTest() throws ApiException {
        PageResultCashReceiptQueryDto response = api.cashReceiptsGet();
        // TODO: test validations
    }

    /**
     * Creates a new Cash Receipt.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void cashReceiptsPostTest() throws ApiException {
        CashReceiptDto cashReceiptDto = null;
        Object response = api.cashReceiptsPost(cashReceiptDto);
        // TODO: test validations
    }

    /**
     * Processes a batch of Cash Receipts.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void cashReceiptsProcessBatchTest() throws ApiException {
        List<BatchItemCashReceiptDto> batchItemCashReceiptDto = null;
        Object response = api.cashReceiptsProcessBatch(batchItemCashReceiptDto);
        // TODO: test validations
    }

    /**
     * Updates an existing Cash Receipt.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void cashReceiptsPutTest() throws ApiException {
        Long id = null;
        CashReceiptDto cashReceiptDto = null;
        Object response = api.cashReceiptsPut(id, cashReceiptDto);
        // TODO: test validations
    }

    /**
     * Returns information about a single Cash Receipt.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void v1CashReceiptsIdGetTest() throws ApiException {
        Long id = null;
        CashReceiptDto response = api.v1CashReceiptsIdGet(id);
        // TODO: test validations
    }

}
