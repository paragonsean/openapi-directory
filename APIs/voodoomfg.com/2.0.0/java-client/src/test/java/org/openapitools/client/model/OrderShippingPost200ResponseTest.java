/*
 * Voodoo Manufacturing 3D Print API
 * Welcome to the Voodoo Manufacturing API docs!  Your Voodoo Manufacturing API key must be included with each request to the API. The API will look for the key in the \"api_key\" header of the request. <a href=\"https://voodoomfg.com/3d-print-api#get-access\" target=\"_blank\">You can request a key here.</a>  This API provides a programmatic interface for submitting printing orders to Voodoo Manufacturing. The general process for creating an order is as follows:   - Get a list of the available materials with the /materials endpoint   - Upload models to the API with the /models endpoint   - Get quotes for shipping methods with the /order/shipping endpoint   - Get a quote for an order with the /order/create endpoint   - Confirm the order with the /order/confirm endpoint  Uploaded models and orders can be retrieved either in bulk or by id at the /model and /order endpoints, respectively.  In some cases, you may wish to get a quote for a specific model without the context of an order. In this case, you may use the /model/quote (if you've already uploaded the model to the API) or the /model/quote_attrs (lets you quote based on calculated model attributes) endpoints. 
 *
 * The version of the OpenAPI document: 2.0.0
 * Contact: support@voodoomfg.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.Rate;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for OrderShippingPost200Response
 */
public class OrderShippingPost200ResponseTest {
    private final OrderShippingPost200Response model = new OrderShippingPost200Response();

    /**
     * Model tests for OrderShippingPost200Response
     */
    @Test
    public void testOrderShippingPost200Response() {
        // TODO: test OrderShippingPost200Response
    }

    /**
     * Test the property 'rates'
     */
    @Test
    public void ratesTest() {
        // TODO: test rates
    }

}
