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
import BankAccountAllOfLinks from './BankAccountAllOfLinks';
import LeadSourceData from './LeadSourceData';

/**
 * The LeadSource model module.
 * @module model/LeadSource
 * @version 2.1
 */
class LeadSource {
    /**
     * Constructs a new <code>LeadSource</code>.
     * @alias module:model/LeadSource
     * @implements module:model/LeadSourceData
     */
    constructor() { 
        LeadSourceData.initialize(this);
        LeadSource.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>LeadSource</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/LeadSource} obj Optional instance to populate.
     * @return {module:model/LeadSource} The populated <code>LeadSource</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new LeadSource();
            LeadSourceData.constructFromObject(data, obj);

            if (data.hasOwnProperty('_links')) {
                obj['_links'] = ApiClient.convertToType(data['_links'], [BankAccountAllOfLinks]);
            }
            if (data.hasOwnProperty('affiliate')) {
                obj['affiliate'] = ApiClient.convertToType(data['affiliate'], 'String');
            }
            if (data.hasOwnProperty('campaign')) {
                obj['campaign'] = ApiClient.convertToType(data['campaign'], 'String');
            }
            if (data.hasOwnProperty('clickId')) {
                obj['clickId'] = ApiClient.convertToType(data['clickId'], 'String');
            }
            if (data.hasOwnProperty('content')) {
                obj['content'] = ApiClient.convertToType(data['content'], 'String');
            }
            if (data.hasOwnProperty('createdTime')) {
                obj['createdTime'] = ApiClient.convertToType(data['createdTime'], 'Date');
            }
            if (data.hasOwnProperty('medium')) {
                obj['medium'] = ApiClient.convertToType(data['medium'], 'String');
            }
            if (data.hasOwnProperty('path')) {
                obj['path'] = ApiClient.convertToType(data['path'], 'String');
            }
            if (data.hasOwnProperty('referrer')) {
                obj['referrer'] = ApiClient.convertToType(data['referrer'], 'String');
            }
            if (data.hasOwnProperty('salesAgent')) {
                obj['salesAgent'] = ApiClient.convertToType(data['salesAgent'], 'String');
            }
            if (data.hasOwnProperty('source')) {
                obj['source'] = ApiClient.convertToType(data['source'], 'String');
            }
            if (data.hasOwnProperty('subAffiliate')) {
                obj['subAffiliate'] = ApiClient.convertToType(data['subAffiliate'], 'String');
            }
            if (data.hasOwnProperty('term')) {
                obj['term'] = ApiClient.convertToType(data['term'], 'String');
            }
            if (data.hasOwnProperty('original')) {
                obj['original'] = ApiClient.convertToType(data['original'], LeadSourceData);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>LeadSource</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>LeadSource</code>.
     */
    static validateJSON(data) {
        if (data['_links']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['_links'])) {
                throw new Error("Expected the field `_links` to be an array in the JSON data but got " + data['_links']);
            }
            // validate the optional field `_links` (array)
            for (const item of data['_links']) {
                BankAccountAllOfLinks.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['affiliate'] && !(typeof data['affiliate'] === 'string' || data['affiliate'] instanceof String)) {
            throw new Error("Expected the field `affiliate` to be a primitive type in the JSON string but got " + data['affiliate']);
        }
        // ensure the json data is a string
        if (data['campaign'] && !(typeof data['campaign'] === 'string' || data['campaign'] instanceof String)) {
            throw new Error("Expected the field `campaign` to be a primitive type in the JSON string but got " + data['campaign']);
        }
        // ensure the json data is a string
        if (data['clickId'] && !(typeof data['clickId'] === 'string' || data['clickId'] instanceof String)) {
            throw new Error("Expected the field `clickId` to be a primitive type in the JSON string but got " + data['clickId']);
        }
        // ensure the json data is a string
        if (data['content'] && !(typeof data['content'] === 'string' || data['content'] instanceof String)) {
            throw new Error("Expected the field `content` to be a primitive type in the JSON string but got " + data['content']);
        }
        // ensure the json data is a string
        if (data['medium'] && !(typeof data['medium'] === 'string' || data['medium'] instanceof String)) {
            throw new Error("Expected the field `medium` to be a primitive type in the JSON string but got " + data['medium']);
        }
        // ensure the json data is a string
        if (data['path'] && !(typeof data['path'] === 'string' || data['path'] instanceof String)) {
            throw new Error("Expected the field `path` to be a primitive type in the JSON string but got " + data['path']);
        }
        // ensure the json data is a string
        if (data['referrer'] && !(typeof data['referrer'] === 'string' || data['referrer'] instanceof String)) {
            throw new Error("Expected the field `referrer` to be a primitive type in the JSON string but got " + data['referrer']);
        }
        // ensure the json data is a string
        if (data['salesAgent'] && !(typeof data['salesAgent'] === 'string' || data['salesAgent'] instanceof String)) {
            throw new Error("Expected the field `salesAgent` to be a primitive type in the JSON string but got " + data['salesAgent']);
        }
        // ensure the json data is a string
        if (data['source'] && !(typeof data['source'] === 'string' || data['source'] instanceof String)) {
            throw new Error("Expected the field `source` to be a primitive type in the JSON string but got " + data['source']);
        }
        // ensure the json data is a string
        if (data['subAffiliate'] && !(typeof data['subAffiliate'] === 'string' || data['subAffiliate'] instanceof String)) {
            throw new Error("Expected the field `subAffiliate` to be a primitive type in the JSON string but got " + data['subAffiliate']);
        }
        // ensure the json data is a string
        if (data['term'] && !(typeof data['term'] === 'string' || data['term'] instanceof String)) {
            throw new Error("Expected the field `term` to be a primitive type in the JSON string but got " + data['term']);
        }
        // validate the optional field `original`
        if (data['original']) { // data not null
          LeadSourceData.validateJSON(data['original']);
        }

        return true;
    }


}



/**
 * The links related to resource.
 * @member {Array.<module:model/BankAccountAllOfLinks>} _links
 */
LeadSource.prototype['_links'] = undefined;

/**
 * Lead source affiliate (eg 123, Bob Smith).
 * @member {String} affiliate
 */
LeadSource.prototype['affiliate'] = undefined;

/**
 * Lead source campaign (eg go-big-123).
 * @member {String} campaign
 */
LeadSource.prototype['campaign'] = undefined;

/**
 * Lead source click id (may come from an ad server).
 * @member {String} clickId
 */
LeadSource.prototype['clickId'] = undefined;

/**
 * Lead source content (eg smiley faces).
 * @member {String} content
 */
LeadSource.prototype['content'] = undefined;

/**
 * Lead source created time.
 * @member {Date} createdTime
 */
LeadSource.prototype['createdTime'] = undefined;

/**
 * Lead source medium (eg search, display).
 * @member {String} medium
 */
LeadSource.prototype['medium'] = undefined;

/**
 * Lead source path url (eg www.example.com/some/landing/path).
 * @member {String} path
 */
LeadSource.prototype['path'] = undefined;

/**
 * Lead source [`referer` url](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer) as determined (eg www.example.com/some/landing/path).
 * @member {String} referrer
 */
LeadSource.prototype['referrer'] = undefined;

/**
 * Lead source sales agent (eg James Bond).
 * @member {String} salesAgent
 */
LeadSource.prototype['salesAgent'] = undefined;

/**
 * Lead source origin (eg google, yahoo).
 * @member {String} source
 */
LeadSource.prototype['source'] = undefined;

/**
 * Lead source sub-affiliate also called a sub-id or click id in some circles (eg 123456).
 * @member {String} subAffiliate
 */
LeadSource.prototype['subAffiliate'] = undefined;

/**
 * Lead source term (eg salt shakers).
 * @member {String} term
 */
LeadSource.prototype['term'] = undefined;

/**
 * @member {module:model/LeadSourceData} original
 */
LeadSource.prototype['original'] = undefined;


// Implement LeadSourceData interface:
/**
 * The links related to resource.
 * @member {Array.<module:model/BankAccountAllOfLinks>} _links
 */
LeadSourceData.prototype['_links'] = undefined;
/**
 * Lead source affiliate (eg 123, Bob Smith).
 * @member {String} affiliate
 */
LeadSourceData.prototype['affiliate'] = undefined;
/**
 * Lead source campaign (eg go-big-123).
 * @member {String} campaign
 */
LeadSourceData.prototype['campaign'] = undefined;
/**
 * Lead source click id (may come from an ad server).
 * @member {String} clickId
 */
LeadSourceData.prototype['clickId'] = undefined;
/**
 * Lead source content (eg smiley faces).
 * @member {String} content
 */
LeadSourceData.prototype['content'] = undefined;
/**
 * Lead source created time.
 * @member {Date} createdTime
 */
LeadSourceData.prototype['createdTime'] = undefined;
/**
 * Lead source medium (eg search, display).
 * @member {String} medium
 */
LeadSourceData.prototype['medium'] = undefined;
/**
 * Lead source path url (eg www.example.com/some/landing/path).
 * @member {String} path
 */
LeadSourceData.prototype['path'] = undefined;
/**
 * Lead source [`referer` url](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer) as determined (eg www.example.com/some/landing/path).
 * @member {String} referrer
 */
LeadSourceData.prototype['referrer'] = undefined;
/**
 * Lead source sales agent (eg James Bond).
 * @member {String} salesAgent
 */
LeadSourceData.prototype['salesAgent'] = undefined;
/**
 * Lead source origin (eg google, yahoo).
 * @member {String} source
 */
LeadSourceData.prototype['source'] = undefined;
/**
 * Lead source sub-affiliate also called a sub-id or click id in some circles (eg 123456).
 * @member {String} subAffiliate
 */
LeadSourceData.prototype['subAffiliate'] = undefined;
/**
 * Lead source term (eg salt shakers).
 * @member {String} term
 */
LeadSourceData.prototype['term'] = undefined;




export default LeadSource;

