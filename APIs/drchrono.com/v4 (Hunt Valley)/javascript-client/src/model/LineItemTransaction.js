/**
 * 
 * This document is intended as a detailed reference for the precise behavior of the drchrono API. If this is your first time using the API, start with our <a href=\"/api-docs-old/tutorial\">tutorial</a>. If you are upgrading from a previous version, take a look at the changelog section.  # Authorization  ## Initial authorization  There are three main steps in the OAuth 2.0 authentication workflow:  1. Redirect the provider to the authorization page. 2. The provider authorizes your application and is redirected back to    your web application. 3. Your application exchanges the `authorization_code` that came with    the redirect for an `access_token` and `refresh_token`.  ### Step 1: Redirect to drchrono  The first step is redirecting your user to drchrono, typically with a button labeled \"Connect to drchrono\" or \"Login with drchrono\".  This is just a link that takes your user to the following URL:      https://drchrono.com/o/authorize/?redirect_uri=REDIRECT_URI_ENCODED&response_type=code&client_id=CLIENT_ID_ENCODED&scope=SCOPES_ENCODED  - `REDIRECT_URI_ENCODED` is the URL-encoded version of the redirect URI (as registered for your application and used in later steps). - `CLIENT_ID_ENCODED` is the URL-encoded version of your application's client ID. - `SCOPES_ENCODED` is a URL-encoded version of a space-separated list of scopes, which can be found in each endpoint or omitted to default to all scopes.  The `scope` parameter consists of an optional, space-separated list of scopes your application is requesting. If omitted, all scopes will be requested.  Scopes are of the form `BASE_SCOPE:[read|write]` where `BASE_SCOPE` is any of `user`, `calendar`, `patients`, `patients:summary`, `billing`, `clinical` and `labs`. You should request only the scopes you need. For instance, an application which sends \"Happy Birthday!\" emails to a doctor's patients on their birthdays would use the scope parameter `\"patients:summary:read\"`, while one that allows patients to schedule appointments online would need at least `\"patients:summary:read patients:summary:write calendar:read calendar:write clinical:read clinical:write\"`.  ### Step 2: Provider authorization  After logging in (if necessary), the provider will be presented with a screen with your application's name and the list of permissions you requested (via the `scope` parameter).  When they click the \"Authorize\" button, they will be redirected to your redirect URI with a `code` query parameter appended, which contains an authorization code to be used in step 3.  If they click the \"Cancel\" button, they will be redirected to your redirect URI with `error=access_denied` instead.  Note: This authorization code expires extremely quickly, so you must perform step 3 immediately, ideally before rendering the resulting page for the end user.  ### Step 3: Token exchange  The `code` obtained from step 2 is usable exactly once to obtain an access token and refresh token.  Here is an example token exchange in Python:      import datetime, pytz, requests      if 'error' in get_params:         raise ValueError('Error authorizing application: %s' % get_params[error])      response = requests.post('https://drchrono.com/o/token/', data={         'code': get_params['code'],         'grant_type': 'authorization_code',         'redirect_uri': 'http://mytestapp.com/redirect_uri',         'client_id': 'abcdefg12345',         'client_secret': 'abcdefg12345',     })     response.raise_for_status()     data = response.json()      # Save these in your database associated with the user     access_token = data['access_token']     refresh_token = data['refresh_token']     expires_timestamp = datetime.datetime.now(pytz.utc) + datetime.timedelta(seconds=data['expires_in'])  You now have all you need to make API requests authenticated as that provider. When using this access token, you'll only be able to access the data that the user has access to and that you have been granted permissions for.  ## Refreshing an access token  Access tokens only last 48 hours (given in seconds in the `'expires_in'` key in the token exchange step above), so they occasionally need to be refreshed.  It would be inconvenient to ask the user to re-authorize every time, so instead you can use the refresh token like the original authorization to obtain a new access token.  Replace the `code` parameter with `refresh_token`, change the value `grant_type` from `authorization_code` to `refresh_token`, and omit the `redirect_uri` parameter.  Example in Python:      ...     response = requests.post('https://drchrono.com/o/token/', data={         'refresh_token': get_refresh_token(),         'grant_type': 'refresh_token',         'client_id': 'abcdefg12345',         'client_secret': 'abcdefg12345',     })     ...  # Webhooks  In order to use drchrono API webhooks, you first need to have an API application on file (even if it is in Test Model). Each API webhook is associated with one API application, go to <a href=\"/api-management/\" target=\"_blank\">here</a> to set up both API applications and webhooks!  Once you registered an API application, you will see webhook section in each saved API applications. Create a webhook and register some events there and save all the changes, then you are good to go!  ## Webhooks setup  All fields under webhooks section are required.  **Callback URL** Callback URl is used to receive all hooks when subscribed events are triggered. This should be an URL under your control.  **Secret token** Secret token is used to verify webhooks, this is very important, please set something with high entropy. Also we will talk more about this later.  **Events**  Events is used to register events you want to receiver notification when they happen. Currently we support following events.  Event name | Event description ---------- | ----------------- `APPOINTMENT_CREATE` | We will deliver a hook any time an appointment is created `APPOINTMENT_MODIFY` | We will deliver a hook any time an appointment is modified `PATIENT_CREATE` | We will deliver a hook any time a patient is created `PATIENT_MODIFY` | We will deliver a hook any time a patient is modified `PATIENT_PROBLEM_CREATE` | We will deliver a hook any time a patient problem is created `PATIENT_PROBLEM_MODIFY` | We will deliver a hook any time a patient problem is modified `PATIENT_ALLERGY_CREATE` | We will deliver a hook any time a patient allergy is created `PATIENT_ALLERGY_MODIFY` | We will deliver a hook any time a patient allergy is modified `PATIENT_MEDICATION_CREATE` | We will deliver a hook any time a patient medication is created `PATIENT_MEDICATION_MODIFY` | We will deliver a hook any time a patient medication is modified `CLINICAL_NOTE_LOCK` | We will deliver a hook any time a clinical note is locked `CLINICAL_NOTE_UNLOCK` | We will deliver a hook any time a clinical note is unlocked `TASK_CREATE` | We will deliver a hook any time a task is created `TASK_MODIFY` | We will deliver a hook any time a task is modified and any time creation, modification and deletion of task notes, associated task item `TASK_DELETE` | We will deliver a hook any time a task is deleted   ## Webhooks verification  In order to make sure the callback URL in webhook is under your control, we added a verification step before we send any hooks out to you.  Verification can be done by clicking \"Verify webhook\" button in webhooks setup page. After you click the button, we will send a `GET` request to the callback URL, along with a parameter called `msg`.  Please use your webhook's secret token as hash key and SHA-256 as digest constructor, hash the `msg` value with <a href=\"https://tools.ietf.org/html/rfc2104.html\">HMAC algorithm</a>. And we expect a `200` JSON response, in JSON response body, there should be a key called `secret_token` existing, and its value should be equal to the <strong>hashed</strong> `msg`. Otherwise, verification will fail.  Here is an example webhook verification in Python:      import hashlib, hmac      def webhook_verify(request):         secret_token = hmac.new(WEBHOOK_SECRET_TOKEN, request.GET['msg'], hashlib.sha256).hexdigest()         return json_response({             'secret_token': secret_token         })  <div class=\"alert alert-warning\"> <b>Note:</b> Verification will be needed when webhook is first created and anytime callback URl is changed. </div>   ## Webhooks header and body  **Header**  Key | Value --- | ----- `X-drchrono-event` | Event that triggered this hook, could be any one event above or `PING` `X-drchrono-signature` | Secret token associated with this webhook `X-drchrono-delivery` | ID of this delivery  **Body**  Key | Value --- | ----- `receiver` | This will be an JSON representation of the webhook `object` | This will be an JSON representation of the object related to the triggered event, this would share same serializer as drchrono API  ## Webhooks ping and deliveries  Webhooks ping and deliveries will be sent as `POST` requests.  **PING**:  You can always ping your webhook to check things, by clicking the \"Ping webhook\" button in webhook setup page. And a hook with header `X-drchrono-event: PING` would be sent to the callback URL.  **Deliveries**:  You can check recent deliveries by clicking the \"deliveries\" link in webhook setup page. And you can resend a hook by clicking \"redeliver\" button after select a specific delivery.  ## Webhooks delivery mechanism  We will delivery a hook the moment a subscribed event is triggered. We will not record any response header or body you send back after you receive the hook. However we only consider the response status code. We will consider any `2xx` responses as successfully delivered. Any other responses, like `302` would be considered failing. And we will try to redeliver unsuccessfully delivered hooks 3 times, first redeliver happens at 1 hour after the initial event, second receliver happens 3 hours after the initial event, and the third redeliver happens 7 hours after the initial event. After these redeliveries, if the delivery is still unsuccessful, you have to redeliver it by hand.   ## Webhooks security  You may want to secure your webhooks to only consider requests send out from drchrono. And this is where <code>secret_token</code> is needed in request header. Try to set the <code>secret_token</code> to something with high entropy, a good example could be taking the output of <code>ruby -rsecurerandom -e 'puts SecureRandom.hex(20)'</code>. After this, you might want to verify all request headers you received on your server with this token.   # iframe integration  Some API apps provide additional functionality for interacting with patient data not offered by drchrono, and can benefit by being incorporated into drchrono's patient information page via iframe.  We have created a simple API to make this possible.  To make an existing API application accessible via an iframe on the patient page, you need to update either \"Patient iframe\" or \"Clinical note iframe\" section in API management page, to make the iframe to appear on (either the patient page or the clinical note page), with the URL that the iframe will use for each page, and the height it should have. The application will be reviewed before it is approved to ensure that it is functional and secure.  ## Register a Doctor  iframe applications will appear as choices on the left-hand menu of the patient page for doctors registered with your application.  To register a doctor with your application, make a `POST` request to the `/api/iframe_integration` endpoint using the access token for the corresponding doctor. This endpoint does not expect any payload.  To disable your iframe application for a doctor, make a `DELETE` request to the same endpoint.  ## Populating the iframe  There are two places where the iframe can be displayed, either within the patient detail page or the clinical note page, shown below respectively:  <img src=\"{% asset 'public/images/iframe_patient_page.png' %}\" alt=\"Iframe on the patient page\"/>  <img src=\"{% asset 'public/images/iframe_clinical_note.png' %}\" alt=\"Iframe on the clinical note page\"/>  When requesting approval for your iframe app, you must specify a URL for one or both of these pages which will serve as the base URL for your IFrame contents. When a doctor views your iframe, the source URL will have various query parameters appended to it, for example for the patient page the `src` parameter of the IFrame will be:  ``` <iframe_url>?doctor_id=<doctor_id>&patient_id=<patient_id>&practice_id=<practice_id>&iat=<iat>&jwt=<jwt> ```  The `jwt` parameter is crucial if your application transfers any sort of PHI and does not implement its own login system.  It encapsulates the other parameters in a [JSON web token (JWT)](http://jwt.io) and signs them using SHA-256 HMAC with your `client_secret` as the key.  This verifies that the iframe is being loaded within one of drchrono's pages by an authorized user.  In production, you should validate the JWT using an approved library (which are listed on the [official site](http://jwt.io)), and only use the parameters extracted from the JWT.  Using Python and Django, this might look like:      import jwt      CLIENT_SECRET = <client_secret>     MAX_TIME_DRIFT_SECONDS = 60      def validate_parameters(request):         token = request.GET['jwt']          return jwt.decode(token, CLIENT_SECRET, algorithms=['HS256'], leeway=MAX_TIME_DRIFT_SECONDS)  Modern browsers' same-origin policy means that data cannot be passed between your application and drchrono's page through the iframe.  Therefore, interaction must happen through the API, using information provided in JWT.  # Versions and deprecation  ## Stability Policy  Changes to this API version will be limited to adding endpoints, or adding fields to existing endpoints, or adding optional query parameters. Any new fields which are not read-only will be optional.  ## Deprecation Policy  The drchrono API is versioned. Versions can be in the following states:  * **Active:** This is our latest and greatest version of the API. It is actively supported by our API team and is improved upon with new features, bug fixes and optimizations that do not break backwards compatibility.  * **Deprecated:** A deprecated API version is considered second best--having been surpassed by our active API version. An API version remains in this state for one year, after which time it falls to the not supported state. A deprecated API version is passively supported; while it won't be removed until becoming unsupported, it may not receive new features but will likely be subject to security updates and performance improvements.  * **Unsupported:** An API version in the not supported state may be deactivated at any time. An application using an unsupported API version should migrate to an active API version.  ## Version Map | Version Name | Previous Name | Start Date | Deprecation Date | |--------------|---------------|------------|------------------| | v2           | v2015_08      | 08/2015    | TBA              | | v3           | v2016_06      | 06/2016    |                  | | v4           | N/A           | 09/2018    |                  |  If you are looking for documentation for an older version  - [V4(Hunt Valley)](/api-docs-old/v4/documentation) (old V4 documentation) - [V3(Sunnyvale)](/api-docs-old/v3/documentation) - [V2(Mountain View)](/api-docs-old/v2/documentation)  # Changelog  Here's changelog for different versions  - [V4 Changelog](/api-docs-old/v4/changelog) - [V3 changelog](/api-docs-old/v3/changelog)  
 *
 * The version of the OpenAPI document: v4 (Hunt Valley)
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The LineItemTransaction model module.
 * @module model/LineItemTransaction
 * @version v4 (Hunt Valley)
 */
class LineItemTransaction {
    /**
     * Constructs a new <code>LineItemTransaction</code>.
     * @alias module:model/LineItemTransaction
     */
    constructor() { 
        
        LineItemTransaction.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>LineItemTransaction</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/LineItemTransaction} obj Optional instance to populate.
     * @return {module:model/LineItemTransaction} The populated <code>LineItemTransaction</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new LineItemTransaction();

            if (data.hasOwnProperty('adjustment')) {
                obj['adjustment'] = ApiClient.convertToType(data['adjustment'], 'Number');
            }
            if (data.hasOwnProperty('adjustment_group_code')) {
                obj['adjustment_group_code'] = ApiClient.convertToType(data['adjustment_group_code'], 'String');
            }
            if (data.hasOwnProperty('adjustment_reason')) {
                obj['adjustment_reason'] = ApiClient.convertToType(data['adjustment_reason'], 'String');
            }
            if (data.hasOwnProperty('appointment')) {
                obj['appointment'] = ApiClient.convertToType(data['appointment'], 'Number');
            }
            if (data.hasOwnProperty('check_date')) {
                obj['check_date'] = ApiClient.convertToType(data['check_date'], 'String');
            }
            if (data.hasOwnProperty('claim_status')) {
                obj['claim_status'] = ApiClient.convertToType(data['claim_status'], 'String');
            }
            if (data.hasOwnProperty('created_at')) {
                obj['created_at'] = ApiClient.convertToType(data['created_at'], 'String');
            }
            if (data.hasOwnProperty('doctor')) {
                obj['doctor'] = ApiClient.convertToType(data['doctor'], 'Number');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('ins_name')) {
                obj['ins_name'] = ApiClient.convertToType(data['ins_name'], 'Number');
            }
            if (data.hasOwnProperty('ins_paid')) {
                obj['ins_paid'] = ApiClient.convertToType(data['ins_paid'], 'Number');
            }
            if (data.hasOwnProperty('line_item')) {
                obj['line_item'] = ApiClient.convertToType(data['line_item'], 'Number');
            }
            if (data.hasOwnProperty('patient')) {
                obj['patient'] = ApiClient.convertToType(data['patient'], 'Number');
            }
            if (data.hasOwnProperty('posted_date')) {
                obj['posted_date'] = ApiClient.convertToType(data['posted_date'], 'String');
            }
            if (data.hasOwnProperty('trace_number')) {
                obj['trace_number'] = ApiClient.convertToType(data['trace_number'], 'String');
            }
            if (data.hasOwnProperty('updated_at')) {
                obj['updated_at'] = ApiClient.convertToType(data['updated_at'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>LineItemTransaction</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>LineItemTransaction</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['adjustment_group_code'] && !(typeof data['adjustment_group_code'] === 'string' || data['adjustment_group_code'] instanceof String)) {
            throw new Error("Expected the field `adjustment_group_code` to be a primitive type in the JSON string but got " + data['adjustment_group_code']);
        }
        // ensure the json data is a string
        if (data['adjustment_reason'] && !(typeof data['adjustment_reason'] === 'string' || data['adjustment_reason'] instanceof String)) {
            throw new Error("Expected the field `adjustment_reason` to be a primitive type in the JSON string but got " + data['adjustment_reason']);
        }
        // ensure the json data is a string
        if (data['check_date'] && !(typeof data['check_date'] === 'string' || data['check_date'] instanceof String)) {
            throw new Error("Expected the field `check_date` to be a primitive type in the JSON string but got " + data['check_date']);
        }
        // ensure the json data is a string
        if (data['claim_status'] && !(typeof data['claim_status'] === 'string' || data['claim_status'] instanceof String)) {
            throw new Error("Expected the field `claim_status` to be a primitive type in the JSON string but got " + data['claim_status']);
        }
        // ensure the json data is a string
        if (data['created_at'] && !(typeof data['created_at'] === 'string' || data['created_at'] instanceof String)) {
            throw new Error("Expected the field `created_at` to be a primitive type in the JSON string but got " + data['created_at']);
        }
        // ensure the json data is a string
        if (data['posted_date'] && !(typeof data['posted_date'] === 'string' || data['posted_date'] instanceof String)) {
            throw new Error("Expected the field `posted_date` to be a primitive type in the JSON string but got " + data['posted_date']);
        }
        // ensure the json data is a string
        if (data['trace_number'] && !(typeof data['trace_number'] === 'string' || data['trace_number'] instanceof String)) {
            throw new Error("Expected the field `trace_number` to be a primitive type in the JSON string but got " + data['trace_number']);
        }
        // ensure the json data is a string
        if (data['updated_at'] && !(typeof data['updated_at'] === 'string' || data['updated_at'] instanceof String)) {
            throw new Error("Expected the field `updated_at` to be a primitive type in the JSON string but got " + data['updated_at']);
        }

        return true;
    }


}



/**
 * Adjustment from total billed
 * @member {Number} adjustment
 */
LineItemTransaction.prototype['adjustment'] = undefined;

/**
 * Group code for adjustment
 * @member {module:model/LineItemTransaction.AdjustmentGroupCodeEnum} adjustment_group_code
 */
LineItemTransaction.prototype['adjustment_group_code'] = undefined;

/**
 * Reason for adjustment
 * @member {module:model/LineItemTransaction.AdjustmentReasonEnum} adjustment_reason
 */
LineItemTransaction.prototype['adjustment_reason'] = undefined;

/**
 * Appointment ID
 * @member {Number} appointment
 */
LineItemTransaction.prototype['appointment'] = undefined;

/**
 * Date of check
 * @member {String} check_date
 */
LineItemTransaction.prototype['check_date'] = undefined;

/**
 * Status of claim
 * @member {module:model/LineItemTransaction.ClaimStatusEnum} claim_status
 */
LineItemTransaction.prototype['claim_status'] = undefined;

/**
 * 
 * @member {String} created_at
 */
LineItemTransaction.prototype['created_at'] = undefined;

/**
 * Doctor ID
 * @member {Number} doctor
 */
LineItemTransaction.prototype['doctor'] = undefined;

/**
 * 
 * @member {Number} id
 */
LineItemTransaction.prototype['id'] = undefined;

/**
 * Can be one of the following, `1`(Primary Insurance), `2`(Secondary Insurance)
 * @member {Number} ins_name
 */
LineItemTransaction.prototype['ins_name'] = undefined;

/**
 * 
 * @member {Number} ins_paid
 */
LineItemTransaction.prototype['ins_paid'] = undefined;

/**
 * ID of `/api/line_item` object
 * @member {Number} line_item
 */
LineItemTransaction.prototype['line_item'] = undefined;

/**
 * 
 * @member {Number} patient
 */
LineItemTransaction.prototype['patient'] = undefined;

/**
 * Date when transaction is created
 * @member {String} posted_date
 */
LineItemTransaction.prototype['posted_date'] = undefined;

/**
 * Check number
 * @member {String} trace_number
 */
LineItemTransaction.prototype['trace_number'] = undefined;

/**
 * 
 * @member {String} updated_at
 */
LineItemTransaction.prototype['updated_at'] = undefined;





/**
 * Allowed values for the <code>adjustment_group_code</code> property.
 * @enum {String}
 * @readonly
 */
LineItemTransaction['AdjustmentGroupCodeEnum'] = {

    /**
     * value: ""
     * @const
     */
    "empty": "",

    /**
     * value: "CO"
     * @const
     */
    "CO": "CO",

    /**
     * value: "OA"
     * @const
     */
    "OA": "OA",

    /**
     * value: "PI"
     * @const
     */
    "PI": "PI",

    /**
     * value: "PR"
     * @const
     */
    "PR": "PR"
};


/**
 * Allowed values for the <code>adjustment_reason</code> property.
 * @enum {String}
 * @readonly
 */
LineItemTransaction['AdjustmentReasonEnum'] = {

    /**
     * value: "-3"
     * @const
     */
    "-3": "-3",

    /**
     * value: "-2"
     * @const
     */
    "-2": "-2",

    /**
     * value: "-4"
     * @const
     */
    "-4": "-4",

    /**
     * value: "-1"
     * @const
     */
    "-1": "-1",

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
     * value: "10"
     * @const
     */
    "10": "10",

    /**
     * value: "11"
     * @const
     */
    "11": "11",

    /**
     * value: "12"
     * @const
     */
    "12": "12",

    /**
     * value: "13"
     * @const
     */
    "13": "13",

    /**
     * value: "14"
     * @const
     */
    "14": "14",

    /**
     * value: "15"
     * @const
     */
    "15": "15",

    /**
     * value: "16"
     * @const
     */
    "16": "16",

    /**
     * value: "18"
     * @const
     */
    "18": "18",

    /**
     * value: "19"
     * @const
     */
    "19": "19",

    /**
     * value: "20"
     * @const
     */
    "20": "20",

    /**
     * value: "21"
     * @const
     */
    "21": "21",

    /**
     * value: "22"
     * @const
     */
    "22": "22",

    /**
     * value: "23"
     * @const
     */
    "23": "23",

    /**
     * value: "24"
     * @const
     */
    "24": "24",

    /**
     * value: "26"
     * @const
     */
    "26": "26",

    /**
     * value: "27"
     * @const
     */
    "27": "27",

    /**
     * value: "29"
     * @const
     */
    "29": "29",

    /**
     * value: "31"
     * @const
     */
    "31": "31",

    /**
     * value: "32"
     * @const
     */
    "32": "32",

    /**
     * value: "33"
     * @const
     */
    "33": "33",

    /**
     * value: "34"
     * @const
     */
    "34": "34",

    /**
     * value: "35"
     * @const
     */
    "35": "35",

    /**
     * value: "39"
     * @const
     */
    "39": "39",

    /**
     * value: "40"
     * @const
     */
    "40": "40",

    /**
     * value: "44"
     * @const
     */
    "44": "44",

    /**
     * value: "45"
     * @const
     */
    "45": "45",

    /**
     * value: "49"
     * @const
     */
    "49": "49",

    /**
     * value: "50"
     * @const
     */
    "50": "50",

    /**
     * value: "51"
     * @const
     */
    "51": "51",

    /**
     * value: "53"
     * @const
     */
    "53": "53",

    /**
     * value: "54"
     * @const
     */
    "54": "54",

    /**
     * value: "55"
     * @const
     */
    "55": "55",

    /**
     * value: "56"
     * @const
     */
    "56": "56",

    /**
     * value: "58"
     * @const
     */
    "58": "58",

    /**
     * value: "59"
     * @const
     */
    "59": "59",

    /**
     * value: "60"
     * @const
     */
    "60": "60",

    /**
     * value: "61"
     * @const
     */
    "61": "61",

    /**
     * value: "66"
     * @const
     */
    "66": "66",

    /**
     * value: "69"
     * @const
     */
    "69": "69",

    /**
     * value: "70"
     * @const
     */
    "70": "70",

    /**
     * value: "74"
     * @const
     */
    "74": "74",

    /**
     * value: "75"
     * @const
     */
    "75": "75",

    /**
     * value: "76"
     * @const
     */
    "76": "76",

    /**
     * value: "78"
     * @const
     */
    "78": "78",

    /**
     * value: "85"
     * @const
     */
    "85": "85",

    /**
     * value: "87"
     * @const
     */
    "87": "87",

    /**
     * value: "89"
     * @const
     */
    "89": "89",

    /**
     * value: "90"
     * @const
     */
    "90": "90",

    /**
     * value: "91"
     * @const
     */
    "91": "91",

    /**
     * value: "94"
     * @const
     */
    "94": "94",

    /**
     * value: "95"
     * @const
     */
    "95": "95",

    /**
     * value: "96"
     * @const
     */
    "96": "96",

    /**
     * value: "97"
     * @const
     */
    "97": "97",

    /**
     * value: "100"
     * @const
     */
    "100": "100",

    /**
     * value: "101"
     * @const
     */
    "101": "101",

    /**
     * value: "102"
     * @const
     */
    "102": "102",

    /**
     * value: "103"
     * @const
     */
    "103": "103",

    /**
     * value: "104"
     * @const
     */
    "104": "104",

    /**
     * value: "105"
     * @const
     */
    "105": "105",

    /**
     * value: "106"
     * @const
     */
    "106": "106",

    /**
     * value: "107"
     * @const
     */
    "107": "107",

    /**
     * value: "108"
     * @const
     */
    "108": "108",

    /**
     * value: "109"
     * @const
     */
    "109": "109",

    /**
     * value: "110"
     * @const
     */
    "110": "110",

    /**
     * value: "111"
     * @const
     */
    "111": "111",

    /**
     * value: "112"
     * @const
     */
    "112": "112",

    /**
     * value: "114"
     * @const
     */
    "114": "114",

    /**
     * value: "115"
     * @const
     */
    "115": "115",

    /**
     * value: "116"
     * @const
     */
    "116": "116",

    /**
     * value: "117"
     * @const
     */
    "117": "117",

    /**
     * value: "118"
     * @const
     */
    "118": "118",

    /**
     * value: "119"
     * @const
     */
    "119": "119",

    /**
     * value: "121"
     * @const
     */
    "121": "121",

    /**
     * value: "122"
     * @const
     */
    "122": "122",

    /**
     * value: "125"
     * @const
     */
    "125": "125",

    /**
     * value: "128"
     * @const
     */
    "128": "128",

    /**
     * value: "129"
     * @const
     */
    "129": "129",

    /**
     * value: "130"
     * @const
     */
    "130": "130",

    /**
     * value: "131"
     * @const
     */
    "131": "131",

    /**
     * value: "132"
     * @const
     */
    "132": "132",

    /**
     * value: "133"
     * @const
     */
    "133": "133",

    /**
     * value: "134"
     * @const
     */
    "134": "134",

    /**
     * value: "135"
     * @const
     */
    "135": "135",

    /**
     * value: "136"
     * @const
     */
    "136": "136",

    /**
     * value: "137"
     * @const
     */
    "137": "137",

    /**
     * value: "138"
     * @const
     */
    "138": "138",

    /**
     * value: "139"
     * @const
     */
    "139": "139",

    /**
     * value: "140"
     * @const
     */
    "140": "140",

    /**
     * value: "142"
     * @const
     */
    "142": "142",

    /**
     * value: "143"
     * @const
     */
    "143": "143",

    /**
     * value: "144"
     * @const
     */
    "144": "144",

    /**
     * value: "146"
     * @const
     */
    "146": "146",

    /**
     * value: "147"
     * @const
     */
    "147": "147",

    /**
     * value: "148"
     * @const
     */
    "148": "148",

    /**
     * value: "149"
     * @const
     */
    "149": "149",

    /**
     * value: "150"
     * @const
     */
    "150": "150",

    /**
     * value: "151"
     * @const
     */
    "151": "151",

    /**
     * value: "152"
     * @const
     */
    "152": "152",

    /**
     * value: "153"
     * @const
     */
    "153": "153",

    /**
     * value: "154"
     * @const
     */
    "154": "154",

    /**
     * value: "155"
     * @const
     */
    "155": "155",

    /**
     * value: "157"
     * @const
     */
    "157": "157",

    /**
     * value: "158"
     * @const
     */
    "158": "158",

    /**
     * value: "159"
     * @const
     */
    "159": "159",

    /**
     * value: "160"
     * @const
     */
    "160": "160",

    /**
     * value: "161"
     * @const
     */
    "161": "161",

    /**
     * value: "162"
     * @const
     */
    "162": "162",

    /**
     * value: "163"
     * @const
     */
    "163": "163",

    /**
     * value: "164"
     * @const
     */
    "164": "164",

    /**
     * value: "165"
     * @const
     */
    "165": "165",

    /**
     * value: "166"
     * @const
     */
    "166": "166",

    /**
     * value: "167"
     * @const
     */
    "167": "167",

    /**
     * value: "168"
     * @const
     */
    "168": "168",

    /**
     * value: "169"
     * @const
     */
    "169": "169",

    /**
     * value: "170"
     * @const
     */
    "170": "170",

    /**
     * value: "171"
     * @const
     */
    "171": "171",

    /**
     * value: "172"
     * @const
     */
    "172": "172",

    /**
     * value: "173"
     * @const
     */
    "173": "173",

    /**
     * value: "174"
     * @const
     */
    "174": "174",

    /**
     * value: "175"
     * @const
     */
    "175": "175",

    /**
     * value: "176"
     * @const
     */
    "176": "176",

    /**
     * value: "177"
     * @const
     */
    "177": "177",

    /**
     * value: "178"
     * @const
     */
    "178": "178",

    /**
     * value: "179"
     * @const
     */
    "179": "179",

    /**
     * value: "180"
     * @const
     */
    "180": "180",

    /**
     * value: "181"
     * @const
     */
    "181": "181",

    /**
     * value: "182"
     * @const
     */
    "182": "182",

    /**
     * value: "183"
     * @const
     */
    "183": "183",

    /**
     * value: "184"
     * @const
     */
    "184": "184",

    /**
     * value: "185"
     * @const
     */
    "185": "185",

    /**
     * value: "186"
     * @const
     */
    "186": "186",

    /**
     * value: "187"
     * @const
     */
    "187": "187",

    /**
     * value: "188"
     * @const
     */
    "188": "188",

    /**
     * value: "189"
     * @const
     */
    "189": "189",

    /**
     * value: "190"
     * @const
     */
    "190": "190",

    /**
     * value: "191"
     * @const
     */
    "191": "191",

    /**
     * value: "192"
     * @const
     */
    "192": "192",

    /**
     * value: "193"
     * @const
     */
    "193": "193",

    /**
     * value: "194"
     * @const
     */
    "194": "194",

    /**
     * value: "195"
     * @const
     */
    "195": "195",

    /**
     * value: "197"
     * @const
     */
    "197": "197",

    /**
     * value: "198"
     * @const
     */
    "198": "198",

    /**
     * value: "199"
     * @const
     */
    "199": "199",

    /**
     * value: "200"
     * @const
     */
    "200": "200",

    /**
     * value: "201"
     * @const
     */
    "201": "201",

    /**
     * value: "202"
     * @const
     */
    "202": "202",

    /**
     * value: "203"
     * @const
     */
    "203": "203",

    /**
     * value: "204"
     * @const
     */
    "204": "204",

    /**
     * value: "205"
     * @const
     */
    "205": "205",

    /**
     * value: "206"
     * @const
     */
    "206": "206",

    /**
     * value: "207"
     * @const
     */
    "207": "207",

    /**
     * value: "208"
     * @const
     */
    "208": "208",

    /**
     * value: "209"
     * @const
     */
    "209": "209",

    /**
     * value: "210"
     * @const
     */
    "210": "210",

    /**
     * value: "211"
     * @const
     */
    "211": "211",

    /**
     * value: "212"
     * @const
     */
    "212": "212",

    /**
     * value: "213"
     * @const
     */
    "213": "213",

    /**
     * value: "214"
     * @const
     */
    "214": "214",

    /**
     * value: "215"
     * @const
     */
    "215": "215",

    /**
     * value: "216"
     * @const
     */
    "216": "216",

    /**
     * value: "217"
     * @const
     */
    "217": "217",

    /**
     * value: "218"
     * @const
     */
    "218": "218",

    /**
     * value: "219"
     * @const
     */
    "219": "219",

    /**
     * value: "220"
     * @const
     */
    "220": "220",

    /**
     * value: "221"
     * @const
     */
    "221": "221",

    /**
     * value: "222"
     * @const
     */
    "222": "222",

    /**
     * value: "223"
     * @const
     */
    "223": "223",

    /**
     * value: "224"
     * @const
     */
    "224": "224",

    /**
     * value: "225"
     * @const
     */
    "225": "225",

    /**
     * value: "226"
     * @const
     */
    "226": "226",

    /**
     * value: "227"
     * @const
     */
    "227": "227",

    /**
     * value: "228"
     * @const
     */
    "228": "228",

    /**
     * value: "229"
     * @const
     */
    "229": "229",

    /**
     * value: "230"
     * @const
     */
    "230": "230",

    /**
     * value: "231"
     * @const
     */
    "231": "231",

    /**
     * value: "232"
     * @const
     */
    "232": "232",

    /**
     * value: "233"
     * @const
     */
    "233": "233",

    /**
     * value: "234"
     * @const
     */
    "234": "234",

    /**
     * value: "235"
     * @const
     */
    "235": "235",

    /**
     * value: "236"
     * @const
     */
    "236": "236",

    /**
     * value: "237"
     * @const
     */
    "237": "237",

    /**
     * value: "238"
     * @const
     */
    "238": "238",

    /**
     * value: "239"
     * @const
     */
    "239": "239",

    /**
     * value: "240"
     * @const
     */
    "240": "240",

    /**
     * value: "241"
     * @const
     */
    "241": "241",

    /**
     * value: "242"
     * @const
     */
    "242": "242",

    /**
     * value: "243"
     * @const
     */
    "243": "243",

    /**
     * value: "244"
     * @const
     */
    "244": "244",

    /**
     * value: "245"
     * @const
     */
    "245": "245",

    /**
     * value: "246"
     * @const
     */
    "246": "246",

    /**
     * value: "247"
     * @const
     */
    "247": "247",

    /**
     * value: "248"
     * @const
     */
    "248": "248",

    /**
     * value: "249"
     * @const
     */
    "249": "249",

    /**
     * value: "250"
     * @const
     */
    "250": "250",

    /**
     * value: "251"
     * @const
     */
    "251": "251",

    /**
     * value: "252"
     * @const
     */
    "252": "252",

    /**
     * value: "253"
     * @const
     */
    "253": "253",

    /**
     * value: "254"
     * @const
     */
    "254": "254",

    /**
     * value: "256"
     * @const
     */
    "256": "256",

    /**
     * value: "257"
     * @const
     */
    "257": "257",

    /**
     * value: "258"
     * @const
     */
    "258": "258",

    /**
     * value: "259"
     * @const
     */
    "259": "259",

    /**
     * value: "260"
     * @const
     */
    "260": "260",

    /**
     * value: "261"
     * @const
     */
    "261": "261",

    /**
     * value: "262"
     * @const
     */
    "262": "262",

    /**
     * value: "263"
     * @const
     */
    "263": "263",

    /**
     * value: "264"
     * @const
     */
    "264": "264",

    /**
     * value: "265"
     * @const
     */
    "265": "265",

    /**
     * value: "266"
     * @const
     */
    "266": "266",

    /**
     * value: "267"
     * @const
     */
    "267": "267",

    /**
     * value: "268"
     * @const
     */
    "268": "268",

    /**
     * value: "269"
     * @const
     */
    "269": "269",

    /**
     * value: "270"
     * @const
     */
    "270": "270",

    /**
     * value: "271"
     * @const
     */
    "271": "271",

    /**
     * value: "272"
     * @const
     */
    "272": "272",

    /**
     * value: "273"
     * @const
     */
    "273": "273",

    /**
     * value: "274"
     * @const
     */
    "274": "274",

    /**
     * value: "275"
     * @const
     */
    "275": "275",

    /**
     * value: "276"
     * @const
     */
    "276": "276",

    /**
     * value: "277"
     * @const
     */
    "277": "277",

    /**
     * value: "287"
     * @const
     */
    "287": "287",

    /**
     * value: "288"
     * @const
     */
    "288": "288",

    /**
     * value: "A0"
     * @const
     */
    "A0": "A0",

    /**
     * value: "A1"
     * @const
     */
    "A1": "A1",

    /**
     * value: "A5"
     * @const
     */
    "A5": "A5",

    /**
     * value: "A6"
     * @const
     */
    "A6": "A6",

    /**
     * value: "A7"
     * @const
     */
    "A7": "A7",

    /**
     * value: "A8"
     * @const
     */
    "A8": "A8",

    /**
     * value: "B1"
     * @const
     */
    "B1": "B1",

    /**
     * value: "B4"
     * @const
     */
    "B4": "B4",

    /**
     * value: "B5"
     * @const
     */
    "B5": "B5",

    /**
     * value: "B7"
     * @const
     */
    "B7": "B7",

    /**
     * value: "B8"
     * @const
     */
    "B8": "B8",

    /**
     * value: "B9"
     * @const
     */
    "B9": "B9",

    /**
     * value: "B10"
     * @const
     */
    "B10": "B10",

    /**
     * value: "B11"
     * @const
     */
    "B11": "B11",

    /**
     * value: "B12"
     * @const
     */
    "B12": "B12",

    /**
     * value: "B13"
     * @const
     */
    "B13": "B13",

    /**
     * value: "B14"
     * @const
     */
    "B14": "B14",

    /**
     * value: "B15"
     * @const
     */
    "B15": "B15",

    /**
     * value: "B16"
     * @const
     */
    "B16": "B16",

    /**
     * value: "B20"
     * @const
     */
    "B20": "B20",

    /**
     * value: "B22"
     * @const
     */
    "B22": "B22",

    /**
     * value: "B23"
     * @const
     */
    "B23": "B23",

    /**
     * value: "P1"
     * @const
     */
    "P1": "P1",

    /**
     * value: "P2"
     * @const
     */
    "P2": "P2",

    /**
     * value: "P3"
     * @const
     */
    "P3": "P3",

    /**
     * value: "P4"
     * @const
     */
    "P4": "P4",

    /**
     * value: "P5"
     * @const
     */
    "P5": "P5",

    /**
     * value: "P6"
     * @const
     */
    "P6": "P6",

    /**
     * value: "P7"
     * @const
     */
    "P7": "P7",

    /**
     * value: "P8"
     * @const
     */
    "P8": "P8",

    /**
     * value: "P9"
     * @const
     */
    "P9": "P9",

    /**
     * value: "P10"
     * @const
     */
    "P10": "P10",

    /**
     * value: "P11"
     * @const
     */
    "P11": "P11",

    /**
     * value: "P12"
     * @const
     */
    "P12": "P12",

    /**
     * value: "P13"
     * @const
     */
    "P13": "P13",

    /**
     * value: "P14"
     * @const
     */
    "P14": "P14",

    /**
     * value: "P15"
     * @const
     */
    "P15": "P15",

    /**
     * value: "P16"
     * @const
     */
    "P16": "P16",

    /**
     * value: "P17"
     * @const
     */
    "P17": "P17",

    /**
     * value: "P18"
     * @const
     */
    "P18": "P18",

    /**
     * value: "P19"
     * @const
     */
    "P19": "P19",

    /**
     * value: "P20"
     * @const
     */
    "P20": "P20",

    /**
     * value: "P21"
     * @const
     */
    "P21": "P21",

    /**
     * value: "P22"
     * @const
     */
    "P22": "P22",

    /**
     * value: "P23"
     * @const
     */
    "P23": "P23",

    /**
     * value: "W1"
     * @const
     */
    "W1": "W1",

    /**
     * value: "W2"
     * @const
     */
    "W2": "W2",

    /**
     * value: "W3"
     * @const
     */
    "W3": "W3",

    /**
     * value: "W4"
     * @const
     */
    "W4": "W4",

    /**
     * value: "Y1"
     * @const
     */
    "Y1": "Y1",

    /**
     * value: "Y2"
     * @const
     */
    "Y2": "Y2",

    /**
     * value: "Y3"
     * @const
     */
    "Y3": "Y3"
};


/**
 * Allowed values for the <code>claim_status</code> property.
 * @enum {String}
 * @readonly
 */
LineItemTransaction['ClaimStatusEnum'] = {

    /**
     * value: ""
     * @const
     */
    "empty": "",

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
     * value: "10"
     * @const
     */
    "10": "10",

    /**
     * value: "13"
     * @const
     */
    "13": "13",

    /**
     * value: "15"
     * @const
     */
    "15": "15",

    /**
     * value: "16"
     * @const
     */
    "16": "16",

    /**
     * value: "17"
     * @const
     */
    "17": "17",

    /**
     * value: "19"
     * @const
     */
    "19": "19",

    /**
     * value: "20"
     * @const
     */
    "20": "20",

    /**
     * value: "21"
     * @const
     */
    "21": "21",

    /**
     * value: "22"
     * @const
     */
    "22": "22",

    /**
     * value: "23"
     * @const
     */
    "23": "23",

    /**
     * value: "25"
     * @const
     */
    "25": "25",

    /**
     * value: "27"
     * @const
     */
    "27": "27"
};



export default LineItemTransaction;

