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

#include "OAILabResult.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILabResult::OAILabResult(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILabResult::OAILabResult() {
    this->initializeModel();
}

OAILabResult::~OAILabResult() {}

void OAILabResult::initializeModel() {

    m_abnormal_status_isSet = false;
    m_abnormal_status_isValid = false;

    m_comments_isSet = false;
    m_comments_isValid = false;

    m_document_isSet = false;
    m_document_isValid = false;

    m_group_code_isSet = false;
    m_group_code_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_abnormal_isSet = false;
    m_is_abnormal_isValid = false;

    m_lab_order_isSet = false;
    m_lab_order_isValid = false;

    m_lab_test_isSet = false;
    m_lab_test_isValid = false;

    m_normal_range_isSet = false;
    m_normal_range_isValid = false;

    m_observation_code_isSet = false;
    m_observation_code_isValid = false;

    m_observation_description_isSet = false;
    m_observation_description_isValid = false;

    m_specimen_received_isSet = false;
    m_specimen_received_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_test_performed_isSet = false;
    m_test_performed_isValid = false;

    m_unit_isSet = false;
    m_unit_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;

    m_value_is_numeric_isSet = false;
    m_value_is_numeric_isValid = false;
}

void OAILabResult::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILabResult::fromJsonObject(QJsonObject json) {

    m_abnormal_status_isValid = ::OpenAPI::fromJsonValue(m_abnormal_status, json[QString("abnormal_status")]);
    m_abnormal_status_isSet = !json[QString("abnormal_status")].isNull() && m_abnormal_status_isValid;

    m_comments_isValid = ::OpenAPI::fromJsonValue(m_comments, json[QString("comments")]);
    m_comments_isSet = !json[QString("comments")].isNull() && m_comments_isValid;

    m_document_isValid = ::OpenAPI::fromJsonValue(m_document, json[QString("document")]);
    m_document_isSet = !json[QString("document")].isNull() && m_document_isValid;

    m_group_code_isValid = ::OpenAPI::fromJsonValue(m_group_code, json[QString("group_code")]);
    m_group_code_isSet = !json[QString("group_code")].isNull() && m_group_code_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_abnormal_isValid = ::OpenAPI::fromJsonValue(m_is_abnormal, json[QString("is_abnormal")]);
    m_is_abnormal_isSet = !json[QString("is_abnormal")].isNull() && m_is_abnormal_isValid;

    m_lab_order_isValid = ::OpenAPI::fromJsonValue(m_lab_order, json[QString("lab_order")]);
    m_lab_order_isSet = !json[QString("lab_order")].isNull() && m_lab_order_isValid;

    m_lab_test_isValid = ::OpenAPI::fromJsonValue(m_lab_test, json[QString("lab_test")]);
    m_lab_test_isSet = !json[QString("lab_test")].isNull() && m_lab_test_isValid;

    m_normal_range_isValid = ::OpenAPI::fromJsonValue(m_normal_range, json[QString("normal_range")]);
    m_normal_range_isSet = !json[QString("normal_range")].isNull() && m_normal_range_isValid;

    m_observation_code_isValid = ::OpenAPI::fromJsonValue(m_observation_code, json[QString("observation_code")]);
    m_observation_code_isSet = !json[QString("observation_code")].isNull() && m_observation_code_isValid;

    m_observation_description_isValid = ::OpenAPI::fromJsonValue(m_observation_description, json[QString("observation_description")]);
    m_observation_description_isSet = !json[QString("observation_description")].isNull() && m_observation_description_isValid;

    m_specimen_received_isValid = ::OpenAPI::fromJsonValue(m_specimen_received, json[QString("specimen_received")]);
    m_specimen_received_isSet = !json[QString("specimen_received")].isNull() && m_specimen_received_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_test_performed_isValid = ::OpenAPI::fromJsonValue(m_test_performed, json[QString("test_performed")]);
    m_test_performed_isSet = !json[QString("test_performed")].isNull() && m_test_performed_isValid;

    m_unit_isValid = ::OpenAPI::fromJsonValue(m_unit, json[QString("unit")]);
    m_unit_isSet = !json[QString("unit")].isNull() && m_unit_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;

    m_value_is_numeric_isValid = ::OpenAPI::fromJsonValue(m_value_is_numeric, json[QString("value_is_numeric")]);
    m_value_is_numeric_isSet = !json[QString("value_is_numeric")].isNull() && m_value_is_numeric_isValid;
}

QString OAILabResult::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILabResult::asJsonObject() const {
    QJsonObject obj;
    if (m_abnormal_status_isSet) {
        obj.insert(QString("abnormal_status"), ::OpenAPI::toJsonValue(m_abnormal_status));
    }
    if (m_comments_isSet) {
        obj.insert(QString("comments"), ::OpenAPI::toJsonValue(m_comments));
    }
    if (m_document_isSet) {
        obj.insert(QString("document"), ::OpenAPI::toJsonValue(m_document));
    }
    if (m_group_code_isSet) {
        obj.insert(QString("group_code"), ::OpenAPI::toJsonValue(m_group_code));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_abnormal_isSet) {
        obj.insert(QString("is_abnormal"), ::OpenAPI::toJsonValue(m_is_abnormal));
    }
    if (m_lab_order_isSet) {
        obj.insert(QString("lab_order"), ::OpenAPI::toJsonValue(m_lab_order));
    }
    if (m_lab_test_isSet) {
        obj.insert(QString("lab_test"), ::OpenAPI::toJsonValue(m_lab_test));
    }
    if (m_normal_range_isSet) {
        obj.insert(QString("normal_range"), ::OpenAPI::toJsonValue(m_normal_range));
    }
    if (m_observation_code_isSet) {
        obj.insert(QString("observation_code"), ::OpenAPI::toJsonValue(m_observation_code));
    }
    if (m_observation_description_isSet) {
        obj.insert(QString("observation_description"), ::OpenAPI::toJsonValue(m_observation_description));
    }
    if (m_specimen_received_isSet) {
        obj.insert(QString("specimen_received"), ::OpenAPI::toJsonValue(m_specimen_received));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_test_performed_isSet) {
        obj.insert(QString("test_performed"), ::OpenAPI::toJsonValue(m_test_performed));
    }
    if (m_unit_isSet) {
        obj.insert(QString("unit"), ::OpenAPI::toJsonValue(m_unit));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    if (m_value_is_numeric_isSet) {
        obj.insert(QString("value_is_numeric"), ::OpenAPI::toJsonValue(m_value_is_numeric));
    }
    return obj;
}

QString OAILabResult::getAbnormalStatus() const {
    return m_abnormal_status;
}
void OAILabResult::setAbnormalStatus(const QString &abnormal_status) {
    m_abnormal_status = abnormal_status;
    m_abnormal_status_isSet = true;
}

bool OAILabResult::is_abnormal_status_Set() const{
    return m_abnormal_status_isSet;
}

bool OAILabResult::is_abnormal_status_Valid() const{
    return m_abnormal_status_isValid;
}

QString OAILabResult::getComments() const {
    return m_comments;
}
void OAILabResult::setComments(const QString &comments) {
    m_comments = comments;
    m_comments_isSet = true;
}

bool OAILabResult::is_comments_Set() const{
    return m_comments_isSet;
}

bool OAILabResult::is_comments_Valid() const{
    return m_comments_isValid;
}

qint32 OAILabResult::getDocument() const {
    return m_document;
}
void OAILabResult::setDocument(const qint32 &document) {
    m_document = document;
    m_document_isSet = true;
}

bool OAILabResult::is_document_Set() const{
    return m_document_isSet;
}

bool OAILabResult::is_document_Valid() const{
    return m_document_isValid;
}

QString OAILabResult::getGroupCode() const {
    return m_group_code;
}
void OAILabResult::setGroupCode(const QString &group_code) {
    m_group_code = group_code;
    m_group_code_isSet = true;
}

bool OAILabResult::is_group_code_Set() const{
    return m_group_code_isSet;
}

bool OAILabResult::is_group_code_Valid() const{
    return m_group_code_isValid;
}

qint32 OAILabResult::getId() const {
    return m_id;
}
void OAILabResult::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAILabResult::is_id_Set() const{
    return m_id_isSet;
}

bool OAILabResult::is_id_Valid() const{
    return m_id_isValid;
}

QString OAILabResult::getIsAbnormal() const {
    return m_is_abnormal;
}
void OAILabResult::setIsAbnormal(const QString &is_abnormal) {
    m_is_abnormal = is_abnormal;
    m_is_abnormal_isSet = true;
}

bool OAILabResult::is_is_abnormal_Set() const{
    return m_is_abnormal_isSet;
}

bool OAILabResult::is_is_abnormal_Valid() const{
    return m_is_abnormal_isValid;
}

QString OAILabResult::getLabOrder() const {
    return m_lab_order;
}
void OAILabResult::setLabOrder(const QString &lab_order) {
    m_lab_order = lab_order;
    m_lab_order_isSet = true;
}

bool OAILabResult::is_lab_order_Set() const{
    return m_lab_order_isSet;
}

bool OAILabResult::is_lab_order_Valid() const{
    return m_lab_order_isValid;
}

qint32 OAILabResult::getLabTest() const {
    return m_lab_test;
}
void OAILabResult::setLabTest(const qint32 &lab_test) {
    m_lab_test = lab_test;
    m_lab_test_isSet = true;
}

bool OAILabResult::is_lab_test_Set() const{
    return m_lab_test_isSet;
}

bool OAILabResult::is_lab_test_Valid() const{
    return m_lab_test_isValid;
}

QString OAILabResult::getNormalRange() const {
    return m_normal_range;
}
void OAILabResult::setNormalRange(const QString &normal_range) {
    m_normal_range = normal_range;
    m_normal_range_isSet = true;
}

bool OAILabResult::is_normal_range_Set() const{
    return m_normal_range_isSet;
}

bool OAILabResult::is_normal_range_Valid() const{
    return m_normal_range_isValid;
}

QString OAILabResult::getObservationCode() const {
    return m_observation_code;
}
void OAILabResult::setObservationCode(const QString &observation_code) {
    m_observation_code = observation_code;
    m_observation_code_isSet = true;
}

bool OAILabResult::is_observation_code_Set() const{
    return m_observation_code_isSet;
}

bool OAILabResult::is_observation_code_Valid() const{
    return m_observation_code_isValid;
}

QString OAILabResult::getObservationDescription() const {
    return m_observation_description;
}
void OAILabResult::setObservationDescription(const QString &observation_description) {
    m_observation_description = observation_description;
    m_observation_description_isSet = true;
}

bool OAILabResult::is_observation_description_Set() const{
    return m_observation_description_isSet;
}

bool OAILabResult::is_observation_description_Valid() const{
    return m_observation_description_isValid;
}

QString OAILabResult::getSpecimenReceived() const {
    return m_specimen_received;
}
void OAILabResult::setSpecimenReceived(const QString &specimen_received) {
    m_specimen_received = specimen_received;
    m_specimen_received_isSet = true;
}

bool OAILabResult::is_specimen_received_Set() const{
    return m_specimen_received_isSet;
}

bool OAILabResult::is_specimen_received_Valid() const{
    return m_specimen_received_isValid;
}

QString OAILabResult::getStatus() const {
    return m_status;
}
void OAILabResult::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAILabResult::is_status_Set() const{
    return m_status_isSet;
}

bool OAILabResult::is_status_Valid() const{
    return m_status_isValid;
}

QString OAILabResult::getTestPerformed() const {
    return m_test_performed;
}
void OAILabResult::setTestPerformed(const QString &test_performed) {
    m_test_performed = test_performed;
    m_test_performed_isSet = true;
}

bool OAILabResult::is_test_performed_Set() const{
    return m_test_performed_isSet;
}

bool OAILabResult::is_test_performed_Valid() const{
    return m_test_performed_isValid;
}

QString OAILabResult::getUnit() const {
    return m_unit;
}
void OAILabResult::setUnit(const QString &unit) {
    m_unit = unit;
    m_unit_isSet = true;
}

bool OAILabResult::is_unit_Set() const{
    return m_unit_isSet;
}

bool OAILabResult::is_unit_Valid() const{
    return m_unit_isValid;
}

QString OAILabResult::getValue() const {
    return m_value;
}
void OAILabResult::setValue(const QString &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAILabResult::is_value_Set() const{
    return m_value_isSet;
}

bool OAILabResult::is_value_Valid() const{
    return m_value_isValid;
}

bool OAILabResult::isValueIsNumeric() const {
    return m_value_is_numeric;
}
void OAILabResult::setValueIsNumeric(const bool &value_is_numeric) {
    m_value_is_numeric = value_is_numeric;
    m_value_is_numeric_isSet = true;
}

bool OAILabResult::is_value_is_numeric_Set() const{
    return m_value_is_numeric_isSet;
}

bool OAILabResult::is_value_is_numeric_Valid() const{
    return m_value_is_numeric_isValid;
}

bool OAILabResult::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_abnormal_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_comments_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_document_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_group_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_abnormal_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lab_order_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lab_test_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_normal_range_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_observation_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_observation_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_specimen_received_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_test_performed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value_is_numeric_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILabResult::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_document_isValid && m_lab_test_isValid && m_status_isValid && m_test_performed_isValid && m_value_isValid && true;
}

} // namespace OpenAPI
