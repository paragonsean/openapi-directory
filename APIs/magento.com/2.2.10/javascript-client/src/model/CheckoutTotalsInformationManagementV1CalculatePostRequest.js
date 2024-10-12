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
import CheckoutDataTotalsInformationInterface from './CheckoutDataTotalsInformationInterface';

/**
 * The CheckoutTotalsInformationManagementV1CalculatePostRequest model module.
 * @module model/CheckoutTotalsInformationManagementV1CalculatePostRequest
 * @version 2.2.10
 */
class CheckoutTotalsInformationManagementV1CalculatePostRequest {
    /**
     * Constructs a new <code>CheckoutTotalsInformationManagementV1CalculatePostRequest</code>.
     * @alias module:model/CheckoutTotalsInformationManagementV1CalculatePostRequest
     * @param addressInformation {module:model/CheckoutDataTotalsInformationInterface} 
     */
    constructor(addressInformation) { 
        
        CheckoutTotalsInformationManagementV1CalculatePostRequest.initialize(this, addressInformation);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, addressInformation) { 
        obj['addressInformation'] = addressInformation;
    }

    /**
     * Constructs a <code>CheckoutTotalsInformationManagementV1CalculatePostRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CheckoutTotalsInformationManagementV1CalculatePostRequest} obj Optional instance to populate.
     * @return {module:model/CheckoutTotalsInformationManagementV1CalculatePostRequest} The populated <code>CheckoutTotalsInformationManagementV1CalculatePostRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CheckoutTotalsInformationManagementV1CalculatePostRequest();

            if (data.hasOwnProperty('addressInformation')) {
                obj['addressInformation'] = CheckoutDataTotalsInformationInterface.constructFromObject(data['addressInformation']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CheckoutTotalsInformationManagementV1CalculatePostRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CheckoutTotalsInformationManagementV1CalculatePostRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CheckoutTotalsInformationManagementV1CalculatePostRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `addressInformation`
        if (data['addressInformation']) { // data not null
          CheckoutDataTotalsInformationInterface.validateJSON(data['addressInformation']);
        }

        return true;
    }


}

CheckoutTotalsInformationManagementV1CalculatePostRequest.RequiredProperties = ["addressInformation"];

/**
 * @member {module:model/CheckoutDataTotalsInformationInterface} addressInformation
 */
CheckoutTotalsInformationManagementV1CalculatePostRequest.prototype['addressInformation'] = undefined;






export default CheckoutTotalsInformationManagementV1CalculatePostRequest;

