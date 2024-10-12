/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest model module.
 * @module model/NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest
 * @version 2.2.10
 */
class NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest {
    /**
     * Constructs a new <code>NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest</code>.
     * @alias module:model/NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest
     * @param shippingMethod {String} The shipping method code.
     */
    constructor(shippingMethod) { 
        
        NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest.initialize(this, shippingMethod);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, shippingMethod) { 
        obj['shippingMethod'] = shippingMethod;
    }

    /**
     * Constructs a <code>NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest} obj Optional instance to populate.
     * @return {module:model/NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest} The populated <code>NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest();

            if (data.hasOwnProperty('shippingMethod')) {
                obj['shippingMethod'] = ApiClient.convertToType(data['shippingMethod'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['shippingMethod'] && !(typeof data['shippingMethod'] === 'string' || data['shippingMethod'] instanceof String)) {
            throw new Error("Expected the field `shippingMethod` to be a primitive type in the JSON string but got " + data['shippingMethod']);
        }

        return true;
    }


}

NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest.RequiredProperties = ["shippingMethod"];

/**
 * The shipping method code.
 * @member {String} shippingMethod
 */
NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest.prototype['shippingMethod'] = undefined;






export default NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest;

