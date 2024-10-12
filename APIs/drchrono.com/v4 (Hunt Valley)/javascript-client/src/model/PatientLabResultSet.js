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
 * The PatientLabResultSet model module.
 * @module model/PatientLabResultSet
 * @version v4 (Hunt Valley)
 */
class PatientLabResultSet {
    /**
     * Constructs a new <code>PatientLabResultSet</code>.
     * @alias module:model/PatientLabResultSet
     * @param orderingDoctor {Number} 
     * @param patient {Number} 
     */
    constructor(orderingDoctor, patient) { 
        
        PatientLabResultSet.initialize(this, orderingDoctor, patient);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, orderingDoctor, patient) { 
        obj['ordering_doctor'] = orderingDoctor;
        obj['patient'] = patient;
    }

    /**
     * Constructs a <code>PatientLabResultSet</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PatientLabResultSet} obj Optional instance to populate.
     * @return {module:model/PatientLabResultSet} The populated <code>PatientLabResultSet</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PatientLabResultSet();

            if (data.hasOwnProperty('created_at')) {
                obj['created_at'] = ApiClient.convertToType(data['created_at'], 'String');
            }
            if (data.hasOwnProperty('date_test_performed')) {
                obj['date_test_performed'] = ApiClient.convertToType(data['date_test_performed'], 'String');
            }
            if (data.hasOwnProperty('doctor_comments')) {
                obj['doctor_comments'] = ApiClient.convertToType(data['doctor_comments'], 'String');
            }
            if (data.hasOwnProperty('doctor_signoff')) {
                obj['doctor_signoff'] = ApiClient.convertToType(data['doctor_signoff'], 'Boolean');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('lab_abnormal_flag')) {
                obj['lab_abnormal_flag'] = ApiClient.convertToType(data['lab_abnormal_flag'], 'String');
            }
            if (data.hasOwnProperty('lab_imported_from_ccr')) {
                obj['lab_imported_from_ccr'] = ApiClient.convertToType(data['lab_imported_from_ccr'], 'String');
            }
            if (data.hasOwnProperty('lab_normal_range')) {
                obj['lab_normal_range'] = ApiClient.convertToType(data['lab_normal_range'], 'String');
            }
            if (data.hasOwnProperty('lab_normal_range_units')) {
                obj['lab_normal_range_units'] = ApiClient.convertToType(data['lab_normal_range_units'], 'String');
            }
            if (data.hasOwnProperty('lab_order_status')) {
                obj['lab_order_status'] = ApiClient.convertToType(data['lab_order_status'], 'String');
            }
            if (data.hasOwnProperty('lab_result_value')) {
                obj['lab_result_value'] = ApiClient.convertToType(data['lab_result_value'], 'String');
            }
            if (data.hasOwnProperty('lab_result_value_as_float')) {
                obj['lab_result_value_as_float'] = ApiClient.convertToType(data['lab_result_value_as_float'], 'Number');
            }
            if (data.hasOwnProperty('lab_result_value_units')) {
                obj['lab_result_value_units'] = ApiClient.convertToType(data['lab_result_value_units'], 'String');
            }
            if (data.hasOwnProperty('loinc_code')) {
                obj['loinc_code'] = ApiClient.convertToType(data['loinc_code'], 'String');
            }
            if (data.hasOwnProperty('ordering_doctor')) {
                obj['ordering_doctor'] = ApiClient.convertToType(data['ordering_doctor'], 'Number');
            }
            if (data.hasOwnProperty('patient')) {
                obj['patient'] = ApiClient.convertToType(data['patient'], 'Number');
            }
            if (data.hasOwnProperty('scanned_in_result')) {
                obj['scanned_in_result'] = ApiClient.convertToType(data['scanned_in_result'], 'String');
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
            if (data.hasOwnProperty('updated_at')) {
                obj['updated_at'] = ApiClient.convertToType(data['updated_at'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PatientLabResultSet</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PatientLabResultSet</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PatientLabResultSet.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['created_at'] && !(typeof data['created_at'] === 'string' || data['created_at'] instanceof String)) {
            throw new Error("Expected the field `created_at` to be a primitive type in the JSON string but got " + data['created_at']);
        }
        // ensure the json data is a string
        if (data['date_test_performed'] && !(typeof data['date_test_performed'] === 'string' || data['date_test_performed'] instanceof String)) {
            throw new Error("Expected the field `date_test_performed` to be a primitive type in the JSON string but got " + data['date_test_performed']);
        }
        // ensure the json data is a string
        if (data['doctor_comments'] && !(typeof data['doctor_comments'] === 'string' || data['doctor_comments'] instanceof String)) {
            throw new Error("Expected the field `doctor_comments` to be a primitive type in the JSON string but got " + data['doctor_comments']);
        }
        // ensure the json data is a string
        if (data['lab_abnormal_flag'] && !(typeof data['lab_abnormal_flag'] === 'string' || data['lab_abnormal_flag'] instanceof String)) {
            throw new Error("Expected the field `lab_abnormal_flag` to be a primitive type in the JSON string but got " + data['lab_abnormal_flag']);
        }
        // ensure the json data is a string
        if (data['lab_imported_from_ccr'] && !(typeof data['lab_imported_from_ccr'] === 'string' || data['lab_imported_from_ccr'] instanceof String)) {
            throw new Error("Expected the field `lab_imported_from_ccr` to be a primitive type in the JSON string but got " + data['lab_imported_from_ccr']);
        }
        // ensure the json data is a string
        if (data['lab_normal_range'] && !(typeof data['lab_normal_range'] === 'string' || data['lab_normal_range'] instanceof String)) {
            throw new Error("Expected the field `lab_normal_range` to be a primitive type in the JSON string but got " + data['lab_normal_range']);
        }
        // ensure the json data is a string
        if (data['lab_normal_range_units'] && !(typeof data['lab_normal_range_units'] === 'string' || data['lab_normal_range_units'] instanceof String)) {
            throw new Error("Expected the field `lab_normal_range_units` to be a primitive type in the JSON string but got " + data['lab_normal_range_units']);
        }
        // ensure the json data is a string
        if (data['lab_order_status'] && !(typeof data['lab_order_status'] === 'string' || data['lab_order_status'] instanceof String)) {
            throw new Error("Expected the field `lab_order_status` to be a primitive type in the JSON string but got " + data['lab_order_status']);
        }
        // ensure the json data is a string
        if (data['lab_result_value'] && !(typeof data['lab_result_value'] === 'string' || data['lab_result_value'] instanceof String)) {
            throw new Error("Expected the field `lab_result_value` to be a primitive type in the JSON string but got " + data['lab_result_value']);
        }
        // ensure the json data is a string
        if (data['lab_result_value_units'] && !(typeof data['lab_result_value_units'] === 'string' || data['lab_result_value_units'] instanceof String)) {
            throw new Error("Expected the field `lab_result_value_units` to be a primitive type in the JSON string but got " + data['lab_result_value_units']);
        }
        // ensure the json data is a string
        if (data['loinc_code'] && !(typeof data['loinc_code'] === 'string' || data['loinc_code'] instanceof String)) {
            throw new Error("Expected the field `loinc_code` to be a primitive type in the JSON string but got " + data['loinc_code']);
        }
        // ensure the json data is a string
        if (data['scanned_in_result'] && !(typeof data['scanned_in_result'] === 'string' || data['scanned_in_result'] instanceof String)) {
            throw new Error("Expected the field `scanned_in_result` to be a primitive type in the JSON string but got " + data['scanned_in_result']);
        }
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }
        // ensure the json data is a string
        if (data['updated_at'] && !(typeof data['updated_at'] === 'string' || data['updated_at'] instanceof String)) {
            throw new Error("Expected the field `updated_at` to be a primitive type in the JSON string but got " + data['updated_at']);
        }

        return true;
    }


}

PatientLabResultSet.RequiredProperties = ["ordering_doctor", "patient"];

/**
 * 
 * @member {String} created_at
 */
PatientLabResultSet.prototype['created_at'] = undefined;

/**
 * Date of lab test.
 * @member {String} date_test_performed
 */
PatientLabResultSet.prototype['date_test_performed'] = undefined;

/**
 * Comment from the doctor on lab result.
 * @member {String} doctor_comments
 */
PatientLabResultSet.prototype['doctor_comments'] = undefined;

/**
 * Check this box when the doctor has reviewed the lab result and taken appropriate action.
 * @member {Boolean} doctor_signoff
 */
PatientLabResultSet.prototype['doctor_signoff'] = undefined;

/**
 * 
 * @member {Number} id
 */
PatientLabResultSet.prototype['id'] = undefined;

/**
 * HL7 codified abnormal flag for the result.
 * @member {module:model/PatientLabResultSet.LabAbnormalFlagEnum} lab_abnormal_flag
 */
PatientLabResultSet.prototype['lab_abnormal_flag'] = undefined;

/**
 * Imported CCR document that contains lab results.
 * @member {String} lab_imported_from_ccr
 */
PatientLabResultSet.prototype['lab_imported_from_ccr'] = undefined;

/**
 * 
 * @member {String} lab_normal_range
 */
PatientLabResultSet.prototype['lab_normal_range'] = undefined;

/**
 * 
 * @member {String} lab_normal_range_units
 */
PatientLabResultSet.prototype['lab_normal_range_units'] = undefined;

/**
 * Status of the lab order.
 * @member {module:model/PatientLabResultSet.LabOrderStatusEnum} lab_order_status
 */
PatientLabResultSet.prototype['lab_order_status'] = undefined;

/**
 * 
 * @member {String} lab_result_value
 */
PatientLabResultSet.prototype['lab_result_value'] = undefined;

/**
 * 
 * @member {Number} lab_result_value_as_float
 */
PatientLabResultSet.prototype['lab_result_value_as_float'] = undefined;

/**
 * 
 * @member {String} lab_result_value_units
 */
PatientLabResultSet.prototype['lab_result_value_units'] = undefined;

/**
 * 
 * @member {String} loinc_code
 */
PatientLabResultSet.prototype['loinc_code'] = undefined;

/**
 * 
 * @member {Number} ordering_doctor
 */
PatientLabResultSet.prototype['ordering_doctor'] = undefined;

/**
 * 
 * @member {Number} patient
 */
PatientLabResultSet.prototype['patient'] = undefined;

/**
 * Scanned in PDF for this lab result (optional).
 * @member {String} scanned_in_result
 */
PatientLabResultSet.prototype['scanned_in_result'] = undefined;

/**
 * 
 * @member {String} title
 */
PatientLabResultSet.prototype['title'] = undefined;

/**
 * 
 * @member {String} updated_at
 */
PatientLabResultSet.prototype['updated_at'] = undefined;





/**
 * Allowed values for the <code>lab_abnormal_flag</code> property.
 * @enum {String}
 * @readonly
 */
PatientLabResultSet['LabAbnormalFlagEnum'] = {

    /**
     * value: ""
     * @const
     */
    "empty": "",

    /**
     * value: "L"
     * @const
     */
    "L": "L",

    /**
     * value: "H"
     * @const
     */
    "H": "H",

    /**
     * value: "LL"
     * @const
     */
    "LL": "LL",

    /**
     * value: "HH"
     * @const
     */
    "HH": "HH",

    /**
     * value: "<"
     * @const
     */
    "LESS_THAN": "<",

    /**
     * value: ">"
     * @const
     */
    "GREATER_THAN": ">",

    /**
     * value: "N"
     * @const
     */
    "N": "N",

    /**
     * value: "A"
     * @const
     */
    "A": "A",

    /**
     * value: "AA"
     * @const
     */
    "AA": "AA",

    /**
     * value: "null"
     * @const
     */
    "null": "null",

    /**
     * value: "U"
     * @const
     */
    "U": "U",

    /**
     * value: "D"
     * @const
     */
    "D": "D",

    /**
     * value: "B"
     * @const
     */
    "B": "B",

    /**
     * value: "W"
     * @const
     */
    "W": "W",

    /**
     * value: "S"
     * @const
     */
    "S": "S",

    /**
     * value: "R"
     * @const
     */
    "R": "R",

    /**
     * value: "I"
     * @const
     */
    "I": "I",

    /**
     * value: "MS"
     * @const
     */
    "MS": "MS",

    /**
     * value: "VS"
     * @const
     */
    "VS": "VS"
};


/**
 * Allowed values for the <code>lab_order_status</code> property.
 * @enum {String}
 * @readonly
 */
PatientLabResultSet['LabOrderStatusEnum'] = {

    /**
     * value: ""
     * @const
     */
    "empty": "",

    /**
     * value: "Order Entered"
     * @const
     */
    "Order Entered": "Order Entered",

    /**
     * value: "Discontinued"
     * @const
     */
    "Discontinued": "Discontinued",

    /**
     * value: "In Progress"
     * @const
     */
    "In Progress": "In Progress",

    /**
     * value: "Results Received"
     * @const
     */
    "Results Received": "Results Received",

    /**
     * value: "Results Reviewed with Patient"
     * @const
     */
    "Results Reviewed with Patient": "Results Reviewed with Patient",

    /**
     * value: "Paper Order"
     * @const
     */
    "Paper Order": "Paper Order"
};



export default PatientLabResultSet;

