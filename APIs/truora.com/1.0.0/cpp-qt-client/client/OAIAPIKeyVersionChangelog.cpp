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

#include "OAIAPIKeyVersionChangelog.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAPIKeyVersionChangelog::OAIAPIKeyVersionChangelog(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAPIKeyVersionChangelog::OAIAPIKeyVersionChangelog() {
    this->initializeModel();
}

OAIAPIKeyVersionChangelog::~OAIAPIKeyVersionChangelog() {}

void OAIAPIKeyVersionChangelog::initializeModel() {

    m_added_isSet = false;
    m_added_isValid = false;

    m_changed_isSet = false;
    m_changed_isValid = false;

    m_deprecated_isSet = false;
    m_deprecated_isValid = false;

    m_fixed_isSet = false;
    m_fixed_isValid = false;

    m_notes_isSet = false;
    m_notes_isValid = false;

    m_removed_isSet = false;
    m_removed_isValid = false;

    m_security_isSet = false;
    m_security_isValid = false;
}

void OAIAPIKeyVersionChangelog::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAPIKeyVersionChangelog::fromJsonObject(QJsonObject json) {

    m_added_isValid = ::OpenAPI::fromJsonValue(m_added, json[QString("added")]);
    m_added_isSet = !json[QString("added")].isNull() && m_added_isValid;

    m_changed_isValid = ::OpenAPI::fromJsonValue(m_changed, json[QString("changed")]);
    m_changed_isSet = !json[QString("changed")].isNull() && m_changed_isValid;

    m_deprecated_isValid = ::OpenAPI::fromJsonValue(m_deprecated, json[QString("deprecated")]);
    m_deprecated_isSet = !json[QString("deprecated")].isNull() && m_deprecated_isValid;

    m_fixed_isValid = ::OpenAPI::fromJsonValue(m_fixed, json[QString("fixed")]);
    m_fixed_isSet = !json[QString("fixed")].isNull() && m_fixed_isValid;

    m_notes_isValid = ::OpenAPI::fromJsonValue(m_notes, json[QString("notes")]);
    m_notes_isSet = !json[QString("notes")].isNull() && m_notes_isValid;

    m_removed_isValid = ::OpenAPI::fromJsonValue(m_removed, json[QString("removed")]);
    m_removed_isSet = !json[QString("removed")].isNull() && m_removed_isValid;

    m_security_isValid = ::OpenAPI::fromJsonValue(m_security, json[QString("security")]);
    m_security_isSet = !json[QString("security")].isNull() && m_security_isValid;
}

QString OAIAPIKeyVersionChangelog::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAPIKeyVersionChangelog::asJsonObject() const {
    QJsonObject obj;
    if (m_added.size() > 0) {
        obj.insert(QString("added"), ::OpenAPI::toJsonValue(m_added));
    }
    if (m_changed.size() > 0) {
        obj.insert(QString("changed"), ::OpenAPI::toJsonValue(m_changed));
    }
    if (m_deprecated.size() > 0) {
        obj.insert(QString("deprecated"), ::OpenAPI::toJsonValue(m_deprecated));
    }
    if (m_fixed.size() > 0) {
        obj.insert(QString("fixed"), ::OpenAPI::toJsonValue(m_fixed));
    }
    if (m_notes_isSet) {
        obj.insert(QString("notes"), ::OpenAPI::toJsonValue(m_notes));
    }
    if (m_removed.size() > 0) {
        obj.insert(QString("removed"), ::OpenAPI::toJsonValue(m_removed));
    }
    if (m_security.size() > 0) {
        obj.insert(QString("security"), ::OpenAPI::toJsonValue(m_security));
    }
    return obj;
}

QList<QString> OAIAPIKeyVersionChangelog::getAdded() const {
    return m_added;
}
void OAIAPIKeyVersionChangelog::setAdded(const QList<QString> &added) {
    m_added = added;
    m_added_isSet = true;
}

bool OAIAPIKeyVersionChangelog::is_added_Set() const{
    return m_added_isSet;
}

bool OAIAPIKeyVersionChangelog::is_added_Valid() const{
    return m_added_isValid;
}

QList<QString> OAIAPIKeyVersionChangelog::getChanged() const {
    return m_changed;
}
void OAIAPIKeyVersionChangelog::setChanged(const QList<QString> &changed) {
    m_changed = changed;
    m_changed_isSet = true;
}

bool OAIAPIKeyVersionChangelog::is_changed_Set() const{
    return m_changed_isSet;
}

bool OAIAPIKeyVersionChangelog::is_changed_Valid() const{
    return m_changed_isValid;
}

QList<QString> OAIAPIKeyVersionChangelog::getDeprecated() const {
    return m_deprecated;
}
void OAIAPIKeyVersionChangelog::setDeprecated(const QList<QString> &deprecated) {
    m_deprecated = deprecated;
    m_deprecated_isSet = true;
}

bool OAIAPIKeyVersionChangelog::is_deprecated_Set() const{
    return m_deprecated_isSet;
}

bool OAIAPIKeyVersionChangelog::is_deprecated_Valid() const{
    return m_deprecated_isValid;
}

QList<QString> OAIAPIKeyVersionChangelog::getFixed() const {
    return m_fixed;
}
void OAIAPIKeyVersionChangelog::setFixed(const QList<QString> &fixed) {
    m_fixed = fixed;
    m_fixed_isSet = true;
}

bool OAIAPIKeyVersionChangelog::is_fixed_Set() const{
    return m_fixed_isSet;
}

bool OAIAPIKeyVersionChangelog::is_fixed_Valid() const{
    return m_fixed_isValid;
}

QString OAIAPIKeyVersionChangelog::getNotes() const {
    return m_notes;
}
void OAIAPIKeyVersionChangelog::setNotes(const QString &notes) {
    m_notes = notes;
    m_notes_isSet = true;
}

bool OAIAPIKeyVersionChangelog::is_notes_Set() const{
    return m_notes_isSet;
}

bool OAIAPIKeyVersionChangelog::is_notes_Valid() const{
    return m_notes_isValid;
}

QList<QString> OAIAPIKeyVersionChangelog::getRemoved() const {
    return m_removed;
}
void OAIAPIKeyVersionChangelog::setRemoved(const QList<QString> &removed) {
    m_removed = removed;
    m_removed_isSet = true;
}

bool OAIAPIKeyVersionChangelog::is_removed_Set() const{
    return m_removed_isSet;
}

bool OAIAPIKeyVersionChangelog::is_removed_Valid() const{
    return m_removed_isValid;
}

QList<QString> OAIAPIKeyVersionChangelog::getSecurity() const {
    return m_security;
}
void OAIAPIKeyVersionChangelog::setSecurity(const QList<QString> &security) {
    m_security = security;
    m_security_isSet = true;
}

bool OAIAPIKeyVersionChangelog::is_security_Set() const{
    return m_security_isSet;
}

bool OAIAPIKeyVersionChangelog::is_security_Valid() const{
    return m_security_isValid;
}

bool OAIAPIKeyVersionChangelog::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_added.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_changed.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_deprecated.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_fixed.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_removed.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_security.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAPIKeyVersionChangelog::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
