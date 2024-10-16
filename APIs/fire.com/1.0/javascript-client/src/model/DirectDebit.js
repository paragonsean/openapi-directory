/**
 * Fire Financial Services Business API
 * The fire.com API allows you to deeply integrate Business Account features into your application or back-office systems.  The API provides read access to your profile, accounts and transactions, event-driven notifications of activity on the account and payment initiation via batches. Each feature has its own HTTP endpoint and every endpoint has its own permission.   The API exposes 3 main areas of functionality: financial functions, service information and service configuration. ## Financial Functions These functions provide access to your account details, transactions, payee accounts, payment initiation etc. ## Service Functions These provide information about the fees and limits applied to your account. ## Service configuration These provide information about your service configs - applications, webhooks, API tokens, etc. 
 *
 * The version of the OpenAPI document: 1.0
 * Contact: api@fire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Currency from './Currency';

/**
 * The DirectDebit model module.
 * @module model/DirectDebit
 * @version 1.0
 */
class DirectDebit {
    /**
     * Constructs a new <code>DirectDebit</code>.
     * @alias module:model/DirectDebit
     */
    constructor() { 
        
        DirectDebit.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DirectDebit</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DirectDebit} obj Optional instance to populate.
     * @return {module:model/DirectDebit} The populated <code>DirectDebit</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DirectDebit();

            if (data.hasOwnProperty('amount')) {
                obj['amount'] = ApiClient.convertToType(data['amount'], 'Number');
            }
            if (data.hasOwnProperty('currency')) {
                obj['currency'] = Currency.constructFromObject(data['currency']);
            }
            if (data.hasOwnProperty('dateCreated')) {
                obj['dateCreated'] = ApiClient.convertToType(data['dateCreated'], 'Date');
            }
            if (data.hasOwnProperty('directDebitReference')) {
                obj['directDebitReference'] = ApiClient.convertToType(data['directDebitReference'], 'String');
            }
            if (data.hasOwnProperty('directDebitUuid')) {
                obj['directDebitUuid'] = ApiClient.convertToType(data['directDebitUuid'], 'String');
            }
            if (data.hasOwnProperty('isDDIC')) {
                obj['isDDIC'] = ApiClient.convertToType(data['isDDIC'], 'Boolean');
            }
            if (data.hasOwnProperty('lastUpdated')) {
                obj['lastUpdated'] = ApiClient.convertToType(data['lastUpdated'], 'Date');
            }
            if (data.hasOwnProperty('mandateUUid')) {
                obj['mandateUUid'] = ApiClient.convertToType(data['mandateUUid'], 'String');
            }
            if (data.hasOwnProperty('originatorAlias')) {
                obj['originatorAlias'] = ApiClient.convertToType(data['originatorAlias'], 'String');
            }
            if (data.hasOwnProperty('originatorName')) {
                obj['originatorName'] = ApiClient.convertToType(data['originatorName'], 'String');
            }
            if (data.hasOwnProperty('originatorReference')) {
                obj['originatorReference'] = ApiClient.convertToType(data['originatorReference'], 'String');
            }
            if (data.hasOwnProperty('schemeRejectReason')) {
                obj['schemeRejectReason'] = ApiClient.convertToType(data['schemeRejectReason'], 'String');
            }
            if (data.hasOwnProperty('schemeRejectReasonCode')) {
                obj['schemeRejectReasonCode'] = ApiClient.convertToType(data['schemeRejectReasonCode'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('targetIcan')) {
                obj['targetIcan'] = ApiClient.convertToType(data['targetIcan'], 'Number');
            }
            if (data.hasOwnProperty('targetPayeeId')) {
                obj['targetPayeeId'] = ApiClient.convertToType(data['targetPayeeId'], 'Number');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DirectDebit</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DirectDebit</code>.
     */
    static validateJSON(data) {
        // validate the optional field `currency`
        if (data['currency']) { // data not null
          Currency.validateJSON(data['currency']);
        }
        // ensure the json data is a string
        if (data['directDebitReference'] && !(typeof data['directDebitReference'] === 'string' || data['directDebitReference'] instanceof String)) {
            throw new Error("Expected the field `directDebitReference` to be a primitive type in the JSON string but got " + data['directDebitReference']);
        }
        // ensure the json data is a string
        if (data['directDebitUuid'] && !(typeof data['directDebitUuid'] === 'string' || data['directDebitUuid'] instanceof String)) {
            throw new Error("Expected the field `directDebitUuid` to be a primitive type in the JSON string but got " + data['directDebitUuid']);
        }
        // ensure the json data is a string
        if (data['mandateUUid'] && !(typeof data['mandateUUid'] === 'string' || data['mandateUUid'] instanceof String)) {
            throw new Error("Expected the field `mandateUUid` to be a primitive type in the JSON string but got " + data['mandateUUid']);
        }
        // ensure the json data is a string
        if (data['originatorAlias'] && !(typeof data['originatorAlias'] === 'string' || data['originatorAlias'] instanceof String)) {
            throw new Error("Expected the field `originatorAlias` to be a primitive type in the JSON string but got " + data['originatorAlias']);
        }
        // ensure the json data is a string
        if (data['originatorName'] && !(typeof data['originatorName'] === 'string' || data['originatorName'] instanceof String)) {
            throw new Error("Expected the field `originatorName` to be a primitive type in the JSON string but got " + data['originatorName']);
        }
        // ensure the json data is a string
        if (data['originatorReference'] && !(typeof data['originatorReference'] === 'string' || data['originatorReference'] instanceof String)) {
            throw new Error("Expected the field `originatorReference` to be a primitive type in the JSON string but got " + data['originatorReference']);
        }
        // ensure the json data is a string
        if (data['schemeRejectReason'] && !(typeof data['schemeRejectReason'] === 'string' || data['schemeRejectReason'] instanceof String)) {
            throw new Error("Expected the field `schemeRejectReason` to be a primitive type in the JSON string but got " + data['schemeRejectReason']);
        }
        // ensure the json data is a string
        if (data['schemeRejectReasonCode'] && !(typeof data['schemeRejectReasonCode'] === 'string' || data['schemeRejectReasonCode'] instanceof String)) {
            throw new Error("Expected the field `schemeRejectReasonCode` to be a primitive type in the JSON string but got " + data['schemeRejectReasonCode']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * Value of the payment
 * @member {Number} amount
 */
DirectDebit.prototype['amount'] = undefined;

/**
 * @member {module:model/Currency} currency
 */
DirectDebit.prototype['currency'] = undefined;

/**
 * Date the direct debit was created. Milliseconds since the epoch (1970).
 * @member {Date} dateCreated
 */
DirectDebit.prototype['dateCreated'] = undefined;

/**
 * The direct debit reference.
 * @member {String} directDebitReference
 */
DirectDebit.prototype['directDebitReference'] = undefined;

/**
 * The UUID for the direct debit payment
 * @member {String} directDebitUuid
 */
DirectDebit.prototype['directDebitUuid'] = undefined;

/**
 * DDIC is a Direct Debit Indemnity Claim (i.e.a refund). If if the DD is requested to be refunded it is marked isDDIC true.
 * @member {Boolean} isDDIC
 */
DirectDebit.prototype['isDDIC'] = undefined;

/**
 * Date the direct debit was last updated. Milliseconds since the epoch (1970).
 * @member {Date} lastUpdated
 */
DirectDebit.prototype['lastUpdated'] = undefined;

/**
 * The UUID for the mandate
 * @member {String} mandateUUid
 */
DirectDebit.prototype['mandateUUid'] = undefined;

/**
 * The Alias of the party who sets up the direct debit.
 * @member {String} originatorAlias
 */
DirectDebit.prototype['originatorAlias'] = undefined;

/**
 * The creator of the party who sets up the direct debit.
 * @member {String} originatorName
 */
DirectDebit.prototype['originatorName'] = undefined;

/**
 * Set by party who sets up the direct debit.
 * @member {String} originatorReference
 */
DirectDebit.prototype['originatorReference'] = undefined;

/**
 * Reason why rejected
 * @member {String} schemeRejectReason
 */
DirectDebit.prototype['schemeRejectReason'] = undefined;

/**
 * The reject code returned by the bank indicating an issue with the direct debit. Each ARRUD code represents a rejection reason.
 * @member {module:model/DirectDebit.SchemeRejectReasonCodeEnum} schemeRejectReasonCode
 */
DirectDebit.prototype['schemeRejectReasonCode'] = undefined;

/**
 * The statuses of the direct debit payments associated with the mandate. * 'RECIEVED' - Direct Debit has been recieved * 'REJECT_REQUESTED' - The direct debit has a rejected request associated with it * 'REJECT_READY_FOR_PROCESSING'  * 'REJECT_RECORD_IN_PROGRESS' * 'REJECT_RECORDED' * 'REJECT_FILE_CREATED' * 'REJECT_FILE_SENT' * 'COLLECTED' - Direct debit collected * 'REFUND_REQUESTED' - Refund requested on direct debit * 'REFUND_RECORD_IN_PROGRESS' - Refund in progress on direct debit * 'REFUND_RECORDED' * 'REFUND_FILE_CREATED' * 'REFUND_FILE_SENT'  
 * @member {module:model/DirectDebit.StatusEnum} status
 */
DirectDebit.prototype['status'] = undefined;

/**
 * The ican of your fire account that the money was taken from
 * @member {Number} targetIcan
 */
DirectDebit.prototype['targetIcan'] = undefined;

/**
 * The payee that was created when the DD was processed
 * @member {Number} targetPayeeId
 */
DirectDebit.prototype['targetPayeeId'] = undefined;

/**
 * The type of the direct debit.
 * @member {module:model/DirectDebit.TypeEnum} type
 */
DirectDebit.prototype['type'] = undefined;





/**
 * Allowed values for the <code>schemeRejectReasonCode</code> property.
 * @enum {String}
 * @readonly
 */
DirectDebit['SchemeRejectReasonCodeEnum'] = {

    /**
     * value: "0"
     * @const
     */
    "0": "0",

    /**
     * value: "1"
     * @const
     */
    "1": "1",

    /**
     * value: "2"
     * @const
     */
    "2": "2",

    /**
     * value: "3"
     * @const
     */
    "3": "3",

    /**
     * value: "4"
     * @const
     */
    "4": "4",

    /**
     * value: "5"
     * @const
     */
    "5": "5",

    /**
     * value: "6"
     * @const
     */
    "6": "6",

    /**
     * value: "7"
     * @const
     */
    "7": "7",

    /**
     * value: "8"
     * @const
     */
    "8": "8",

    /**
     * value: "9"
     * @const
     */
    "9": "9",

    /**
     * value: "A"
     * @const
     */
    "A": "A",

    /**
     * value: "B"
     * @const
     */
    "B": "B"
};


/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
DirectDebit['StatusEnum'] = {

    /**
     * value: "RECIEVED"
     * @const
     */
    "RECIEVED": "RECIEVED",

    /**
     * value: "REJECT_REQUESTED"
     * @const
     */
    "REJECT_REQUESTED": "REJECT_REQUESTED",

    /**
     * value: "REJECT_READY_FOR_PROCESSING"
     * @const
     */
    "REJECT_READY_FOR_PROCESSING": "REJECT_READY_FOR_PROCESSING",

    /**
     * value: "REJECT_RECORD_IN_PROGRESS"
     * @const
     */
    "REJECT_RECORD_IN_PROGRESS": "REJECT_RECORD_IN_PROGRESS",

    /**
     * value: "REJECT_RECORDED"
     * @const
     */
    "REJECT_RECORDED": "REJECT_RECORDED",

    /**
     * value: "REJECT_FILE_CREATED"
     * @const
     */
    "REJECT_FILE_CREATED": "REJECT_FILE_CREATED",

    /**
     * value: "REJECT_FILE_SENT"
     * @const
     */
    "REJECT_FILE_SENT": "REJECT_FILE_SENT",

    /**
     * value: "COLLECTED"
     * @const
     */
    "COLLECTED": "COLLECTED",

    /**
     * value: "REFUND_REQUESTED"
     * @const
     */
    "REFUND_REQUESTED": "REFUND_REQUESTED",

    /**
     * value: "REFUND_RECORD_IN_PROGRESS"
     * @const
     */
    "REFUND_RECORD_IN_PROGRESS": "REFUND_RECORD_IN_PROGRESS",

    /**
     * value: "REFUND_RECORDED"
     * @const
     */
    "REFUND_RECORDED": "REFUND_RECORDED",

    /**
     * value: "REFUND_FILE_CREATED"
     * @const
     */
    "REFUND_FILE_CREATED": "REFUND_FILE_CREATED",

    /**
     * value: "REFUND_FILE_SENT"
     * @const
     */
    "REFUND_FILE_SENT": "REFUND_FILE_SENT"
};


/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
DirectDebit['TypeEnum'] = {

    /**
     * value: "FIRST_COLLECTION"
     * @const
     */
    "FIRST_COLLECTION": "FIRST_COLLECTION",

    /**
     * value: "ONGOING_COLLECTION"
     * @const
     */
    "ONGOING_COLLECTION": "ONGOING_COLLECTION",

    /**
     * value: "REPRESENTED_COLLECTION"
     * @const
     */
    "REPRESENTED_COLLECTION": "REPRESENTED_COLLECTION",

    /**
     * value: "FINAL_COLLECTION"
     * @const
     */
    "FINAL_COLLECTION": "FINAL_COLLECTION"
};



export default DirectDebit;

