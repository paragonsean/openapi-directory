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
import AddCoupons200ResponseItemsInnerAdditionalInfo from './AddCoupons200ResponseItemsInnerAdditionalInfo';
import AddCoupons200ResponseItemsInnerBundleItemsInner from './AddCoupons200ResponseItemsInnerBundleItemsInner';
import AddCoupons200ResponseItemsInnerPriceDefinition from './AddCoupons200ResponseItemsInnerPriceDefinition';
import AddCoupons200ResponseItemsInnerPriceTagsInner from './AddCoupons200ResponseItemsInnerPriceTagsInner';
import AddCoupons200ResponseItemsInnerProductCategories from './AddCoupons200ResponseItemsInnerProductCategories';

/**
 * The PlaceOrder200ResponseOrdersInnerItemsInner model module.
 * @module model/PlaceOrder200ResponseOrdersInnerItemsInner
 * @version 1.0
 */
class PlaceOrder200ResponseOrdersInnerItemsInner {
    /**
     * Constructs a new <code>PlaceOrder200ResponseOrdersInnerItemsInner</code>.
     * @alias module:model/PlaceOrder200ResponseOrdersInnerItemsInner
     */
    constructor() { 
        
        PlaceOrder200ResponseOrdersInnerItemsInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PlaceOrder200ResponseOrdersInnerItemsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PlaceOrder200ResponseOrdersInnerItemsInner} obj Optional instance to populate.
     * @return {module:model/PlaceOrder200ResponseOrdersInnerItemsInner} The populated <code>PlaceOrder200ResponseOrdersInnerItemsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PlaceOrder200ResponseOrdersInnerItemsInner();

            if (data.hasOwnProperty('additionalInfo')) {
                obj['additionalInfo'] = AddCoupons200ResponseItemsInnerAdditionalInfo.constructFromObject(data['additionalInfo']);
            }
            if (data.hasOwnProperty('attachments')) {
                obj['attachments'] = ApiClient.convertToType(data['attachments'], ['String']);
            }
            if (data.hasOwnProperty('availability')) {
                obj['availability'] = ApiClient.convertToType(data['availability'], 'String');
            }
            if (data.hasOwnProperty('bundleItems')) {
                obj['bundleItems'] = ApiClient.convertToType(data['bundleItems'], [AddCoupons200ResponseItemsInnerBundleItemsInner]);
            }
            if (data.hasOwnProperty('detailUrl')) {
                obj['detailUrl'] = ApiClient.convertToType(data['detailUrl'], 'String');
            }
            if (data.hasOwnProperty('ean')) {
                obj['ean'] = ApiClient.convertToType(data['ean'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('imageUrl')) {
                obj['imageUrl'] = ApiClient.convertToType(data['imageUrl'], 'String');
            }
            if (data.hasOwnProperty('isGift')) {
                obj['isGift'] = ApiClient.convertToType(data['isGift'], 'Boolean');
            }
            if (data.hasOwnProperty('listPrice')) {
                obj['listPrice'] = ApiClient.convertToType(data['listPrice'], 'Number');
            }
            if (data.hasOwnProperty('manualPrice')) {
                obj['manualPrice'] = ApiClient.convertToType(data['manualPrice'], 'Number');
            }
            if (data.hasOwnProperty('manualPriceAppliedBy')) {
                obj['manualPriceAppliedBy'] = ApiClient.convertToType(data['manualPriceAppliedBy'], 'String');
            }
            if (data.hasOwnProperty('manufacturerCode')) {
                obj['manufacturerCode'] = ApiClient.convertToType(data['manufacturerCode'], 'String');
            }
            if (data.hasOwnProperty('measurementUnit')) {
                obj['measurementUnit'] = ApiClient.convertToType(data['measurementUnit'], 'String');
            }
            if (data.hasOwnProperty('modalType')) {
                obj['modalType'] = ApiClient.convertToType(data['modalType'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('parentAssemblyBinding')) {
                obj['parentAssemblyBinding'] = ApiClient.convertToType(data['parentAssemblyBinding'], 'String');
            }
            if (data.hasOwnProperty('parentItemIndex')) {
                obj['parentItemIndex'] = ApiClient.convertToType(data['parentItemIndex'], 'Number');
            }
            if (data.hasOwnProperty('preSaleDate')) {
                obj['preSaleDate'] = ApiClient.convertToType(data['preSaleDate'], 'String');
            }
            if (data.hasOwnProperty('price')) {
                obj['price'] = ApiClient.convertToType(data['price'], 'Number');
            }
            if (data.hasOwnProperty('priceDefinition')) {
                obj['priceDefinition'] = AddCoupons200ResponseItemsInnerPriceDefinition.constructFromObject(data['priceDefinition']);
            }
            if (data.hasOwnProperty('priceTags')) {
                obj['priceTags'] = ApiClient.convertToType(data['priceTags'], [AddCoupons200ResponseItemsInnerPriceTagsInner]);
            }
            if (data.hasOwnProperty('priceValidUntil')) {
                obj['priceValidUntil'] = ApiClient.convertToType(data['priceValidUntil'], 'String');
            }
            if (data.hasOwnProperty('productCategories')) {
                obj['productCategories'] = AddCoupons200ResponseItemsInnerProductCategories.constructFromObject(data['productCategories']);
            }
            if (data.hasOwnProperty('productCategoryIds')) {
                obj['productCategoryIds'] = ApiClient.convertToType(data['productCategoryIds'], 'String');
            }
            if (data.hasOwnProperty('productId')) {
                obj['productId'] = ApiClient.convertToType(data['productId'], 'String');
            }
            if (data.hasOwnProperty('productRefId')) {
                obj['productRefId'] = ApiClient.convertToType(data['productRefId'], 'String');
            }
            if (data.hasOwnProperty('quantity')) {
                obj['quantity'] = ApiClient.convertToType(data['quantity'], 'Number');
            }
            if (data.hasOwnProperty('refId')) {
                obj['refId'] = ApiClient.convertToType(data['refId'], 'String');
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
            if (data.hasOwnProperty('skuName')) {
                obj['skuName'] = ApiClient.convertToType(data['skuName'], 'String');
            }
            if (data.hasOwnProperty('tax')) {
                obj['tax'] = ApiClient.convertToType(data['tax'], 'Number');
            }
            if (data.hasOwnProperty('uniqueId')) {
                obj['uniqueId'] = ApiClient.convertToType(data['uniqueId'], 'String');
            }
            if (data.hasOwnProperty('unitMultiplier')) {
                obj['unitMultiplier'] = ApiClient.convertToType(data['unitMultiplier'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PlaceOrder200ResponseOrdersInnerItemsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PlaceOrder200ResponseOrdersInnerItemsInner</code>.
     */
    static validateJSON(data) {
        // validate the optional field `additionalInfo`
        if (data['additionalInfo']) { // data not null
          AddCoupons200ResponseItemsInnerAdditionalInfo.validateJSON(data['additionalInfo']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['attachments'])) {
            throw new Error("Expected the field `attachments` to be an array in the JSON data but got " + data['attachments']);
        }
        // ensure the json data is a string
        if (data['availability'] && !(typeof data['availability'] === 'string' || data['availability'] instanceof String)) {
            throw new Error("Expected the field `availability` to be a primitive type in the JSON string but got " + data['availability']);
        }
        if (data['bundleItems']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['bundleItems'])) {
                throw new Error("Expected the field `bundleItems` to be an array in the JSON data but got " + data['bundleItems']);
            }
            // validate the optional field `bundleItems` (array)
            for (const item of data['bundleItems']) {
                AddCoupons200ResponseItemsInnerBundleItemsInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['detailUrl'] && !(typeof data['detailUrl'] === 'string' || data['detailUrl'] instanceof String)) {
            throw new Error("Expected the field `detailUrl` to be a primitive type in the JSON string but got " + data['detailUrl']);
        }
        // ensure the json data is a string
        if (data['ean'] && !(typeof data['ean'] === 'string' || data['ean'] instanceof String)) {
            throw new Error("Expected the field `ean` to be a primitive type in the JSON string but got " + data['ean']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['imageUrl'] && !(typeof data['imageUrl'] === 'string' || data['imageUrl'] instanceof String)) {
            throw new Error("Expected the field `imageUrl` to be a primitive type in the JSON string but got " + data['imageUrl']);
        }
        // ensure the json data is a string
        if (data['manualPriceAppliedBy'] && !(typeof data['manualPriceAppliedBy'] === 'string' || data['manualPriceAppliedBy'] instanceof String)) {
            throw new Error("Expected the field `manualPriceAppliedBy` to be a primitive type in the JSON string but got " + data['manualPriceAppliedBy']);
        }
        // ensure the json data is a string
        if (data['manufacturerCode'] && !(typeof data['manufacturerCode'] === 'string' || data['manufacturerCode'] instanceof String)) {
            throw new Error("Expected the field `manufacturerCode` to be a primitive type in the JSON string but got " + data['manufacturerCode']);
        }
        // ensure the json data is a string
        if (data['measurementUnit'] && !(typeof data['measurementUnit'] === 'string' || data['measurementUnit'] instanceof String)) {
            throw new Error("Expected the field `measurementUnit` to be a primitive type in the JSON string but got " + data['measurementUnit']);
        }
        // ensure the json data is a string
        if (data['modalType'] && !(typeof data['modalType'] === 'string' || data['modalType'] instanceof String)) {
            throw new Error("Expected the field `modalType` to be a primitive type in the JSON string but got " + data['modalType']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['parentAssemblyBinding'] && !(typeof data['parentAssemblyBinding'] === 'string' || data['parentAssemblyBinding'] instanceof String)) {
            throw new Error("Expected the field `parentAssemblyBinding` to be a primitive type in the JSON string but got " + data['parentAssemblyBinding']);
        }
        // ensure the json data is a string
        if (data['preSaleDate'] && !(typeof data['preSaleDate'] === 'string' || data['preSaleDate'] instanceof String)) {
            throw new Error("Expected the field `preSaleDate` to be a primitive type in the JSON string but got " + data['preSaleDate']);
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
                AddCoupons200ResponseItemsInnerPriceTagsInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['priceValidUntil'] && !(typeof data['priceValidUntil'] === 'string' || data['priceValidUntil'] instanceof String)) {
            throw new Error("Expected the field `priceValidUntil` to be a primitive type in the JSON string but got " + data['priceValidUntil']);
        }
        // validate the optional field `productCategories`
        if (data['productCategories']) { // data not null
          AddCoupons200ResponseItemsInnerProductCategories.validateJSON(data['productCategories']);
        }
        // ensure the json data is a string
        if (data['productCategoryIds'] && !(typeof data['productCategoryIds'] === 'string' || data['productCategoryIds'] instanceof String)) {
            throw new Error("Expected the field `productCategoryIds` to be a primitive type in the JSON string but got " + data['productCategoryIds']);
        }
        // ensure the json data is a string
        if (data['productId'] && !(typeof data['productId'] === 'string' || data['productId'] instanceof String)) {
            throw new Error("Expected the field `productId` to be a primitive type in the JSON string but got " + data['productId']);
        }
        // ensure the json data is a string
        if (data['productRefId'] && !(typeof data['productRefId'] === 'string' || data['productRefId'] instanceof String)) {
            throw new Error("Expected the field `productRefId` to be a primitive type in the JSON string but got " + data['productRefId']);
        }
        // ensure the json data is a string
        if (data['refId'] && !(typeof data['refId'] === 'string' || data['refId'] instanceof String)) {
            throw new Error("Expected the field `refId` to be a primitive type in the JSON string but got " + data['refId']);
        }
        // ensure the json data is a string
        if (data['seller'] && !(typeof data['seller'] === 'string' || data['seller'] instanceof String)) {
            throw new Error("Expected the field `seller` to be a primitive type in the JSON string but got " + data['seller']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['sellerChain'])) {
            throw new Error("Expected the field `sellerChain` to be an array in the JSON data but got " + data['sellerChain']);
        }
        // ensure the json data is a string
        if (data['skuName'] && !(typeof data['skuName'] === 'string' || data['skuName'] instanceof String)) {
            throw new Error("Expected the field `skuName` to be a primitive type in the JSON string but got " + data['skuName']);
        }
        // ensure the json data is a string
        if (data['uniqueId'] && !(typeof data['uniqueId'] === 'string' || data['uniqueId'] instanceof String)) {
            throw new Error("Expected the field `uniqueId` to be a primitive type in the JSON string but got " + data['uniqueId']);
        }

        return true;
    }


}



/**
 * @member {module:model/AddCoupons200ResponseItemsInnerAdditionalInfo} additionalInfo
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['additionalInfo'] = undefined;

/**
 * Array containing information on attachments.
 * @member {Array.<String>} attachments
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['attachments'] = undefined;

/**
 * Availability
 * @member {String} availability
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['availability'] = undefined;

/**
 * Information on services sold along with the SKU. Example: a gift package.
 * @member {Array.<module:model/AddCoupons200ResponseItemsInnerBundleItemsInner>} bundleItems
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['bundleItems'] = undefined;

/**
 * Detail URL.
 * @member {String} detailUrl
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['detailUrl'] = undefined;

/**
 * European Article Number.
 * @member {String} ean
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['ean'] = undefined;

/**
 * ID of the item.
 * @member {String} id
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['id'] = undefined;

/**
 * Image URL.
 * @member {String} imageUrl
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['imageUrl'] = undefined;

/**
 * Indicates whether item is a gift.
 * @member {Boolean} isGift
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['isGift'] = undefined;

/**
 * List price in cents.
 * @member {Number} listPrice
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['listPrice'] = undefined;

/**
 * Manual price in cents.
 * @member {Number} manualPrice
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['manualPrice'] = undefined;

/**
 * User that applied the manual price, if that is the case.
 * @member {String} manualPriceAppliedBy
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['manualPriceAppliedBy'] = undefined;

/**
 * Manufacturer code.
 * @member {String} manufacturerCode
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['manufacturerCode'] = undefined;

/**
 * Measurement unit
 * @member {String} measurementUnit
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['measurementUnit'] = undefined;

/**
 * Modal type.
 * @member {String} modalType
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['modalType'] = undefined;

/**
 * Product name.
 * @member {String} name
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['name'] = undefined;

/**
 * Parent assembly binding.
 * @member {String} parentAssemblyBinding
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['parentAssemblyBinding'] = undefined;

/**
 * Parent item index.
 * @member {Number} parentItemIndex
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['parentItemIndex'] = undefined;

/**
 * Presale date.
 * @member {String} preSaleDate
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['preSaleDate'] = undefined;

/**
 * Price in cents.
 * @member {Number} price
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['price'] = undefined;

/**
 * @member {module:model/AddCoupons200ResponseItemsInnerPriceDefinition} priceDefinition
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['priceDefinition'] = undefined;

/**
 * Array of price tags, each of which, modifies the price in some way, like discounts or rates that apply to the item in the context of the order.
 * @member {Array.<module:model/AddCoupons200ResponseItemsInnerPriceTagsInner>} priceTags
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['priceTags'] = undefined;

/**
 * Price expiration date and time.
 * @member {String} priceValidUntil
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['priceValidUntil'] = undefined;

/**
 * @member {module:model/AddCoupons200ResponseItemsInnerProductCategories} productCategories
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['productCategories'] = undefined;

/**
 * Product category IDs.
 * @member {String} productCategoryIds
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['productCategoryIds'] = undefined;

/**
 * Product ID.
 * @member {String} productId
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['productId'] = undefined;

/**
 * Product Ref ID.
 * @member {String} productRefId
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['productRefId'] = undefined;

/**
 * Quantity.
 * @member {Number} quantity
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['quantity'] = undefined;

/**
 * Ref ID.
 * @member {String} refId
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['refId'] = undefined;

/**
 * Reward value in cents.
 * @member {Number} rewardValue
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['rewardValue'] = undefined;

/**
 * Seller.
 * @member {String} seller
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['seller'] = undefined;

/**
 * Sellers involved in the chain. The list should contain only one seller, unless it is a [Multilevel Omnichannel Inventory](https://help.vtex.com/pt/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4) order.
 * @member {Array.<String>} sellerChain
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['sellerChain'] = undefined;

/**
 * Selling price in cents. Note that this field may be subject to rounding discrepancies. We recommend retrieving data from the `priceDefinition` data structure instead.
 * @member {Number} sellingPrice
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['sellingPrice'] = undefined;

/**
 * SKU name.
 * @member {String} skuName
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['skuName'] = undefined;

/**
 * Tax value in cents.
 * @member {Number} tax
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['tax'] = undefined;

/**
 * Unique ID.
 * @member {String} uniqueId
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['uniqueId'] = undefined;

/**
 * Unit multiplier
 * @member {Number} unitMultiplier
 */
PlaceOrder200ResponseOrdersInnerItemsInner.prototype['unitMultiplier'] = undefined;






export default PlaceOrder200ResponseOrdersInnerItemsInner;

