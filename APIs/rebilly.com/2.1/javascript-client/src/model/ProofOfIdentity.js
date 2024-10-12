/**
 * Rebilly REST API
 * # Introduction The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable resource URLs.  It returns HTTP response codes to indicate errors.  It also accepts and returns JSON in the HTTP body.  You can use your favorite HTTP/REST library for your programming language to use Rebilly's API, or you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php) and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).  We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com) is supported by an API which is documented and available for use so that you may automate any workflows necessary.  This document contains the most commonly integrated resources.  # Authentication  When you sign up for an account, you are given your first secret API key. You can generate additional API keys, and delete API keys (as you may need to rotate your keys in the future). You authenticate to the Rebilly API by providing your secret key in the request header.  Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key. - [Secret API key](#section/Authentication/SecretApiKey): used for requests made   from the server side. Never share these keys. Keep them guarded and secure. - [Publishable API key](#section/Authentication/PublishableApiKey): used for    requests from the client side. For now can only be used to create    a [Payment Token](#operation/PostToken) and    a [File token](#operation/PostFile). - [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.  Never share your secret keys. Keep them guarded and secure.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  # Errors Rebilly follow's the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Forbidden &lt;RedocResponse pointer={\"#/components/responses/Forbidden\"} /&gt;  ## Conflict &lt;RedocResponse pointer={\"#/components/responses/Conflict\"} /&gt;  ## NotFound &lt;RedocResponse pointer={\"#/components/responses/NotFound\"} /&gt;  ## Unauthorized &lt;RedocResponse pointer={\"#/components/responses/Unauthorized\"} /&gt;  ## ValidationError &lt;RedocResponse pointer={\"#/components/responses/ValidationError\"} /&gt;  # SDKs  Rebilly offers a Javascript SDK and a PHP SDK to help interact with the API.  However, no SDK is required to use the API.  Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),  a client-side iFrame-based solution to help create payment tokens while minimizing PCI DSS compliance burdens and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is interacting with the [payment tokens creation operation](#operation/PostToken).  ## Javascript SDK  Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks). SDK code examples are included in these docs.  ## PHP SDK For all PHP SDK examples provided in these docs you will need to configure the `$client`. You may do it like this:  ```php $client = new Rebilly\\Client([     'apiKey' =&gt; 'YourApiKeyHere',     'baseUrl' =&gt; 'https://api.rebilly.com', ]); ```  # Using filter with collections Rebilly provides collections filtering. You can use `?filter` param on collections to define which records should be shown in the response.  Here is filter format description:  - Fields and values in filter are separated with `:`: `?filter=firstName:John`.  - Sub-fields are separated with `.`: `?filter=billingAddress.country:US`.  - Multiple filters are separated with `;`: `?filter=firstName:John;lastName:Doe`. They will be joined with `AND` logic. In this example: `firstName:John` AND `lastName:Doe`.  - You can use multiple values using `,` as values separator: `?filter=firstName:John,Bob`. Multiple values specified for a field will be joined with `OR` logic. In this example: `firstName:John` OR `firstName:Bob`.  - To negate the filter use `!`: `?filter=firstName:!John`. Note that you can negate multiple values like this: `?filter=firstName:!John,!Bob`. This filter rule will exclude all Johns and Bobs from the response.  - You can use range filters like this: `?filter=amount:1..10`.  - You can use gte (greater than or equals) filter like this: `?filter=amount:1..`, or lte (less than or equals) than filter like this: `?filter=amount:..10`. This also works for datetime-based fields.  - You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: `?filter=firstName:@yourListName`. You can also exclude list values: `?filter=firstName:!@yourListName`.  - Datetime-based fields accept values formatted using RFC 3339 like this: `?filter=createdTime:2021-02-14T13:30:00Z`.   # Expand to include embedded objects Rebilly provides the ability to pre-load additional  objects with a request.   You can use `?expand` param on most requests to expand and include embedded objects within the `_embedded` property of the response.  The `_embedded` property contains an array of  objects keyed by the expand parameter value(s).  You may expand multiple objects by passing them as comma-separated to the expand value like so:  ``` ?expand=recentInvoice,customer ```  And in the response, you would see:  ``` \"_embedded\": [     \"recentInvoice\": {...},     \"customer\": {...} ] ``` Expand may be utilitized not only on `GET` requests but also on `PATCH`, `POST`, `PUT` requests too.   # Getting started guide  Rebilly's API has over 300 operations.  That's more than you'll  need to implement your use cases.  If you have a use  case you would like to implement, please consult us for feedback on the best API operations for the task.  Our getting started guide will demonstrate a basic order form use case.  It will allow us to highlight core resources in Rebilly that will be helpful for many other use cases too.  Within 25 minutes, you'll have sent API requests (via our console) to create a subscription order. 
 *
 * The version of the OpenAPI document: 2.1
 * Contact: integrations@rebilly.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import KycDocument from './KycDocument';
import KycDocumentRejection from './KycDocumentRejection';
import KycDocumentSubtypes from './KycDocumentSubtypes';
import KycDocumentTypes from './KycDocumentTypes';
import ProofOfIdentityAllOfDocumentMatches from './ProofOfIdentityAllOfDocumentMatches';
import ProofOfIdentityAllOfLinks from './ProofOfIdentityAllOfLinks';

/**
 * The ProofOfIdentity model module.
 * @module model/ProofOfIdentity
 * @version 2.1
 */
class ProofOfIdentity {
    /**
     * Constructs a new <code>ProofOfIdentity</code>.
     * @alias module:model/ProofOfIdentity
     * @implements module:model/KycDocument
     * @param documentType {module:model/KycDocumentTypes} Document type submitted for validation, only identity-proof type is analyzed in an automated manner.
     * @param status {module:model/ProofOfIdentity.StatusEnum} Status of the validation.
     * @param customerId {String} The сustomer's ID.
     */
    constructor(documentType, status, customerId) { 
        KycDocument.initialize(this, documentType, status, customerId);
        ProofOfIdentity.initialize(this, documentType, status, customerId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, documentType, status, customerId) { 
        obj['documentType'] = documentType;
        obj['status'] = status;
        obj['customerId'] = customerId;
    }

    /**
     * Constructs a <code>ProofOfIdentity</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ProofOfIdentity} obj Optional instance to populate.
     * @return {module:model/ProofOfIdentity} The populated <code>ProofOfIdentity</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ProofOfIdentity();
            KycDocument.constructFromObject(data, obj);

            if (data.hasOwnProperty('_links')) {
                obj['_links'] = ApiClient.convertToType(data['_links'], [ProofOfIdentityAllOfLinks]);
            }
            if (data.hasOwnProperty('createdTime')) {
                obj['createdTime'] = ApiClient.convertToType(data['createdTime'], 'Date');
            }
            if (data.hasOwnProperty('documentSubtype')) {
                obj['documentSubtype'] = ApiClient.convertToType(data['documentSubtype'], KycDocumentSubtypes);
            }
            if (data.hasOwnProperty('documentType')) {
                obj['documentType'] = ApiClient.convertToType(data['documentType'], KycDocumentTypes);
            }
            if (data.hasOwnProperty('fileId')) {
                obj['fileId'] = ApiClient.convertToType(data['fileId'], 'String');
            }
            if (data.hasOwnProperty('fileIds')) {
                obj['fileIds'] = ApiClient.convertToType(data['fileIds'], ['String']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('processedTime')) {
                obj['processedTime'] = ApiClient.convertToType(data['processedTime'], 'Date');
            }
            if (data.hasOwnProperty('rejectionReason')) {
                obj['rejectionReason'] = KycDocumentRejection.constructFromObject(data['rejectionReason']);
            }
            if (data.hasOwnProperty('requestId')) {
                obj['requestId'] = ApiClient.convertToType(data['requestId'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('updatedTime')) {
                obj['updatedTime'] = ApiClient.convertToType(data['updatedTime'], 'Date');
            }
            if (data.hasOwnProperty('customerId')) {
                obj['customerId'] = ApiClient.convertToType(data['customerId'], 'String');
            }
            if (data.hasOwnProperty('matchLevel')) {
                obj['matchLevel'] = ApiClient.convertToType(data['matchLevel'], 'Number');
            }
            if (data.hasOwnProperty('notes')) {
                obj['notes'] = ApiClient.convertToType(data['notes'], 'String');
            }
            if (data.hasOwnProperty('reason')) {
                obj['reason'] = ApiClient.convertToType(data['reason'], 'String');
            }
            if (data.hasOwnProperty('reviewTime')) {
                obj['reviewTime'] = ApiClient.convertToType(data['reviewTime'], 'Date');
            }
            if (data.hasOwnProperty('reviewerId')) {
                obj['reviewerId'] = ApiClient.convertToType(data['reviewerId'], 'String');
            }
            if (data.hasOwnProperty('reviewerName')) {
                obj['reviewerName'] = ApiClient.convertToType(data['reviewerName'], 'String');
            }
            if (data.hasOwnProperty('documentMatches')) {
                obj['documentMatches'] = ProofOfIdentityAllOfDocumentMatches.constructFromObject(data['documentMatches']);
            }
            if (data.hasOwnProperty('parsedData')) {
                obj['parsedData'] = ProofOfIdentityAllOfDocumentMatches.constructFromObject(data['parsedData']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ProofOfIdentity</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ProofOfIdentity</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ProofOfIdentity.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['_links']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['_links'])) {
                throw new Error("Expected the field `_links` to be an array in the JSON data but got " + data['_links']);
            }
            // validate the optional field `_links` (array)
            for (const item of data['_links']) {
                ProofOfIdentityAllOfLinks.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['fileId'] && !(typeof data['fileId'] === 'string' || data['fileId'] instanceof String)) {
            throw new Error("Expected the field `fileId` to be a primitive type in the JSON string but got " + data['fileId']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['fileIds'])) {
            throw new Error("Expected the field `fileIds` to be an array in the JSON data but got " + data['fileIds']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // validate the optional field `rejectionReason`
        if (data['rejectionReason']) { // data not null
          KycDocumentRejection.validateJSON(data['rejectionReason']);
        }
        // ensure the json data is a string
        if (data['requestId'] && !(typeof data['requestId'] === 'string' || data['requestId'] instanceof String)) {
            throw new Error("Expected the field `requestId` to be a primitive type in the JSON string but got " + data['requestId']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        // ensure the json data is a string
        if (data['customerId'] && !(typeof data['customerId'] === 'string' || data['customerId'] instanceof String)) {
            throw new Error("Expected the field `customerId` to be a primitive type in the JSON string but got " + data['customerId']);
        }
        // ensure the json data is a string
        if (data['notes'] && !(typeof data['notes'] === 'string' || data['notes'] instanceof String)) {
            throw new Error("Expected the field `notes` to be a primitive type in the JSON string but got " + data['notes']);
        }
        // ensure the json data is a string
        if (data['reason'] && !(typeof data['reason'] === 'string' || data['reason'] instanceof String)) {
            throw new Error("Expected the field `reason` to be a primitive type in the JSON string but got " + data['reason']);
        }
        // ensure the json data is a string
        if (data['reviewerId'] && !(typeof data['reviewerId'] === 'string' || data['reviewerId'] instanceof String)) {
            throw new Error("Expected the field `reviewerId` to be a primitive type in the JSON string but got " + data['reviewerId']);
        }
        // ensure the json data is a string
        if (data['reviewerName'] && !(typeof data['reviewerName'] === 'string' || data['reviewerName'] instanceof String)) {
            throw new Error("Expected the field `reviewerName` to be a primitive type in the JSON string but got " + data['reviewerName']);
        }
        // validate the optional field `documentMatches`
        if (data['documentMatches']) { // data not null
          ProofOfIdentityAllOfDocumentMatches.validateJSON(data['documentMatches']);
        }
        // validate the optional field `parsedData`
        if (data['parsedData']) { // data not null
          ProofOfIdentityAllOfDocumentMatches.validateJSON(data['parsedData']);
        }

        return true;
    }


}

ProofOfIdentity.RequiredProperties = ["documentType", "status", "customerId"];

/**
 * The links related to resource.
 * @member {Array.<module:model/ProofOfIdentityAllOfLinks>} _links
 */
ProofOfIdentity.prototype['_links'] = undefined;

/**
 * Creation date/time.
 * @member {Date} createdTime
 */
ProofOfIdentity.prototype['createdTime'] = undefined;

/**
 * Document subtype submitted for validation.
 * @member {module:model/KycDocumentSubtypes} documentSubtype
 */
ProofOfIdentity.prototype['documentSubtype'] = undefined;

/**
 * Document type submitted for validation, only identity-proof type is analyzed in an automated manner.
 * @member {module:model/KycDocumentTypes} documentType
 */
ProofOfIdentity.prototype['documentType'] = undefined;

/**
 * Linked file object id.
 * @member {String} fileId
 */
ProofOfIdentity.prototype['fileId'] = undefined;

/**
 * Linked file object id's.
 * @member {Array.<String>} fileIds
 */
ProofOfIdentity.prototype['fileIds'] = undefined;

/**
 * The resource ID. Defaults to UUID v4.
 * @member {String} id
 */
ProofOfIdentity.prototype['id'] = undefined;

/**
 * Processing date/time.
 * @member {Date} processedTime
 */
ProofOfIdentity.prototype['processedTime'] = undefined;

/**
 * @member {module:model/KycDocumentRejection} rejectionReason
 */
ProofOfIdentity.prototype['rejectionReason'] = undefined;

/**
 * KYC request identifier string.
 * @member {String} requestId
 */
ProofOfIdentity.prototype['requestId'] = undefined;

/**
 * Status of the validation.
 * @member {module:model/ProofOfIdentity.StatusEnum} status
 */
ProofOfIdentity.prototype['status'] = undefined;

/**
 * Latest update date/time.
 * @member {Date} updatedTime
 */
ProofOfIdentity.prototype['updatedTime'] = undefined;

/**
 * The сustomer's ID.
 * @member {String} customerId
 */
ProofOfIdentity.prototype['customerId'] = undefined;

/**
 * The level of strictness for the document matches.
 * @member {Number} matchLevel
 */
ProofOfIdentity.prototype['matchLevel'] = undefined;

/**
 * Reviewer notes.
 * @member {String} notes
 */
ProofOfIdentity.prototype['notes'] = undefined;

/**
 * Reason for uploading.
 * @member {String} reason
 */
ProofOfIdentity.prototype['reason'] = undefined;

/**
 * Date and time of manual review.
 * @member {Date} reviewTime
 */
ProofOfIdentity.prototype['reviewTime'] = undefined;

/**
 * Reviewer's user ID.
 * @member {String} reviewerId
 */
ProofOfIdentity.prototype['reviewerId'] = undefined;

/**
 * Reviewer's first and last name.
 * @member {String} reviewerName
 */
ProofOfIdentity.prototype['reviewerName'] = undefined;

/**
 * @member {module:model/ProofOfIdentityAllOfDocumentMatches} documentMatches
 */
ProofOfIdentity.prototype['documentMatches'] = undefined;

/**
 * @member {module:model/ProofOfIdentityAllOfDocumentMatches} parsedData
 */
ProofOfIdentity.prototype['parsedData'] = undefined;


// Implement KycDocument interface:
/**
 * The links related to resource.
 * @member {Array.<module:model/CommonKycDocumentLinksInner>} _links
 */
KycDocument.prototype['_links'] = undefined;
/**
 * Creation date/time.
 * @member {Date} createdTime
 */
KycDocument.prototype['createdTime'] = undefined;
/**
 * Document subtype submitted for validation.
 * @member {module:model/KycDocumentSubtypes} documentSubtype
 */
KycDocument.prototype['documentSubtype'] = undefined;
/**
 * Document type submitted for validation, only identity-proof type is analyzed in an automated manner.
 * @member {module:model/KycDocumentTypes} documentType
 */
KycDocument.prototype['documentType'] = undefined;
/**
 * Linked file object id.
 * @member {String} fileId
 */
KycDocument.prototype['fileId'] = undefined;
/**
 * Linked file object id's.
 * @member {Array.<String>} fileIds
 */
KycDocument.prototype['fileIds'] = undefined;
/**
 * The resource ID. Defaults to UUID v4.
 * @member {String} id
 */
KycDocument.prototype['id'] = undefined;
/**
 * Processing date/time.
 * @member {Date} processedTime
 */
KycDocument.prototype['processedTime'] = undefined;
/**
 * @member {module:model/KycDocumentRejection} rejectionReason
 */
KycDocument.prototype['rejectionReason'] = undefined;
/**
 * KYC request identifier string.
 * @member {String} requestId
 */
KycDocument.prototype['requestId'] = undefined;
/**
 * Status of the validation.
 * @member {module:model/KycDocument.StatusEnum} status
 */
KycDocument.prototype['status'] = undefined;
/**
 * Latest update date/time.
 * @member {Date} updatedTime
 */
KycDocument.prototype['updatedTime'] = undefined;
/**
 * The сustomer's ID.
 * @member {String} customerId
 */
KycDocument.prototype['customerId'] = undefined;
/**
 * The level of strictness for the document matches.
 * @member {Number} matchLevel
 */
KycDocument.prototype['matchLevel'] = undefined;
/**
 * Reviewer notes.
 * @member {String} notes
 */
KycDocument.prototype['notes'] = undefined;
/**
 * Reason for uploading.
 * @member {String} reason
 */
KycDocument.prototype['reason'] = undefined;
/**
 * Date and time of manual review.
 * @member {Date} reviewTime
 */
KycDocument.prototype['reviewTime'] = undefined;
/**
 * Reviewer's user ID.
 * @member {String} reviewerId
 */
KycDocument.prototype['reviewerId'] = undefined;
/**
 * Reviewer's first and last name.
 * @member {String} reviewerName
 */
KycDocument.prototype['reviewerName'] = undefined;



/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
ProofOfIdentity['StatusEnum'] = {

    /**
     * value: "pending"
     * @const
     */
    "pending": "pending",

    /**
     * value: "in-progress"
     * @const
     */
    "in-progress": "in-progress",

    /**
     * value: "accepted"
     * @const
     */
    "accepted": "accepted",

    /**
     * value: "rejected"
     * @const
     */
    "rejected": "rejected"
};



export default ProofOfIdentity;

