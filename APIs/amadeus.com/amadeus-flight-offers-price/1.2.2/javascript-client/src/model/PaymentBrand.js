/**
 * Flight Offers Price
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.2.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
/**
* Enum class PaymentBrand.
* @enum {}
* @readonly
*/
export default class PaymentBrand {
    
        /**
         * value: "VISA"
         * @const
         */
        "VISA" = "VISA";

    
        /**
         * value: "AMERICAN_EXPRESS"
         * @const
         */
        "AMERICAN_EXPRESS" = "AMERICAN_EXPRESS";

    
        /**
         * value: "MASTERCARD"
         * @const
         */
        "MASTERCARD" = "MASTERCARD";

    
        /**
         * value: "VISA_ELECTRON"
         * @const
         */
        "VISA_ELECTRON" = "VISA_ELECTRON";

    
        /**
         * value: "VISA_DEBIT"
         * @const
         */
        "VISA_DEBIT" = "VISA_DEBIT";

    
        /**
         * value: "MASTERCARD_DEBIT"
         * @const
         */
        "MASTERCARD_DEBIT" = "MASTERCARD_DEBIT";

    
        /**
         * value: "MAESTRO"
         * @const
         */
        "MAESTRO" = "MAESTRO";

    
        /**
         * value: "DINERS"
         * @const
         */
        "DINERS" = "DINERS";

    
        /**
         * value: "MASTERCARD_IXARIS"
         * @const
         */
        "MASTERCARD_IXARIS" = "MASTERCARD_IXARIS";

    
        /**
         * value: "VISA_IXARIS"
         * @const
         */
        "VISA_IXARIS" = "VISA_IXARIS";

    
        /**
         * value: "MASTERCARD_AIRPLUS"
         * @const
         */
        "MASTERCARD_AIRPLUS" = "MASTERCARD_AIRPLUS";

    
        /**
         * value: "UATP_AIRPLUS"
         * @const
         */
        "UATP_AIRPLUS" = "UATP_AIRPLUS";

    

    /**
    * Returns a <code>PaymentBrand</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/PaymentBrand} The enum <code>PaymentBrand</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

