/*
 * nextAuth API
 * API for the nextAuth server
 *
 * The version of the OpenAPI document: 2.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.Transaction;
import org.openapitools.client.model.TransactionId;
import org.openapitools.client.model.TransactionResult;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for TransactionsApi
 */
@Disabled
public class TransactionsApiTest {

    private final TransactionsApi api = new TransactionsApi();

    /**
     * Create a transaction to be approved within the current session.
     *
     * Create a transaction for approval within the current session. Required permission: &#39;sessions&#39;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createTransactionTest() throws ApiException {
        String serverid = null;
        String xNonce = null;
        Transaction msg = null;
        TransactionId response = api.createTransaction(serverid, xNonce, msg);
        // TODO: test validations
    }

    /**
     * Get transaction result for a given transaction.
     *
     * Get transaction result for a given transaction id. Required permission: &#39;sessions&#39;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTransactionResultTest() throws ApiException {
        String serverid = null;
        String transactionid = null;
        TransactionResult response = api.getTransactionResult(serverid, transactionid);
        // TODO: test validations
    }

}
