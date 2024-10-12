/**
 * Checkout API
 * >ℹ️ Check the new [Checkout onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/checkout-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about the Checkout and is organized by focusing on the developer's journey.    The Checkout API allows you to obtain and configure information about the shopping cart and its attachments, personalization of custom fields, orderForm structure, fulfillment data, order management, and identification of the sellers delivery region.    >ℹ️ Data modification operations (`POST`, `PATCH`, `PUT` or `DELETE` endpoints) shall not be performed in parallel in the Checkout APIs. They need to be enqueued by the client/requester. Otherwise, old values ​​can be overwritten incorrectly or competition errors may occur.    >⚠️ All endpoints that consult or edit the orderForm can change the authentication depending on the customer context. If you are handling information from a customer with a complete profile on the store, authentication will be required. You can only access or modify the customer data for these profiles with an authenticated request.    ## Shopping cart    Allows merchants to simulate, configure and customize shopping cart information.    - [POST - Cart Simulation](https://developers.vtex.com/vtex-rest-api/reference/cartsimulation)  - [GET - Get current or create a new cart](https://developers.vtex.com/vtex-rest-api/reference/createanewcart)  - [GET - Get cart information by ID](https://developers.vtex.com/vtex-rest-api/reference/getcartinformationbyid)  - [POST - Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems)  - [GET - Remove all personal data](https://developers.vtex.com/vtex-rest-api/reference/removeallpersonaldata)  - [POST - Update cart items](https://developers.vtex.com/vtex-rest-api/reference/itemsupdate)  - [POST - Add cart items](https://developers.vtex.com/vtex-rest-api/reference/items)  - [PUT - Change price](https://developers.vtex.com/vtex-rest-api/reference/pricechange)  - [PATCH - Ignore profile data](https://developers.vtex.com/vtex-rest-api/reference/ignoreprofiledata)  - [GET - Cart installments](https://developers.vtex.com/vtex-rest-api/reference/getcartinstallments)  - [POST - Add coupons to the cart](https://developers.vtex.com/vtex-rest-api/reference/addcoupons)      ## Cart attachments    Allows merchants to obtain client profiles and add information to a given shopping cart.    - [GET - Get client profile by email](https://developers.vtex.com/vtex-rest-api/reference/getclientprofilebyemail)  - [POST - Add client profile](https://developers.vtex.com/vtex-rest-api/reference/addclientprofile)  - [POST - Add shipping address and select delivery option](https://developers.vtex.com/vtex-rest-api/reference/addshippingaddress)  - [POST - Add client preferences](https://developers.vtex.com/vtex-rest-api/reference/addclientpreferences)  - [POST - Add marketing data](https://developers.vtex.com/vtex-rest-api/reference/addmarketingdata)  - [POST - Add payment data](https://developers.vtex.com/vtex-rest-api/reference/addpaymentdata)  - [POST - Add merchant context data](https://developers.vtex.com/vtex-rest-api/reference/addmerchantcontextdata)      ## Custom data    Allows merchants to manage custom fields that were created by an app in their account.    - [PUT - Set multiple custom field values](https://developers.vtex.com/vtex-rest-api/reference/setmultiplecustomfieldvalues)  - [PUT - Set single custom field value](https://developers.vtex.com/vtex-rest-api/reference/setsinglecustomfieldvalue)  - [DELETE - Remove single custom field value](https://developers.vtex.com/vtex-rest-api/reference/removesinglecustomfieldvalue)      ## Configuration    Allows merchants to configure orderForm in the account and seller exchange on a given order.    - [GET - Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration)  - [POST - Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration)  - [GET - Get window to change seller](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller)  - [POST - Update window to change seller](https://developers.vtex.com/vtex-rest-api/reference/updatewindowtochangeseller)  - [POST - Clear orderForm messages](https://developers.vtex.com/vtex-rest-api/reference/clearorderformmessages)      ## Fulfillment    Allows merchants to obtain pickup points and address information.    - [GET - List pickup points by location](https://developers.vtex.com/vtex-rest-api/reference/listpickupppointsbylocation)  - [GET - Get address by postal code](https://developers.vtex.com/vtex-rest-api/reference/getaddressbypostalcode)      ## Order placement    Allows merchants to place and process orders by creating a new cart or using an existing cart.    - [POST - Place order from an existing cart](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)  - [PUT - Place order](https://developers.vtex.com/vtex-rest-api/reference/placeorder)  - [POST - Process order](https://developers.vtex.com/vtex-rest-api/reference/processorder)      ## Region    Allows merchants to obtain a list of sellers serving a specific delivery region.    - [GET - Get sellers by region or address](https://developers.vtex.com/vtex-rest-api/reference/getsellersbyregion)
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import AddCoupons200ResponseAvailableAddressesInner from './AddCoupons200ResponseAvailableAddressesInner';
import AddCoupons200ResponseClientPreferencesData from './AddCoupons200ResponseClientPreferencesData';
import AddCoupons200ResponseClientProfileData from './AddCoupons200ResponseClientProfileData';
import AddCoupons200ResponseItemMetadata from './AddCoupons200ResponseItemMetadata';
import AddCoupons200ResponseItemsInner from './AddCoupons200ResponseItemsInner';
import AddCoupons200ResponseItemsOrdination from './AddCoupons200ResponseItemsOrdination';
import AddCoupons200ResponseMarketingData from './AddCoupons200ResponseMarketingData';
import AddCoupons200ResponsePaymentData from './AddCoupons200ResponsePaymentData';
import AddCoupons200ResponseRatesAndBenefitsData from './AddCoupons200ResponseRatesAndBenefitsData';
import AddCoupons200ResponseSellersInner from './AddCoupons200ResponseSellersInner';
import AddCoupons200ResponseShippingData from './AddCoupons200ResponseShippingData';

/**
 * The AddCoupons200Response model module.
 * @module model/AddCoupons200Response
 * @version 1.0
 */
class AddCoupons200Response {
    /**
     * Constructs a new <code>AddCoupons200Response</code>.
     * @alias module:model/AddCoupons200Response
     */
    constructor() { 
        
        AddCoupons200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['openTextField'] = 'open-text-example';
    }

    /**
     * Constructs a <code>AddCoupons200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AddCoupons200Response} obj Optional instance to populate.
     * @return {module:model/AddCoupons200Response} The populated <code>AddCoupons200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AddCoupons200Response();

            if (data.hasOwnProperty('allowManualPrice')) {
                obj['allowManualPrice'] = ApiClient.convertToType(data['allowManualPrice'], 'Boolean');
            }
            if (data.hasOwnProperty('availableAccounts')) {
                obj['availableAccounts'] = ApiClient.convertToType(data['availableAccounts'], ['String']);
            }
            if (data.hasOwnProperty('availableAddresses')) {
                obj['availableAddresses'] = ApiClient.convertToType(data['availableAddresses'], [AddCoupons200ResponseAvailableAddressesInner]);
            }
            if (data.hasOwnProperty('canEditData')) {
                obj['canEditData'] = ApiClient.convertToType(data['canEditData'], 'Boolean');
            }
            if (data.hasOwnProperty('clientPreferencesData')) {
                obj['clientPreferencesData'] = AddCoupons200ResponseClientPreferencesData.constructFromObject(data['clientPreferencesData']);
            }
            if (data.hasOwnProperty('clientProfileData')) {
                obj['clientProfileData'] = AddCoupons200ResponseClientProfileData.constructFromObject(data['clientProfileData']);
            }
            if (data.hasOwnProperty('commercialConditionData')) {
                obj['commercialConditionData'] = ApiClient.convertToType(data['commercialConditionData'], Object);
            }
            if (data.hasOwnProperty('customData')) {
                obj['customData'] = ApiClient.convertToType(data['customData'], Object);
            }
            if (data.hasOwnProperty('giftRegistryData')) {
                obj['giftRegistryData'] = ApiClient.convertToType(data['giftRegistryData'], Object);
            }
            if (data.hasOwnProperty('hooksData')) {
                obj['hooksData'] = ApiClient.convertToType(data['hooksData'], Object);
            }
            if (data.hasOwnProperty('ignoreProfileData')) {
                obj['ignoreProfileData'] = ApiClient.convertToType(data['ignoreProfileData'], 'Boolean');
            }
            if (data.hasOwnProperty('invoiceData')) {
                obj['invoiceData'] = ApiClient.convertToType(data['invoiceData'], Object);
            }
            if (data.hasOwnProperty('isCheckedIn')) {
                obj['isCheckedIn'] = ApiClient.convertToType(data['isCheckedIn'], 'Boolean');
            }
            if (data.hasOwnProperty('itemMetadata')) {
                obj['itemMetadata'] = AddCoupons200ResponseItemMetadata.constructFromObject(data['itemMetadata']);
            }
            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [AddCoupons200ResponseItemsInner]);
            }
            if (data.hasOwnProperty('itemsOrdination')) {
                obj['itemsOrdination'] = AddCoupons200ResponseItemsOrdination.constructFromObject(data['itemsOrdination']);
            }
            if (data.hasOwnProperty('loggedIn')) {
                obj['loggedIn'] = ApiClient.convertToType(data['loggedIn'], 'Boolean');
            }
            if (data.hasOwnProperty('marketingData')) {
                obj['marketingData'] = AddCoupons200ResponseMarketingData.constructFromObject(data['marketingData']);
            }
            if (data.hasOwnProperty('messages')) {
                obj['messages'] = ApiClient.convertToType(data['messages'], [Object]);
            }
            if (data.hasOwnProperty('openTextField')) {
                obj['openTextField'] = ApiClient.convertToType(data['openTextField'], 'String');
            }
            if (data.hasOwnProperty('orderFormId')) {
                obj['orderFormId'] = ApiClient.convertToType(data['orderFormId'], 'String');
            }
            if (data.hasOwnProperty('paymentData')) {
                obj['paymentData'] = AddCoupons200ResponsePaymentData.constructFromObject(data['paymentData']);
            }
            if (data.hasOwnProperty('profileProvider')) {
                obj['profileProvider'] = ApiClient.convertToType(data['profileProvider'], 'String');
            }
            if (data.hasOwnProperty('ratesAndBenefitsData')) {
                obj['ratesAndBenefitsData'] = AddCoupons200ResponseRatesAndBenefitsData.constructFromObject(data['ratesAndBenefitsData']);
            }
            if (data.hasOwnProperty('salesChannel')) {
                obj['salesChannel'] = ApiClient.convertToType(data['salesChannel'], 'String');
            }
            if (data.hasOwnProperty('selectableGifts')) {
                obj['selectableGifts'] = ApiClient.convertToType(data['selectableGifts'], [Object]);
            }
            if (data.hasOwnProperty('sellers')) {
                obj['sellers'] = ApiClient.convertToType(data['sellers'], [AddCoupons200ResponseSellersInner]);
            }
            if (data.hasOwnProperty('shippingData')) {
                obj['shippingData'] = AddCoupons200ResponseShippingData.constructFromObject(data['shippingData']);
            }
            if (data.hasOwnProperty('storeId')) {
                obj['storeId'] = ApiClient.convertToType(data['storeId'], 'String');
            }
            if (data.hasOwnProperty('storePreferencesData')) {
                obj['storePreferencesData'] = ApiClient.convertToType(data['storePreferencesData'], Object);
            }
            if (data.hasOwnProperty('subscriptionData')) {
                obj['subscriptionData'] = ApiClient.convertToType(data['subscriptionData'], Object);
            }
            if (data.hasOwnProperty('totalizers')) {
                obj['totalizers'] = ApiClient.convertToType(data['totalizers'], [Object]);
            }
            if (data.hasOwnProperty('userProfileId')) {
                obj['userProfileId'] = ApiClient.convertToType(data['userProfileId'], 'String');
            }
            if (data.hasOwnProperty('userType')) {
                obj['userType'] = ApiClient.convertToType(data['userType'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AddCoupons200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AddCoupons200Response</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['availableAccounts'])) {
            throw new Error("Expected the field `availableAccounts` to be an array in the JSON data but got " + data['availableAccounts']);
        }
        if (data['availableAddresses']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['availableAddresses'])) {
                throw new Error("Expected the field `availableAddresses` to be an array in the JSON data but got " + data['availableAddresses']);
            }
            // validate the optional field `availableAddresses` (array)
            for (const item of data['availableAddresses']) {
                AddCoupons200ResponseAvailableAddressesInner.validateJSON(item);
            };
        }
        // validate the optional field `clientPreferencesData`
        if (data['clientPreferencesData']) { // data not null
          AddCoupons200ResponseClientPreferencesData.validateJSON(data['clientPreferencesData']);
        }
        // validate the optional field `clientProfileData`
        if (data['clientProfileData']) { // data not null
          AddCoupons200ResponseClientProfileData.validateJSON(data['clientProfileData']);
        }
        // validate the optional field `itemMetadata`
        if (data['itemMetadata']) { // data not null
          AddCoupons200ResponseItemMetadata.validateJSON(data['itemMetadata']);
        }
        if (data['items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['items'])) {
                throw new Error("Expected the field `items` to be an array in the JSON data but got " + data['items']);
            }
            // validate the optional field `items` (array)
            for (const item of data['items']) {
                AddCoupons200ResponseItemsInner.validateJSON(item);
            };
        }
        // validate the optional field `itemsOrdination`
        if (data['itemsOrdination']) { // data not null
          AddCoupons200ResponseItemsOrdination.validateJSON(data['itemsOrdination']);
        }
        // validate the optional field `marketingData`
        if (data['marketingData']) { // data not null
          AddCoupons200ResponseMarketingData.validateJSON(data['marketingData']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['messages'])) {
            throw new Error("Expected the field `messages` to be an array in the JSON data but got " + data['messages']);
        }
        // ensure the json data is a string
        if (data['openTextField'] && !(typeof data['openTextField'] === 'string' || data['openTextField'] instanceof String)) {
            throw new Error("Expected the field `openTextField` to be a primitive type in the JSON string but got " + data['openTextField']);
        }
        // ensure the json data is a string
        if (data['orderFormId'] && !(typeof data['orderFormId'] === 'string' || data['orderFormId'] instanceof String)) {
            throw new Error("Expected the field `orderFormId` to be a primitive type in the JSON string but got " + data['orderFormId']);
        }
        // validate the optional field `paymentData`
        if (data['paymentData']) { // data not null
          AddCoupons200ResponsePaymentData.validateJSON(data['paymentData']);
        }
        // ensure the json data is a string
        if (data['profileProvider'] && !(typeof data['profileProvider'] === 'string' || data['profileProvider'] instanceof String)) {
            throw new Error("Expected the field `profileProvider` to be a primitive type in the JSON string but got " + data['profileProvider']);
        }
        // validate the optional field `ratesAndBenefitsData`
        if (data['ratesAndBenefitsData']) { // data not null
          AddCoupons200ResponseRatesAndBenefitsData.validateJSON(data['ratesAndBenefitsData']);
        }
        // ensure the json data is a string
        if (data['salesChannel'] && !(typeof data['salesChannel'] === 'string' || data['salesChannel'] instanceof String)) {
            throw new Error("Expected the field `salesChannel` to be a primitive type in the JSON string but got " + data['salesChannel']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['selectableGifts'])) {
            throw new Error("Expected the field `selectableGifts` to be an array in the JSON data but got " + data['selectableGifts']);
        }
        if (data['sellers']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['sellers'])) {
                throw new Error("Expected the field `sellers` to be an array in the JSON data but got " + data['sellers']);
            }
            // validate the optional field `sellers` (array)
            for (const item of data['sellers']) {
                AddCoupons200ResponseSellersInner.validateJSON(item);
            };
        }
        // validate the optional field `shippingData`
        if (data['shippingData']) { // data not null
          AddCoupons200ResponseShippingData.validateJSON(data['shippingData']);
        }
        // ensure the json data is a string
        if (data['storeId'] && !(typeof data['storeId'] === 'string' || data['storeId'] instanceof String)) {
            throw new Error("Expected the field `storeId` to be a primitive type in the JSON string but got " + data['storeId']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['totalizers'])) {
            throw new Error("Expected the field `totalizers` to be an array in the JSON data but got " + data['totalizers']);
        }
        // ensure the json data is a string
        if (data['userProfileId'] && !(typeof data['userProfileId'] === 'string' || data['userProfileId'] instanceof String)) {
            throw new Error("Expected the field `userProfileId` to be a primitive type in the JSON string but got " + data['userProfileId']);
        }
        // ensure the json data is a string
        if (data['userType'] && !(typeof data['userType'] === 'string' || data['userType'] instanceof String)) {
            throw new Error("Expected the field `userType` to be a primitive type in the JSON string but got " + data['userType']);
        }

        return true;
    }


}



/**
 * Permission to modify item price manually.
 * @member {Boolean} allowManualPrice
 */
AddCoupons200Response.prototype['allowManualPrice'] = undefined;

/**
 * Available accounts.
 * @member {Array.<String>} availableAccounts
 */
AddCoupons200Response.prototype['availableAccounts'] = undefined;

/**
 * Information on each available address.
 * @member {Array.<module:model/AddCoupons200ResponseAvailableAddressesInner>} availableAddresses
 */
AddCoupons200Response.prototype['availableAddresses'] = undefined;

/**
 * Data can be edited.
 * @member {Boolean} canEditData
 */
AddCoupons200Response.prototype['canEditData'] = undefined;

/**
 * @member {module:model/AddCoupons200ResponseClientPreferencesData} clientPreferencesData
 */
AddCoupons200Response.prototype['clientPreferencesData'] = undefined;

/**
 * @member {module:model/AddCoupons200ResponseClientProfileData} clientProfileData
 */
AddCoupons200Response.prototype['clientProfileData'] = undefined;

/**
 * Object containing commercial condition information.
 * @member {Object} commercialConditionData
 */
AddCoupons200Response.prototype['commercialConditionData'] = undefined;

/**
 * Customer additional information.
 * @member {Object} customData
 */
AddCoupons200Response.prototype['customData'] = undefined;

/**
 * Gift registry list information.
 * @member {Object} giftRegistryData
 */
AddCoupons200Response.prototype['giftRegistryData'] = undefined;

/**
 * Hooks information.
 * @member {Object} hooksData
 */
AddCoupons200Response.prototype['hooksData'] = undefined;

/**
 * Ignore customer profile data.
 * @member {Boolean} ignoreProfileData
 */
AddCoupons200Response.prototype['ignoreProfileData'] = undefined;

/**
 * Object containing information pertinent to the order's invoice.
 * @member {Object} invoiceData
 */
AddCoupons200Response.prototype['invoiceData'] = undefined;

/**
 * Indicates whether order is checked in.
 * @member {Boolean} isCheckedIn
 */
AddCoupons200Response.prototype['isCheckedIn'] = undefined;

/**
 * @member {module:model/AddCoupons200ResponseItemMetadata} itemMetadata
 */
AddCoupons200Response.prototype['itemMetadata'] = undefined;

/**
 * Information on each item in the order.
 * @member {Array.<module:model/AddCoupons200ResponseItemsInner>} items
 */
AddCoupons200Response.prototype['items'] = undefined;

/**
 * @member {module:model/AddCoupons200ResponseItemsOrdination} itemsOrdination
 */
AddCoupons200Response.prototype['itemsOrdination'] = undefined;

/**
 * Indicates whether the user is logged into the store.
 * @member {Boolean} loggedIn
 */
AddCoupons200Response.prototype['loggedIn'] = undefined;

/**
 * @member {module:model/AddCoupons200ResponseMarketingData} marketingData
 */
AddCoupons200Response.prototype['marketingData'] = undefined;

/**
 * Array containing an object for each message generated by our servers while processing the request.
 * @member {Array.<Object>} messages
 */
AddCoupons200Response.prototype['messages'] = undefined;

/**
 * Optional field meant to hold additional information about the order. We recommend using this field for text, not data formats such as `JSON` even if escaped. For that purpose, see [Creating customizable fields](https://developers.vtex.com/vtex-rest-api/docs/creating-customizable-fields-in-the-cart-with-checkout-api-1)
 * @member {String} openTextField
 * @default 'open-text-example'
 */
AddCoupons200Response.prototype['openTextField'] = 'open-text-example';

/**
 * ID of the orderForm corresponding to a specific cart.
 * @member {String} orderFormId
 */
AddCoupons200Response.prototype['orderFormId'] = undefined;

/**
 * @member {module:model/AddCoupons200ResponsePaymentData} paymentData
 */
AddCoupons200Response.prototype['paymentData'] = undefined;

/**
 * Profile provider.
 * @member {String} profileProvider
 */
AddCoupons200Response.prototype['profileProvider'] = undefined;

/**
 * @member {module:model/AddCoupons200ResponseRatesAndBenefitsData} ratesAndBenefitsData
 */
AddCoupons200Response.prototype['ratesAndBenefitsData'] = undefined;

/**
 * Attribute created by the seller, in their VTEX store configuration.
 * @member {String} salesChannel
 */
AddCoupons200Response.prototype['salesChannel'] = undefined;

/**
 * Array containing the data of the item selected as a gift.
 * @member {Array.<Object>} selectableGifts
 */
AddCoupons200Response.prototype['selectableGifts'] = undefined;

/**
 * Information on each seller.
 * @member {Array.<module:model/AddCoupons200ResponseSellersInner>} sellers
 */
AddCoupons200Response.prototype['sellers'] = undefined;

/**
 * @member {module:model/AddCoupons200ResponseShippingData} shippingData
 */
AddCoupons200Response.prototype['shippingData'] = undefined;

/**
 * ID of the store.
 * @member {String} storeId
 */
AddCoupons200Response.prototype['storeId'] = undefined;

/**
 * Object containing data from the store's configuration (stored in VTEX's License Manager).
 * @member {Object} storePreferencesData
 */
AddCoupons200Response.prototype['storePreferencesData'] = undefined;

/**
 * Subscription information.
 * @member {Object} subscriptionData
 */
AddCoupons200Response.prototype['subscriptionData'] = undefined;

/**
 * Array containing an object for each totalizer for the purchase. Totalizers contain the sum of values for a specific part of the order (e.g. Total item value, Total shipping value).
 * @member {Array.<Object>} totalizers
 */
AddCoupons200Response.prototype['totalizers'] = undefined;

/**
 * Unique ID associated with the customer profile.
 * @member {String} userProfileId
 */
AddCoupons200Response.prototype['userProfileId'] = undefined;

/**
 * User type.
 * @member {String} userType
 */
AddCoupons200Response.prototype['userType'] = undefined;

/**
 * Total value of the order without separating cents. For example, $24.99 is represented `2499`.
 * @member {Number} value
 */
AddCoupons200Response.prototype['value'] = undefined;






export default AddCoupons200Response;

