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
import PaymentConfiguration from './PaymentConfiguration';
import UpdateorderFormconfigurationRequestAppsInner from './UpdateorderFormconfigurationRequestAppsInner';
import UpdateorderFormconfigurationRequestTaxConfiguration from './UpdateorderFormconfigurationRequestTaxConfiguration';

/**
 * The UpdateorderFormconfigurationRequest model module.
 * @module model/UpdateorderFormconfigurationRequest
 * @version 1.0
 */
class UpdateorderFormconfigurationRequest {
    /**
     * Constructs a new <code>UpdateorderFormconfigurationRequest</code>.
     * @alias module:model/UpdateorderFormconfigurationRequest
     * @param allowManualPrice {Boolean} Allows the editing of SKU prices right in the cart.
     * @param allowMultipleDeliveries {Boolean} On the same purchase, allows the selection of items from multiple delivery channels.
     * @param apps {Array.<module:model/UpdateorderFormconfigurationRequestAppsInner>} Array of objects containing Apps configuration information.
     * @param decimalDigitsPrecision {Number} Number of price digits.
     * @param minimumQuantityAccumulatedForItems {Number} Minimum SKU quantity by cart.
     * @param minimumValueAccumulated {Number} Minimum cart value.
     * @param paymentConfiguration {module:model/PaymentConfiguration} 
     * @param taxConfiguration {module:model/UpdateorderFormconfigurationRequestTaxConfiguration} 
     */
    constructor(allowManualPrice, allowMultipleDeliveries, apps, decimalDigitsPrecision, minimumQuantityAccumulatedForItems, minimumValueAccumulated, paymentConfiguration, taxConfiguration) { 
        
        UpdateorderFormconfigurationRequest.initialize(this, allowManualPrice, allowMultipleDeliveries, apps, decimalDigitsPrecision, minimumQuantityAccumulatedForItems, minimumValueAccumulated, paymentConfiguration, taxConfiguration);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, allowManualPrice, allowMultipleDeliveries, apps, decimalDigitsPrecision, minimumQuantityAccumulatedForItems, minimumValueAccumulated, paymentConfiguration, taxConfiguration) { 
        obj['allowManualPrice'] = allowManualPrice;
        obj['allowMultipleDeliveries'] = allowMultipleDeliveries;
        obj['apps'] = apps;
        obj['decimalDigitsPrecision'] = decimalDigitsPrecision;
        obj['minimumQuantityAccumulatedForItems'] = minimumQuantityAccumulatedForItems;
        obj['minimumValueAccumulated'] = minimumValueAccumulated;
        obj['paymentConfiguration'] = paymentConfiguration;
        obj['recaptchaValidation'] = 'vtexCriteria';
        obj['taxConfiguration'] = taxConfiguration;
    }

    /**
     * Constructs a <code>UpdateorderFormconfigurationRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateorderFormconfigurationRequest} obj Optional instance to populate.
     * @return {module:model/UpdateorderFormconfigurationRequest} The populated <code>UpdateorderFormconfigurationRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateorderFormconfigurationRequest();

            if (data.hasOwnProperty('allowManualPrice')) {
                obj['allowManualPrice'] = ApiClient.convertToType(data['allowManualPrice'], 'Boolean');
            }
            if (data.hasOwnProperty('allowMultipleDeliveries')) {
                obj['allowMultipleDeliveries'] = ApiClient.convertToType(data['allowMultipleDeliveries'], 'Boolean');
            }
            if (data.hasOwnProperty('apps')) {
                obj['apps'] = ApiClient.convertToType(data['apps'], [UpdateorderFormconfigurationRequestAppsInner]);
            }
            if (data.hasOwnProperty('decimalDigitsPrecision')) {
                obj['decimalDigitsPrecision'] = ApiClient.convertToType(data['decimalDigitsPrecision'], 'Number');
            }
            if (data.hasOwnProperty('maskFirstPurchaseData')) {
                obj['maskFirstPurchaseData'] = ApiClient.convertToType(data['maskFirstPurchaseData'], 'Boolean');
            }
            if (data.hasOwnProperty('maxNumberOfWhiteLabelSellers')) {
                obj['maxNumberOfWhiteLabelSellers'] = ApiClient.convertToType(data['maxNumberOfWhiteLabelSellers'], 'Number');
            }
            if (data.hasOwnProperty('minimumQuantityAccumulatedForItems')) {
                obj['minimumQuantityAccumulatedForItems'] = ApiClient.convertToType(data['minimumQuantityAccumulatedForItems'], 'Number');
            }
            if (data.hasOwnProperty('minimumValueAccumulated')) {
                obj['minimumValueAccumulated'] = ApiClient.convertToType(data['minimumValueAccumulated'], 'Number');
            }
            if (data.hasOwnProperty('paymentConfiguration')) {
                obj['paymentConfiguration'] = PaymentConfiguration.constructFromObject(data['paymentConfiguration']);
            }
            if (data.hasOwnProperty('paymentSystemToCheckFirstInstallment')) {
                obj['paymentSystemToCheckFirstInstallment'] = ApiClient.convertToType(data['paymentSystemToCheckFirstInstallment'], 'String');
            }
            if (data.hasOwnProperty('recaptchaValidation')) {
                obj['recaptchaValidation'] = ApiClient.convertToType(data['recaptchaValidation'], 'String');
            }
            if (data.hasOwnProperty('taxConfiguration')) {
                obj['taxConfiguration'] = UpdateorderFormconfigurationRequestTaxConfiguration.constructFromObject(data['taxConfiguration']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateorderFormconfigurationRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateorderFormconfigurationRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of UpdateorderFormconfigurationRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['apps']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['apps'])) {
                throw new Error("Expected the field `apps` to be an array in the JSON data but got " + data['apps']);
            }
            // validate the optional field `apps` (array)
            for (const item of data['apps']) {
                UpdateorderFormconfigurationRequestAppsInner.validateJSON(item);
            };
        }
        // validate the optional field `paymentConfiguration`
        if (data['paymentConfiguration']) { // data not null
          PaymentConfiguration.validateJSON(data['paymentConfiguration']);
        }
        // ensure the json data is a string
        if (data['paymentSystemToCheckFirstInstallment'] && !(typeof data['paymentSystemToCheckFirstInstallment'] === 'string' || data['paymentSystemToCheckFirstInstallment'] instanceof String)) {
            throw new Error("Expected the field `paymentSystemToCheckFirstInstallment` to be a primitive type in the JSON string but got " + data['paymentSystemToCheckFirstInstallment']);
        }
        // ensure the json data is a string
        if (data['recaptchaValidation'] && !(typeof data['recaptchaValidation'] === 'string' || data['recaptchaValidation'] instanceof String)) {
            throw new Error("Expected the field `recaptchaValidation` to be a primitive type in the JSON string but got " + data['recaptchaValidation']);
        }
        // validate the optional field `taxConfiguration`
        if (data['taxConfiguration']) { // data not null
          UpdateorderFormconfigurationRequestTaxConfiguration.validateJSON(data['taxConfiguration']);
        }

        return true;
    }


}

UpdateorderFormconfigurationRequest.RequiredProperties = ["allowManualPrice", "allowMultipleDeliveries", "apps", "decimalDigitsPrecision", "minimumQuantityAccumulatedForItems", "minimumValueAccumulated", "paymentConfiguration", "taxConfiguration"];

/**
 * Allows the editing of SKU prices right in the cart.
 * @member {Boolean} allowManualPrice
 */
UpdateorderFormconfigurationRequest.prototype['allowManualPrice'] = undefined;

/**
 * On the same purchase, allows the selection of items from multiple delivery channels.
 * @member {Boolean} allowMultipleDeliveries
 */
UpdateorderFormconfigurationRequest.prototype['allowMultipleDeliveries'] = undefined;

/**
 * Array of objects containing Apps configuration information.
 * @member {Array.<module:model/UpdateorderFormconfigurationRequestAppsInner>} apps
 */
UpdateorderFormconfigurationRequest.prototype['apps'] = undefined;

/**
 * Number of price digits.
 * @member {Number} decimalDigitsPrecision
 */
UpdateorderFormconfigurationRequest.prototype['decimalDigitsPrecision'] = undefined;

/**
 * Allows, on a first purchase, masking client's data. It could be useful when a shared cart is used and the client doesn't want to share its data.
 * @member {Boolean} maskFirstPurchaseData
 */
UpdateorderFormconfigurationRequest.prototype['maskFirstPurchaseData'] = undefined;

/**
 * Allows the input of a limit of white label sellers involved on the cart.
 * @member {Number} maxNumberOfWhiteLabelSellers
 */
UpdateorderFormconfigurationRequest.prototype['maxNumberOfWhiteLabelSellers'] = undefined;

/**
 * Minimum SKU quantity by cart.
 * @member {Number} minimumQuantityAccumulatedForItems
 */
UpdateorderFormconfigurationRequest.prototype['minimumQuantityAccumulatedForItems'] = undefined;

/**
 * Minimum cart value.
 * @member {Number} minimumValueAccumulated
 */
UpdateorderFormconfigurationRequest.prototype['minimumValueAccumulated'] = undefined;

/**
 * @member {module:model/PaymentConfiguration} paymentConfiguration
 */
UpdateorderFormconfigurationRequest.prototype['paymentConfiguration'] = undefined;

/**
 * If you want to apply a first installment discount to a particular payment system, set this field to that payment system's ID. Learn more: [Configuring a discount for orders prepaid in full](https://help.vtex.com/en/tutorial/configurar-desconto-de-preco-a-vista--7Lfcj9Wb5dpYfA2gKkACIt).
 * @member {String} paymentSystemToCheckFirstInstallment
 */
UpdateorderFormconfigurationRequest.prototype['paymentSystemToCheckFirstInstallment'] = undefined;

/**
 * Configures reCAPTCHA validation for the account, defining in which situations the shopper will be prompted to validate a purchase with reCAPTCHA. Learn more about [reCAPTCHA validation for VTEX stores](https://help.vtex.com/tutorial/recaptcha-no-checkout--18Te3oDd7f4qcjKu9jhNzP)    Possible values are:  - `\"never\"`: no purchases are validated with reCAPTCHA.  - `\"always\"`: every purchase is validated with reCAPTCHA.  - `\"vtexCriteria\"`: only some purchases are validated with reCAPTCHA in order to minimize friction and improve shopping experience. VTEX’s algorithm determines which sessions are trustworthy and which should be validated with reCAPTCHA. This is the recommended option.
 * @member {String} recaptchaValidation
 * @default 'vtexCriteria'
 */
UpdateorderFormconfigurationRequest.prototype['recaptchaValidation'] = 'vtexCriteria';

/**
 * @member {module:model/UpdateorderFormconfigurationRequestTaxConfiguration} taxConfiguration
 */
UpdateorderFormconfigurationRequest.prototype['taxConfiguration'] = undefined;






export default UpdateorderFormconfigurationRequest;

