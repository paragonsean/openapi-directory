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

#include "OAIPatientLabResultSet.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPatientLabResultSet::OAIPatientLabResultSet(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPatientLabResultSet::OAIPatientLabResultSet() {
    this->initializeModel();
}

OAIPatientLabResultSet::~OAIPatientLabResultSet() {}

void OAIPatientLabResultSet::initializeModel() {

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_date_test_performed_isSet = false;
    m_date_test_performed_isValid = false;

    m_doctor_comments_isSet = false;
    m_doctor_comments_isValid = false;

    m_doctor_signoff_isSet = false;
    m_doctor_signoff_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_lab_abnormal_flag_isSet = false;
    m_lab_abnormal_flag_isValid = false;

    m_lab_imported_from_ccr_isSet = false;
    m_lab_imported_from_ccr_isValid = false;

    m_lab_normal_range_isSet = false;
    m_lab_normal_range_isValid = false;

    m_lab_normal_range_units_isSet = false;
    m_lab_normal_range_units_isValid = false;

    m_lab_order_status_isSet = false;
    m_lab_order_status_isValid = false;

    m_lab_result_value_isSet = false;
    m_lab_result_value_isValid = false;

    m_lab_result_value_as_float_isSet = false;
    m_lab_result_value_as_float_isValid = false;

    m_lab_result_value_units_isSet = false;
    m_lab_result_value_units_isValid = false;

    m_loinc_code_isSet = false;
    m_loinc_code_isValid = false;

    m_ordering_doctor_isSet = false;
    m_ordering_doctor_isValid = false;

    m_patient_isSet = false;
    m_patient_isValid = false;

    m_scanned_in_result_isSet = false;
    m_scanned_in_result_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;
}

void OAIPatientLabResultSet::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPatientLabResultSet::fromJsonObject(QJsonObject json) {

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_date_test_performed_isValid = ::OpenAPI::fromJsonValue(m_date_test_performed, json[QString("date_test_performed")]);
    m_date_test_performed_isSet = !json[QString("date_test_performed")].isNull() && m_date_test_performed_isValid;

    m_doctor_comments_isValid = ::OpenAPI::fromJsonValue(m_doctor_comments, json[QString("doctor_comments")]);
    m_doctor_comments_isSet = !json[QString("doctor_comments")].isNull() && m_doctor_comments_isValid;

    m_doctor_signoff_isValid = ::OpenAPI::fromJsonValue(m_doctor_signoff, json[QString("doctor_signoff")]);
    m_doctor_signoff_isSet = !json[QString("doctor_signoff")].isNull() && m_doctor_signoff_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_lab_abnormal_flag_isValid = ::OpenAPI::fromJsonValue(m_lab_abnormal_flag, json[QString("lab_abnormal_flag")]);
    m_lab_abnormal_flag_isSet = !json[QString("lab_abnormal_flag")].isNull() && m_lab_abnormal_flag_isValid;

    m_lab_imported_from_ccr_isValid = ::OpenAPI::fromJsonValue(m_lab_imported_from_ccr, json[QString("lab_imported_from_ccr")]);
    m_lab_imported_from_ccr_isSet = !json[QString("lab_imported_from_ccr")].isNull() && m_lab_imported_from_ccr_isValid;

    m_lab_normal_range_isValid = ::OpenAPI::fromJsonValue(m_lab_normal_range, json[QString("lab_normal_range")]);
    m_lab_normal_range_isSet = !json[QString("lab_normal_range")].isNull() && m_lab_normal_range_isValid;

    m_lab_normal_range_units_isValid = ::OpenAPI::fromJsonValue(m_lab_normal_range_units, json[QString("lab_normal_range_units")]);
    m_lab_normal_range_units_isSet = !json[QString("lab_normal_range_units")].isNull() && m_lab_normal_range_units_isValid;

    m_lab_order_status_isValid = ::OpenAPI::fromJsonValue(m_lab_order_status, json[QString("lab_order_status")]);
    m_lab_order_status_isSet = !json[QString("lab_order_status")].isNull() && m_lab_order_status_isValid;

    m_lab_result_value_isValid = ::OpenAPI::fromJsonValue(m_lab_result_value, json[QString("lab_result_value")]);
    m_lab_result_value_isSet = !json[QString("lab_result_value")].isNull() && m_lab_result_value_isValid;

    m_lab_result_value_as_float_isValid = ::OpenAPI::fromJsonValue(m_lab_result_value_as_float, json[QString("lab_result_value_as_float")]);
    m_lab_result_value_as_float_isSet = !json[QString("lab_result_value_as_float")].isNull() && m_lab_result_value_as_float_isValid;

    m_lab_result_value_units_isValid = ::OpenAPI::fromJsonValue(m_lab_result_value_units, json[QString("lab_result_value_units")]);
    m_lab_result_value_units_isSet = !json[QString("lab_result_value_units")].isNull() && m_lab_result_value_units_isValid;

    m_loinc_code_isValid = ::OpenAPI::fromJsonValue(m_loinc_code, json[QString("loinc_code")]);
    m_loinc_code_isSet = !json[QString("loinc_code")].isNull() && m_loinc_code_isValid;

    m_ordering_doctor_isValid = ::OpenAPI::fromJsonValue(m_ordering_doctor, json[QString("ordering_doctor")]);
    m_ordering_doctor_isSet = !json[QString("ordering_doctor")].isNull() && m_ordering_doctor_isValid;

    m_patient_isValid = ::OpenAPI::fromJsonValue(m_patient, json[QString("patient")]);
    m_patient_isSet = !json[QString("patient")].isNull() && m_patient_isValid;

    m_scanned_in_result_isValid = ::OpenAPI::fromJsonValue(m_scanned_in_result, json[QString("scanned_in_result")]);
    m_scanned_in_result_isSet = !json[QString("scanned_in_result")].isNull() && m_scanned_in_result_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updated_at")]);
    m_updated_at_isSet = !json[QString("updated_at")].isNull() && m_updated_at_isValid;
}

QString OAIPatientLabResultSet::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPatientLabResultSet::asJsonObject() const {
    QJsonObject obj;
    if (m_created_at_isSet) {
        obj.insert(QString("created_at"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_date_test_performed_isSet) {
        obj.insert(QString("date_test_performed"), ::OpenAPI::toJsonValue(m_date_test_performed));
    }
    if (m_doctor_comments_isSet) {
        obj.insert(QString("doctor_comments"), ::OpenAPI::toJsonValue(m_doctor_comments));
    }
    if (m_doctor_signoff_isSet) {
        obj.insert(QString("doctor_signoff"), ::OpenAPI::toJsonValue(m_doctor_signoff));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_lab_abnormal_flag_isSet) {
        obj.insert(QString("lab_abnormal_flag"), ::OpenAPI::toJsonValue(m_lab_abnormal_flag));
    }
    if (m_lab_imported_from_ccr_isSet) {
        obj.insert(QString("lab_imported_from_ccr"), ::OpenAPI::toJsonValue(m_lab_imported_from_ccr));
    }
    if (m_lab_normal_range_isSet) {
        obj.insert(QString("lab_normal_range"), ::OpenAPI::toJsonValue(m_lab_normal_range));
    }
    if (m_lab_normal_range_units_isSet) {
        obj.insert(QString("lab_normal_range_units"), ::OpenAPI::toJsonValue(m_lab_normal_range_units));
    }
    if (m_lab_order_status_isSet) {
        obj.insert(QString("lab_order_status"), ::OpenAPI::toJsonValue(m_lab_order_status));
    }
    if (m_lab_result_value_isSet) {
        obj.insert(QString("lab_result_value"), ::OpenAPI::toJsonValue(m_lab_result_value));
    }
    if (m_lab_result_value_as_float_isSet) {
        obj.insert(QString("lab_result_value_as_float"), ::OpenAPI::toJsonValue(m_lab_result_value_as_float));
    }
    if (m_lab_result_value_units_isSet) {
        obj.insert(QString("lab_result_value_units"), ::OpenAPI::toJsonValue(m_lab_result_value_units));
    }
    if (m_loinc_code_isSet) {
        obj.insert(QString("loinc_code"), ::OpenAPI::toJsonValue(m_loinc_code));
    }
    if (m_ordering_doctor_isSet) {
        obj.insert(QString("ordering_doctor"), ::OpenAPI::toJsonValue(m_ordering_doctor));
    }
    if (m_patient_isSet) {
        obj.insert(QString("patient"), ::OpenAPI::toJsonValue(m_patient));
    }
    if (m_scanned_in_result_isSet) {
        obj.insert(QString("scanned_in_result"), ::OpenAPI::toJsonValue(m_scanned_in_result));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updated_at"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    return obj;
}

QString OAIPatientLabResultSet::getCreatedAt() const {
    return m_created_at;
}
void OAIPatientLabResultSet::setCreatedAt(const QString &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIPatientLabResultSet::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIPatientLabResultSet::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIPatientLabResultSet::getDateTestPerformed() const {
    return m_date_test_performed;
}
void OAIPatientLabResultSet::setDateTestPerformed(const QString &date_test_performed) {
    m_date_test_performed = date_test_performed;
    m_date_test_performed_isSet = true;
}

bool OAIPatientLabResultSet::is_date_test_performed_Set() const{
    return m_date_test_performed_isSet;
}

bool OAIPatientLabResultSet::is_date_test_performed_Valid() const{
    return m_date_test_performed_isValid;
}

QString OAIPatientLabResultSet::getDoctorComments() const {
    return m_doctor_comments;
}
void OAIPatientLabResultSet::setDoctorComments(const QString &doctor_comments) {
    m_doctor_comments = doctor_comments;
    m_doctor_comments_isSet = true;
}

bool OAIPatientLabResultSet::is_doctor_comments_Set() const{
    return m_doctor_comments_isSet;
}

bool OAIPatientLabResultSet::is_doctor_comments_Valid() const{
    return m_doctor_comments_isValid;
}

bool OAIPatientLabResultSet::isDoctorSignoff() const {
    return m_doctor_signoff;
}
void OAIPatientLabResultSet::setDoctorSignoff(const bool &doctor_signoff) {
    m_doctor_signoff = doctor_signoff;
    m_doctor_signoff_isSet = true;
}

bool OAIPatientLabResultSet::is_doctor_signoff_Set() const{
    return m_doctor_signoff_isSet;
}

bool OAIPatientLabResultSet::is_doctor_signoff_Valid() const{
    return m_doctor_signoff_isValid;
}

qint32 OAIPatientLabResultSet::getId() const {
    return m_id;
}
void OAIPatientLabResultSet::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIPatientLabResultSet::is_id_Set() const{
    return m_id_isSet;
}

bool OAIPatientLabResultSet::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIPatientLabResultSet::getLabAbnormalFlag() const {
    return m_lab_abnormal_flag;
}
void OAIPatientLabResultSet::setLabAbnormalFlag(const QString &lab_abnormal_flag) {
    m_lab_abnormal_flag = lab_abnormal_flag;
    m_lab_abnormal_flag_isSet = true;
}

bool OAIPatientLabResultSet::is_lab_abnormal_flag_Set() const{
    return m_lab_abnormal_flag_isSet;
}

bool OAIPatientLabResultSet::is_lab_abnormal_flag_Valid() const{
    return m_lab_abnormal_flag_isValid;
}

QString OAIPatientLabResultSet::getLabImportedFromCcr() const {
    return m_lab_imported_from_ccr;
}
void OAIPatientLabResultSet::setLabImportedFromCcr(const QString &lab_imported_from_ccr) {
    m_lab_imported_from_ccr = lab_imported_from_ccr;
    m_lab_imported_from_ccr_isSet = true;
}

bool OAIPatientLabResultSet::is_lab_imported_from_ccr_Set() const{
    return m_lab_imported_from_ccr_isSet;
}

bool OAIPatientLabResultSet::is_lab_imported_from_ccr_Valid() const{
    return m_lab_imported_from_ccr_isValid;
}

QString OAIPatientLabResultSet::getLabNormalRange() const {
    return m_lab_normal_range;
}
void OAIPatientLabResultSet::setLabNormalRange(const QString &lab_normal_range) {
    m_lab_normal_range = lab_normal_range;
    m_lab_normal_range_isSet = true;
}

bool OAIPatientLabResultSet::is_lab_normal_range_Set() const{
    return m_lab_normal_range_isSet;
}

bool OAIPatientLabResultSet::is_lab_normal_range_Valid() const{
    return m_lab_normal_range_isValid;
}

QString OAIPatientLabResultSet::getLabNormalRangeUnits() const {
    return m_lab_normal_range_units;
}
void OAIPatientLabResultSet::setLabNormalRangeUnits(const QString &lab_normal_range_units) {
    m_lab_normal_range_units = lab_normal_range_units;
    m_lab_normal_range_units_isSet = true;
}

bool OAIPatientLabResultSet::is_lab_normal_range_units_Set() const{
    return m_lab_normal_range_units_isSet;
}

bool OAIPatientLabResultSet::is_lab_normal_range_units_Valid() const{
    return m_lab_normal_range_units_isValid;
}

QString OAIPatientLabResultSet::getLabOrderStatus() const {
    return m_lab_order_status;
}
void OAIPatientLabResultSet::setLabOrderStatus(const QString &lab_order_status) {
    m_lab_order_status = lab_order_status;
    m_lab_order_status_isSet = true;
}

bool OAIPatientLabResultSet::is_lab_order_status_Set() const{
    return m_lab_order_status_isSet;
}

bool OAIPatientLabResultSet::is_lab_order_status_Valid() const{
    return m_lab_order_status_isValid;
}

QString OAIPatientLabResultSet::getLabResultValue() const {
    return m_lab_result_value;
}
void OAIPatientLabResultSet::setLabResultValue(const QString &lab_result_value) {
    m_lab_result_value = lab_result_value;
    m_lab_result_value_isSet = true;
}

bool OAIPatientLabResultSet::is_lab_result_value_Set() const{
    return m_lab_result_value_isSet;
}

bool OAIPatientLabResultSet::is_lab_result_value_Valid() const{
    return m_lab_result_value_isValid;
}

double OAIPatientLabResultSet::getLabResultValueAsFloat() const {
    return m_lab_result_value_as_float;
}
void OAIPatientLabResultSet::setLabResultValueAsFloat(const double &lab_result_value_as_float) {
    m_lab_result_value_as_float = lab_result_value_as_float;
    m_lab_result_value_as_float_isSet = true;
}

bool OAIPatientLabResultSet::is_lab_result_value_as_float_Set() const{
    return m_lab_result_value_as_float_isSet;
}

bool OAIPatientLabResultSet::is_lab_result_value_as_float_Valid() const{
    return m_lab_result_value_as_float_isValid;
}

QString OAIPatientLabResultSet::getLabResultValueUnits() const {
    return m_lab_result_value_units;
}
void OAIPatientLabResultSet::setLabResultValueUnits(const QString &lab_result_value_units) {
    m_lab_result_value_units = lab_result_value_units;
    m_lab_result_value_units_isSet = true;
}

bool OAIPatientLabResultSet::is_lab_result_value_units_Set() const{
    return m_lab_result_value_units_isSet;
}

bool OAIPatientLabResultSet::is_lab_result_value_units_Valid() const{
    return m_lab_result_value_units_isValid;
}

QString OAIPatientLabResultSet::getLoincCode() const {
    return m_loinc_code;
}
void OAIPatientLabResultSet::setLoincCode(const QString &loinc_code) {
    m_loinc_code = loinc_code;
    m_loinc_code_isSet = true;
}

bool OAIPatientLabResultSet::is_loinc_code_Set() const{
    return m_loinc_code_isSet;
}

bool OAIPatientLabResultSet::is_loinc_code_Valid() const{
    return m_loinc_code_isValid;
}

qint32 OAIPatientLabResultSet::getOrderingDoctor() const {
    return m_ordering_doctor;
}
void OAIPatientLabResultSet::setOrderingDoctor(const qint32 &ordering_doctor) {
    m_ordering_doctor = ordering_doctor;
    m_ordering_doctor_isSet = true;
}

bool OAIPatientLabResultSet::is_ordering_doctor_Set() const{
    return m_ordering_doctor_isSet;
}

bool OAIPatientLabResultSet::is_ordering_doctor_Valid() const{
    return m_ordering_doctor_isValid;
}

qint32 OAIPatientLabResultSet::getPatient() const {
    return m_patient;
}
void OAIPatientLabResultSet::setPatient(const qint32 &patient) {
    m_patient = patient;
    m_patient_isSet = true;
}

bool OAIPatientLabResultSet::is_patient_Set() const{
    return m_patient_isSet;
}

bool OAIPatientLabResultSet::is_patient_Valid() const{
    return m_patient_isValid;
}

QString OAIPatientLabResultSet::getScannedInResult() const {
    return m_scanned_in_result;
}
void OAIPatientLabResultSet::setScannedInResult(const QString &scanned_in_result) {
    m_scanned_in_result = scanned_in_result;
    m_scanned_in_result_isSet = true;
}

bool OAIPatientLabResultSet::is_scanned_in_result_Set() const{
    return m_scanned_in_result_isSet;
}

bool OAIPatientLabResultSet::is_scanned_in_result_Valid() const{
    return m_scanned_in_result_isValid;
}

QString OAIPatientLabResultSet::getTitle() const {
    return m_title;
}
void OAIPatientLabResultSet::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIPatientLabResultSet::is_title_Set() const{
    return m_title_isSet;
}

bool OAIPatientLabResultSet::is_title_Valid() const{
    return m_title_isValid;
}

QString OAIPatientLabResultSet::getUpdatedAt() const {
    return m_updated_at;
}
void OAIPatientLabResultSet::setUpdatedAt(const QString &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIPatientLabResultSet::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIPatientLabResultSet::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

bool OAIPatientLabResultSet::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_test_performed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_doctor_comments_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_doctor_signoff_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lab_abnormal_flag_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lab_imported_from_ccr_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lab_normal_range_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lab_normal_range_units_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lab_order_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lab_result_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lab_result_value_as_float_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lab_result_value_units_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_loinc_code_isSet) {
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

        if (m_scanned_in_result_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPatientLabResultSet::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_ordering_doctor_isValid && m_patient_isValid && true;
}

} // namespace OpenAPI
