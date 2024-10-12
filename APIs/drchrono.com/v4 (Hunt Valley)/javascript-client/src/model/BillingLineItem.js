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
 * The BillingLineItem model module.
 * @module model/BillingLineItem
 * @version v4 (Hunt Valley)
 */
class BillingLineItem {
    /**
     * Constructs a new <code>BillingLineItem</code>.
     * @alias module:model/BillingLineItem
     * @param appointment {Number} Appointment ID
     * @param code {String} 
     * @param diagnosisPointers {Array.<String>} List of 4 diagnosis pointers
     * @param procedureType {module:model/BillingLineItem.ProcedureTypeEnum} One of `\"CPT(C)\"`, `\"HCPCS(H)\"`, `\"Custom(U)\"`, use 1 character identifier when using `POST`
     */
    constructor(appointment, code, diagnosisPointers, procedureType) { 
        
        BillingLineItem.initialize(this, appointment, code, diagnosisPointers, procedureType);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, appointment, code, diagnosisPointers, procedureType) { 
        obj['appointment'] = appointment;
        obj['code'] = code;
        obj['diagnosis_pointers'] = diagnosisPointers;
        obj['procedure_type'] = procedureType;
    }

    /**
     * Constructs a <code>BillingLineItem</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BillingLineItem} obj Optional instance to populate.
     * @return {module:model/BillingLineItem} The populated <code>BillingLineItem</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BillingLineItem();

            if (data.hasOwnProperty('adjustment')) {
                obj['adjustment'] = ApiClient.convertToType(data['adjustment'], 'Number');
            }
            if (data.hasOwnProperty('allowed')) {
                obj['allowed'] = ApiClient.convertToType(data['allowed'], 'Number');
            }
            if (data.hasOwnProperty('appointment')) {
                obj['appointment'] = ApiClient.convertToType(data['appointment'], 'Number');
            }
            if (data.hasOwnProperty('balance_ins')) {
                obj['balance_ins'] = ApiClient.convertToType(data['balance_ins'], 'Number');
            }
            if (data.hasOwnProperty('balance_pt')) {
                obj['balance_pt'] = ApiClient.convertToType(data['balance_pt'], 'Number');
            }
            if (data.hasOwnProperty('balance_total')) {
                obj['balance_total'] = ApiClient.convertToType(data['balance_total'], 'String');
            }
            if (data.hasOwnProperty('billed')) {
                obj['billed'] = ApiClient.convertToType(data['billed'], 'Number');
            }
            if (data.hasOwnProperty('billing_status')) {
                obj['billing_status'] = ApiClient.convertToType(data['billing_status'], 'String');
            }
            if (data.hasOwnProperty('code')) {
                obj['code'] = ApiClient.convertToType(data['code'], 'String');
            }
            if (data.hasOwnProperty('denied_flag')) {
                obj['denied_flag'] = ApiClient.convertToType(data['denied_flag'], 'Boolean');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('diagnosis_pointers')) {
                obj['diagnosis_pointers'] = ApiClient.convertToType(data['diagnosis_pointers'], ['String']);
            }
            if (data.hasOwnProperty('doctor')) {
                obj['doctor'] = ApiClient.convertToType(data['doctor'], 'String');
            }
            if (data.hasOwnProperty('expected_reimbursement')) {
                obj['expected_reimbursement'] = ApiClient.convertToType(data['expected_reimbursement'], 'Number');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('ins1_paid')) {
                obj['ins1_paid'] = ApiClient.convertToType(data['ins1_paid'], 'Number');
            }
            if (data.hasOwnProperty('ins2_paid')) {
                obj['ins2_paid'] = ApiClient.convertToType(data['ins2_paid'], 'Number');
            }
            if (data.hasOwnProperty('ins3_paid')) {
                obj['ins3_paid'] = ApiClient.convertToType(data['ins3_paid'], 'Number');
            }
            if (data.hasOwnProperty('ins_total')) {
                obj['ins_total'] = ApiClient.convertToType(data['ins_total'], 'String');
            }
            if (data.hasOwnProperty('insurance_status')) {
                obj['insurance_status'] = ApiClient.convertToType(data['insurance_status'], 'String');
            }
            if (data.hasOwnProperty('modifiers')) {
                obj['modifiers'] = ApiClient.convertToType(data['modifiers'], ['String']);
            }
            if (data.hasOwnProperty('paid_total')) {
                obj['paid_total'] = ApiClient.convertToType(data['paid_total'], 'String');
            }
            if (data.hasOwnProperty('patient')) {
                obj['patient'] = ApiClient.convertToType(data['patient'], 'String');
            }
            if (data.hasOwnProperty('posted_date')) {
                obj['posted_date'] = ApiClient.convertToType(data['posted_date'], 'String');
            }
            if (data.hasOwnProperty('price')) {
                obj['price'] = ApiClient.convertToType(data['price'], 'Number');
            }
            if (data.hasOwnProperty('procedure_type')) {
                obj['procedure_type'] = ApiClient.convertToType(data['procedure_type'], 'String');
            }
            if (data.hasOwnProperty('pt_paid')) {
                obj['pt_paid'] = ApiClient.convertToType(data['pt_paid'], 'Number');
            }
            if (data.hasOwnProperty('quantity')) {
                obj['quantity'] = ApiClient.convertToType(data['quantity'], 'Number');
            }
            if (data.hasOwnProperty('service_date')) {
                obj['service_date'] = ApiClient.convertToType(data['service_date'], 'String');
            }
            if (data.hasOwnProperty('units')) {
                obj['units'] = ApiClient.convertToType(data['units'], 'String');
            }
            if (data.hasOwnProperty('updated_at')) {
                obj['updated_at'] = ApiClient.convertToType(data['updated_at'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BillingLineItem</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BillingLineItem</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of BillingLineItem.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['balance_total'] && !(typeof data['balance_total'] === 'string' || data['balance_total'] instanceof String)) {
            throw new Error("Expected the field `balance_total` to be a primitive type in the JSON string but got " + data['balance_total']);
        }
        // ensure the json data is a string
        if (data['billing_status'] && !(typeof data['billing_status'] === 'string' || data['billing_status'] instanceof String)) {
            throw new Error("Expected the field `billing_status` to be a primitive type in the JSON string but got " + data['billing_status']);
        }
        // ensure the json data is a string
        if (data['code'] && !(typeof data['code'] === 'string' || data['code'] instanceof String)) {
            throw new Error("Expected the field `code` to be a primitive type in the JSON string but got " + data['code']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['diagnosis_pointers'])) {
            throw new Error("Expected the field `diagnosis_pointers` to be an array in the JSON data but got " + data['diagnosis_pointers']);
        }
        // ensure the json data is a string
        if (data['doctor'] && !(typeof data['doctor'] === 'string' || data['doctor'] instanceof String)) {
            throw new Error("Expected the field `doctor` to be a primitive type in the JSON string but got " + data['doctor']);
        }
        // ensure the json data is a string
        if (data['ins_total'] && !(typeof data['ins_total'] === 'string' || data['ins_total'] instanceof String)) {
            throw new Error("Expected the field `ins_total` to be a primitive type in the JSON string but got " + data['ins_total']);
        }
        // ensure the json data is a string
        if (data['insurance_status'] && !(typeof data['insurance_status'] === 'string' || data['insurance_status'] instanceof String)) {
            throw new Error("Expected the field `insurance_status` to be a primitive type in the JSON string but got " + data['insurance_status']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['modifiers'])) {
            throw new Error("Expected the field `modifiers` to be an array in the JSON data but got " + data['modifiers']);
        }
        // ensure the json data is a string
        if (data['paid_total'] && !(typeof data['paid_total'] === 'string' || data['paid_total'] instanceof String)) {
            throw new Error("Expected the field `paid_total` to be a primitive type in the JSON string but got " + data['paid_total']);
        }
        // ensure the json data is a string
        if (data['patient'] && !(typeof data['patient'] === 'string' || data['patient'] instanceof String)) {
            throw new Error("Expected the field `patient` to be a primitive type in the JSON string but got " + data['patient']);
        }
        // ensure the json data is a string
        if (data['posted_date'] && !(typeof data['posted_date'] === 'string' || data['posted_date'] instanceof String)) {
            throw new Error("Expected the field `posted_date` to be a primitive type in the JSON string but got " + data['posted_date']);
        }
        // ensure the json data is a string
        if (data['procedure_type'] && !(typeof data['procedure_type'] === 'string' || data['procedure_type'] instanceof String)) {
            throw new Error("Expected the field `procedure_type` to be a primitive type in the JSON string but got " + data['procedure_type']);
        }
        // ensure the json data is a string
        if (data['service_date'] && !(typeof data['service_date'] === 'string' || data['service_date'] instanceof String)) {
            throw new Error("Expected the field `service_date` to be a primitive type in the JSON string but got " + data['service_date']);
        }
        // ensure the json data is a string
        if (data['units'] && !(typeof data['units'] === 'string' || data['units'] instanceof String)) {
            throw new Error("Expected the field `units` to be a primitive type in the JSON string but got " + data['units']);
        }
        // ensure the json data is a string
        if (data['updated_at'] && !(typeof data['updated_at'] === 'string' || data['updated_at'] instanceof String)) {
            throw new Error("Expected the field `updated_at` to be a primitive type in the JSON string but got " + data['updated_at']);
        }

        return true;
    }


}

BillingLineItem.RequiredProperties = ["appointment", "code", "diagnosis_pointers", "procedure_type"];

/**
 * Adjustment from total billed
 * @member {Number} adjustment
 */
BillingLineItem.prototype['adjustment'] = undefined;

/**
 * Amount allowed by insurance
 * @member {Number} allowed
 */
BillingLineItem.prototype['allowed'] = undefined;

/**
 * Appointment ID
 * @member {Number} appointment
 */
BillingLineItem.prototype['appointment'] = undefined;

/**
 * Insurance balance
 * @member {Number} balance_ins
 */
BillingLineItem.prototype['balance_ins'] = undefined;

/**
 * Patient balance
 * @member {Number} balance_pt
 */
BillingLineItem.prototype['balance_pt'] = undefined;

/**
 * Total balance
 * @member {String} balance_total
 */
BillingLineItem.prototype['balance_total'] = undefined;

/**
 * Total billed
 * @member {Number} billed
 */
BillingLineItem.prototype['billed'] = undefined;

/**
 * One of `\"\"`, `\"Incomplete Information\"`, `\"In Process Emdeon\"`, `\"In Process iHCFA\"`, `\"In Process Gateway\"`, `\"Rejected Emdeon\"`, `\"Rejected iHCFA\"`, `\"Rejected Gateway\"`, `\"In Process Payer\"`, `\"Payer Acknowledged\"`, `\"Rejected Payer\"`, `\"Paid in Full\"`,  `\"Partially Paid\"`,  `\"Coordination of Benefits\"`,  `\"ERA Received\"`,  `\"ERA Denied\"`
 * @member {module:model/BillingLineItem.BillingStatusEnum} billing_status
 */
BillingLineItem.prototype['billing_status'] = undefined;

/**
 * 
 * @member {String} code
 */
BillingLineItem.prototype['code'] = undefined;

/**
 * 
 * @member {Boolean} denied_flag
 */
BillingLineItem.prototype['denied_flag'] = undefined;

/**
 * 
 * @member {String} description
 */
BillingLineItem.prototype['description'] = undefined;

/**
 * List of 4 diagnosis pointers
 * @member {Array.<String>} diagnosis_pointers
 */
BillingLineItem.prototype['diagnosis_pointers'] = undefined;

/**
 * Doctor ID
 * @member {String} doctor
 */
BillingLineItem.prototype['doctor'] = undefined;

/**
 * 
 * @member {Number} expected_reimbursement
 */
BillingLineItem.prototype['expected_reimbursement'] = undefined;

/**
 * 
 * @member {Number} id
 */
BillingLineItem.prototype['id'] = undefined;

/**
 * Amount paid by patient's primary insurer
 * @member {Number} ins1_paid
 */
BillingLineItem.prototype['ins1_paid'] = undefined;

/**
 * Amount paid by patient's secondary insurer
 * @member {Number} ins2_paid
 */
BillingLineItem.prototype['ins2_paid'] = undefined;

/**
 * Amount paid by patinet's tertiary insurer
 * @member {Number} ins3_paid
 */
BillingLineItem.prototype['ins3_paid'] = undefined;

/**
 * Total amount paid by patient's insurers
 * @member {String} ins_total
 */
BillingLineItem.prototype['ins_total'] = undefined;

/**
 * This corresponds to the \"Status/Adj Type\" from billing detail screen
 * @member {String} insurance_status
 */
BillingLineItem.prototype['insurance_status'] = undefined;

/**
 * List of 4 code modifiers
 * @member {Array.<String>} modifiers
 */
BillingLineItem.prototype['modifiers'] = undefined;

/**
 * Total amount paid
 * @member {String} paid_total
 */
BillingLineItem.prototype['paid_total'] = undefined;

/**
 * Patient ID
 * @member {String} patient
 */
BillingLineItem.prototype['patient'] = undefined;

/**
 * 
 * @member {String} posted_date
 */
BillingLineItem.prototype['posted_date'] = undefined;

/**
 * Price of procedure
 * @member {Number} price
 */
BillingLineItem.prototype['price'] = undefined;

/**
 * One of `\"CPT(C)\"`, `\"HCPCS(H)\"`, `\"Custom(U)\"`, use 1 character identifier when using `POST`
 * @member {module:model/BillingLineItem.ProcedureTypeEnum} procedure_type
 */
BillingLineItem.prototype['procedure_type'] = undefined;

/**
 * Amount paid by patient
 * @member {Number} pt_paid
 */
BillingLineItem.prototype['pt_paid'] = undefined;

/**
 * 
 * @member {Number} quantity
 */
BillingLineItem.prototype['quantity'] = undefined;

/**
 * Date on which the service was rendered
 * @member {String} service_date
 */
BillingLineItem.prototype['service_date'] = undefined;

/**
 * Default to \"UN\"
 * @member {String} units
 */
BillingLineItem.prototype['units'] = undefined;

/**
 * 
 * @member {String} updated_at
 */
BillingLineItem.prototype['updated_at'] = undefined;





/**
 * Allowed values for the <code>billing_status</code> property.
 * @enum {String}
 * @readonly
 */
BillingLineItem['BillingStatusEnum'] = {

    /**
     * value: ""
     * @const
     */
    "empty": "",

    /**
     * value: "Incomplete Information"
     * @const
     */
    "Incomplete Information": "Incomplete Information",

    /**
     * value: "In Process Emdeon"
     * @const
     */
    "In Process Emdeon": "In Process Emdeon",

    /**
     * value: "In Process iHCFA"
     * @const
     */
    "In Process iHCFA": "In Process iHCFA",

    /**
     * value: "In Process Gateway"
     * @const
     */
    "In Process Gateway": "In Process Gateway",

    /**
     * value: "In Process Jopari"
     * @const
     */
    "In Process Jopari": "In Process Jopari",

    /**
     * value: "In Process Waystar"
     * @const
     */
    "In Process Waystar": "In Process Waystar",

    /**
     * value: "Rejected Emdeon"
     * @const
     */
    "Rejected Emdeon": "Rejected Emdeon",

    /**
     * value: "Rejected iHCFA"
     * @const
     */
    "Rejected iHCFA": "Rejected iHCFA",

    /**
     * value: "Rejected Gateway"
     * @const
     */
    "Rejected Gateway": "Rejected Gateway",

    /**
     * value: "Rejected Jopari"
     * @const
     */
    "Rejected Jopari": "Rejected Jopari",

    /**
     * value: "Rejected Waystar"
     * @const
     */
    "Rejected Waystar": "Rejected Waystar",

    /**
     * value: "In Process Payer"
     * @const
     */
    "In Process Payer": "In Process Payer",

    /**
     * value: "Payer Acknowledged"
     * @const
     */
    "Payer Acknowledged": "Payer Acknowledged",

    /**
     * value: "Rejected Payer"
     * @const
     */
    "Rejected Payer": "Rejected Payer",

    /**
     * value: "Paid in Full"
     * @const
     */
    "Paid in Full": "Paid in Full",

    /**
     * value: "Partially Paid"
     * @const
     */
    "Partially Paid": "Partially Paid",

    /**
     * value: "Coordination of Benefits"
     * @const
     */
    "Coordination of Benefits": "Coordination of Benefits",

    /**
     * value: "ERA Received"
     * @const
     */
    "ERA Received": "ERA Received",

    /**
     * value: "ERA Denied"
     * @const
     */
    "ERA Denied": "ERA Denied"
};


/**
 * Allowed values for the <code>procedure_type</code> property.
 * @enum {String}
 * @readonly
 */
BillingLineItem['ProcedureTypeEnum'] = {

    /**
     * value: "C"
     * @const
     */
    "C": "C",

    /**
     * value: "H"
     * @const
     */
    "H": "H",

    /**
     * value: "U"
     * @const
     */
    "U": "U",

    /**
     * value: "S"
     * @const
     */
    "S": "S"
};



export default BillingLineItem;

