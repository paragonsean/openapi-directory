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
import Amount from './Amount';
import AuthenticationObject from './AuthenticationObject';
import ChallengeData from './ChallengeData';
import LinksPaymentInitiation from './LinksPaymentInitiation';
import TppMessage2XX from './TppMessage2XX';
import TransactionStatus from './TransactionStatus';

/**
 * The PaymentInitationRequestResponse201 model module.
 * @module model/PaymentInitationRequestResponse201
 * @version 1.3.8_2020-12-14 - Swiss edition 1.3.8.1-CH
 */
class PaymentInitationRequestResponse201 {
    /**
     * Constructs a new <code>PaymentInitationRequestResponse201</code>.
     * Body of the response for a successful payment initiation request.
     * @alias module:model/PaymentInitationRequestResponse201
     * @param links {module:model/LinksPaymentInitiation} 
     * @param paymentId {String} Resource identification of the generated payment initiation resource.
     * @param transactionStatus {module:model/TransactionStatus} 
     */
    constructor(links, paymentId, transactionStatus) { 
        
        PaymentInitationRequestResponse201.initialize(this, links, paymentId, transactionStatus);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, links, paymentId, transactionStatus) { 
        obj['_links'] = links;
        obj['paymentId'] = paymentId;
        obj['transactionStatus'] = transactionStatus;
    }

    /**
     * Constructs a <code>PaymentInitationRequestResponse201</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PaymentInitationRequestResponse201} obj Optional instance to populate.
     * @return {module:model/PaymentInitationRequestResponse201} The populated <code>PaymentInitationRequestResponse201</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PaymentInitationRequestResponse201();

            if (data.hasOwnProperty('_links')) {
                obj['_links'] = LinksPaymentInitiation.constructFromObject(data['_links']);
            }
            if (data.hasOwnProperty('challengeData')) {
                obj['challengeData'] = ChallengeData.constructFromObject(data['challengeData']);
            }
            if (data.hasOwnProperty('chosenScaMethod')) {
                obj['chosenScaMethod'] = AuthenticationObject.constructFromObject(data['chosenScaMethod']);
            }
            if (data.hasOwnProperty('currencyConversionFee')) {
                obj['currencyConversionFee'] = Amount.constructFromObject(data['currencyConversionFee']);
            }
            if (data.hasOwnProperty('estimatedInterbankSettlementAmount')) {
                obj['estimatedInterbankSettlementAmount'] = Amount.constructFromObject(data['estimatedInterbankSettlementAmount']);
            }
            if (data.hasOwnProperty('estimatedTotalAmount')) {
                obj['estimatedTotalAmount'] = Amount.constructFromObject(data['estimatedTotalAmount']);
            }
            if (data.hasOwnProperty('paymentId')) {
                obj['paymentId'] = ApiClient.convertToType(data['paymentId'], 'String');
            }
            if (data.hasOwnProperty('psuMessage')) {
                obj['psuMessage'] = ApiClient.convertToType(data['psuMessage'], 'String');
            }
            if (data.hasOwnProperty('scaMethods')) {
                obj['scaMethods'] = ApiClient.convertToType(data['scaMethods'], [AuthenticationObject]);
            }
            if (data.hasOwnProperty('tppMessages')) {
                obj['tppMessages'] = ApiClient.convertToType(data['tppMessages'], [TppMessage2XX]);
            }
            if (data.hasOwnProperty('transactionFeeIndicator')) {
                obj['transactionFeeIndicator'] = ApiClient.convertToType(data['transactionFeeIndicator'], 'Boolean');
            }
            if (data.hasOwnProperty('transactionFees')) {
                obj['transactionFees'] = Amount.constructFromObject(data['transactionFees']);
            }
            if (data.hasOwnProperty('transactionStatus')) {
                obj['transactionStatus'] = TransactionStatus.constructFromObject(data['transactionStatus']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PaymentInitationRequestResponse201</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PaymentInitationRequestResponse201</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PaymentInitationRequestResponse201.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `challengeData`
        if (data['challengeData']) { // data not null
          ChallengeData.validateJSON(data['challengeData']);
        }
        // validate the optional field `chosenScaMethod`
        if (data['chosenScaMethod']) { // data not null
          AuthenticationObject.validateJSON(data['chosenScaMethod']);
        }
        // validate the optional field `currencyConversionFee`
        if (data['currencyConversionFee']) { // data not null
          Amount.validateJSON(data['currencyConversionFee']);
        }
        // validate the optional field `estimatedInterbankSettlementAmount`
        if (data['estimatedInterbankSettlementAmount']) { // data not null
          Amount.validateJSON(data['estimatedInterbankSettlementAmount']);
        }
        // validate the optional field `estimatedTotalAmount`
        if (data['estimatedTotalAmount']) { // data not null
          Amount.validateJSON(data['estimatedTotalAmount']);
        }
        // ensure the json data is a string
        if (data['paymentId'] && !(typeof data['paymentId'] === 'string' || data['paymentId'] instanceof String)) {
            throw new Error("Expected the field `paymentId` to be a primitive type in the JSON string but got " + data['paymentId']);
        }
        // ensure the json data is a string
        if (data['psuMessage'] && !(typeof data['psuMessage'] === 'string' || data['psuMessage'] instanceof String)) {
            throw new Error("Expected the field `psuMessage` to be a primitive type in the JSON string but got " + data['psuMessage']);
        }
        if (data['scaMethods']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['scaMethods'])) {
                throw new Error("Expected the field `scaMethods` to be an array in the JSON data but got " + data['scaMethods']);
            }
            // validate the optional field `scaMethods` (array)
            for (const item of data['scaMethods']) {
                AuthenticationObject.validateJSON(item);
            };
        }
        if (data['tppMessages']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['tppMessages'])) {
                throw new Error("Expected the field `tppMessages` to be an array in the JSON data but got " + data['tppMessages']);
            }
            // validate the optional field `tppMessages` (array)
            for (const item of data['tppMessages']) {
                TppMessage2XX.validateJSON(item);
            };
        }
        // validate the optional field `transactionFees`
        if (data['transactionFees']) { // data not null
          Amount.validateJSON(data['transactionFees']);
        }

        return true;
    }


}

PaymentInitationRequestResponse201.RequiredProperties = ["_links", "paymentId", "transactionStatus"];

/**
 * @member {module:model/LinksPaymentInitiation} _links
 */
PaymentInitationRequestResponse201.prototype['_links'] = undefined;

/**
 * @member {module:model/ChallengeData} challengeData
 */
PaymentInitationRequestResponse201.prototype['challengeData'] = undefined;

/**
 * @member {module:model/AuthenticationObject} chosenScaMethod
 */
PaymentInitationRequestResponse201.prototype['chosenScaMethod'] = undefined;

/**
 * @member {module:model/Amount} currencyConversionFee
 */
PaymentInitationRequestResponse201.prototype['currencyConversionFee'] = undefined;

/**
 * @member {module:model/Amount} estimatedInterbankSettlementAmount
 */
PaymentInitationRequestResponse201.prototype['estimatedInterbankSettlementAmount'] = undefined;

/**
 * @member {module:model/Amount} estimatedTotalAmount
 */
PaymentInitationRequestResponse201.prototype['estimatedTotalAmount'] = undefined;

/**
 * Resource identification of the generated payment initiation resource.
 * @member {String} paymentId
 */
PaymentInitationRequestResponse201.prototype['paymentId'] = undefined;

/**
 * Text to be displayed to the PSU.
 * @member {String} psuMessage
 */
PaymentInitationRequestResponse201.prototype['psuMessage'] = undefined;

/**
 * This data element might be contained, if SCA is required and if the PSU has a choice between different authentication methods.  Depending on the risk management of the ASPSP this choice might be offered before or after the PSU has been identified with the first relevant factor, or if an access token is transported.  If this data element is contained, then there is also a hyperlink of type 'startAuthorisationWithAuthenticationMethodSelection' contained in the response body.  These methods shall be presented towards the PSU for selection by the TPP. 
 * @member {Array.<module:model/AuthenticationObject>} scaMethods
 */
PaymentInitationRequestResponse201.prototype['scaMethods'] = undefined;

/**
 * @member {Array.<module:model/TppMessage2XX>} tppMessages
 */
PaymentInitationRequestResponse201.prototype['tppMessages'] = undefined;

/**
 * If equals 'true', the transaction will involve specific transaction cost as shown by the ASPSP in their public price list or as agreed between ASPSP and PSU. If equals 'false', the transaction will not involve additional specific transaction costs to the PSU unless the fee amount is given specifically in the data elements transactionFees and/or currencyConversionFees. If this data element is not used, there is no information about transaction fees unless the fee amount is given explicitly in the data element transactionFees and/or currencyConversionFees. 
 * @member {Boolean} transactionFeeIndicator
 */
PaymentInitationRequestResponse201.prototype['transactionFeeIndicator'] = undefined;

/**
 * @member {module:model/Amount} transactionFees
 */
PaymentInitationRequestResponse201.prototype['transactionFees'] = undefined;

/**
 * @member {module:model/TransactionStatus} transactionStatus
 */
PaymentInitationRequestResponse201.prototype['transactionStatus'] = undefined;






export default PaymentInitationRequestResponse201;

