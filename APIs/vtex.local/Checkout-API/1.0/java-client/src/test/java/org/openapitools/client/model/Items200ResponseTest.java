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
import org.openapitools.client.model.AddCoupons200ResponseAvailableAddressesInner;
import org.openapitools.client.model.AddCoupons200ResponseClientProfileData;
import org.openapitools.client.model.AddCoupons200ResponseItemMetadata;
import org.openapitools.client.model.AddCoupons200ResponseItemsOrdination;
import org.openapitools.client.model.AddCoupons200ResponsePaymentData;
import org.openapitools.client.model.AddCoupons200ResponseRatesAndBenefitsData;
import org.openapitools.client.model.AddCoupons200ResponseSellersInner;
import org.openapitools.client.model.AddCoupons200ResponseShippingData;
import org.openapitools.client.model.Items200ResponseClientPreferencesData;
import org.openapitools.client.model.Items200ResponseItemsInner;
import org.openapitools.client.model.Items200ResponseMarketingData;
import org.openapitools.jackson.nullable.JsonNullable;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for Items200Response
 */
public class Items200ResponseTest {
    private final Items200Response model = new Items200Response();

    /**
     * Model tests for Items200Response
     */
    @Test
    public void testItems200Response() {
        // TODO: test Items200Response
    }

    /**
     * Test the property 'allowManualPrice'
     */
    @Test
    public void allowManualPriceTest() {
        // TODO: test allowManualPrice
    }

    /**
     * Test the property 'availableAccounts'
     */
    @Test
    public void availableAccountsTest() {
        // TODO: test availableAccounts
    }

    /**
     * Test the property 'availableAddresses'
     */
    @Test
    public void availableAddressesTest() {
        // TODO: test availableAddresses
    }

    /**
     * Test the property 'canEditData'
     */
    @Test
    public void canEditDataTest() {
        // TODO: test canEditData
    }

    /**
     * Test the property 'clientPreferencesData'
     */
    @Test
    public void clientPreferencesDataTest() {
        // TODO: test clientPreferencesData
    }

    /**
     * Test the property 'clientProfileData'
     */
    @Test
    public void clientProfileDataTest() {
        // TODO: test clientProfileData
    }

    /**
     * Test the property 'commercialConditionData'
     */
    @Test
    public void commercialConditionDataTest() {
        // TODO: test commercialConditionData
    }

    /**
     * Test the property 'customData'
     */
    @Test
    public void customDataTest() {
        // TODO: test customData
    }

    /**
     * Test the property 'giftRegistryData'
     */
    @Test
    public void giftRegistryDataTest() {
        // TODO: test giftRegistryData
    }

    /**
     * Test the property 'hooksData'
     */
    @Test
    public void hooksDataTest() {
        // TODO: test hooksData
    }

    /**
     * Test the property 'ignoreProfileData'
     */
    @Test
    public void ignoreProfileDataTest() {
        // TODO: test ignoreProfileData
    }

    /**
     * Test the property 'invoiceData'
     */
    @Test
    public void invoiceDataTest() {
        // TODO: test invoiceData
    }

    /**
     * Test the property 'isCheckedIn'
     */
    @Test
    public void isCheckedInTest() {
        // TODO: test isCheckedIn
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
     * Test the property 'itemsOrdination'
     */
    @Test
    public void itemsOrdinationTest() {
        // TODO: test itemsOrdination
    }

    /**
     * Test the property 'loggedIn'
     */
    @Test
    public void loggedInTest() {
        // TODO: test loggedIn
    }

    /**
     * Test the property 'marketingData'
     */
    @Test
    public void marketingDataTest() {
        // TODO: test marketingData
    }

    /**
     * Test the property 'messages'
     */
    @Test
    public void messagesTest() {
        // TODO: test messages
    }

    /**
     * Test the property 'openTextField'
     */
    @Test
    public void openTextFieldTest() {
        // TODO: test openTextField
    }

    /**
     * Test the property 'orderFormId'
     */
    @Test
    public void orderFormIdTest() {
        // TODO: test orderFormId
    }

    /**
     * Test the property 'paymentData'
     */
    @Test
    public void paymentDataTest() {
        // TODO: test paymentData
    }

    /**
     * Test the property 'profileProvider'
     */
    @Test
    public void profileProviderTest() {
        // TODO: test profileProvider
    }

    /**
     * Test the property 'ratesAndBenefitsData'
     */
    @Test
    public void ratesAndBenefitsDataTest() {
        // TODO: test ratesAndBenefitsData
    }

    /**
     * Test the property 'salesChannel'
     */
    @Test
    public void salesChannelTest() {
        // TODO: test salesChannel
    }

    /**
     * Test the property 'selectableGifts'
     */
    @Test
    public void selectableGiftsTest() {
        // TODO: test selectableGifts
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
     * Test the property 'storeId'
     */
    @Test
    public void storeIdTest() {
        // TODO: test storeId
    }

    /**
     * Test the property 'storePreferencesData'
     */
    @Test
    public void storePreferencesDataTest() {
        // TODO: test storePreferencesData
    }

    /**
     * Test the property 'subscriptionData'
     */
    @Test
    public void subscriptionDataTest() {
        // TODO: test subscriptionData
    }

    /**
     * Test the property 'totalizers'
     */
    @Test
    public void totalizersTest() {
        // TODO: test totalizers
    }

    /**
     * Test the property 'userProfileId'
     */
    @Test
    public void userProfileIdTest() {
        // TODO: test userProfileId
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
