/*
 * VAT API
 * A developer friendly API to help your business achieve VAT compliance
 *
 * The version of the OpenAPI document: 1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ApiUsage;
import org.openapitools.client.model.ConvertPrice;
import org.openapitools.client.model.CountryCodeCheck;
import org.openapitools.client.model.CreateInvoice;
import org.openapitools.client.model.CurrencyConversion;
import org.openapitools.client.model.IPCheck;
import org.openapitools.client.model.InvoiceData;
import org.openapitools.client.model.RetrieveInvoice;
import org.openapitools.client.model.UpdateInvoice;
import org.openapitools.client.model.UpdateInvoiceArray;
import org.openapitools.client.model.VatRates;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ApiApi
 */
@Disabled
public class ApiApiTest {

    private final ApiApi api = new ApiApi();

    /**
     * Check api requests remaining on current subscription plan
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiUsageTest() throws ApiException {
        String responseType = null;
        ApiUsage response = api.apiUsage(responseType);
        // TODO: test validations
    }

    /**
     * Convert a price to or from VAT price.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void convertPriceTest() throws ApiException {
        String code = null;
        Integer price = null;
        String responseType = null;
        String countryRate = null;
        String type = null;
        ConvertPrice response = api.convertPrice(code, price, responseType, countryRate, type);
        // TODO: test validations
    }

    /**
     * Retrieve a countries VAT rates by its 2 digit country code
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void countryCodeCheckTest() throws ApiException {
        String code = null;
        String responseType = null;
        CountryCodeCheck response = api.countryCodeCheck(code, responseType);
        // TODO: test validations
    }

    /**
     * Create a VAT invoice
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createInvoiceTest() throws ApiException {
        InvoiceData body = null;
        String responseType = null;
        CreateInvoice response = api.createInvoice(body, responseType);
        // TODO: test validations
    }

    /**
     * Convert a currency
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void currencyConversionTest() throws ApiException {
        String currencyFrom = null;
        String currencyTo = null;
        String responseType = null;
        Integer amount = null;
        CurrencyConversion response = api.currencyConversion(currencyFrom, currencyTo, responseType, amount);
        // TODO: test validations
    }

    /**
     * Retrieve an invoice
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getInvoiceTest() throws ApiException {
        Integer id = null;
        String responseType = null;
        RetrieveInvoice response = api.getInvoice(id, responseType);
        // TODO: test validations
    }

    /**
     * Delete an invoice
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void invoiceDeleteTest() throws ApiException {
        Integer id = null;
        String responseType = null;
        api.invoiceDelete(id, responseType);
        // TODO: test validations
    }

    /**
     * Update an existing invoice
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void invoiceUpdateTest() throws ApiException {
        Integer id = null;
        UpdateInvoiceArray body = null;
        String responseType = null;
        UpdateInvoice response = api.invoiceUpdate(id, body, responseType);
        // TODO: test validations
    }

    /**
     * Retrieve a countries VAT rates from an IP address
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void ipCheckTest() throws ApiException {
        String address = null;
        String responseType = null;
        IPCheck response = api.ipCheck(address, responseType);
        // TODO: test validations
    }

    /**
     * Validate a VAT number
     *
     * &lt;p&gt;We highly recommend if you are able, to check a VAT number on your end first to save wasted API lookups. It maybe that your customer has simply entered the wrong format. &lt;a href&#x3D;&#39;http://www.braemoor.co.uk/software/vat.shtml&#39; target&#x3D;&#39;_blank&#39;&gt;Heres a client side way to check the format using Javascript&lt;/a&gt;&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void vatNumberValidateTest() throws ApiException {
        String vatid = null;
        String responseType = null;
        api.vatNumberValidate(vatid, responseType);
        // TODO: test validations
    }

    /**
     * Retrieve all current EU VAT rates
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void vatRatesTest() throws ApiException {
        String responseType = null;
        VatRates response = api.vatRates(responseType);
        // TODO: test validations
    }

}
