/**
 * Flight Order Management
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
/**
* Enum class TravelerPricingFareOption.
* @enum {}
* @readonly
*/
export default class TravelerPricingFareOption {
    
        /**
         * value: "STANDARD"
         * @const
         */
        "STANDARD" = "STANDARD";

    
        /**
         * value: "INCLUSIVE_TOUR"
         * @const
         */
        "INCLUSIVE_TOUR" = "INCLUSIVE_TOUR";

    
        /**
         * value: "SPANISH_MELILLA_RESIDENT"
         * @const
         */
        "SPANISH_MELILLA_RESIDENT" = "SPANISH_MELILLA_RESIDENT";

    
        /**
         * value: "SPANISH_CEUTA_RESIDENT"
         * @const
         */
        "SPANISH_CEUTA_RESIDENT" = "SPANISH_CEUTA_RESIDENT";

    
        /**
         * value: "SPANISH_CANARY_RESIDENT"
         * @const
         */
        "SPANISH_CANARY_RESIDENT" = "SPANISH_CANARY_RESIDENT";

    
        /**
         * value: "SPANISH_BALEARIC_RESIDENT"
         * @const
         */
        "SPANISH_BALEARIC_RESIDENT" = "SPANISH_BALEARIC_RESIDENT";

    
        /**
         * value: "AIR_FRANCE_METROPOLITAN_DISCOUNT_PASS"
         * @const
         */
        "AIR_FRANCE_METROPOLITAN_DISCOUNT_PASS" = "AIR_FRANCE_METROPOLITAN_DISCOUNT_PASS";

    
        /**
         * value: "AIR_FRANCE_DOM_DISCOUNT_PASS"
         * @const
         */
        "AIR_FRANCE_DOM_DISCOUNT_PASS" = "AIR_FRANCE_DOM_DISCOUNT_PASS";

    
        /**
         * value: "AIR_FRANCE_COMBINED_DISCOUNT_PASS"
         * @const
         */
        "AIR_FRANCE_COMBINED_DISCOUNT_PASS" = "AIR_FRANCE_COMBINED_DISCOUNT_PASS";

    
        /**
         * value: "AIR_FRANCE_FAMILY"
         * @const
         */
        "AIR_FRANCE_FAMILY" = "AIR_FRANCE_FAMILY";

    
        /**
         * value: "ADULT_WITH_COMPANION"
         * @const
         */
        "ADULT_WITH_COMPANION" = "ADULT_WITH_COMPANION";

    
        /**
         * value: "COMPANION"
         * @const
         */
        "COMPANION" = "COMPANION";

    

    /**
    * Returns a <code>TravelerPricingFareOption</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/TravelerPricingFareOption} The enum <code>TravelerPricingFareOption</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

