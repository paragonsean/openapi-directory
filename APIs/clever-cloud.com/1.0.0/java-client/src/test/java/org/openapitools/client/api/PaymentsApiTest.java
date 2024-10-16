/*
 * Clever-Cloud API
 * Public API for managing Clever-Cloud data and products
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.Body;
import org.openapitools.client.model.PaymentData;
import org.openapitools.client.model.PaymentProvider;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for PaymentsApi
 */
@Disabled
public class PaymentsApiTest {

    private final PaymentsApi api = new PaymentsApi();

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteOrganisationsIdPaymentsBillingsBid_1Test() throws ApiException {
        String id = null;
        String bid = null;
        api.deleteOrganisationsIdPaymentsBillingsBid_1(id, bid);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteOrganisationsIdPaymentsRecurring_1Test() throws ApiException {
        String id = null;
        api.deleteOrganisationsIdPaymentsRecurring_1(id);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteSelfPaymentsBillingsBid_0Test() throws ApiException {
        String bid = null;
        api.deleteSelfPaymentsBillingsBid_0(bid);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteSelfPaymentsMethodsMId_0Test() throws ApiException {
        String mId = null;
        api.deleteSelfPaymentsMethodsMId_0(mId);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteSelfPaymentsRecurring_0Test() throws ApiException {
        api.deleteSelfPaymentsRecurring_0();
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganisationsIdPaymentsBillingsBidPdf_1Test() throws ApiException {
        String id = null;
        String bid = null;
        String token = null;
        api.getOrganisationsIdPaymentsBillingsBidPdf_1(id, bid, token);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganisationsIdPaymentsBillingsBid_1Test() throws ApiException {
        String id = null;
        String bid = null;
        api.getOrganisationsIdPaymentsBillingsBid_1(id, bid);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganisationsIdPaymentsBillings_1Test() throws ApiException {
        String id = null;
        api.getOrganisationsIdPaymentsBillings_1(id);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOrganisationsIdPaymentsFullPricePrice_1Test() throws ApiException {
        String id = null;
        String price = null;
        api.getOrganisationsIdPaymentsFullPricePrice_1(id, price);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPaymentsCouponsName_0Test() throws ApiException {
        String name = null;
        api.getPaymentsCouponsName_0(name);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPaymentsProviders_0Test() throws ApiException {
        List<PaymentProvider> response = api.getPaymentsProviders_0();
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPaymentsTokensStripe_0Test() throws ApiException {
        api.getPaymentsTokensStripe_0();
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getSelfPaymentsBillingsBidPdf_0Test() throws ApiException {
        String bid = null;
        String token = null;
        api.getSelfPaymentsBillingsBidPdf_0(bid, token);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getSelfPaymentsBillingsBid_0Test() throws ApiException {
        String bid = null;
        api.getSelfPaymentsBillingsBid_0(bid);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getSelfPaymentsBillings_0Test() throws ApiException {
        api.getSelfPaymentsBillings_0();
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getSelfPaymentsFullpricePrice_0Test() throws ApiException {
        String price = null;
        api.getSelfPaymentsFullpricePrice_0(price);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getSelfPaymentsMethods_0Test() throws ApiException {
        api.getSelfPaymentsMethods_0();
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void organisationsIdPaymentsBillingsUnpaidGet_1Test() throws ApiException {
        String id = null;
        api.organisationsIdPaymentsBillingsUnpaidGet_1(id);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void organisationsIdPaymentsMethodsDefaultGet_1Test() throws ApiException {
        String id = null;
        api.organisationsIdPaymentsMethodsDefaultGet_1(id);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void organisationsIdPaymentsMethodsDefaultPut_1Test() throws ApiException {
        String id = null;
        PaymentData paymentData = null;
        api.organisationsIdPaymentsMethodsDefaultPut_1(id, paymentData);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void organisationsIdPaymentsMethodsGet_1Test() throws ApiException {
        String id = null;
        api.organisationsIdPaymentsMethodsGet_1(id);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void organisationsIdPaymentsMethodsMIdDelete_1Test() throws ApiException {
        String mId = null;
        String id = null;
        api.organisationsIdPaymentsMethodsMIdDelete_1(mId, id);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void organisationsIdPaymentsMethodsPost_1Test() throws ApiException {
        String id = null;
        Body body = null;
        api.organisationsIdPaymentsMethodsPost_1(id, body);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void organisationsIdPaymentsMonthlyinvoiceGet_1Test() throws ApiException {
        String id = null;
        api.organisationsIdPaymentsMonthlyinvoiceGet_1(id);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_1Test() throws ApiException {
        String id = null;
        api.organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_1(id);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void organisationsIdPaymentsRecurringGet_1Test() throws ApiException {
        String id = null;
        api.organisationsIdPaymentsRecurringGet_1(id);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void paymentsAssetsPayButtonTokenButtonPngGet_0Test() throws ApiException {
        String token = null;
        api.paymentsAssetsPayButtonTokenButtonPngGet_0(token);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void paymentsBidEndStripePost_0Test() throws ApiException {
        String bid = null;
        api.paymentsBidEndStripePost_0(bid);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postOrganisationsIdPaymentsBillings_1Test() throws ApiException {
        String id = null;
        api.postOrganisationsIdPaymentsBillings_1(id);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postSelfPaymentsBillings_0Test() throws ApiException {
        api.postSelfPaymentsBillings_0();
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postSelfPaymentsMethods_0Test() throws ApiException {
        api.postSelfPaymentsMethods_0();
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putOrganisationsIdPaymentsBillingsBid_1Test() throws ApiException {
        String id = null;
        String bid = null;
        api.putOrganisationsIdPaymentsBillingsBid_1(id, bid);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putSelfPaymentsBillingsBid_0Test() throws ApiException {
        String bid = null;
        api.putSelfPaymentsBillingsBid_0(bid);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void selfPaymentsMethodsDefaultGet_0Test() throws ApiException {
        api.selfPaymentsMethodsDefaultGet_0();
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void selfPaymentsMethodsDefaultPut_0Test() throws ApiException {
        api.selfPaymentsMethodsDefaultPut_0();
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void selfPaymentsMonthlyinvoiceGet_0Test() throws ApiException {
        api.selfPaymentsMonthlyinvoiceGet_0();
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void selfPaymentsMonthlyinvoiceMaxcreditPut_0Test() throws ApiException {
        api.selfPaymentsMonthlyinvoiceMaxcreditPut_0();
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void selfPaymentsRecurringGet_0Test() throws ApiException {
        api.selfPaymentsRecurringGet_0();
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void selfPaymentsTokensStripeGet_0Test() throws ApiException {
        api.selfPaymentsTokensStripeGet_0();
        // TODO: test validations
    }

}
