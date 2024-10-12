/**
 * 
 * This document is intended as a detailed reference for the precise behavior of the drchrono API. If this is your first time using the API, start with our <a href=\"/api-docs-old/tutorial\">tutorial</a>. If you are upgrading from a previous version, take a look at the changelog section.  # Authorization  ## Initial authorization  There are three main steps in the OAuth 2.0 authentication workflow:  1. Redirect the provider to the authorization page. 2. The provider authorizes your application and is redirected back to    your web application. 3. Your application exchanges the `authorization_code` that came with    the redirect for an `access_token` and `refresh_token`.  ### Step 1: Redirect to drchrono  The first step is redirecting your user to drchrono, typically with a button labeled \"Connect to drchrono\" or \"Login with drchrono\".  This is just a link that takes your user to the following URL:      https://drchrono.com/o/authorize/?redirect_uri=REDIRECT_URI_ENCODED&response_type=code&client_id=CLIENT_ID_ENCODED&scope=SCOPES_ENCODED  - `REDIRECT_URI_ENCODED` is the URL-encoded version of the redirect URI (as registered for your application and used in later steps). - `CLIENT_ID_ENCODED` is the URL-encoded version of your application's client ID. - `SCOPES_ENCODED` is a URL-encoded version of a space-separated list of scopes, which can be found in each endpoint or omitted to default to all scopes.  The `scope` parameter consists of an optional, space-separated list of scopes your application is requesting. If omitted, all scopes will be requested.  Scopes are of the form `BASE_SCOPE:[read|write]` where `BASE_SCOPE` is any of `user`, `calendar`, `patients`, `patients:summary`, `billing`, `clinical` and `labs`. You should request only the scopes you need. For instance, an application which sends \"Happy Birthday!\" emails to a doctor's patients on their birthdays would use the scope parameter `\"patients:summary:read\"`, while one that allows patients to schedule appointments online would need at least `\"patients:summary:read patients:summary:write calendar:read calendar:write clinical:read clinical:write\"`.  ### Step 2: Provider authorization  After logging in (if necessary), the provider will be presented with a screen with your application's name and the list of permissions you requested (via the `scope` parameter).  When they click the \"Authorize\" button, they will be redirected to your redirect URI with a `code` query parameter appended, which contains an authorization code to be used in step 3.  If they click the \"Cancel\" button, they will be redirected to your redirect URI with `error=access_denied` instead.  Note: This authorization code expires extremely quickly, so you must perform step 3 immediately, ideally before rendering the resulting page for the end user.  ### Step 3: Token exchange  The `code` obtained from step 2 is usable exactly once to obtain an access token and refresh token.  Here is an example token exchange in Python:      import datetime, pytz, requests      if 'error' in get_params:         raise ValueError('Error authorizing application: %s' % get_params[error])      response = requests.post('https://drchrono.com/o/token/', data={         'code': get_params['code'],         'grant_type': 'authorization_code',         'redirect_uri': 'http://mytestapp.com/redirect_uri',         'client_id': 'abcdefg12345',         'client_secret': 'abcdefg12345',     })     response.raise_for_status()     data = response.json()      # Save these in your database associated with the user     access_token = data['access_token']     refresh_token = data['refresh_token']     expires_timestamp = datetime.datetime.now(pytz.utc) + datetime.timedelta(seconds=data['expires_in'])  You now have all you need to make API requests authenticated as that provider. When using this access token, you'll only be able to access the data that the user has access to and that you have been granted permissions for.  ## Refreshing an access token  Access tokens only last 48 hours (given in seconds in the `'expires_in'` key in the token exchange step above), so they occasionally need to be refreshed.  It would be inconvenient to ask the user to re-authorize every time, so instead you can use the refresh token like the original authorization to obtain a new access token.  Replace the `code` parameter with `refresh_token`, change the value `grant_type` from `authorization_code` to `refresh_token`, and omit the `redirect_uri` parameter.  Example in Python:      ...     response = requests.post('https://drchrono.com/o/token/', data={         'refresh_token': get_refresh_token(),         'grant_type': 'refresh_token',         'client_id': 'abcdefg12345',         'client_secret': 'abcdefg12345',     })     ...  # Webhooks  In order to use drchrono API webhooks, you first need to have an API application on file (even if it is in Test Model). Each API webhook is associated with one API application, go to <a href=\"/api-management/\" target=\"_blank\">here</a> to set up both API applications and webhooks!  Once you registered an API application, you will see webhook section in each saved API applications. Create a webhook and register some events there and save all the changes, then you are good to go!  ## Webhooks setup  All fields under webhooks section are required.  **Callback URL** Callback URl is used to receive all hooks when subscribed events are triggered. This should be an URL under your control.  **Secret token** Secret token is used to verify webhooks, this is very important, please set something with high entropy. Also we will talk more about this later.  **Events**  Events is used to register events you want to receiver notification when they happen. Currently we support following events.  Event name | Event description ---------- | ----------------- `APPOINTMENT_CREATE` | We will deliver a hook any time an appointment is created `APPOINTMENT_MODIFY` | We will deliver a hook any time an appointment is modified `PATIENT_CREATE` | We will deliver a hook any time a patient is created `PATIENT_MODIFY` | We will deliver a hook any time a patient is modified `PATIENT_PROBLEM_CREATE` | We will deliver a hook any time a patient problem is created `PATIENT_PROBLEM_MODIFY` | We will deliver a hook any time a patient problem is modified `PATIENT_ALLERGY_CREATE` | We will deliver a hook any time a patient allergy is created `PATIENT_ALLERGY_MODIFY` | We will deliver a hook any time a patient allergy is modified `PATIENT_MEDICATION_CREATE` | We will deliver a hook any time a patient medication is created `PATIENT_MEDICATION_MODIFY` | We will deliver a hook any time a patient medication is modified `CLINICAL_NOTE_LOCK` | We will deliver a hook any time a clinical note is locked `CLINICAL_NOTE_UNLOCK` | We will deliver a hook any time a clinical note is unlocked `TASK_CREATE` | We will deliver a hook any time a task is created `TASK_MODIFY` | We will deliver a hook any time a task is modified and any time creation, modification and deletion of task notes, associated task item `TASK_DELETE` | We will deliver a hook any time a task is deleted   ## Webhooks verification  In order to make sure the callback URL in webhook is under your control, we added a verification step before we send any hooks out to you.  Verification can be done by clicking \"Verify webhook\" button in webhooks setup page. After you click the button, we will send a `GET` request to the callback URL, along with a parameter called `msg`.  Please use your webhook's secret token as hash key and SHA-256 as digest constructor, hash the `msg` value with <a href=\"https://tools.ietf.org/html/rfc2104.html\">HMAC algorithm</a>. And we expect a `200` JSON response, in JSON response body, there should be a key called `secret_token` existing, and its value should be equal to the <strong>hashed</strong> `msg`. Otherwise, verification will fail.  Here is an example webhook verification in Python:      import hashlib, hmac      def webhook_verify(request):         secret_token = hmac.new(WEBHOOK_SECRET_TOKEN, request.GET['msg'], hashlib.sha256).hexdigest()         return json_response({             'secret_token': secret_token         })  <div class=\"alert alert-warning\"> <b>Note:</b> Verification will be needed when webhook is first created and anytime callback URl is changed. </div>   ## Webhooks header and body  **Header**  Key | Value --- | ----- `X-drchrono-event` | Event that triggered this hook, could be any one event above or `PING` `X-drchrono-signature` | Secret token associated with this webhook `X-drchrono-delivery` | ID of this delivery  **Body**  Key | Value --- | ----- `receiver` | This will be an JSON representation of the webhook `object` | This will be an JSON representation of the object related to the triggered event, this would share same serializer as drchrono API  ## Webhooks ping and deliveries  Webhooks ping and deliveries will be sent as `POST` requests.  **PING**:  You can always ping your webhook to check things, by clicking the \"Ping webhook\" button in webhook setup page. And a hook with header `X-drchrono-event: PING` would be sent to the callback URL.  **Deliveries**:  You can check recent deliveries by clicking the \"deliveries\" link in webhook setup page. And you can resend a hook by clicking \"redeliver\" button after select a specific delivery.  ## Webhooks delivery mechanism  We will delivery a hook the moment a subscribed event is triggered. We will not record any response header or body you send back after you receive the hook. However we only consider the response status code. We will consider any `2xx` responses as successfully delivered. Any other responses, like `302` would be considered failing. And we will try to redeliver unsuccessfully delivered hooks 3 times, first redeliver happens at 1 hour after the initial event, second receliver happens 3 hours after the initial event, and the third redeliver happens 7 hours after the initial event. After these redeliveries, if the delivery is still unsuccessful, you have to redeliver it by hand.   ## Webhooks security  You may want to secure your webhooks to only consider requests send out from drchrono. And this is where <code>secret_token</code> is needed in request header. Try to set the <code>secret_token</code> to something with high entropy, a good example could be taking the output of <code>ruby -rsecurerandom -e 'puts SecureRandom.hex(20)'</code>. After this, you might want to verify all request headers you received on your server with this token.   # iframe integration  Some API apps provide additional functionality for interacting with patient data not offered by drchrono, and can benefit by being incorporated into drchrono's patient information page via iframe.  We have created a simple API to make this possible.  To make an existing API application accessible via an iframe on the patient page, you need to update either \"Patient iframe\" or \"Clinical note iframe\" section in API management page, to make the iframe to appear on (either the patient page or the clinical note page), with the URL that the iframe will use for each page, and the height it should have. The application will be reviewed before it is approved to ensure that it is functional and secure.  ## Register a Doctor  iframe applications will appear as choices on the left-hand menu of the patient page for doctors registered with your application.  To register a doctor with your application, make a `POST` request to the `/api/iframe_integration` endpoint using the access token for the corresponding doctor. This endpoint does not expect any payload.  To disable your iframe application for a doctor, make a `DELETE` request to the same endpoint.  ## Populating the iframe  There are two places where the iframe can be displayed, either within the patient detail page or the clinical note page, shown below respectively:  <img src=\"{% asset 'public/images/iframe_patient_page.png' %}\" alt=\"Iframe on the patient page\"/>  <img src=\"{% asset 'public/images/iframe_clinical_note.png' %}\" alt=\"Iframe on the clinical note page\"/>  When requesting approval for your iframe app, you must specify a URL for one or both of these pages which will serve as the base URL for your IFrame contents. When a doctor views your iframe, the source URL will have various query parameters appended to it, for example for the patient page the `src` parameter of the IFrame will be:  ``` <iframe_url>?doctor_id=<doctor_id>&patient_id=<patient_id>&practice_id=<practice_id>&iat=<iat>&jwt=<jwt> ```  The `jwt` parameter is crucial if your application transfers any sort of PHI and does not implement its own login system.  It encapsulates the other parameters in a [JSON web token (JWT)](http://jwt.io) and signs them using SHA-256 HMAC with your `client_secret` as the key.  This verifies that the iframe is being loaded within one of drchrono's pages by an authorized user.  In production, you should validate the JWT using an approved library (which are listed on the [official site](http://jwt.io)), and only use the parameters extracted from the JWT.  Using Python and Django, this might look like:      import jwt      CLIENT_SECRET = <client_secret>     MAX_TIME_DRIFT_SECONDS = 60      def validate_parameters(request):         token = request.GET['jwt']          return jwt.decode(token, CLIENT_SECRET, algorithms=['HS256'], leeway=MAX_TIME_DRIFT_SECONDS)  Modern browsers' same-origin policy means that data cannot be passed between your application and drchrono's page through the iframe.  Therefore, interaction must happen through the API, using information provided in JWT.  # Versions and deprecation  ## Stability Policy  Changes to this API version will be limited to adding endpoints, or adding fields to existing endpoints, or adding optional query parameters. Any new fields which are not read-only will be optional.  ## Deprecation Policy  The drchrono API is versioned. Versions can be in the following states:  * **Active:** This is our latest and greatest version of the API. It is actively supported by our API team and is improved upon with new features, bug fixes and optimizations that do not break backwards compatibility.  * **Deprecated:** A deprecated API version is considered second best--having been surpassed by our active API version. An API version remains in this state for one year, after which time it falls to the not supported state. A deprecated API version is passively supported; while it won't be removed until becoming unsupported, it may not receive new features but will likely be subject to security updates and performance improvements.  * **Unsupported:** An API version in the not supported state may be deactivated at any time. An application using an unsupported API version should migrate to an active API version.  ## Version Map | Version Name | Previous Name | Start Date | Deprecation Date | |--------------|---------------|------------|------------------| | v2           | v2015_08      | 08/2015    | TBA              | | v3           | v2016_06      | 06/2016    |                  | | v4           | N/A           | 09/2018    |                  |  If you are looking for documentation for an older version  - [V4(Hunt Valley)](/api-docs-old/v4/documentation) (old V4 documentation) - [V3(Sunnyvale)](/api-docs-old/v3/documentation) - [V2(Mountain View)](/api-docs-old/v2/documentation)  # Changelog  Here's changelog for different versions  - [V4 Changelog](/api-docs-old/v4/changelog) - [V3 changelog](/api-docs-old/v3/changelog)  
 *
 * The version of the OpenAPI document: v4 (Hunt Valley)
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAppointment.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppointment::OAIAppointment(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppointment::OAIAppointment() {
    this->initializeModel();
}

OAIAppointment::~OAIAppointment() {}

void OAIAppointment::initializeModel() {

    m_allow_overlapping_isSet = false;
    m_allow_overlapping_isValid = false;

    m_appt_is_break_isSet = false;
    m_appt_is_break_isValid = false;

    m_base_recurring_appointment_isSet = false;
    m_base_recurring_appointment_isValid = false;

    m_billing_notes_isSet = false;
    m_billing_notes_isValid = false;

    m_billing_provider_isSet = false;
    m_billing_provider_isValid = false;

    m_billing_status_isSet = false;
    m_billing_status_isValid = false;

    m_clinical_note_isSet = false;
    m_clinical_note_isValid = false;

    m_cloned_from_isSet = false;
    m_cloned_from_isValid = false;

    m_color_isSet = false;
    m_color_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_custom_vitals_isSet = false;
    m_custom_vitals_isValid = false;

    m_deleted_flag_isSet = false;
    m_deleted_flag_isValid = false;

    m_doctor_isSet = false;
    m_doctor_isValid = false;

    m_duration_isSet = false;
    m_duration_isValid = false;

    m_exam_room_isSet = false;
    m_exam_room_isValid = false;

    m_extended_updated_at_isSet = false;
    m_extended_updated_at_isValid = false;

    m_first_billed_date_isSet = false;
    m_first_billed_date_isValid = false;

    m_icd10_codes_isSet = false;
    m_icd10_codes_isValid = false;

    m_icd9_codes_isSet = false;
    m_icd9_codes_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_ins1_status_isSet = false;
    m_ins1_status_isValid = false;

    m_ins2_status_isSet = false;
    m_ins2_status_isValid = false;

    m_is_virtual_base_isSet = false;
    m_is_virtual_base_isValid = false;

    m_is_walk_in_isSet = false;
    m_is_walk_in_isValid = false;

    m_last_billed_date_isSet = false;
    m_last_billed_date_isValid = false;

    m_notes_isSet = false;
    m_notes_isValid = false;

    m_office_isSet = false;
    m_office_isValid = false;

    m_patient_isSet = false;
    m_patient_isValid = false;

    m_primary_insurance_id_number_isSet = false;
    m_primary_insurance_id_number_isValid = false;

    m_primary_insurer_name_isSet = false;
    m_primary_insurer_name_isValid = false;

    m_primary_insurer_payer_id_isSet = false;
    m_primary_insurer_payer_id_isValid = false;

    m_profile_isSet = false;
    m_profile_isValid = false;

    m_reason_isSet = false;
    m_reason_isValid = false;

    m_recurring_appointment_isSet = false;
    m_recurring_appointment_isValid = false;

    m_reminder_profile_isSet = false;
    m_reminder_profile_isValid = false;

    m_reminders_isSet = false;
    m_reminders_isValid = false;

    m_scheduled_time_isSet = false;
    m_scheduled_time_isValid = false;

    m_secondary_insurance_id_number_isSet = false;
    m_secondary_insurance_id_number_isValid = false;

    m_secondary_insurer_name_isSet = false;
    m_secondary_insurer_name_isValid = false;

    m_secondary_insurer_payer_id_isSet = false;
    m_secondary_insurer_payer_id_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_status_transitions_isSet = false;
    m_status_transitions_isValid = false;

    m_supervising_provider_isSet = false;
    m_supervising_provider_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_vitals_isSet = false;
    m_vitals_isValid = false;
}

void OAIAppointment::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppointment::fromJsonObject(QJsonObject json) {

    m_allow_overlapping_isValid = ::OpenAPI::fromJsonValue(m_allow_overlapping, json[QString("allow_overlapping")]);
    m_allow_overlapping_isSet = !json[QString("allow_overlapping")].isNull() && m_allow_overlapping_isValid;

    m_appt_is_break_isValid = ::OpenAPI::fromJsonValue(m_appt_is_break, json[QString("appt_is_break")]);
    m_appt_is_break_isSet = !json[QString("appt_is_break")].isNull() && m_appt_is_break_isValid;

    m_base_recurring_appointment_isValid = ::OpenAPI::fromJsonValue(m_base_recurring_appointment, json[QString("base_recurring_appointment")]);
    m_base_recurring_appointment_isSet = !json[QString("base_recurring_appointment")].isNull() && m_base_recurring_appointment_isValid;

    m_billing_notes_isValid = ::OpenAPI::fromJsonValue(m_billing_notes, json[QString("billing_notes")]);
    m_billing_notes_isSet = !json[QString("billing_notes")].isNull() && m_billing_notes_isValid;

    m_billing_provider_isValid = ::OpenAPI::fromJsonValue(m_billing_provider, json[QString("billing_provider")]);
    m_billing_provider_isSet = !json[QString("billing_provider")].isNull() && m_billing_provider_isValid;

    m_billing_status_isValid = ::OpenAPI::fromJsonValue(m_billing_status, json[QString("billing_status")]);
    m_billing_status_isSet = !json[QString("billing_status")].isNull() && m_billing_status_isValid;

    m_clinical_note_isValid = ::OpenAPI::fromJsonValue(m_clinical_note, json[QString("clinical_note")]);
    m_clinical_note_isSet = !json[QString("clinical_note")].isNull() && m_clinical_note_isValid;

    m_cloned_from_isValid = ::OpenAPI::fromJsonValue(m_cloned_from, json[QString("cloned_from")]);
    m_cloned_from_isSet = !json[QString("cloned_from")].isNull() && m_cloned_from_isValid;

    m_color_isValid = ::OpenAPI::fromJsonValue(m_color, json[QString("color")]);
    m_color_isSet = !json[QString("color")].isNull() && m_color_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("custom_fields")]);
    m_custom_fields_isSet = !json[QString("custom_fields")].isNull() && m_custom_fields_isValid;

    m_custom_vitals_isValid = ::OpenAPI::fromJsonValue(m_custom_vitals, json[QString("custom_vitals")]);
    m_custom_vitals_isSet = !json[QString("custom_vitals")].isNull() && m_custom_vitals_isValid;

    m_deleted_flag_isValid = ::OpenAPI::fromJsonValue(m_deleted_flag, json[QString("deleted_flag")]);
    m_deleted_flag_isSet = !json[QString("deleted_flag")].isNull() && m_deleted_flag_isValid;

    m_doctor_isValid = ::OpenAPI::fromJsonValue(m_doctor, json[QString("doctor")]);
    m_doctor_isSet = !json[QString("doctor")].isNull() && m_doctor_isValid;

    m_duration_isValid = ::OpenAPI::fromJsonValue(m_duration, json[QString("duration")]);
    m_duration_isSet = !json[QString("duration")].isNull() && m_duration_isValid;

    m_exam_room_isValid = ::OpenAPI::fromJsonValue(m_exam_room, json[QString("exam_room")]);
    m_exam_room_isSet = !json[QString("exam_room")].isNull() && m_exam_room_isValid;

    m_extended_updated_at_isValid = ::OpenAPI::fromJsonValue(m_extended_updated_at, json[QString("extended_updated_at")]);
    m_extended_updated_at_isSet = !json[QString("extended_updated_at")].isNull() && m_extended_updated_at_isValid;

    m_first_billed_date_isValid = ::OpenAPI::fromJsonValue(m_first_billed_date, json[QString("first_billed_date")]);
    m_first_billed_date_isSet = !json[QString("first_billed_date")].isNull() && m_first_billed_date_isValid;

    m_icd10_codes_isValid = ::OpenAPI::fromJsonValue(m_icd10_codes, json[QString("icd10_codes")]);
    m_icd10_codes_isSet = !json[QString("icd10_codes")].isNull() && m_icd10_codes_isValid;

    m_icd9_codes_isValid = ::OpenAPI::fromJsonValue(m_icd9_codes, json[QString("icd9_codes")]);
    m_icd9_codes_isSet = !json[QString("icd9_codes")].isNull() && m_icd9_codes_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_ins1_status_isValid = ::OpenAPI::fromJsonValue(m_ins1_status, json[QString("ins1_status")]);
    m_ins1_status_isSet = !json[QString("ins1_status")].isNull() && m_ins1_status_isValid;

    m_ins2_status_isValid = ::OpenAPI::fromJsonValue(m_ins2_status, json[QString("ins2_status")]);
    m_ins2_status_isSet = !json[QString("ins2_status")].isNull() && m_ins2_status_isValid;

    m_is_virtual_base_isValid = ::OpenAPI::fromJsonValue(m_is_virtual_base, json[QString("is_virtual_base")]);
    m_is_virtual_base_isSet = !json[QString("is_virtual_base")].isNull() && m_is_virtual_base_isValid;

    m_is_walk_in_isValid = ::OpenAPI::fromJsonValue(m_is_walk_in, json[QString("is_walk_in")]);
    m_is_walk_in_isSet = !json[QString("is_walk_in")].isNull() && m_is_walk_in_isValid;

    m_last_billed_date_isValid = ::OpenAPI::fromJsonValue(m_last_billed_date, json[QString("last_billed_date")]);
    m_last_billed_date_isSet = !json[QString("last_billed_date")].isNull() && m_last_billed_date_isValid;

    m_notes_isValid = ::OpenAPI::fromJsonValue(m_notes, json[QString("notes")]);
    m_notes_isSet = !json[QString("notes")].isNull() && m_notes_isValid;

    m_office_isValid = ::OpenAPI::fromJsonValue(m_office, json[QString("office")]);
    m_office_isSet = !json[QString("office")].isNull() && m_office_isValid;

    m_patient_isValid = ::OpenAPI::fromJsonValue(m_patient, json[QString("patient")]);
    m_patient_isSet = !json[QString("patient")].isNull() && m_patient_isValid;

    m_primary_insurance_id_number_isValid = ::OpenAPI::fromJsonValue(m_primary_insurance_id_number, json[QString("primary_insurance_id_number")]);
    m_primary_insurance_id_number_isSet = !json[QString("primary_insurance_id_number")].isNull() && m_primary_insurance_id_number_isValid;

    m_primary_insurer_name_isValid = ::OpenAPI::fromJsonValue(m_primary_insurer_name, json[QString("primary_insurer_name")]);
    m_primary_insurer_name_isSet = !json[QString("primary_insurer_name")].isNull() && m_primary_insurer_name_isValid;

    m_primary_insurer_payer_id_isValid = ::OpenAPI::fromJsonValue(m_primary_insurer_payer_id, json[QString("primary_insurer_payer_id")]);
    m_primary_insurer_payer_id_isSet = !json[QString("primary_insurer_payer_id")].isNull() && m_primary_insurer_payer_id_isValid;

    m_profile_isValid = ::OpenAPI::fromJsonValue(m_profile, json[QString("profile")]);
    m_profile_isSet = !json[QString("profile")].isNull() && m_profile_isValid;

    m_reason_isValid = ::OpenAPI::fromJsonValue(m_reason, json[QString("reason")]);
    m_reason_isSet = !json[QString("reason")].isNull() && m_reason_isValid;

    m_recurring_appointment_isValid = ::OpenAPI::fromJsonValue(m_recurring_appointment, json[QString("recurring_appointment")]);
    m_recurring_appointment_isSet = !json[QString("recurring_appointment")].isNull() && m_recurring_appointment_isValid;

    m_reminder_profile_isValid = ::OpenAPI::fromJsonValue(m_reminder_profile, json[QString("reminder_profile")]);
    m_reminder_profile_isSet = !json[QString("reminder_profile")].isNull() && m_reminder_profile_isValid;

    m_reminders_isValid = ::OpenAPI::fromJsonValue(m_reminders, json[QString("reminders")]);
    m_reminders_isSet = !json[QString("reminders")].isNull() && m_reminders_isValid;

    m_scheduled_time_isValid = ::OpenAPI::fromJsonValue(m_scheduled_time, json[QString("scheduled_time")]);
    m_scheduled_time_isSet = !json[QString("scheduled_time")].isNull() && m_scheduled_time_isValid;

    m_secondary_insurance_id_number_isValid = ::OpenAPI::fromJsonValue(m_secondary_insurance_id_number, json[QString("secondary_insurance_id_number")]);
    m_secondary_insurance_id_number_isSet = !json[QString("secondary_insurance_id_number")].isNull() && m_secondary_insurance_id_number_isValid;

    m_secondary_insurer_name_isValid = ::OpenAPI::fromJsonValue(m_secondary_insurer_name, json[QString("secondary_insurer_name")]);
    m_secondary_insurer_name_isSet = !json[QString("secondary_insurer_name")].isNull() && m_secondary_insurer_name_isValid;

    m_secondary_insurer_payer_id_isValid = ::OpenAPI::fromJsonValue(m_secondary_insurer_payer_id, json[QString("secondary_insurer_payer_id")]);
    m_secondary_insurer_payer_id_isSet = !json[QString("secondary_insurer_payer_id")].isNull() && m_secondary_insurer_payer_id_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_status_transitions_isValid = ::OpenAPI::fromJsonValue(m_status_transitions, json[QString("status_transitions")]);
    m_status_transitions_isSet = !json[QString("status_transitions")].isNull() && m_status_transitions_isValid;

    m_supervising_provider_isValid = ::OpenAPI::fromJsonValue(m_supervising_provider, json[QString("supervising_provider")]);
    m_supervising_provider_isSet = !json[QString("supervising_provider")].isNull() && m_supervising_provider_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updated_at")]);
    m_updated_at_isSet = !json[QString("updated_at")].isNull() && m_updated_at_isValid;

    m_vitals_isValid = ::OpenAPI::fromJsonValue(m_vitals, json[QString("vitals")]);
    m_vitals_isSet = !json[QString("vitals")].isNull() && m_vitals_isValid;
}

QString OAIAppointment::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppointment::asJsonObject() const {
    QJsonObject obj;
    if (m_allow_overlapping_isSet) {
        obj.insert(QString("allow_overlapping"), ::OpenAPI::toJsonValue(m_allow_overlapping));
    }
    if (m_appt_is_break_isSet) {
        obj.insert(QString("appt_is_break"), ::OpenAPI::toJsonValue(m_appt_is_break));
    }
    if (m_base_recurring_appointment_isSet) {
        obj.insert(QString("base_recurring_appointment"), ::OpenAPI::toJsonValue(m_base_recurring_appointment));
    }
    if (m_billing_notes.size() > 0) {
        obj.insert(QString("billing_notes"), ::OpenAPI::toJsonValue(m_billing_notes));
    }
    if (m_billing_provider_isSet) {
        obj.insert(QString("billing_provider"), ::OpenAPI::toJsonValue(m_billing_provider));
    }
    if (m_billing_status_isSet) {
        obj.insert(QString("billing_status"), ::OpenAPI::toJsonValue(m_billing_status));
    }
    if (m_clinical_note.isSet()) {
        obj.insert(QString("clinical_note"), ::OpenAPI::toJsonValue(m_clinical_note));
    }
    if (m_cloned_from_isSet) {
        obj.insert(QString("cloned_from"), ::OpenAPI::toJsonValue(m_cloned_from));
    }
    if (m_color_isSet) {
        obj.insert(QString("color"), ::OpenAPI::toJsonValue(m_color));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("created_at"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_custom_fields.size() > 0) {
        obj.insert(QString("custom_fields"), ::OpenAPI::toJsonValue(m_custom_fields));
    }
    if (m_custom_vitals.size() > 0) {
        obj.insert(QString("custom_vitals"), ::OpenAPI::toJsonValue(m_custom_vitals));
    }
    if (m_deleted_flag_isSet) {
        obj.insert(QString("deleted_flag"), ::OpenAPI::toJsonValue(m_deleted_flag));
    }
    if (m_doctor_isSet) {
        obj.insert(QString("doctor"), ::OpenAPI::toJsonValue(m_doctor));
    }
    if (m_duration_isSet) {
        obj.insert(QString("duration"), ::OpenAPI::toJsonValue(m_duration));
    }
    if (m_exam_room_isSet) {
        obj.insert(QString("exam_room"), ::OpenAPI::toJsonValue(m_exam_room));
    }
    if (m_extended_updated_at_isSet) {
        obj.insert(QString("extended_updated_at"), ::OpenAPI::toJsonValue(m_extended_updated_at));
    }
    if (m_first_billed_date_isSet) {
        obj.insert(QString("first_billed_date"), ::OpenAPI::toJsonValue(m_first_billed_date));
    }
    if (m_icd10_codes.size() > 0) {
        obj.insert(QString("icd10_codes"), ::OpenAPI::toJsonValue(m_icd10_codes));
    }
    if (m_icd9_codes.size() > 0) {
        obj.insert(QString("icd9_codes"), ::OpenAPI::toJsonValue(m_icd9_codes));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_ins1_status_isSet) {
        obj.insert(QString("ins1_status"), ::OpenAPI::toJsonValue(m_ins1_status));
    }
    if (m_ins2_status_isSet) {
        obj.insert(QString("ins2_status"), ::OpenAPI::toJsonValue(m_ins2_status));
    }
    if (m_is_virtual_base_isSet) {
        obj.insert(QString("is_virtual_base"), ::OpenAPI::toJsonValue(m_is_virtual_base));
    }
    if (m_is_walk_in_isSet) {
        obj.insert(QString("is_walk_in"), ::OpenAPI::toJsonValue(m_is_walk_in));
    }
    if (m_last_billed_date_isSet) {
        obj.insert(QString("last_billed_date"), ::OpenAPI::toJsonValue(m_last_billed_date));
    }
    if (m_notes_isSet) {
        obj.insert(QString("notes"), ::OpenAPI::toJsonValue(m_notes));
    }
    if (m_office_isSet) {
        obj.insert(QString("office"), ::OpenAPI::toJsonValue(m_office));
    }
    if (m_patient_isSet) {
        obj.insert(QString("patient"), ::OpenAPI::toJsonValue(m_patient));
    }
    if (m_primary_insurance_id_number_isSet) {
        obj.insert(QString("primary_insurance_id_number"), ::OpenAPI::toJsonValue(m_primary_insurance_id_number));
    }
    if (m_primary_insurer_name_isSet) {
        obj.insert(QString("primary_insurer_name"), ::OpenAPI::toJsonValue(m_primary_insurer_name));
    }
    if (m_primary_insurer_payer_id_isSet) {
        obj.insert(QString("primary_insurer_payer_id"), ::OpenAPI::toJsonValue(m_primary_insurer_payer_id));
    }
    if (m_profile_isSet) {
        obj.insert(QString("profile"), ::OpenAPI::toJsonValue(m_profile));
    }
    if (m_reason_isSet) {
        obj.insert(QString("reason"), ::OpenAPI::toJsonValue(m_reason));
    }
    if (m_recurring_appointment_isSet) {
        obj.insert(QString("recurring_appointment"), ::OpenAPI::toJsonValue(m_recurring_appointment));
    }
    if (m_reminder_profile_isSet) {
        obj.insert(QString("reminder_profile"), ::OpenAPI::toJsonValue(m_reminder_profile));
    }
    if (m_reminders.size() > 0) {
        obj.insert(QString("reminders"), ::OpenAPI::toJsonValue(m_reminders));
    }
    if (m_scheduled_time_isSet) {
        obj.insert(QString("scheduled_time"), ::OpenAPI::toJsonValue(m_scheduled_time));
    }
    if (m_secondary_insurance_id_number_isSet) {
        obj.insert(QString("secondary_insurance_id_number"), ::OpenAPI::toJsonValue(m_secondary_insurance_id_number));
    }
    if (m_secondary_insurer_name_isSet) {
        obj.insert(QString("secondary_insurer_name"), ::OpenAPI::toJsonValue(m_secondary_insurer_name));
    }
    if (m_secondary_insurer_payer_id_isSet) {
        obj.insert(QString("secondary_insurer_payer_id"), ::OpenAPI::toJsonValue(m_secondary_insurer_payer_id));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_status_transitions.size() > 0) {
        obj.insert(QString("status_transitions"), ::OpenAPI::toJsonValue(m_status_transitions));
    }
    if (m_supervising_provider_isSet) {
        obj.insert(QString("supervising_provider"), ::OpenAPI::toJsonValue(m_supervising_provider));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updated_at"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    if (m_vitals.isSet()) {
        obj.insert(QString("vitals"), ::OpenAPI::toJsonValue(m_vitals));
    }
    return obj;
}

bool OAIAppointment::isAllowOverlapping() const {
    return m_allow_overlapping;
}
void OAIAppointment::setAllowOverlapping(const bool &allow_overlapping) {
    m_allow_overlapping = allow_overlapping;
    m_allow_overlapping_isSet = true;
}

bool OAIAppointment::is_allow_overlapping_Set() const{
    return m_allow_overlapping_isSet;
}

bool OAIAppointment::is_allow_overlapping_Valid() const{
    return m_allow_overlapping_isValid;
}

bool OAIAppointment::isApptIsBreak() const {
    return m_appt_is_break;
}
void OAIAppointment::setApptIsBreak(const bool &appt_is_break) {
    m_appt_is_break = appt_is_break;
    m_appt_is_break_isSet = true;
}

bool OAIAppointment::is_appt_is_break_Set() const{
    return m_appt_is_break_isSet;
}

bool OAIAppointment::is_appt_is_break_Valid() const{
    return m_appt_is_break_isValid;
}

QString OAIAppointment::getBaseRecurringAppointment() const {
    return m_base_recurring_appointment;
}
void OAIAppointment::setBaseRecurringAppointment(const QString &base_recurring_appointment) {
    m_base_recurring_appointment = base_recurring_appointment;
    m_base_recurring_appointment_isSet = true;
}

bool OAIAppointment::is_base_recurring_appointment_Set() const{
    return m_base_recurring_appointment_isSet;
}

bool OAIAppointment::is_base_recurring_appointment_Valid() const{
    return m_base_recurring_appointment_isValid;
}

QList<OAIClaimBillingNotes_1> OAIAppointment::getBillingNotes() const {
    return m_billing_notes;
}
void OAIAppointment::setBillingNotes(const QList<OAIClaimBillingNotes_1> &billing_notes) {
    m_billing_notes = billing_notes;
    m_billing_notes_isSet = true;
}

bool OAIAppointment::is_billing_notes_Set() const{
    return m_billing_notes_isSet;
}

bool OAIAppointment::is_billing_notes_Valid() const{
    return m_billing_notes_isValid;
}

QString OAIAppointment::getBillingProvider() const {
    return m_billing_provider;
}
void OAIAppointment::setBillingProvider(const QString &billing_provider) {
    m_billing_provider = billing_provider;
    m_billing_provider_isSet = true;
}

bool OAIAppointment::is_billing_provider_Set() const{
    return m_billing_provider_isSet;
}

bool OAIAppointment::is_billing_provider_Valid() const{
    return m_billing_provider_isValid;
}

QString OAIAppointment::getBillingStatus() const {
    return m_billing_status;
}
void OAIAppointment::setBillingStatus(const QString &billing_status) {
    m_billing_status = billing_status;
    m_billing_status_isSet = true;
}

bool OAIAppointment::is_billing_status_Set() const{
    return m_billing_status_isSet;
}

bool OAIAppointment::is_billing_status_Valid() const{
    return m_billing_status_isValid;
}

OAIClinicalNote_1 OAIAppointment::getClinicalNote() const {
    return m_clinical_note;
}
void OAIAppointment::setClinicalNote(const OAIClinicalNote_1 &clinical_note) {
    m_clinical_note = clinical_note;
    m_clinical_note_isSet = true;
}

bool OAIAppointment::is_clinical_note_Set() const{
    return m_clinical_note_isSet;
}

bool OAIAppointment::is_clinical_note_Valid() const{
    return m_clinical_note_isValid;
}

qint32 OAIAppointment::getClonedFrom() const {
    return m_cloned_from;
}
void OAIAppointment::setClonedFrom(const qint32 &cloned_from) {
    m_cloned_from = cloned_from;
    m_cloned_from_isSet = true;
}

bool OAIAppointment::is_cloned_from_Set() const{
    return m_cloned_from_isSet;
}

bool OAIAppointment::is_cloned_from_Valid() const{
    return m_cloned_from_isValid;
}

QString OAIAppointment::getColor() const {
    return m_color;
}
void OAIAppointment::setColor(const QString &color) {
    m_color = color;
    m_color_isSet = true;
}

bool OAIAppointment::is_color_Set() const{
    return m_color_isSet;
}

bool OAIAppointment::is_color_Valid() const{
    return m_color_isValid;
}

QString OAIAppointment::getCreatedAt() const {
    return m_created_at;
}
void OAIAppointment::setCreatedAt(const QString &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIAppointment::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIAppointment::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QList<OAICustomAppointmentFieldValue> OAIAppointment::getCustomFields() const {
    return m_custom_fields;
}
void OAIAppointment::setCustomFields(const QList<OAICustomAppointmentFieldValue> &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAIAppointment::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAIAppointment::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

QList<OAICustomVitalValue> OAIAppointment::getCustomVitals() const {
    return m_custom_vitals;
}
void OAIAppointment::setCustomVitals(const QList<OAICustomVitalValue> &custom_vitals) {
    m_custom_vitals = custom_vitals;
    m_custom_vitals_isSet = true;
}

bool OAIAppointment::is_custom_vitals_Set() const{
    return m_custom_vitals_isSet;
}

bool OAIAppointment::is_custom_vitals_Valid() const{
    return m_custom_vitals_isValid;
}

bool OAIAppointment::isDeletedFlag() const {
    return m_deleted_flag;
}
void OAIAppointment::setDeletedFlag(const bool &deleted_flag) {
    m_deleted_flag = deleted_flag;
    m_deleted_flag_isSet = true;
}

bool OAIAppointment::is_deleted_flag_Set() const{
    return m_deleted_flag_isSet;
}

bool OAIAppointment::is_deleted_flag_Valid() const{
    return m_deleted_flag_isValid;
}

qint32 OAIAppointment::getDoctor() const {
    return m_doctor;
}
void OAIAppointment::setDoctor(const qint32 &doctor) {
    m_doctor = doctor;
    m_doctor_isSet = true;
}

bool OAIAppointment::is_doctor_Set() const{
    return m_doctor_isSet;
}

bool OAIAppointment::is_doctor_Valid() const{
    return m_doctor_isValid;
}

qint32 OAIAppointment::getDuration() const {
    return m_duration;
}
void OAIAppointment::setDuration(const qint32 &duration) {
    m_duration = duration;
    m_duration_isSet = true;
}

bool OAIAppointment::is_duration_Set() const{
    return m_duration_isSet;
}

bool OAIAppointment::is_duration_Valid() const{
    return m_duration_isValid;
}

qint32 OAIAppointment::getExamRoom() const {
    return m_exam_room;
}
void OAIAppointment::setExamRoom(const qint32 &exam_room) {
    m_exam_room = exam_room;
    m_exam_room_isSet = true;
}

bool OAIAppointment::is_exam_room_Set() const{
    return m_exam_room_isSet;
}

bool OAIAppointment::is_exam_room_Valid() const{
    return m_exam_room_isValid;
}

QString OAIAppointment::getExtendedUpdatedAt() const {
    return m_extended_updated_at;
}
void OAIAppointment::setExtendedUpdatedAt(const QString &extended_updated_at) {
    m_extended_updated_at = extended_updated_at;
    m_extended_updated_at_isSet = true;
}

bool OAIAppointment::is_extended_updated_at_Set() const{
    return m_extended_updated_at_isSet;
}

bool OAIAppointment::is_extended_updated_at_Valid() const{
    return m_extended_updated_at_isValid;
}

QString OAIAppointment::getFirstBilledDate() const {
    return m_first_billed_date;
}
void OAIAppointment::setFirstBilledDate(const QString &first_billed_date) {
    m_first_billed_date = first_billed_date;
    m_first_billed_date_isSet = true;
}

bool OAIAppointment::is_first_billed_date_Set() const{
    return m_first_billed_date_isSet;
}

bool OAIAppointment::is_first_billed_date_Valid() const{
    return m_first_billed_date_isValid;
}

QList<QString> OAIAppointment::getIcd10Codes() const {
    return m_icd10_codes;
}
void OAIAppointment::setIcd10Codes(const QList<QString> &icd10_codes) {
    m_icd10_codes = icd10_codes;
    m_icd10_codes_isSet = true;
}

bool OAIAppointment::is_icd10_codes_Set() const{
    return m_icd10_codes_isSet;
}

bool OAIAppointment::is_icd10_codes_Valid() const{
    return m_icd10_codes_isValid;
}

QList<QString> OAIAppointment::getIcd9Codes() const {
    return m_icd9_codes;
}
void OAIAppointment::setIcd9Codes(const QList<QString> &icd9_codes) {
    m_icd9_codes = icd9_codes;
    m_icd9_codes_isSet = true;
}

bool OAIAppointment::is_icd9_codes_Set() const{
    return m_icd9_codes_isSet;
}

bool OAIAppointment::is_icd9_codes_Valid() const{
    return m_icd9_codes_isValid;
}

QString OAIAppointment::getId() const {
    return m_id;
}
void OAIAppointment::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIAppointment::is_id_Set() const{
    return m_id_isSet;
}

bool OAIAppointment::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIAppointment::getIns1Status() const {
    return m_ins1_status;
}
void OAIAppointment::setIns1Status(const QString &ins1_status) {
    m_ins1_status = ins1_status;
    m_ins1_status_isSet = true;
}

bool OAIAppointment::is_ins1_status_Set() const{
    return m_ins1_status_isSet;
}

bool OAIAppointment::is_ins1_status_Valid() const{
    return m_ins1_status_isValid;
}

QString OAIAppointment::getIns2Status() const {
    return m_ins2_status;
}
void OAIAppointment::setIns2Status(const QString &ins2_status) {
    m_ins2_status = ins2_status;
    m_ins2_status_isSet = true;
}

bool OAIAppointment::is_ins2_status_Set() const{
    return m_ins2_status_isSet;
}

bool OAIAppointment::is_ins2_status_Valid() const{
    return m_ins2_status_isValid;
}

bool OAIAppointment::isIsVirtualBase() const {
    return m_is_virtual_base;
}
void OAIAppointment::setIsVirtualBase(const bool &is_virtual_base) {
    m_is_virtual_base = is_virtual_base;
    m_is_virtual_base_isSet = true;
}

bool OAIAppointment::is_is_virtual_base_Set() const{
    return m_is_virtual_base_isSet;
}

bool OAIAppointment::is_is_virtual_base_Valid() const{
    return m_is_virtual_base_isValid;
}

bool OAIAppointment::isIsWalkIn() const {
    return m_is_walk_in;
}
void OAIAppointment::setIsWalkIn(const bool &is_walk_in) {
    m_is_walk_in = is_walk_in;
    m_is_walk_in_isSet = true;
}

bool OAIAppointment::is_is_walk_in_Set() const{
    return m_is_walk_in_isSet;
}

bool OAIAppointment::is_is_walk_in_Valid() const{
    return m_is_walk_in_isValid;
}

QString OAIAppointment::getLastBilledDate() const {
    return m_last_billed_date;
}
void OAIAppointment::setLastBilledDate(const QString &last_billed_date) {
    m_last_billed_date = last_billed_date;
    m_last_billed_date_isSet = true;
}

bool OAIAppointment::is_last_billed_date_Set() const{
    return m_last_billed_date_isSet;
}

bool OAIAppointment::is_last_billed_date_Valid() const{
    return m_last_billed_date_isValid;
}

QString OAIAppointment::getNotes() const {
    return m_notes;
}
void OAIAppointment::setNotes(const QString &notes) {
    m_notes = notes;
    m_notes_isSet = true;
}

bool OAIAppointment::is_notes_Set() const{
    return m_notes_isSet;
}

bool OAIAppointment::is_notes_Valid() const{
    return m_notes_isValid;
}

qint32 OAIAppointment::getOffice() const {
    return m_office;
}
void OAIAppointment::setOffice(const qint32 &office) {
    m_office = office;
    m_office_isSet = true;
}

bool OAIAppointment::is_office_Set() const{
    return m_office_isSet;
}

bool OAIAppointment::is_office_Valid() const{
    return m_office_isValid;
}

qint32 OAIAppointment::getPatient() const {
    return m_patient;
}
void OAIAppointment::setPatient(const qint32 &patient) {
    m_patient = patient;
    m_patient_isSet = true;
}

bool OAIAppointment::is_patient_Set() const{
    return m_patient_isSet;
}

bool OAIAppointment::is_patient_Valid() const{
    return m_patient_isValid;
}

QString OAIAppointment::getPrimaryInsuranceIdNumber() const {
    return m_primary_insurance_id_number;
}
void OAIAppointment::setPrimaryInsuranceIdNumber(const QString &primary_insurance_id_number) {
    m_primary_insurance_id_number = primary_insurance_id_number;
    m_primary_insurance_id_number_isSet = true;
}

bool OAIAppointment::is_primary_insurance_id_number_Set() const{
    return m_primary_insurance_id_number_isSet;
}

bool OAIAppointment::is_primary_insurance_id_number_Valid() const{
    return m_primary_insurance_id_number_isValid;
}

QString OAIAppointment::getPrimaryInsurerName() const {
    return m_primary_insurer_name;
}
void OAIAppointment::setPrimaryInsurerName(const QString &primary_insurer_name) {
    m_primary_insurer_name = primary_insurer_name;
    m_primary_insurer_name_isSet = true;
}

bool OAIAppointment::is_primary_insurer_name_Set() const{
    return m_primary_insurer_name_isSet;
}

bool OAIAppointment::is_primary_insurer_name_Valid() const{
    return m_primary_insurer_name_isValid;
}

QString OAIAppointment::getPrimaryInsurerPayerId() const {
    return m_primary_insurer_payer_id;
}
void OAIAppointment::setPrimaryInsurerPayerId(const QString &primary_insurer_payer_id) {
    m_primary_insurer_payer_id = primary_insurer_payer_id;
    m_primary_insurer_payer_id_isSet = true;
}

bool OAIAppointment::is_primary_insurer_payer_id_Set() const{
    return m_primary_insurer_payer_id_isSet;
}

bool OAIAppointment::is_primary_insurer_payer_id_Valid() const{
    return m_primary_insurer_payer_id_isValid;
}

qint32 OAIAppointment::getProfile() const {
    return m_profile;
}
void OAIAppointment::setProfile(const qint32 &profile) {
    m_profile = profile;
    m_profile_isSet = true;
}

bool OAIAppointment::is_profile_Set() const{
    return m_profile_isSet;
}

bool OAIAppointment::is_profile_Valid() const{
    return m_profile_isValid;
}

QString OAIAppointment::getReason() const {
    return m_reason;
}
void OAIAppointment::setReason(const QString &reason) {
    m_reason = reason;
    m_reason_isSet = true;
}

bool OAIAppointment::is_reason_Set() const{
    return m_reason_isSet;
}

bool OAIAppointment::is_reason_Valid() const{
    return m_reason_isValid;
}

bool OAIAppointment::isRecurringAppointment() const {
    return m_recurring_appointment;
}
void OAIAppointment::setRecurringAppointment(const bool &recurring_appointment) {
    m_recurring_appointment = recurring_appointment;
    m_recurring_appointment_isSet = true;
}

bool OAIAppointment::is_recurring_appointment_Set() const{
    return m_recurring_appointment_isSet;
}

bool OAIAppointment::is_recurring_appointment_Valid() const{
    return m_recurring_appointment_isValid;
}

QString OAIAppointment::getReminderProfile() const {
    return m_reminder_profile;
}
void OAIAppointment::setReminderProfile(const QString &reminder_profile) {
    m_reminder_profile = reminder_profile;
    m_reminder_profile_isSet = true;
}

bool OAIAppointment::is_reminder_profile_Set() const{
    return m_reminder_profile_isSet;
}

bool OAIAppointment::is_reminder_profile_Valid() const{
    return m_reminder_profile_isValid;
}

QList<OAISimpleReminder> OAIAppointment::getReminders() const {
    return m_reminders;
}
void OAIAppointment::setReminders(const QList<OAISimpleReminder> &reminders) {
    m_reminders = reminders;
    m_reminders_isSet = true;
}

bool OAIAppointment::is_reminders_Set() const{
    return m_reminders_isSet;
}

bool OAIAppointment::is_reminders_Valid() const{
    return m_reminders_isValid;
}

QString OAIAppointment::getScheduledTime() const {
    return m_scheduled_time;
}
void OAIAppointment::setScheduledTime(const QString &scheduled_time) {
    m_scheduled_time = scheduled_time;
    m_scheduled_time_isSet = true;
}

bool OAIAppointment::is_scheduled_time_Set() const{
    return m_scheduled_time_isSet;
}

bool OAIAppointment::is_scheduled_time_Valid() const{
    return m_scheduled_time_isValid;
}

QString OAIAppointment::getSecondaryInsuranceIdNumber() const {
    return m_secondary_insurance_id_number;
}
void OAIAppointment::setSecondaryInsuranceIdNumber(const QString &secondary_insurance_id_number) {
    m_secondary_insurance_id_number = secondary_insurance_id_number;
    m_secondary_insurance_id_number_isSet = true;
}

bool OAIAppointment::is_secondary_insurance_id_number_Set() const{
    return m_secondary_insurance_id_number_isSet;
}

bool OAIAppointment::is_secondary_insurance_id_number_Valid() const{
    return m_secondary_insurance_id_number_isValid;
}

QString OAIAppointment::getSecondaryInsurerName() const {
    return m_secondary_insurer_name;
}
void OAIAppointment::setSecondaryInsurerName(const QString &secondary_insurer_name) {
    m_secondary_insurer_name = secondary_insurer_name;
    m_secondary_insurer_name_isSet = true;
}

bool OAIAppointment::is_secondary_insurer_name_Set() const{
    return m_secondary_insurer_name_isSet;
}

bool OAIAppointment::is_secondary_insurer_name_Valid() const{
    return m_secondary_insurer_name_isValid;
}

QString OAIAppointment::getSecondaryInsurerPayerId() const {
    return m_secondary_insurer_payer_id;
}
void OAIAppointment::setSecondaryInsurerPayerId(const QString &secondary_insurer_payer_id) {
    m_secondary_insurer_payer_id = secondary_insurer_payer_id;
    m_secondary_insurer_payer_id_isSet = true;
}

bool OAIAppointment::is_secondary_insurer_payer_id_Set() const{
    return m_secondary_insurer_payer_id_isSet;
}

bool OAIAppointment::is_secondary_insurer_payer_id_Valid() const{
    return m_secondary_insurer_payer_id_isValid;
}

QString OAIAppointment::getStatus() const {
    return m_status;
}
void OAIAppointment::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIAppointment::is_status_Set() const{
    return m_status_isSet;
}

bool OAIAppointment::is_status_Valid() const{
    return m_status_isValid;
}

QList<OAIAppointmentStatusTransition> OAIAppointment::getStatusTransitions() const {
    return m_status_transitions;
}
void OAIAppointment::setStatusTransitions(const QList<OAIAppointmentStatusTransition> &status_transitions) {
    m_status_transitions = status_transitions;
    m_status_transitions_isSet = true;
}

bool OAIAppointment::is_status_transitions_Set() const{
    return m_status_transitions_isSet;
}

bool OAIAppointment::is_status_transitions_Valid() const{
    return m_status_transitions_isValid;
}

QString OAIAppointment::getSupervisingProvider() const {
    return m_supervising_provider;
}
void OAIAppointment::setSupervisingProvider(const QString &supervising_provider) {
    m_supervising_provider = supervising_provider;
    m_supervising_provider_isSet = true;
}

bool OAIAppointment::is_supervising_provider_Set() const{
    return m_supervising_provider_isSet;
}

bool OAIAppointment::is_supervising_provider_Valid() const{
    return m_supervising_provider_isValid;
}

QString OAIAppointment::getUpdatedAt() const {
    return m_updated_at;
}
void OAIAppointment::setUpdatedAt(const QString &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIAppointment::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIAppointment::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

OAISystemVitals OAIAppointment::getVitals() const {
    return m_vitals;
}
void OAIAppointment::setVitals(const OAISystemVitals &vitals) {
    m_vitals = vitals;
    m_vitals_isSet = true;
}

bool OAIAppointment::is_vitals_Set() const{
    return m_vitals_isSet;
}

bool OAIAppointment::is_vitals_Valid() const{
    return m_vitals_isValid;
}

bool OAIAppointment::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_allow_overlapping_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_appt_is_break_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_base_recurring_appointment_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_billing_notes.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_billing_provider_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_billing_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_clinical_note.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_cloned_from_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_color_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_fields.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_vitals.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_deleted_flag_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_doctor_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_exam_room_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_extended_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_billed_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_icd10_codes.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_icd9_codes.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ins1_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ins2_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_virtual_base_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_walk_in_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_billed_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_office_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_patient_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_primary_insurance_id_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_primary_insurer_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_primary_insurer_payer_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_profile_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_recurring_appointment_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reminder_profile_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reminders.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_scheduled_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_secondary_insurance_id_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_secondary_insurer_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_secondary_insurer_payer_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_transitions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_supervising_provider_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vitals.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAppointment::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_doctor_isValid && m_exam_room_isValid && m_office_isValid && m_patient_isValid && m_scheduled_time_isValid && true;
}

} // namespace OpenAPI
