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
 * The Coverage model module.
 * @module model/Coverage
 * @version v4 (Hunt Valley)
 */
class Coverage {
    /**
     * Constructs a new <code>Coverage</code>.
     * @alias module:model/Coverage
     */
    constructor() { 
        
        Coverage.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Coverage</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Coverage} obj Optional instance to populate.
     * @return {module:model/Coverage} The populated <code>Coverage</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Coverage();

            if (data.hasOwnProperty('appointment')) {
                obj['appointment'] = ApiClient.convertToType(data['appointment'], 'String');
            }
            if (data.hasOwnProperty('cob_level')) {
                obj['cob_level'] = ApiClient.convertToType(data['cob_level'], 'String');
            }
            if (data.hasOwnProperty('coverage_details')) {
                obj['coverage_details'] = ApiClient.convertToType(data['coverage_details'], 'String');
            }
            if (data.hasOwnProperty('coverage_subscriber')) {
                obj['coverage_subscriber'] = ApiClient.convertToType(data['coverage_subscriber'], 'String');
            }
            if (data.hasOwnProperty('eligibility')) {
                obj['eligibility'] = ApiClient.convertToType(data['eligibility'], 'String');
            }
            if (data.hasOwnProperty('patient')) {
                obj['patient'] = ApiClient.convertToType(data['patient'], 'String');
            }
            if (data.hasOwnProperty('payer_name')) {
                obj['payer_name'] = ApiClient.convertToType(data['payer_name'], 'String');
            }
            if (data.hasOwnProperty('query_date')) {
                obj['query_date'] = ApiClient.convertToType(data['query_date'], 'String');
            }
            if (data.hasOwnProperty('request_service_type')) {
                obj['request_service_type'] = ApiClient.convertToType(data['request_service_type'], 'String');
            }
            if (data.hasOwnProperty('service_type_description')) {
                obj['service_type_description'] = ApiClient.convertToType(data['service_type_description'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Coverage</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Coverage</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['appointment'] && !(typeof data['appointment'] === 'string' || data['appointment'] instanceof String)) {
            throw new Error("Expected the field `appointment` to be a primitive type in the JSON string but got " + data['appointment']);
        }
        // ensure the json data is a string
        if (data['cob_level'] && !(typeof data['cob_level'] === 'string' || data['cob_level'] instanceof String)) {
            throw new Error("Expected the field `cob_level` to be a primitive type in the JSON string but got " + data['cob_level']);
        }
        // ensure the json data is a string
        if (data['coverage_details'] && !(typeof data['coverage_details'] === 'string' || data['coverage_details'] instanceof String)) {
            throw new Error("Expected the field `coverage_details` to be a primitive type in the JSON string but got " + data['coverage_details']);
        }
        // ensure the json data is a string
        if (data['coverage_subscriber'] && !(typeof data['coverage_subscriber'] === 'string' || data['coverage_subscriber'] instanceof String)) {
            throw new Error("Expected the field `coverage_subscriber` to be a primitive type in the JSON string but got " + data['coverage_subscriber']);
        }
        // ensure the json data is a string
        if (data['eligibility'] && !(typeof data['eligibility'] === 'string' || data['eligibility'] instanceof String)) {
            throw new Error("Expected the field `eligibility` to be a primitive type in the JSON string but got " + data['eligibility']);
        }
        // ensure the json data is a string
        if (data['patient'] && !(typeof data['patient'] === 'string' || data['patient'] instanceof String)) {
            throw new Error("Expected the field `patient` to be a primitive type in the JSON string but got " + data['patient']);
        }
        // ensure the json data is a string
        if (data['payer_name'] && !(typeof data['payer_name'] === 'string' || data['payer_name'] instanceof String)) {
            throw new Error("Expected the field `payer_name` to be a primitive type in the JSON string but got " + data['payer_name']);
        }
        // ensure the json data is a string
        if (data['query_date'] && !(typeof data['query_date'] === 'string' || data['query_date'] instanceof String)) {
            throw new Error("Expected the field `query_date` to be a primitive type in the JSON string but got " + data['query_date']);
        }
        // ensure the json data is a string
        if (data['request_service_type'] && !(typeof data['request_service_type'] === 'string' || data['request_service_type'] instanceof String)) {
            throw new Error("Expected the field `request_service_type` to be a primitive type in the JSON string but got " + data['request_service_type']);
        }
        // ensure the json data is a string
        if (data['service_type_description'] && !(typeof data['service_type_description'] === 'string' || data['service_type_description'] instanceof String)) {
            throw new Error("Expected the field `service_type_description` to be a primitive type in the JSON string but got " + data['service_type_description']);
        }

        return true;
    }


}



/**
 * 
 * @member {String} appointment
 */
Coverage.prototype['appointment'] = undefined;

/**
 * The level of insurance the eligibility check was run on. Can be one of the following: `Primary Insurance` or `Secondary Insurance`
 * @member {String} cob_level
 */
Coverage.prototype['cob_level'] = undefined;

/**
 * A variable size object containing the details of the eligibility check, if returned by the clearinghouse that ran the eligibility check
 * @member {String} coverage_details
 */
Coverage.prototype['coverage_details'] = undefined;

/**
 * A variable size object containing subscriber information, if returned by the clearinghouse that ran the eligibility check
 * @member {String} coverage_subscriber
 */
Coverage.prototype['coverage_subscriber'] = undefined;

/**
 *  Value | Description --- | ---- `'1'` | Active Coverage `'2'` | Active - Full Risk Capitation `'3'` | Active - Services Capitated `'4'` | Active - Services Capitated to Primary Care Physician `'5'` | Active - Pending Investigation `'6'` | Inactive `'7'` | Inactive - Pending Eligibility Update `'8'` | Inactive - Pending Investigation `'A'` | Co-Insurance `'B'` | Co-Payment `'C'` | Deductible `'CB'` | Coverage Basis `'D'` | Benefit Description `'E'` | Exclusions `'F'` | Limitations `'G'` | Out of Pocket (Stop Loss) `'H'` | Unlimited `'I'` | Non-Covered `'J'` | Cost Containment `'K'` | Reserve `'L'` | Primary Care Provider `'M'` | Pre-existing Condition `'MC'` | Managed Care Coordinator `'N'` | Services Restricted to Following Provider `'O'` | Not Deemed a Medical Necessity `'P'` | Benefit Disclaimer `'Q'` | Second Surgical Opinion Required `'R'` | Other or Additional Payor `'S'` | Prior Year(s) History `'T'` | Card(s) Reported Lost/Stolen `'U'` | Contact Following Entity for Eligibility or Benefit Information `'V'` | Cannot Process `'W'` | Other Source of Data `'X'` | Health Care Facility `'Y'` | Spend Down 
 * @member {String} eligibility
 */
Coverage.prototype['eligibility'] = undefined;

/**
 * 
 * @member {String} patient
 */
Coverage.prototype['patient'] = undefined;

/**
 * The name of the payer as returned by the clearinghouse that ran the eligibility check
 * @member {String} payer_name
 */
Coverage.prototype['payer_name'] = undefined;

/**
 * The time at which the request was made
 * @member {String} query_date
 */
Coverage.prototype['query_date'] = undefined;

/**
 *  Value | Description --- | ---- `'1'` | Medical Care `'2'` | Surgical `'3'` | Consultation `'4'` | Diagnostic X-Ray `'5'` | Diagnostic Lab `'6'` | Radiation Therapy `'7'` | Anesthesia `'8'` | Surgical Assistance `'9'` | Other Medical `'10'` | Blood Charges `'11'` | Used Durable Medical Equipment `'12'` | Durable Medical Equipment Purchase `'13'` | Ambulatory Service Center Facility `'14'` | Renal Supplies in the Home `'15'` | Alternate Method Dialysis `'16'` | Chronic Renal Disease (CRD) Equipment `'17'` | Pre-Admission Testing `'18'` | Durable Medical Equipment Rental `'19'` | Pneumonia Vaccine `'20'` | Second Surgical Opinion `'21'` | Third Surgical Opinion `'22'` | Social Work `'23'` | Diagnostic Dental `'24'` | Periodontics `'25'` | Restorative `'26'` | Endodontics `'27'` | Maxillofacial Prosthetics `'28'` | Adjunctive Dental Services `'30'` | Health Benefit Plan Coverage `'32'` | Plan Waiting Period `'33'` | Chiropractic `'34'` | Chiropractic Office Visits `'35'` | Dental Care `'36'` | Dental Crowns `'37'` | Dental Accident `'38'` | Orthodontics `'39'` | Prosthodontics `'40'` | Oral Surgery `'41'` | Routine (Preventive) Dental `'42'` | Home Health Care `'43'` | Home Health Prescriptions `'44'` | Home Health Visits `'45'` | Hospice `'46'` | Respite Care `'47'` | Hospital `'48'` | Hospital - Inpatient `'49'` | Hospital - Room and Board `'50'` | Hospital - Outpatient `'51'` | Hospital - Emergency Accident `'52'` | Hospital - Emergency Medical `'53'` | Hospital - Ambulatory Surgical `'54'` | Long Term Care `'55'` | Major Medical `'56'` | Medically Related Transportation `'57'` | Air Transportation `'58'` | Cabulance `'59'` | Licensed Ambulance `'60'` | General Benefits `'61'` | In-vitro Fertilization `'62'` | MRI/CAT Scan `'63'` | Donor Procedures `'64'` | Acupuncture `'65'` | Newborn Care `'66'` | Pathology `'67'` | Smoking Cessation `'68'` | Well Baby Care `'69'` | Maternity `'70'` | Transplants `'71'` | Audiology Exam `'72'` | Inhalation Therapy `'73'` | Diagnostic Medical `'74'` | Private Duty Nursing `'75'` | Prosthetic Device `'76'` | Dialysis `'77'` | Otological Exam `'78'` | Chemotherapy `'79'` | Allergy Testing `'80'` | Immunizations `'81'` | Routine Physical `'82'` | Family Planning `'83'` | Infertility `'84'` | Abortion `'85'` | AIDS `'86'` | Emergency Services `'87'` | Cancer `'88'` | Pharmacy `'89'` | Free Standing Prescription Drug `'90'` | Mail Order Prescription Drug `'91'` | Brand Name Prescription Drug `'92'` | Generic Prescription Drug `'93'` | Podiatry `'94'` | Podiatry - Office Visits `'95'` | Podiatry - Nursing Home Visits `'96'` | Professional (Physician) `'97'` | Anesthesiologist `'98'` | Professional (Physician) Visit - Office `'99'` | Professional (Physician) Visit - Inpatient `'A0'` | Professional (Physician) Visit - Outpatient `'A1'` | Professional (Physician) Visit - Nursing Home `'A2'` | Professional (Physician) Visit - Skilled Nursing Facility `'A3'` | Professional (Physician) Visit - Home `'A4'` | Psychiatric `'A5'` | Psychiatric - Room and Board `'A6'` | Psychotherapy `'A7'` | Psychiatric - Inpatient `'A8'` | Psychiatric - Outpatient `'A9'` | Rehabilitation `'AA'` | Rehabilitation - Room and Board `'AB'` | Rehabilitation - Inpatient `'AC'` | Rehabilitation - Outpatient `'AD'` | Occupational Therapy `'AE'` | Physical Medicine `'AF'` | Speech Therapy `'AG'` | Skilled Nursing Care `'AH'` | Skilled Nursing Care - Room and Board `'AI'` | Substance Abuse `'AJ'` | Alcoholism `'AK'` | Drug Addiction `'AL'` | Vision (Optometry) `'AM'` | Frames `'AN'` | Routine Exam `'AO'` | Lenses `'AQ'` | Nonmedically Necessary Physical `'AR'` | Experimental Drug Therapy `'B1'` | Burn Care `'B2'` | Brand Name Prescription Drug - Formulary `'B3'` | Brand Name Prescription Drug - Non-Formulary `'BA'` | Independent Medical Evaluation `'BB'` | Partial Hospitalization (Psychiatric) `'BC'` | Day Care (Psychiatric) `'BD'` | Cognitive Therapy `'BE'` | Massage Therapy `'BF'` | Pulmonary Rehabilitation `'BG'` | Cardiac Rehabilitation `'BH'` | Pediatric `'BI'` | Nursery `'BJ'` | Skin `'BK'` | Orthopedic `'BL'` | Cardiac `'BM'` | Lymphatic `'BN'` | Gastrointestinal `'BP'` | Endocrine `'BQ'` | Neurology `'BR'` | Eye `'BS'` | Invasive Procedures `'BT'` | Gynecological `'BU'` | Obstetrical `'BV'` | Obstetrical/Gynecological `'BW'` | Mail Order Prescription Drug: Brand Name `'BX'` | Mail Order Prescription Drug: Generic `'BY'` | Physician Visit - Office: Sick `'BZ'` | Physician Visit - Office: Well `'C1'` | Coronary Care `'CA'` | Private Duty Nursing - Inpatient `'CB'` | Private Duty Nursing - Home `'CC'` | Surgical Benefits - Professional (Physician) `'CD'` | Surgical Benefits - Facility `'CE'` | Mental Health Provider - Inpatient `'CF'` | Mental Health Provider - Outpatient `'CG'` | Mental Health Facility - Inpatient `'CH'` | Mental Health Facility - Outpatient `'CI'` | Substance Abuse Facility - Inpatient `'CJ'` | Substance Abuse Facility - Outpatient `'CK'` | Screening X-ray `'CL'` | Screening laboratory `'CM'` | Mammogram, High Risk Patient `'CN'` | Mammogram, Low Risk Patient `'CO'` | Flu Vaccination `'CP'` | Eyewear and Eyewear Accessories `'CQ'` | Case Management `'DG'` | Dermatology `'DM'` | Durable Medical Equipment `'DS'` | Diabetic Supplies `'GF'` | Generic Prescription Drug - Formulary `'GN'` | Generic Prescription Drug - Non-Formulary `'GY'` | Allergy `'IC'` | Intensive Care `'MH'` | Mental Health `'NI'` | Neonatal Intensive Care `'ON'` | Oncology `'PT'` | Physical Therapy `'PU'` | Pulmonary `'RN'` | Renal `'RT'` | Residential Psychiatric Treatment `'TC'` | Transitional Care `'TN'` | Transitional Nursery Care `'UC'` | Urgent Care 
 * @member {module:model/Coverage.RequestServiceTypeEnum} request_service_type
 */
Coverage.prototype['request_service_type'] = undefined;

/**
 * 
 * @member {String} service_type_description
 */
Coverage.prototype['service_type_description'] = undefined;





/**
 * Allowed values for the <code>request_service_type</code> property.
 * @enum {String}
 * @readonly
 */
Coverage['RequestServiceTypeEnum'] = {

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
     * value: "17"
     * @const
     */
    "17": "17",

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
     * value: "25"
     * @const
     */
    "25": "25",

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
     * value: "28"
     * @const
     */
    "28": "28",

    /**
     * value: "30"
     * @const
     */
    "30": "30",

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
     * value: "36"
     * @const
     */
    "36": "36",

    /**
     * value: "37"
     * @const
     */
    "37": "37",

    /**
     * value: "38"
     * @const
     */
    "38": "38",

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
     * value: "41"
     * @const
     */
    "41": "41",

    /**
     * value: "42"
     * @const
     */
    "42": "42",

    /**
     * value: "43"
     * @const
     */
    "43": "43",

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
     * value: "46"
     * @const
     */
    "46": "46",

    /**
     * value: "47"
     * @const
     */
    "47": "47",

    /**
     * value: "48"
     * @const
     */
    "48": "48",

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
     * value: "52"
     * @const
     */
    "52": "52",

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
     * value: "57"
     * @const
     */
    "57": "57",

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
     * value: "62"
     * @const
     */
    "62": "62",

    /**
     * value: "63"
     * @const
     */
    "63": "63",

    /**
     * value: "64"
     * @const
     */
    "64": "64",

    /**
     * value: "65"
     * @const
     */
    "65": "65",

    /**
     * value: "66"
     * @const
     */
    "66": "66",

    /**
     * value: "67"
     * @const
     */
    "67": "67",

    /**
     * value: "68"
     * @const
     */
    "68": "68",

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
     * value: "71"
     * @const
     */
    "71": "71",

    /**
     * value: "72"
     * @const
     */
    "72": "72",

    /**
     * value: "73"
     * @const
     */
    "73": "73",

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
     * value: "77"
     * @const
     */
    "77": "77",

    /**
     * value: "78"
     * @const
     */
    "78": "78",

    /**
     * value: "79"
     * @const
     */
    "79": "79",

    /**
     * value: "80"
     * @const
     */
    "80": "80",

    /**
     * value: "81"
     * @const
     */
    "81": "81",

    /**
     * value: "82"
     * @const
     */
    "82": "82",

    /**
     * value: "83"
     * @const
     */
    "83": "83",

    /**
     * value: "84"
     * @const
     */
    "84": "84",

    /**
     * value: "85"
     * @const
     */
    "85": "85",

    /**
     * value: "86"
     * @const
     */
    "86": "86",

    /**
     * value: "87"
     * @const
     */
    "87": "87",

    /**
     * value: "88"
     * @const
     */
    "88": "88",

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
     * value: "92"
     * @const
     */
    "92": "92",

    /**
     * value: "93"
     * @const
     */
    "93": "93",

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
     * value: "98"
     * @const
     */
    "98": "98",

    /**
     * value: "99"
     * @const
     */
    "99": "99",

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
     * value: "A2"
     * @const
     */
    "A2": "A2",

    /**
     * value: "A3"
     * @const
     */
    "A3": "A3",

    /**
     * value: "A4"
     * @const
     */
    "A4": "A4",

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
     * value: "A9"
     * @const
     */
    "A9": "A9",

    /**
     * value: "AA"
     * @const
     */
    "AA": "AA",

    /**
     * value: "AB"
     * @const
     */
    "AB": "AB",

    /**
     * value: "AC"
     * @const
     */
    "AC": "AC",

    /**
     * value: "AD"
     * @const
     */
    "AD": "AD",

    /**
     * value: "AE"
     * @const
     */
    "AE": "AE",

    /**
     * value: "AF"
     * @const
     */
    "AF": "AF",

    /**
     * value: "AG"
     * @const
     */
    "AG": "AG",

    /**
     * value: "AH"
     * @const
     */
    "AH": "AH",

    /**
     * value: "AI"
     * @const
     */
    "AI": "AI",

    /**
     * value: "AJ"
     * @const
     */
    "AJ": "AJ",

    /**
     * value: "AK"
     * @const
     */
    "AK": "AK",

    /**
     * value: "AL"
     * @const
     */
    "AL": "AL",

    /**
     * value: "AM"
     * @const
     */
    "AM": "AM",

    /**
     * value: "AN"
     * @const
     */
    "AN": "AN",

    /**
     * value: "AO"
     * @const
     */
    "AO": "AO",

    /**
     * value: "AQ"
     * @const
     */
    "AQ": "AQ",

    /**
     * value: "AR"
     * @const
     */
    "AR": "AR",

    /**
     * value: "B1"
     * @const
     */
    "B1": "B1",

    /**
     * value: "B2"
     * @const
     */
    "B2": "B2",

    /**
     * value: "B3"
     * @const
     */
    "B3": "B3",

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
     * value: "BC"
     * @const
     */
    "BC": "BC",

    /**
     * value: "BD"
     * @const
     */
    "BD": "BD",

    /**
     * value: "BE"
     * @const
     */
    "BE": "BE",

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
     * value: "BH"
     * @const
     */
    "BH": "BH",

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
     * value: "BK"
     * @const
     */
    "BK": "BK",

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
     * value: "BP"
     * @const
     */
    "BP": "BP",

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
     * value: "BT"
     * @const
     */
    "BT": "BT",

    /**
     * value: "BU"
     * @const
     */
    "BU": "BU",

    /**
     * value: "BV"
     * @const
     */
    "BV": "BV",

    /**
     * value: "BW"
     * @const
     */
    "BW": "BW",

    /**
     * value: "BX"
     * @const
     */
    "BX": "BX",

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
     * value: "C1"
     * @const
     */
    "C1": "C1",

    /**
     * value: "CA"
     * @const
     */
    "CA": "CA",

    /**
     * value: "CB"
     * @const
     */
    "CB": "CB",

    /**
     * value: "CC"
     * @const
     */
    "CC": "CC",

    /**
     * value: "CD"
     * @const
     */
    "CD": "CD",

    /**
     * value: "CE"
     * @const
     */
    "CE": "CE",

    /**
     * value: "CF"
     * @const
     */
    "CF": "CF",

    /**
     * value: "CG"
     * @const
     */
    "CG": "CG",

    /**
     * value: "CH"
     * @const
     */
    "CH": "CH",

    /**
     * value: "CI"
     * @const
     */
    "CI": "CI",

    /**
     * value: "CJ"
     * @const
     */
    "CJ": "CJ",

    /**
     * value: "CK"
     * @const
     */
    "CK": "CK",

    /**
     * value: "CL"
     * @const
     */
    "CL": "CL",

    /**
     * value: "CM"
     * @const
     */
    "CM": "CM",

    /**
     * value: "CN"
     * @const
     */
    "CN": "CN",

    /**
     * value: "CO"
     * @const
     */
    "CO": "CO",

    /**
     * value: "CP"
     * @const
     */
    "CP": "CP",

    /**
     * value: "CQ"
     * @const
     */
    "CQ": "CQ",

    /**
     * value: "DG"
     * @const
     */
    "DG": "DG",

    /**
     * value: "DM"
     * @const
     */
    "DM": "DM",

    /**
     * value: "DS"
     * @const
     */
    "DS": "DS",

    /**
     * value: "GF"
     * @const
     */
    "GF": "GF",

    /**
     * value: "GN"
     * @const
     */
    "GN": "GN",

    /**
     * value: "GY"
     * @const
     */
    "GY": "GY",

    /**
     * value: "IC"
     * @const
     */
    "IC": "IC",

    /**
     * value: "MH"
     * @const
     */
    "MH": "MH",

    /**
     * value: "NI"
     * @const
     */
    "NI": "NI",

    /**
     * value: "true"
     * @const
     */
    "true": "true",

    /**
     * value: "PT"
     * @const
     */
    "PT": "PT",

    /**
     * value: "PU"
     * @const
     */
    "PU": "PU",

    /**
     * value: "RN"
     * @const
     */
    "RN": "RN",

    /**
     * value: "RT"
     * @const
     */
    "RT": "RT",

    /**
     * value: "TC"
     * @const
     */
    "TC": "TC",

    /**
     * value: "TN"
     * @const
     */
    "TN": "TN",

    /**
     * value: "UC"
     * @const
     */
    "UC": "UC"
};



export default Coverage;

