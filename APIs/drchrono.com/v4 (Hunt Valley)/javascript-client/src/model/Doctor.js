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
 * The Doctor model module.
 * @module model/Doctor
 * @version v4 (Hunt Valley)
 */
class Doctor {
    /**
     * Constructs a new <code>Doctor</code>.
     * @alias module:model/Doctor
     */
    constructor() { 
        
        Doctor.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Doctor</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Doctor} obj Optional instance to populate.
     * @return {module:model/Doctor} The populated <code>Doctor</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Doctor();

            if (data.hasOwnProperty('cell_phone')) {
                obj['cell_phone'] = ApiClient.convertToType(data['cell_phone'], 'String');
            }
            if (data.hasOwnProperty('country')) {
                obj['country'] = ApiClient.convertToType(data['country'], 'String');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('first_name')) {
                obj['first_name'] = ApiClient.convertToType(data['first_name'], 'String');
            }
            if (data.hasOwnProperty('group_npi_number')) {
                obj['group_npi_number'] = ApiClient.convertToType(data['group_npi_number'], 'String');
            }
            if (data.hasOwnProperty('home_phone')) {
                obj['home_phone'] = ApiClient.convertToType(data['home_phone'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('is_account_suspended')) {
                obj['is_account_suspended'] = ApiClient.convertToType(data['is_account_suspended'], 'Boolean');
            }
            if (data.hasOwnProperty('job_title')) {
                obj['job_title'] = ApiClient.convertToType(data['job_title'], 'String');
            }
            if (data.hasOwnProperty('last_name')) {
                obj['last_name'] = ApiClient.convertToType(data['last_name'], 'String');
            }
            if (data.hasOwnProperty('npi_number')) {
                obj['npi_number'] = ApiClient.convertToType(data['npi_number'], 'String');
            }
            if (data.hasOwnProperty('office_phone')) {
                obj['office_phone'] = ApiClient.convertToType(data['office_phone'], 'String');
            }
            if (data.hasOwnProperty('practice_group')) {
                obj['practice_group'] = ApiClient.convertToType(data['practice_group'], 'String');
            }
            if (data.hasOwnProperty('practice_group_name')) {
                obj['practice_group_name'] = ApiClient.convertToType(data['practice_group_name'], 'String');
            }
            if (data.hasOwnProperty('profile_picture')) {
                obj['profile_picture'] = ApiClient.convertToType(data['profile_picture'], 'String');
            }
            if (data.hasOwnProperty('specialty')) {
                obj['specialty'] = ApiClient.convertToType(data['specialty'], 'String');
            }
            if (data.hasOwnProperty('suffix')) {
                obj['suffix'] = ApiClient.convertToType(data['suffix'], 'String');
            }
            if (data.hasOwnProperty('timezone')) {
                obj['timezone'] = ApiClient.convertToType(data['timezone'], 'String');
            }
            if (data.hasOwnProperty('website')) {
                obj['website'] = ApiClient.convertToType(data['website'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Doctor</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Doctor</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['cell_phone'] && !(typeof data['cell_phone'] === 'string' || data['cell_phone'] instanceof String)) {
            throw new Error("Expected the field `cell_phone` to be a primitive type in the JSON string but got " + data['cell_phone']);
        }
        // ensure the json data is a string
        if (data['country'] && !(typeof data['country'] === 'string' || data['country'] instanceof String)) {
            throw new Error("Expected the field `country` to be a primitive type in the JSON string but got " + data['country']);
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['first_name'] && !(typeof data['first_name'] === 'string' || data['first_name'] instanceof String)) {
            throw new Error("Expected the field `first_name` to be a primitive type in the JSON string but got " + data['first_name']);
        }
        // ensure the json data is a string
        if (data['group_npi_number'] && !(typeof data['group_npi_number'] === 'string' || data['group_npi_number'] instanceof String)) {
            throw new Error("Expected the field `group_npi_number` to be a primitive type in the JSON string but got " + data['group_npi_number']);
        }
        // ensure the json data is a string
        if (data['home_phone'] && !(typeof data['home_phone'] === 'string' || data['home_phone'] instanceof String)) {
            throw new Error("Expected the field `home_phone` to be a primitive type in the JSON string but got " + data['home_phone']);
        }
        // ensure the json data is a string
        if (data['job_title'] && !(typeof data['job_title'] === 'string' || data['job_title'] instanceof String)) {
            throw new Error("Expected the field `job_title` to be a primitive type in the JSON string but got " + data['job_title']);
        }
        // ensure the json data is a string
        if (data['last_name'] && !(typeof data['last_name'] === 'string' || data['last_name'] instanceof String)) {
            throw new Error("Expected the field `last_name` to be a primitive type in the JSON string but got " + data['last_name']);
        }
        // ensure the json data is a string
        if (data['npi_number'] && !(typeof data['npi_number'] === 'string' || data['npi_number'] instanceof String)) {
            throw new Error("Expected the field `npi_number` to be a primitive type in the JSON string but got " + data['npi_number']);
        }
        // ensure the json data is a string
        if (data['office_phone'] && !(typeof data['office_phone'] === 'string' || data['office_phone'] instanceof String)) {
            throw new Error("Expected the field `office_phone` to be a primitive type in the JSON string but got " + data['office_phone']);
        }
        // ensure the json data is a string
        if (data['practice_group'] && !(typeof data['practice_group'] === 'string' || data['practice_group'] instanceof String)) {
            throw new Error("Expected the field `practice_group` to be a primitive type in the JSON string but got " + data['practice_group']);
        }
        // ensure the json data is a string
        if (data['practice_group_name'] && !(typeof data['practice_group_name'] === 'string' || data['practice_group_name'] instanceof String)) {
            throw new Error("Expected the field `practice_group_name` to be a primitive type in the JSON string but got " + data['practice_group_name']);
        }
        // ensure the json data is a string
        if (data['profile_picture'] && !(typeof data['profile_picture'] === 'string' || data['profile_picture'] instanceof String)) {
            throw new Error("Expected the field `profile_picture` to be a primitive type in the JSON string but got " + data['profile_picture']);
        }
        // ensure the json data is a string
        if (data['specialty'] && !(typeof data['specialty'] === 'string' || data['specialty'] instanceof String)) {
            throw new Error("Expected the field `specialty` to be a primitive type in the JSON string but got " + data['specialty']);
        }
        // ensure the json data is a string
        if (data['suffix'] && !(typeof data['suffix'] === 'string' || data['suffix'] instanceof String)) {
            throw new Error("Expected the field `suffix` to be a primitive type in the JSON string but got " + data['suffix']);
        }
        // ensure the json data is a string
        if (data['timezone'] && !(typeof data['timezone'] === 'string' || data['timezone'] instanceof String)) {
            throw new Error("Expected the field `timezone` to be a primitive type in the JSON string but got " + data['timezone']);
        }
        // ensure the json data is a string
        if (data['website'] && !(typeof data['website'] === 'string' || data['website'] instanceof String)) {
            throw new Error("Expected the field `website` to be a primitive type in the JSON string but got " + data['website']);
        }

        return true;
    }


}



/**
 * 
 * @member {String} cell_phone
 */
Doctor.prototype['cell_phone'] = undefined;

/**
 * Two-letter conutry code. Default is `US`
 * @member {module:model/Doctor.CountryEnum} country
 */
Doctor.prototype['country'] = undefined;

/**
 * 
 * @member {String} email
 */
Doctor.prototype['email'] = undefined;

/**
 * 
 * @member {String} first_name
 */
Doctor.prototype['first_name'] = undefined;

/**
 * 
 * @member {String} group_npi_number
 */
Doctor.prototype['group_npi_number'] = undefined;

/**
 * 
 * @member {String} home_phone
 */
Doctor.prototype['home_phone'] = undefined;

/**
 * 
 * @member {Number} id
 */
Doctor.prototype['id'] = undefined;

/**
 * Indicates the doctor's account is suspended or not
 * @member {Boolean} is_account_suspended
 */
Doctor.prototype['is_account_suspended'] = undefined;

/**
 * 
 * @member {module:model/Doctor.JobTitleEnum} job_title
 */
Doctor.prototype['job_title'] = undefined;

/**
 * 
 * @member {String} last_name
 */
Doctor.prototype['last_name'] = undefined;

/**
 * If both this field and `group_npi_number` are set, prefer this field
 * @member {String} npi_number
 */
Doctor.prototype['npi_number'] = undefined;

/**
 * 
 * @member {String} office_phone
 */
Doctor.prototype['office_phone'] = undefined;

/**
 * The ID of the practice group this user belongs to. This can be used to identify users in the same practice.
 * @member {String} practice_group
 */
Doctor.prototype['practice_group'] = undefined;

/**
 * 
 * @member {String} practice_group_name
 */
Doctor.prototype['practice_group_name'] = undefined;

/**
 * 
 * @member {String} profile_picture
 */
Doctor.prototype['profile_picture'] = undefined;

/**
 * 
 * @member {String} specialty
 */
Doctor.prototype['specialty'] = undefined;

/**
 * 
 * @member {String} suffix
 */
Doctor.prototype['suffix'] = undefined;

/**
 * 
 * @member {String} timezone
 */
Doctor.prototype['timezone'] = undefined;

/**
 * 
 * @member {String} website
 */
Doctor.prototype['website'] = undefined;





/**
 * Allowed values for the <code>country</code> property.
 * @enum {String}
 * @readonly
 */
Doctor['CountryEnum'] = {

    /**
     * value: "BD"
     * @const
     */
    "BD": "BD",

    /**
     * value: "WF"
     * @const
     */
    "WF": "WF",

    /**
     * value: "BF"
     * @const
     */
    "BF": "BF",

    /**
     * value: "BG"
     * @const
     */
    "BG": "BG",

    /**
     * value: "BA"
     * @const
     */
    "BA": "BA",

    /**
     * value: "BB"
     * @const
     */
    "BB": "BB",

    /**
     * value: "BE"
     * @const
     */
    "BE": "BE",

    /**
     * value: "BL"
     * @const
     */
    "BL": "BL",

    /**
     * value: "BM"
     * @const
     */
    "BM": "BM",

    /**
     * value: "BN"
     * @const
     */
    "BN": "BN",

    /**
     * value: "BO"
     * @const
     */
    "BO": "BO",

    /**
     * value: "JP"
     * @const
     */
    "JP": "JP",

    /**
     * value: "BI"
     * @const
     */
    "BI": "BI",

    /**
     * value: "BJ"
     * @const
     */
    "BJ": "BJ",

    /**
     * value: "BT"
     * @const
     */
    "BT": "BT",

    /**
     * value: "JM"
     * @const
     */
    "JM": "JM",

    /**
     * value: "BV"
     * @const
     */
    "BV": "BV",

    /**
     * value: "JO"
     * @const
     */
    "JO": "JO",

    /**
     * value: "WS"
     * @const
     */
    "WS": "WS",

    /**
     * value: "BQ"
     * @const
     */
    "BQ": "BQ",

    /**
     * value: "BR"
     * @const
     */
    "BR": "BR",

    /**
     * value: "BS"
     * @const
     */
    "BS": "BS",

    /**
     * value: "JE"
     * @const
     */
    "JE": "JE",

    /**
     * value: "BY"
     * @const
     */
    "BY": "BY",

    /**
     * value: "BZ"
     * @const
     */
    "BZ": "BZ",

    /**
     * value: "RU"
     * @const
     */
    "RU": "RU",

    /**
     * value: "RW"
     * @const
     */
    "RW": "RW",

    /**
     * value: "RS"
     * @const
     */
    "RS": "RS",

    /**
     * value: "TL"
     * @const
     */
    "TL": "TL",

    /**
     * value: "RE"
     * @const
     */
    "RE": "RE",

    /**
     * value: "TM"
     * @const
     */
    "TM": "TM",

    /**
     * value: "TJ"
     * @const
     */
    "TJ": "TJ",

    /**
     * value: "RO"
     * @const
     */
    "RO": "RO",

    /**
     * value: "TK"
     * @const
     */
    "TK": "TK",

    /**
     * value: "GW"
     * @const
     */
    "GW": "GW",

    /**
     * value: "GU"
     * @const
     */
    "GU": "GU",

    /**
     * value: "GT"
     * @const
     */
    "GT": "GT",

    /**
     * value: "GS"
     * @const
     */
    "GS": "GS",

    /**
     * value: "GR"
     * @const
     */
    "GR": "GR",

    /**
     * value: "GQ"
     * @const
     */
    "GQ": "GQ",

    /**
     * value: "GP"
     * @const
     */
    "GP": "GP",

    /**
     * value: "BH"
     * @const
     */
    "BH": "BH",

    /**
     * value: "GY"
     * @const
     */
    "GY": "GY",

    /**
     * value: "GG"
     * @const
     */
    "GG": "GG",

    /**
     * value: "GF"
     * @const
     */
    "GF": "GF",

    /**
     * value: "GE"
     * @const
     */
    "GE": "GE",

    /**
     * value: "GD"
     * @const
     */
    "GD": "GD",

    /**
     * value: "GB"
     * @const
     */
    "GB": "GB",

    /**
     * value: "GA"
     * @const
     */
    "GA": "GA",

    /**
     * value: "GN"
     * @const
     */
    "GN": "GN",

    /**
     * value: "GM"
     * @const
     */
    "GM": "GM",

    /**
     * value: "GL"
     * @const
     */
    "GL": "GL",

    /**
     * value: "KW"
     * @const
     */
    "KW": "KW",

    /**
     * value: "GI"
     * @const
     */
    "GI": "GI",

    /**
     * value: "GH"
     * @const
     */
    "GH": "GH",

    /**
     * value: "OM"
     * @const
     */
    "OM": "OM",

    /**
     * value: "TN"
     * @const
     */
    "TN": "TN",

    /**
     * value: "BW"
     * @const
     */
    "BW": "BW",

    /**
     * value: "HR"
     * @const
     */
    "HR": "HR",

    /**
     * value: "HT"
     * @const
     */
    "HT": "HT",

    /**
     * value: "HU"
     * @const
     */
    "HU": "HU",

    /**
     * value: "HK"
     * @const
     */
    "HK": "HK",

    /**
     * value: "HN"
     * @const
     */
    "HN": "HN",

    /**
     * value: "HM"
     * @const
     */
    "HM": "HM",

    /**
     * value: "KR"
     * @const
     */
    "KR": "KR",

    /**
     * value: "AD"
     * @const
     */
    "AD": "AD",

    /**
     * value: "PR"
     * @const
     */
    "PR": "PR",

    /**
     * value: "PS"
     * @const
     */
    "PS": "PS",

    /**
     * value: "PW"
     * @const
     */
    "PW": "PW",

    /**
     * value: "PT"
     * @const
     */
    "PT": "PT",

    /**
     * value: "KN"
     * @const
     */
    "KN": "KN",

    /**
     * value: "PY"
     * @const
     */
    "PY": "PY",

    /**
     * value: "AI"
     * @const
     */
    "AI": "AI",

    /**
     * value: "PA"
     * @const
     */
    "PA": "PA",

    /**
     * value: "PF"
     * @const
     */
    "PF": "PF",

    /**
     * value: "PG"
     * @const
     */
    "PG": "PG",

    /**
     * value: "PE"
     * @const
     */
    "PE": "PE",

    /**
     * value: "PK"
     * @const
     */
    "PK": "PK",

    /**
     * value: "PH"
     * @const
     */
    "PH": "PH",

    /**
     * value: "PN"
     * @const
     */
    "PN": "PN",

    /**
     * value: "PL"
     * @const
     */
    "PL": "PL",

    /**
     * value: "PM"
     * @const
     */
    "PM": "PM",

    /**
     * value: "ZM"
     * @const
     */
    "ZM": "ZM",

    /**
     * value: "EH"
     * @const
     */
    "EH": "EH",

    /**
     * value: "EE"
     * @const
     */
    "EE": "EE",

    /**
     * value: "EG"
     * @const
     */
    "EG": "EG",

    /**
     * value: "ZA"
     * @const
     */
    "ZA": "ZA",

    /**
     * value: "EC"
     * @const
     */
    "EC": "EC",

    /**
     * value: "AL"
     * @const
     */
    "AL": "AL",

    /**
     * value: "AO"
     * @const
     */
    "AO": "AO",

    /**
     * value: "KZ"
     * @const
     */
    "KZ": "KZ",

    /**
     * value: "ET"
     * @const
     */
    "ET": "ET",

    /**
     * value: "ZW"
     * @const
     */
    "ZW": "ZW",

    /**
     * value: "KY"
     * @const
     */
    "KY": "KY",

    /**
     * value: "ES"
     * @const
     */
    "ES": "ES",

    /**
     * value: "ER"
     * @const
     */
    "ER": "ER",

    /**
     * value: "ME"
     * @const
     */
    "ME": "ME",

    /**
     * value: "MD"
     * @const
     */
    "MD": "MD",

    /**
     * value: "MG"
     * @const
     */
    "MG": "MG",

    /**
     * value: "MF"
     * @const
     */
    "MF": "MF",

    /**
     * value: "MA"
     * @const
     */
    "MA": "MA",

    /**
     * value: "MC"
     * @const
     */
    "MC": "MC",

    /**
     * value: "UZ"
     * @const
     */
    "UZ": "UZ",

    /**
     * value: "MM"
     * @const
     */
    "MM": "MM",

    /**
     * value: "ML"
     * @const
     */
    "ML": "ML",

    /**
     * value: "MO"
     * @const
     */
    "MO": "MO",

    /**
     * value: "MN"
     * @const
     */
    "MN": "MN",

    /**
     * value: "MH"
     * @const
     */
    "MH": "MH",

    /**
     * value: "MK"
     * @const
     */
    "MK": "MK",

    /**
     * value: "MU"
     * @const
     */
    "MU": "MU",

    /**
     * value: "MT"
     * @const
     */
    "MT": "MT",

    /**
     * value: "MW"
     * @const
     */
    "MW": "MW",

    /**
     * value: "MV"
     * @const
     */
    "MV": "MV",

    /**
     * value: "MQ"
     * @const
     */
    "MQ": "MQ",

    /**
     * value: "MP"
     * @const
     */
    "MP": "MP",

    /**
     * value: "MS"
     * @const
     */
    "MS": "MS",

    /**
     * value: "MR"
     * @const
     */
    "MR": "MR",

    /**
     * value: "AU"
     * @const
     */
    "AU": "AU",

    /**
     * value: "UG"
     * @const
     */
    "UG": "UG",

    /**
     * value: "MY"
     * @const
     */
    "MY": "MY",

    /**
     * value: "MX"
     * @const
     */
    "MX": "MX",

    /**
     * value: "MZ"
     * @const
     */
    "MZ": "MZ",

    /**
     * value: "FR"
     * @const
     */
    "FR": "FR",

    /**
     * value: "AW"
     * @const
     */
    "AW": "AW",

    /**
     * value: "AF"
     * @const
     */
    "AF": "AF",

    /**
     * value: "AX"
     * @const
     */
    "AX": "AX",

    /**
     * value: "FI"
     * @const
     */
    "FI": "FI",

    /**
     * value: "FJ"
     * @const
     */
    "FJ": "FJ",

    /**
     * value: "FK"
     * @const
     */
    "FK": "FK",

    /**
     * value: "FM"
     * @const
     */
    "FM": "FM",

    /**
     * value: "FO"
     * @const
     */
    "FO": "FO",

    /**
     * value: "NI"
     * @const
     */
    "NI": "NI",

    /**
     * value: "NL"
     * @const
     */
    "NL": "NL",

    /**
     * value: "false"
     * @const
     */
    "false": "false",

    /**
     * value: "NA"
     * @const
     */
    "NA": "NA",

    /**
     * value: "VU"
     * @const
     */
    "VU": "VU",

    /**
     * value: "NC"
     * @const
     */
    "NC": "NC",

    /**
     * value: "NE"
     * @const
     */
    "NE": "NE",

    /**
     * value: "NF"
     * @const
     */
    "NF": "NF",

    /**
     * value: "NG"
     * @const
     */
    "NG": "NG",

    /**
     * value: "NZ"
     * @const
     */
    "NZ": "NZ",

    /**
     * value: "NP"
     * @const
     */
    "NP": "NP",

    /**
     * value: "NR"
     * @const
     */
    "NR": "NR",

    /**
     * value: "NU"
     * @const
     */
    "NU": "NU",

    /**
     * value: "CK"
     * @const
     */
    "CK": "CK",

    /**
     * value: "CI"
     * @const
     */
    "CI": "CI",

    /**
     * value: "CH"
     * @const
     */
    "CH": "CH",

    /**
     * value: "CO"
     * @const
     */
    "CO": "CO",

    /**
     * value: "CN"
     * @const
     */
    "CN": "CN",

    /**
     * value: "CM"
     * @const
     */
    "CM": "CM",

    /**
     * value: "CL"
     * @const
     */
    "CL": "CL",

    /**
     * value: "CC"
     * @const
     */
    "CC": "CC",

    /**
     * value: "CA"
     * @const
     */
    "CA": "CA",

    /**
     * value: "CG"
     * @const
     */
    "CG": "CG",

    /**
     * value: "CF"
     * @const
     */
    "CF": "CF",

    /**
     * value: "CD"
     * @const
     */
    "CD": "CD",

    /**
     * value: "CZ"
     * @const
     */
    "CZ": "CZ",

    /**
     * value: "CY"
     * @const
     */
    "CY": "CY",

    /**
     * value: "CX"
     * @const
     */
    "CX": "CX",

    /**
     * value: "CR"
     * @const
     */
    "CR": "CR",

    /**
     * value: "KP"
     * @const
     */
    "KP": "KP",

    /**
     * value: "CW"
     * @const
     */
    "CW": "CW",

    /**
     * value: "CV"
     * @const
     */
    "CV": "CV",

    /**
     * value: "CU"
     * @const
     */
    "CU": "CU",

    /**
     * value: "SZ"
     * @const
     */
    "SZ": "SZ",

    /**
     * value: "SY"
     * @const
     */
    "SY": "SY",

    /**
     * value: "SX"
     * @const
     */
    "SX": "SX",

    /**
     * value: "KG"
     * @const
     */
    "KG": "KG",

    /**
     * value: "KE"
     * @const
     */
    "KE": "KE",

    /**
     * value: "SS"
     * @const
     */
    "SS": "SS",

    /**
     * value: "SR"
     * @const
     */
    "SR": "SR",

    /**
     * value: "KI"
     * @const
     */
    "KI": "KI",

    /**
     * value: "KH"
     * @const
     */
    "KH": "KH",

    /**
     * value: "SV"
     * @const
     */
    "SV": "SV",

    /**
     * value: "KM"
     * @const
     */
    "KM": "KM",

    /**
     * value: "ST"
     * @const
     */
    "ST": "ST",

    /**
     * value: "SK"
     * @const
     */
    "SK": "SK",

    /**
     * value: "SJ"
     * @const
     */
    "SJ": "SJ",

    /**
     * value: "SI"
     * @const
     */
    "SI": "SI",

    /**
     * value: "SH"
     * @const
     */
    "SH": "SH",

    /**
     * value: "SO"
     * @const
     */
    "SO": "SO",

    /**
     * value: "SN"
     * @const
     */
    "SN": "SN",

    /**
     * value: "SM"
     * @const
     */
    "SM": "SM",

    /**
     * value: "SL"
     * @const
     */
    "SL": "SL",

    /**
     * value: "SC"
     * @const
     */
    "SC": "SC",

    /**
     * value: "SB"
     * @const
     */
    "SB": "SB",

    /**
     * value: "SA"
     * @const
     */
    "SA": "SA",

    /**
     * value: "SG"
     * @const
     */
    "SG": "SG",

    /**
     * value: "SE"
     * @const
     */
    "SE": "SE",

    /**
     * value: "SD"
     * @const
     */
    "SD": "SD",

    /**
     * value: "DO"
     * @const
     */
    "DO": "DO",

    /**
     * value: "DM"
     * @const
     */
    "DM": "DM",

    /**
     * value: "DJ"
     * @const
     */
    "DJ": "DJ",

    /**
     * value: "DK"
     * @const
     */
    "DK": "DK",

    /**
     * value: "DE"
     * @const
     */
    "DE": "DE",

    /**
     * value: "YE"
     * @const
     */
    "YE": "YE",

    /**
     * value: "AT"
     * @const
     */
    "AT": "AT",

    /**
     * value: "DZ"
     * @const
     */
    "DZ": "DZ",

    /**
     * value: "US"
     * @const
     */
    "US": "US",

    /**
     * value: "UY"
     * @const
     */
    "UY": "UY",

    /**
     * value: "YT"
     * @const
     */
    "YT": "YT",

    /**
     * value: "UM"
     * @const
     */
    "UM": "UM",

    /**
     * value: "LB"
     * @const
     */
    "LB": "LB",

    /**
     * value: "LC"
     * @const
     */
    "LC": "LC",

    /**
     * value: "LA"
     * @const
     */
    "LA": "LA",

    /**
     * value: "TV"
     * @const
     */
    "TV": "TV",

    /**
     * value: "TW"
     * @const
     */
    "TW": "TW",

    /**
     * value: "TT"
     * @const
     */
    "TT": "TT",

    /**
     * value: "TR"
     * @const
     */
    "TR": "TR",

    /**
     * value: "LK"
     * @const
     */
    "LK": "LK",

    /**
     * value: "LI"
     * @const
     */
    "LI": "LI",

    /**
     * value: "LV"
     * @const
     */
    "LV": "LV",

    /**
     * value: "TO"
     * @const
     */
    "TO": "TO",

    /**
     * value: "LT"
     * @const
     */
    "LT": "LT",

    /**
     * value: "LU"
     * @const
     */
    "LU": "LU",

    /**
     * value: "LR"
     * @const
     */
    "LR": "LR",

    /**
     * value: "LS"
     * @const
     */
    "LS": "LS",

    /**
     * value: "TH"
     * @const
     */
    "TH": "TH",

    /**
     * value: "TF"
     * @const
     */
    "TF": "TF",

    /**
     * value: "TG"
     * @const
     */
    "TG": "TG",

    /**
     * value: "TD"
     * @const
     */
    "TD": "TD",

    /**
     * value: "TC"
     * @const
     */
    "TC": "TC",

    /**
     * value: "LY"
     * @const
     */
    "LY": "LY",

    /**
     * value: "VA"
     * @const
     */
    "VA": "VA",

    /**
     * value: "VC"
     * @const
     */
    "VC": "VC",

    /**
     * value: "AE"
     * @const
     */
    "AE": "AE",

    /**
     * value: "VE"
     * @const
     */
    "VE": "VE",

    /**
     * value: "AG"
     * @const
     */
    "AG": "AG",

    /**
     * value: "VG"
     * @const
     */
    "VG": "VG",

    /**
     * value: "IQ"
     * @const
     */
    "IQ": "IQ",

    /**
     * value: "VI"
     * @const
     */
    "VI": "VI",

    /**
     * value: "IS"
     * @const
     */
    "IS": "IS",

    /**
     * value: "IR"
     * @const
     */
    "IR": "IR",

    /**
     * value: "AM"
     * @const
     */
    "AM": "AM",

    /**
     * value: "IT"
     * @const
     */
    "IT": "IT",

    /**
     * value: "VN"
     * @const
     */
    "VN": "VN",

    /**
     * value: "AQ"
     * @const
     */
    "AQ": "AQ",

    /**
     * value: "AS"
     * @const
     */
    "AS": "AS",

    /**
     * value: "AR"
     * @const
     */
    "AR": "AR",

    /**
     * value: "IM"
     * @const
     */
    "IM": "IM",

    /**
     * value: "IL"
     * @const
     */
    "IL": "IL",

    /**
     * value: "IO"
     * @const
     */
    "IO": "IO",

    /**
     * value: "IN"
     * @const
     */
    "IN": "IN",

    /**
     * value: "TZ"
     * @const
     */
    "TZ": "TZ",

    /**
     * value: "AZ"
     * @const
     */
    "AZ": "AZ",

    /**
     * value: "IE"
     * @const
     */
    "IE": "IE",

    /**
     * value: "ID"
     * @const
     */
    "ID": "ID",

    /**
     * value: "UA"
     * @const
     */
    "UA": "UA",

    /**
     * value: "QA"
     * @const
     */
    "QA": "QA"
};


/**
 * Allowed values for the <code>job_title</code> property.
 * @enum {String}
 * @readonly
 */
Doctor['JobTitleEnum'] = {

    /**
     * value: ""
     * @const
     */
    "empty": "",

    /**
     * value: "Provider/Staff (Private Practice)"
     * @const
     */
    "Provider/Staff (Private Practice)": "Provider/Staff (Private Practice)",

    /**
     * value: "Provider/Staff (Hospital)"
     * @const
     */
    "Provider/Staff (Hospital)": "Provider/Staff (Hospital)",

    /**
     * value: "Patients/Interview Candidate"
     * @const
     */
    "Patients/Interview Candidate": "Patients/Interview Candidate",

    /**
     * value: "Educator/Student"
     * @const
     */
    "Educator/Student": "Educator/Student",

    /**
     * value: "API/Developer"
     * @const
     */
    "API/Developer": "API/Developer",

    /**
     * value: "Consultant"
     * @const
     */
    "Consultant": "Consultant",

    /**
     * value: "Other"
     * @const
     */
    "Other": "Other"
};



export default Doctor;

