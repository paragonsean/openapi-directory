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
 * The Patient1 model module.
 * @module model/Patient1
 * @version v4 (Hunt Valley)
 */
class Patient1 {
    /**
     * Constructs a new <code>Patient1</code>.
     * 
     * @alias module:model/Patient1
     */
    constructor() { 
        
        Patient1.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Patient1</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Patient1} obj Optional instance to populate.
     * @return {module:model/Patient1} The populated <code>Patient1</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Patient1();

            if (data.hasOwnProperty('address')) {
                obj['address'] = ApiClient.convertToType(data['address'], 'String');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('fax')) {
                obj['fax'] = ApiClient.convertToType(data['fax'], 'String');
            }
            if (data.hasOwnProperty('first_name')) {
                obj['first_name'] = ApiClient.convertToType(data['first_name'], 'String');
            }
            if (data.hasOwnProperty('last_name')) {
                obj['last_name'] = ApiClient.convertToType(data['last_name'], 'String');
            }
            if (data.hasOwnProperty('middle_name')) {
                obj['middle_name'] = ApiClient.convertToType(data['middle_name'], 'String');
            }
            if (data.hasOwnProperty('npi')) {
                obj['npi'] = ApiClient.convertToType(data['npi'], 'String');
            }
            if (data.hasOwnProperty('phone')) {
                obj['phone'] = ApiClient.convertToType(data['phone'], 'String');
            }
            if (data.hasOwnProperty('provider_number')) {
                obj['provider_number'] = ApiClient.convertToType(data['provider_number'], 'String');
            }
            if (data.hasOwnProperty('provider_qualifier')) {
                obj['provider_qualifier'] = ApiClient.convertToType(data['provider_qualifier'], 'String');
            }
            if (data.hasOwnProperty('specialty')) {
                obj['specialty'] = ApiClient.convertToType(data['specialty'], 'String');
            }
            if (data.hasOwnProperty('suffix')) {
                obj['suffix'] = ApiClient.convertToType(data['suffix'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Patient1</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Patient1</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['address'] && !(typeof data['address'] === 'string' || data['address'] instanceof String)) {
            throw new Error("Expected the field `address` to be a primitive type in the JSON string but got " + data['address']);
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['fax'] && !(typeof data['fax'] === 'string' || data['fax'] instanceof String)) {
            throw new Error("Expected the field `fax` to be a primitive type in the JSON string but got " + data['fax']);
        }
        // ensure the json data is a string
        if (data['first_name'] && !(typeof data['first_name'] === 'string' || data['first_name'] instanceof String)) {
            throw new Error("Expected the field `first_name` to be a primitive type in the JSON string but got " + data['first_name']);
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
        if (data['npi'] && !(typeof data['npi'] === 'string' || data['npi'] instanceof String)) {
            throw new Error("Expected the field `npi` to be a primitive type in the JSON string but got " + data['npi']);
        }
        // ensure the json data is a string
        if (data['phone'] && !(typeof data['phone'] === 'string' || data['phone'] instanceof String)) {
            throw new Error("Expected the field `phone` to be a primitive type in the JSON string but got " + data['phone']);
        }
        // ensure the json data is a string
        if (data['provider_number'] && !(typeof data['provider_number'] === 'string' || data['provider_number'] instanceof String)) {
            throw new Error("Expected the field `provider_number` to be a primitive type in the JSON string but got " + data['provider_number']);
        }
        // ensure the json data is a string
        if (data['provider_qualifier'] && !(typeof data['provider_qualifier'] === 'string' || data['provider_qualifier'] instanceof String)) {
            throw new Error("Expected the field `provider_qualifier` to be a primitive type in the JSON string but got " + data['provider_qualifier']);
        }
        // ensure the json data is a string
        if (data['specialty'] && !(typeof data['specialty'] === 'string' || data['specialty'] instanceof String)) {
            throw new Error("Expected the field `specialty` to be a primitive type in the JSON string but got " + data['specialty']);
        }
        // ensure the json data is a string
        if (data['suffix'] && !(typeof data['suffix'] === 'string' || data['suffix'] instanceof String)) {
            throw new Error("Expected the field `suffix` to be a primitive type in the JSON string but got " + data['suffix']);
        }

        return true;
    }


}



/**
 * 
 * @member {String} address
 */
Patient1.prototype['address'] = undefined;

/**
 * 
 * @member {String} email
 */
Patient1.prototype['email'] = undefined;

/**
 * Should follow format \"xxx-xx-xxxx\"
 * @member {String} fax
 */
Patient1.prototype['fax'] = undefined;

/**
 * 
 * @member {String} first_name
 */
Patient1.prototype['first_name'] = undefined;

/**
 * 
 * @member {String} last_name
 */
Patient1.prototype['last_name'] = undefined;

/**
 * 
 * @member {String} middle_name
 */
Patient1.prototype['middle_name'] = undefined;

/**
 * 
 * @member {String} npi
 */
Patient1.prototype['npi'] = undefined;

/**
 * Should follow format \"xxx-xx-xxxx\"
 * @member {String} phone
 */
Patient1.prototype['phone'] = undefined;

/**
 * 
 * @member {String} provider_number
 */
Patient1.prototype['provider_number'] = undefined;

/**
 * Can be one of following, `''`, `'0B'`(State License #), `'1G'`(Provider UPIN #), `'G2'`(Provider Commercial #)
 * @member {module:model/Patient1.ProviderQualifierEnum} provider_qualifier
 */
Patient1.prototype['provider_qualifier'] = undefined;

/**
 * Can be one of following, `''`, `'Acupuncture'`, `'Advanced Practice Midwife'`, `'Aesthetic Medicine'`, `'Aesthetician'`, `'Allergist/Immunologist'`, `'Anesthesiologist'`, `'Cardiac Electrophysiologist'`, `'Cardiologist'`, `'Cardiothoracic Surgeon'`, `'Child/Adolescent Psychiatry'`, `'Chiropractor'`, `'Clinical Social Worker'`, `'Colorectal Surgeon'`, `'Correactology'`, `'Cosmetic Medicine'`, `'Counselor Mental Health'`, `'Counselor Professional'`, `'Counselor'`, `'Dentist'`, `'Diabetology'`, `'Dermatologist'`, `'Diagnostic Medical Sonographer'`, `'Dietitian, Registered'`, `'Ear-Nose-Throat Specialist (ENT)'`, `'Emergency Medicine Physician'`, `'Endocrinologist'`, `'Endodontist'`, `'Epidemiologist'`, `'Family Practitioner'`, `'Gastroenterologist'`, `'General Practice'`, `'General Surgeon'`, `'Geneticist'`, `'Geriatrician'`, `'Gerontologist'`, `'Gynecologist (no OB)'`, `'Gynegologic Oncologist'`, `'Hand Surgeon'`, `'Hematologist'`, `'Home Care'`, `'Hospice'`, `'Hospitalist'`, `'Infectious Disease Specialist'`, `'Integrative and Functional Medicine'`, `'Integrative Medicine'`, `'Internist'`, `'Interventional Radiology'`, `'Laboratory Medicine Specialist'`, `'Laser Surgery'`, `'Massage Therapist'`, `'Naturopathic Physician'`, `'Neonatologist'`, `'Nephrologist'`, `'Neurologist'`, `'Neuropsychology'`, `'Neurosurgeon'`, `'Not Actively Practicing'`, `'Nuclear Medicine Specialist'`, `'Nurse Practitioner'`, `'Nursing'`, `'Nutritionist'`, `'Obstetrician/Gynecologist'`, `'Occupational Medicine'`, `'Occupational Therapist'`, `'Oncologist'`, `'Ophthalmologist'`, `'Optometrist'`, `'Oral Surgeon'`, `'Orofacial Pain'`, `'Orthodontist'`, `'Orthopedic Surgeon'`, `'Orthotist'`, `'Other'`, `'Pain Management Specialist'`, `'Pathologist'`, `'Pediatric Dentist'`, `'Pediatric Gastroenterology'`, `'Pediatric Surgeon'`, `'Pediatrician'`, `'Perinatologist'`, `'Periodontist'`, `'Physical Medicine and Rehab Specialist'`, `'Physical Therapist'`, `'Physician Assistant'`, `'Plastic Surgeon'`, `'Podiatrist'`, `'Preventive-Aging Medicine'`, `'Preventive Medicine/Occupational-Environmental Medicine'`, `'Primary Care Physician'`, `'Prosthetist'`, `'Prosthodontist'`, `'Psychiatrist'`, `'Psychologist'`, `'Public Health Professional'`, `'Pulmonologist'`, `'Radiation Oncologist'`, `'Radiologist'`, `'Registered Nurse'`, `'Religious Nonmedical Practitioner'`, `'Reproductive Endocrinologist'`, `'Reproductive Medicine'`, `'Rheumatologist'`, `'Sleep Medicine'`, `'Speech-Language Pathologist'`, `'Sports Medicine Specialist'`, `'Urologist'`, `'Urgent Care'`, `'Vascular Surgeon'`
 * @member {module:model/Patient1.SpecialtyEnum} specialty
 */
Patient1.prototype['specialty'] = undefined;

/**
 * 
 * @member {String} suffix
 */
Patient1.prototype['suffix'] = undefined;





/**
 * Allowed values for the <code>provider_qualifier</code> property.
 * @enum {String}
 * @readonly
 */
Patient1['ProviderQualifierEnum'] = {

    /**
     * value: ""
     * @const
     */
    "empty": "",

    /**
     * value: "0B"
     * @const
     */
    "0B": "0B",

    /**
     * value: "1G"
     * @const
     */
    "1G": "1G",

    /**
     * value: "G2"
     * @const
     */
    "G2": "G2"
};


/**
 * Allowed values for the <code>specialty</code> property.
 * @enum {String}
 * @readonly
 */
Patient1['SpecialtyEnum'] = {

    /**
     * value: ""
     * @const
     */
    "empty": "",

    /**
     * value: "Acupuncture"
     * @const
     */
    "Acupuncture": "Acupuncture",

    /**
     * value: "Advanced Practice Midwife"
     * @const
     */
    "Advanced Practice Midwife": "Advanced Practice Midwife",

    /**
     * value: "Aesthetic Medicine"
     * @const
     */
    "Aesthetic Medicine": "Aesthetic Medicine",

    /**
     * value: "Aesthetician"
     * @const
     */
    "Aesthetician": "Aesthetician",

    /**
     * value: "Allergist/Immunologist"
     * @const
     */
    "Allergist/Immunologist": "Allergist/Immunologist",

    /**
     * value: "Anesthesiologist"
     * @const
     */
    "Anesthesiologist": "Anesthesiologist",

    /**
     * value: "Cardiac Electrophysiologist"
     * @const
     */
    "Cardiac Electrophysiologist": "Cardiac Electrophysiologist",

    /**
     * value: "Cardiologist"
     * @const
     */
    "Cardiologist": "Cardiologist",

    /**
     * value: "Cardiothoracic Surgeon"
     * @const
     */
    "Cardiothoracic Surgeon": "Cardiothoracic Surgeon",

    /**
     * value: "Child/Adolescent Psychiatry"
     * @const
     */
    "Child/Adolescent Psychiatry": "Child/Adolescent Psychiatry",

    /**
     * value: "Chiropractor"
     * @const
     */
    "Chiropractor": "Chiropractor",

    /**
     * value: "Clinical Social Worker"
     * @const
     */
    "Clinical Social Worker": "Clinical Social Worker",

    /**
     * value: "Colorectal Surgeon"
     * @const
     */
    "Colorectal Surgeon": "Colorectal Surgeon",

    /**
     * value: "Correactology"
     * @const
     */
    "Correactology": "Correactology",

    /**
     * value: "Cosmetic Medicine"
     * @const
     */
    "Cosmetic Medicine": "Cosmetic Medicine",

    /**
     * value: "Counselor Mental Health"
     * @const
     */
    "Counselor Mental Health": "Counselor Mental Health",

    /**
     * value: "Counselor Professional"
     * @const
     */
    "Counselor Professional": "Counselor Professional",

    /**
     * value: "Counselor"
     * @const
     */
    "Counselor": "Counselor",

    /**
     * value: "Dentist"
     * @const
     */
    "Dentist": "Dentist",

    /**
     * value: "Diabetology"
     * @const
     */
    "Diabetology": "Diabetology",

    /**
     * value: "Dermatologist"
     * @const
     */
    "Dermatologist": "Dermatologist",

    /**
     * value: "Diagnostic Medical Sonographer"
     * @const
     */
    "Diagnostic Medical Sonographer": "Diagnostic Medical Sonographer",

    /**
     * value: "Dietitian, Registered"
     * @const
     */
    "Dietitian, Registered": "Dietitian, Registered",

    /**
     * value: "Ear-Nose-Throat Specialist (ENT)"
     * @const
     */
    "Ear-Nose-Throat Specialist (ENT)": "Ear-Nose-Throat Specialist (ENT)",

    /**
     * value: "Emergency Medicine Physician"
     * @const
     */
    "Emergency Medicine Physician": "Emergency Medicine Physician",

    /**
     * value: "Endocrinologist"
     * @const
     */
    "Endocrinologist": "Endocrinologist",

    /**
     * value: "Endodontist"
     * @const
     */
    "Endodontist": "Endodontist",

    /**
     * value: "Epidemiologist"
     * @const
     */
    "Epidemiologist": "Epidemiologist",

    /**
     * value: "Family Practitioner"
     * @const
     */
    "Family Practitioner": "Family Practitioner",

    /**
     * value: "Gastroenterologist"
     * @const
     */
    "Gastroenterologist": "Gastroenterologist",

    /**
     * value: "General Practice"
     * @const
     */
    "General Practice": "General Practice",

    /**
     * value: "General Surgeon"
     * @const
     */
    "General Surgeon": "General Surgeon",

    /**
     * value: "Geneticist"
     * @const
     */
    "Geneticist": "Geneticist",

    /**
     * value: "Geriatrician"
     * @const
     */
    "Geriatrician": "Geriatrician",

    /**
     * value: "Gerontologist"
     * @const
     */
    "Gerontologist": "Gerontologist",

    /**
     * value: "Gynecologist (no OB)"
     * @const
     */
    "Gynecologist (no OB)": "Gynecologist (no OB)",

    /**
     * value: "Gynegologic Oncologist"
     * @const
     */
    "Gynegologic Oncologist": "Gynegologic Oncologist",

    /**
     * value: "Hand Surgeon"
     * @const
     */
    "Hand Surgeon": "Hand Surgeon",

    /**
     * value: "Hematologist"
     * @const
     */
    "Hematologist": "Hematologist",

    /**
     * value: "Home Care"
     * @const
     */
    "Home Care": "Home Care",

    /**
     * value: "Hospice"
     * @const
     */
    "Hospice": "Hospice",

    /**
     * value: "Hospitalist"
     * @const
     */
    "Hospitalist": "Hospitalist",

    /**
     * value: "Infectious Disease Specialist"
     * @const
     */
    "Infectious Disease Specialist": "Infectious Disease Specialist",

    /**
     * value: "Integrative and Functional Medicine"
     * @const
     */
    "Integrative and Functional Medicine": "Integrative and Functional Medicine",

    /**
     * value: "Integrative Medicine"
     * @const
     */
    "Integrative Medicine": "Integrative Medicine",

    /**
     * value: "Internist"
     * @const
     */
    "Internist": "Internist",

    /**
     * value: "Interventional Radiology"
     * @const
     */
    "Interventional Radiology": "Interventional Radiology",

    /**
     * value: "Laboratory Medicine Specialist"
     * @const
     */
    "Laboratory Medicine Specialist": "Laboratory Medicine Specialist",

    /**
     * value: "Laser Surgery"
     * @const
     */
    "Laser Surgery": "Laser Surgery",

    /**
     * value: "Massage Therapist"
     * @const
     */
    "Massage Therapist": "Massage Therapist",

    /**
     * value: "Naturopathic Physician"
     * @const
     */
    "Naturopathic Physician": "Naturopathic Physician",

    /**
     * value: "Neonatologist"
     * @const
     */
    "Neonatologist": "Neonatologist",

    /**
     * value: "Nephrologist"
     * @const
     */
    "Nephrologist": "Nephrologist",

    /**
     * value: "Neurologist"
     * @const
     */
    "Neurologist": "Neurologist",

    /**
     * value: "Neuropsychology"
     * @const
     */
    "Neuropsychology": "Neuropsychology",

    /**
     * value: "Neurosurgeon"
     * @const
     */
    "Neurosurgeon": "Neurosurgeon",

    /**
     * value: "Not Actively Practicing"
     * @const
     */
    "Not Actively Practicing": "Not Actively Practicing",

    /**
     * value: "Nuclear Medicine Specialist"
     * @const
     */
    "Nuclear Medicine Specialist": "Nuclear Medicine Specialist",

    /**
     * value: "Nurse Practitioner"
     * @const
     */
    "Nurse Practitioner": "Nurse Practitioner",

    /**
     * value: "Nursing"
     * @const
     */
    "Nursing": "Nursing",

    /**
     * value: "Nutritionist"
     * @const
     */
    "Nutritionist": "Nutritionist",

    /**
     * value: "Obstetrician/Gynecologist"
     * @const
     */
    "Obstetrician/Gynecologist": "Obstetrician/Gynecologist",

    /**
     * value: "Occupational Medicine"
     * @const
     */
    "Occupational Medicine": "Occupational Medicine",

    /**
     * value: "Occupational Therapist"
     * @const
     */
    "Occupational Therapist": "Occupational Therapist",

    /**
     * value: "Oncologist"
     * @const
     */
    "Oncologist": "Oncologist",

    /**
     * value: "Ophthalmologist"
     * @const
     */
    "Ophthalmologist": "Ophthalmologist",

    /**
     * value: "Optometrist"
     * @const
     */
    "Optometrist": "Optometrist",

    /**
     * value: "Oral Surgeon"
     * @const
     */
    "Oral Surgeon": "Oral Surgeon",

    /**
     * value: "Orofacial Pain"
     * @const
     */
    "Orofacial Pain": "Orofacial Pain",

    /**
     * value: "Orthodontist"
     * @const
     */
    "Orthodontist": "Orthodontist",

    /**
     * value: "Orthopedic Surgeon"
     * @const
     */
    "Orthopedic Surgeon": "Orthopedic Surgeon",

    /**
     * value: "Orthotist"
     * @const
     */
    "Orthotist": "Orthotist",

    /**
     * value: "Other"
     * @const
     */
    "Other": "Other",

    /**
     * value: "Pain Management Specialist"
     * @const
     */
    "Pain Management Specialist": "Pain Management Specialist",

    /**
     * value: "Pathologist"
     * @const
     */
    "Pathologist": "Pathologist",

    /**
     * value: "Pediatric Dentist"
     * @const
     */
    "Pediatric Dentist": "Pediatric Dentist",

    /**
     * value: "Pediatric Gastroenterology"
     * @const
     */
    "Pediatric Gastroenterology": "Pediatric Gastroenterology",

    /**
     * value: "Pediatric Surgeon"
     * @const
     */
    "Pediatric Surgeon": "Pediatric Surgeon",

    /**
     * value: "Pediatrician"
     * @const
     */
    "Pediatrician": "Pediatrician",

    /**
     * value: "Perinatologist"
     * @const
     */
    "Perinatologist": "Perinatologist",

    /**
     * value: "Periodontist"
     * @const
     */
    "Periodontist": "Periodontist",

    /**
     * value: "Physical Medicine and Rehab Specialist"
     * @const
     */
    "Physical Medicine and Rehab Specialist": "Physical Medicine and Rehab Specialist",

    /**
     * value: "Physical Therapist"
     * @const
     */
    "Physical Therapist": "Physical Therapist",

    /**
     * value: "Physician Assistant"
     * @const
     */
    "Physician Assistant": "Physician Assistant",

    /**
     * value: "Plastic Surgeon"
     * @const
     */
    "Plastic Surgeon": "Plastic Surgeon",

    /**
     * value: "Podiatrist"
     * @const
     */
    "Podiatrist": "Podiatrist",

    /**
     * value: "Preventive-Aging Medicine"
     * @const
     */
    "Preventive-Aging Medicine": "Preventive-Aging Medicine",

    /**
     * value: "Preventive Medicine/Occupational-Environmental Medicine"
     * @const
     */
    "Preventive Medicine/Occupational-Environmental Medicine": "Preventive Medicine/Occupational-Environmental Medicine",

    /**
     * value: "Primary Care Physician"
     * @const
     */
    "Primary Care Physician": "Primary Care Physician",

    /**
     * value: "Prosthetist"
     * @const
     */
    "Prosthetist": "Prosthetist",

    /**
     * value: "Prosthodontist"
     * @const
     */
    "Prosthodontist": "Prosthodontist",

    /**
     * value: "Psychiatrist"
     * @const
     */
    "Psychiatrist": "Psychiatrist",

    /**
     * value: "Psychologist"
     * @const
     */
    "Psychologist": "Psychologist",

    /**
     * value: "Public Health Professional"
     * @const
     */
    "Public Health Professional": "Public Health Professional",

    /**
     * value: "Pulmonologist"
     * @const
     */
    "Pulmonologist": "Pulmonologist",

    /**
     * value: "Radiation Oncologist"
     * @const
     */
    "Radiation Oncologist": "Radiation Oncologist",

    /**
     * value: "Radiologist"
     * @const
     */
    "Radiologist": "Radiologist",

    /**
     * value: "Registered Nurse"
     * @const
     */
    "Registered Nurse": "Registered Nurse",

    /**
     * value: "Religious Nonmedical Practitioner"
     * @const
     */
    "Religious Nonmedical Practitioner": "Religious Nonmedical Practitioner",

    /**
     * value: "Reproductive Endocrinologist"
     * @const
     */
    "Reproductive Endocrinologist": "Reproductive Endocrinologist",

    /**
     * value: "Reproductive Medicine"
     * @const
     */
    "Reproductive Medicine": "Reproductive Medicine",

    /**
     * value: "Rheumatologist"
     * @const
     */
    "Rheumatologist": "Rheumatologist",

    /**
     * value: "Sleep Medicine"
     * @const
     */
    "Sleep Medicine": "Sleep Medicine",

    /**
     * value: "Speech-Language Pathologist"
     * @const
     */
    "Speech-Language Pathologist": "Speech-Language Pathologist",

    /**
     * value: "Sports Medicine Specialist"
     * @const
     */
    "Sports Medicine Specialist": "Sports Medicine Specialist",

    /**
     * value: "Urologist"
     * @const
     */
    "Urologist": "Urologist",

    /**
     * value: "Urgent Care"
     * @const
     */
    "Urgent Care": "Urgent Care",

    /**
     * value: "Vascular Surgeon"
     * @const
     */
    "Vascular Surgeon": "Vascular Surgeon"
};



export default Patient1;

