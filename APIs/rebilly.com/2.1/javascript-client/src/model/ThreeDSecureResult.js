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

/**
 * The ThreeDSecureResult model module.
 * @module model/ThreeDSecureResult
 * @version 2.1
 */
class ThreeDSecureResult {
    /**
     * Constructs a new <code>ThreeDSecureResult</code>.
     * @alias module:model/ThreeDSecureResult
     * @param authenticated {module:model/ThreeDSecureResult.AuthenticatedEnum} 3D Secure authentication response status.
     * @param enrolled {module:model/ThreeDSecureResult.EnrolledEnum} Is the cardholder enrolled in 3D Secure.
     * @param isDowngraded {Boolean} If 3D Secure 2 was attempted but downgraded to 3D Secure 1.
     * @param liability {module:model/ThreeDSecureResult.LiabilityEnum} 
     */
    constructor(authenticated, enrolled, isDowngraded, liability) { 
        
        ThreeDSecureResult.initialize(this, authenticated, enrolled, isDowngraded, liability);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, authenticated, enrolled, isDowngraded, liability) { 
        obj['authenticated'] = authenticated;
        obj['enrolled'] = enrolled;
        obj['isDowngraded'] = isDowngraded || false;
        obj['liability'] = liability;
    }

    /**
     * Constructs a <code>ThreeDSecureResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ThreeDSecureResult} obj Optional instance to populate.
     * @return {module:model/ThreeDSecureResult} The populated <code>ThreeDSecureResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ThreeDSecureResult();

            if (data.hasOwnProperty('authenticated')) {
                obj['authenticated'] = ApiClient.convertToType(data['authenticated'], 'String');
            }
            if (data.hasOwnProperty('enrolled')) {
                obj['enrolled'] = ApiClient.convertToType(data['enrolled'], 'String');
            }
            if (data.hasOwnProperty('flow')) {
                obj['flow'] = ApiClient.convertToType(data['flow'], 'String');
            }
            if (data.hasOwnProperty('isDowngraded')) {
                obj['isDowngraded'] = ApiClient.convertToType(data['isDowngraded'], 'Boolean');
            }
            if (data.hasOwnProperty('liability')) {
                obj['liability'] = ApiClient.convertToType(data['liability'], 'String');
            }
            if (data.hasOwnProperty('version')) {
                obj['version'] = ApiClient.convertToType(data['version'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ThreeDSecureResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ThreeDSecureResult</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ThreeDSecureResult.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['authenticated'] && !(typeof data['authenticated'] === 'string' || data['authenticated'] instanceof String)) {
            throw new Error("Expected the field `authenticated` to be a primitive type in the JSON string but got " + data['authenticated']);
        }
        // ensure the json data is a string
        if (data['enrolled'] && !(typeof data['enrolled'] === 'string' || data['enrolled'] instanceof String)) {
            throw new Error("Expected the field `enrolled` to be a primitive type in the JSON string but got " + data['enrolled']);
        }
        // ensure the json data is a string
        if (data['flow'] && !(typeof data['flow'] === 'string' || data['flow'] instanceof String)) {
            throw new Error("Expected the field `flow` to be a primitive type in the JSON string but got " + data['flow']);
        }
        // ensure the json data is a string
        if (data['liability'] && !(typeof data['liability'] === 'string' || data['liability'] instanceof String)) {
            throw new Error("Expected the field `liability` to be a primitive type in the JSON string but got " + data['liability']);
        }
        // ensure the json data is a string
        if (data['version'] && !(typeof data['version'] === 'string' || data['version'] instanceof String)) {
            throw new Error("Expected the field `version` to be a primitive type in the JSON string but got " + data['version']);
        }

        return true;
    }


}

ThreeDSecureResult.RequiredProperties = ["authenticated", "enrolled", "isDowngraded", "liability"];

/**
 * 3D Secure authentication response status.
 * @member {module:model/ThreeDSecureResult.AuthenticatedEnum} authenticated
 */
ThreeDSecureResult.prototype['authenticated'] = undefined;

/**
 * Is the cardholder enrolled in 3D Secure.
 * @member {module:model/ThreeDSecureResult.EnrolledEnum} enrolled
 */
ThreeDSecureResult.prototype['enrolled'] = undefined;

/**
 * 3D Secure 2 authentication flow.
 * @member {module:model/ThreeDSecureResult.FlowEnum} flow
 */
ThreeDSecureResult.prototype['flow'] = undefined;

/**
 * If 3D Secure 2 was attempted but downgraded to 3D Secure 1.
 * @member {Boolean} isDowngraded
 * @default false
 */
ThreeDSecureResult.prototype['isDowngraded'] = false;

/**
 * @member {module:model/ThreeDSecureResult.LiabilityEnum} liability
 */
ThreeDSecureResult.prototype['liability'] = undefined;

/**
 * 3D Secure version.
 * @member {module:model/ThreeDSecureResult.VersionEnum} version
 */
ThreeDSecureResult.prototype['version'] = undefined;





/**
 * Allowed values for the <code>authenticated</code> property.
 * @enum {String}
 * @readonly
 */
ThreeDSecureResult['AuthenticatedEnum'] = {

    /**
     * value: "true"
     * @const
     */
    "true": "true",

    /**
     * value: "false"
     * @const
     */
    "false": "false",

    /**
     * value: "not applicable"
     * @const
     */
    "not applicable": "not applicable",

    /**
     * value: "attempted"
     * @const
     */
    "attempted": "attempted"
};


/**
 * Allowed values for the <code>enrolled</code> property.
 * @enum {String}
 * @readonly
 */
ThreeDSecureResult['EnrolledEnum'] = {

    /**
     * value: "true"
     * @const
     */
    "true": "true",

    /**
     * value: "false"
     * @const
     */
    "false": "false",

    /**
     * value: "invalid card/timeout"
     * @const
     */
    "invalid card/timeout": "invalid card/timeout",

    /**
     * value: "unavailable"
     * @const
     */
    "unavailable": "unavailable"
};


/**
 * Allowed values for the <code>flow</code> property.
 * @enum {String}
 * @readonly
 */
ThreeDSecureResult['FlowEnum'] = {

    /**
     * value: "frictionless"
     * @const
     */
    "frictionless": "frictionless",

    /**
     * value: "challenge"
     * @const
     */
    "challenge": "challenge"
};


/**
 * Allowed values for the <code>liability</code> property.
 * @enum {String}
 * @readonly
 */
ThreeDSecureResult['LiabilityEnum'] = {

    /**
     * value: "protected"
     * @const
     */
    "protected": "protected",

    /**
     * value: "not protected"
     * @const
     */
    "not protected": "not protected",

    /**
     * value: "protected (attempt)"
     * @const
     */
    "protected (attempt)": "protected (attempt)"
};


/**
 * Allowed values for the <code>version</code> property.
 * @enum {String}
 * @readonly
 */
ThreeDSecureResult['VersionEnum'] = {

    /**
     * value: "1.0.2"
     * @const
     */
    "1.0.2": "1.0.2",

    /**
     * value: "2.1.0"
     * @const
     */
    "2.1.0": "2.1.0",

    /**
     * value: "2.2.0"
     * @const
     */
    "2.2.0": "2.2.0"
};



export default ThreeDSecureResult;

