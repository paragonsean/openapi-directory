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
import VaccineDose from './VaccineDose';

/**
 * The PatientVaccineRecord model module.
 * @module model/PatientVaccineRecord
 * @version v4 (Hunt Valley)
 */
class PatientVaccineRecord {
    /**
     * Constructs a new <code>PatientVaccineRecord</code>.
     * @alias module:model/PatientVaccineRecord
     * @param cvxCode {String} Vaccine cvx code
     * @param name {String} 
     * @param patient {Number} 
     */
    constructor(cvxCode, name, patient) { 
        
        PatientVaccineRecord.initialize(this, cvxCode, name, patient);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, cvxCode, name, patient) { 
        obj['cvx_code'] = cvxCode;
        obj['name'] = name;
        obj['patient'] = patient;
    }

    /**
     * Constructs a <code>PatientVaccineRecord</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PatientVaccineRecord} obj Optional instance to populate.
     * @return {module:model/PatientVaccineRecord} The populated <code>PatientVaccineRecord</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PatientVaccineRecord();

            if (data.hasOwnProperty('administered_at')) {
                obj['administered_at'] = ApiClient.convertToType(data['administered_at'], 'Number');
            }
            if (data.hasOwnProperty('administered_by')) {
                obj['administered_by'] = ApiClient.convertToType(data['administered_by'], 'String');
            }
            if (data.hasOwnProperty('administration_start')) {
                obj['administration_start'] = ApiClient.convertToType(data['administration_start'], 'String');
            }
            if (data.hasOwnProperty('amount')) {
                obj['amount'] = ApiClient.convertToType(data['amount'], 'Number');
            }
            if (data.hasOwnProperty('comments')) {
                obj['comments'] = ApiClient.convertToType(data['comments'], 'String');
            }
            if (data.hasOwnProperty('completion_status')) {
                obj['completion_status'] = ApiClient.convertToType(data['completion_status'], 'String');
            }
            if (data.hasOwnProperty('consent_form')) {
                obj['consent_form'] = ApiClient.convertToType(data['consent_form'], 'Number');
            }
            if (data.hasOwnProperty('cpt_code')) {
                obj['cpt_code'] = ApiClient.convertToType(data['cpt_code'], 'String');
            }
            if (data.hasOwnProperty('created_at')) {
                obj['created_at'] = ApiClient.convertToType(data['created_at'], 'String');
            }
            if (data.hasOwnProperty('cvx_code')) {
                obj['cvx_code'] = ApiClient.convertToType(data['cvx_code'], 'String');
            }
            if (data.hasOwnProperty('doses')) {
                obj['doses'] = ApiClient.convertToType(data['doses'], [VaccineDose]);
            }
            if (data.hasOwnProperty('entered_by')) {
                obj['entered_by'] = ApiClient.convertToType(data['entered_by'], 'String');
            }
            if (data.hasOwnProperty('funding_eligibility')) {
                obj['funding_eligibility'] = ApiClient.convertToType(data['funding_eligibility'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('next_dose_date')) {
                obj['next_dose_date'] = ApiClient.convertToType(data['next_dose_date'], 'String');
            }
            if (data.hasOwnProperty('observed_immunity')) {
                obj['observed_immunity'] = ApiClient.convertToType(data['observed_immunity'], 'String');
            }
            if (data.hasOwnProperty('ordering_doctor')) {
                obj['ordering_doctor'] = ApiClient.convertToType(data['ordering_doctor'], 'Number');
            }
            if (data.hasOwnProperty('patient')) {
                obj['patient'] = ApiClient.convertToType(data['patient'], 'Number');
            }
            if (data.hasOwnProperty('record_source')) {
                obj['record_source'] = ApiClient.convertToType(data['record_source'], 'String');
            }
            if (data.hasOwnProperty('route')) {
                obj['route'] = ApiClient.convertToType(data['route'], 'String');
            }
            if (data.hasOwnProperty('site')) {
                obj['site'] = ApiClient.convertToType(data['site'], 'String');
            }
            if (data.hasOwnProperty('units')) {
                obj['units'] = ApiClient.convertToType(data['units'], 'String');
            }
            if (data.hasOwnProperty('updated_at')) {
                obj['updated_at'] = ApiClient.convertToType(data['updated_at'], 'String');
            }
            if (data.hasOwnProperty('vaccine_inventory')) {
                obj['vaccine_inventory'] = ApiClient.convertToType(data['vaccine_inventory'], 'Number');
            }
            if (data.hasOwnProperty('vis')) {
                obj['vis'] = ApiClient.convertToType(data['vis'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PatientVaccineRecord</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PatientVaccineRecord</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PatientVaccineRecord.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['administered_by'] && !(typeof data['administered_by'] === 'string' || data['administered_by'] instanceof String)) {
            throw new Error("Expected the field `administered_by` to be a primitive type in the JSON string but got " + data['administered_by']);
        }
        // ensure the json data is a string
        if (data['administration_start'] && !(typeof data['administration_start'] === 'string' || data['administration_start'] instanceof String)) {
            throw new Error("Expected the field `administration_start` to be a primitive type in the JSON string but got " + data['administration_start']);
        }
        // ensure the json data is a string
        if (data['comments'] && !(typeof data['comments'] === 'string' || data['comments'] instanceof String)) {
            throw new Error("Expected the field `comments` to be a primitive type in the JSON string but got " + data['comments']);
        }
        // ensure the json data is a string
        if (data['completion_status'] && !(typeof data['completion_status'] === 'string' || data['completion_status'] instanceof String)) {
            throw new Error("Expected the field `completion_status` to be a primitive type in the JSON string but got " + data['completion_status']);
        }
        // ensure the json data is a string
        if (data['cpt_code'] && !(typeof data['cpt_code'] === 'string' || data['cpt_code'] instanceof String)) {
            throw new Error("Expected the field `cpt_code` to be a primitive type in the JSON string but got " + data['cpt_code']);
        }
        // ensure the json data is a string
        if (data['created_at'] && !(typeof data['created_at'] === 'string' || data['created_at'] instanceof String)) {
            throw new Error("Expected the field `created_at` to be a primitive type in the JSON string but got " + data['created_at']);
        }
        // ensure the json data is a string
        if (data['cvx_code'] && !(typeof data['cvx_code'] === 'string' || data['cvx_code'] instanceof String)) {
            throw new Error("Expected the field `cvx_code` to be a primitive type in the JSON string but got " + data['cvx_code']);
        }
        if (data['doses']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['doses'])) {
                throw new Error("Expected the field `doses` to be an array in the JSON data but got " + data['doses']);
            }
            // validate the optional field `doses` (array)
            for (const item of data['doses']) {
                VaccineDose.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['entered_by'] && !(typeof data['entered_by'] === 'string' || data['entered_by'] instanceof String)) {
            throw new Error("Expected the field `entered_by` to be a primitive type in the JSON string but got " + data['entered_by']);
        }
        // ensure the json data is a string
        if (data['funding_eligibility'] && !(typeof data['funding_eligibility'] === 'string' || data['funding_eligibility'] instanceof String)) {
            throw new Error("Expected the field `funding_eligibility` to be a primitive type in the JSON string but got " + data['funding_eligibility']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['next_dose_date'] && !(typeof data['next_dose_date'] === 'string' || data['next_dose_date'] instanceof String)) {
            throw new Error("Expected the field `next_dose_date` to be a primitive type in the JSON string but got " + data['next_dose_date']);
        }
        // ensure the json data is a string
        if (data['observed_immunity'] && !(typeof data['observed_immunity'] === 'string' || data['observed_immunity'] instanceof String)) {
            throw new Error("Expected the field `observed_immunity` to be a primitive type in the JSON string but got " + data['observed_immunity']);
        }
        // ensure the json data is a string
        if (data['record_source'] && !(typeof data['record_source'] === 'string' || data['record_source'] instanceof String)) {
            throw new Error("Expected the field `record_source` to be a primitive type in the JSON string but got " + data['record_source']);
        }
        // ensure the json data is a string
        if (data['route'] && !(typeof data['route'] === 'string' || data['route'] instanceof String)) {
            throw new Error("Expected the field `route` to be a primitive type in the JSON string but got " + data['route']);
        }
        // ensure the json data is a string
        if (data['site'] && !(typeof data['site'] === 'string' || data['site'] instanceof String)) {
            throw new Error("Expected the field `site` to be a primitive type in the JSON string but got " + data['site']);
        }
        // ensure the json data is a string
        if (data['units'] && !(typeof data['units'] === 'string' || data['units'] instanceof String)) {
            throw new Error("Expected the field `units` to be a primitive type in the JSON string but got " + data['units']);
        }
        // ensure the json data is a string
        if (data['updated_at'] && !(typeof data['updated_at'] === 'string' || data['updated_at'] instanceof String)) {
            throw new Error("Expected the field `updated_at` to be a primitive type in the JSON string but got " + data['updated_at']);
        }
        // ensure the json data is a string
        if (data['vis'] && !(typeof data['vis'] === 'string' || data['vis'] instanceof String)) {
            throw new Error("Expected the field `vis` to be a primitive type in the JSON string but got " + data['vis']);
        }

        return true;
    }


}

PatientVaccineRecord.RequiredProperties = ["cvx_code", "name", "patient"];

/**
 * ID of `/api/offices` where the administration happened
 * @member {Number} administered_at
 */
PatientVaccineRecord.prototype['administered_at'] = undefined;

/**
 * ID of `/api/users` who performs the administration
 * @member {String} administered_by
 */
PatientVaccineRecord.prototype['administered_by'] = undefined;

/**
 * Datetime when the administration starts
 * @member {String} administration_start
 */
PatientVaccineRecord.prototype['administration_start'] = undefined;

/**
 * Amount of vaccine administered
 * @member {Number} amount
 */
PatientVaccineRecord.prototype['amount'] = undefined;

/**
 * 
 * @member {String} comments
 */
PatientVaccineRecord.prototype['comments'] = undefined;

/**
 * Vaccination status, can be `CP`(Complete), `RE`(Refused), `NA`(Not administered), `PA`(Partially administered)
 * @member {module:model/PatientVaccineRecord.CompletionStatusEnum} completion_status
 */
PatientVaccineRecord.prototype['completion_status'] = undefined;

/**
 * Consent form related with vaccine record
 * @member {Number} consent_form
 */
PatientVaccineRecord.prototype['consent_form'] = undefined;

/**
 * Vaccine cpt code
 * @member {String} cpt_code
 */
PatientVaccineRecord.prototype['cpt_code'] = undefined;

/**
 * 
 * @member {String} created_at
 */
PatientVaccineRecord.prototype['created_at'] = undefined;

/**
 * Vaccine cvx code
 * @member {String} cvx_code
 */
PatientVaccineRecord.prototype['cvx_code'] = undefined;

/**
 * Vaccine dose IDs received in consent form signed hook
 * @member {Array.<module:model/VaccineDose>} doses
 */
PatientVaccineRecord.prototype['doses'] = undefined;

/**
 * ID of user who created the record
 * @member {String} entered_by
 */
PatientVaccineRecord.prototype['entered_by'] = undefined;

/**
 * The funding program that should pay for a given immunization
 * @member {module:model/PatientVaccineRecord.FundingEligibilityEnum} funding_eligibility
 */
PatientVaccineRecord.prototype['funding_eligibility'] = undefined;

/**
 * 
 * @member {Number} id
 */
PatientVaccineRecord.prototype['id'] = undefined;

/**
 * 
 * @member {String} name
 */
PatientVaccineRecord.prototype['name'] = undefined;

/**
 * Date for next dose of vaccine
 * @member {String} next_dose_date
 */
PatientVaccineRecord.prototype['next_dose_date'] = undefined;

/**
 * 
 * @member {module:model/PatientVaccineRecord.ObservedImmunityEnum} observed_immunity
 */
PatientVaccineRecord.prototype['observed_immunity'] = undefined;

/**
 * 
 * @member {Number} ordering_doctor
 */
PatientVaccineRecord.prototype['ordering_doctor'] = undefined;

/**
 * 
 * @member {Number} patient
 */
PatientVaccineRecord.prototype['patient'] = undefined;

/**
 * 
 * @member {module:model/PatientVaccineRecord.RecordSourceEnum} record_source
 */
PatientVaccineRecord.prototype['record_source'] = undefined;

/**
 * 
 * @member {String} route
 */
PatientVaccineRecord.prototype['route'] = undefined;

/**
 * 
 * @member {String} site
 */
PatientVaccineRecord.prototype['site'] = undefined;

/**
 * 
 * @member {String} units
 */
PatientVaccineRecord.prototype['units'] = undefined;

/**
 * 
 * @member {String} updated_at
 */
PatientVaccineRecord.prototype['updated_at'] = undefined;

/**
 * ID of `/api/vaccine_inventories` the vaccine is from
 * @member {Number} vaccine_inventory
 */
PatientVaccineRecord.prototype['vaccine_inventory'] = undefined;

/**
 * Related vaccine information statement
 * @member {String} vis
 */
PatientVaccineRecord.prototype['vis'] = undefined;





/**
 * Allowed values for the <code>completion_status</code> property.
 * @enum {String}
 * @readonly
 */
PatientVaccineRecord['CompletionStatusEnum'] = {

    /**
     * value: "CP"
     * @const
     */
    "CP": "CP",

    /**
     * value: "RE"
     * @const
     */
    "RE": "RE",

    /**
     * value: "NA"
     * @const
     */
    "NA": "NA",

    /**
     * value: "PA"
     * @const
     */
    "PA": "PA"
};


/**
 * Allowed values for the <code>funding_eligibility</code> property.
 * @enum {String}
 * @readonly
 */
PatientVaccineRecord['FundingEligibilityEnum'] = {

    /**
     * value: "V01"
     * @const
     */
    "V01": "V01",

    /**
     * value: "V02"
     * @const
     */
    "V02": "V02",

    /**
     * value: "V03"
     * @const
     */
    "V03": "V03",

    /**
     * value: "V04"
     * @const
     */
    "V04": "V04",

    /**
     * value: "V05"
     * @const
     */
    "V05": "V05",

    /**
     * value: "V07"
     * @const
     */
    "V07": "V07"
};


/**
 * Allowed values for the <code>observed_immunity</code> property.
 * @enum {String}
 * @readonly
 */
PatientVaccineRecord['ObservedImmunityEnum'] = {

    /**
     * value: "398102009"
     * @const
     */
    "398102009": "398102009",

    /**
     * value: "409498004"
     * @const
     */
    "409498004": "409498004",

    /**
     * value: "397428000"
     * @const
     */
    "397428000": "397428000",

    /**
     * value: "18624000"
     * @const
     */
    "18624000": "18624000",

    /**
     * value: "91428005"
     * @const
     */
    "91428005": "91428005",

    /**
     * value: "271511000"
     * @const
     */
    "271511000": "271511000",

    /**
     * value: "240532009"
     * @const
     */
    "240532009": "240532009",

    /**
     * value: "6142004"
     * @const
     */
    "6142004": "6142004",

    /**
     * value: "52947006"
     * @const
     */
    "52947006": "52947006",

    /**
     * value: "14189004"
     * @const
     */
    "14189004": "14189004",

    /**
     * value: "23511006"
     * @const
     */
    "23511006": "23511006",

    /**
     * value: "36989005"
     * @const
     */
    "36989005": "36989005",

    /**
     * value: "27836007"
     * @const
     */
    "27836007": "27836007",

    /**
     * value: "16814004"
     * @const
     */
    "16814004": "16814004",

    /**
     * value: "14168008"
     * @const
     */
    "14168008": "14168008",

    /**
     * value: "36653000"
     * @const
     */
    "36653000": "36653000",

    /**
     * value: "76902006"
     * @const
     */
    "76902006": "76902006",

    /**
     * value: "66071002"
     * @const
     */
    "66071002": "66071002",

    /**
     * value: "4834000"
     * @const
     */
    "4834000": "4834000",

    /**
     * value: "111852003"
     * @const
     */
    "111852003": "111852003",

    /**
     * value: "38907003"
     * @const
     */
    "38907003": "38907003",

    /**
     * value: "40468003"
     * @const
     */
    "40468003": "40468003",

    /**
     * value: "16541001"
     * @const
     */
    "16541001": "16541001"
};


/**
 * Allowed values for the <code>record_source</code> property.
 * @enum {String}
 * @readonly
 */
PatientVaccineRecord['RecordSourceEnum'] = {

    /**
     * value: "00"
     * @const
     */
    "00": "00",

    /**
     * value: "01"
     * @const
     */
    "01": "01",

    /**
     * value: "02"
     * @const
     */
    "02": "02",

    /**
     * value: "03"
     * @const
     */
    "03": "03",

    /**
     * value: "04"
     * @const
     */
    "04": "04",

    /**
     * value: "05"
     * @const
     */
    "05": "05",

    /**
     * value: "06"
     * @const
     */
    "06": "06",

    /**
     * value: "07"
     * @const
     */
    "07": "07",

    /**
     * value: "08"
     * @const
     */
    "08": "08"
};



export default PatientVaccineRecord;

