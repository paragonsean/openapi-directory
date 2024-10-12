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
import org.openapitools.client.model.AddCoupons200ResponseItemsInnerAdditionalInfo;
import org.openapitools.client.model.AddCoupons200ResponseItemsInnerBundleItemsInner;
import org.openapitools.client.model.AddCoupons200ResponseItemsInnerPriceDefinition;
import org.openapitools.client.model.AddCoupons200ResponseItemsInnerPriceTagsInner;
import org.openapitools.client.model.AddCoupons200ResponseItemsInnerProductCategories;
import org.openapitools.jackson.nullable.JsonNullable;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for AddCoupons200ResponseItemsInner
 */
public class AddCoupons200ResponseItemsInnerTest {
    private final AddCoupons200ResponseItemsInner model = new AddCoupons200ResponseItemsInner();

    /**
     * Model tests for AddCoupons200ResponseItemsInner
     */
    @Test
    public void testAddCoupons200ResponseItemsInner() {
        // TODO: test AddCoupons200ResponseItemsInner
    }

    /**
     * Test the property 'additionalInfo'
     */
    @Test
    public void additionalInfoTest() {
        // TODO: test additionalInfo
    }

    /**
     * Test the property 'attachments'
     */
    @Test
    public void attachmentsTest() {
        // TODO: test attachments
    }

    /**
     * Test the property 'availability'
     */
    @Test
    public void availabilityTest() {
        // TODO: test availability
    }

    /**
     * Test the property 'bundleItems'
     */
    @Test
    public void bundleItemsTest() {
        // TODO: test bundleItems
    }

    /**
     * Test the property 'detailUrl'
     */
    @Test
    public void detailUrlTest() {
        // TODO: test detailUrl
    }

    /**
     * Test the property 'ean'
     */
    @Test
    public void eanTest() {
        // TODO: test ean
    }

    /**
     * Test the property 'id'
     */
    @Test
    public void idTest() {
        // TODO: test id
    }

    /**
     * Test the property 'imageUrl'
     */
    @Test
    public void imageUrlTest() {
        // TODO: test imageUrl
    }

    /**
     * Test the property 'isGift'
     */
    @Test
    public void isGiftTest() {
        // TODO: test isGift
    }

    /**
     * Test the property 'listPrice'
     */
    @Test
    public void listPriceTest() {
        // TODO: test listPrice
    }

    /**
     * Test the property 'manualPrice'
     */
    @Test
    public void manualPriceTest() {
        // TODO: test manualPrice
    }

    /**
     * Test the property 'manualPriceAppliedBy'
     */
    @Test
    public void manualPriceAppliedByTest() {
        // TODO: test manualPriceAppliedBy
    }

    /**
     * Test the property 'manufacturerCode'
     */
    @Test
    public void manufacturerCodeTest() {
        // TODO: test manufacturerCode
    }

    /**
     * Test the property 'measurementUnit'
     */
    @Test
    public void measurementUnitTest() {
        // TODO: test measurementUnit
    }

    /**
     * Test the property 'modalType'
     */
    @Test
    public void modalTypeTest() {
        // TODO: test modalType
    }

    /**
     * Test the property 'name'
     */
    @Test
    public void nameTest() {
        // TODO: test name
    }

    /**
     * Test the property 'parentAssemblyBinding'
     */
    @Test
    public void parentAssemblyBindingTest() {
        // TODO: test parentAssemblyBinding
    }

    /**
     * Test the property 'parentItemIndex'
     */
    @Test
    public void parentItemIndexTest() {
        // TODO: test parentItemIndex
    }

    /**
     * Test the property 'preSaleDate'
     */
    @Test
    public void preSaleDateTest() {
        // TODO: test preSaleDate
    }

    /**
     * Test the property 'price'
     */
    @Test
    public void priceTest() {
        // TODO: test price
    }

    /**
     * Test the property 'priceDefinition'
     */
    @Test
    public void priceDefinitionTest() {
        // TODO: test priceDefinition
    }

    /**
     * Test the property 'priceTags'
     */
    @Test
    public void priceTagsTest() {
        // TODO: test priceTags
    }

    /**
     * Test the property 'priceValidUntil'
     */
    @Test
    public void priceValidUntilTest() {
        // TODO: test priceValidUntil
    }

    /**
     * Test the property 'productCategories'
     */
    @Test
    public void productCategoriesTest() {
        // TODO: test productCategories
    }

    /**
     * Test the property 'productCategoryIds'
     */
    @Test
    public void productCategoryIdsTest() {
        // TODO: test productCategoryIds
    }

    /**
     * Test the property 'productId'
     */
    @Test
    public void productIdTest() {
        // TODO: test productId
    }

    /**
     * Test the property 'productRefId'
     */
    @Test
    public void productRefIdTest() {
        // TODO: test productRefId
    }

    /**
     * Test the property 'quantity'
     */
    @Test
    public void quantityTest() {
        // TODO: test quantity
    }

    /**
     * Test the property 'refId'
     */
    @Test
    public void refIdTest() {
        // TODO: test refId
    }

    /**
     * Test the property 'rewardValue'
     */
    @Test
    public void rewardValueTest() {
        // TODO: test rewardValue
    }

    /**
     * Test the property 'seller'
     */
    @Test
    public void sellerTest() {
        // TODO: test seller
    }

    /**
     * Test the property 'sellerChain'
     */
    @Test
    public void sellerChainTest() {
        // TODO: test sellerChain
    }

    /**
     * Test the property 'sellingPrice'
     */
    @Test
    public void sellingPriceTest() {
        // TODO: test sellingPrice
    }

    /**
     * Test the property 'skuName'
     */
    @Test
    public void skuNameTest() {
        // TODO: test skuName
    }

    /**
     * Test the property 'tax'
     */
    @Test
    public void taxTest() {
        // TODO: test tax
    }

    /**
     * Test the property 'uniqueId'
     */
    @Test
    public void uniqueIdTest() {
        // TODO: test uniqueId
    }

    /**
     * Test the property 'unitMultiplier'
     */
    @Test
    public void unitMultiplierTest() {
        // TODO: test unitMultiplier
    }

}
