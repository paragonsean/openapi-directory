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
import AutoAccidentInsurance from './AutoAccidentInsurance';
import CustomPatientFieldValue from './CustomPatientFieldValue';
import Patient1 from './Patient1';
import PatientFlag from './PatientFlag';
import PatientFlagType1 from './PatientFlagType1';
import PrimaryInsurance from './PrimaryInsurance';
import SecondaryInsurance from './SecondaryInsurance';
import TertiaryInsurance from './TertiaryInsurance';
import WorkerCompInsurance from './WorkerCompInsurance';

/**
 * The Patient model module.
 * @module model/Patient
 * @version v4 (Hunt Valley)
 */
class Patient {
    /**
     * Constructs a new <code>Patient</code>.
     * @alias module:model/Patient
     * @param doctor {Number} 
     * @param gender {module:model/Patient.GenderEnum} One of `\"Male\"`, `\"Female\"`, or `\"Other\"`
     */
    constructor(doctor, gender) { 
        
        Patient.initialize(this, doctor, gender);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, doctor, gender) { 
        obj['doctor'] = doctor;
        obj['gender'] = gender;
    }

    /**
     * Constructs a <code>Patient</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Patient} obj Optional instance to populate.
     * @return {module:model/Patient} The populated <code>Patient</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Patient();

            if (data.hasOwnProperty('address')) {
                obj['address'] = ApiClient.convertToType(data['address'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_insurance')) {
                obj['auto_accident_insurance'] = AutoAccidentInsurance.constructFromObject(data['auto_accident_insurance']);
            }
            if (data.hasOwnProperty('cell_phone')) {
                obj['cell_phone'] = ApiClient.convertToType(data['cell_phone'], 'String');
            }
            if (data.hasOwnProperty('chart_id')) {
                obj['chart_id'] = ApiClient.convertToType(data['chart_id'], 'String');
            }
            if (data.hasOwnProperty('city')) {
                obj['city'] = ApiClient.convertToType(data['city'], 'String');
            }
            if (data.hasOwnProperty('copay')) {
                obj['copay'] = ApiClient.convertToType(data['copay'], 'String');
            }
            if (data.hasOwnProperty('custom_demographics')) {
                obj['custom_demographics'] = ApiClient.convertToType(data['custom_demographics'], [CustomPatientFieldValue]);
            }
            if (data.hasOwnProperty('date_of_birth')) {
                obj['date_of_birth'] = ApiClient.convertToType(data['date_of_birth'], 'String');
            }
            if (data.hasOwnProperty('date_of_first_appointment')) {
                obj['date_of_first_appointment'] = ApiClient.convertToType(data['date_of_first_appointment'], 'String');
            }
            if (data.hasOwnProperty('date_of_last_appointment')) {
                obj['date_of_last_appointment'] = ApiClient.convertToType(data['date_of_last_appointment'], 'String');
            }
            if (data.hasOwnProperty('default_pharmacy')) {
                obj['default_pharmacy'] = ApiClient.convertToType(data['default_pharmacy'], 'String');
            }
            if (data.hasOwnProperty('disable_sms_messages')) {
                obj['disable_sms_messages'] = ApiClient.convertToType(data['disable_sms_messages'], 'Boolean');
            }
            if (data.hasOwnProperty('doctor')) {
                obj['doctor'] = ApiClient.convertToType(data['doctor'], 'Number');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('emergency_contact_name')) {
                obj['emergency_contact_name'] = ApiClient.convertToType(data['emergency_contact_name'], 'String');
            }
            if (data.hasOwnProperty('emergency_contact_phone')) {
                obj['emergency_contact_phone'] = ApiClient.convertToType(data['emergency_contact_phone'], 'String');
            }
            if (data.hasOwnProperty('emergency_contact_relation')) {
                obj['emergency_contact_relation'] = ApiClient.convertToType(data['emergency_contact_relation'], 'String');
            }
            if (data.hasOwnProperty('employer')) {
                obj['employer'] = ApiClient.convertToType(data['employer'], 'String');
            }
            if (data.hasOwnProperty('employer_address')) {
                obj['employer_address'] = ApiClient.convertToType(data['employer_address'], 'String');
            }
            if (data.hasOwnProperty('employer_city')) {
                obj['employer_city'] = ApiClient.convertToType(data['employer_city'], 'String');
            }
            if (data.hasOwnProperty('employer_state')) {
                obj['employer_state'] = ApiClient.convertToType(data['employer_state'], 'String');
            }
            if (data.hasOwnProperty('employer_zip_code')) {
                obj['employer_zip_code'] = ApiClient.convertToType(data['employer_zip_code'], 'String');
            }
            if (data.hasOwnProperty('ethnicity')) {
                obj['ethnicity'] = ApiClient.convertToType(data['ethnicity'], 'String');
            }
            if (data.hasOwnProperty('first_name')) {
                obj['first_name'] = ApiClient.convertToType(data['first_name'], 'String');
            }
            if (data.hasOwnProperty('gender')) {
                obj['gender'] = ApiClient.convertToType(data['gender'], 'String');
            }
            if (data.hasOwnProperty('home_phone')) {
                obj['home_phone'] = ApiClient.convertToType(data['home_phone'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('last_name')) {
                obj['last_name'] = ApiClient.convertToType(data['last_name'], 'String');
            }
            if (data.hasOwnProperty('middle_name')) {
                obj['middle_name'] = ApiClient.convertToType(data['middle_name'], 'String');
            }
            if (data.hasOwnProperty('nick_name')) {
                obj['nick_name'] = ApiClient.convertToType(data['nick_name'], 'String');
            }
            if (data.hasOwnProperty('office_phone')) {
                obj['office_phone'] = ApiClient.convertToType(data['office_phone'], 'String');
            }
            if (data.hasOwnProperty('offices')) {
                obj['offices'] = ApiClient.convertToType(data['offices'], ['Number']);
            }
            if (data.hasOwnProperty('patient_flags')) {
                obj['patient_flags'] = ApiClient.convertToType(data['patient_flags'], [PatientFlagType1]);
            }
            if (data.hasOwnProperty('patient_flags_attached')) {
                obj['patient_flags_attached'] = ApiClient.convertToType(data['patient_flags_attached'], [PatientFlag]);
            }
            if (data.hasOwnProperty('patient_payment_profile')) {
                obj['patient_payment_profile'] = ApiClient.convertToType(data['patient_payment_profile'], 'String');
            }
            if (data.hasOwnProperty('patient_photo')) {
                obj['patient_photo'] = ApiClient.convertToType(data['patient_photo'], 'String');
            }
            if (data.hasOwnProperty('patient_photo_date')) {
                obj['patient_photo_date'] = ApiClient.convertToType(data['patient_photo_date'], 'String');
            }
            if (data.hasOwnProperty('patient_status')) {
                obj['patient_status'] = ApiClient.convertToType(data['patient_status'], 'String');
            }
            if (data.hasOwnProperty('preferred_language')) {
                obj['preferred_language'] = ApiClient.convertToType(data['preferred_language'], 'String');
            }
            if (data.hasOwnProperty('primary_care_physician')) {
                obj['primary_care_physician'] = ApiClient.convertToType(data['primary_care_physician'], 'String');
            }
            if (data.hasOwnProperty('primary_insurance')) {
                obj['primary_insurance'] = PrimaryInsurance.constructFromObject(data['primary_insurance']);
            }
            if (data.hasOwnProperty('race')) {
                obj['race'] = ApiClient.convertToType(data['race'], 'String');
            }
            if (data.hasOwnProperty('referring_doctor')) {
                obj['referring_doctor'] = Patient1.constructFromObject(data['referring_doctor']);
            }
            if (data.hasOwnProperty('referring_source')) {
                obj['referring_source'] = ApiClient.convertToType(data['referring_source'], 'String');
            }
            if (data.hasOwnProperty('responsible_party_email')) {
                obj['responsible_party_email'] = ApiClient.convertToType(data['responsible_party_email'], 'String');
            }
            if (data.hasOwnProperty('responsible_party_name')) {
                obj['responsible_party_name'] = ApiClient.convertToType(data['responsible_party_name'], 'String');
            }
            if (data.hasOwnProperty('responsible_party_phone')) {
                obj['responsible_party_phone'] = ApiClient.convertToType(data['responsible_party_phone'], 'String');
            }
            if (data.hasOwnProperty('responsible_party_relation')) {
                obj['responsible_party_relation'] = ApiClient.convertToType(data['responsible_party_relation'], 'String');
            }
            if (data.hasOwnProperty('secondary_insurance')) {
                obj['secondary_insurance'] = SecondaryInsurance.constructFromObject(data['secondary_insurance']);
            }
            if (data.hasOwnProperty('social_security_number')) {
                obj['social_security_number'] = ApiClient.convertToType(data['social_security_number'], 'String');
            }
            if (data.hasOwnProperty('state')) {
                obj['state'] = ApiClient.convertToType(data['state'], 'String');
            }
            if (data.hasOwnProperty('tertiary_insurance')) {
                obj['tertiary_insurance'] = TertiaryInsurance.constructFromObject(data['tertiary_insurance']);
            }
            if (data.hasOwnProperty('updated_at')) {
                obj['updated_at'] = ApiClient.convertToType(data['updated_at'], 'String');
            }
            if (data.hasOwnProperty('workers_comp_insurance')) {
                obj['workers_comp_insurance'] = WorkerCompInsurance.constructFromObject(data['workers_comp_insurance']);
            }
            if (data.hasOwnProperty('zip_code')) {
                obj['zip_code'] = ApiClient.convertToType(data['zip_code'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Patient</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Patient</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Patient.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['address'] && !(typeof data['address'] === 'string' || data['address'] instanceof String)) {
            throw new Error("Expected the field `address` to be a primitive type in the JSON string but got " + data['address']);
        }
        // validate the optional field `auto_accident_insurance`
        if (data['auto_accident_insurance']) { // data not null
          AutoAccidentInsurance.validateJSON(data['auto_accident_insurance']);
        }
        // ensure the json data is a string
        if (data['cell_phone'] && !(typeof data['cell_phone'] === 'string' || data['cell_phone'] instanceof String)) {
            throw new Error("Expected the field `cell_phone` to be a primitive type in the JSON string but got " + data['cell_phone']);
        }
        // ensure the json data is a string
        if (data['chart_id'] && !(typeof data['chart_id'] === 'string' || data['chart_id'] instanceof String)) {
            throw new Error("Expected the field `chart_id` to be a primitive type in the JSON string but got " + data['chart_id']);
        }
        // ensure the json data is a string
        if (data['city'] && !(typeof data['city'] === 'string' || data['city'] instanceof String)) {
            throw new Error("Expected the field `city` to be a primitive type in the JSON string but got " + data['city']);
        }
        // ensure the json data is a string
        if (data['copay'] && !(typeof data['copay'] === 'string' || data['copay'] instanceof String)) {
            throw new Error("Expected the field `copay` to be a primitive type in the JSON string but got " + data['copay']);
        }
        if (data['custom_demographics']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['custom_demographics'])) {
                throw new Error("Expected the field `custom_demographics` to be an array in the JSON data but got " + data['custom_demographics']);
            }
            // validate the optional field `custom_demographics` (array)
            for (const item of data['custom_demographics']) {
                CustomPatientFieldValue.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['date_of_birth'] && !(typeof data['date_of_birth'] === 'string' || data['date_of_birth'] instanceof String)) {
            throw new Error("Expected the field `date_of_birth` to be a primitive type in the JSON string but got " + data['date_of_birth']);
        }
        // ensure the json data is a string
        if (data['date_of_first_appointment'] && !(typeof data['date_of_first_appointment'] === 'string' || data['date_of_first_appointment'] instanceof String)) {
            throw new Error("Expected the field `date_of_first_appointment` to be a primitive type in the JSON string but got " + data['date_of_first_appointment']);
        }
        // ensure the json data is a string
        if (data['date_of_last_appointment'] && !(typeof data['date_of_last_appointment'] === 'string' || data['date_of_last_appointment'] instanceof String)) {
            throw new Error("Expected the field `date_of_last_appointment` to be a primitive type in the JSON string but got " + data['date_of_last_appointment']);
        }
        // ensure the json data is a string
        if (data['default_pharmacy'] && !(typeof data['default_pharmacy'] === 'string' || data['default_pharmacy'] instanceof String)) {
            throw new Error("Expected the field `default_pharmacy` to be a primitive type in the JSON string but got " + data['default_pharmacy']);
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['emergency_contact_name'] && !(typeof data['emergency_contact_name'] === 'string' || data['emergency_contact_name'] instanceof String)) {
            throw new Error("Expected the field `emergency_contact_name` to be a primitive type in the JSON string but got " + data['emergency_contact_name']);
        }
        // ensure the json data is a string
        if (data['emergency_contact_phone'] && !(typeof data['emergency_contact_phone'] === 'string' || data['emergency_contact_phone'] instanceof String)) {
            throw new Error("Expected the field `emergency_contact_phone` to be a primitive type in the JSON string but got " + data['emergency_contact_phone']);
        }
        // ensure the json data is a string
        if (data['emergency_contact_relation'] && !(typeof data['emergency_contact_relation'] === 'string' || data['emergency_contact_relation'] instanceof String)) {
            throw new Error("Expected the field `emergency_contact_relation` to be a primitive type in the JSON string but got " + data['emergency_contact_relation']);
        }
        // ensure the json data is a string
        if (data['employer'] && !(typeof data['employer'] === 'string' || data['employer'] instanceof String)) {
            throw new Error("Expected the field `employer` to be a primitive type in the JSON string but got " + data['employer']);
        }
        // ensure the json data is a string
        if (data['employer_address'] && !(typeof data['employer_address'] === 'string' || data['employer_address'] instanceof String)) {
            throw new Error("Expected the field `employer_address` to be a primitive type in the JSON string but got " + data['employer_address']);
        }
        // ensure the json data is a string
        if (data['employer_city'] && !(typeof data['employer_city'] === 'string' || data['employer_city'] instanceof String)) {
            throw new Error("Expected the field `employer_city` to be a primitive type in the JSON string but got " + data['employer_city']);
        }
        // ensure the json data is a string
        if (data['employer_state'] && !(typeof data['employer_state'] === 'string' || data['employer_state'] instanceof String)) {
            throw new Error("Expected the field `employer_state` to be a primitive type in the JSON string but got " + data['employer_state']);
        }
        // ensure the json data is a string
        if (data['employer_zip_code'] && !(typeof data['employer_zip_code'] === 'string' || data['employer_zip_code'] instanceof String)) {
            throw new Error("Expected the field `employer_zip_code` to be a primitive type in the JSON string but got " + data['employer_zip_code']);
        }
        // ensure the json data is a string
        if (data['ethnicity'] && !(typeof data['ethnicity'] === 'string' || data['ethnicity'] instanceof String)) {
            throw new Error("Expected the field `ethnicity` to be a primitive type in the JSON string but got " + data['ethnicity']);
        }
        // ensure the json data is a string
        if (data['first_name'] && !(typeof data['first_name'] === 'string' || data['first_name'] instanceof String)) {
            throw new Error("Expected the field `first_name` to be a primitive type in the JSON string but got " + data['first_name']);
        }
        // ensure the json data is a string
        if (data['gender'] && !(typeof data['gender'] === 'string' || data['gender'] instanceof String)) {
            throw new Error("Expected the field `gender` to be a primitive type in the JSON string but got " + data['gender']);
        }
        // ensure the json data is a string
        if (data['home_phone'] && !(typeof data['home_phone'] === 'string' || data['home_phone'] instanceof String)) {
            throw new Error("Expected the field `home_phone` to be a primitive type in the JSON string but got " + data['home_phone']);
        }
        // ensure the json data is a string
        if (data['last_name'] && !(typeof data['last_name'] === 'string' || data['last_name'] instanceof String)) {
            throw new Error("Expected the field `last_name` to be a primitive type in the JSON string but got " + data['last_name']);
        }
        // ensure the json data is a string
        if (data['middle_name'] && !(typeof data['middle_name'] === 'string' || data['middle_name'] instanceof String)) {
            throw new Error("Expected the field `middle_name` to be a primitive type in the JSON string but got " + data['middle_name']);
        }
        // ensure the json data is a string
        if (data['nick_name'] && !(typeof data['nick_name'] === 'string' || data['nick_name'] instanceof String)) {
            throw new Error("Expected the field `nick_name` to be a primitive type in the JSON string but got " + data['nick_name']);
        }
        // ensure the json data is a string
        if (data['office_phone'] && !(typeof data['office_phone'] === 'string' || data['office_phone'] instanceof String)) {
            throw new Error("Expected the field `office_phone` to be a primitive type in the JSON string but got " + data['office_phone']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['offices'])) {
            throw new Error("Expected the field `offices` to be an array in the JSON data but got " + data['offices']);
        }
        if (data['patient_flags']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['patient_flags'])) {
                throw new Error("Expected the field `patient_flags` to be an array in the JSON data but got " + data['patient_flags']);
            }
            // validate the optional field `patient_flags` (array)
            for (const item of data['patient_flags']) {
                PatientFlagType1.validateJSON(item);
            };
        }
        if (data['patient_flags_attached']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['patient_flags_attached'])) {
                throw new Error("Expected the field `patient_flags_attached` to be an array in the JSON data but got " + data['patient_flags_attached']);
            }
            // validate the optional field `patient_flags_attached` (array)
            for (const item of data['patient_flags_attached']) {
                PatientFlag.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['patient_payment_profile'] && !(typeof data['patient_payment_profile'] === 'string' || data['patient_payment_profile'] instanceof String)) {
            throw new Error("Expected the field `patient_payment_profile` to be a primitive type in the JSON string but got " + data['patient_payment_profile']);
        }
        // ensure the json data is a string
        if (data['patient_photo'] && !(typeof data['patient_photo'] === 'string' || data['patient_photo'] instanceof String)) {
            throw new Error("Expected the field `patient_photo` to be a primitive type in the JSON string but got " + data['patient_photo']);
        }
        // ensure the json data is a string
        if (data['patient_photo_date'] && !(typeof data['patient_photo_date'] === 'string' || data['patient_photo_date'] instanceof String)) {
            throw new Error("Expected the field `patient_photo_date` to be a primitive type in the JSON string but got " + data['patient_photo_date']);
        }
        // ensure the json data is a string
        if (data['patient_status'] && !(typeof data['patient_status'] === 'string' || data['patient_status'] instanceof String)) {
            throw new Error("Expected the field `patient_status` to be a primitive type in the JSON string but got " + data['patient_status']);
        }
        // ensure the json data is a string
        if (data['preferred_language'] && !(typeof data['preferred_language'] === 'string' || data['preferred_language'] instanceof String)) {
            throw new Error("Expected the field `preferred_language` to be a primitive type in the JSON string but got " + data['preferred_language']);
        }
        // ensure the json data is a string
        if (data['primary_care_physician'] && !(typeof data['primary_care_physician'] === 'string' || data['primary_care_physician'] instanceof String)) {
            throw new Error("Expected the field `primary_care_physician` to be a primitive type in the JSON string but got " + data['primary_care_physician']);
        }
        // validate the optional field `primary_insurance`
        if (data['primary_insurance']) { // data not null
          PrimaryInsurance.validateJSON(data['primary_insurance']);
        }
        // ensure the json data is a string
        if (data['race'] && !(typeof data['race'] === 'string' || data['race'] instanceof String)) {
            throw new Error("Expected the field `race` to be a primitive type in the JSON string but got " + data['race']);
        }
        // validate the optional field `referring_doctor`
        if (data['referring_doctor']) { // data not null
          Patient1.validateJSON(data['referring_doctor']);
        }
        // ensure the json data is a string
        if (data['referring_source'] && !(typeof data['referring_source'] === 'string' || data['referring_source'] instanceof String)) {
            throw new Error("Expected the field `referring_source` to be a primitive type in the JSON string but got " + data['referring_source']);
        }
        // ensure the json data is a string
        if (data['responsible_party_email'] && !(typeof data['responsible_party_email'] === 'string' || data['responsible_party_email'] instanceof String)) {
            throw new Error("Expected the field `responsible_party_email` to be a primitive type in the JSON string but got " + data['responsible_party_email']);
        }
        // ensure the json data is a string
        if (data['responsible_party_name'] && !(typeof data['responsible_party_name'] === 'string' || data['responsible_party_name'] instanceof String)) {
            throw new Error("Expected the field `responsible_party_name` to be a primitive type in the JSON string but got " + data['responsible_party_name']);
        }
        // ensure the json data is a string
        if (data['responsible_party_phone'] && !(typeof data['responsible_party_phone'] === 'string' || data['responsible_party_phone'] instanceof String)) {
            throw new Error("Expected the field `responsible_party_phone` to be a primitive type in the JSON string but got " + data['responsible_party_phone']);
        }
        // ensure the json data is a string
        if (data['responsible_party_relation'] && !(typeof data['responsible_party_relation'] === 'string' || data['responsible_party_relation'] instanceof String)) {
            throw new Error("Expected the field `responsible_party_relation` to be a primitive type in the JSON string but got " + data['responsible_party_relation']);
        }
        // validate the optional field `secondary_insurance`
        if (data['secondary_insurance']) { // data not null
          SecondaryInsurance.validateJSON(data['secondary_insurance']);
        }
        // ensure the json data is a string
        if (data['social_security_number'] && !(typeof data['social_security_number'] === 'string' || data['social_security_number'] instanceof String)) {
            throw new Error("Expected the field `social_security_number` to be a primitive type in the JSON string but got " + data['social_security_number']);
        }
        // ensure the json data is a string
        if (data['state'] && !(typeof data['state'] === 'string' || data['state'] instanceof String)) {
            throw new Error("Expected the field `state` to be a primitive type in the JSON string but got " + data['state']);
        }
        // validate the optional field `tertiary_insurance`
        if (data['tertiary_insurance']) { // data not null
          TertiaryInsurance.validateJSON(data['tertiary_insurance']);
        }
        // ensure the json data is a string
        if (data['updated_at'] && !(typeof data['updated_at'] === 'string' || data['updated_at'] instanceof String)) {
            throw new Error("Expected the field `updated_at` to be a primitive type in the JSON string but got " + data['updated_at']);
        }
        // validate the optional field `workers_comp_insurance`
        if (data['workers_comp_insurance']) { // data not null
          WorkerCompInsurance.validateJSON(data['workers_comp_insurance']);
        }
        // ensure the json data is a string
        if (data['zip_code'] && !(typeof data['zip_code'] === 'string' || data['zip_code'] instanceof String)) {
            throw new Error("Expected the field `zip_code` to be a primitive type in the JSON string but got " + data['zip_code']);
        }

        return true;
    }


}

Patient.RequiredProperties = ["doctor", "gender"];

/**
 * 
 * @member {String} address
 */
Patient.prototype['address'] = undefined;

/**
 * @member {module:model/AutoAccidentInsurance} auto_accident_insurance
 */
Patient.prototype['auto_accident_insurance'] = undefined;

/**
 * 
 * @member {String} cell_phone
 */
Patient.prototype['cell_phone'] = undefined;

/**
 * Automatically set using first & last name if absent
 * @member {String} chart_id
 */
Patient.prototype['chart_id'] = undefined;

/**
 * 
 * @member {String} city
 */
Patient.prototype['city'] = undefined;

/**
 * 
 * @member {String} copay
 */
Patient.prototype['copay'] = undefined;

/**
 * 
 * @member {Array.<module:model/CustomPatientFieldValue>} custom_demographics
 */
Patient.prototype['custom_demographics'] = undefined;

/**
 * 
 * @member {String} date_of_birth
 */
Patient.prototype['date_of_birth'] = undefined;

/**
 * Date of first patient visit.
 * @member {String} date_of_first_appointment
 */
Patient.prototype['date_of_first_appointment'] = undefined;

/**
 * Date of previous patient visit
 * @member {String} date_of_last_appointment
 */
Patient.prototype['date_of_last_appointment'] = undefined;

/**
 * ncpdp id of patient's default pharmacy
 * @member {String} default_pharmacy
 */
Patient.prototype['default_pharmacy'] = undefined;

/**
 * If True, suppress SMS/Txt messages to this patient even if we have a cell phone # for them.
 * @member {Boolean} disable_sms_messages
 */
Patient.prototype['disable_sms_messages'] = undefined;

/**
 * 
 * @member {Number} doctor
 */
Patient.prototype['doctor'] = undefined;

/**
 * 
 * @member {String} email
 */
Patient.prototype['email'] = undefined;

/**
 * 
 * @member {String} emergency_contact_name
 */
Patient.prototype['emergency_contact_name'] = undefined;

/**
 * 
 * @member {String} emergency_contact_phone
 */
Patient.prototype['emergency_contact_phone'] = undefined;

/**
 * 
 * @member {String} emergency_contact_relation
 */
Patient.prototype['emergency_contact_relation'] = undefined;

/**
 * 
 * @member {String} employer
 */
Patient.prototype['employer'] = undefined;

/**
 * 
 * @member {String} employer_address
 */
Patient.prototype['employer_address'] = undefined;

/**
 * 
 * @member {String} employer_city
 */
Patient.prototype['employer_city'] = undefined;

/**
 * Two-letter abbreviation
 * @member {String} employer_state
 */
Patient.prototype['employer_state'] = undefined;

/**
 * 
 * @member {String} employer_zip_code
 */
Patient.prototype['employer_zip_code'] = undefined;

/**
 * One of `\"blank\"`, `\"hispanic\"`, `\"not_hispanic\"` or `\"declined\"`
 * @member {module:model/Patient.EthnicityEnum} ethnicity
 */
Patient.prototype['ethnicity'] = undefined;

/**
 * 
 * @member {String} first_name
 */
Patient.prototype['first_name'] = undefined;

/**
 * One of `\"Male\"`, `\"Female\"`, or `\"Other\"`
 * @member {module:model/Patient.GenderEnum} gender
 */
Patient.prototype['gender'] = undefined;

/**
 * 
 * @member {String} home_phone
 */
Patient.prototype['home_phone'] = undefined;

/**
 * 
 * @member {Number} id
 */
Patient.prototype['id'] = undefined;

/**
 * 
 * @member {String} last_name
 */
Patient.prototype['last_name'] = undefined;

/**
 * 
 * @member {String} middle_name
 */
Patient.prototype['middle_name'] = undefined;

/**
 * Common name for patient, should be used instead of first name if supplied.
 * @member {String} nick_name
 */
Patient.prototype['nick_name'] = undefined;

/**
 * 
 * @member {String} office_phone
 */
Patient.prototype['office_phone'] = undefined;

/**
 * IDs of every office this patient has been to
 * @member {Array.<Number>} offices
 */
Patient.prototype['offices'] = undefined;

/**
 * Possible patient flag type that can be attached to the patient
 * @member {Array.<module:model/PatientFlagType1>} patient_flags
 */
Patient.prototype['patient_flags'] = undefined;

/**
 * Patient flags attached to the patient
 * @member {Array.<module:model/PatientFlag>} patient_flags_attached
 */
Patient.prototype['patient_flags_attached'] = undefined;

/**
 * One of `\"\"`, `\"Cash\"`, `\"Insurance\"`, `\"Insurance Out of Network\"`, `\"Auto Accident\"` or `\"Worker's Comp\"`.<br>**Note:** Patient must already have either `primary_insurance` or `secondary_insurance` or new `primary_insurance` or `secondary_insurance` is passed in request if `Insurance`, `Auto Accident` or `Worker's Comp` payment profiles are chosen.
 * @member {module:model/Patient.PatientPaymentProfileEnum} patient_payment_profile
 */
Patient.prototype['patient_payment_profile'] = undefined;

/**
 * 
 * @member {String} patient_photo
 */
Patient.prototype['patient_photo'] = undefined;

/**
 * Cannot be passed without `patient_photo`
 * @member {String} patient_photo_date
 */
Patient.prototype['patient_photo_date'] = undefined;

/**
 * One of `\"A\"` (active), `\"I\"` (inactive), `\"D\"` (inactive-deceased)
 * @member {module:model/Patient.PatientStatusEnum} patient_status
 */
Patient.prototype['patient_status'] = undefined;

/**
 * Use ISO 639 alpha-3 codes
 * @member {module:model/Patient.PreferredLanguageEnum} preferred_language
 */
Patient.prototype['preferred_language'] = undefined;

/**
 * Referring doctor for this patient
 * @member {String} primary_care_physician
 */
Patient.prototype['primary_care_physician'] = undefined;

/**
 * @member {module:model/PrimaryInsurance} primary_insurance
 */
Patient.prototype['primary_insurance'] = undefined;

/**
 * One of `\"blank\"`, `\"indian\"`, `\"asian\"`, `\"black\"`, `\"hawaiian\"`, `\"white\"` or `\"declined\"`
 * @member {module:model/Patient.RaceEnum} race
 */
Patient.prototype['race'] = undefined;

/**
 * @member {module:model/Patient1} referring_doctor
 */
Patient.prototype['referring_doctor'] = undefined;

/**
 * Referring source.
 * @member {String} referring_source
 */
Patient.prototype['referring_source'] = undefined;

/**
 * 
 * @member {String} responsible_party_email
 */
Patient.prototype['responsible_party_email'] = undefined;

/**
 * 
 * @member {String} responsible_party_name
 */
Patient.prototype['responsible_party_name'] = undefined;

/**
 * 
 * @member {String} responsible_party_phone
 */
Patient.prototype['responsible_party_phone'] = undefined;

/**
 * 
 * @member {String} responsible_party_relation
 */
Patient.prototype['responsible_party_relation'] = undefined;

/**
 * @member {module:model/SecondaryInsurance} secondary_insurance
 */
Patient.prototype['secondary_insurance'] = undefined;

/**
 * 
 * @member {String} social_security_number
 */
Patient.prototype['social_security_number'] = undefined;

/**
 * Two-letter abbreviation
 * @member {String} state
 */
Patient.prototype['state'] = undefined;

/**
 * @member {module:model/TertiaryInsurance} tertiary_insurance
 */
Patient.prototype['tertiary_insurance'] = undefined;

/**
 * 
 * @member {String} updated_at
 */
Patient.prototype['updated_at'] = undefined;

/**
 * @member {module:model/WorkerCompInsurance} workers_comp_insurance
 */
Patient.prototype['workers_comp_insurance'] = undefined;

/**
 * 
 * @member {String} zip_code
 */
Patient.prototype['zip_code'] = undefined;





/**
 * Allowed values for the <code>ethnicity</code> property.
 * @enum {String}
 * @readonly
 */
Patient['EthnicityEnum'] = {

    /**
     * value: "blank"
     * @const
     */
    "blank": "blank",

    /**
     * value: "hispanic"
     * @const
     */
    "hispanic": "hispanic",

    /**
     * value: "not_hispanic"
     * @const
     */
    "not_hispanic": "not_hispanic",

    /**
     * value: "declined"
     * @const
     */
    "declined": "declined"
};


/**
 * Allowed values for the <code>gender</code> property.
 * @enum {String}
 * @readonly
 */
Patient['GenderEnum'] = {

    /**
     * value: ""
     * @const
     */
    "empty": "",

    /**
     * value: "Male"
     * @const
     */
    "Male": "Male",

    /**
     * value: "Female"
     * @const
     */
    "Female": "Female",

    /**
     * value: "Other"
     * @const
     */
    "Other": "Other",

    /**
     * value: "UNK"
     * @const
     */
    "UNK": "UNK",

    /**
     * value: "ASKU"
     * @const
     */
    "ASKU": "ASKU"
};


/**
 * Allowed values for the <code>patient_payment_profile</code> property.
 * @enum {String}
 * @readonly
 */
Patient['PatientPaymentProfileEnum'] = {

    /**
     * value: ""
     * @const
     */
    "empty": "",

    /**
     * value: "Cash"
     * @const
     */
    "Cash": "Cash",

    /**
     * value: "Insurance"
     * @const
     */
    "Insurance": "Insurance",

    /**
     * value: "Insurance Out of Network"
     * @const
     */
    "Insurance Out of Network": "Insurance Out of Network",

    /**
     * value: "Auto Accident"
     * @const
     */
    "Auto Accident": "Auto Accident",

    /**
     * value: "Worker's Comp"
     * @const
     */
    "Worker&#39;s Comp": "Worker's Comp"
};


/**
 * Allowed values for the <code>patient_status</code> property.
 * @enum {String}
 * @readonly
 */
Patient['PatientStatusEnum'] = {

    /**
     * value: "A"
     * @const
     */
    "A": "A",

    /**
     * value: "I"
     * @const
     */
    "I": "I",

    /**
     * value: "D"
     * @const
     */
    "D": "D"
};


/**
 * Allowed values for the <code>preferred_language</code> property.
 * @enum {String}
 * @readonly
 */
Patient['PreferredLanguageEnum'] = {

    /**
     * value: "blank"
     * @const
     */
    "blank": "blank",

    /**
     * value: "eng"
     * @const
     */
    "eng": "eng",

    /**
     * value: "zho"
     * @const
     */
    "zho": "zho",

    /**
     * value: "fra"
     * @const
     */
    "fra": "fra",

    /**
     * value: "ita"
     * @const
     */
    "ita": "ita",

    /**
     * value: "jpn"
     * @const
     */
    "jpn": "jpn",

    /**
     * value: "por"
     * @const
     */
    "por": "por",

    /**
     * value: "rus"
     * @const
     */
    "rus": "rus",

    /**
     * value: "spa"
     * @const
     */
    "spa": "spa",

    /**
     * value: "other"
     * @const
     */
    "other": "other",

    /**
     * value: "unknown"
     * @const
     */
    "unknown": "unknown",

    /**
     * value: "declined"
     * @const
     */
    "declined": "declined"
};


/**
 * Allowed values for the <code>race</code> property.
 * @enum {String}
 * @readonly
 */
Patient['RaceEnum'] = {

    /**
     * value: "blank"
     * @const
     */
    "blank": "blank",

    /**
     * value: "indian"
     * @const
     */
    "indian": "indian",

    /**
     * value: "asian"
     * @const
     */
    "asian": "asian",

    /**
     * value: "black"
     * @const
     */
    "black": "black",

    /**
     * value: "hawaiian"
     * @const
     */
    "hawaiian": "hawaiian",

    /**
     * value: "white"
     * @const
     */
    "white": "white",

    /**
     * value: "other"
     * @const
     */
    "other": "other",

    /**
     * value: "declined"
     * @const
     */
    "declined": "declined"
};



export default Patient;

