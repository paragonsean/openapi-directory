/**
 * Zapier Natural Language Actions (NLA) API - Beta
 * <img src=\"https://cdn.zappy.app/945f9bf9e44126873952ec5113949c3f.png\" width=\"100\" />  ## Hi, there! Welcome to the **Zapier Natural Language Actions API docs**. You are currently viewing the **root** API.  The endpoints of this **root** API are static and useful for reference. To see the live playground with dynamic API endpoints that match up to your own **actions**, [log in first](/login/zapier/), then go here:  **[NLA Dynamic API](/api/v1/dynamic/docs).**   ## Overview <a name=\"overview\"></a>  Zapier is an integration platform with over 5,000+ apps and 50,000+ actions. You can view the [full list here](https://zapier.com/apps). Zapier is used by millions of users, most of whom are non-technical builders -- but often savvy with software. Zapier offers several no code products to connect together the various apps on our platform. NLA exposes the same integrations Zapier uses to build our products, to you, to plug-in the capabilties of Zapier's platform into your own products.   For example, you can use the NLA API to: * Send messages in [Slack](https://zapier.com/apps/slack/integrations) * Add a row to a [Google Sheet](https://zapier.com/apps/google-sheets/integrations) * Draft a new email in [Gmail](https://zapier.com/apps/gmail/integrations) * ... and thousands more, with one universal natural language API  The typical use-case for NLA is to expose our ecosystem of thousands of apps/actions within your own product. NLA is optimized for products that receive user input in natural language (eg. chat, assistant, or other large language model based experience) -- that said, it can also be used to power _any_ product that needs integrations. In this case, think of NLA as a more friendly, human API.  NLA contains a decade of experience with API shenanigans, so you don't have to. Common API complexity, automatically handled: * **Every type of auth** (Basic, Session, API Key, OAuth v1, Oauth v2, Digest, ...), Zapier securely handles and signs requests for you * **Support for create, update, and search actions**, endpoints optimized for natural language usage * **Support for custom fields**, Spreadsheet, CRM, and Mailing List friendly! * **Reference by name, not ID**, humans use natural language names, not IDs, to reference things in their apps, so NLA does too * **Smart, human defaults**, APIs sometimes have 100 options. Zapier's platform data helps us make NLA simpler for users out of the box  #### Two Usage Modes <a name=\"usage-modes\"></a>  NLA handles all the underlying API auth and translation from natural language --> underlying API call --> return simplified output. The key idea is you (the developer), or your users, expose a set of actions via an oauth-like setup window, which you can then query and execute via a REST API. NLA offers both API Key and OAuth for signing NLA API requests.  1. **Server-side only** (API Key): for quickly getting started, testing, and production scenarios where your app will only use actions exposed in the developer's Zapier account (and will use the developer's connected accounts on Zapier.com)  2. **User-facing** (Oauth): for production scenarios where you are deploying an end-user facing application and your app needs access to end-user's exposed actions and connected accounts on Zapier.com  #### Why Natural Language?   Simply, it makes the API easier to use for both developers and users (and also for [large language models](https://en.wikipedia.org/wiki/Wikipedia:Large_language_models)!)  We designed NLA to expose the power of Zapier's platform without passing along the complexity. A few design choices: * There is a [user-facing component](https://cdn.zappy.app/83728f684b91c0afe7d435445fe4ac90.png) to NLA, exposed via a popup window, users set up and enable basic actions which \"expose\" them to you, the `provider`. * The default action setup for users is minimal and fast. [All required fields are guessed](https://cdn.zappy.app/20afede9be56bf4e30d31986bc5325f8.png). This guessing is accomplished using an lanuage model on the NLA side. * Users can [choose to override any guessed field](https://cdn.zappy.app/e07f6eabfe7512e9decf01cba0c9e847.png) with a fixed value or choice, increasing trust to use the natural language interface. * Custom fields (ex. spreadsheet columns) can also be [dynamically guessed at action run time](https://cdn.zappy.app/9061499b4b973200fc345f695b33e3c7.png), or fixed by the user.  Using the API is then simple:  ``` curl -v \\     -d '{\"instructions\": \"Add Bryan Helmig at Zapier to my NLA test sheet, oh and he loves guitars!\"}' \\     -H \"Authorization: Bearer <ACCESS_TOKEN>\" \\     -H \"Content-Type: application/json\" \\     'https://nla.zapier.com/api/v1/dynamic/exposed/<ACTION_ID>/execute/' ```  Or mix in some fixed values:  ``` curl -v \\     -d '{\"instructions\": \"Send a short poem about automation to slack\", \"channel\": \"#fun-zapier\"}' \\     -H \"Authorization: Bearer <ACCESS_TOKEN>\" \\     -H \"Content-Type: application/json\" \\     'https://nla.zapier.com/api/v1/dynamic/exposed/<ACTION_ID>/execute/' ```  ## Auth <a name=\"auth\"></a>  #### For Quickly Exploring <a name=\"exploring\"></a>  It's best to take advantage of session auth built into the OpenAPI docs.  1. [Log in](/login/zapier/) 2. [Create and enable an action](/demo/) using our `demo` provider  then all your enabled (\"exposed\") actions will be available at the bottom of the the **[dynamic API](/api/v1/dynamic/docs)**.  #### For Testing or Production (Server-side only mode) <a name=\"server-side\"></a>  For development purposes, or using NLA in a server-side only use case, you can get started quickly using the provider `dev`. You can generate an `API key` using this provider and make authenticated requests.  Please follow these steps:  1. Go to the [Dev App provider](/dev/provider/debug/) debug page. 2. Look for \"User\" -> \"Information\" -> \"API Key\". If a key does not exist, follow the instructions to generate one. 3. Use this key in the header `x-api-key` to make authenticated requests.  Test that the API key is working:  ``` curl -v \\     -H \"Content-Type: application/json\" \\     -H \"x-api-key: <API_KEY>\" \\     'https://nla.zapier.com/api/v1/check/' ```  #### For Production (User-facing mode) <a name=\"production\"></a>  The API is authenticated via [standard OAuth v2](https://oauth.net/2/). Submit [this form](https://share.hsforms.com/1DWkLQ7SpSZCuZbTxcBB98gck10t) to get access and receive a `cliend_id`, `client_secret`, and your `provider` name (ex. 'acme'). You'll also need to share with us a `redirect_uri` to receive each `code`. This API uses both `access_token` and `refresh_token`.  Each of your users will get a per-user access token which you'll use to sign requests. The access token both authenticates and authorizes a request to access or run (execute) a given user's actions.  The basic auth flow is:  1. **Send user to our OAuth start URL, ideally in a popup window**  ```javascript var url = https://nla.zapier.com/oauth/authorize/?     response_type=code&     client_id=<YOUR_CLIENT_ID>&     redirect_uri=<YOUR_REDIRECT_URI>&     scope=nla%3Aexposed_actions%3Aexecute var nla = window.open(url, 'nla', 'width=650,height=700'); ```  2. **User approves request for access**  3. **NLA will redirect user via `GET` to the `redirect_uri` you provided us with a `?code=` in the query string**  4. **Snag the `code` and `POST` it to the NLA token endpoint `https://nla.zapier.com/oauth/token/`**  ``` curl -v \\     -d '{ \\         \"code\": \"<CODE>\", \\         \"grant_type\": \"authorization_code\", \\         \"client_id\": \"<YOUR_CLIENT_ID>\", \\         \"client_secret\": \"<YOUR_CLIENT_SECRET>\" \\         }' \\     -H \"Content-Type: application/json\" \\     -X POST 'https://nla.zapier.com/oauth/token/' ```  5. **Finally, receive `refresh_token` and `access_token` in response**  Save the refresh token, you'll need to use it to request a new access tokehn when it expires.  Now you can use the `access_token` to make authenticated requests:  ``` curl -v -H \"Authorization: Bearer <ACCESS_TOKEN>\" https://nla.zapier.com/api/v1/dynamic/openapi.json ```  6. **When the `access_token` expires, refresh it**  ``` curl -v \\     -d '{ \\         \"refresh_token\": \"<REFRESH_TOKEN>\", \\         \"grant_type\": \"refresh_token\", \\         \"client_id\": \"<YOUR_CLIENT_ID>\", \\         \"client_secret\": \"<YOUR_CLIENT_SECRET>\" \\         }' \\     -H \"Content-Type: application/json\" \\     -X POST 'https://nla.zapier.com/oauth/token/' ```  ## Action Setup Window <a name=\"action-setup-window\"></a>  Users set up their actions inside a window popup, that looks and feels similar to an OAuth window. The setup URL is the same for all your users: `https://nla.zapier.com/<PROVIDER>/start/`  You can check the validity of an access/refresh token by checking against the `api/v1/check/` endpoint to determine if you should present the `oauth/authorize/` or `<PROVIDER>/start/` url.  You'd typically include a button or link somewhere inside your product to open the setup window.  ```javascript var nla = window.open('https://nla.zapier.com/<PROVIDER>/start', 'nla', 'width=650,height=700'); ```  _Note: the setup window is optimized for 650px width, 700px height_  ## Using the API <a name=\"using-the-api\"></a>  #### Understanding the AI guessing flow <a name=\"ai-guessing\"></a>  NLA is optimized for a chat/assistant style usage paradigm where you want to offload as much work to a large language model, as possible. For end users, the action setup flow that takes ~seconds (compared to minutes/hours with traditional, complex integration setup).  An action is then run (executed) via an API call with one single natural language parameter `instructions`. In the chat/assistant use case, these instructions are likely being generated by your own large language model. However NLA works just as well even in more traditional software paradigm where `instructions` are perhaps hard-coded into your codebase or supplied by the user directly.  Consider the case where you've built a chat product and your end user wants to expose a \"Send Slack Message\" action to your product. Their action setup [might look like this](https://cdn.zappy.app/d19215e5a2fb3896f6cddf435dfcbe27.png).  The user only has to pick Slack and authorize their Slack account. By default, all required fields are set to \"Have AI guess\". In this example there are two required fields: Channel and Message Text.  If a field uses \"Have AI guess\", two things happen: 1. When the action is run via the API, NLA will interpret passed `instructions` (using a language model) to fill in the values for Channel and Message Text. NLA is smart about fields like Channel -- Slack's API requires a Channel ID, not a plain text Channel name. NLA handles all such cases automatically. 2. The field will be listed as an optional hint parameter in the OpenAPI spec (see \"hint parameters\" below) which allows you (the developer) to override any `instructions` guessing.  Sometimes language models hallucinate or guess wrong. And if this were a particuarly sensitive Slack message, the user may not want to leave the selection of \"Channel\" up to chance. NLA allows the user [to use a specific, fixed value like this](https://cdn.zappy.app/dc4976635259b4889f8412d231fb3be4.png).  Now when the action executes, the Message Text will still be automatically guessed but Channel will be fixed to \"#testing\". This significantly increases user trust and unlocks use cases where the user may have partial but not full trust in an AI guessing.  We call the set of fields the user denoted \"Have AI guess\" as \"hint parameters\" -- Message Text above in the above example is one. They are *always* optional. When running actions via the API, you (the developer) can choose to supply none/any/all hint parameters. Any hint parameters provided are treated exactly like \"Use a specific value\" at the user layer -- as an override.   One aside: custom fields. Zapier supports custom fields throughout the platform. The degenerate case is a spreadsheet, where _every_ column is a custom field. This introduces complexity because sheet columns are unknowable at action setup time if the user picks \"Have AI guess\" for which spreadsheet. NLA handles such custom fields using the same pattern as above with one distinction: they are not listed as hint parameters because they are literally unknowable until run time. Also as you may expect, if the user picks a specific spreadsheet during action setup, custom fields act like regular fields and flow through normally.  In the typical chat/assistant product use case, you'll want to expose these hint parameters alongside the exposed action list to your own language model. Your language model is likely to have broader context about the user vs the narrowly constrained `instructions` string passed to the API and will result in a better guess.  In summary:  ``` [user supplied \"Use specific value\"] --overrides--> [API call supplied hint parameters] --overrides--> [API call supplied \"instructions\"] ```   #### Common API use cases <a name=\"common-api-uses\"></a>  There are three common usages: 1. Get a list of the current user's exposed actions 2. Get a list of an action's optional hint parameters 3. Execute an action  Let's go through each, assuming you have a valid access token already.  ### 1. Get a list of the current user's exposed actions <a name=\"list-exposed-actions\"></a>  ``` # via the RESTful list endpoint: curl -v -H \"Authorization: Bearer <ACCESS_TOKEN>\" https://nla.zapier.com/api/v1/dynamic/exposed/  # via the dynamic openapi.json schema: curl -v -H \"Authorization: Bearer <ACCESS_TOKEN>\" https://nla.zapier.com/api/v1/dynamic/openapi.json ```  Example of [full list endpoint response here](https://nla.zapier.com/api/v1/dynamic/exposed/), snipped below:  ``` {     \"results\": [         {             \"id\": \"01GTB1KMX72QTJEXXXXXXXXXX\",             \"description\": \"Slack: Send Channel Message\",             ... ```  Example of [full openapi.json response here](https://nla.zapier.com/api/v1/dynamic/openapi.json), snipped below:  ``` {     ...     \"paths\": {         ...         \"/api/v1/dynamic/exposed/01GTB1KMX72QTJEXXXXXXXXXX/execute/\": {             \"post\": {                 \"operationId\": \"exposed_01GTB1KMX72QTJEXXXXXXXXXX_execute\",                 \"summary\": \"Slack: Send Channel Message (execute)\",                 ...  ```  ### 2. Get a list of an action's optional hint parameters <a name=\"get-hints\"></a>  As a reminder, hint parameters are _always_ optional. By default, all parameters are filled in via guessing based on a provided `instructions` parameter. If a hint parameter is supplied in an API request along with instructions, the hint parameter will _override_ the guess.  ``` # via the RESTful list endpoint: curl -v -H \"Authorization: Bearer <ACCESS_TOKEN>\" https://nla.zapier.com/api/v1/dynamic/exposed/  # via the dynamic openapi.json schema: curl -v -H \"Authorization: Bearer <ACCESS_TOKEN>\" https://nla.zapier.com/api/v1/dynamic/openapi.json ```  Example of [full list endpoint response here](https://nla.zapier.com/api/v1/dynamic/exposed/), snipped below:  ``` {     \"results\": [         {             \"id\": \"01GTB1KMX72QTJEXXXXXXXXXX\",             \"description\": \"Slack: Send Channel Message\",             \"input_params\": {                 \"instructions\": \"str\",                 \"Message_Text\": \"str\",                 \"Channel\": \"str\",                 ... ```  Example of [full openapi.json response here](https://nla.zapier.com/api/v1/dynamic/openapi.json), snipped below:  ``` {     ...     \"components\": {         \"schemas\": {             ...             \"PreviewExecuteRequest_01GTB1KMX72QTJEXXXXXXXXXX\": {                 \"title\": \"PreviewExecuteRequest_01GTB1KMX72QTJEXXXXXXXXXX\",                 \"type\": \"object\",                 \"properties\": {                     \"instructions\": {                         ...                     },                     \"Message_Text\": {                         ...                     },                     \"Channel_Name\": {                         ...                     }  ```  _Note: Every list of input_params will contain `instructions`, the only required parameter for execution._   ### 3. Execute (or preview) an action <a name=\"execute-action\"></a>  Finally, with an action ID and any desired, optional, hint parameters in hand, we can run (execute) an action. The parameter `instructions` is the only required parameter run an action.  ``` curl -v \\     -d '{\"instructions\": \"send a short poem about automation and robots to slack\", \"Channel_Name\": \"#fun-zapier\"}' \\     -H \"Content-Type: application/json\" \\     -X POST 'https://nla.zapier.com/api/v1/dynamic/exposed/01GTB1KMX72QTJEXXXXXXXXXX/execute/' ```  Another example, this time an action to retrieve data:  ``` curl -v \\     -d '{\"instructions\": \"grab the latest email from bryan helmig\"}' \\     -H \"Content-Type: application/json\" \\     -X POST 'https://nla.zapier.com/api/v1/dynamic/exposed/01GTA3G1WD49GN1XXXXXXXXX/execute/' ```  One more example, this time requesting a preview of the action:  ``` curl -v \\     -d '{\"instructions\": \"say Hello World to #fun-zapier\", \"preview_only\": true}' \\     -H \"Content-Type: application/json\" \\     -X POST 'https://nla.zapier.com/api/v1/dynamic/exposed/01GTB1KMX72QTJEXXXXXXXXXX/execute/' ```   #### Execution Return Data <a name=\"return-data\"></a>  ##### The Status Key <a name=\"status-key\"></a>  All actions will contain a `status`. The status can be one of four values:  `success`  The action executed successfully and found results.  `error`  The action failed to execute. An `error` key will have its value populated.  Example:  ```     {         ...         \"action_used\": \"Gmail: Send Email\",         \"result\": null,         \"status\": \"error\",         \"error\": \"Error from app: Required field \"subject\" (subject) is missing. Required field \"Body\" (body) is missing.\"     } ```  `empty`  The action executed successfully, but no results were found. This status exists to be explicit that having an empty `result` is correct.  `preview`  The action is a preview and not a real execution. A `review_url` key will contain a URL to optionally execute the action from a browser, or just rerun without the `preview_only` input parameter.  Example:  ```     {         ...         \"action_used\": \"Slack: Send Channel Message\",         \"input_params\": {             \"Channel\": \"fun-zapier\",             \"Message_Text\": \"Hello World\"         },         \"review_url\": \"https://nla.zapier.com/execution/01GW2E2ZNE5W07D32E41HFT5GJ/?needs_confirmation=true\",         \"status\": \"preview\",     } ```  ##### The Result Key <a name=\"result-key\"></a>  All actions will return trimmed `result` data. `result` is ideal for humans and language models alike! By default, `full_results` is not included but can be useful for machines (contact us if you'd like access to full results). The trimmed version is created using some AI and heuristics:  * selects for data that is plain text and human readable * discards machine data like IDs, headers, etc. * prioritizes data that is very popular on Zapier * reduces final result into about ~500 words  Trimmed results are ideal for inserting directly back into the prompt context of a large language models without blowing up context token window limits.  Example of a trimmed results payload from \"Gmail: Find Email\":  ```     {         \"result\": {             \"from__email\": \"mike@zapier.com\",             \"from__name\": \"Mike Knoop\",             \"subject\": \"Re: Getting setup\",             \"body_plain\": \"Hi Karla, thanks for following up. I can confirm I got access to everything! ... Thanks! Mike\",             \"cc__emails\": \"bryan@zapier.com, wade@zapier.com\"             \"to__email\": \"Mike Knoop\",         }     } ``` ## Changelog <a name=\"changelog\"></a>  **Mar 20, 2023** Shipped two minor but breaking changes, and one other minor change to the API's response data:  * Route: `/api/v1/configuration-link/`   * Key `url` is now `configuration_link` **(breaking change)** * Route: `/api/v1/exposed/{exposed_app_action_id}/execute/`   * Key `rating_url` is now `review_url` **(breaking change)** * Route: `/api/v1/exposed/`   * Added `configuration_link` key
 *
 * The version of the OpenAPI document: 1.0.0
 * 
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
    constructor(basePath = 'https://nla.zapier.com') {
        /**
         * The base URL against which to resolve every API call's (relative) path.
         * @type {String}
         * @default https://nla.zapier.com
         */
        this.basePath = basePath.replace(/\/+$/, '');

        /**
         * The authentication methods to be included for all API calls.
         * @type {Array.<String>}
         */
        this.authentications = {
            'AccessPointApiKeyHeader': {type: 'apiKey', 'in': 'header', name: 'X-API-Key'},
            'AccessPointApiKeyQuery': {type: 'apiKey', 'in': 'query', name: 'api_key'},
            'AccessPointOAuth': {type: 'oauth2'},
            'SessionAuth': {type: 'apiKey', 'in': 'query', name: 'sessionid'}
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
              'url': "https://nla.zapier.com",
              'description': "No description provided",
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
