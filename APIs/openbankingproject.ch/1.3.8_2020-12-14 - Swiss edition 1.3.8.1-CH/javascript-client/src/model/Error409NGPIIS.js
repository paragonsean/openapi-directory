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
import LinksAll from './LinksAll';
import TppMessage409PIIS from './TppMessage409PIIS';

/**
 * The Error409NGPIIS model module.
 * @module model/Error409NGPIIS
 * @version 1.3.8_2020-12-14 - Swiss edition 1.3.8.1-CH
 */
class Error409NGPIIS {
    /**
     * Constructs a new <code>Error409NGPIIS</code>.
     * NextGen specific definition of reporting error information in case of a HTTP error code 409. 
     * @alias module:model/Error409NGPIIS
     */
    constructor() { 
        
        Error409NGPIIS.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Error409NGPIIS</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Error409NGPIIS} obj Optional instance to populate.
     * @return {module:model/Error409NGPIIS} The populated <code>Error409NGPIIS</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Error409NGPIIS();

            if (data.hasOwnProperty('_links')) {
                obj['_links'] = LinksAll.constructFromObject(data['_links']);
            }
            if (data.hasOwnProperty('tppMessages')) {
                obj['tppMessages'] = ApiClient.convertToType(data['tppMessages'], [TppMessage409PIIS]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Error409NGPIIS</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Error409NGPIIS</code>.
     */
    static validateJSON(data) {
        if (data['tppMessages']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['tppMessages'])) {
                throw new Error("Expected the field `tppMessages` to be an array in the JSON data but got " + data['tppMessages']);
            }
            // validate the optional field `tppMessages` (array)
            for (const item of data['tppMessages']) {
                TppMessage409PIIS.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {module:model/LinksAll} _links
 */
Error409NGPIIS.prototype['_links'] = undefined;

/**
 * @member {Array.<module:model/TppMessage409PIIS>} tppMessages
 */
Error409NGPIIS.prototype['tppMessages'] = undefined;






export default Error409NGPIIS;

