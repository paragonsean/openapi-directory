/*
 * Fire Financial Services Business API
 * The fire.com API allows you to deeply integrate Business Account features into your application or back-office systems.  The API provides read access to your profile, accounts and transactions, event-driven notifications of activity on the account and payment initiation via batches. Each feature has its own HTTP endpoint and every endpoint has its own permission.   The API exposes 3 main areas of functionality: financial functions, service information and service configuration. ## Financial Functions These functions provide access to your account details, transactions, payee accounts, payment initiation etc. ## Service Functions These provide information about the fees and limits applied to your account. ## Service configuration These provide information about your service configs - applications, webhooks, API tokens, etc. 
 *
 * The version of the OpenAPI document: 1.0
 * Contact: api@fire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.AddBankTransferBatchPaymentRequest;
import org.openapitools.client.model.Batch;
import org.openapitools.client.model.BatchApprovers;
import org.openapitools.client.model.BatchItemInternalTransfer;
import org.openapitools.client.model.BatchItemInternationalTransferMode1;
import org.openapitools.client.model.BatchItems;
import org.openapitools.client.model.NewBatch;
import org.openapitools.client.model.NewBatchItemResponse;
import org.openapitools.client.model.NewBatchResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for PaymentBatchesApi
 */
@Disabled
public class PaymentBatchesApiTest {

    private final PaymentBatchesApi api = new PaymentBatchesApi();

    /**
     * Add a bank transfer payment to the batch.
     *
     * There are two ways to process bank transfers - by Payee ID (**Mode 1**) or by Payee Account Details (**Mode 2**).  **Mode 1:** Use the payee IDs of existing approved payees set up against your account. These batches can be approved in the normal manner.  **Mode 2:** Use the account details of the payee. In the event that these details correspond to an existing approved payee, the batch can be approved as normal. If the account details are new, a batch of New Payees will automatically be created. This batch will need to be approved before the Payment batch can be approved. These payees will then exist as approved payees for future batches. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addBankTransferBatchPaymentTest() throws ApiException {
        String batchUuid = null;
        AddBankTransferBatchPaymentRequest addBankTransferBatchPaymentRequest = null;
        NewBatchItemResponse response = api.addBankTransferBatchPayment(batchUuid, addBankTransferBatchPaymentRequest);
        // TODO: test validations
    }

    /**
     * Add an internal transfer payment to the batch
     *
     * Simply specify the source account, destination account, amount and a reference.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addInternalTransferBatchPaymentTest() throws ApiException {
        String batchUuid = null;
        BatchItemInternalTransfer batchItemInternalTransfer = null;
        NewBatchItemResponse response = api.addInternalTransferBatchPayment(batchUuid, batchItemInternalTransfer);
        // TODO: test validations
    }

    /**
     * Add an international transfer payment to the batch.
     *
     * International transfers must be added to a batch using the Payee ID (**Mode 1**). Payees must be set up using the web application.  **Mode 1:** Use the payee IDs of existing approved payees set up against your account. These batches can be approved in the normal manner. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addInternationalTransferBatchPaymentTest() throws ApiException {
        String batchUuid = null;
        BatchItemInternationalTransferMode1 batchItemInternationalTransferMode1 = null;
        NewBatchItemResponse response = api.addInternationalTransferBatchPayment(batchUuid, batchItemInternationalTransferMode1);
        // TODO: test validations
    }

    /**
     * Cancel a batch
     *
     * Cancels the Batch. You can only cancel a batch before it is submitted for approval (while it is in the OPEN state).
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void cancelBatchPaymentTest() throws ApiException {
        String batchUuid = null;
        api.cancelBatchPayment(batchUuid);
        // TODO: test validations
    }

    /**
     * Create a new batch of payments
     *
     * The fire.com API allows businesses to automate payments between their accounts or to third parties across the UK and Europe.  For added security, the API can only set up the payments in batches. These batches must be approved by an authorised user via the firework mobile app.   The process is as follows:  **1.**Create a new batch  **2.**Add payments to the batch  **3.**Submit the batch for approval  Once the batch is submitted, the authorised users will receive notifications to their firework mobile apps. They can review the contents of the batch and then approve or reject it. If approved, the batch is then processed. You can avail of enhanced security by using Dual Authorisation to verify payments if you wish. Dual Authorisation can be enabled by you when setting up your API application in firework online.  **Batch Life Cycle Events**  A batch webhook can be specified to receive details of all the payments as they are processed. This webhook receives notifications for every event in the batch lifecycle.  The following events are triggered during a batch:  **batch.opened:** Contains the details of the batch opened. Checks that the callback URL exists - unless a HTTP 200 response is returned, the callback URL will not be configured.  **batch.item-added:** Details of the item added to the batch  **batch.item-removed:** Details of the item removed from the batch  **batch.cancelled:** Notifies that the batch was cancelled.  **batch.submitted:** Notifes that the batch was submitted  **batch.approved:** Notifies that the batch was approved.  **batch.rejected:** Notifies that the batch was rejected.  **batch.failed:** Notifies that the batch failed - includes the details of the failure (insufficient funds etc)  **batch.completed:** Notifies that the batch completed successfully. Includes a summary.  Push notifications are sent to the firework mobile app for many of these events too - these can be configured from within the app.  This is the first step in creating a batch payment. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createBatchPaymentTest() throws ApiException {
        NewBatch newBatch = null;
        NewBatchResponse response = api.createBatchPayment(newBatch);
        // TODO: test validations
    }

    /**
     * Remove a Payment from the Batch (Bank Transfers)
     *
     * Removes a Payment from the Batch (Bank Transfers). You can only remove payments before the batch is submitted for approval (while it is in the OPEN state).
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteBankTransferBatchPaymentTest() throws ApiException {
        String batchUuid = null;
        String itemUuid = null;
        api.deleteBankTransferBatchPayment(batchUuid, itemUuid);
        // TODO: test validations
    }

    /**
     * Remove a Payment from the Batch (Internal Transfer)
     *
     * Removes a Payment from the Batch (Internal Transfer). You can only remove payments before the batch is submitted for approval (while it is in the OPEN state).
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteInternalTransferBatchPaymentTest() throws ApiException {
        String batchUuid = null;
        String itemUuid = null;
        api.deleteInternalTransferBatchPayment(batchUuid, itemUuid);
        // TODO: test validations
    }

    /**
     * Remove a Payment from the Batch (International Transfers)
     *
     * Removes a Payment from the Batch (International Transfers). You can only remove payments before the batch is submitted for approval (while it is in the OPEN state).
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteInternationalTransferBatchPaymentTest() throws ApiException {
        String batchUuid = null;
        String itemUuid = null;
        api.deleteInternationalTransferBatchPayment(batchUuid, itemUuid);
        // TODO: test validations
    }

    /**
     * List batches
     *
     * Returns the list of batch with the specified types and statuses. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getBatchesTest() throws ApiException {
        String batchStatus = null;
        String batchTypes = null;
        String orderBy = null;
        String order = null;
        BatchItems response = api.getBatches(batchStatus, batchTypes, orderBy, order);
        // TODO: test validations
    }

    /**
     * Get details of a single Batch
     *
     * Returns the details of the batch specified in the API endpoint - {batchUuid}.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDetailsSingleBatchTest() throws ApiException {
        String batchUuid = null;
        Batch response = api.getDetailsSingleBatch(batchUuid);
        // TODO: test validations
    }

    /**
     * List items in a Batch (Bank Transfers)
     *
     * Returns a paginated list of items in the specified batch.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getItemsBatchBankTransferTest() throws ApiException {
        String batchUuid = null;
        Long offset = null;
        Long limit = null;
        BatchItems response = api.getItemsBatchBankTransfer(batchUuid, offset, limit);
        // TODO: test validations
    }

    /**
     * List items in a Batch (Internal Transfers)
     *
     * Returns a paginated list of items in the specified batch.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getItemsBatchInternalTrasnferTest() throws ApiException {
        String batchUuid = null;
        Long offset = null;
        Long limit = null;
        BatchItems response = api.getItemsBatchInternalTrasnfer(batchUuid, offset, limit);
        // TODO: test validations
    }

    /**
     * List items in a Batch (International Transfers)
     *
     * Returns a paginated list of items in the specified batch.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getItemsBatchInternationalTransferTest() throws ApiException {
        String batchUuid = null;
        Long offset = null;
        Long limit = null;
        BatchItems response = api.getItemsBatchInternationalTransfer(batchUuid, offset, limit);
        // TODO: test validations
    }

    /**
     * List Approvers for a Batch
     *
     * Returns a list of approvers for this batch.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getListofApproversForBatchTest() throws ApiException {
        String batchUuid = null;
        BatchApprovers response = api.getListofApproversForBatch(batchUuid);
        // TODO: test validations
    }

    /**
     * Submit a batch for approval
     *
     * Submits the Batch (for approval in the case of a **BANK_TRANSFER** or **INTERNATIONAL_TRANSFER**). If this is an **INTERNAL_TRANSFER** batch, the transfers are immediately queued for processing. If this is a **BANK_TRANSFER** or **INTERNATIONAL_TRANSFER** batch, this will trigger requests for approval to the firework mobile apps of authorised users. Once those users approve the batch, it is queued for processing.  You can only submit a batch while it is in the OPEN state. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void submitBatchTest() throws ApiException {
        String batchUuid = null;
        api.submitBatch(batchUuid);
        // TODO: test validations
    }

}
