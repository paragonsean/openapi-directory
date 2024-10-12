/*
 * API V1
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
import java.math.BigDecimal;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DefaultApi
 */
@Disabled
public class DefaultApiTest {

    private final DefaultApi api = new DefaultApi();

    /**
     * Calculate shipping carbon offset
     *
     * Calculates the donation amount (to CarbonFund 501\\(c\\)3) needed to offset a physical shipment. This calculation depends on the weight, primary transportation method, and distance of the shipment. Provide the distance of the shipment using the origin and destination address, or directly with the number of miles. For convenience, this endpoint also returns the id of the nonprofit CarbonFund, for making a subsequent donation to. See the [Carbon offsets guide](/recipes/carbon-offsets/) for more on using this endpoint.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV1DonationsCarbonCalculateGetTest() throws ApiException {
        BigDecimal weightLb = null;
        BigDecimal originAddress = null;
        BigDecimal destinationAddress = null;
        BigDecimal distanceMi = null;
        String transportationMethod = null;
        api.apiV1DonationsCarbonCalculateGet(weightLb, originAddress, destinationAddress, distanceMi, transportationMethod);
        // TODO: test validations
    }

    /**
     * Retrieve carbon offset stats
     *
     * Measures your carbon offset impact in relatable terms. Provide the id of a donation to CarbonFund to see stats about that specific donation. If you omit the donation id, this endpoint returns aggregate stats for all of your CarbonFund donations.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV1DonationsCarbonStatsGetTest() throws ApiException {
        BigDecimal id = null;
        api.apiV1DonationsCarbonStatsGet(id);
        // TODO: test validations
    }

    /**
     * Create a donation
     *
     * Creates a donation to any nonprofit. CHANGE keeps track of your donations, bills you at the end of the month, and handles the nonprofit payouts for you.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV1DonationsCreatePostTest() throws ApiException {
        String amount = null;
        String nonprofitId = null;
        String fundingSource = null;
        String zipCode = null;
        api.apiV1DonationsCreatePost(amount, nonprofitId, fundingSource, zipCode);
        // TODO: test validations
    }

    /**
     * Calculate crypto carbon offset
     *
     * Calculates the donation amount (to CarbonFund 501\\(c\\)3) needed to offset a cryptocurrency transaction. For convenience, this endpoint also returns the id of the nonprofit CarbonFund, for making a subsequent donation to. See the [Carbon offsets guide](/recipes/carbon-offsets/) for more on using this endpoint.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV1DonationsCryptoCalculateGetTest() throws ApiException {
        String currency = null;
        BigDecimal count = null;
        api.apiV1DonationsCryptoCalculateGet(currency, count);
        // TODO: test validations
    }

    /**
     * List your donations
     *
     * Retrieves a list of donations you&#39;ve previously made. The donations are returned in order of creation, with the most recent donations appearing first. This endpoint is paginated.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV1DonationsIndexGetTest() throws ApiException {
        BigDecimal page = null;
        api.apiV1DonationsIndexGet(page);
        // TODO: test validations
    }

    /**
     * Retrieve a donation
     *
     * Retrieves the details of a donation you&#39;ve previously made.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV1DonationsShowGetTest() throws ApiException {
        String id = null;
        api.apiV1DonationsShowGet(id);
        // TODO: test validations
    }

    /**
     * Search a nonprofit
     *
     * Retrieves a list of nonprofits whose names match the provided name. This endpoint is paginated.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV1NonprofitsListGetTest() throws ApiException {
        String name = null;
        BigDecimal page = null;
        api.apiV1NonprofitsListGet(name, page);
        // TODO: test validations
    }

    /**
     * Show a nonprofit
     *
     * Retrieves information for a nonprofit.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV1NonprofitsShowGetTest() throws ApiException {
        String id = null;
        api.apiV1NonprofitsShowGet(id);
        // TODO: test validations
    }

}
