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
import AppointmentStatusTransition from './AppointmentStatusTransition';
import ClaimBillingNotes1 from './ClaimBillingNotes1';
import ClinicalNote1 from './ClinicalNote1';
import CustomAppointmentFieldValue from './CustomAppointmentFieldValue';
import CustomVitalValue from './CustomVitalValue';
import SimpleReminder from './SimpleReminder';
import SystemVitals from './SystemVitals';

/**
 * The Appointment model module.
 * @module model/Appointment
 * @version v4 (Hunt Valley)
 */
class Appointment {
    /**
     * Constructs a new <code>Appointment</code>.
     * @alias module:model/Appointment
     * @param doctor {Number} Doctor ID
     * @param examRoom {Number} Index of the exam room that this appointment occurs in. See `/api/offices`
     * @param office {Number} Office ID
     * @param patient {Number} ID of this appointment's patient. Breaks have a null patient field.
     * @param scheduledTime {String} The starting time of the appointment
     */
    constructor(doctor, examRoom, office, patient, scheduledTime) { 
        
        Appointment.initialize(this, doctor, examRoom, office, patient, scheduledTime);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, doctor, examRoom, office, patient, scheduledTime) { 
        obj['doctor'] = doctor;
        obj['exam_room'] = examRoom;
        obj['office'] = office;
        obj['patient'] = patient;
        obj['scheduled_time'] = scheduledTime;
    }

    /**
     * Constructs a <code>Appointment</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Appointment} obj Optional instance to populate.
     * @return {module:model/Appointment} The populated <code>Appointment</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Appointment();

            if (data.hasOwnProperty('allow_overlapping')) {
                obj['allow_overlapping'] = ApiClient.convertToType(data['allow_overlapping'], 'Boolean');
            }
            if (data.hasOwnProperty('appt_is_break')) {
                obj['appt_is_break'] = ApiClient.convertToType(data['appt_is_break'], 'Boolean');
            }
            if (data.hasOwnProperty('base_recurring_appointment')) {
                obj['base_recurring_appointment'] = ApiClient.convertToType(data['base_recurring_appointment'], 'String');
            }
            if (data.hasOwnProperty('billing_notes')) {
                obj['billing_notes'] = ApiClient.convertToType(data['billing_notes'], [ClaimBillingNotes1]);
            }
            if (data.hasOwnProperty('billing_provider')) {
                obj['billing_provider'] = ApiClient.convertToType(data['billing_provider'], 'String');
            }
            if (data.hasOwnProperty('billing_status')) {
                obj['billing_status'] = ApiClient.convertToType(data['billing_status'], 'String');
            }
            if (data.hasOwnProperty('clinical_note')) {
                obj['clinical_note'] = ClinicalNote1.constructFromObject(data['clinical_note']);
            }
            if (data.hasOwnProperty('cloned_from')) {
                obj['cloned_from'] = ApiClient.convertToType(data['cloned_from'], 'Number');
            }
            if (data.hasOwnProperty('color')) {
                obj['color'] = ApiClient.convertToType(data['color'], 'String');
            }
            if (data.hasOwnProperty('created_at')) {
                obj['created_at'] = ApiClient.convertToType(data['created_at'], 'String');
            }
            if (data.hasOwnProperty('custom_fields')) {
                obj['custom_fields'] = ApiClient.convertToType(data['custom_fields'], [CustomAppointmentFieldValue]);
            }
            if (data.hasOwnProperty('custom_vitals')) {
                obj['custom_vitals'] = ApiClient.convertToType(data['custom_vitals'], [CustomVitalValue]);
            }
            if (data.hasOwnProperty('deleted_flag')) {
                obj['deleted_flag'] = ApiClient.convertToType(data['deleted_flag'], 'Boolean');
            }
            if (data.hasOwnProperty('doctor')) {
                obj['doctor'] = ApiClient.convertToType(data['doctor'], 'Number');
            }
            if (data.hasOwnProperty('duration')) {
                obj['duration'] = ApiClient.convertToType(data['duration'], 'Number');
            }
            if (data.hasOwnProperty('exam_room')) {
                obj['exam_room'] = ApiClient.convertToType(data['exam_room'], 'Number');
            }
            if (data.hasOwnProperty('extended_updated_at')) {
                obj['extended_updated_at'] = ApiClient.convertToType(data['extended_updated_at'], 'String');
            }
            if (data.hasOwnProperty('first_billed_date')) {
                obj['first_billed_date'] = ApiClient.convertToType(data['first_billed_date'], 'String');
            }
            if (data.hasOwnProperty('icd10_codes')) {
                obj['icd10_codes'] = ApiClient.convertToType(data['icd10_codes'], ['String']);
            }
            if (data.hasOwnProperty('icd9_codes')) {
                obj['icd9_codes'] = ApiClient.convertToType(data['icd9_codes'], ['String']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('ins1_status')) {
                obj['ins1_status'] = ApiClient.convertToType(data['ins1_status'], 'String');
            }
            if (data.hasOwnProperty('ins2_status')) {
                obj['ins2_status'] = ApiClient.convertToType(data['ins2_status'], 'String');
            }
            if (data.hasOwnProperty('is_virtual_base')) {
                obj['is_virtual_base'] = ApiClient.convertToType(data['is_virtual_base'], 'Boolean');
            }
            if (data.hasOwnProperty('is_walk_in')) {
                obj['is_walk_in'] = ApiClient.convertToType(data['is_walk_in'], 'Boolean');
            }
            if (data.hasOwnProperty('last_billed_date')) {
                obj['last_billed_date'] = ApiClient.convertToType(data['last_billed_date'], 'String');
            }
            if (data.hasOwnProperty('notes')) {
                obj['notes'] = ApiClient.convertToType(data['notes'], 'String');
            }
            if (data.hasOwnProperty('office')) {
                obj['office'] = ApiClient.convertToType(data['office'], 'Number');
            }
            if (data.hasOwnProperty('patient')) {
                obj['patient'] = ApiClient.convertToType(data['patient'], 'Number');
            }
            if (data.hasOwnProperty('primary_insurance_id_number')) {
                obj['primary_insurance_id_number'] = ApiClient.convertToType(data['primary_insurance_id_number'], 'String');
            }
            if (data.hasOwnProperty('primary_insurer_name')) {
                obj['primary_insurer_name'] = ApiClient.convertToType(data['primary_insurer_name'], 'String');
            }
            if (data.hasOwnProperty('primary_insurer_payer_id')) {
                obj['primary_insurer_payer_id'] = ApiClient.convertToType(data['primary_insurer_payer_id'], 'String');
            }
            if (data.hasOwnProperty('profile')) {
                obj['profile'] = ApiClient.convertToType(data['profile'], 'Number');
            }
            if (data.hasOwnProperty('reason')) {
                obj['reason'] = ApiClient.convertToType(data['reason'], 'String');
            }
            if (data.hasOwnProperty('recurring_appointment')) {
                obj['recurring_appointment'] = ApiClient.convertToType(data['recurring_appointment'], 'Boolean');
            }
            if (data.hasOwnProperty('reminder_profile')) {
                obj['reminder_profile'] = ApiClient.convertToType(data['reminder_profile'], 'String');
            }
            if (data.hasOwnProperty('reminders')) {
                obj['reminders'] = ApiClient.convertToType(data['reminders'], [SimpleReminder]);
            }
            if (data.hasOwnProperty('scheduled_time')) {
                obj['scheduled_time'] = ApiClient.convertToType(data['scheduled_time'], 'String');
            }
            if (data.hasOwnProperty('secondary_insurance_id_number')) {
                obj['secondary_insurance_id_number'] = ApiClient.convertToType(data['secondary_insurance_id_number'], 'String');
            }
            if (data.hasOwnProperty('secondary_insurer_name')) {
                obj['secondary_insurer_name'] = ApiClient.convertToType(data['secondary_insurer_name'], 'String');
            }
            if (data.hasOwnProperty('secondary_insurer_payer_id')) {
                obj['secondary_insurer_payer_id'] = ApiClient.convertToType(data['secondary_insurer_payer_id'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('status_transitions')) {
                obj['status_transitions'] = ApiClient.convertToType(data['status_transitions'], [AppointmentStatusTransition]);
            }
            if (data.hasOwnProperty('supervising_provider')) {
                obj['supervising_provider'] = ApiClient.convertToType(data['supervising_provider'], 'String');
            }
            if (data.hasOwnProperty('updated_at')) {
                obj['updated_at'] = ApiClient.convertToType(data['updated_at'], 'String');
            }
            if (data.hasOwnProperty('vitals')) {
                obj['vitals'] = SystemVitals.constructFromObject(data['vitals']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Appointment</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Appointment</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Appointment.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['base_recurring_appointment'] && !(typeof data['base_recurring_appointment'] === 'string' || data['base_recurring_appointment'] instanceof String)) {
            throw new Error("Expected the field `base_recurring_appointment` to be a primitive type in the JSON string but got " + data['base_recurring_appointment']);
        }
        if (data['billing_notes']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['billing_notes'])) {
                throw new Error("Expected the field `billing_notes` to be an array in the JSON data but got " + data['billing_notes']);
            }
            // validate the optional field `billing_notes` (array)
            for (const item of data['billing_notes']) {
                ClaimBillingNotes1.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['billing_provider'] && !(typeof data['billing_provider'] === 'string' || data['billing_provider'] instanceof String)) {
            throw new Error("Expected the field `billing_provider` to be a primitive type in the JSON string but got " + data['billing_provider']);
        }
        // ensure the json data is a string
        if (data['billing_status'] && !(typeof data['billing_status'] === 'string' || data['billing_status'] instanceof String)) {
            throw new Error("Expected the field `billing_status` to be a primitive type in the JSON string but got " + data['billing_status']);
        }
        // validate the optional field `clinical_note`
        if (data['clinical_note']) { // data not null
          ClinicalNote1.validateJSON(data['clinical_note']);
        }
        // ensure the json data is a string
        if (data['color'] && !(typeof data['color'] === 'string' || data['color'] instanceof String)) {
            throw new Error("Expected the field `color` to be a primitive type in the JSON string but got " + data['color']);
        }
        // ensure the json data is a string
        if (data['created_at'] && !(typeof data['created_at'] === 'string' || data['created_at'] instanceof String)) {
            throw new Error("Expected the field `created_at` to be a primitive type in the JSON string but got " + data['created_at']);
        }
        if (data['custom_fields']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['custom_fields'])) {
                throw new Error("Expected the field `custom_fields` to be an array in the JSON data but got " + data['custom_fields']);
            }
            // validate the optional field `custom_fields` (array)
            for (const item of data['custom_fields']) {
                CustomAppointmentFieldValue.validateJSON(item);
            };
        }
        if (data['custom_vitals']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['custom_vitals'])) {
                throw new Error("Expected the field `custom_vitals` to be an array in the JSON data but got " + data['custom_vitals']);
            }
            // validate the optional field `custom_vitals` (array)
            for (const item of data['custom_vitals']) {
                CustomVitalValue.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['extended_updated_at'] && !(typeof data['extended_updated_at'] === 'string' || data['extended_updated_at'] instanceof String)) {
            throw new Error("Expected the field `extended_updated_at` to be a primitive type in the JSON string but got " + data['extended_updated_at']);
        }
        // ensure the json data is a string
        if (data['first_billed_date'] && !(typeof data['first_billed_date'] === 'string' || data['first_billed_date'] instanceof String)) {
            throw new Error("Expected the field `first_billed_date` to be a primitive type in the JSON string but got " + data['first_billed_date']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['icd10_codes'])) {
            throw new Error("Expected the field `icd10_codes` to be an array in the JSON data but got " + data['icd10_codes']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['icd9_codes'])) {
            throw new Error("Expected the field `icd9_codes` to be an array in the JSON data but got " + data['icd9_codes']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['ins1_status'] && !(typeof data['ins1_status'] === 'string' || data['ins1_status'] instanceof String)) {
            throw new Error("Expected the field `ins1_status` to be a primitive type in the JSON string but got " + data['ins1_status']);
        }
        // ensure the json data is a string
        if (data['ins2_status'] && !(typeof data['ins2_status'] === 'string' || data['ins2_status'] instanceof String)) {
            throw new Error("Expected the field `ins2_status` to be a primitive type in the JSON string but got " + data['ins2_status']);
        }
        // ensure the json data is a string
        if (data['last_billed_date'] && !(typeof data['last_billed_date'] === 'string' || data['last_billed_date'] instanceof String)) {
            throw new Error("Expected the field `last_billed_date` to be a primitive type in the JSON string but got " + data['last_billed_date']);
        }
        // ensure the json data is a string
        if (data['notes'] && !(typeof data['notes'] === 'string' || data['notes'] instanceof String)) {
            throw new Error("Expected the field `notes` to be a primitive type in the JSON string but got " + data['notes']);
        }
        // ensure the json data is a string
        if (data['primary_insurance_id_number'] && !(typeof data['primary_insurance_id_number'] === 'string' || data['primary_insurance_id_number'] instanceof String)) {
            throw new Error("Expected the field `primary_insurance_id_number` to be a primitive type in the JSON string but got " + data['primary_insurance_id_number']);
        }
        // ensure the json data is a string
        if (data['primary_insurer_name'] && !(typeof data['primary_insurer_name'] === 'string' || data['primary_insurer_name'] instanceof String)) {
            throw new Error("Expected the field `primary_insurer_name` to be a primitive type in the JSON string but got " + data['primary_insurer_name']);
        }
        // ensure the json data is a string
        if (data['primary_insurer_payer_id'] && !(typeof data['primary_insurer_payer_id'] === 'string' || data['primary_insurer_payer_id'] instanceof String)) {
            throw new Error("Expected the field `primary_insurer_payer_id` to be a primitive type in the JSON string but got " + data['primary_insurer_payer_id']);
        }
        // ensure the json data is a string
        if (data['reason'] && !(typeof data['reason'] === 'string' || data['reason'] instanceof String)) {
            throw new Error("Expected the field `reason` to be a primitive type in the JSON string but got " + data['reason']);
        }
        // ensure the json data is a string
        if (data['reminder_profile'] && !(typeof data['reminder_profile'] === 'string' || data['reminder_profile'] instanceof String)) {
            throw new Error("Expected the field `reminder_profile` to be a primitive type in the JSON string but got " + data['reminder_profile']);
        }
        if (data['reminders']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['reminders'])) {
                throw new Error("Expected the field `reminders` to be an array in the JSON data but got " + data['reminders']);
            }
            // validate the optional field `reminders` (array)
            for (const item of data['reminders']) {
                SimpleReminder.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['scheduled_time'] && !(typeof data['scheduled_time'] === 'string' || data['scheduled_time'] instanceof String)) {
            throw new Error("Expected the field `scheduled_time` to be a primitive type in the JSON string but got " + data['scheduled_time']);
        }
        // ensure the json data is a string
        if (data['secondary_insurance_id_number'] && !(typeof data['secondary_insurance_id_number'] === 'string' || data['secondary_insurance_id_number'] instanceof String)) {
            throw new Error("Expected the field `secondary_insurance_id_number` to be a primitive type in the JSON string but got " + data['secondary_insurance_id_number']);
        }
        // ensure the json data is a string
        if (data['secondary_insurer_name'] && !(typeof data['secondary_insurer_name'] === 'string' || data['secondary_insurer_name'] instanceof String)) {
            throw new Error("Expected the field `secondary_insurer_name` to be a primitive type in the JSON string but got " + data['secondary_insurer_name']);
        }
        // ensure the json data is a string
        if (data['secondary_insurer_payer_id'] && !(typeof data['secondary_insurer_payer_id'] === 'string' || data['secondary_insurer_payer_id'] instanceof String)) {
            throw new Error("Expected the field `secondary_insurer_payer_id` to be a primitive type in the JSON string but got " + data['secondary_insurer_payer_id']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        if (data['status_transitions']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['status_transitions'])) {
                throw new Error("Expected the field `status_transitions` to be an array in the JSON data but got " + data['status_transitions']);
            }
            // validate the optional field `status_transitions` (array)
            for (const item of data['status_transitions']) {
                AppointmentStatusTransition.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['supervising_provider'] && !(typeof data['supervising_provider'] === 'string' || data['supervising_provider'] instanceof String)) {
            throw new Error("Expected the field `supervising_provider` to be a primitive type in the JSON string but got " + data['supervising_provider']);
        }
        // ensure the json data is a string
        if (data['updated_at'] && !(typeof data['updated_at'] === 'string' || data['updated_at'] instanceof String)) {
            throw new Error("Expected the field `updated_at` to be a primitive type in the JSON string but got " + data['updated_at']);
        }
        // validate the optional field `vitals`
        if (data['vitals']) { // data not null
          SystemVitals.validateJSON(data['vitals']);
        }

        return true;
    }


}

Appointment.RequiredProperties = ["doctor", "exam_room", "office", "patient", "scheduled_time"];

/**
 * Bypass overlap check.
 * @member {Boolean} allow_overlapping
 */
Appointment.prototype['allow_overlapping'] = undefined;

/**
 * 
 * @member {Boolean} appt_is_break
 */
Appointment.prototype['appt_is_break'] = undefined;

/**
 * ID of base appointment of a recurrign series
 * @member {String} base_recurring_appointment
 */
Appointment.prototype['base_recurring_appointment'] = undefined;

/**
 * Billing notes of the appointment. For writing, check `/api/claim_billing_notes`
 * @member {Array.<module:model/ClaimBillingNotes1>} billing_notes
 */
Appointment.prototype['billing_notes'] = undefined;

/**
 * 
 * @member {String} billing_provider
 */
Appointment.prototype['billing_provider'] = undefined;

/**
 * Should be one of `Auto Accident Claim`, `Balance Due`, `Bill Insurance`, `Bill Secondary Insurance`, `Durable Medical Equipment Claim`, `Internal Review`, `Paid In Full`, `Settled`, `Worker's Comp Claim` or one of the custom billing status
 * @member {String} billing_status
 */
Appointment.prototype['billing_status'] = undefined;

/**
 * @member {module:model/ClinicalNote1} clinical_note
 */
Appointment.prototype['clinical_note'] = undefined;

/**
 * ID of the original appointment which this appointment cloned from. Will be null if the appointment is not cloned.
 * @member {Number} cloned_from
 */
Appointment.prototype['cloned_from'] = undefined;

/**
 * 
 * @member {String} color
 */
Appointment.prototype['color'] = undefined;

/**
 * 
 * @member {String} created_at
 */
Appointment.prototype['created_at'] = undefined;

/**
 * Custom appointment fields
 * @member {Array.<module:model/CustomAppointmentFieldValue>} custom_fields
 */
Appointment.prototype['custom_fields'] = undefined;

/**
 * Custom vitals associated with this appointment.
 * @member {Array.<module:model/CustomVitalValue>} custom_vitals
 */
Appointment.prototype['custom_vitals'] = undefined;

/**
 * Whether the appointmetn is deleted.
 * @member {Boolean} deleted_flag
 */
Appointment.prototype['deleted_flag'] = undefined;

/**
 * Doctor ID
 * @member {Number} doctor
 */
Appointment.prototype['doctor'] = undefined;

/**
 * Length of the appointment in minutes. Optional if `profile` is provided.
 * @member {Number} duration
 */
Appointment.prototype['duration'] = undefined;

/**
 * Index of the exam room that this appointment occurs in. See `/api/offices`
 * @member {Number} exam_room
 */
Appointment.prototype['exam_room'] = undefined;

/**
 * The most recent update time among appointment itself, its vitals and its custom vitals
 * @member {String} extended_updated_at
 */
Appointment.prototype['extended_updated_at'] = undefined;

/**
 * 
 * @member {String} first_billed_date
 */
Appointment.prototype['first_billed_date'] = undefined;

/**
 * 
 * @member {Array.<String>} icd10_codes
 */
Appointment.prototype['icd10_codes'] = undefined;

/**
 * 
 * @member {Array.<String>} icd9_codes
 */
Appointment.prototype['icd9_codes'] = undefined;

/**
 * Unique identifier. Usually numeric, but not always
 * @member {String} id
 */
Appointment.prototype['id'] = undefined;

/**
 * Billing status of primary insurer
 * @member {module:model/Appointment.Ins1StatusEnum} ins1_status
 */
Appointment.prototype['ins1_status'] = undefined;

/**
 * Billing status of secondary insurer
 * @member {module:model/Appointment.Ins2StatusEnum} ins2_status
 */
Appointment.prototype['ins2_status'] = undefined;

/**
 * 
 * @member {Boolean} is_virtual_base
 */
Appointment.prototype['is_virtual_base'] = undefined;

/**
 * Whether the appointment is a walk-in appointment
 * @member {Boolean} is_walk_in
 */
Appointment.prototype['is_walk_in'] = undefined;

/**
 * 
 * @member {String} last_billed_date
 */
Appointment.prototype['last_billed_date'] = undefined;

/**
 * 
 * @member {String} notes
 */
Appointment.prototype['notes'] = undefined;

/**
 * Office ID
 * @member {Number} office
 */
Appointment.prototype['office'] = undefined;

/**
 * ID of this appointment's patient. Breaks have a null patient field.
 * @member {Number} patient
 */
Appointment.prototype['patient'] = undefined;

/**
 * 
 * @member {String} primary_insurance_id_number
 */
Appointment.prototype['primary_insurance_id_number'] = undefined;

/**
 * 
 * @member {String} primary_insurer_name
 */
Appointment.prototype['primary_insurer_name'] = undefined;

/**
 * 
 * @member {String} primary_insurer_payer_id
 */
Appointment.prototype['primary_insurer_payer_id'] = undefined;

/**
 * ID of an `/api/appointment_profiles` instance. The profile sets default values for `color`, `duration`, and `reason` on creation, which can be overriden by setting these values explicitly.
 * @member {Number} profile
 */
Appointment.prototype['profile'] = undefined;

/**
 * Default to `\"\"`
 * @member {String} reason
 */
Appointment.prototype['reason'] = undefined;

/**
 * Whether the appointment is a recurring appointment or not
 * @member {Boolean} recurring_appointment
 */
Appointment.prototype['recurring_appointment'] = undefined;

/**
 * Write-only. ID of an `/api/reminder_profiles` instance. Set this to apply a reminder profile to the appointment. Cannot be applied to an appointment with reminders.
 * @member {String} reminder_profile
 */
Appointment.prototype['reminder_profile'] = undefined;

/**
 * Scheduled reminders of the appointment
 * @member {Array.<module:model/SimpleReminder>} reminders
 */
Appointment.prototype['reminders'] = undefined;

/**
 * The starting time of the appointment
 * @member {String} scheduled_time
 */
Appointment.prototype['scheduled_time'] = undefined;

/**
 * 
 * @member {String} secondary_insurance_id_number
 */
Appointment.prototype['secondary_insurance_id_number'] = undefined;

/**
 * 
 * @member {String} secondary_insurer_name
 */
Appointment.prototype['secondary_insurer_name'] = undefined;

/**
 * 
 * @member {String} secondary_insurer_payer_id
 */
Appointment.prototype['secondary_insurer_payer_id'] = undefined;

/**
 * One of ``, `Arrived`, `Checked In`, `In Room`, `Cancelled`, `Complete`, `Confirmed`, `In Session`, `No Show`, `Not Confirmed`, or `Rescheduled`. Or one of the custom statuses.
 * @member {module:model/Appointment.StatusEnum} status
 */
Appointment.prototype['status'] = undefined;

/**
 * 
 * @member {Array.<module:model/AppointmentStatusTransition>} status_transitions
 */
Appointment.prototype['status_transitions'] = undefined;

/**
 * Supervising provider of appointment if set.
 * @member {String} supervising_provider
 */
Appointment.prototype['supervising_provider'] = undefined;

/**
 * 
 * @member {String} updated_at
 */
Appointment.prototype['updated_at'] = undefined;

/**
 * @member {module:model/SystemVitals} vitals
 */
Appointment.prototype['vitals'] = undefined;





/**
 * Allowed values for the <code>ins1_status</code> property.
 * @enum {String}
 * @readonly
 */
Appointment['Ins1StatusEnum'] = {

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
     * value: "Rejected Emdeon"
     * @const
     */
    "Rejected Emdeon": "Rejected Emdeon",

    /**
     * value: "Rejected Jopari"
     * @const
     */
    "Rejected Jopari": "Rejected Jopari",

    /**
     * value: "In Process Payor"
     * @const
     */
    "In Process Payor": "In Process Payor",

    /**
     * value: "Rejected Waystar Professional"
     * @const
     */
    "Rejected Waystar Professional": "Rejected Waystar Professional",

    /**
     * value: "Rejected Waystar Institutional"
     * @const
     */
    "Rejected Waystar Institutional": "Rejected Waystar Institutional",

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
     * value: "Rejected Payor"
     * @const
     */
    "Rejected Payor": "Rejected Payor",

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
    "ERA Denied": "ERA Denied",

    /**
     * value: "HCFA Form Faxed"
     * @const
     */
    "HCFA Form Faxed": "HCFA Form Faxed"
};


/**
 * Allowed values for the <code>ins2_status</code> property.
 * @enum {String}
 * @readonly
 */
Appointment['Ins2StatusEnum'] = {

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
     * value: "Rejected Emdeon"
     * @const
     */
    "Rejected Emdeon": "Rejected Emdeon",

    /**
     * value: "Rejected Jopari"
     * @const
     */
    "Rejected Jopari": "Rejected Jopari",

    /**
     * value: "In Process Payor"
     * @const
     */
    "In Process Payor": "In Process Payor",

    /**
     * value: "Rejected Waystar Professional"
     * @const
     */
    "Rejected Waystar Professional": "Rejected Waystar Professional",

    /**
     * value: "Rejected Waystar Institutional"
     * @const
     */
    "Rejected Waystar Institutional": "Rejected Waystar Institutional",

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
     * value: "Rejected Payor"
     * @const
     */
    "Rejected Payor": "Rejected Payor",

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
    "ERA Denied": "ERA Denied",

    /**
     * value: "HCFA Form Faxed"
     * @const
     */
    "HCFA Form Faxed": "HCFA Form Faxed"
};


/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
Appointment['StatusEnum'] = {

    /**
     * value: ""
     * @const
     */
    "empty": "",

    /**
     * value: "Arrived"
     * @const
     */
    "Arrived": "Arrived",

    /**
     * value: "Checked In"
     * @const
     */
    "Checked In": "Checked In",

    /**
     * value: "Checked In Online"
     * @const
     */
    "Checked In Online": "Checked In Online",

    /**
     * value: "In Room"
     * @const
     */
    "In Room": "In Room",

    /**
     * value: "In Session"
     * @const
     */
    "In Session": "In Session",

    /**
     * value: "Complete"
     * @const
     */
    "Complete": "Complete",

    /**
     * value: "Confirmed"
     * @const
     */
    "Confirmed": "Confirmed",

    /**
     * value: "Not Confirmed"
     * @const
     */
    "Not Confirmed": "Not Confirmed",

    /**
     * value: "Rescheduled"
     * @const
     */
    "Rescheduled": "Rescheduled",

    /**
     * value: "Cancelled"
     * @const
     */
    "Cancelled": "Cancelled",

    /**
     * value: "No Show"
     * @const
     */
    "No Show": "No Show"
};



export default Appointment;

