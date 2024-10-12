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
import org.openapitools.client.model.AddCoupons200ResponseClientProfileData;
import org.openapitools.client.model.AddCoupons200ResponseItemMetadata;
import org.openapitools.client.model.AddCoupons200ResponsePaymentData;
import org.openapitools.client.model.AddCoupons200ResponseRatesAndBenefitsData;
import org.openapitools.client.model.AddCoupons200ResponseSellersInner;
import org.openapitools.client.model.AddCoupons200ResponseShippingData;
import org.openapitools.client.model.CartSimulation200ResponseLogisticsInfoInnerTotalsInner;
import org.openapitools.client.model.PlaceOrder200ResponseOrdersInnerItemsInner;
import org.openapitools.jackson.nullable.JsonNullable;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for PlaceOrder200ResponseOrdersInner
 */
public class PlaceOrder200ResponseOrdersInnerTest {
    private final PlaceOrder200ResponseOrdersInner model = new PlaceOrder200ResponseOrdersInner();

    /**
     * Model tests for PlaceOrder200ResponseOrdersInner
     */
    @Test
    public void testPlaceOrder200ResponseOrdersInner() {
        // TODO: test PlaceOrder200ResponseOrdersInner
    }

    /**
     * Test the property 'allowCancelation'
     */
    @Test
    public void allowCancelationTest() {
        // TODO: test allowCancelation
    }

    /**
     * Test the property 'allowChangeSeller'
     */
    @Test
    public void allowChangeSellerTest() {
        // TODO: test allowChangeSeller
    }

    /**
     * Test the property 'allowEdition'
     */
    @Test
    public void allowEditionTest() {
        // TODO: test allowEdition
    }

    /**
     * Test the property 'checkedInPickupPointId'
     */
    @Test
    public void checkedInPickupPointIdTest() {
        // TODO: test checkedInPickupPointId
    }

    /**
     * Test the property 'clientProfileData'
     */
    @Test
    public void clientProfileDataTest() {
        // TODO: test clientProfileData
    }

    /**
     * Test the property 'creationDate'
     */
    @Test
    public void creationDateTest() {
        // TODO: test creationDate
    }

    /**
     * Test the property 'followUpEmail'
     */
    @Test
    public void followUpEmailTest() {
        // TODO: test followUpEmail
    }

    /**
     * Test the property 'hostName'
     */
    @Test
    public void hostNameTest() {
        // TODO: test hostName
    }

    /**
     * Test the property 'isCheckedIn'
     */
    @Test
    public void isCheckedInTest() {
        // TODO: test isCheckedIn
    }

    /**
     * Test the property 'isCompleted'
     */
    @Test
    public void isCompletedTest() {
        // TODO: test isCompleted
    }

    /**
     * Test the property 'isUserDataVisible'
     */
    @Test
    public void isUserDataVisibleTest() {
        // TODO: test isUserDataVisible
    }

    /**
     * Test the property 'itemMetadata'
     */
    @Test
    public void itemMetadataTest() {
        // TODO: test itemMetadata
    }

    /**
     * Test the property 'items'
     */
    @Test
    public void itemsTest() {
        // TODO: test items
    }

    /**
     * Test the property 'lastChange'
     */
    @Test
    public void lastChangeTest() {
        // TODO: test lastChange
    }

    /**
     * Test the property 'merchantName'
     */
    @Test
    public void merchantNameTest() {
        // TODO: test merchantName
    }

    /**
     * Test the property 'orderFormCreationDate'
     */
    @Test
    public void orderFormCreationDateTest() {
        // TODO: test orderFormCreationDate
    }

    /**
     * Test the property 'orderGroup'
     */
    @Test
    public void orderGroupTest() {
        // TODO: test orderGroup
    }

    /**
     * Test the property 'orderId'
     */
    @Test
    public void orderIdTest() {
        // TODO: test orderId
    }

    /**
     * Test the property 'paymentData'
     */
    @Test
    public void paymentDataTest() {
        // TODO: test paymentData
    }

    /**
     * Test the property 'ratesAndBenefitsData'
     */
    @Test
    public void ratesAndBenefitsDataTest() {
        // TODO: test ratesAndBenefitsData
    }

    /**
     * Test the property 'roundingError'
     */
    @Test
    public void roundingErrorTest() {
        // TODO: test roundingError
    }

    /**
     * Test the property 'salesAssociateId'
     */
    @Test
    public void salesAssociateIdTest() {
        // TODO: test salesAssociateId
    }

    /**
     * Test the property 'salesChannel'
     */
    @Test
    public void salesChannelTest() {
        // TODO: test salesChannel
    }

    /**
     * Test the property 'sellerOrderId'
     */
    @Test
    public void sellerOrderIdTest() {
        // TODO: test sellerOrderId
    }

    /**
     * Test the property 'sellers'
     */
    @Test
    public void sellersTest() {
        // TODO: test sellers
    }

    /**
     * Test the property 'shippingData'
     */
    @Test
    public void shippingDataTest() {
        // TODO: test shippingData
    }

    /**
     * Test the property 'state'
     */
    @Test
    public void stateTest() {
        // TODO: test state
    }

    /**
     * Test the property 'storeId'
     */
    @Test
    public void storeIdTest() {
        // TODO: test storeId
    }

    /**
     * Test the property 'timeZoneCreationDate'
     */
    @Test
    public void timeZoneCreationDateTest() {
        // TODO: test timeZoneCreationDate
    }

    /**
     * Test the property 'timeZoneLastChange'
     */
    @Test
    public void timeZoneLastChangeTest() {
        // TODO: test timeZoneLastChange
    }

    /**
     * Test the property 'totals'
     */
    @Test
    public void totalsTest() {
        // TODO: test totals
    }

    /**
     * Test the property 'userType'
     */
    @Test
    public void userTypeTest() {
        // TODO: test userType
    }

    /**
     * Test the property 'value'
     */
    @Test
    public void valueTest() {
        // TODO: test value
    }

}
