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

#include "OAIPatientVaccineRecord.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPatientVaccineRecord::OAIPatientVaccineRecord(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPatientVaccineRecord::OAIPatientVaccineRecord() {
    this->initializeModel();
}

OAIPatientVaccineRecord::~OAIPatientVaccineRecord() {}

void OAIPatientVaccineRecord::initializeModel() {

    m_administered_at_isSet = false;
    m_administered_at_isValid = false;

    m_administered_by_isSet = false;
    m_administered_by_isValid = false;

    m_administration_start_isSet = false;
    m_administration_start_isValid = false;

    m_amount_isSet = false;
    m_amount_isValid = false;

    m_comments_isSet = false;
    m_comments_isValid = false;

    m_completion_status_isSet = false;
    m_completion_status_isValid = false;

    m_consent_form_isSet = false;
    m_consent_form_isValid = false;

    m_cpt_code_isSet = false;
    m_cpt_code_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_cvx_code_isSet = false;
    m_cvx_code_isValid = false;

    m_doses_isSet = false;
    m_doses_isValid = false;

    m_entered_by_isSet = false;
    m_entered_by_isValid = false;

    m_funding_eligibility_isSet = false;
    m_funding_eligibility_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_next_dose_date_isSet = false;
    m_next_dose_date_isValid = false;

    m_observed_immunity_isSet = false;
    m_observed_immunity_isValid = false;

    m_ordering_doctor_isSet = false;
    m_ordering_doctor_isValid = false;

    m_patient_isSet = false;
    m_patient_isValid = false;

    m_record_source_isSet = false;
    m_record_source_isValid = false;

    m_route_isSet = false;
    m_route_isValid = false;

    m_site_isSet = false;
    m_site_isValid = false;

    m_units_isSet = false;
    m_units_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_vaccine_inventory_isSet = false;
    m_vaccine_inventory_isValid = false;

    m_vis_isSet = false;
    m_vis_isValid = false;
}

void OAIPatientVaccineRecord::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPatientVaccineRecord::fromJsonObject(QJsonObject json) {

    m_administered_at_isValid = ::OpenAPI::fromJsonValue(m_administered_at, json[QString("administered_at")]);
    m_administered_at_isSet = !json[QString("administered_at")].isNull() && m_administered_at_isValid;

    m_administered_by_isValid = ::OpenAPI::fromJsonValue(m_administered_by, json[QString("administered_by")]);
    m_administered_by_isSet = !json[QString("administered_by")].isNull() && m_administered_by_isValid;

    m_administration_start_isValid = ::OpenAPI::fromJsonValue(m_administration_start, json[QString("administration_start")]);
    m_administration_start_isSet = !json[QString("administration_start")].isNull() && m_administration_start_isValid;

    m_amount_isValid = ::OpenAPI::fromJsonValue(m_amount, json[QString("amount")]);
    m_amount_isSet = !json[QString("amount")].isNull() && m_amount_isValid;

    m_comments_isValid = ::OpenAPI::fromJsonValue(m_comments, json[QString("comments")]);
    m_comments_isSet = !json[QString("comments")].isNull() && m_comments_isValid;

    m_completion_status_isValid = ::OpenAPI::fromJsonValue(m_completion_status, json[QString("completion_status")]);
    m_completion_status_isSet = !json[QString("completion_status")].isNull() && m_completion_status_isValid;

    m_consent_form_isValid = ::OpenAPI::fromJsonValue(m_consent_form, json[QString("consent_form")]);
    m_consent_form_isSet = !json[QString("consent_form")].isNull() && m_consent_form_isValid;

    m_cpt_code_isValid = ::OpenAPI::fromJsonValue(m_cpt_code, json[QString("cpt_code")]);
    m_cpt_code_isSet = !json[QString("cpt_code")].isNull() && m_cpt_code_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_cvx_code_isValid = ::OpenAPI::fromJsonValue(m_cvx_code, json[QString("cvx_code")]);
    m_cvx_code_isSet = !json[QString("cvx_code")].isNull() && m_cvx_code_isValid;

    m_doses_isValid = ::OpenAPI::fromJsonValue(m_doses, json[QString("doses")]);
    m_doses_isSet = !json[QString("doses")].isNull() && m_doses_isValid;

    m_entered_by_isValid = ::OpenAPI::fromJsonValue(m_entered_by, json[QString("entered_by")]);
    m_entered_by_isSet = !json[QString("entered_by")].isNull() && m_entered_by_isValid;

    m_funding_eligibility_isValid = ::OpenAPI::fromJsonValue(m_funding_eligibility, json[QString("funding_eligibility")]);
    m_funding_eligibility_isSet = !json[QString("funding_eligibility")].isNull() && m_funding_eligibility_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_next_dose_date_isValid = ::OpenAPI::fromJsonValue(m_next_dose_date, json[QString("next_dose_date")]);
    m_next_dose_date_isSet = !json[QString("next_dose_date")].isNull() && m_next_dose_date_isValid;

    m_observed_immunity_isValid = ::OpenAPI::fromJsonValue(m_observed_immunity, json[QString("observed_immunity")]);
    m_observed_immunity_isSet = !json[QString("observed_immunity")].isNull() && m_observed_immunity_isValid;

    m_ordering_doctor_isValid = ::OpenAPI::fromJsonValue(m_ordering_doctor, json[QString("ordering_doctor")]);
    m_ordering_doctor_isSet = !json[QString("ordering_doctor")].isNull() && m_ordering_doctor_isValid;

    m_patient_isValid = ::OpenAPI::fromJsonValue(m_patient, json[QString("patient")]);
    m_patient_isSet = !json[QString("patient")].isNull() && m_patient_isValid;

    m_record_source_isValid = ::OpenAPI::fromJsonValue(m_record_source, json[QString("record_source")]);
    m_record_source_isSet = !json[QString("record_source")].isNull() && m_record_source_isValid;

    m_route_isValid = ::OpenAPI::fromJsonValue(m_route, json[QString("route")]);
    m_route_isSet = !json[QString("route")].isNull() && m_route_isValid;

    m_site_isValid = ::OpenAPI::fromJsonValue(m_site, json[QString("site")]);
    m_site_isSet = !json[QString("site")].isNull() && m_site_isValid;

    m_units_isValid = ::OpenAPI::fromJsonValue(m_units, json[QString("units")]);
    m_units_isSet = !json[QString("units")].isNull() && m_units_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updated_at")]);
    m_updated_at_isSet = !json[QString("updated_at")].isNull() && m_updated_at_isValid;

    m_vaccine_inventory_isValid = ::OpenAPI::fromJsonValue(m_vaccine_inventory, json[QString("vaccine_inventory")]);
    m_vaccine_inventory_isSet = !json[QString("vaccine_inventory")].isNull() && m_vaccine_inventory_isValid;

    m_vis_isValid = ::OpenAPI::fromJsonValue(m_vis, json[QString("vis")]);
    m_vis_isSet = !json[QString("vis")].isNull() && m_vis_isValid;
}

QString OAIPatientVaccineRecord::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPatientVaccineRecord::asJsonObject() const {
    QJsonObject obj;
    if (m_administered_at_isSet) {
        obj.insert(QString("administered_at"), ::OpenAPI::toJsonValue(m_administered_at));
    }
    if (m_administered_by_isSet) {
        obj.insert(QString("administered_by"), ::OpenAPI::toJsonValue(m_administered_by));
    }
    if (m_administration_start_isSet) {
        obj.insert(QString("administration_start"), ::OpenAPI::toJsonValue(m_administration_start));
    }
    if (m_amount_isSet) {
        obj.insert(QString("amount"), ::OpenAPI::toJsonValue(m_amount));
    }
    if (m_comments_isSet) {
        obj.insert(QString("comments"), ::OpenAPI::toJsonValue(m_comments));
    }
    if (m_completion_status_isSet) {
        obj.insert(QString("completion_status"), ::OpenAPI::toJsonValue(m_completion_status));
    }
    if (m_consent_form_isSet) {
        obj.insert(QString("consent_form"), ::OpenAPI::toJsonValue(m_consent_form));
    }
    if (m_cpt_code_isSet) {
        obj.insert(QString("cpt_code"), ::OpenAPI::toJsonValue(m_cpt_code));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("created_at"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_cvx_code_isSet) {
        obj.insert(QString("cvx_code"), ::OpenAPI::toJsonValue(m_cvx_code));
    }
    if (m_doses.size() > 0) {
        obj.insert(QString("doses"), ::OpenAPI::toJsonValue(m_doses));
    }
    if (m_entered_by_isSet) {
        obj.insert(QString("entered_by"), ::OpenAPI::toJsonValue(m_entered_by));
    }
    if (m_funding_eligibility_isSet) {
        obj.insert(QString("funding_eligibility"), ::OpenAPI::toJsonValue(m_funding_eligibility));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_next_dose_date_isSet) {
        obj.insert(QString("next_dose_date"), ::OpenAPI::toJsonValue(m_next_dose_date));
    }
    if (m_observed_immunity_isSet) {
        obj.insert(QString("observed_immunity"), ::OpenAPI::toJsonValue(m_observed_immunity));
    }
    if (m_ordering_doctor_isSet) {
        obj.insert(QString("ordering_doctor"), ::OpenAPI::toJsonValue(m_ordering_doctor));
    }
    if (m_patient_isSet) {
        obj.insert(QString("patient"), ::OpenAPI::toJsonValue(m_patient));
    }
    if (m_record_source_isSet) {
        obj.insert(QString("record_source"), ::OpenAPI::toJsonValue(m_record_source));
    }
    if (m_route_isSet) {
        obj.insert(QString("route"), ::OpenAPI::toJsonValue(m_route));
    }
    if (m_site_isSet) {
        obj.insert(QString("site"), ::OpenAPI::toJsonValue(m_site));
    }
    if (m_units_isSet) {
        obj.insert(QString("units"), ::OpenAPI::toJsonValue(m_units));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updated_at"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    if (m_vaccine_inventory_isSet) {
        obj.insert(QString("vaccine_inventory"), ::OpenAPI::toJsonValue(m_vaccine_inventory));
    }
    if (m_vis_isSet) {
        obj.insert(QString("vis"), ::OpenAPI::toJsonValue(m_vis));
    }
    return obj;
}

qint32 OAIPatientVaccineRecord::getAdministeredAt() const {
    return m_administered_at;
}
void OAIPatientVaccineRecord::setAdministeredAt(const qint32 &administered_at) {
    m_administered_at = administered_at;
    m_administered_at_isSet = true;
}

bool OAIPatientVaccineRecord::is_administered_at_Set() const{
    return m_administered_at_isSet;
}

bool OAIPatientVaccineRecord::is_administered_at_Valid() const{
    return m_administered_at_isValid;
}

QString OAIPatientVaccineRecord::getAdministeredBy() const {
    return m_administered_by;
}
void OAIPatientVaccineRecord::setAdministeredBy(const QString &administered_by) {
    m_administered_by = administered_by;
    m_administered_by_isSet = true;
}

bool OAIPatientVaccineRecord::is_administered_by_Set() const{
    return m_administered_by_isSet;
}

bool OAIPatientVaccineRecord::is_administered_by_Valid() const{
    return m_administered_by_isValid;
}

QString OAIPatientVaccineRecord::getAdministrationStart() const {
    return m_administration_start;
}
void OAIPatientVaccineRecord::setAdministrationStart(const QString &administration_start) {
    m_administration_start = administration_start;
    m_administration_start_isSet = true;
}

bool OAIPatientVaccineRecord::is_administration_start_Set() const{
    return m_administration_start_isSet;
}

bool OAIPatientVaccineRecord::is_administration_start_Valid() const{
    return m_administration_start_isValid;
}

double OAIPatientVaccineRecord::getAmount() const {
    return m_amount;
}
void OAIPatientVaccineRecord::setAmount(const double &amount) {
    m_amount = amount;
    m_amount_isSet = true;
}

bool OAIPatientVaccineRecord::is_amount_Set() const{
    return m_amount_isSet;
}

bool OAIPatientVaccineRecord::is_amount_Valid() const{
    return m_amount_isValid;
}

QString OAIPatientVaccineRecord::getComments() const {
    return m_comments;
}
void OAIPatientVaccineRecord::setComments(const QString &comments) {
    m_comments = comments;
    m_comments_isSet = true;
}

bool OAIPatientVaccineRecord::is_comments_Set() const{
    return m_comments_isSet;
}

bool OAIPatientVaccineRecord::is_comments_Valid() const{
    return m_comments_isValid;
}

QString OAIPatientVaccineRecord::getCompletionStatus() const {
    return m_completion_status;
}
void OAIPatientVaccineRecord::setCompletionStatus(const QString &completion_status) {
    m_completion_status = completion_status;
    m_completion_status_isSet = true;
}

bool OAIPatientVaccineRecord::is_completion_status_Set() const{
    return m_completion_status_isSet;
}

bool OAIPatientVaccineRecord::is_completion_status_Valid() const{
    return m_completion_status_isValid;
}

qint32 OAIPatientVaccineRecord::getConsentForm() const {
    return m_consent_form;
}
void OAIPatientVaccineRecord::setConsentForm(const qint32 &consent_form) {
    m_consent_form = consent_form;
    m_consent_form_isSet = true;
}

bool OAIPatientVaccineRecord::is_consent_form_Set() const{
    return m_consent_form_isSet;
}

bool OAIPatientVaccineRecord::is_consent_form_Valid() const{
    return m_consent_form_isValid;
}

QString OAIPatientVaccineRecord::getCptCode() const {
    return m_cpt_code;
}
void OAIPatientVaccineRecord::setCptCode(const QString &cpt_code) {
    m_cpt_code = cpt_code;
    m_cpt_code_isSet = true;
}

bool OAIPatientVaccineRecord::is_cpt_code_Set() const{
    return m_cpt_code_isSet;
}

bool OAIPatientVaccineRecord::is_cpt_code_Valid() const{
    return m_cpt_code_isValid;
}

QString OAIPatientVaccineRecord::getCreatedAt() const {
    return m_created_at;
}
void OAIPatientVaccineRecord::setCreatedAt(const QString &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIPatientVaccineRecord::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIPatientVaccineRecord::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIPatientVaccineRecord::getCvxCode() const {
    return m_cvx_code;
}
void OAIPatientVaccineRecord::setCvxCode(const QString &cvx_code) {
    m_cvx_code = cvx_code;
    m_cvx_code_isSet = true;
}

bool OAIPatientVaccineRecord::is_cvx_code_Set() const{
    return m_cvx_code_isSet;
}

bool OAIPatientVaccineRecord::is_cvx_code_Valid() const{
    return m_cvx_code_isValid;
}

QList<OAIVaccineDose> OAIPatientVaccineRecord::getDoses() const {
    return m_doses;
}
void OAIPatientVaccineRecord::setDoses(const QList<OAIVaccineDose> &doses) {
    m_doses = doses;
    m_doses_isSet = true;
}

bool OAIPatientVaccineRecord::is_doses_Set() const{
    return m_doses_isSet;
}

bool OAIPatientVaccineRecord::is_doses_Valid() const{
    return m_doses_isValid;
}

QString OAIPatientVaccineRecord::getEnteredBy() const {
    return m_entered_by;
}
void OAIPatientVaccineRecord::setEnteredBy(const QString &entered_by) {
    m_entered_by = entered_by;
    m_entered_by_isSet = true;
}

bool OAIPatientVaccineRecord::is_entered_by_Set() const{
    return m_entered_by_isSet;
}

bool OAIPatientVaccineRecord::is_entered_by_Valid() const{
    return m_entered_by_isValid;
}

QString OAIPatientVaccineRecord::getFundingEligibility() const {
    return m_funding_eligibility;
}
void OAIPatientVaccineRecord::setFundingEligibility(const QString &funding_eligibility) {
    m_funding_eligibility = funding_eligibility;
    m_funding_eligibility_isSet = true;
}

bool OAIPatientVaccineRecord::is_funding_eligibility_Set() const{
    return m_funding_eligibility_isSet;
}

bool OAIPatientVaccineRecord::is_funding_eligibility_Valid() const{
    return m_funding_eligibility_isValid;
}

qint32 OAIPatientVaccineRecord::getId() const {
    return m_id;
}
void OAIPatientVaccineRecord::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIPatientVaccineRecord::is_id_Set() const{
    return m_id_isSet;
}

bool OAIPatientVaccineRecord::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIPatientVaccineRecord::getName() const {
    return m_name;
}
void OAIPatientVaccineRecord::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIPatientVaccineRecord::is_name_Set() const{
    return m_name_isSet;
}

bool OAIPatientVaccineRecord::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIPatientVaccineRecord::getNextDoseDate() const {
    return m_next_dose_date;
}
void OAIPatientVaccineRecord::setNextDoseDate(const QString &next_dose_date) {
    m_next_dose_date = next_dose_date;
    m_next_dose_date_isSet = true;
}

bool OAIPatientVaccineRecord::is_next_dose_date_Set() const{
    return m_next_dose_date_isSet;
}

bool OAIPatientVaccineRecord::is_next_dose_date_Valid() const{
    return m_next_dose_date_isValid;
}

QString OAIPatientVaccineRecord::getObservedImmunity() const {
    return m_observed_immunity;
}
void OAIPatientVaccineRecord::setObservedImmunity(const QString &observed_immunity) {
    m_observed_immunity = observed_immunity;
    m_observed_immunity_isSet = true;
}

bool OAIPatientVaccineRecord::is_observed_immunity_Set() const{
    return m_observed_immunity_isSet;
}

bool OAIPatientVaccineRecord::is_observed_immunity_Valid() const{
    return m_observed_immunity_isValid;
}

qint32 OAIPatientVaccineRecord::getOrderingDoctor() const {
    return m_ordering_doctor;
}
void OAIPatientVaccineRecord::setOrderingDoctor(const qint32 &ordering_doctor) {
    m_ordering_doctor = ordering_doctor;
    m_ordering_doctor_isSet = true;
}

bool OAIPatientVaccineRecord::is_ordering_doctor_Set() const{
    return m_ordering_doctor_isSet;
}

bool OAIPatientVaccineRecord::is_ordering_doctor_Valid() const{
    return m_ordering_doctor_isValid;
}

qint32 OAIPatientVaccineRecord::getPatient() const {
    return m_patient;
}
void OAIPatientVaccineRecord::setPatient(const qint32 &patient) {
    m_patient = patient;
    m_patient_isSet = true;
}

bool OAIPatientVaccineRecord::is_patient_Set() const{
    return m_patient_isSet;
}

bool OAIPatientVaccineRecord::is_patient_Valid() const{
    return m_patient_isValid;
}

QString OAIPatientVaccineRecord::getRecordSource() const {
    return m_record_source;
}
void OAIPatientVaccineRecord::setRecordSource(const QString &record_source) {
    m_record_source = record_source;
    m_record_source_isSet = true;
}

bool OAIPatientVaccineRecord::is_record_source_Set() const{
    return m_record_source_isSet;
}

bool OAIPatientVaccineRecord::is_record_source_Valid() const{
    return m_record_source_isValid;
}

QString OAIPatientVaccineRecord::getRoute() const {
    return m_route;
}
void OAIPatientVaccineRecord::setRoute(const QString &route) {
    m_route = route;
    m_route_isSet = true;
}

bool OAIPatientVaccineRecord::is_route_Set() const{
    return m_route_isSet;
}

bool OAIPatientVaccineRecord::is_route_Valid() const{
    return m_route_isValid;
}

QString OAIPatientVaccineRecord::getSite() const {
    return m_site;
}
void OAIPatientVaccineRecord::setSite(const QString &site) {
    m_site = site;
    m_site_isSet = true;
}

bool OAIPatientVaccineRecord::is_site_Set() const{
    return m_site_isSet;
}

bool OAIPatientVaccineRecord::is_site_Valid() const{
    return m_site_isValid;
}

QString OAIPatientVaccineRecord::getUnits() const {
    return m_units;
}
void OAIPatientVaccineRecord::setUnits(const QString &units) {
    m_units = units;
    m_units_isSet = true;
}

bool OAIPatientVaccineRecord::is_units_Set() const{
    return m_units_isSet;
}

bool OAIPatientVaccineRecord::is_units_Valid() const{
    return m_units_isValid;
}

QString OAIPatientVaccineRecord::getUpdatedAt() const {
    return m_updated_at;
}
void OAIPatientVaccineRecord::setUpdatedAt(const QString &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIPatientVaccineRecord::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIPatientVaccineRecord::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

qint32 OAIPatientVaccineRecord::getVaccineInventory() const {
    return m_vaccine_inventory;
}
void OAIPatientVaccineRecord::setVaccineInventory(const qint32 &vaccine_inventory) {
    m_vaccine_inventory = vaccine_inventory;
    m_vaccine_inventory_isSet = true;
}

bool OAIPatientVaccineRecord::is_vaccine_inventory_Set() const{
    return m_vaccine_inventory_isSet;
}

bool OAIPatientVaccineRecord::is_vaccine_inventory_Valid() const{
    return m_vaccine_inventory_isValid;
}

QString OAIPatientVaccineRecord::getVis() const {
    return m_vis;
}
void OAIPatientVaccineRecord::setVis(const QString &vis) {
    m_vis = vis;
    m_vis_isSet = true;
}

bool OAIPatientVaccineRecord::is_vis_Set() const{
    return m_vis_isSet;
}

bool OAIPatientVaccineRecord::is_vis_Valid() const{
    return m_vis_isValid;
}

bool OAIPatientVaccineRecord::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_administered_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_administered_by_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_administration_start_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_comments_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_completion_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_consent_form_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cpt_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cvx_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_doses.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_entered_by_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_funding_eligibility_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_next_dose_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_observed_immunity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ordering_doctor_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_patient_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_record_source_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_route_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_site_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_units_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vaccine_inventory_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vis_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPatientVaccineRecord::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_cvx_code_isValid && m_name_isValid && m_patient_isValid && true;
}

} // namespace OpenAPI
