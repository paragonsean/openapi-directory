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
 * The PatientDrug model module.
 * @module model/PatientDrug
 * @version v4 (Hunt Valley)
 */
class PatientDrug {
    /**
     * Constructs a new <code>PatientDrug</code>.
     * @alias module:model/PatientDrug
     * @param doctor {Number} Prescribing doctor ID
     * @param patient {Number} 
     */
    constructor(doctor, patient) { 
        
        PatientDrug.initialize(this, doctor, patient);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, doctor, patient) { 
        obj['doctor'] = doctor;
        obj['patient'] = patient;
    }

    /**
     * Constructs a <code>PatientDrug</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PatientDrug} obj Optional instance to populate.
     * @return {module:model/PatientDrug} The populated <code>PatientDrug</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PatientDrug();

            if (data.hasOwnProperty('appointment')) {
                obj['appointment'] = ApiClient.convertToType(data['appointment'], 'Number');
            }
            if (data.hasOwnProperty('date_prescribed')) {
                obj['date_prescribed'] = ApiClient.convertToType(data['date_prescribed'], 'String');
            }
            if (data.hasOwnProperty('date_started_taking')) {
                obj['date_started_taking'] = ApiClient.convertToType(data['date_started_taking'], 'String');
            }
            if (data.hasOwnProperty('date_stopped_taking')) {
                obj['date_stopped_taking'] = ApiClient.convertToType(data['date_stopped_taking'], 'String');
            }
            if (data.hasOwnProperty('daw')) {
                obj['daw'] = ApiClient.convertToType(data['daw'], 'Boolean');
            }
            if (data.hasOwnProperty('dispense_quantity')) {
                obj['dispense_quantity'] = ApiClient.convertToType(data['dispense_quantity'], 'Number');
            }
            if (data.hasOwnProperty('doctor')) {
                obj['doctor'] = ApiClient.convertToType(data['doctor'], 'Number');
            }
            if (data.hasOwnProperty('dosage_quantity')) {
                obj['dosage_quantity'] = ApiClient.convertToType(data['dosage_quantity'], 'String');
            }
            if (data.hasOwnProperty('dosage_units')) {
                obj['dosage_units'] = ApiClient.convertToType(data['dosage_units'], 'String');
            }
            if (data.hasOwnProperty('frequency')) {
                obj['frequency'] = ApiClient.convertToType(data['frequency'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('indication')) {
                obj['indication'] = ApiClient.convertToType(data['indication'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('ndc')) {
                obj['ndc'] = ApiClient.convertToType(data['ndc'], 'String');
            }
            if (data.hasOwnProperty('notes')) {
                obj['notes'] = ApiClient.convertToType(data['notes'], 'String');
            }
            if (data.hasOwnProperty('number_refills')) {
                obj['number_refills'] = ApiClient.convertToType(data['number_refills'], 'Number');
            }
            if (data.hasOwnProperty('order_status')) {
                obj['order_status'] = ApiClient.convertToType(data['order_status'], 'String');
            }
            if (data.hasOwnProperty('patient')) {
                obj['patient'] = ApiClient.convertToType(data['patient'], 'Number');
            }
            if (data.hasOwnProperty('pharmacy_note')) {
                obj['pharmacy_note'] = ApiClient.convertToType(data['pharmacy_note'], 'String');
            }
            if (data.hasOwnProperty('prn')) {
                obj['prn'] = ApiClient.convertToType(data['prn'], 'Boolean');
            }
            if (data.hasOwnProperty('route')) {
                obj['route'] = ApiClient.convertToType(data['route'], 'String');
            }
            if (data.hasOwnProperty('rxnorm')) {
                obj['rxnorm'] = ApiClient.convertToType(data['rxnorm'], 'String');
            }
            if (data.hasOwnProperty('signature_note')) {
                obj['signature_note'] = ApiClient.convertToType(data['signature_note'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PatientDrug</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PatientDrug</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PatientDrug.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['date_prescribed'] && !(typeof data['date_prescribed'] === 'string' || data['date_prescribed'] instanceof String)) {
            throw new Error("Expected the field `date_prescribed` to be a primitive type in the JSON string but got " + data['date_prescribed']);
        }
        // ensure the json data is a string
        if (data['date_started_taking'] && !(typeof data['date_started_taking'] === 'string' || data['date_started_taking'] instanceof String)) {
            throw new Error("Expected the field `date_started_taking` to be a primitive type in the JSON string but got " + data['date_started_taking']);
        }
        // ensure the json data is a string
        if (data['date_stopped_taking'] && !(typeof data['date_stopped_taking'] === 'string' || data['date_stopped_taking'] instanceof String)) {
            throw new Error("Expected the field `date_stopped_taking` to be a primitive type in the JSON string but got " + data['date_stopped_taking']);
        }
        // ensure the json data is a string
        if (data['dosage_quantity'] && !(typeof data['dosage_quantity'] === 'string' || data['dosage_quantity'] instanceof String)) {
            throw new Error("Expected the field `dosage_quantity` to be a primitive type in the JSON string but got " + data['dosage_quantity']);
        }
        // ensure the json data is a string
        if (data['dosage_units'] && !(typeof data['dosage_units'] === 'string' || data['dosage_units'] instanceof String)) {
            throw new Error("Expected the field `dosage_units` to be a primitive type in the JSON string but got " + data['dosage_units']);
        }
        // ensure the json data is a string
        if (data['frequency'] && !(typeof data['frequency'] === 'string' || data['frequency'] instanceof String)) {
            throw new Error("Expected the field `frequency` to be a primitive type in the JSON string but got " + data['frequency']);
        }
        // ensure the json data is a string
        if (data['indication'] && !(typeof data['indication'] === 'string' || data['indication'] instanceof String)) {
            throw new Error("Expected the field `indication` to be a primitive type in the JSON string but got " + data['indication']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['ndc'] && !(typeof data['ndc'] === 'string' || data['ndc'] instanceof String)) {
            throw new Error("Expected the field `ndc` to be a primitive type in the JSON string but got " + data['ndc']);
        }
        // ensure the json data is a string
        if (data['notes'] && !(typeof data['notes'] === 'string' || data['notes'] instanceof String)) {
            throw new Error("Expected the field `notes` to be a primitive type in the JSON string but got " + data['notes']);
        }
        // ensure the json data is a string
        if (data['order_status'] && !(typeof data['order_status'] === 'string' || data['order_status'] instanceof String)) {
            throw new Error("Expected the field `order_status` to be a primitive type in the JSON string but got " + data['order_status']);
        }
        // ensure the json data is a string
        if (data['pharmacy_note'] && !(typeof data['pharmacy_note'] === 'string' || data['pharmacy_note'] instanceof String)) {
            throw new Error("Expected the field `pharmacy_note` to be a primitive type in the JSON string but got " + data['pharmacy_note']);
        }
        // ensure the json data is a string
        if (data['route'] && !(typeof data['route'] === 'string' || data['route'] instanceof String)) {
            throw new Error("Expected the field `route` to be a primitive type in the JSON string but got " + data['route']);
        }
        // ensure the json data is a string
        if (data['rxnorm'] && !(typeof data['rxnorm'] === 'string' || data['rxnorm'] instanceof String)) {
            throw new Error("Expected the field `rxnorm` to be a primitive type in the JSON string but got " + data['rxnorm']);
        }
        // ensure the json data is a string
        if (data['signature_note'] && !(typeof data['signature_note'] === 'string' || data['signature_note'] instanceof String)) {
            throw new Error("Expected the field `signature_note` to be a primitive type in the JSON string but got " + data['signature_note']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }

        return true;
    }


}

PatientDrug.RequiredProperties = ["doctor", "patient"];

/**
 * Appointment ID corresponding to the initial prescription
 * @member {Number} appointment
 */
PatientDrug.prototype['appointment'] = undefined;

/**
 * 
 * @member {String} date_prescribed
 */
PatientDrug.prototype['date_prescribed'] = undefined;

/**
 * 
 * @member {String} date_started_taking
 */
PatientDrug.prototype['date_started_taking'] = undefined;

/**
 * 
 * @member {String} date_stopped_taking
 */
PatientDrug.prototype['date_stopped_taking'] = undefined;

/**
 * If true, the prescription should be dispensed as written and not substituted
 * @member {Boolean} daw
 */
PatientDrug.prototype['daw'] = undefined;

/**
 * 
 * @member {Number} dispense_quantity
 */
PatientDrug.prototype['dispense_quantity'] = undefined;

/**
 * Prescribing doctor ID
 * @member {Number} doctor
 */
PatientDrug.prototype['doctor'] = undefined;

/**
 * Please note, this used to be an decimal field, you can still pass decimal value to it. Or you can pass in some formatted string if needed.
 * @member {String} dosage_quantity
 */
PatientDrug.prototype['dosage_quantity'] = undefined;

/**
 * 
 * @member {String} dosage_units
 */
PatientDrug.prototype['dosage_units'] = undefined;

/**
 * Frequency pf administration
 * @member {String} frequency
 */
PatientDrug.prototype['frequency'] = undefined;

/**
 * 
 * @member {Number} id
 */
PatientDrug.prototype['id'] = undefined;

/**
 * 
 * @member {String} indication
 */
PatientDrug.prototype['indication'] = undefined;

/**
 * 
 * @member {String} name
 */
PatientDrug.prototype['name'] = undefined;

/**
 * 
 * @member {String} ndc
 */
PatientDrug.prototype['ndc'] = undefined;

/**
 * Any additional notes from the provider
 * @member {String} notes
 */
PatientDrug.prototype['notes'] = undefined;

/**
 * 
 * @member {Number} number_refills
 */
PatientDrug.prototype['number_refills'] = undefined;

/**
 * One of `\"\"`, `\"Ordered\"`, `\"Administered during visit\"`, `\"Electronic eRx Sent\"`, `\"Phoned into Pharmacy\"`, `\"Faxed to Pharmacy\"`, `\"Paper Rx\"`, `\"Prescription Printed\"`, `\"Discontinued\"`, `\"Prescribed by other Dr\"` or `\"Over the Counter\"`. If omitted in writing, default to `\"\"`
 * @member {module:model/PatientDrug.OrderStatusEnum} order_status
 */
PatientDrug.prototype['order_status'] = undefined;

/**
 * 
 * @member {Number} patient
 */
PatientDrug.prototype['patient'] = undefined;

/**
 * 
 * @member {String} pharmacy_note
 */
PatientDrug.prototype['pharmacy_note'] = undefined;

/**
 * If `True`, the medication should be taken when necessary
 * @member {Boolean} prn
 */
PatientDrug.prototype['prn'] = undefined;

/**
 * Route of administration
 * @member {String} route
 */
PatientDrug.prototype['route'] = undefined;

/**
 * RxNorm code for the medication
 * @member {String} rxnorm
 */
PatientDrug.prototype['rxnorm'] = undefined;

/**
 * 
 * @member {String} signature_note
 */
PatientDrug.prototype['signature_note'] = undefined;

/**
 * If present, one of `\"active\"` or `\"inactive\"`. If omitted in writing, default to `\"active\"`
 * @member {module:model/PatientDrug.StatusEnum} status
 */
PatientDrug.prototype['status'] = undefined;





/**
 * Allowed values for the <code>order_status</code> property.
 * @enum {String}
 * @readonly
 */
PatientDrug['OrderStatusEnum'] = {

    /**
     * value: ""
     * @const
     */
    "empty": "",

    /**
     * value: "Ordered"
     * @const
     */
    "Ordered": "Ordered",

    /**
     * value: "Administered during visit"
     * @const
     */
    "Administered during visit": "Administered during visit",

    /**
     * value: "Electronic eRx Sent"
     * @const
     */
    "Electronic eRx Sent": "Electronic eRx Sent",

    /**
     * value: "Phoned into Pharmacy"
     * @const
     */
    "Phoned into Pharmacy": "Phoned into Pharmacy",

    /**
     * value: "Faxed to Pharmacy"
     * @const
     */
    "Faxed to Pharmacy": "Faxed to Pharmacy",

    /**
     * value: "Paper Rx"
     * @const
     */
    "Paper Rx": "Paper Rx",

    /**
     * value: "Prescription Printed"
     * @const
     */
    "Prescription Printed": "Prescription Printed",

    /**
     * value: "Discontinued"
     * @const
     */
    "Discontinued": "Discontinued",

    /**
     * value: "Prescribed by other Dr"
     * @const
     */
    "Prescribed by other Dr": "Prescribed by other Dr",

    /**
     * value: "Over the Counter"
     * @const
     */
    "Over the Counter": "Over the Counter"
};


/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
PatientDrug['StatusEnum'] = {

    /**
     * value: "active"
     * @const
     */
    "active": "active",

    /**
     * value: "inactive"
     * @const
     */
    "inactive": "inactive"
};



export default PatientDrug;

