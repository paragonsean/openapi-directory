/**
 * Checks API
 * **NOTE:** This is a preview of the API and it is not considered stable since refinements are still being made.  # Introduction  Welcome to the  **Truora Check** [**RESTful API**](https://en.wikipedia.org/wiki/Representational_state_transfer) reference. You may also want to check out our [**Validations API docs**](https://docs.validations.truora.com/) or our [**Signals API docs**](https://docs.signals.truora.com/).  Truora Check API allows performing full background checks on people, vehicles and companies. There are three main types of background checks:  - **Personal background check**: Verifies national IDs in multiple databases of public and legal entities in the LATAM region. For every national ID, returns information on: personal identity, criminal records, international background check, and professional background.  - **Vehicle background check**: Verifies the vehicle documents and the owner identity in multiple databases of public and legal entities in the LATAM region. For every vehicle and owner type, returns information on: personal identity, driving records, criminal records, and vehicle information.    - **Company background check**: Verifies the tax ID or a company name in multiple databases of public and legal entities in the LATAM region. For every company, returns the associated: business status, legal and criminal records, and media reports.  # API Key V1 is live!  API key version 1 is now live. Users with version 0 API keys are not immediately required to upgrade to V1 but should plan to do so at their earliest convenience. The changes for integration with API keys v1 are as follows:  - The field ``user_authorized`` is now required to perform person checks. This field indicates the API user has authorization to perform the check in compliance with data protection law. - The field ``homonym_scores`` is no longer included in our person check response as its results are already included in the body of the check and keeping them duplicated is generating unnecessary confusion.   # API composition  ## Endpoints  - **Check endpoints**: Provide an easy way to create and search for a background check. They also allow inserting groups of checks into reports. Each check contains scores, datasets and databases.   ```plain https://api.truora.com/v1/checks ```  - **Report endpoints**: Support batch uploads and grouping multiple checks together. Excel and .csv files are supported for batch uploads.   ```plain https://api.truora.com/v1/reports ```  - **Configuration endpoints**: Allows personalizing data sets and scores for customized background checks.  ```plain https://api.truora.com/v1/config ```  - **Continuous check endpoints**: Allows creating recurring checks and get notified whenever a change in the check score occurs.  ```plain https://api.truora.com/v1/continuous_checks ```  - **Behavior endpoints**: Allows sharing anonymous feedback about a person behavior when interacting with the company.  ```plain https://api.truora.com/v1/behaviour ```  - **Hooks endpoints**: Allows sending notifications via requests to your service or another third-party service whenever certain events occur.  ```plain https://api.truora.com/v1/hooks ```  ## Datasets  Categories that group the resulting information for background checks from databases are called datasets. Datasets are divided in:  - **Personal identity**: Corroborates the existence and validates personal identity documents.   - **Criminal record**: Checks for crimes according to each country penal code or criminal code. Keep in mind that data aged less than 10 years is usually more consistent.  - **Legal background**: Checks for lawsuits filed. Keep in mind that data aged less than 10 years is usually more consistent.  - **International background**: Checks international lists for crimes related to identity theft, money laundering, terrorist financing, and high crimes.  - **Professional background**: Checks professional regulatory entities for relevant information.  - **Affiliations and insurances**: Checks the history and status of social security affiliations.  - **Alert in media**: Checks major media agencies for relevant news related to violent actions.      - **Vehicle information**: Checks for the physical characteristics of the vehicle, technical status, insurance history, and other relevant information.  - **Traffic fines**: Checks for outstanding traffic fines.  - **Driving licenses**: Shows information relevant to the driver. Such as license status and driver certificates.  - **Business background**: Checks for business status, legal and criminal history, and other relevant information.  - **Taxes and Finances**: Checks for the information related to personal finances, liabilities, and taxes.  ## Requests Format  The POST requests receive a body that must be encoded in `www-x-form-urlencoded`, for instance:  ```plain type=person&national_id=123456&country=CO ```  The responses are always encoded in `JSON` format.  ## Errors  Whenever there is an error, a JSON with the following format is returned:  ```json {     \"code\": <Truora error code>,     \"http_code\": <The HTTP status of the response>,     \"message\": <The error message> } ```  for instance:  ```json {     \"code\": 10404,     \"http_code\": 404,     \"message\": \"The Check was not found\" } ```  ## SDKs  If your favorite language was not on the next list, You can use our [OpenAPI 3 spec](https://docs.truora.com/openapi.json) to generate it using the [Open API Generator](https://openapi-generator.tech/docs/installation).  To download the SDK click on the desired programming language:  - [C# .Net Core](https://truora-sdk.s3.amazonaws.com/checks/checks_csharp-netcore_latest.zip)  - [Elixir](https://truora-sdk.s3.amazonaws.com/checks/checks_elixir_latest.zip)  - [Go](https://truora-sdk.s3.amazonaws.com/checks/checks_go_latest.zip)  - [Java](https://truora-sdk.s3.amazonaws.com/checks/checks_java_latest.zip)  - [JavaScript](https://truora-sdk.s3.amazonaws.com/checks/checks_javascript_latest.zip)  - [Objc](https://truora-sdk.s3.amazonaws.com/checks/checks_objc_latest.zip)  - [Php](https://truora-sdk.s3.amazonaws.com/checks/checks_php_latest.zip)  - [Python](https://truora-sdk.s3.amazonaws.com/checks/checks_python_latest.zip)  - [Ruby](https://truora-sdk.s3.amazonaws.com/checks/checks_ruby_latest.zip)  You can see the full list of supported platforms here:  https://openapi-generator.tech/docs/generators   
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: api@truora.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIHook.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIHook::OAIHook(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIHook::OAIHook() {
    this->initializeModel();
}

OAIHook::~OAIHook() {}

void OAIHook::initializeModel() {

    m_actions_isSet = false;
    m_actions_isValid = false;

    m_event_type_isSet = false;
    m_event_type_isValid = false;

    m_signing_key_isSet = false;
    m_signing_key_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_subscriber_type_isSet = false;
    m_subscriber_type_isValid = false;

    m_subscriber_url_isSet = false;
    m_subscriber_url_isValid = false;
}

void OAIHook::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIHook::fromJsonObject(QJsonObject json) {

    m_actions_isValid = ::OpenAPI::fromJsonValue(m_actions, json[QString("actions")]);
    m_actions_isSet = !json[QString("actions")].isNull() && m_actions_isValid;

    m_event_type_isValid = ::OpenAPI::fromJsonValue(m_event_type, json[QString("event_type")]);
    m_event_type_isSet = !json[QString("event_type")].isNull() && m_event_type_isValid;

    m_signing_key_isValid = ::OpenAPI::fromJsonValue(m_signing_key, json[QString("signing_key")]);
    m_signing_key_isSet = !json[QString("signing_key")].isNull() && m_signing_key_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_subscriber_type_isValid = ::OpenAPI::fromJsonValue(m_subscriber_type, json[QString("subscriber_type")]);
    m_subscriber_type_isSet = !json[QString("subscriber_type")].isNull() && m_subscriber_type_isValid;

    m_subscriber_url_isValid = ::OpenAPI::fromJsonValue(m_subscriber_url, json[QString("subscriber_url")]);
    m_subscriber_url_isSet = !json[QString("subscriber_url")].isNull() && m_subscriber_url_isValid;
}

QString OAIHook::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIHook::asJsonObject() const {
    QJsonObject obj;
    if (m_actions.size() > 0) {
        obj.insert(QString("actions"), ::OpenAPI::toJsonValue(m_actions));
    }
    if (m_event_type_isSet) {
        obj.insert(QString("event_type"), ::OpenAPI::toJsonValue(m_event_type));
    }
    if (m_signing_key_isSet) {
        obj.insert(QString("signing_key"), ::OpenAPI::toJsonValue(m_signing_key));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_subscriber_type_isSet) {
        obj.insert(QString("subscriber_type"), ::OpenAPI::toJsonValue(m_subscriber_type));
    }
    if (m_subscriber_url_isSet) {
        obj.insert(QString("subscriber_url"), ::OpenAPI::toJsonValue(m_subscriber_url));
    }
    return obj;
}

QList<QString> OAIHook::getActions() const {
    return m_actions;
}
void OAIHook::setActions(const QList<QString> &actions) {
    m_actions = actions;
    m_actions_isSet = true;
}

bool OAIHook::is_actions_Set() const{
    return m_actions_isSet;
}

bool OAIHook::is_actions_Valid() const{
    return m_actions_isValid;
}

QString OAIHook::getEventType() const {
    return m_event_type;
}
void OAIHook::setEventType(const QString &event_type) {
    m_event_type = event_type;
    m_event_type_isSet = true;
}

bool OAIHook::is_event_type_Set() const{
    return m_event_type_isSet;
}

bool OAIHook::is_event_type_Valid() const{
    return m_event_type_isValid;
}

QString OAIHook::getSigningKey() const {
    return m_signing_key;
}
void OAIHook::setSigningKey(const QString &signing_key) {
    m_signing_key = signing_key;
    m_signing_key_isSet = true;
}

bool OAIHook::is_signing_key_Set() const{
    return m_signing_key_isSet;
}

bool OAIHook::is_signing_key_Valid() const{
    return m_signing_key_isValid;
}

QString OAIHook::getStatus() const {
    return m_status;
}
void OAIHook::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIHook::is_status_Set() const{
    return m_status_isSet;
}

bool OAIHook::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIHook::getSubscriberType() const {
    return m_subscriber_type;
}
void OAIHook::setSubscriberType(const QString &subscriber_type) {
    m_subscriber_type = subscriber_type;
    m_subscriber_type_isSet = true;
}

bool OAIHook::is_subscriber_type_Set() const{
    return m_subscriber_type_isSet;
}

bool OAIHook::is_subscriber_type_Valid() const{
    return m_subscriber_type_isValid;
}

QString OAIHook::getSubscriberUrl() const {
    return m_subscriber_url;
}
void OAIHook::setSubscriberUrl(const QString &subscriber_url) {
    m_subscriber_url = subscriber_url;
    m_subscriber_url_isSet = true;
}

bool OAIHook::is_subscriber_url_Set() const{
    return m_subscriber_url_isSet;
}

bool OAIHook::is_subscriber_url_Valid() const{
    return m_subscriber_url_isValid;
}

bool OAIHook::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_actions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_event_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_signing_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_subscriber_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_subscriber_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIHook::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
