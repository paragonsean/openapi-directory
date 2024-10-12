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
import AddCoupons200ResponseClientProfileData from './AddCoupons200ResponseClientProfileData';
import AddCoupons200ResponseItemMetadata from './AddCoupons200ResponseItemMetadata';
import AddCoupons200ResponsePaymentData from './AddCoupons200ResponsePaymentData';
import AddCoupons200ResponseRatesAndBenefitsData from './AddCoupons200ResponseRatesAndBenefitsData';
import AddCoupons200ResponseSellersInner from './AddCoupons200ResponseSellersInner';
import AddCoupons200ResponseShippingData from './AddCoupons200ResponseShippingData';
import CartSimulation200ResponseLogisticsInfoInnerTotalsInner from './CartSimulation200ResponseLogisticsInfoInnerTotalsInner';
import PlaceOrder200ResponseOrdersInnerItemsInner from './PlaceOrder200ResponseOrdersInnerItemsInner';

/**
 * The PlaceOrder200ResponseOrdersInner model module.
 * @module model/PlaceOrder200ResponseOrdersInner
 * @version 1.0
 */
class PlaceOrder200ResponseOrdersInner {
    /**
     * Constructs a new <code>PlaceOrder200ResponseOrdersInner</code>.
     * @alias module:model/PlaceOrder200ResponseOrdersInner
     */
    constructor() { 
        
        PlaceOrder200ResponseOrdersInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['isCheckedIn'] = false;
    }

    /**
     * Constructs a <code>PlaceOrder200ResponseOrdersInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PlaceOrder200ResponseOrdersInner} obj Optional instance to populate.
     * @return {module:model/PlaceOrder200ResponseOrdersInner} The populated <code>PlaceOrder200ResponseOrdersInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PlaceOrder200ResponseOrdersInner();

            if (data.hasOwnProperty('allowCancelation')) {
                obj['allowCancelation'] = ApiClient.convertToType(data['allowCancelation'], 'Boolean');
            }
            if (data.hasOwnProperty('allowChangeSeller')) {
                obj['allowChangeSeller'] = ApiClient.convertToType(data['allowChangeSeller'], 'Boolean');
            }
            if (data.hasOwnProperty('allowEdition')) {
                obj['allowEdition'] = ApiClient.convertToType(data['allowEdition'], 'Boolean');
            }
            if (data.hasOwnProperty('checkedInPickupPointId')) {
                obj['checkedInPickupPointId'] = ApiClient.convertToType(data['checkedInPickupPointId'], 'String');
            }
            if (data.hasOwnProperty('clientProfileData')) {
                obj['clientProfileData'] = AddCoupons200ResponseClientProfileData.constructFromObject(data['clientProfileData']);
            }
            if (data.hasOwnProperty('creationDate')) {
                obj['creationDate'] = ApiClient.convertToType(data['creationDate'], 'String');
            }
            if (data.hasOwnProperty('followUpEmail')) {
                obj['followUpEmail'] = ApiClient.convertToType(data['followUpEmail'], 'String');
            }
            if (data.hasOwnProperty('hostName')) {
                obj['hostName'] = ApiClient.convertToType(data['hostName'], 'String');
            }
            if (data.hasOwnProperty('isCheckedIn')) {
                obj['isCheckedIn'] = ApiClient.convertToType(data['isCheckedIn'], 'Boolean');
            }
            if (data.hasOwnProperty('isCompleted')) {
                obj['isCompleted'] = ApiClient.convertToType(data['isCompleted'], 'Boolean');
            }
            if (data.hasOwnProperty('isUserDataVisible')) {
                obj['isUserDataVisible'] = ApiClient.convertToType(data['isUserDataVisible'], 'Boolean');
            }
            if (data.hasOwnProperty('itemMetadata')) {
                obj['itemMetadata'] = AddCoupons200ResponseItemMetadata.constructFromObject(data['itemMetadata']);
            }
            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [PlaceOrder200ResponseOrdersInnerItemsInner]);
            }
            if (data.hasOwnProperty('lastChange')) {
                obj['lastChange'] = ApiClient.convertToType(data['lastChange'], 'String');
            }
            if (data.hasOwnProperty('merchantName')) {
                obj['merchantName'] = ApiClient.convertToType(data['merchantName'], 'String');
            }
            if (data.hasOwnProperty('orderFormCreationDate')) {
                obj['orderFormCreationDate'] = ApiClient.convertToType(data['orderFormCreationDate'], 'String');
            }
            if (data.hasOwnProperty('orderGroup')) {
                obj['orderGroup'] = ApiClient.convertToType(data['orderGroup'], 'String');
            }
            if (data.hasOwnProperty('orderId')) {
                obj['orderId'] = ApiClient.convertToType(data['orderId'], 'String');
            }
            if (data.hasOwnProperty('paymentData')) {
                obj['paymentData'] = AddCoupons200ResponsePaymentData.constructFromObject(data['paymentData']);
            }
            if (data.hasOwnProperty('ratesAndBenefitsData')) {
                obj['ratesAndBenefitsData'] = AddCoupons200ResponseRatesAndBenefitsData.constructFromObject(data['ratesAndBenefitsData']);
            }
            if (data.hasOwnProperty('roundingError')) {
                obj['roundingError'] = ApiClient.convertToType(data['roundingError'], 'Number');
            }
            if (data.hasOwnProperty('salesAssociateId')) {
                obj['salesAssociateId'] = ApiClient.convertToType(data['salesAssociateId'], 'String');
            }
            if (data.hasOwnProperty('salesChannel')) {
                obj['salesChannel'] = ApiClient.convertToType(data['salesChannel'], 'String');
            }
            if (data.hasOwnProperty('sellerOrderId')) {
                obj['sellerOrderId'] = ApiClient.convertToType(data['sellerOrderId'], 'String');
            }
            if (data.hasOwnProperty('sellers')) {
                obj['sellers'] = ApiClient.convertToType(data['sellers'], [AddCoupons200ResponseSellersInner]);
            }
            if (data.hasOwnProperty('shippingData')) {
                obj['shippingData'] = AddCoupons200ResponseShippingData.constructFromObject(data['shippingData']);
            }
            if (data.hasOwnProperty('state')) {
                obj['state'] = ApiClient.convertToType(data['state'], 'String');
            }
            if (data.hasOwnProperty('storeId')) {
                obj['storeId'] = ApiClient.convertToType(data['storeId'], 'String');
            }
            if (data.hasOwnProperty('timeZoneCreationDate')) {
                obj['timeZoneCreationDate'] = ApiClient.convertToType(data['timeZoneCreationDate'], 'String');
            }
            if (data.hasOwnProperty('timeZoneLastChange')) {
                obj['timeZoneLastChange'] = ApiClient.convertToType(data['timeZoneLastChange'], 'String');
            }
            if (data.hasOwnProperty('totals')) {
                obj['totals'] = ApiClient.convertToType(data['totals'], [CartSimulation200ResponseLogisticsInfoInnerTotalsInner]);
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
     * Validates the JSON data with respect to <code>PlaceOrder200ResponseOrdersInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PlaceOrder200ResponseOrdersInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['checkedInPickupPointId'] && !(typeof data['checkedInPickupPointId'] === 'string' || data['checkedInPickupPointId'] instanceof String)) {
            throw new Error("Expected the field `checkedInPickupPointId` to be a primitive type in the JSON string but got " + data['checkedInPickupPointId']);
        }
        // validate the optional field `clientProfileData`
        if (data['clientProfileData']) { // data not null
          AddCoupons200ResponseClientProfileData.validateJSON(data['clientProfileData']);
        }
        // ensure the json data is a string
        if (data['creationDate'] && !(typeof data['creationDate'] === 'string' || data['creationDate'] instanceof String)) {
            throw new Error("Expected the field `creationDate` to be a primitive type in the JSON string but got " + data['creationDate']);
        }
        // ensure the json data is a string
        if (data['followUpEmail'] && !(typeof data['followUpEmail'] === 'string' || data['followUpEmail'] instanceof String)) {
            throw new Error("Expected the field `followUpEmail` to be a primitive type in the JSON string but got " + data['followUpEmail']);
        }
        // ensure the json data is a string
        if (data['hostName'] && !(typeof data['hostName'] === 'string' || data['hostName'] instanceof String)) {
            throw new Error("Expected the field `hostName` to be a primitive type in the JSON string but got " + data['hostName']);
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
                PlaceOrder200ResponseOrdersInnerItemsInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['lastChange'] && !(typeof data['lastChange'] === 'string' || data['lastChange'] instanceof String)) {
            throw new Error("Expected the field `lastChange` to be a primitive type in the JSON string but got " + data['lastChange']);
        }
        // ensure the json data is a string
        if (data['merchantName'] && !(typeof data['merchantName'] === 'string' || data['merchantName'] instanceof String)) {
            throw new Error("Expected the field `merchantName` to be a primitive type in the JSON string but got " + data['merchantName']);
        }
        // ensure the json data is a string
        if (data['orderFormCreationDate'] && !(typeof data['orderFormCreationDate'] === 'string' || data['orderFormCreationDate'] instanceof String)) {
            throw new Error("Expected the field `orderFormCreationDate` to be a primitive type in the JSON string but got " + data['orderFormCreationDate']);
        }
        // ensure the json data is a string
        if (data['orderGroup'] && !(typeof data['orderGroup'] === 'string' || data['orderGroup'] instanceof String)) {
            throw new Error("Expected the field `orderGroup` to be a primitive type in the JSON string but got " + data['orderGroup']);
        }
        // ensure the json data is a string
        if (data['orderId'] && !(typeof data['orderId'] === 'string' || data['orderId'] instanceof String)) {
            throw new Error("Expected the field `orderId` to be a primitive type in the JSON string but got " + data['orderId']);
        }
        // validate the optional field `paymentData`
        if (data['paymentData']) { // data not null
          AddCoupons200ResponsePaymentData.validateJSON(data['paymentData']);
        }
        // validate the optional field `ratesAndBenefitsData`
        if (data['ratesAndBenefitsData']) { // data not null
          AddCoupons200ResponseRatesAndBenefitsData.validateJSON(data['ratesAndBenefitsData']);
        }
        // ensure the json data is a string
        if (data['salesAssociateId'] && !(typeof data['salesAssociateId'] === 'string' || data['salesAssociateId'] instanceof String)) {
            throw new Error("Expected the field `salesAssociateId` to be a primitive type in the JSON string but got " + data['salesAssociateId']);
        }
        // ensure the json data is a string
        if (data['salesChannel'] && !(typeof data['salesChannel'] === 'string' || data['salesChannel'] instanceof String)) {
            throw new Error("Expected the field `salesChannel` to be a primitive type in the JSON string but got " + data['salesChannel']);
        }
        // ensure the json data is a string
        if (data['sellerOrderId'] && !(typeof data['sellerOrderId'] === 'string' || data['sellerOrderId'] instanceof String)) {
            throw new Error("Expected the field `sellerOrderId` to be a primitive type in the JSON string but got " + data['sellerOrderId']);
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
        if (data['state'] && !(typeof data['state'] === 'string' || data['state'] instanceof String)) {
            throw new Error("Expected the field `state` to be a primitive type in the JSON string but got " + data['state']);
        }
        // ensure the json data is a string
        if (data['storeId'] && !(typeof data['storeId'] === 'string' || data['storeId'] instanceof String)) {
            throw new Error("Expected the field `storeId` to be a primitive type in the JSON string but got " + data['storeId']);
        }
        // ensure the json data is a string
        if (data['timeZoneCreationDate'] && !(typeof data['timeZoneCreationDate'] === 'string' || data['timeZoneCreationDate'] instanceof String)) {
            throw new Error("Expected the field `timeZoneCreationDate` to be a primitive type in the JSON string but got " + data['timeZoneCreationDate']);
        }
        // ensure the json data is a string
        if (data['timeZoneLastChange'] && !(typeof data['timeZoneLastChange'] === 'string' || data['timeZoneLastChange'] instanceof String)) {
            throw new Error("Expected the field `timeZoneLastChange` to be a primitive type in the JSON string but got " + data['timeZoneLastChange']);
        }
        if (data['totals']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['totals'])) {
                throw new Error("Expected the field `totals` to be an array in the JSON data but got " + data['totals']);
            }
            // validate the optional field `totals` (array)
            for (const item of data['totals']) {
                CartSimulation200ResponseLogisticsInfoInnerTotalsInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['userType'] && !(typeof data['userType'] === 'string' || data['userType'] instanceof String)) {
            throw new Error("Expected the field `userType` to be a primitive type in the JSON string but got " + data['userType']);
        }

        return true;
    }


}



/**
 * Indicates whether cancelation is allowed.
 * @member {Boolean} allowCancelation
 */
PlaceOrder200ResponseOrdersInner.prototype['allowCancelation'] = undefined;

/**
 * Indicates whether seller changing is allowed.
 * @member {Boolean} allowChangeSeller
 */
PlaceOrder200ResponseOrdersInner.prototype['allowChangeSeller'] = undefined;

/**
 * Indicates whether edition is allowed.
 * @member {Boolean} allowEdition
 */
PlaceOrder200ResponseOrdersInner.prototype['allowEdition'] = undefined;

/**
 * Checked in pickuppoint.
 * @member {String} checkedInPickupPointId
 */
PlaceOrder200ResponseOrdersInner.prototype['checkedInPickupPointId'] = undefined;

/**
 * @member {module:model/AddCoupons200ResponseClientProfileData} clientProfileData
 */
PlaceOrder200ResponseOrdersInner.prototype['clientProfileData'] = undefined;

/**
 * Creation date.
 * @member {String} creationDate
 */
PlaceOrder200ResponseOrdersInner.prototype['creationDate'] = undefined;

/**
 * Follow up email address.
 * @member {String} followUpEmail
 */
PlaceOrder200ResponseOrdersInner.prototype['followUpEmail'] = undefined;

/**
 * Host name.
 * @member {String} hostName
 */
PlaceOrder200ResponseOrdersInner.prototype['hostName'] = undefined;

/**
 * Indicates whether order is checked in.
 * @member {Boolean} isCheckedIn
 * @default false
 */
PlaceOrder200ResponseOrdersInner.prototype['isCheckedIn'] = false;

/**
 * Indicates whether order is completed.
 * @member {Boolean} isCompleted
 */
PlaceOrder200ResponseOrdersInner.prototype['isCompleted'] = undefined;

/**
 * Indicates whether user data is visible.
 * @member {Boolean} isUserDataVisible
 */
PlaceOrder200ResponseOrdersInner.prototype['isUserDataVisible'] = undefined;

/**
 * @member {module:model/AddCoupons200ResponseItemMetadata} itemMetadata
 */
PlaceOrder200ResponseOrdersInner.prototype['itemMetadata'] = undefined;

/**
 * Information on each item in the order.
 * @member {Array.<module:model/PlaceOrder200ResponseOrdersInnerItemsInner>} items
 */
PlaceOrder200ResponseOrdersInner.prototype['items'] = undefined;

/**
 * Last change.
 * @member {String} lastChange
 */
PlaceOrder200ResponseOrdersInner.prototype['lastChange'] = undefined;

/**
 * Merchant name.
 * @member {String} merchantName
 */
PlaceOrder200ResponseOrdersInner.prototype['merchantName'] = undefined;

/**
 * `orderForm` creation date.
 * @member {String} orderFormCreationDate
 */
PlaceOrder200ResponseOrdersInner.prototype['orderFormCreationDate'] = undefined;

/**
 * Order group. Orders that involve different sellers are split into different orders of a same order group.
 * @member {String} orderGroup
 */
PlaceOrder200ResponseOrdersInner.prototype['orderGroup'] = undefined;

/**
 * ID of the order in the Order Management System (OMS).
 * @member {String} orderId
 */
PlaceOrder200ResponseOrdersInner.prototype['orderId'] = undefined;

/**
 * @member {module:model/AddCoupons200ResponsePaymentData} paymentData
 */
PlaceOrder200ResponseOrdersInner.prototype['paymentData'] = undefined;

/**
 * @member {module:model/AddCoupons200ResponseRatesAndBenefitsData} ratesAndBenefitsData
 */
PlaceOrder200ResponseOrdersInner.prototype['ratesAndBenefitsData'] = undefined;

/**
 * Rounding error.
 * @member {Number} roundingError
 */
PlaceOrder200ResponseOrdersInner.prototype['roundingError'] = undefined;

/**
 * Sales Associate (Seller) identification code.
 * @member {String} salesAssociateId
 */
PlaceOrder200ResponseOrdersInner.prototype['salesAssociateId'] = undefined;

/**
 * Sales channel.
 * @member {String} salesChannel
 */
PlaceOrder200ResponseOrdersInner.prototype['salesChannel'] = undefined;

/**
 * ID of the order in the seller.
 * @member {String} sellerOrderId
 */
PlaceOrder200ResponseOrdersInner.prototype['sellerOrderId'] = undefined;

/**
 * Information on each seller.
 * @member {Array.<module:model/AddCoupons200ResponseSellersInner>} sellers
 */
PlaceOrder200ResponseOrdersInner.prototype['sellers'] = undefined;

/**
 * @member {module:model/AddCoupons200ResponseShippingData} shippingData
 */
PlaceOrder200ResponseOrdersInner.prototype['shippingData'] = undefined;

/**
 * State.
 * @member {String} state
 */
PlaceOrder200ResponseOrdersInner.prototype['state'] = undefined;

/**
 * Store ID.
 * @member {String} storeId
 */
PlaceOrder200ResponseOrdersInner.prototype['storeId'] = undefined;

/**
 * Time zone creation date.
 * @member {String} timeZoneCreationDate
 */
PlaceOrder200ResponseOrdersInner.prototype['timeZoneCreationDate'] = undefined;

/**
 * Time zone last change.
 * @member {String} timeZoneLastChange
 */
PlaceOrder200ResponseOrdersInner.prototype['timeZoneLastChange'] = undefined;

/**
 * Information on order totals.
 * @member {Array.<module:model/CartSimulation200ResponseLogisticsInfoInnerTotalsInner>} totals
 */
PlaceOrder200ResponseOrdersInner.prototype['totals'] = undefined;

/**
 * User type.
 * @member {String} userType
 */
PlaceOrder200ResponseOrdersInner.prototype['userType'] = undefined;

/**
 * Value of the order.
 * @member {Number} value
 */
PlaceOrder200ResponseOrdersInner.prototype['value'] = undefined;






export default PlaceOrder200ResponseOrdersInner;

