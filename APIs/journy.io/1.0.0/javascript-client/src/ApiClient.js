/**
 * Developer documentation
 * # Welcome  Implementing a new tool can be daunting, but it doesn't have to. You can implement journy.io in a few different ways to ensure it fits with the rest of your tech stack seamlessly.  We welcome your feedback, ideas and suggestions. We really want to make your life easier, so if we’re falling short or should be doing something different, we want to hear about it. Send us an email at [hi@journy.io](mailto:hi@journy.io) or reach out via the chat on our website or on our platform.  There are multiple ways you can send us data about users and accounts. We have both frontend and backend APIs, which can be used together at the same time.  If you already use [Segment](https://segment.com/), you can [get up and running with journy.io in seconds](https://help.journy.io/en/articles/6488307-the-segment-connector).  # Concepts  ## Users  The most basic entity is a user, a specific individual that completed an interaction with your product.  We support multiple types of users, often differentiated by it's external ID prefix. E.g. In the case you are building an ordering app, there could easily be an administrator (who updates products and checks for orders) and the end-customers who place orders. One could have a typical ADM-XXXXXXXX ID, while the other would be referenced by USR-XXXXXXXXX.  ## Accounts  In B2B SaaS, users can be part of multiple accounts. E.g. Imagine you're building a content scheduling app where an agency can manage the social media posts of their clients. Each client of the agency has its own account in the product.  If your app doesn't have the concept of a team or group of users, you can ignore accounts.  ## Events  An event is a data point that represents an interaction between a user and/or an account; and your product. Events can represents any range of interactions. E.g. Every time a customer creates an invoice in an invoicing app. Actions like creating an invoice can be tracked as an event in journy.io.  It's critical to track events properly. You'll need to provide either an account ID, or a user ID, or both; when tracking an event. E.g. If a user updates his personal settings, you can omit the account ID as the event would not be related to any account. In a same logic, an account could get a 'suspend account' event (with account ID) from an internal process, whereas no user would be associated. In most cases, events will be associated to both 1 user and 1 account.  You can optionally pass extra details as metadata (e.g. amount of the invoice). This gets particarly powerfull when creating computed properties on those event metadata. E.g. Our above ordering app could send journy.io 'Place Order' events with metadata 'price', on which journy.io very easily would compute a total order value (for each account) for the last 30 days.  💡 Metadata does not update the properties of a user or account.  # Frontend vs backend  The best implementations we see employ a hybrid approach to maximize data quality while maintaining the flexibility to easily collect the data they need.  We recommend using our JavaScript snippet to track screen views and our backend API to sync users, sync accounts and track events.  When evaluating how to track a particular event, we suggest starting with server-side and only use frontend if it's not possible to collect purely server-side. This can be the case if you need to track interactions with your product that don't result in any natural server requests (such as a button click that opens a modal).  # Frontend  ## Setup  💡 You can find the JavaScript snippet in the website settings in the connections view.  Copy the JavaScript snippet and place it in the head or body of your application.  The snippet automatically calls `journy(\"init\", { ... })` and `journy(\"pageview\")`.  ## Identify user  💡 A user ID should be a robust, static, unique identifier that you recognize a user by in your own systems. Because these IDs are consistent across a customer’s lifetime, you should include a user ID in identify calls as often as you can. Ideally, the user ID should be a database ID.  💡 journy.io does not recommend using simple email addresses or usernames as user ID, as these can change over time. journy.io recommends that you use static IDs instead, so the IDs never change. When you use a static ID, you can still recognize the user in your analytics tools, even if the user changes their email address.  💡 The properties `full_name`, `first_name`, `last_name`, `phone` and `registered_at` will be used for creating contacts in destinations like Intercom, HubSpot, Salesforce, ...  `journy(\"identify\")` allows you to identify the user that is currently using your product.  ```ts journy(\"identify\", {   // Email or user ID is required   email: \"john.doe@acme.com\",   // Unique identifier for the user in your database   userId: \"20\",    // Optional   // Hash of the user ID using a backend secret   // You can find the secret in the website settings   // Recommended to prevent spoofing   verification: \"hash\",    // Optional   properties: {     full_name: \"John Doe\",     // or     first_name: \"John\",     last_name: \"Doe\",      phone: \"123\",     registered_at: new Date(/_* ... *_/),     is_admin: true,     key_with_empty_value: \"\",     this_property_will_be_deleted: null,   }, }); ```  ## Identify account  💡 An account ID should be a robust, static, unique identifier that you recognize an account by in your own systems. Ideally, the account ID should be a database ID.  💡 The properties `name`, `mrr`, `plan` and `registered_at` will be used to create companies in destinations like Intercom, HubSpot, Salesforce, ...  `journy(\"account\")` allows you to identify the business account (i.e. organization) using your product.  ```ts journy(\"account\", {   // Required   // Unique identifier for the account in your database   accountId: \"30\",    // Optional   // Hash of the account ID using a backend secret   // You can find the secret in the website settings   // Recommended to prevent spoofing   verification: \"hash\",    // Optional   properties: {     name: \"ACME, Inc\",     mrr: 399,     plan: \"Pro\",     registered_at: new Date(/_* ... *_/),     is_paying: true,     key_with_empty_value: \"\",     this_property_will_be_deleted: null,   }, }); ```  ## Send page view  💡 In applications, we advise you to use screen views instead of page views.  The JavaScript snippet in the site settings includes a `pageview` by default.  ```ts journy(\"pageview\"); ```  If you have a B2B application, we recommend to set account ID for every page view that happens within the context of an account.  💡 An account ID should be a robust, static, unique identifier that you recognize an account by in your own systems. Ideally, the account ID should be a database ID.  ```ts journy(\"pageview\", {   accountId: \"30\",    // Optional   // Hash of the account ID using a backend secret   // You can find the secret in the website settings   // Recommended to prevent spoofing   verification: \"hash\", }); ```  ## Send screen view  In applications, we strongly advise you to use screen views instead of page views.  Page URLs in applications often include the account ID (e.g. https://app.acme.com/accountId/settings).  This makes it difficult to create signals, segments, ... based on those URLs.  That's what screen views solve. It allows you to set a name for the screen being viewed (e.g. Account settings).  ```ts journy(\"screen\", { name: \"Personal settings\" }); ```  If you have a B2B application, we recommend to set account ID for every screen view that happens within the context of an account.  Example: \"Personal settings\" would be without account ID, \"Team settings\" would be with account ID.  💡 An account ID should be a robust, static, unique identifier that you recognize an account by in your own systems. Ideally, the account ID should be a database ID.  ```ts journy(\"screen\", {   name: \"Account settings\",   accountId: \"30\",    // Optional   // Hash of the account ID using a backend secret   // You can find the secret in the website settings   // Recommended to prevent spoofing   verification: \"hash\", }); ```  ## Trigger an event  💡 Use past tense for event names.  User events:  ```js journy(\"event\", {   // required   name: \"signed_in\",    // optional   metadata: {     key: \"value\",   }, }); ```  Account events:  💡 An account ID should be a robust, static, unique identifier that you recognize an account by in your own systems. Ideally, the account ID should be a database ID.  ```js journy(\"event\", {   // required   name: \"created_invoice\",   accountId: \"30\",    // Optional   // Hash of the account ID using a backend secret   // You can find the secret in the website settings   // Recommended to prevent spoofing   verification: \"hash\",    // optional   metadata: {     key: \"value\",     amount: 100,     allow_wire_transfer: true,   }, }); ```  ## Identity verification  Identity verification ensures that one person can't impersonate another.  Identity verification requires you to add an hash (HMAC) (that you generate on your server using SHA256) to your installation snippet alongside your user ID and account ID.  journy.io won't accept requests for a logged-in user without a valid hash. The hash is calculated using a secret key, which you should never share. Without this secret key, no third party can send journy.io a valid hash for one of your users, so they can't impersonate your users.  This is optional but highly recommended.  You can enable identify verification in the website settings in the connections view.  ```js journy(\"identify\", {   userId: \"userId\",   verification: \"USER_ID_HMAC_VALUE_HERE\" })  journy(\"account\", {   accountId: \"accountId\",   verification: \"ACCOUNT_ID_HMAC_VALUE_HERE\" })  journy(\"event\", {   accountId: \"accountId\",   verification: \"ACCOUNT_ID_HMAC_VALUE_HERE\" }) ```  ### PHP  ```php <?php  hash_hmac(   'sha256', // hash function   id, // user or account ID   'secret' // secret key (keep safe!) ); ```  ### Node.js  ```js import { createHmac } from \"crypto\"  createHmac(   \"sha256\", // hash function   'secret' // secret key (keep safe!) ).update(id).digest(\"hex\") // user or account ID ```  ### Ruby  ```ruby OpenSSL::HMAC.hexdigest(   'sha256', # hash function   'secret', # secret key (keep safe!)   id.to_s # user or account ID ) ```  ### Python  ``` import hmac import hashlib  hmac.new(   b'secret', # secret key (keep safe!)   bytes(id, encoding='utf-8'), # user or account ID   digestmod=hashlib.sha256 # hash function ).hexdigest() ```  ## Single page application  You can use our JavaScript snippet inside single page applications.  You should call `journy(\"screen\")` (or `journy(\"pageview\")`) whenever a user in your application transitions to another page. You can do this by listening to router change events. The current page URL will always be resolved using `window.location.href`.  You can trigger events using `journy(\"event\")` whenever you need to.  ### Next.js  We built a demo app with Next.js. You can find the code [here](https://github.com/journy-io/js-sdk-demo-app).  This [component](https://github.com/journy-io/js-sdk-demo-app/blob/main/components/Journy.js) should be a great start.  You can use the `Script` component from Next.js to load the web snippet and call `init`.  Don't forget to listen on route changes. You can use the `useRouter` hook for that.  ### React Router v6  You can use the [`useLocation`](https://reactrouter.com/docs/en/v6/api#uselocation) hook to listen for route changes:  ```js import React, { useEffect } from \"react\"; import { useLocation } from 'react-router-dom';  function App() {   const location = useLocation();    useEffect(() => {     journy(\"screen\", { name: \"name\" });     // or     journy(\"pageview\");   }, [location]);    return (       // ...   ); } ```  ### Vue Router  You can use [`router.afterEach`](https://router.vuejs.org/guide/advanced/navigation-guards.html#global-after-hooks) to listen for route changes:  ```js const router = new VueRouter({ ... });  router.afterEach((to, from) => {   journy(\"screen\", { name: \"name\" });   // or   journy(\"pageview\"); }); ```  Note: We don't accept a page URL argument for `journy(\"pageview\")`. The current page URL will always be resolved using `window.location.href`.  ## TypeScript  We published an [npm package](https://www.npmjs.com/package/@journyio/web-types) with type definitions to enable type-safe usage of our JavaScript snippet. The code and documentation is available on [GitHub](https://github.com/journy-io/web-types).  ## Localhost  By default a site doesn't allow page views from other domains than the registered domain. This makes it difficult to test your tracking implementation locally.  You can enable \"Allow any domain\" in the site settings to disable the domain check.  This will allow you to test the JavaScript snippet with localhost as hostname.  # Backend  The journy.io API is organized around REST. Our API has predictable resource-oriented URLs, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.  The API is hosted on api.journy.io.  ## Official SDKs  Our SDKs are designed to help you interact with our APIs with less friction. They are written in several different languages and help bridge the gap between your application and journy.io APIs. They take away the need to know the exact URL and HTTP method to use for each API call among other things leaving you more time to focus on making your application.  | Language   | Package                                                                        | Source code                                                                | |------------|--------------------------------------------------------------------------------|----------------------------------------------------------------------------| | 💚 Node.js | [npm install @journyio/sdk ](https://www.npmjs.com/package/@journyio/sdk)      | [github.com/journy-io/js-sdk](https://github.com/journy-io/js-sdk)         | | 🐘 PHP     | [composer require journy-io/sdk](https://packagist.org/packages/journy-io/sdk) | [github.com/journy-io/php-sdk](https://github.com/journy-io/php-sdk)       | | 🐍 Python  | [pip install journyio-sdk](https://pypi.org/project/journyio-sdk/)             | [github.com/journy-io/python-sdk](https://github.com/journy-io/python-sdk) | | 💎 Ruby    | Coming soon                                                                    | Coming soon                                                                |  Your favourite programming language not included? [Let us know!](mailto:hi@journy.io)  In the meanwhile, you can use [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) to generate a client for your programming language.  ## Authentication  The journy.io API uses API keys to authenticate requests. You can view and manage your API keys in the [connections screen](https://system.journy.io).  Your API keys carry many privileges, so be sure to keep them secure! Do not share your secret API keys in publicly accessible areas such as GitHub, client-side code, and so forth.  All API requests must be made over HTTPS. Calls made over plain HTTP will fail. API requests without authentication will also fail.  For every request send to the API we expect a header `X-Api-Key` to be set with the API Key.  ## Permissions  When creating an API Key in [the application](https://system.journy.io) you will have the choice to give permissions to an API Key (which you can change later on). These permissions restrict the API Key from different actions. When an API Key tries to perform a certain action it doesn't have the permissions for, you will receive a `401: Unauthorized` response.  ## Rate limiting  To prevent abuse of the API there is a maximum throughput of 1800 requests per minute. If you need a higher throughput, please contact us.  To keep our platform healthy and stable, we'll block API keys that consistently hit our rate limits. Therefore, please consider taking this throughput into account.  In every response the headers `X-RateLimit-Limit` and `X-RateLimit-Remaining` will be set. The `X-RateLimit-Limit`-header will always contain the current limit of requests per minute. The `X-RateLimit-Remaining`-header will always contain the amount of requests you have left in the current sliding window.  💡 The client-side tracking uses different rate limits.  ## Errors  journy.io uses conventional HTTP response codes to indicate the success or failure of an API request. In general: Codes in the 2xx range indicate success. Codes in the 4xx range indicate an error that failed given the information provided (e.g. a required parameter was omitted). Codes in the 5xx range indicate an error with journy.io's servers (these are rare).  When performing a `POST`- or `PUT`-request with a requestBody, or when including parameters, these parameters and fields will automatically be checked and validated against the API Spec. When any error occurs, you will get a response with an `errors`-field, structured as follows:  ```json {   \"errors\": {     \"parameters\": {       \"header\": {         \"headerParameterName\": \"Describe what's wrong with the header parameter.\",         ...       },       \"query\": {         \"queryParameterName\": \"Describe what's wrong with the query parameter.\",         ...       },       \"path\": {         \"pathParameterName\": \"Describe what's wrong with the path parameter.\",         ...       },     },     \"fields\": {       \"fieldName\": \"Describe what's wrong with the fieldName.\",       \"object.fieldName\": \"Describe what's wrong with the fieldName of the included object.\",        ...     }   } } ```  ## Best practices  ### Track accounts & users immediately on creation  When you create an account in your database, immediately sending data about that account to journy.io helps your team stay in sync. The same goes for users. Call [Upsert account](#operation/upsertAccount) as soon as possible, right after the account is first created in your database.  ### Update account data daily  Not every account is active every day. But, you may have properties on the account that change through background processing. That's why we recommend updating every one of your accounts' data in a recurring daily process. This way, you know that your accounts are updated every day in journy.io.  ## Changelog  ### December 2021  [POST /events](#operation/trackJourneyEvent) will be moved to [POST /track](#operation/trackEvent). [POST /events](#operation/trackJourneyEvent) is deprecated and will be removed in the future.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: hi@journy.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import superagent from "superagent";
import querystring from "querystring";

/**
* @module ApiClient
* @version 1.0.0
*/

/**
* Manages low level client-server communications, parameter marshalling, etc. There should not be any need for an
* application to use this class directly - the *Api and model classes provide the public API for the service. The
* contents of this file should be regarded as internal but are documented for completeness.
* @alias module:ApiClient
* @class
*/
class ApiClient {
    /**
     * The base URL against which to resolve every API call's (relative) path.
     * Overrides the default value set in spec file if present
     * @param {String} basePath
     */
    constructor(basePath = 'https://api.journy.io') {
        /**
         * The base URL against which to resolve every API call's (relative) path.
         * @type {String}
         * @default https://api.journy.io
         */
        this.basePath = basePath.replace(/\/+$/, '');

        /**
         * The authentication methods to be included for all API calls.
         * @type {Array.<String>}
         */
        this.authentications = {
        }

        /**
         * The default HTTP headers to be included for all API calls.
         * @type {Array.<String>}
         * @default {}
         */
        this.defaultHeaders = {
            'User-Agent': 'OpenAPI-Generator/1.0.0/Javascript'
        };

        /**
         * The default HTTP timeout for all API calls.
         * @type {Number}
         * @default 60000
         */
        this.timeout = 60000;

        /**
         * If set to false an additional timestamp parameter is added to all API GET calls to
         * prevent browser caching
         * @type {Boolean}
         * @default true
         */
        this.cache = true;

        /**
         * If set to true, the client will save the cookies from each server
         * response, and return them in the next request.
         * @default false
         */
        this.enableCookies = false;

        /*
         * Used to save and return cookies in a node.js (non-browser) setting,
         * if this.enableCookies is set to true.
         */
        if (typeof window === 'undefined') {
          this.agent = new superagent.agent();
        }

        /*
         * Allow user to override superagent agent
         */
         this.requestAgent = null;

        /*
         * Allow user to add superagent plugins
         */
        this.plugins = null;

    }

    /**
    * Returns a string representation for an actual parameter.
    * @param param The actual parameter.
    * @returns {String} The string representation of <code>param</code>.
    */
    paramToString(param) {
        if (param == undefined || param == null) {
            return '';
        }
        if (param instanceof Date) {
            return param.toJSON();
        }
        if (ApiClient.canBeJsonified(param)) {
            return JSON.stringify(param);
        }

        return param.toString();
    }

    /**
    * Returns a boolean indicating if the parameter could be JSON.stringified
    * @param param The actual parameter
    * @returns {Boolean} Flag indicating if <code>param</code> can be JSON.stringified
    */
    static canBeJsonified(str) {
        if (typeof str !== 'string' && typeof str !== 'object') return false;
        try {
            const type = str.toString();
            return type === '[object Object]'
                || type === '[object Array]';
        } catch (err) {
            return false;
        }
    };

   /**
    * Builds full URL by appending the given path to the base URL and replacing path parameter place-holders with parameter values.
    * NOTE: query parameters are not handled here.
    * @param {String} path The path to append to the base URL.
    * @param {Object} pathParams The parameter values to append.
    * @param {String} apiBasePath Base path defined in the path, operation level to override the default one
    * @returns {String} The encoded path with parameter values substituted.
    */
    buildUrl(path, pathParams, apiBasePath) {
        if (!path.match(/^\//)) {
            path = '/' + path;
        }

        var url = this.basePath + path;

        // use API (operation, path) base path if defined
        if (apiBasePath !== null && apiBasePath !== undefined) {
            url = apiBasePath + path;
        }

        url = url.replace(/\{([\w-\.#]+)\}/g, (fullMatch, key) => {
            var value;
            if (pathParams.hasOwnProperty(key)) {
                value = this.paramToString(pathParams[key]);
            } else {
                value = fullMatch;
            }

            return encodeURIComponent(value);
        });

        return url;
    }

    /**
    * Checks whether the given content type represents JSON.<br>
    * JSON content type examples:<br>
    * <ul>
    * <li>application/json</li>
    * <li>application/json; charset=UTF8</li>
    * <li>APPLICATION/JSON</li>
    * </ul>
    * @param {String} contentType The MIME content type to check.
    * @returns {Boolean} <code>true</code> if <code>contentType</code> represents JSON, otherwise <code>false</code>.
    */
    isJsonMime(contentType) {
        return Boolean(contentType != null && contentType.match(/^application\/json(;.*)?$/i));
    }

    /**
    * Chooses a content type from the given array, with JSON preferred; i.e. return JSON if included, otherwise return the first.
    * @param {Array.<String>} contentTypes
    * @returns {String} The chosen content type, preferring JSON.
    */
    jsonPreferredMime(contentTypes) {
        for (var i = 0; i < contentTypes.length; i++) {
            if (this.isJsonMime(contentTypes[i])) {
                return contentTypes[i];
            }
        }

        return contentTypes[0];
    }

    /**
    * Checks whether the given parameter value represents file-like content.
    * @param param The parameter to check.
    * @returns {Boolean} <code>true</code> if <code>param</code> represents a file.
    */
    isFileParam(param) {
        // fs.ReadStream in Node.js and Electron (but not in runtime like browserify)
        if (typeof require === 'function') {
            let fs;
            try {
                fs = require('fs');
            } catch (err) {}
            if (fs && fs.ReadStream && param instanceof fs.ReadStream) {
                return true;
            }
        }

        // Buffer in Node.js
        if (typeof Buffer === 'function' && param instanceof Buffer) {
            return true;
        }

        // Blob in browser
        if (typeof Blob === 'function' && param instanceof Blob) {
            return true;
        }

        // File in browser (it seems File object is also instance of Blob, but keep this for safe)
        if (typeof File === 'function' && param instanceof File) {
            return true;
        }

        return false;
    }

    /**
    * Normalizes parameter values:
    * <ul>
    * <li>remove nils</li>
    * <li>keep files and arrays</li>
    * <li>format to string with `paramToString` for other cases</li>
    * </ul>
    * @param {Object.<String, Object>} params The parameters as object properties.
    * @returns {Object.<String, Object>} normalized parameters.
    */
    normalizeParams(params) {
        var newParams = {};
        for (var key in params) {
            if (params.hasOwnProperty(key) && params[key] != undefined && params[key] != null) {
                var value = params[key];
                if (this.isFileParam(value) || Array.isArray(value)) {
                    newParams[key] = value;
                } else {
                    newParams[key] = this.paramToString(value);
                }
            }
        }

        return newParams;
    }

    /**
    * Builds a string representation of an array-type actual parameter, according to the given collection format.
    * @param {Array} param An array parameter.
    * @param {module:ApiClient.CollectionFormatEnum} collectionFormat The array element separator strategy.
    * @returns {String|Array} A string representation of the supplied collection, using the specified delimiter. Returns
    * <code>param</code> as is if <code>collectionFormat</code> is <code>multi</code>.
    */
    buildCollectionParam(param, collectionFormat) {
        if (param == null) {
            return null;
        }
        switch (collectionFormat) {
            case 'csv':
                return param.map(this.paramToString, this).join(',');
            case 'ssv':
                return param.map(this.paramToString, this).join(' ');
            case 'tsv':
                return param.map(this.paramToString, this).join('\t');
            case 'pipes':
                return param.map(this.paramToString, this).join('|');
            case 'multi':
                //return the array directly as SuperAgent will handle it as expected
                return param.map(this.paramToString, this);
            case 'passthrough':
                return param;
            default:
                throw new Error('Unknown collection format: ' + collectionFormat);
        }
    }

    /**
    * Applies authentication headers to the request.
    * @param {Object} request The request object created by a <code>superagent()</code> call.
    * @param {Array.<String>} authNames An array of authentication method names.
    */
    applyAuthToRequest(request, authNames) {
        authNames.forEach((authName) => {
            var auth = this.authentications[authName];
            switch (auth.type) {
                case 'basic':
                    if (auth.username || auth.password) {
                        request.auth(auth.username || '', auth.password || '');
                    }

                    break;
                case 'bearer':
                    if (auth.accessToken) {
                        var localVarBearerToken = typeof auth.accessToken === 'function'
                          ? auth.accessToken()
                          : auth.accessToken
                        request.set({'Authorization': 'Bearer ' + localVarBearerToken});
                    }

                    break;
                case 'apiKey':
                    if (auth.apiKey) {
                        var data = {};
                        if (auth.apiKeyPrefix) {
                            data[auth.name] = auth.apiKeyPrefix + ' ' + auth.apiKey;
                        } else {
                            data[auth.name] = auth.apiKey;
                        }

                        if (auth['in'] === 'header') {
                            request.set(data);
                        } else {
                            request.query(data);
                        }
                    }

                    break;
                case 'oauth2':
                    if (auth.accessToken) {
                        request.set({'Authorization': 'Bearer ' + auth.accessToken});
                    }

                    break;
                default:
                    throw new Error('Unknown authentication type: ' + auth.type);
            }
        });
    }

   /**
    * Deserializes an HTTP response body into a value of the specified type.
    * @param {Object} response A SuperAgent response object.
    * @param {(String|Array.<String>|Object.<String, Object>|Function)} returnType The type to return. Pass a string for simple types
    * or the constructor function for a complex type. Pass an array containing the type name to return an array of that type. To
    * return an object, pass an object with one property whose name is the key type and whose value is the corresponding value type:
    * all properties on <code>data<code> will be converted to this type.
    * @returns A value of the specified type.
    */
    deserialize(response, returnType) {
        if (response == null || returnType == null || response.status == 204) {
            return null;
        }

        // Rely on SuperAgent for parsing response body.
        // See http://visionmedia.github.io/superagent/#parsing-response-bodies
        var data = response.body;
        if (data == null || (typeof data === 'object' && typeof data.length === 'undefined' && !Object.keys(data).length)) {
            // SuperAgent does not always produce a body; use the unparsed response as a fallback
            data = response.text;
        }

        return ApiClient.convertToType(data, returnType);
    }

   /**
    * Callback function to receive the result of the operation.
    * @callback module:ApiClient~callApiCallback
    * @param {String} error Error message, if any.
    * @param data The data returned by the service call.
    * @param {String} response The complete HTTP response.
    */

   /**
    * Invokes the REST service using the supplied settings and parameters.
    * @param {String} path The base URL to invoke.
    * @param {String} httpMethod The HTTP method to use.
    * @param {Object.<String, String>} pathParams A map of path parameters and their values.
    * @param {Object.<String, Object>} queryParams A map of query parameters and their values.
    * @param {Object.<String, Object>} headerParams A map of header parameters and their values.
    * @param {Object.<String, Object>} formParams A map of form parameters and their values.
    * @param {Object} bodyParam The value to pass as the request body.
    * @param {Array.<String>} authNames An array of authentication type names.
    * @param {Array.<String>} contentTypes An array of request MIME types.
    * @param {Array.<String>} accepts An array of acceptable response MIME types.
    * @param {(String|Array|ObjectFunction)} returnType The required type to return; can be a string for simple types or the
    * constructor for a complex type.
    * @param {String} apiBasePath base path defined in the operation/path level to override the default one
    * @param {module:ApiClient~callApiCallback} callback The callback function.
    * @returns {Object} The SuperAgent request object.
    */
    callApi(path, httpMethod, pathParams,
        queryParams, headerParams, formParams, bodyParam, authNames, contentTypes, accepts,
        returnType, apiBasePath, callback) {

        var url = this.buildUrl(path, pathParams, apiBasePath);
        var request = superagent(httpMethod, url);

        if (this.plugins !== null) {
            for (var index in this.plugins) {
                if (this.plugins.hasOwnProperty(index)) {
                    request.use(this.plugins[index])
                }
            }
        }

        // apply authentications
        this.applyAuthToRequest(request, authNames);

        // set query parameters
        if (httpMethod.toUpperCase() === 'GET' && this.cache === false) {
            queryParams['_'] = new Date().getTime();
        }

        request.query(this.normalizeParams(queryParams));

        // set header parameters
        request.set(this.defaultHeaders).set(this.normalizeParams(headerParams));

        // set requestAgent if it is set by user
        if (this.requestAgent) {
          request.agent(this.requestAgent);
        }

        // set request timeout
        request.timeout(this.timeout);

        var contentType = this.jsonPreferredMime(contentTypes);
        if (contentType) {
            // Issue with superagent and multipart/form-data (https://github.com/visionmedia/superagent/issues/746)
            if(contentType != 'multipart/form-data') {
                request.type(contentType);
            }
        }

        if (contentType === 'application/x-www-form-urlencoded') {
            request.send(querystring.stringify(this.normalizeParams(formParams)));
        } else if (contentType == 'multipart/form-data') {
            var _formParams = this.normalizeParams(formParams);
            for (var key in _formParams) {
                if (_formParams.hasOwnProperty(key)) {
                    let _formParamsValue = _formParams[key];
                    if (this.isFileParam(_formParamsValue)) {
                        // file field
                        request.attach(key, _formParamsValue);
                    } else if (Array.isArray(_formParamsValue) && _formParamsValue.length
                        && this.isFileParam(_formParamsValue[0])) {
                        // multiple files
                        _formParamsValue.forEach(file => request.attach(key, file));
                    } else {
                        request.field(key, _formParamsValue);
                    }
                }
            }
        } else if (bodyParam !== null && bodyParam !== undefined) {
            if (!request.header['Content-Type']) {
                request.type('application/json');
            }
            request.send(bodyParam);
        }

        var accept = this.jsonPreferredMime(accepts);
        if (accept) {
            request.accept(accept);
        }

        if (returnType === 'Blob') {
          request.responseType('blob');
        } else if (returnType === 'String') {
          request.responseType('text');
        }

        // Attach previously saved cookies, if enabled
        if (this.enableCookies){
            if (typeof window === 'undefined') {
                this.agent._attachCookies(request);
            }
            else {
                request.withCredentials();
            }
        }

        request.end((error, response) => {
            if (callback) {
                var data = null;
                if (!error) {
                    try {
                        data = this.deserialize(response, returnType);
                        if (this.enableCookies && typeof window === 'undefined'){
                            this.agent._saveCookies(response);
                        }
                    } catch (err) {
                        error = err;
                    }
                }

                callback(error, data, response);
            }
        });

        return request;
    }

    /**
    * Parses an ISO-8601 string representation or epoch representation of a date value.
    * @param {String} str The date value as a string.
    * @returns {Date} The parsed date object.
    */
    static parseDate(str) {
        if (isNaN(str)) {
            return new Date(str.replace(/(\d)(T)(\d)/i, '$1 $3'));
        }
        return new Date(+str);
    }

    /**
    * Converts a value to the specified type.
    * @param {(String|Object)} data The data to convert, as a string or object.
    * @param {(String|Array.<String>|Object.<String, Object>|Function)} type The type to return. Pass a string for simple types
    * or the constructor function for a complex type. Pass an array containing the type name to return an array of that type. To
    * return an object, pass an object with one property whose name is the key type and whose value is the corresponding value type:
    * all properties on <code>data<code> will be converted to this type.
    * @returns An instance of the specified type or null or undefined if data is null or undefined.
    */
    static convertToType(data, type) {
        if (data === null || data === undefined)
            return data

        switch (type) {
            case 'Boolean':
                return Boolean(data);
            case 'Integer':
                return parseInt(data, 10);
            case 'Number':
                return parseFloat(data);
            case 'String':
                return String(data);
            case 'Date':
                return ApiClient.parseDate(String(data));
            case 'Blob':
                return data;
            default:
                if (type === Object) {
                    // generic object, return directly
                    return data;
                } else if (typeof type.constructFromObject === 'function') {
                    // for model type like User and enum class
                    return type.constructFromObject(data);
                } else if (Array.isArray(type)) {
                    // for array type like: ['String']
                    var itemType = type[0];

                    return data.map((item) => {
                        return ApiClient.convertToType(item, itemType);
                    });
                } else if (typeof type === 'object') {
                    // for plain object type like: {'String': 'Integer'}
                    var keyType, valueType;
                    for (var k in type) {
                        if (type.hasOwnProperty(k)) {
                            keyType = k;
                            valueType = type[k];
                            break;
                        }
                    }

                    var result = {};
                    for (var k in data) {
                        if (data.hasOwnProperty(k)) {
                            var key = ApiClient.convertToType(k, keyType);
                            var value = ApiClient.convertToType(data[k], valueType);
                            result[key] = value;
                        }
                    }

                    return result;
                } else {
                    // for unknown type, return the data directly
                    return data;
                }
        }
    }

  /**
    * Gets an array of host settings
    * @returns An array of host settings
    */
    hostSettings() {
        return [
            {
              'url': "https://api.journy.io",
              'description': "Production",
            }
      ];
    }

    getBasePathFromSettings(index, variables={}) {
        var servers = this.hostSettings();

        // check array index out of bound
        if (index < 0 || index >= servers.length) {
            throw new Error("Invalid index " + index + " when selecting the host settings. Must be less than " + servers.length);
        }

        var server = servers[index];
        var url = server['url'];

        // go through variable and assign a value
        for (var variable_name in server['variables']) {
            if (variable_name in variables) {
                let variable = server['variables'][variable_name];
                if ( !('enum_values' in variable) || variable['enum_values'].includes(variables[variable_name]) ) {
                    url = url.replace("{" + variable_name + "}", variables[variable_name]);
                } else {
                    throw new Error("The variable `" + variable_name + "` in the host URL has invalid value " + variables[variable_name] + ". Must be " + server['variables'][variable_name]['enum_values'] + ".");
                }
            } else {
                // use default value
                url = url.replace("{" + variable_name + "}", server['variables'][variable_name]['default_value'])
            }
        }
        return url;
    }

    /**
    * Constructs a new map or array model from REST data.
    * @param data {Object|Array} The REST data.
    * @param obj {Object|Array} The target object or array.
    */
    static constructFromObject(data, obj, itemType) {
        if (Array.isArray(data)) {
            for (var i = 0; i < data.length; i++) {
                if (data.hasOwnProperty(i))
                    obj[i] = ApiClient.convertToType(data[i], itemType);
            }
        } else {
            for (var k in data) {
                if (data.hasOwnProperty(k))
                    obj[k] = ApiClient.convertToType(data[k], itemType);
            }
        }
    };
}

/**
 * Enumeration of collection format separator strategies.
 * @enum {String}
 * @readonly
 */
ApiClient.CollectionFormatEnum = {
    /**
     * Comma-separated values. Value: <code>csv</code>
     * @const
     */
    CSV: ',',

    /**
     * Space-separated values. Value: <code>ssv</code>
     * @const
     */
    SSV: ' ',

    /**
     * Tab-separated values. Value: <code>tsv</code>
     * @const
     */
    TSV: '\t',

    /**
     * Pipe(|)-separated values. Value: <code>pipes</code>
     * @const
     */
    PIPES: '|',

    /**
     * Native array. Value: <code>multi</code>
     * @const
     */
    MULTI: 'multi'
};

/**
* The default API client implementation.
* @type {module:ApiClient}
*/
ApiClient.instance = new ApiClient();
export default ApiClient;
