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
import AttachmentEmbeddedInner from './AttachmentEmbeddedInner';
import AttachmentLinksInner from './AttachmentLinksInner';

/**
 * The Attachment model module.
 * @module model/Attachment
 * @version 2.1
 */
class Attachment {
    /**
     * Constructs a new <code>Attachment</code>.
     * @alias module:model/Attachment
     * @param fileId {String} Linked File object id.
     * @param relatedId {String} Linked object Id.
     * @param relatedType {module:model/Attachment.RelatedTypeEnum} Linked object type.
     */
    constructor(fileId, relatedId, relatedType) { 
        
        Attachment.initialize(this, fileId, relatedId, relatedType);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, fileId, relatedId, relatedType) { 
        obj['fileId'] = fileId;
        obj['relatedId'] = relatedId;
        obj['relatedType'] = relatedType;
    }

    /**
     * Constructs a <code>Attachment</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Attachment} obj Optional instance to populate.
     * @return {module:model/Attachment} The populated <code>Attachment</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Attachment();

            if (data.hasOwnProperty('_embedded')) {
                obj['_embedded'] = ApiClient.convertToType(data['_embedded'], [AttachmentEmbeddedInner]);
            }
            if (data.hasOwnProperty('_links')) {
                obj['_links'] = ApiClient.convertToType(data['_links'], [AttachmentLinksInner]);
            }
            if (data.hasOwnProperty('createdTime')) {
                obj['createdTime'] = ApiClient.convertToType(data['createdTime'], 'Date');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('fileId')) {
                obj['fileId'] = ApiClient.convertToType(data['fileId'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('relatedId')) {
                obj['relatedId'] = ApiClient.convertToType(data['relatedId'], 'String');
            }
            if (data.hasOwnProperty('relatedType')) {
                obj['relatedType'] = ApiClient.convertToType(data['relatedType'], 'String');
            }
            if (data.hasOwnProperty('updatedTime')) {
                obj['updatedTime'] = ApiClient.convertToType(data['updatedTime'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Attachment</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Attachment</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Attachment.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['_embedded']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['_embedded'])) {
                throw new Error("Expected the field `_embedded` to be an array in the JSON data but got " + data['_embedded']);
            }
            // validate the optional field `_embedded` (array)
            for (const item of data['_embedded']) {
                AttachmentEmbeddedInner.validateJSON(item);
            };
        }
        if (data['_links']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['_links'])) {
                throw new Error("Expected the field `_links` to be an array in the JSON data but got " + data['_links']);
            }
            // validate the optional field `_links` (array)
            for (const item of data['_links']) {
                AttachmentLinksInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['fileId'] && !(typeof data['fileId'] === 'string' || data['fileId'] instanceof String)) {
            throw new Error("Expected the field `fileId` to be a primitive type in the JSON string but got " + data['fileId']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['relatedId'] && !(typeof data['relatedId'] === 'string' || data['relatedId'] instanceof String)) {
            throw new Error("Expected the field `relatedId` to be a primitive type in the JSON string but got " + data['relatedId']);
        }
        // ensure the json data is a string
        if (data['relatedType'] && !(typeof data['relatedType'] === 'string' || data['relatedType'] instanceof String)) {
            throw new Error("Expected the field `relatedType` to be a primitive type in the JSON string but got " + data['relatedType']);
        }

        return true;
    }


}

Attachment.RequiredProperties = ["fileId", "relatedId", "relatedType"];

/**
 * Any embedded objects available that are requested by the `expand` querystring parameter.
 * @member {Array.<module:model/AttachmentEmbeddedInner>} _embedded
 */
Attachment.prototype['_embedded'] = undefined;

/**
 * The links related to resource.
 * @member {Array.<module:model/AttachmentLinksInner>} _links
 */
Attachment.prototype['_links'] = undefined;

/**
 * Creation date/time.
 * @member {Date} createdTime
 */
Attachment.prototype['createdTime'] = undefined;

/**
 * The Attachment description.
 * @member {String} description
 */
Attachment.prototype['description'] = undefined;

/**
 * Linked File object id.
 * @member {String} fileId
 */
Attachment.prototype['fileId'] = undefined;

/**
 * The resource ID. Defaults to UUID v4.
 * @member {String} id
 */
Attachment.prototype['id'] = undefined;

/**
 * The Original Attachment name.
 * @member {String} name
 */
Attachment.prototype['name'] = undefined;

/**
 * Linked object Id.
 * @member {String} relatedId
 */
Attachment.prototype['relatedId'] = undefined;

/**
 * Linked object type.
 * @member {module:model/Attachment.RelatedTypeEnum} relatedType
 */
Attachment.prototype['relatedType'] = undefined;

/**
 * Latest update date/time.
 * @member {Date} updatedTime
 */
Attachment.prototype['updatedTime'] = undefined;





/**
 * Allowed values for the <code>relatedType</code> property.
 * @enum {String}
 * @readonly
 */
Attachment['RelatedTypeEnum'] = {

    /**
     * value: "customer"
     * @const
     */
    "customer": "customer",

    /**
     * value: "dispute"
     * @const
     */
    "dispute": "dispute",

    /**
     * value: "gateway-timeline-comment"
     * @const
     */
    "gateway-timeline-comment": "gateway-timeline-comment",

    /**
     * value: "invoice"
     * @const
     */
    "invoice": "invoice",

    /**
     * value: "organization"
     * @const
     */
    "organization": "organization",

    /**
     * value: "payment"
     * @const
     */
    "payment": "payment",

    /**
     * value: "plan"
     * @const
     */
    "plan": "plan",

    /**
     * value: "product"
     * @const
     */
    "product": "product",

    /**
     * value: "subscription"
     * @const
     */
    "subscription": "subscription",

    /**
     * value: "transaction"
     * @const
     */
    "transaction": "transaction",

    /**
     * value: "customer-timeline-comment"
     * @const
     */
    "customer-timeline-comment": "customer-timeline-comment",

    /**
     * value: "transaction-timeline-comment"
     * @const
     */
    "transaction-timeline-comment": "transaction-timeline-comment",

    /**
     * value: "order-timeline-comment"
     * @const
     */
    "order-timeline-comment": "order-timeline-comment"
};



export default Attachment;

