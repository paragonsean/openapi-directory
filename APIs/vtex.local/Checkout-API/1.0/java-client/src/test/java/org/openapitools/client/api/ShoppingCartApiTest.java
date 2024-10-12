/*
 * Checkout API
 * >ℹ️ Check the new [Checkout onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/checkout-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about the Checkout and is organized by focusing on the developer's journey.    The Checkout API allows you to obtain and configure information about the shopping cart and its attachments, personalization of custom fields, orderForm structure, fulfillment data, order management, and identification of the sellers delivery region.    >ℹ️ Data modification operations (`POST`, `PATCH`, `PUT` or `DELETE` endpoints) shall not be performed in parallel in the Checkout APIs. They need to be enqueued by the client/requester. Otherwise, old values ​​can be overwritten incorrectly or competition errors may occur.    >⚠️ All endpoints that consult or edit the orderForm can change the authentication depending on the customer context. If you are handling information from a customer with a complete profile on the store, authentication will be required. You can only access or modify the customer data for these profiles with an authenticated request.    ## Shopping cart    Allows merchants to simulate, configure and customize shopping cart information.    - [POST - Cart Simulation](https://developers.vtex.com/vtex-rest-api/reference/cartsimulation)  - [GET - Get current or create a new cart](https://developers.vtex.com/vtex-rest-api/reference/createanewcart)  - [GET - Get cart information by ID](https://developers.vtex.com/vtex-rest-api/reference/getcartinformationbyid)  - [POST - Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems)  - [GET - Remove all personal data](https://developers.vtex.com/vtex-rest-api/reference/removeallpersonaldata)  - [POST - Update cart items](https://developers.vtex.com/vtex-rest-api/reference/itemsupdate)  - [POST - Add cart items](https://developers.vtex.com/vtex-rest-api/reference/items)  - [PUT - Change price](https://developers.vtex.com/vtex-rest-api/reference/pricechange)  - [PATCH - Ignore profile data](https://developers.vtex.com/vtex-rest-api/reference/ignoreprofiledata)  - [GET - Cart installments](https://developers.vtex.com/vtex-rest-api/reference/getcartinstallments)  - [POST - Add coupons to the cart](https://developers.vtex.com/vtex-rest-api/reference/addcoupons)      ## Cart attachments    Allows merchants to obtain client profiles and add information to a given shopping cart.    - [GET - Get client profile by email](https://developers.vtex.com/vtex-rest-api/reference/getclientprofilebyemail)  - [POST - Add client profile](https://developers.vtex.com/vtex-rest-api/reference/addclientprofile)  - [POST - Add shipping address and select delivery option](https://developers.vtex.com/vtex-rest-api/reference/addshippingaddress)  - [POST - Add client preferences](https://developers.vtex.com/vtex-rest-api/reference/addclientpreferences)  - [POST - Add marketing data](https://developers.vtex.com/vtex-rest-api/reference/addmarketingdata)  - [POST - Add payment data](https://developers.vtex.com/vtex-rest-api/reference/addpaymentdata)  - [POST - Add merchant context data](https://developers.vtex.com/vtex-rest-api/reference/addmerchantcontextdata)      ## Custom data    Allows merchants to manage custom fields that were created by an app in their account.    - [PUT - Set multiple custom field values](https://developers.vtex.com/vtex-rest-api/reference/setmultiplecustomfieldvalues)  - [PUT - Set single custom field value](https://developers.vtex.com/vtex-rest-api/reference/setsinglecustomfieldvalue)  - [DELETE - Remove single custom field value](https://developers.vtex.com/vtex-rest-api/reference/removesinglecustomfieldvalue)      ## Configuration    Allows merchants to configure orderForm in the account and seller exchange on a given order.    - [GET - Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration)  - [POST - Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration)  - [GET - Get window to change seller](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller)  - [POST - Update window to change seller](https://developers.vtex.com/vtex-rest-api/reference/updatewindowtochangeseller)  - [POST - Clear orderForm messages](https://developers.vtex.com/vtex-rest-api/reference/clearorderformmessages)      ## Fulfillment    Allows merchants to obtain pickup points and address information.    - [GET - List pickup points by location](https://developers.vtex.com/vtex-rest-api/reference/listpickupppointsbylocation)  - [GET - Get address by postal code](https://developers.vtex.com/vtex-rest-api/reference/getaddressbypostalcode)      ## Order placement    Allows merchants to place and process orders by creating a new cart or using an existing cart.    - [POST - Place order from an existing cart](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)  - [PUT - Place order](https://developers.vtex.com/vtex-rest-api/reference/placeorder)  - [POST - Process order](https://developers.vtex.com/vtex-rest-api/reference/processorder)      ## Region    Allows merchants to obtain a list of sellers serving a specific delivery region.    - [GET - Get sellers by region or address](https://developers.vtex.com/vtex-rest-api/reference/getsellersbyregion)
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.AddCoupons200Response;
import org.openapitools.client.model.AddCouponsRequest;
import org.openapitools.client.model.CartSimulation200Response;
import org.openapitools.client.model.CartSimulationRequest;
import org.openapitools.client.model.IgnoreProfileDataRequest;
import org.openapitools.client.model.Items200Response;
import org.openapitools.client.model.ItemsRequest;
import org.openapitools.client.model.ItemsUpdate200Response;
import org.openapitools.client.model.ItemsUpdateRequest;
import org.openapitools.client.model.PriceChangeRequest;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ShoppingCartApi
 */
@Disabled
public class ShoppingCartApiTest {

    private final ShoppingCartApi api = new ShoppingCartApi();

    /**
     * Add coupons to the cart
     *
     * Use this request to add coupons to a given shopping cart.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addCouponsTest() throws ApiException {
        String orderFormId = null;
        String contentType = null;
        String accept = null;
        AddCouponsRequest addCouponsRequest = null;
        AddCoupons200Response response = api.addCoupons(orderFormId, contentType, accept, addCouponsRequest);
        // TODO: test validations
    }

    /**
     * Cart simulation
     *
     * This endpoint is used to simulate a cart in VTEX Checkout.    It receives an **SKU ID**, the **quantity** of items in the cart and the ID of the **Seller**.    It sends back all information about the cart, such as the selling price of each item, rates and benefits data, payment and logistics info.    This is useful whenever you need to know the availability of fulfilling an order for a specific cart setting, since the API response will let you know the updated price, inventory and shipping data.    **Important**: The fields (&#x60;sku id&#x60;, &#x60;quantity&#x60;, &#x60;seller&#x60;, &#x60;country&#x60;, &#x60;postalCode&#x60; and &#x60;geoCoordinates&#x60;) are just examples of content that you can simulate in your cart. You can add more fields to the request as per your need. Access the [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) guide to check the available fields.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void cartSimulationTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer rnbBehavior = null;
        Integer sc = null;
        CartSimulationRequest cartSimulationRequest = null;
        CartSimulation200Response response = api.cartSimulation(contentType, accept, rnbBehavior, sc, cartSimulationRequest);
        // TODO: test validations
    }

    /**
     * Get current or create a new cart
     *
     * You can use this request to get your current shopping cart information (&#x60;orderFormId&#x60;) or to create a new cart.    **Important**: To create a new empty shopping cart you need to send this request with the query param &#x60;forceNewCart&#x3D;true&#x60;.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; obtained in response is the identification code of the newly created cart.    &gt; This request has a time out of 45 seconds.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createANewCartTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Boolean forceNewCart = null;
        api.createANewCart(contentType, accept, forceNewCart);
        // TODO: test validations
    }

    /**
     * Get cart information by ID
     *
     * Use this request to get all information associated to a given shopping  cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 45 seconds.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getCartInformationByIdTest() throws ApiException {
        String orderFormId = null;
        String contentType = null;
        String accept = null;
        Boolean refreshOutdatedData = null;
        api.getCartInformationById(orderFormId, contentType, accept, refreshOutdatedData);
        // TODO: test validations
    }

    /**
     * Cart installments
     *
     * Retrieves possible amount of installments and respective values for a given cart with a given payment method.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    This endpoint can be used to get the installment options for only one payment method at a time.    This endpoint should be called only after the selected &#x60;orderForm&#x60; already has a &#x60;paymentData&#x60;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getCartInstallmentsTest() throws ApiException {
        String orderFormId = null;
        Integer paymentSystem = null;
        String contentType = null;
        String accept = null;
        api.getCartInstallments(orderFormId, paymentSystem, contentType, accept);
        // TODO: test validations
    }

    /**
     * Ignore profile data
     *
     * When a shopper provides an email address at Checkout, the platform tries to retrieve existing profile information for that email and add it to the shopping cart information. Use this request if you want to change this behavior for a given cart, meaning profile information will not be included in the order automattically.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    Note that this request will only work if you have not sent the &#x60;clientProfileData&#x60; to the cart yet. Sending it to a cart that already has a &#x60;clientProfileData&#x60; should return a status &#x60;403 Forbidden&#x60; error, with an &#x60;Access denied&#x60; message.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void ignoreProfileDataTest() throws ApiException {
        String orderFormId = null;
        String contentType = null;
        String accept = null;
        IgnoreProfileDataRequest ignoreProfileDataRequest = null;
        api.ignoreProfileData(orderFormId, contentType, accept, ignoreProfileDataRequest);
        // TODO: test validations
    }

    /**
     * Add cart items
     *
     * Use this request to add a new item to the shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 45 seconds.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void itemsTest() throws ApiException {
        String contentType = null;
        String accept = null;
        String orderFormId = null;
        ItemsRequest itemsRequest = null;
        List<Object> allowedOutdatedData = null;
        Items200Response response = api.items(contentType, accept, orderFormId, itemsRequest, allowedOutdatedData);
        // TODO: test validations
    }

    /**
     * Update cart items
     *
     * You can use this request to:    1. Change the quantity of one or more items in a specific cart.  2. Remove an item from the cart (by sending the &#x60;quantity&#x60; value &#x3D; &#x60;0&#x60; in the request body).    **Important**: To remove all items from the cart at the same time, use the [Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems) endpoint.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure that represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 45 seconds.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void itemsUpdateTest() throws ApiException {
        String contentType = null;
        String accept = null;
        String orderFormId = null;
        ItemsUpdateRequest itemsUpdateRequest = null;
        List<Object> allowedOutdatedData = null;
        ItemsUpdate200Response response = api.itemsUpdate(contentType, accept, orderFormId, itemsUpdateRequest, allowedOutdatedData);
        // TODO: test validations
    }

    /**
     * Change price
     *
     * This request changes the price of an SKU in a cart. You can also perform type of bulk price change with the [Update cart items request](https://developers.vtex.com/vtex-rest-api/reference/shopping-cart#itemsupdate)    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    You need to inform which cart you are referring to, by sending its &#x60;orderFormId&#x60;; and what is the item whose price you want to change, by sending its &#x60;itemIndex&#x60;.    You also need to pass the new price value in the body.    Remember that, to use this endpoint, the feature of *manual price* must be active. To check if it&#39;s active, use the [Get orderForm configuration](https://developers.vtex.com/reference#getorderformconfiguration) endpoint. To make it active, use the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) endpoint, making the &#x60;allowManualPrice&#x60; field &#x60;true&#x60;.    &gt; Whenever you use this request to change the price of an item, all items in that cart with the same SKU are affected by this change. This applies even to items that share the SKU but have been separated into different objects in the &#x60;items&#x60; array due to customizations or attachments, for example.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void priceChangeTest() throws ApiException {
        String orderFormId = null;
        String itemIndex = null;
        String contentType = null;
        String accept = null;
        PriceChangeRequest priceChangeRequest = null;
        api.priceChange(orderFormId, itemIndex, contentType, accept, priceChangeRequest);
        // TODO: test validations
    }

    /**
     * Remove all items
     *
     * This request removes all items from a given cart, leaving it empty.    You must send an empty JSON in the body of the request.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    **Important**: **Request Body** must always be sent with empty value \&quot;{ }\&quot; in this endpoint.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void removeAllItemsTest() throws ApiException {
        String orderFormId = null;
        String contentType = null;
        String accept = null;
        Object body = null;
        Object response = api.removeAllItems(orderFormId, contentType, accept, body);
        // TODO: test validations
    }

    /**
     * Remove all personal data
     *
     * This call removes all user information, making a cart anonymous while leaving the items.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure that represents a shopping cart and contains all information about it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    This call works by creating a new orderForm, setting a new cookie, and returning a redirect 302 to the cart URL (&#x60;/checkout/#/orderform&#x60;).
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void removeallpersonaldataTest() throws ApiException {
        String contentType = null;
        String accept = null;
        String orderFormId = null;
        Object response = api.removeallpersonaldata(contentType, accept, orderFormId);
        // TODO: test validations
    }

}
