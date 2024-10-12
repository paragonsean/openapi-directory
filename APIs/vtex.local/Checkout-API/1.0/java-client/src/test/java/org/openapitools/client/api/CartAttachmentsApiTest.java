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
import org.openapitools.client.model.AddClientPreferencesRequest;
import org.openapitools.client.model.AddClientProfileRequest;
import org.openapitools.client.model.AddMarketingDataRequest;
import org.openapitools.client.model.AddMerchantContextData200Response;
import org.openapitools.client.model.AddMerchantContextDataRequest;
import org.openapitools.client.model.AddPaymentDataRequest;
import org.openapitools.client.model.AddShippingAddressRequest;
import org.openapitools.client.model.GetClientProfileByEmail200Response;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CartAttachmentsApi
 */
@Disabled
public class CartAttachmentsApiTest {

    private final CartAttachmentsApi api = new CartAttachmentsApi();

    /**
     * Add client preferences
     *
     * Use this request to include client preferences information to a given shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addClientPreferencesTest() throws ApiException {
        String contentType = null;
        String accept = null;
        String orderFormId = null;
        AddClientPreferencesRequest addClientPreferencesRequest = null;
        Object response = api.addClientPreferences(contentType, accept, orderFormId, addClientPreferencesRequest);
        // TODO: test validations
    }

    /**
     * Add client profile
     *
     * Use this request to include client profile information to a given shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.    &gt;⚠️ The authentication of this endpoint can change depending on the customer context. If you are modifying information from a customer with a complete profile on the store, the response will return the customer&#39;s data masked. You can only access the customer data with an authenticated request.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addClientProfileTest() throws ApiException {
        String contentType = null;
        String accept = null;
        String orderFormId = null;
        AddClientProfileRequest addClientProfileRequest = null;
        api.addClientProfile(contentType, accept, orderFormId, addClientProfileRequest);
        // TODO: test validations
    }

    /**
     * Add marketing data
     *
     * Use this request to include marketing information to a given shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addMarketingDataTest() throws ApiException {
        String contentType = null;
        String accept = null;
        String orderFormId = null;
        AddMarketingDataRequest addMarketingDataRequest = null;
        api.addMarketingData(contentType, accept, orderFormId, addMarketingDataRequest);
        // TODO: test validations
    }

    /**
     * Add merchant context data
     *
     * This endpoint is used for the merchant to add to the cart any relevant information that is related to the context of a specific order.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addMerchantContextDataTest() throws ApiException {
        String contentType = null;
        String accept = null;
        String orderFormId = null;
        AddMerchantContextDataRequest addMerchantContextDataRequest = null;
        AddMerchantContextData200Response response = api.addMerchantContextData(contentType, accept, orderFormId, addMerchantContextDataRequest);
        // TODO: test validations
    }

    /**
     * Add payment data
     *
     * Use this request to include payment information to a given shopping cart. The payment information attachment in the shopping cart does not determine the final order payment method in itself. However, it allows tha platform to update any relevant information that may be impacted by the payment method.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addPaymentDataTest() throws ApiException {
        String contentType = null;
        String accept = null;
        String orderFormId = null;
        AddPaymentDataRequest addPaymentDataRequest = null;
        api.addPaymentData(contentType, accept, orderFormId, addPaymentDataRequest);
        // TODO: test validations
    }

    /**
     * Add shipping address and select delivery option
     *
     * Use this request to include shipping information and/or selected delivery option to a given shopping cart.    To add shipping addresses send the &#x60;selectedAddresses&#x60; array. For delivery option use the &#x60;logisticsInfo&#x60; array.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.    &gt;⚠️ The authentication of this endpoint can change depending on the customer context. If you are modifying information from a customer with a complete profile on the store, the response will return the customer&#39;s data masked. You can only access the customer data with an authenticated request.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addShippingAddressTest() throws ApiException {
        String contentType = null;
        String accept = null;
        String orderFormId = null;
        AddShippingAddressRequest addShippingAddressRequest = null;
        api.addShippingAddress(contentType, accept, orderFormId, addShippingAddressRequest);
        // TODO: test validations
    }

    /**
     * Get client profile by email
     *
     * Retrieve a client&#39;s profile information by providing an email address.    If the response body fields are empty, the following situations may have occurred:    1. There is no client registered with the email address provided in your store, or;  2. Client profile is invalid or incomplete. For more information, see [SmartCheckout - Customer information automatic fill-in](https://help.vtex.com/en/tutorial/smartcheckout-customer-information-automatic-fill-in--2Nuu3xAFzdhIzJIldAdtan).    &gt;⚠️ The authentication of this endpoint can change depending on the customer context. If you are consulting information from a customer with a complete profile on the store, the response will return the customer&#39;s data masked. You can only access the customer data with an authenticated request.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getClientProfileByEmailTest() throws ApiException {
        String contentType = null;
        String accept = null;
        String email = null;
        GetClientProfileByEmail200Response response = api.getClientProfileByEmail(contentType, accept, email);
        // TODO: test validations
    }

}
