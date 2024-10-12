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
import AddCoupons200ResponseItemsInnerPriceDefinition from './AddCoupons200ResponseItemsInnerPriceDefinition';
import CartSimulation200ResponseItemsInnerPriceTagsInner from './CartSimulation200ResponseItemsInnerPriceTagsInner';

/**
 * The CartSimulation200ResponseItemsInner model module.
 * @module model/CartSimulation200ResponseItemsInner
 * @version 1.0
 */
class CartSimulation200ResponseItemsInner {
    /**
     * Constructs a new <code>CartSimulation200ResponseItemsInner</code>.
     * @alias module:model/CartSimulation200ResponseItemsInner
     */
    constructor() { 
        
        CartSimulation200ResponseItemsInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CartSimulation200ResponseItemsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CartSimulation200ResponseItemsInner} obj Optional instance to populate.
     * @return {module:model/CartSimulation200ResponseItemsInner} The populated <code>CartSimulation200ResponseItemsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CartSimulation200ResponseItemsInner();

            if (data.hasOwnProperty('availability')) {
                obj['availability'] = ApiClient.convertToType(data['availability'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('listPrice')) {
                obj['listPrice'] = ApiClient.convertToType(data['listPrice'], 'Number');
            }
            if (data.hasOwnProperty('measurementUnit')) {
                obj['measurementUnit'] = ApiClient.convertToType(data['measurementUnit'], 'String');
            }
            if (data.hasOwnProperty('offerings')) {
                obj['offerings'] = ApiClient.convertToType(data['offerings'], [Object]);
            }
            if (data.hasOwnProperty('parentAssemblyBinding')) {
                obj['parentAssemblyBinding'] = ApiClient.convertToType(data['parentAssemblyBinding'], 'String');
            }
            if (data.hasOwnProperty('parentItemIndex')) {
                obj['parentItemIndex'] = ApiClient.convertToType(data['parentItemIndex'], 'Number');
            }
            if (data.hasOwnProperty('price')) {
                obj['price'] = ApiClient.convertToType(data['price'], 'Number');
            }
            if (data.hasOwnProperty('priceDefinition')) {
                obj['priceDefinition'] = AddCoupons200ResponseItemsInnerPriceDefinition.constructFromObject(data['priceDefinition']);
            }
            if (data.hasOwnProperty('priceTags')) {
                obj['priceTags'] = ApiClient.convertToType(data['priceTags'], [CartSimulation200ResponseItemsInnerPriceTagsInner]);
            }
            if (data.hasOwnProperty('priceValidUntil')) {
                obj['priceValidUntil'] = ApiClient.convertToType(data['priceValidUntil'], 'String');
            }
            if (data.hasOwnProperty('quantity')) {
                obj['quantity'] = ApiClient.convertToType(data['quantity'], 'Number');
            }
            if (data.hasOwnProperty('requestIndex')) {
                obj['requestIndex'] = ApiClient.convertToType(data['requestIndex'], 'Number');
            }
            if (data.hasOwnProperty('rewardValue')) {
                obj['rewardValue'] = ApiClient.convertToType(data['rewardValue'], 'Number');
            }
            if (data.hasOwnProperty('seller')) {
                obj['seller'] = ApiClient.convertToType(data['seller'], 'String');
            }
            if (data.hasOwnProperty('sellerChain')) {
                obj['sellerChain'] = ApiClient.convertToType(data['sellerChain'], ['String']);
            }
            if (data.hasOwnProperty('sellingPrice')) {
                obj['sellingPrice'] = ApiClient.convertToType(data['sellingPrice'], 'Number');
            }
            if (data.hasOwnProperty('tax')) {
                obj['tax'] = ApiClient.convertToType(data['tax'], 'Number');
            }
            if (data.hasOwnProperty('unitMultiplier')) {
                obj['unitMultiplier'] = ApiClient.convertToType(data['unitMultiplier'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CartSimulation200ResponseItemsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CartSimulation200ResponseItemsInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['availability'] && !(typeof data['availability'] === 'string' || data['availability'] instanceof String)) {
            throw new Error("Expected the field `availability` to be a primitive type in the JSON string but got " + data['availability']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['measurementUnit'] && !(typeof data['measurementUnit'] === 'string' || data['measurementUnit'] instanceof String)) {
            throw new Error("Expected the field `measurementUnit` to be a primitive type in the JSON string but got " + data['measurementUnit']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['offerings'])) {
            throw new Error("Expected the field `offerings` to be an array in the JSON data but got " + data['offerings']);
        }
        // ensure the json data is a string
        if (data['parentAssemblyBinding'] && !(typeof data['parentAssemblyBinding'] === 'string' || data['parentAssemblyBinding'] instanceof String)) {
            throw new Error("Expected the field `parentAssemblyBinding` to be a primitive type in the JSON string but got " + data['parentAssemblyBinding']);
        }
        // validate the optional field `priceDefinition`
        if (data['priceDefinition']) { // data not null
          AddCoupons200ResponseItemsInnerPriceDefinition.validateJSON(data['priceDefinition']);
        }
        if (data['priceTags']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['priceTags'])) {
                throw new Error("Expected the field `priceTags` to be an array in the JSON data but got " + data['priceTags']);
            }
            // validate the optional field `priceTags` (array)
            for (const item of data['priceTags']) {
                CartSimulation200ResponseItemsInnerPriceTagsInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['priceValidUntil'] && !(typeof data['priceValidUntil'] === 'string' || data['priceValidUntil'] instanceof String)) {
            throw new Error("Expected the field `priceValidUntil` to be a primitive type in the JSON string but got " + data['priceValidUntil']);
        }
        // ensure the json data is a string
        if (data['seller'] && !(typeof data['seller'] === 'string' || data['seller'] instanceof String)) {
            throw new Error("Expected the field `seller` to be a primitive type in the JSON string but got " + data['seller']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['sellerChain'])) {
            throw new Error("Expected the field `sellerChain` to be an array in the JSON data but got " + data['sellerChain']);
        }

        return true;
    }


}



/**
 * Availability.
 * @member {String} availability
 */
CartSimulation200ResponseItemsInner.prototype['availability'] = undefined;

/**
 * ID of the item.
 * @member {String} id
 */
CartSimulation200ResponseItemsInner.prototype['id'] = undefined;

/**
 * List price in cents.
 * @member {Number} listPrice
 */
CartSimulation200ResponseItemsInner.prototype['listPrice'] = undefined;

/**
 * Measurement unit.
 * @member {String} measurementUnit
 */
CartSimulation200ResponseItemsInner.prototype['measurementUnit'] = undefined;

/**
 * Array containing offering information.
 * @member {Array.<Object>} offerings
 */
CartSimulation200ResponseItemsInner.prototype['offerings'] = undefined;

/**
 * Parent assembly binding.
 * @member {String} parentAssemblyBinding
 */
CartSimulation200ResponseItemsInner.prototype['parentAssemblyBinding'] = undefined;

/**
 * Parent item index.
 * @member {Number} parentItemIndex
 */
CartSimulation200ResponseItemsInner.prototype['parentItemIndex'] = undefined;

/**
 * Price in cents.
 * @member {Number} price
 */
CartSimulation200ResponseItemsInner.prototype['price'] = undefined;

/**
 * @member {module:model/AddCoupons200ResponseItemsInnerPriceDefinition} priceDefinition
 */
CartSimulation200ResponseItemsInner.prototype['priceDefinition'] = undefined;

/**
 * Array of price tags, each of which, modifies the price in some way, like discounts or rates that apply to the item in the context of the order.
 * @member {Array.<module:model/CartSimulation200ResponseItemsInnerPriceTagsInner>} priceTags
 */
CartSimulation200ResponseItemsInner.prototype['priceTags'] = undefined;

/**
 * Price expiration date and time.
 * @member {String} priceValidUntil
 */
CartSimulation200ResponseItemsInner.prototype['priceValidUntil'] = undefined;

/**
 * The quantity of the item the cart.
 * @member {Number} quantity
 */
CartSimulation200ResponseItemsInner.prototype['quantity'] = undefined;

/**
 * Request index information.
 * @member {Number} requestIndex
 */
CartSimulation200ResponseItemsInner.prototype['requestIndex'] = undefined;

/**
 * Reward value in cents.
 * @member {Number} rewardValue
 */
CartSimulation200ResponseItemsInner.prototype['rewardValue'] = undefined;

/**
 * The seller responsible for the SKU.
 * @member {String} seller
 */
CartSimulation200ResponseItemsInner.prototype['seller'] = undefined;

/**
 * Sellers involved in the chain. The list should contain only one seller, unless it is a [Multilevel Omnichannel Inventory](https://help.vtex.com/en/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4) order.
 * @member {Array.<String>} sellerChain
 */
CartSimulation200ResponseItemsInner.prototype['sellerChain'] = undefined;

/**
 * Selling price in cents. Note that this field may be subject to rounding discrepancies. We recommend retrieving data from the `priceDefinition` data structure instead.
 * @member {Number} sellingPrice
 */
CartSimulation200ResponseItemsInner.prototype['sellingPrice'] = undefined;

/**
 * Tax value in cents.
 * @member {Number} tax
 */
CartSimulation200ResponseItemsInner.prototype['tax'] = undefined;

/**
 * Unit multiplier.
 * @member {Number} unitMultiplier
 */
CartSimulation200ResponseItemsInner.prototype['unitMultiplier'] = undefined;






export default CartSimulation200ResponseItemsInner;

