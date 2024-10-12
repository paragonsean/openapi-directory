/**
 * Swiss NextGen Banking API-Framework
 * # Summary The **Swiss NextGen API** is based on the NextGenPSD2 *Framework Version 1.3.4* of the Berlin Group which offers a modern, open, harmonised and interoperable set of Application Programming Interfaces (APIs) as the safest and most efficient way to provide data securely. The NextGen Framework reduces XS2A complexity and costs, addresses the problem of multiple competing standards in Europe and, aligned with the goals of the Euro Retail Payments Board, enables European banking customers to benefit from innovative products and services ('Banking as a Service') by granting TPPs safe and secure (authenticated and authorised) access to their bank accounts and financial data.  The Swiss edtion refines the message formats specific to Switzerland and defines some matching examples.  The possible Approaches are:   * Redirect SCA Approach   * *(Not recommended by obp.ch community) OAuth SCA Approach*   * *(Not recommended by obp.ch community) Decoupled SCA Approach*   * *(Not recommended by obp.ch community) Embedded SCA Approach without SCA method*   * *(Not recommended by obp.ch community) Embedded SCA Approach with only one SCA method available*   * *(Not recommended by obp.ch community) Embedded SCA Approach with Selection of a SCA method*    Not every message defined in this API definition is necessary for all approaches.   Furthermore this API definition does not differ between methods which are mandatory, conditional, or optional   Therefore for a particular implementation of a compliant API it is only necessary to support   a certain subset of the methods defined in this API definition.    **Please have a look at the implementation guidelines if you are not sure   which message has to be used for the approach you are going to use.**  ## Some General Remarks Related to this version of the OpenAPI Specification: * **This API definition is based on the Implementation Guidelines of the [Berlin Group API](https://www.berlin-group.org/nextgenpsd2-downloads).**   It is not a replacement in any sense.   The main specification is (at the moment) always the Implementation Guidelines of the Berlin Group API. * **This API definition contains the REST-API for requests from the PISP to the ASPSP.** * **This API definition contains the messages for all different approaches defined in the Implementation Guidelines.** * According to the OpenAPI-Specification [https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.1.md]      \"If in is \"header\" and the name field is \"Accept\", \"Content-Type\" or \"Authorization\", the parameter definition SHALL be ignored.\"    The element \"Accept\" will not be defined in this file at any place.    The elements \"Content-Type\" and \"Authorization\" are implicitly defined by the OpenApi tags \"content\" and \"security\".  * There are several predefined types which might occur in payment initiation messages,   but are not used in the standard JSON messages in the Implementation Guidelines.   Therefore they are not used in the corresponding messages in this file either.   We added them for the convenience of the user.   If there is a payment product, which needs these fields, one can easily use the predefined types.   But the ASPSP need not to accept them in general.  * **We omit the definition of all standard HTTP header elements (mandatory/optional/conditional)   except they are mentioned in the Implementation Guidelines.**   Therefore the implementer might add these in his own realisation of a comlient API in addition to the elements defined in this file.  ## General Remarks on Data Types  The Berlin Group definition of UTF-8 strings in context of the API have to support at least the following characters  a b c d e f g h i j k l m n o p q r s t u v w x y z  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z  0 1 2 3 4 5 6 7 8 9  / - ? : ( ) . , ' +  Space 
 *
 * The version of the OpenAPI document: 1.3.8_2020-12-14 - Swiss edition 1.3.8.1-CH
 * Contact: info@obp.ch
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import CardTransaction from './CardTransaction';
import LinksCardAccountReport from './LinksCardAccountReport';

/**
 * The CardAccountReport model module.
 * @module model/CardAccountReport
 * @version 1.3.8_2020-12-14 - Swiss edition 1.3.8.1-CH
 */
class CardAccountReport {
    /**
     * Constructs a new <code>CardAccountReport</code>.
     * JSON based card account report.  This card account report contains transactions resulting from the query parameters. 
     * @alias module:model/CardAccountReport
     * @param links {module:model/LinksCardAccountReport} 
     * @param booked {Array.<module:model/CardTransaction>} Array of transaction details.
     */
    constructor(links, booked) { 
        
        CardAccountReport.initialize(this, links, booked);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, links, booked) { 
        obj['_links'] = links;
        obj['booked'] = booked;
    }

    /**
     * Constructs a <code>CardAccountReport</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CardAccountReport} obj Optional instance to populate.
     * @return {module:model/CardAccountReport} The populated <code>CardAccountReport</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CardAccountReport();

            if (data.hasOwnProperty('_links')) {
                obj['_links'] = LinksCardAccountReport.constructFromObject(data['_links']);
            }
            if (data.hasOwnProperty('booked')) {
                obj['booked'] = ApiClient.convertToType(data['booked'], [CardTransaction]);
            }
            if (data.hasOwnProperty('pending')) {
                obj['pending'] = ApiClient.convertToType(data['pending'], [CardTransaction]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CardAccountReport</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CardAccountReport</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CardAccountReport.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['booked']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['booked'])) {
                throw new Error("Expected the field `booked` to be an array in the JSON data but got " + data['booked']);
            }
            // validate the optional field `booked` (array)
            for (const item of data['booked']) {
                CardTransaction.validateJSON(item);
            };
        }
        if (data['pending']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['pending'])) {
                throw new Error("Expected the field `pending` to be an array in the JSON data but got " + data['pending']);
            }
            // validate the optional field `pending` (array)
            for (const item of data['pending']) {
                CardTransaction.validateJSON(item);
            };
        }

        return true;
    }


}

CardAccountReport.RequiredProperties = ["_links", "booked"];

/**
 * @member {module:model/LinksCardAccountReport} _links
 */
CardAccountReport.prototype['_links'] = undefined;

/**
 * Array of transaction details.
 * @member {Array.<module:model/CardTransaction>} booked
 */
CardAccountReport.prototype['booked'] = undefined;

/**
 * Array of transaction details.
 * @member {Array.<module:model/CardTransaction>} pending
 */
CardAccountReport.prototype['pending'] = undefined;






export default CardAccountReport;

