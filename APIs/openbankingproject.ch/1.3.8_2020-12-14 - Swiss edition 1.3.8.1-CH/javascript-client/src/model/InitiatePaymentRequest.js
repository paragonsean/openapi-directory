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
import AccountReference16CH from './AccountReference16CH';
import Address from './Address';
import Amount from './Amount';
import BulkPaymentInitiationJson from './BulkPaymentInitiationJson';
import ChargeBearer from './ChargeBearer';
import CreditorAgent7CH from './CreditorAgent7CH';
import DayOfExecution from './DayOfExecution';
import DebtorAgent7CH from './DebtorAgent7CH';
import ExchangeRateInformation1 from './ExchangeRateInformation1';
import ExecutionRule from './ExecutionRule';
import ExternalServiceLevel1Code from './ExternalServiceLevel1Code';
import FrequencyCode from './FrequencyCode';
import PaymentInitiationBulkElementJson from './PaymentInitiationBulkElementJson';
import PaymentInitiationJson from './PaymentInitiationJson';
import PeriodicPaymentInitiationJson from './PeriodicPaymentInitiationJson';
import PurposeCode from './PurposeCode';
import RemittanceInformationStructured from './RemittanceInformationStructured';

/**
 * The InitiatePaymentRequest model module.
 * @module model/InitiatePaymentRequest
 * @version 1.3.8_2020-12-14 - Swiss edition 1.3.8.1-CH
 */
class InitiatePaymentRequest {
    /**
     * Constructs a new <code>InitiatePaymentRequest</code>.
     * @alias module:model/InitiatePaymentRequest
     * @param {(module:model/BulkPaymentInitiationJson|module:model/PaymentInitiationJson|module:model/PeriodicPaymentInitiationJson)} instance The actual instance to initialize InitiatePaymentRequest.
     */
    constructor(instance = null) {
        if (instance === null) {
            this.actualInstance = null;
            return;
        }
        var match = 0;
        var errorMessages = [];
        try {
            if (typeof instance === "PaymentInitiationJson") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                PaymentInitiationJson.validateJSON(instance); // throw an exception if no match
                // create PaymentInitiationJson from JS object
                this.actualInstance = PaymentInitiationJson.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into PaymentInitiationJson
            errorMessages.push("Failed to construct PaymentInitiationJson: " + err)
        }

        try {
            if (typeof instance === "PeriodicPaymentInitiationJson") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                PeriodicPaymentInitiationJson.validateJSON(instance); // throw an exception if no match
                // create PeriodicPaymentInitiationJson from JS object
                this.actualInstance = PeriodicPaymentInitiationJson.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into PeriodicPaymentInitiationJson
            errorMessages.push("Failed to construct PeriodicPaymentInitiationJson: " + err)
        }

        try {
            if (typeof instance === "BulkPaymentInitiationJson") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                BulkPaymentInitiationJson.validateJSON(instance); // throw an exception if no match
                // create BulkPaymentInitiationJson from JS object
                this.actualInstance = BulkPaymentInitiationJson.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into BulkPaymentInitiationJson
            errorMessages.push("Failed to construct BulkPaymentInitiationJson: " + err)
        }

        if (match > 1) {
            throw new Error("Multiple matches found constructing `InitiatePaymentRequest` with oneOf schemas BulkPaymentInitiationJson, PaymentInitiationJson, PeriodicPaymentInitiationJson. Input: " + JSON.stringify(instance));
        } else if (match === 0) {
            this.actualInstance = null; // clear the actual instance in case there are multiple matches
            throw new Error("No match found constructing `InitiatePaymentRequest` with oneOf schemas BulkPaymentInitiationJson, PaymentInitiationJson, PeriodicPaymentInitiationJson. Details: " +
                            errorMessages.join(", "));
        } else { // only 1 match
            // the input is valid
        }
    }

    /**
     * Constructs a <code>InitiatePaymentRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/InitiatePaymentRequest} obj Optional instance to populate.
     * @return {module:model/InitiatePaymentRequest} The populated <code>InitiatePaymentRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        return new InitiatePaymentRequest(data);
    }

    /**
     * Gets the actual instance, which can be <code>BulkPaymentInitiationJson</code>, <code>PaymentInitiationJson</code>, <code>PeriodicPaymentInitiationJson</code>.
     * @return {(module:model/BulkPaymentInitiationJson|module:model/PaymentInitiationJson|module:model/PeriodicPaymentInitiationJson)} The actual instance.
     */
    getActualInstance() {
        return this.actualInstance;
    }

    /**
     * Sets the actual instance, which can be <code>BulkPaymentInitiationJson</code>, <code>PaymentInitiationJson</code>, <code>PeriodicPaymentInitiationJson</code>.
     * @param {(module:model/BulkPaymentInitiationJson|module:model/PaymentInitiationJson|module:model/PeriodicPaymentInitiationJson)} obj The actual instance.
     */
    setActualInstance(obj) {
       this.actualInstance = InitiatePaymentRequest.constructFromObject(obj).getActualInstance();
    }

    /**
     * Returns the JSON representation of the actual instance.
     * @return {string}
     */
    toJSON = function(){
        return this.getActualInstance();
    }

    /**
     * Create an instance of InitiatePaymentRequest from a JSON string.
     * @param {string} json_string JSON string.
     * @return {module:model/InitiatePaymentRequest} An instance of InitiatePaymentRequest.
     */
    static fromJSON = function(json_string){
        return InitiatePaymentRequest.constructFromObject(JSON.parse(json_string));
    }
}

/**
 * @member {module:model/ChargeBearer} chargeBearer
 */
InitiatePaymentRequest.prototype['chargeBearer'] = undefined;

/**
 * @member {module:model/AccountReference16CH} creditorAccount
 */
InitiatePaymentRequest.prototype['creditorAccount'] = undefined;

/**
 * @member {module:model/Address} creditorAddress
 */
InitiatePaymentRequest.prototype['creditorAddress'] = undefined;

/**
 * @member {module:model/CreditorAgent7CH} creditorAgent
 */
InitiatePaymentRequest.prototype['creditorAgent'] = undefined;

/**
 * Creditor agent name.
 * @member {String} creditorAgentName
 */
InitiatePaymentRequest.prototype['creditorAgentName'] = undefined;

/**
 * Identification of Creditors, e.g. a SEPA Creditor ID.
 * @member {String} creditorId
 */
InitiatePaymentRequest.prototype['creditorId'] = undefined;

/**
 * Creditor name.
 * @member {String} creditorName
 */
InitiatePaymentRequest.prototype['creditorName'] = undefined;

/**
 * Creditor Name and Address in a free text field.
 * @member {String} creditorNameAndAddress
 */
InitiatePaymentRequest.prototype['creditorNameAndAddress'] = undefined;

/**
 * @member {module:model/AccountReference16CH} debtorAccount
 */
InitiatePaymentRequest.prototype['debtorAccount'] = undefined;

/**
 * @member {module:model/DebtorAgent7CH} debtorAgent
 */
InitiatePaymentRequest.prototype['debtorAgent'] = undefined;

/**
 * Debtor Id.
 * @member {String} debtorId
 */
InitiatePaymentRequest.prototype['debtorId'] = undefined;

/**
 * Debtor name.
 * @member {String} debtorName
 */
InitiatePaymentRequest.prototype['debtorName'] = undefined;

/**
 * @member {String} endToEndIdentification
 */
InitiatePaymentRequest.prototype['endToEndIdentification'] = undefined;

/**
 * @member {module:model/Amount} equivalentAmount
 */
InitiatePaymentRequest.prototype['equivalentAmount'] = undefined;

/**
 * @member {module:model/ExchangeRateInformation1} exchangeRateInformation
 */
InitiatePaymentRequest.prototype['exchangeRateInformation'] = undefined;

/**
 * @member {module:model/Amount} instructedAmount
 */
InitiatePaymentRequest.prototype['instructedAmount'] = undefined;

/**
 * BICFI 
 * @member {String} intermediaryAgent
 */
InitiatePaymentRequest.prototype['intermediaryAgent'] = undefined;

/**
 * @member {module:model/PurposeCode} purposeCode
 */
InitiatePaymentRequest.prototype['purposeCode'] = undefined;

/**
 * @member {module:model/RemittanceInformationStructured} remittanceInformationStructured
 */
InitiatePaymentRequest.prototype['remittanceInformationStructured'] = undefined;

/**
 * Unstructured remittance information. 
 * @member {String} remittanceInformationUnstructured
 */
InitiatePaymentRequest.prototype['remittanceInformationUnstructured'] = undefined;

/**
 * @member {Date} requestedExecutionDate
 */
InitiatePaymentRequest.prototype['requestedExecutionDate'] = undefined;

/**
 * @member {module:model/ExternalServiceLevel1Code} serviceLevel
 */
InitiatePaymentRequest.prototype['serviceLevel'] = undefined;

/**
 * ISO 4217 Alpha 3 currency code. 
 * @member {String} transactionCurrency
 */
InitiatePaymentRequest.prototype['transactionCurrency'] = undefined;

/**
 * Ultimate creditor.
 * @member {String} ultimateCreditor
 */
InitiatePaymentRequest.prototype['ultimateCreditor'] = undefined;

/**
 * Ultimate debtor.
 * @member {String} ultimateDebtor
 */
InitiatePaymentRequest.prototype['ultimateDebtor'] = undefined;

/**
 * @member {module:model/DayOfExecution} dayOfExecution
 */
InitiatePaymentRequest.prototype['dayOfExecution'] = undefined;

/**
 * The last applicable day of execution. If not given, it is an infinite standing order. 
 * @member {Date} endDate
 */
InitiatePaymentRequest.prototype['endDate'] = undefined;

/**
 * @member {module:model/ExecutionRule} executionRule
 */
InitiatePaymentRequest.prototype['executionRule'] = undefined;

/**
 * @member {module:model/FrequencyCode} frequency
 */
InitiatePaymentRequest.prototype['frequency'] = undefined;

/**
 * The first applicable day of execution starting from this date is the first payment. 
 * @member {Date} startDate
 */
InitiatePaymentRequest.prototype['startDate'] = undefined;

/**
 * If this element equals 'true', the PSU prefers only one booking entry. If this element equals 'false', the PSU prefers individual booking of all contained individual transactions.  The ASPSP will follow this preference according to contracts agreed on with the PSU. 
 * @member {Boolean} batchBookingPreferred
 */
InitiatePaymentRequest.prototype['batchBookingPreferred'] = undefined;

/**
 * A list of generic JSON bodies payment initations for bulk payments via JSON.  Note: Some fields from single payments do not occcur in a bulk payment element 
 * @member {Array.<module:model/PaymentInitiationBulkElementJson>} payments
 */
InitiatePaymentRequest.prototype['payments'] = undefined;

/**
 * @member {Date} requestedExecutionTime
 */
InitiatePaymentRequest.prototype['requestedExecutionTime'] = undefined;


InitiatePaymentRequest.OneOf = ["BulkPaymentInitiationJson", "PaymentInitiationJson", "PeriodicPaymentInitiationJson"];

export default InitiatePaymentRequest;

