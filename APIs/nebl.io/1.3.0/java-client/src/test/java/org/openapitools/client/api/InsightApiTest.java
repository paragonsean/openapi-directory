/*
 * Neblio REST API Suite
 * APIs for Interacting with NTP1 Tokens & The Neblio Blockchain
 *
 * The version of the OpenAPI document: 1.3.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import java.math.BigDecimal;
import org.openapitools.client.model.BroadcastTxResponse;
import org.openapitools.client.model.Error;
import org.openapitools.client.model.GetAddressResponse;
import org.openapitools.client.model.GetAddressUtxosResponseInner;
import org.openapitools.client.model.GetBlockIndexResponse;
import org.openapitools.client.model.GetBlockResponse;
import org.openapitools.client.model.GetRawTxResponse;
import org.openapitools.client.model.GetSyncResponse;
import org.openapitools.client.model.GetTxResponse;
import org.openapitools.client.model.GetTxsResponse;
import org.openapitools.client.model.SendTxRequest;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for InsightApi
 */
@Disabled
public class InsightApiTest {

    private final InsightApi api = new InsightApi();

    /**
     * Returns address object
     *
     * Returns NEBL address object containing information on a specific address
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAddressTest() throws ApiException {
        String address = null;
        GetAddressResponse response = api.getAddress(address);
        // TODO: test validations
    }

    /**
     * Returns address balance in sats
     *
     * Returns NEBL address balance in satoshis
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAddressBalanceTest() throws ApiException {
        String address = null;
        BigDecimal response = api.getAddressBalance(address);
        // TODO: test validations
    }

    /**
     * Returns total received by address in sats
     *
     * Returns total NEBL received by address in satoshis
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAddressTotalReceivedTest() throws ApiException {
        String address = null;
        BigDecimal response = api.getAddressTotalReceived(address);
        // TODO: test validations
    }

    /**
     * Returns total sent by address in sats
     *
     * Returns total NEBL sent by address in satoshis
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAddressTotalSentTest() throws ApiException {
        String address = null;
        BigDecimal response = api.getAddressTotalSent(address);
        // TODO: test validations
    }

    /**
     * Returns address unconfirmed balance in sats
     *
     * Returns NEBL address unconfirmed balance in satoshis
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAddressUnconfirmedBalanceTest() throws ApiException {
        String address = null;
        BigDecimal response = api.getAddressUnconfirmedBalance(address);
        // TODO: test validations
    }

    /**
     * Returns all UTXOs at a given address
     *
     * Returns information on each Unspent Transaction Output contained at an address
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAddressUtxosTest() throws ApiException {
        String address = null;
        List<GetAddressUtxosResponseInner> response = api.getAddressUtxos(address);
        // TODO: test validations
    }

    /**
     * Returns information regarding a Neblio block
     *
     * Returns blockchain data for a given block based upon the block hash
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getBlockTest() throws ApiException {
        String blockhash = null;
        GetBlockResponse response = api.getBlock(blockhash);
        // TODO: test validations
    }

    /**
     * Returns block hash of block
     *
     * Returns the block hash of a block at a given block index
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getBlockIndexTest() throws ApiException {
        BigDecimal blockindex = null;
        GetBlockIndexResponse response = api.getBlockIndex(blockindex);
        // TODO: test validations
    }

    /**
     * Returns raw transaction hex
     *
     * Returns raw transaction hex representing a NEBL transaction
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getRawTxTest() throws ApiException {
        String txid = null;
        GetRawTxResponse response = api.getRawTx(txid);
        // TODO: test validations
    }

    /**
     * Utility API for calling several blockchain node functions
     *
     * Utility API for calling several blockchain node functions - getInfo, getDifficulty, getBestBlockHash, getLastBlockHash
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getStatusTest() throws ApiException {
        String q = null;
        Object response = api.getStatus(q);
        // TODO: test validations
    }

    /**
     * Get node sync status
     *
     * Returns information on the node&#39;s sync progress
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getSyncTest() throws ApiException {
        GetSyncResponse response = api.getSync();
        // TODO: test validations
    }

    /**
     * Returns transaction object
     *
     * Returns NEBL transaction object representing a NEBL transaction
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTxTest() throws ApiException {
        String txid = null;
        GetTxResponse response = api.getTx(txid);
        // TODO: test validations
    }

    /**
     * Get transactions by block or address
     *
     * Returns all transactions by block or address
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTxsTest() throws ApiException {
        String address = null;
        String block = null;
        BigDecimal pageNum = null;
        GetTxsResponse response = api.getTxs(address, block, pageNum);
        // TODO: test validations
    }

    /**
     * Broadcasts a signed raw transaction to the network (not NTP1 specific)
     *
     * Broadcasts a signed raw transaction to the network. If successful returns the txid of the broadcast trasnaction. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void sendTxTest() throws ApiException {
        SendTxRequest sendTxRequest = null;
        BroadcastTxResponse response = api.sendTx(sendTxRequest);
        // TODO: test validations
    }

}
