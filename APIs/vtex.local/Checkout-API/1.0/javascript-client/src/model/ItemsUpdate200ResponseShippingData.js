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
import ItemsUpdate200ResponseShippingDataAddress from './ItemsUpdate200ResponseShippingDataAddress';
import ItemsUpdate200ResponseShippingDataAvailableAddressesInner from './ItemsUpdate200ResponseShippingDataAvailableAddressesInner';
import ItemsUpdate200ResponseShippingDataLogisticsInfoInner from './ItemsUpdate200ResponseShippingDataLogisticsInfoInner';

/**
 * The ItemsUpdate200ResponseShippingData model module.
 * @module model/ItemsUpdate200ResponseShippingData
 * @version 1.0
 */
class ItemsUpdate200ResponseShippingData {
    /**
     * Constructs a new <code>ItemsUpdate200ResponseShippingData</code>.
     * Shipping information pertinent to the order.
     * @alias module:model/ItemsUpdate200ResponseShippingData
     */
    constructor() { 
        
        ItemsUpdate200ResponseShippingData.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ItemsUpdate200ResponseShippingData</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ItemsUpdate200ResponseShippingData} obj Optional instance to populate.
     * @return {module:model/ItemsUpdate200ResponseShippingData} The populated <code>ItemsUpdate200ResponseShippingData</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ItemsUpdate200ResponseShippingData();

            if (data.hasOwnProperty('address')) {
                obj['address'] = ItemsUpdate200ResponseShippingDataAddress.constructFromObject(data['address']);
            }
            if (data.hasOwnProperty('availableAddresses')) {
                obj['availableAddresses'] = ApiClient.convertToType(data['availableAddresses'], [ItemsUpdate200ResponseShippingDataAvailableAddressesInner]);
            }
            if (data.hasOwnProperty('logisticsInfo')) {
                obj['logisticsInfo'] = ApiClient.convertToType(data['logisticsInfo'], [ItemsUpdate200ResponseShippingDataLogisticsInfoInner]);
            }
            if (data.hasOwnProperty('selectedAddresses')) {
                obj['selectedAddresses'] = ApiClient.convertToType(data['selectedAddresses'], [ItemsUpdate200ResponseShippingDataAvailableAddressesInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ItemsUpdate200ResponseShippingData</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ItemsUpdate200ResponseShippingData</code>.
     */
    static validateJSON(data) {
        // validate the optional field `address`
        if (data['address']) { // data not null
          ItemsUpdate200ResponseShippingDataAddress.validateJSON(data['address']);
        }
        if (data['availableAddresses']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['availableAddresses'])) {
                throw new Error("Expected the field `availableAddresses` to be an array in the JSON data but got " + data['availableAddresses']);
            }
            // validate the optional field `availableAddresses` (array)
            for (const item of data['availableAddresses']) {
                ItemsUpdate200ResponseShippingDataAvailableAddressesInner.validateJSON(item);
            };
        }
        if (data['logisticsInfo']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['logisticsInfo'])) {
                throw new Error("Expected the field `logisticsInfo` to be an array in the JSON data but got " + data['logisticsInfo']);
            }
            // validate the optional field `logisticsInfo` (array)
            for (const item of data['logisticsInfo']) {
                ItemsUpdate200ResponseShippingDataLogisticsInfoInner.validateJSON(item);
            };
        }
        if (data['selectedAddresses']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['selectedAddresses'])) {
                throw new Error("Expected the field `selectedAddresses` to be an array in the JSON data but got " + data['selectedAddresses']);
            }
            // validate the optional field `selectedAddresses` (array)
            for (const item of data['selectedAddresses']) {
                ItemsUpdate200ResponseShippingDataAvailableAddressesInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {module:model/ItemsUpdate200ResponseShippingDataAddress} address
 */
ItemsUpdate200ResponseShippingData.prototype['address'] = undefined;

/**
 * Array with information on the available addresses for the order.
 * @member {Array.<module:model/ItemsUpdate200ResponseShippingDataAvailableAddressesInner>} availableAddresses
 */
ItemsUpdate200ResponseShippingData.prototype['availableAddresses'] = undefined;

/**
 * Array with logistics information. Each object in this array corresponds to an object in the `items` array, based on the respective `itemIndex`.
 * @member {Array.<module:model/ItemsUpdate200ResponseShippingDataLogisticsInfoInner>} logisticsInfo
 */
ItemsUpdate200ResponseShippingData.prototype['logisticsInfo'] = undefined;

/**
 * Array with information on the selected addresses for the order.
 * @member {Array.<module:model/ItemsUpdate200ResponseShippingDataAvailableAddressesInner>} selectedAddresses
 */
ItemsUpdate200ResponseShippingData.prototype['selectedAddresses'] = undefined;






export default ItemsUpdate200ResponseShippingData;

