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

#include "OAIPatient.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPatient::OAIPatient(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPatient::OAIPatient() {
    this->initializeModel();
}

OAIPatient::~OAIPatient() {}

void OAIPatient::initializeModel() {

    m_address_isSet = false;
    m_address_isValid = false;

    m_auto_accident_insurance_isSet = false;
    m_auto_accident_insurance_isValid = false;

    m_cell_phone_isSet = false;
    m_cell_phone_isValid = false;

    m_chart_id_isSet = false;
    m_chart_id_isValid = false;

    m_city_isSet = false;
    m_city_isValid = false;

    m_copay_isSet = false;
    m_copay_isValid = false;

    m_custom_demographics_isSet = false;
    m_custom_demographics_isValid = false;

    m_date_of_birth_isSet = false;
    m_date_of_birth_isValid = false;

    m_date_of_first_appointment_isSet = false;
    m_date_of_first_appointment_isValid = false;

    m_date_of_last_appointment_isSet = false;
    m_date_of_last_appointment_isValid = false;

    m_default_pharmacy_isSet = false;
    m_default_pharmacy_isValid = false;

    m_disable_sms_messages_isSet = false;
    m_disable_sms_messages_isValid = false;

    m_doctor_isSet = false;
    m_doctor_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_emergency_contact_name_isSet = false;
    m_emergency_contact_name_isValid = false;

    m_emergency_contact_phone_isSet = false;
    m_emergency_contact_phone_isValid = false;

    m_emergency_contact_relation_isSet = false;
    m_emergency_contact_relation_isValid = false;

    m_employer_isSet = false;
    m_employer_isValid = false;

    m_employer_address_isSet = false;
    m_employer_address_isValid = false;

    m_employer_city_isSet = false;
    m_employer_city_isValid = false;

    m_employer_state_isSet = false;
    m_employer_state_isValid = false;

    m_employer_zip_code_isSet = false;
    m_employer_zip_code_isValid = false;

    m_ethnicity_isSet = false;
    m_ethnicity_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_gender_isSet = false;
    m_gender_isValid = false;

    m_home_phone_isSet = false;
    m_home_phone_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_middle_name_isSet = false;
    m_middle_name_isValid = false;

    m_nick_name_isSet = false;
    m_nick_name_isValid = false;

    m_office_phone_isSet = false;
    m_office_phone_isValid = false;

    m_offices_isSet = false;
    m_offices_isValid = false;

    m_patient_flags_isSet = false;
    m_patient_flags_isValid = false;

    m_patient_flags_attached_isSet = false;
    m_patient_flags_attached_isValid = false;

    m_patient_payment_profile_isSet = false;
    m_patient_payment_profile_isValid = false;

    m_patient_photo_isSet = false;
    m_patient_photo_isValid = false;

    m_patient_photo_date_isSet = false;
    m_patient_photo_date_isValid = false;

    m_patient_status_isSet = false;
    m_patient_status_isValid = false;

    m_preferred_language_isSet = false;
    m_preferred_language_isValid = false;

    m_primary_care_physician_isSet = false;
    m_primary_care_physician_isValid = false;

    m_primary_insurance_isSet = false;
    m_primary_insurance_isValid = false;

    m_race_isSet = false;
    m_race_isValid = false;

    m_referring_doctor_isSet = false;
    m_referring_doctor_isValid = false;

    m_referring_source_isSet = false;
    m_referring_source_isValid = false;

    m_responsible_party_email_isSet = false;
    m_responsible_party_email_isValid = false;

    m_responsible_party_name_isSet = false;
    m_responsible_party_name_isValid = false;

    m_responsible_party_phone_isSet = false;
    m_responsible_party_phone_isValid = false;

    m_responsible_party_relation_isSet = false;
    m_responsible_party_relation_isValid = false;

    m_secondary_insurance_isSet = false;
    m_secondary_insurance_isValid = false;

    m_social_security_number_isSet = false;
    m_social_security_number_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;

    m_tertiary_insurance_isSet = false;
    m_tertiary_insurance_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_workers_comp_insurance_isSet = false;
    m_workers_comp_insurance_isValid = false;

    m_zip_code_isSet = false;
    m_zip_code_isValid = false;
}

void OAIPatient::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPatient::fromJsonObject(QJsonObject json) {

    m_address_isValid = ::OpenAPI::fromJsonValue(m_address, json[QString("address")]);
    m_address_isSet = !json[QString("address")].isNull() && m_address_isValid;

    m_auto_accident_insurance_isValid = ::OpenAPI::fromJsonValue(m_auto_accident_insurance, json[QString("auto_accident_insurance")]);
    m_auto_accident_insurance_isSet = !json[QString("auto_accident_insurance")].isNull() && m_auto_accident_insurance_isValid;

    m_cell_phone_isValid = ::OpenAPI::fromJsonValue(m_cell_phone, json[QString("cell_phone")]);
    m_cell_phone_isSet = !json[QString("cell_phone")].isNull() && m_cell_phone_isValid;

    m_chart_id_isValid = ::OpenAPI::fromJsonValue(m_chart_id, json[QString("chart_id")]);
    m_chart_id_isSet = !json[QString("chart_id")].isNull() && m_chart_id_isValid;

    m_city_isValid = ::OpenAPI::fromJsonValue(m_city, json[QString("city")]);
    m_city_isSet = !json[QString("city")].isNull() && m_city_isValid;

    m_copay_isValid = ::OpenAPI::fromJsonValue(m_copay, json[QString("copay")]);
    m_copay_isSet = !json[QString("copay")].isNull() && m_copay_isValid;

    m_custom_demographics_isValid = ::OpenAPI::fromJsonValue(m_custom_demographics, json[QString("custom_demographics")]);
    m_custom_demographics_isSet = !json[QString("custom_demographics")].isNull() && m_custom_demographics_isValid;

    m_date_of_birth_isValid = ::OpenAPI::fromJsonValue(m_date_of_birth, json[QString("date_of_birth")]);
    m_date_of_birth_isSet = !json[QString("date_of_birth")].isNull() && m_date_of_birth_isValid;

    m_date_of_first_appointment_isValid = ::OpenAPI::fromJsonValue(m_date_of_first_appointment, json[QString("date_of_first_appointment")]);
    m_date_of_first_appointment_isSet = !json[QString("date_of_first_appointment")].isNull() && m_date_of_first_appointment_isValid;

    m_date_of_last_appointment_isValid = ::OpenAPI::fromJsonValue(m_date_of_last_appointment, json[QString("date_of_last_appointment")]);
    m_date_of_last_appointment_isSet = !json[QString("date_of_last_appointment")].isNull() && m_date_of_last_appointment_isValid;

    m_default_pharmacy_isValid = ::OpenAPI::fromJsonValue(m_default_pharmacy, json[QString("default_pharmacy")]);
    m_default_pharmacy_isSet = !json[QString("default_pharmacy")].isNull() && m_default_pharmacy_isValid;

    m_disable_sms_messages_isValid = ::OpenAPI::fromJsonValue(m_disable_sms_messages, json[QString("disable_sms_messages")]);
    m_disable_sms_messages_isSet = !json[QString("disable_sms_messages")].isNull() && m_disable_sms_messages_isValid;

    m_doctor_isValid = ::OpenAPI::fromJsonValue(m_doctor, json[QString("doctor")]);
    m_doctor_isSet = !json[QString("doctor")].isNull() && m_doctor_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_emergency_contact_name_isValid = ::OpenAPI::fromJsonValue(m_emergency_contact_name, json[QString("emergency_contact_name")]);
    m_emergency_contact_name_isSet = !json[QString("emergency_contact_name")].isNull() && m_emergency_contact_name_isValid;

    m_emergency_contact_phone_isValid = ::OpenAPI::fromJsonValue(m_emergency_contact_phone, json[QString("emergency_contact_phone")]);
    m_emergency_contact_phone_isSet = !json[QString("emergency_contact_phone")].isNull() && m_emergency_contact_phone_isValid;

    m_emergency_contact_relation_isValid = ::OpenAPI::fromJsonValue(m_emergency_contact_relation, json[QString("emergency_contact_relation")]);
    m_emergency_contact_relation_isSet = !json[QString("emergency_contact_relation")].isNull() && m_emergency_contact_relation_isValid;

    m_employer_isValid = ::OpenAPI::fromJsonValue(m_employer, json[QString("employer")]);
    m_employer_isSet = !json[QString("employer")].isNull() && m_employer_isValid;

    m_employer_address_isValid = ::OpenAPI::fromJsonValue(m_employer_address, json[QString("employer_address")]);
    m_employer_address_isSet = !json[QString("employer_address")].isNull() && m_employer_address_isValid;

    m_employer_city_isValid = ::OpenAPI::fromJsonValue(m_employer_city, json[QString("employer_city")]);
    m_employer_city_isSet = !json[QString("employer_city")].isNull() && m_employer_city_isValid;

    m_employer_state_isValid = ::OpenAPI::fromJsonValue(m_employer_state, json[QString("employer_state")]);
    m_employer_state_isSet = !json[QString("employer_state")].isNull() && m_employer_state_isValid;

    m_employer_zip_code_isValid = ::OpenAPI::fromJsonValue(m_employer_zip_code, json[QString("employer_zip_code")]);
    m_employer_zip_code_isSet = !json[QString("employer_zip_code")].isNull() && m_employer_zip_code_isValid;

    m_ethnicity_isValid = ::OpenAPI::fromJsonValue(m_ethnicity, json[QString("ethnicity")]);
    m_ethnicity_isSet = !json[QString("ethnicity")].isNull() && m_ethnicity_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("first_name")]);
    m_first_name_isSet = !json[QString("first_name")].isNull() && m_first_name_isValid;

    m_gender_isValid = ::OpenAPI::fromJsonValue(m_gender, json[QString("gender")]);
    m_gender_isSet = !json[QString("gender")].isNull() && m_gender_isValid;

    m_home_phone_isValid = ::OpenAPI::fromJsonValue(m_home_phone, json[QString("home_phone")]);
    m_home_phone_isSet = !json[QString("home_phone")].isNull() && m_home_phone_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("last_name")]);
    m_last_name_isSet = !json[QString("last_name")].isNull() && m_last_name_isValid;

    m_middle_name_isValid = ::OpenAPI::fromJsonValue(m_middle_name, json[QString("middle_name")]);
    m_middle_name_isSet = !json[QString("middle_name")].isNull() && m_middle_name_isValid;

    m_nick_name_isValid = ::OpenAPI::fromJsonValue(m_nick_name, json[QString("nick_name")]);
    m_nick_name_isSet = !json[QString("nick_name")].isNull() && m_nick_name_isValid;

    m_office_phone_isValid = ::OpenAPI::fromJsonValue(m_office_phone, json[QString("office_phone")]);
    m_office_phone_isSet = !json[QString("office_phone")].isNull() && m_office_phone_isValid;

    m_offices_isValid = ::OpenAPI::fromJsonValue(m_offices, json[QString("offices")]);
    m_offices_isSet = !json[QString("offices")].isNull() && m_offices_isValid;

    m_patient_flags_isValid = ::OpenAPI::fromJsonValue(m_patient_flags, json[QString("patient_flags")]);
    m_patient_flags_isSet = !json[QString("patient_flags")].isNull() && m_patient_flags_isValid;

    m_patient_flags_attached_isValid = ::OpenAPI::fromJsonValue(m_patient_flags_attached, json[QString("patient_flags_attached")]);
    m_patient_flags_attached_isSet = !json[QString("patient_flags_attached")].isNull() && m_patient_flags_attached_isValid;

    m_patient_payment_profile_isValid = ::OpenAPI::fromJsonValue(m_patient_payment_profile, json[QString("patient_payment_profile")]);
    m_patient_payment_profile_isSet = !json[QString("patient_payment_profile")].isNull() && m_patient_payment_profile_isValid;

    m_patient_photo_isValid = ::OpenAPI::fromJsonValue(m_patient_photo, json[QString("patient_photo")]);
    m_patient_photo_isSet = !json[QString("patient_photo")].isNull() && m_patient_photo_isValid;

    m_patient_photo_date_isValid = ::OpenAPI::fromJsonValue(m_patient_photo_date, json[QString("patient_photo_date")]);
    m_patient_photo_date_isSet = !json[QString("patient_photo_date")].isNull() && m_patient_photo_date_isValid;

    m_patient_status_isValid = ::OpenAPI::fromJsonValue(m_patient_status, json[QString("patient_status")]);
    m_patient_status_isSet = !json[QString("patient_status")].isNull() && m_patient_status_isValid;

    m_preferred_language_isValid = ::OpenAPI::fromJsonValue(m_preferred_language, json[QString("preferred_language")]);
    m_preferred_language_isSet = !json[QString("preferred_language")].isNull() && m_preferred_language_isValid;

    m_primary_care_physician_isValid = ::OpenAPI::fromJsonValue(m_primary_care_physician, json[QString("primary_care_physician")]);
    m_primary_care_physician_isSet = !json[QString("primary_care_physician")].isNull() && m_primary_care_physician_isValid;

    m_primary_insurance_isValid = ::OpenAPI::fromJsonValue(m_primary_insurance, json[QString("primary_insurance")]);
    m_primary_insurance_isSet = !json[QString("primary_insurance")].isNull() && m_primary_insurance_isValid;

    m_race_isValid = ::OpenAPI::fromJsonValue(m_race, json[QString("race")]);
    m_race_isSet = !json[QString("race")].isNull() && m_race_isValid;

    m_referring_doctor_isValid = ::OpenAPI::fromJsonValue(m_referring_doctor, json[QString("referring_doctor")]);
    m_referring_doctor_isSet = !json[QString("referring_doctor")].isNull() && m_referring_doctor_isValid;

    m_referring_source_isValid = ::OpenAPI::fromJsonValue(m_referring_source, json[QString("referring_source")]);
    m_referring_source_isSet = !json[QString("referring_source")].isNull() && m_referring_source_isValid;

    m_responsible_party_email_isValid = ::OpenAPI::fromJsonValue(m_responsible_party_email, json[QString("responsible_party_email")]);
    m_responsible_party_email_isSet = !json[QString("responsible_party_email")].isNull() && m_responsible_party_email_isValid;

    m_responsible_party_name_isValid = ::OpenAPI::fromJsonValue(m_responsible_party_name, json[QString("responsible_party_name")]);
    m_responsible_party_name_isSet = !json[QString("responsible_party_name")].isNull() && m_responsible_party_name_isValid;

    m_responsible_party_phone_isValid = ::OpenAPI::fromJsonValue(m_responsible_party_phone, json[QString("responsible_party_phone")]);
    m_responsible_party_phone_isSet = !json[QString("responsible_party_phone")].isNull() && m_responsible_party_phone_isValid;

    m_responsible_party_relation_isValid = ::OpenAPI::fromJsonValue(m_responsible_party_relation, json[QString("responsible_party_relation")]);
    m_responsible_party_relation_isSet = !json[QString("responsible_party_relation")].isNull() && m_responsible_party_relation_isValid;

    m_secondary_insurance_isValid = ::OpenAPI::fromJsonValue(m_secondary_insurance, json[QString("secondary_insurance")]);
    m_secondary_insurance_isSet = !json[QString("secondary_insurance")].isNull() && m_secondary_insurance_isValid;

    m_social_security_number_isValid = ::OpenAPI::fromJsonValue(m_social_security_number, json[QString("social_security_number")]);
    m_social_security_number_isSet = !json[QString("social_security_number")].isNull() && m_social_security_number_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;

    m_tertiary_insurance_isValid = ::OpenAPI::fromJsonValue(m_tertiary_insurance, json[QString("tertiary_insurance")]);
    m_tertiary_insurance_isSet = !json[QString("tertiary_insurance")].isNull() && m_tertiary_insurance_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updated_at")]);
    m_updated_at_isSet = !json[QString("updated_at")].isNull() && m_updated_at_isValid;

    m_workers_comp_insurance_isValid = ::OpenAPI::fromJsonValue(m_workers_comp_insurance, json[QString("workers_comp_insurance")]);
    m_workers_comp_insurance_isSet = !json[QString("workers_comp_insurance")].isNull() && m_workers_comp_insurance_isValid;

    m_zip_code_isValid = ::OpenAPI::fromJsonValue(m_zip_code, json[QString("zip_code")]);
    m_zip_code_isSet = !json[QString("zip_code")].isNull() && m_zip_code_isValid;
}

QString OAIPatient::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPatient::asJsonObject() const {
    QJsonObject obj;
    if (m_address_isSet) {
        obj.insert(QString("address"), ::OpenAPI::toJsonValue(m_address));
    }
    if (m_auto_accident_insurance.isSet()) {
        obj.insert(QString("auto_accident_insurance"), ::OpenAPI::toJsonValue(m_auto_accident_insurance));
    }
    if (m_cell_phone_isSet) {
        obj.insert(QString("cell_phone"), ::OpenAPI::toJsonValue(m_cell_phone));
    }
    if (m_chart_id_isSet) {
        obj.insert(QString("chart_id"), ::OpenAPI::toJsonValue(m_chart_id));
    }
    if (m_city_isSet) {
        obj.insert(QString("city"), ::OpenAPI::toJsonValue(m_city));
    }
    if (m_copay_isSet) {
        obj.insert(QString("copay"), ::OpenAPI::toJsonValue(m_copay));
    }
    if (m_custom_demographics.size() > 0) {
        obj.insert(QString("custom_demographics"), ::OpenAPI::toJsonValue(m_custom_demographics));
    }
    if (m_date_of_birth_isSet) {
        obj.insert(QString("date_of_birth"), ::OpenAPI::toJsonValue(m_date_of_birth));
    }
    if (m_date_of_first_appointment_isSet) {
        obj.insert(QString("date_of_first_appointment"), ::OpenAPI::toJsonValue(m_date_of_first_appointment));
    }
    if (m_date_of_last_appointment_isSet) {
        obj.insert(QString("date_of_last_appointment"), ::OpenAPI::toJsonValue(m_date_of_last_appointment));
    }
    if (m_default_pharmacy_isSet) {
        obj.insert(QString("default_pharmacy"), ::OpenAPI::toJsonValue(m_default_pharmacy));
    }
    if (m_disable_sms_messages_isSet) {
        obj.insert(QString("disable_sms_messages"), ::OpenAPI::toJsonValue(m_disable_sms_messages));
    }
    if (m_doctor_isSet) {
        obj.insert(QString("doctor"), ::OpenAPI::toJsonValue(m_doctor));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_emergency_contact_name_isSet) {
        obj.insert(QString("emergency_contact_name"), ::OpenAPI::toJsonValue(m_emergency_contact_name));
    }
    if (m_emergency_contact_phone_isSet) {
        obj.insert(QString("emergency_contact_phone"), ::OpenAPI::toJsonValue(m_emergency_contact_phone));
    }
    if (m_emergency_contact_relation_isSet) {
        obj.insert(QString("emergency_contact_relation"), ::OpenAPI::toJsonValue(m_emergency_contact_relation));
    }
    if (m_employer_isSet) {
        obj.insert(QString("employer"), ::OpenAPI::toJsonValue(m_employer));
    }
    if (m_employer_address_isSet) {
        obj.insert(QString("employer_address"), ::OpenAPI::toJsonValue(m_employer_address));
    }
    if (m_employer_city_isSet) {
        obj.insert(QString("employer_city"), ::OpenAPI::toJsonValue(m_employer_city));
    }
    if (m_employer_state_isSet) {
        obj.insert(QString("employer_state"), ::OpenAPI::toJsonValue(m_employer_state));
    }
    if (m_employer_zip_code_isSet) {
        obj.insert(QString("employer_zip_code"), ::OpenAPI::toJsonValue(m_employer_zip_code));
    }
    if (m_ethnicity_isSet) {
        obj.insert(QString("ethnicity"), ::OpenAPI::toJsonValue(m_ethnicity));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("first_name"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_gender_isSet) {
        obj.insert(QString("gender"), ::OpenAPI::toJsonValue(m_gender));
    }
    if (m_home_phone_isSet) {
        obj.insert(QString("home_phone"), ::OpenAPI::toJsonValue(m_home_phone));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("last_name"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_middle_name_isSet) {
        obj.insert(QString("middle_name"), ::OpenAPI::toJsonValue(m_middle_name));
    }
    if (m_nick_name_isSet) {
        obj.insert(QString("nick_name"), ::OpenAPI::toJsonValue(m_nick_name));
    }
    if (m_office_phone_isSet) {
        obj.insert(QString("office_phone"), ::OpenAPI::toJsonValue(m_office_phone));
    }
    if (m_offices.size() > 0) {
        obj.insert(QString("offices"), ::OpenAPI::toJsonValue(m_offices));
    }
    if (m_patient_flags.size() > 0) {
        obj.insert(QString("patient_flags"), ::OpenAPI::toJsonValue(m_patient_flags));
    }
    if (m_patient_flags_attached.size() > 0) {
        obj.insert(QString("patient_flags_attached"), ::OpenAPI::toJsonValue(m_patient_flags_attached));
    }
    if (m_patient_payment_profile_isSet) {
        obj.insert(QString("patient_payment_profile"), ::OpenAPI::toJsonValue(m_patient_payment_profile));
    }
    if (m_patient_photo_isSet) {
        obj.insert(QString("patient_photo"), ::OpenAPI::toJsonValue(m_patient_photo));
    }
    if (m_patient_photo_date_isSet) {
        obj.insert(QString("patient_photo_date"), ::OpenAPI::toJsonValue(m_patient_photo_date));
    }
    if (m_patient_status_isSet) {
        obj.insert(QString("patient_status"), ::OpenAPI::toJsonValue(m_patient_status));
    }
    if (m_preferred_language_isSet) {
        obj.insert(QString("preferred_language"), ::OpenAPI::toJsonValue(m_preferred_language));
    }
    if (m_primary_care_physician_isSet) {
        obj.insert(QString("primary_care_physician"), ::OpenAPI::toJsonValue(m_primary_care_physician));
    }
    if (m_primary_insurance.isSet()) {
        obj.insert(QString("primary_insurance"), ::OpenAPI::toJsonValue(m_primary_insurance));
    }
    if (m_race_isSet) {
        obj.insert(QString("race"), ::OpenAPI::toJsonValue(m_race));
    }
    if (m_referring_doctor.isSet()) {
        obj.insert(QString("referring_doctor"), ::OpenAPI::toJsonValue(m_referring_doctor));
    }
    if (m_referring_source_isSet) {
        obj.insert(QString("referring_source"), ::OpenAPI::toJsonValue(m_referring_source));
    }
    if (m_responsible_party_email_isSet) {
        obj.insert(QString("responsible_party_email"), ::OpenAPI::toJsonValue(m_responsible_party_email));
    }
    if (m_responsible_party_name_isSet) {
        obj.insert(QString("responsible_party_name"), ::OpenAPI::toJsonValue(m_responsible_party_name));
    }
    if (m_responsible_party_phone_isSet) {
        obj.insert(QString("responsible_party_phone"), ::OpenAPI::toJsonValue(m_responsible_party_phone));
    }
    if (m_responsible_party_relation_isSet) {
        obj.insert(QString("responsible_party_relation"), ::OpenAPI::toJsonValue(m_responsible_party_relation));
    }
    if (m_secondary_insurance.isSet()) {
        obj.insert(QString("secondary_insurance"), ::OpenAPI::toJsonValue(m_secondary_insurance));
    }
    if (m_social_security_number_isSet) {
        obj.insert(QString("social_security_number"), ::OpenAPI::toJsonValue(m_social_security_number));
    }
    if (m_state_isSet) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    if (m_tertiary_insurance.isSet()) {
        obj.insert(QString("tertiary_insurance"), ::OpenAPI::toJsonValue(m_tertiary_insurance));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updated_at"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    if (m_workers_comp_insurance.isSet()) {
        obj.insert(QString("workers_comp_insurance"), ::OpenAPI::toJsonValue(m_workers_comp_insurance));
    }
    if (m_zip_code_isSet) {
        obj.insert(QString("zip_code"), ::OpenAPI::toJsonValue(m_zip_code));
    }
    return obj;
}

QString OAIPatient::getAddress() const {
    return m_address;
}
void OAIPatient::setAddress(const QString &address) {
    m_address = address;
    m_address_isSet = true;
}

bool OAIPatient::is_address_Set() const{
    return m_address_isSet;
}

bool OAIPatient::is_address_Valid() const{
    return m_address_isValid;
}

OAIAutoAccidentInsurance OAIPatient::getAutoAccidentInsurance() const {
    return m_auto_accident_insurance;
}
void OAIPatient::setAutoAccidentInsurance(const OAIAutoAccidentInsurance &auto_accident_insurance) {
    m_auto_accident_insurance = auto_accident_insurance;
    m_auto_accident_insurance_isSet = true;
}

bool OAIPatient::is_auto_accident_insurance_Set() const{
    return m_auto_accident_insurance_isSet;
}

bool OAIPatient::is_auto_accident_insurance_Valid() const{
    return m_auto_accident_insurance_isValid;
}

QString OAIPatient::getCellPhone() const {
    return m_cell_phone;
}
void OAIPatient::setCellPhone(const QString &cell_phone) {
    m_cell_phone = cell_phone;
    m_cell_phone_isSet = true;
}

bool OAIPatient::is_cell_phone_Set() const{
    return m_cell_phone_isSet;
}

bool OAIPatient::is_cell_phone_Valid() const{
    return m_cell_phone_isValid;
}

QString OAIPatient::getChartId() const {
    return m_chart_id;
}
void OAIPatient::setChartId(const QString &chart_id) {
    m_chart_id = chart_id;
    m_chart_id_isSet = true;
}

bool OAIPatient::is_chart_id_Set() const{
    return m_chart_id_isSet;
}

bool OAIPatient::is_chart_id_Valid() const{
    return m_chart_id_isValid;
}

QString OAIPatient::getCity() const {
    return m_city;
}
void OAIPatient::setCity(const QString &city) {
    m_city = city;
    m_city_isSet = true;
}

bool OAIPatient::is_city_Set() const{
    return m_city_isSet;
}

bool OAIPatient::is_city_Valid() const{
    return m_city_isValid;
}

QString OAIPatient::getCopay() const {
    return m_copay;
}
void OAIPatient::setCopay(const QString &copay) {
    m_copay = copay;
    m_copay_isSet = true;
}

bool OAIPatient::is_copay_Set() const{
    return m_copay_isSet;
}

bool OAIPatient::is_copay_Valid() const{
    return m_copay_isValid;
}

QList<OAICustomPatientFieldValue> OAIPatient::getCustomDemographics() const {
    return m_custom_demographics;
}
void OAIPatient::setCustomDemographics(const QList<OAICustomPatientFieldValue> &custom_demographics) {
    m_custom_demographics = custom_demographics;
    m_custom_demographics_isSet = true;
}

bool OAIPatient::is_custom_demographics_Set() const{
    return m_custom_demographics_isSet;
}

bool OAIPatient::is_custom_demographics_Valid() const{
    return m_custom_demographics_isValid;
}

QString OAIPatient::getDateOfBirth() const {
    return m_date_of_birth;
}
void OAIPatient::setDateOfBirth(const QString &date_of_birth) {
    m_date_of_birth = date_of_birth;
    m_date_of_birth_isSet = true;
}

bool OAIPatient::is_date_of_birth_Set() const{
    return m_date_of_birth_isSet;
}

bool OAIPatient::is_date_of_birth_Valid() const{
    return m_date_of_birth_isValid;
}

QString OAIPatient::getDateOfFirstAppointment() const {
    return m_date_of_first_appointment;
}
void OAIPatient::setDateOfFirstAppointment(const QString &date_of_first_appointment) {
    m_date_of_first_appointment = date_of_first_appointment;
    m_date_of_first_appointment_isSet = true;
}

bool OAIPatient::is_date_of_first_appointment_Set() const{
    return m_date_of_first_appointment_isSet;
}

bool OAIPatient::is_date_of_first_appointment_Valid() const{
    return m_date_of_first_appointment_isValid;
}

QString OAIPatient::getDateOfLastAppointment() const {
    return m_date_of_last_appointment;
}
void OAIPatient::setDateOfLastAppointment(const QString &date_of_last_appointment) {
    m_date_of_last_appointment = date_of_last_appointment;
    m_date_of_last_appointment_isSet = true;
}

bool OAIPatient::is_date_of_last_appointment_Set() const{
    return m_date_of_last_appointment_isSet;
}

bool OAIPatient::is_date_of_last_appointment_Valid() const{
    return m_date_of_last_appointment_isValid;
}

QString OAIPatient::getDefaultPharmacy() const {
    return m_default_pharmacy;
}
void OAIPatient::setDefaultPharmacy(const QString &default_pharmacy) {
    m_default_pharmacy = default_pharmacy;
    m_default_pharmacy_isSet = true;
}

bool OAIPatient::is_default_pharmacy_Set() const{
    return m_default_pharmacy_isSet;
}

bool OAIPatient::is_default_pharmacy_Valid() const{
    return m_default_pharmacy_isValid;
}

bool OAIPatient::isDisableSmsMessages() const {
    return m_disable_sms_messages;
}
void OAIPatient::setDisableSmsMessages(const bool &disable_sms_messages) {
    m_disable_sms_messages = disable_sms_messages;
    m_disable_sms_messages_isSet = true;
}

bool OAIPatient::is_disable_sms_messages_Set() const{
    return m_disable_sms_messages_isSet;
}

bool OAIPatient::is_disable_sms_messages_Valid() const{
    return m_disable_sms_messages_isValid;
}

qint32 OAIPatient::getDoctor() const {
    return m_doctor;
}
void OAIPatient::setDoctor(const qint32 &doctor) {
    m_doctor = doctor;
    m_doctor_isSet = true;
}

bool OAIPatient::is_doctor_Set() const{
    return m_doctor_isSet;
}

bool OAIPatient::is_doctor_Valid() const{
    return m_doctor_isValid;
}

QString OAIPatient::getEmail() const {
    return m_email;
}
void OAIPatient::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIPatient::is_email_Set() const{
    return m_email_isSet;
}

bool OAIPatient::is_email_Valid() const{
    return m_email_isValid;
}

QString OAIPatient::getEmergencyContactName() const {
    return m_emergency_contact_name;
}
void OAIPatient::setEmergencyContactName(const QString &emergency_contact_name) {
    m_emergency_contact_name = emergency_contact_name;
    m_emergency_contact_name_isSet = true;
}

bool OAIPatient::is_emergency_contact_name_Set() const{
    return m_emergency_contact_name_isSet;
}

bool OAIPatient::is_emergency_contact_name_Valid() const{
    return m_emergency_contact_name_isValid;
}

QString OAIPatient::getEmergencyContactPhone() const {
    return m_emergency_contact_phone;
}
void OAIPatient::setEmergencyContactPhone(const QString &emergency_contact_phone) {
    m_emergency_contact_phone = emergency_contact_phone;
    m_emergency_contact_phone_isSet = true;
}

bool OAIPatient::is_emergency_contact_phone_Set() const{
    return m_emergency_contact_phone_isSet;
}

bool OAIPatient::is_emergency_contact_phone_Valid() const{
    return m_emergency_contact_phone_isValid;
}

QString OAIPatient::getEmergencyContactRelation() const {
    return m_emergency_contact_relation;
}
void OAIPatient::setEmergencyContactRelation(const QString &emergency_contact_relation) {
    m_emergency_contact_relation = emergency_contact_relation;
    m_emergency_contact_relation_isSet = true;
}

bool OAIPatient::is_emergency_contact_relation_Set() const{
    return m_emergency_contact_relation_isSet;
}

bool OAIPatient::is_emergency_contact_relation_Valid() const{
    return m_emergency_contact_relation_isValid;
}

QString OAIPatient::getEmployer() const {
    return m_employer;
}
void OAIPatient::setEmployer(const QString &employer) {
    m_employer = employer;
    m_employer_isSet = true;
}

bool OAIPatient::is_employer_Set() const{
    return m_employer_isSet;
}

bool OAIPatient::is_employer_Valid() const{
    return m_employer_isValid;
}

QString OAIPatient::getEmployerAddress() const {
    return m_employer_address;
}
void OAIPatient::setEmployerAddress(const QString &employer_address) {
    m_employer_address = employer_address;
    m_employer_address_isSet = true;
}

bool OAIPatient::is_employer_address_Set() const{
    return m_employer_address_isSet;
}

bool OAIPatient::is_employer_address_Valid() const{
    return m_employer_address_isValid;
}

QString OAIPatient::getEmployerCity() const {
    return m_employer_city;
}
void OAIPatient::setEmployerCity(const QString &employer_city) {
    m_employer_city = employer_city;
    m_employer_city_isSet = true;
}

bool OAIPatient::is_employer_city_Set() const{
    return m_employer_city_isSet;
}

bool OAIPatient::is_employer_city_Valid() const{
    return m_employer_city_isValid;
}

QString OAIPatient::getEmployerState() const {
    return m_employer_state;
}
void OAIPatient::setEmployerState(const QString &employer_state) {
    m_employer_state = employer_state;
    m_employer_state_isSet = true;
}

bool OAIPatient::is_employer_state_Set() const{
    return m_employer_state_isSet;
}

bool OAIPatient::is_employer_state_Valid() const{
    return m_employer_state_isValid;
}

QString OAIPatient::getEmployerZipCode() const {
    return m_employer_zip_code;
}
void OAIPatient::setEmployerZipCode(const QString &employer_zip_code) {
    m_employer_zip_code = employer_zip_code;
    m_employer_zip_code_isSet = true;
}

bool OAIPatient::is_employer_zip_code_Set() const{
    return m_employer_zip_code_isSet;
}

bool OAIPatient::is_employer_zip_code_Valid() const{
    return m_employer_zip_code_isValid;
}

QString OAIPatient::getEthnicity() const {
    return m_ethnicity;
}
void OAIPatient::setEthnicity(const QString &ethnicity) {
    m_ethnicity = ethnicity;
    m_ethnicity_isSet = true;
}

bool OAIPatient::is_ethnicity_Set() const{
    return m_ethnicity_isSet;
}

bool OAIPatient::is_ethnicity_Valid() const{
    return m_ethnicity_isValid;
}

QString OAIPatient::getFirstName() const {
    return m_first_name;
}
void OAIPatient::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAIPatient::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAIPatient::is_first_name_Valid() const{
    return m_first_name_isValid;
}

QString OAIPatient::getGender() const {
    return m_gender;
}
void OAIPatient::setGender(const QString &gender) {
    m_gender = gender;
    m_gender_isSet = true;
}

bool OAIPatient::is_gender_Set() const{
    return m_gender_isSet;
}

bool OAIPatient::is_gender_Valid() const{
    return m_gender_isValid;
}

QString OAIPatient::getHomePhone() const {
    return m_home_phone;
}
void OAIPatient::setHomePhone(const QString &home_phone) {
    m_home_phone = home_phone;
    m_home_phone_isSet = true;
}

bool OAIPatient::is_home_phone_Set() const{
    return m_home_phone_isSet;
}

bool OAIPatient::is_home_phone_Valid() const{
    return m_home_phone_isValid;
}

qint32 OAIPatient::getId() const {
    return m_id;
}
void OAIPatient::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIPatient::is_id_Set() const{
    return m_id_isSet;
}

bool OAIPatient::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIPatient::getLastName() const {
    return m_last_name;
}
void OAIPatient::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAIPatient::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAIPatient::is_last_name_Valid() const{
    return m_last_name_isValid;
}

QString OAIPatient::getMiddleName() const {
    return m_middle_name;
}
void OAIPatient::setMiddleName(const QString &middle_name) {
    m_middle_name = middle_name;
    m_middle_name_isSet = true;
}

bool OAIPatient::is_middle_name_Set() const{
    return m_middle_name_isSet;
}

bool OAIPatient::is_middle_name_Valid() const{
    return m_middle_name_isValid;
}

QString OAIPatient::getNickName() const {
    return m_nick_name;
}
void OAIPatient::setNickName(const QString &nick_name) {
    m_nick_name = nick_name;
    m_nick_name_isSet = true;
}

bool OAIPatient::is_nick_name_Set() const{
    return m_nick_name_isSet;
}

bool OAIPatient::is_nick_name_Valid() const{
    return m_nick_name_isValid;
}

QString OAIPatient::getOfficePhone() const {
    return m_office_phone;
}
void OAIPatient::setOfficePhone(const QString &office_phone) {
    m_office_phone = office_phone;
    m_office_phone_isSet = true;
}

bool OAIPatient::is_office_phone_Set() const{
    return m_office_phone_isSet;
}

bool OAIPatient::is_office_phone_Valid() const{
    return m_office_phone_isValid;
}

QList<qint32> OAIPatient::getOffices() const {
    return m_offices;
}
void OAIPatient::setOffices(const QList<qint32> &offices) {
    m_offices = offices;
    m_offices_isSet = true;
}

bool OAIPatient::is_offices_Set() const{
    return m_offices_isSet;
}

bool OAIPatient::is_offices_Valid() const{
    return m_offices_isValid;
}

QList<OAIPatientFlagType_1> OAIPatient::getPatientFlags() const {
    return m_patient_flags;
}
void OAIPatient::setPatientFlags(const QList<OAIPatientFlagType_1> &patient_flags) {
    m_patient_flags = patient_flags;
    m_patient_flags_isSet = true;
}

bool OAIPatient::is_patient_flags_Set() const{
    return m_patient_flags_isSet;
}

bool OAIPatient::is_patient_flags_Valid() const{
    return m_patient_flags_isValid;
}

QList<OAIPatientFlag> OAIPatient::getPatientFlagsAttached() const {
    return m_patient_flags_attached;
}
void OAIPatient::setPatientFlagsAttached(const QList<OAIPatientFlag> &patient_flags_attached) {
    m_patient_flags_attached = patient_flags_attached;
    m_patient_flags_attached_isSet = true;
}

bool OAIPatient::is_patient_flags_attached_Set() const{
    return m_patient_flags_attached_isSet;
}

bool OAIPatient::is_patient_flags_attached_Valid() const{
    return m_patient_flags_attached_isValid;
}

QString OAIPatient::getPatientPaymentProfile() const {
    return m_patient_payment_profile;
}
void OAIPatient::setPatientPaymentProfile(const QString &patient_payment_profile) {
    m_patient_payment_profile = patient_payment_profile;
    m_patient_payment_profile_isSet = true;
}

bool OAIPatient::is_patient_payment_profile_Set() const{
    return m_patient_payment_profile_isSet;
}

bool OAIPatient::is_patient_payment_profile_Valid() const{
    return m_patient_payment_profile_isValid;
}

QString OAIPatient::getPatientPhoto() const {
    return m_patient_photo;
}
void OAIPatient::setPatientPhoto(const QString &patient_photo) {
    m_patient_photo = patient_photo;
    m_patient_photo_isSet = true;
}

bool OAIPatient::is_patient_photo_Set() const{
    return m_patient_photo_isSet;
}

bool OAIPatient::is_patient_photo_Valid() const{
    return m_patient_photo_isValid;
}

QString OAIPatient::getPatientPhotoDate() const {
    return m_patient_photo_date;
}
void OAIPatient::setPatientPhotoDate(const QString &patient_photo_date) {
    m_patient_photo_date = patient_photo_date;
    m_patient_photo_date_isSet = true;
}

bool OAIPatient::is_patient_photo_date_Set() const{
    return m_patient_photo_date_isSet;
}

bool OAIPatient::is_patient_photo_date_Valid() const{
    return m_patient_photo_date_isValid;
}

QString OAIPatient::getPatientStatus() const {
    return m_patient_status;
}
void OAIPatient::setPatientStatus(const QString &patient_status) {
    m_patient_status = patient_status;
    m_patient_status_isSet = true;
}

bool OAIPatient::is_patient_status_Set() const{
    return m_patient_status_isSet;
}

bool OAIPatient::is_patient_status_Valid() const{
    return m_patient_status_isValid;
}

QString OAIPatient::getPreferredLanguage() const {
    return m_preferred_language;
}
void OAIPatient::setPreferredLanguage(const QString &preferred_language) {
    m_preferred_language = preferred_language;
    m_preferred_language_isSet = true;
}

bool OAIPatient::is_preferred_language_Set() const{
    return m_preferred_language_isSet;
}

bool OAIPatient::is_preferred_language_Valid() const{
    return m_preferred_language_isValid;
}

QString OAIPatient::getPrimaryCarePhysician() const {
    return m_primary_care_physician;
}
void OAIPatient::setPrimaryCarePhysician(const QString &primary_care_physician) {
    m_primary_care_physician = primary_care_physician;
    m_primary_care_physician_isSet = true;
}

bool OAIPatient::is_primary_care_physician_Set() const{
    return m_primary_care_physician_isSet;
}

bool OAIPatient::is_primary_care_physician_Valid() const{
    return m_primary_care_physician_isValid;
}

OAIPrimaryInsurance OAIPatient::getPrimaryInsurance() const {
    return m_primary_insurance;
}
void OAIPatient::setPrimaryInsurance(const OAIPrimaryInsurance &primary_insurance) {
    m_primary_insurance = primary_insurance;
    m_primary_insurance_isSet = true;
}

bool OAIPatient::is_primary_insurance_Set() const{
    return m_primary_insurance_isSet;
}

bool OAIPatient::is_primary_insurance_Valid() const{
    return m_primary_insurance_isValid;
}

QString OAIPatient::getRace() const {
    return m_race;
}
void OAIPatient::setRace(const QString &race) {
    m_race = race;
    m_race_isSet = true;
}

bool OAIPatient::is_race_Set() const{
    return m_race_isSet;
}

bool OAIPatient::is_race_Valid() const{
    return m_race_isValid;
}

OAIPatient_1 OAIPatient::getReferringDoctor() const {
    return m_referring_doctor;
}
void OAIPatient::setReferringDoctor(const OAIPatient_1 &referring_doctor) {
    m_referring_doctor = referring_doctor;
    m_referring_doctor_isSet = true;
}

bool OAIPatient::is_referring_doctor_Set() const{
    return m_referring_doctor_isSet;
}

bool OAIPatient::is_referring_doctor_Valid() const{
    return m_referring_doctor_isValid;
}

QString OAIPatient::getReferringSource() const {
    return m_referring_source;
}
void OAIPatient::setReferringSource(const QString &referring_source) {
    m_referring_source = referring_source;
    m_referring_source_isSet = true;
}

bool OAIPatient::is_referring_source_Set() const{
    return m_referring_source_isSet;
}

bool OAIPatient::is_referring_source_Valid() const{
    return m_referring_source_isValid;
}

QString OAIPatient::getResponsiblePartyEmail() const {
    return m_responsible_party_email;
}
void OAIPatient::setResponsiblePartyEmail(const QString &responsible_party_email) {
    m_responsible_party_email = responsible_party_email;
    m_responsible_party_email_isSet = true;
}

bool OAIPatient::is_responsible_party_email_Set() const{
    return m_responsible_party_email_isSet;
}

bool OAIPatient::is_responsible_party_email_Valid() const{
    return m_responsible_party_email_isValid;
}

QString OAIPatient::getResponsiblePartyName() const {
    return m_responsible_party_name;
}
void OAIPatient::setResponsiblePartyName(const QString &responsible_party_name) {
    m_responsible_party_name = responsible_party_name;
    m_responsible_party_name_isSet = true;
}

bool OAIPatient::is_responsible_party_name_Set() const{
    return m_responsible_party_name_isSet;
}

bool OAIPatient::is_responsible_party_name_Valid() const{
    return m_responsible_party_name_isValid;
}

QString OAIPatient::getResponsiblePartyPhone() const {
    return m_responsible_party_phone;
}
void OAIPatient::setResponsiblePartyPhone(const QString &responsible_party_phone) {
    m_responsible_party_phone = responsible_party_phone;
    m_responsible_party_phone_isSet = true;
}

bool OAIPatient::is_responsible_party_phone_Set() const{
    return m_responsible_party_phone_isSet;
}

bool OAIPatient::is_responsible_party_phone_Valid() const{
    return m_responsible_party_phone_isValid;
}

QString OAIPatient::getResponsiblePartyRelation() const {
    return m_responsible_party_relation;
}
void OAIPatient::setResponsiblePartyRelation(const QString &responsible_party_relation) {
    m_responsible_party_relation = responsible_party_relation;
    m_responsible_party_relation_isSet = true;
}

bool OAIPatient::is_responsible_party_relation_Set() const{
    return m_responsible_party_relation_isSet;
}

bool OAIPatient::is_responsible_party_relation_Valid() const{
    return m_responsible_party_relation_isValid;
}

OAISecondaryInsurance OAIPatient::getSecondaryInsurance() const {
    return m_secondary_insurance;
}
void OAIPatient::setSecondaryInsurance(const OAISecondaryInsurance &secondary_insurance) {
    m_secondary_insurance = secondary_insurance;
    m_secondary_insurance_isSet = true;
}

bool OAIPatient::is_secondary_insurance_Set() const{
    return m_secondary_insurance_isSet;
}

bool OAIPatient::is_secondary_insurance_Valid() const{
    return m_secondary_insurance_isValid;
}

QString OAIPatient::getSocialSecurityNumber() const {
    return m_social_security_number;
}
void OAIPatient::setSocialSecurityNumber(const QString &social_security_number) {
    m_social_security_number = social_security_number;
    m_social_security_number_isSet = true;
}

bool OAIPatient::is_social_security_number_Set() const{
    return m_social_security_number_isSet;
}

bool OAIPatient::is_social_security_number_Valid() const{
    return m_social_security_number_isValid;
}

QString OAIPatient::getState() const {
    return m_state;
}
void OAIPatient::setState(const QString &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIPatient::is_state_Set() const{
    return m_state_isSet;
}

bool OAIPatient::is_state_Valid() const{
    return m_state_isValid;
}

OAITertiaryInsurance OAIPatient::getTertiaryInsurance() const {
    return m_tertiary_insurance;
}
void OAIPatient::setTertiaryInsurance(const OAITertiaryInsurance &tertiary_insurance) {
    m_tertiary_insurance = tertiary_insurance;
    m_tertiary_insurance_isSet = true;
}

bool OAIPatient::is_tertiary_insurance_Set() const{
    return m_tertiary_insurance_isSet;
}

bool OAIPatient::is_tertiary_insurance_Valid() const{
    return m_tertiary_insurance_isValid;
}

QString OAIPatient::getUpdatedAt() const {
    return m_updated_at;
}
void OAIPatient::setUpdatedAt(const QString &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIPatient::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIPatient::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

OAIWorkerCompInsurance OAIPatient::getWorkersCompInsurance() const {
    return m_workers_comp_insurance;
}
void OAIPatient::setWorkersCompInsurance(const OAIWorkerCompInsurance &workers_comp_insurance) {
    m_workers_comp_insurance = workers_comp_insurance;
    m_workers_comp_insurance_isSet = true;
}

bool OAIPatient::is_workers_comp_insurance_Set() const{
    return m_workers_comp_insurance_isSet;
}

bool OAIPatient::is_workers_comp_insurance_Valid() const{
    return m_workers_comp_insurance_isValid;
}

QString OAIPatient::getZipCode() const {
    return m_zip_code;
}
void OAIPatient::setZipCode(const QString &zip_code) {
    m_zip_code = zip_code;
    m_zip_code_isSet = true;
}

bool OAIPatient::is_zip_code_Set() const{
    return m_zip_code_isSet;
}

bool OAIPatient::is_zip_code_Valid() const{
    return m_zip_code_isValid;
}

bool OAIPatient::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_auto_accident_insurance.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_cell_phone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_chart_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_copay_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_demographics.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_of_birth_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_of_first_appointment_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_of_last_appointment_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_default_pharmacy_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_disable_sms_messages_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_doctor_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_emergency_contact_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_emergency_contact_phone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_emergency_contact_relation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_employer_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_employer_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_employer_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_employer_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_employer_zip_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ethnicity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gender_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_home_phone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_middle_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_nick_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_office_phone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_offices.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_patient_flags.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_patient_flags_attached.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_patient_payment_profile_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_patient_photo_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_patient_photo_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_patient_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_preferred_language_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_primary_care_physician_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_primary_insurance.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_race_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_referring_doctor.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_referring_source_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_responsible_party_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_responsible_party_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_responsible_party_phone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_responsible_party_relation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_secondary_insurance.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_social_security_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tertiary_insurance.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_workers_comp_insurance.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_zip_code_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPatient::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_doctor_isValid && m_gender_isValid && true;
}

} // namespace OpenAPI
