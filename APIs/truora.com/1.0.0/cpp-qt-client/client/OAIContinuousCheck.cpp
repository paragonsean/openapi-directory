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

#include "OAIContinuousCheck.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIContinuousCheck::OAIContinuousCheck(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIContinuousCheck::OAIContinuousCheck() {
    this->initializeModel();
}

OAIContinuousCheck::~OAIContinuousCheck() {}

void OAIContinuousCheck::initializeModel() {

    m_continuous_check_id_isSet = false;
    m_continuous_check_id_isValid = false;

    m_continuous_check_status_isSet = false;
    m_continuous_check_status_isValid = false;

    m_creation_date_isSet = false;
    m_creation_date_isValid = false;

    m_enabled_isSet = false;
    m_enabled_isValid = false;

    m_frequency_isSet = false;
    m_frequency_isValid = false;

    m_history_isSet = false;
    m_history_isValid = false;

    m_last_check_id_isSet = false;
    m_last_check_id_isValid = false;

    m_next_run_date_isSet = false;
    m_next_run_date_isValid = false;

    m_original_check_isSet = false;
    m_original_check_isValid = false;

    m_update_date_isSet = false;
    m_update_date_isValid = false;
}

void OAIContinuousCheck::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIContinuousCheck::fromJsonObject(QJsonObject json) {

    m_continuous_check_id_isValid = ::OpenAPI::fromJsonValue(m_continuous_check_id, json[QString("ContinuousCheckID")]);
    m_continuous_check_id_isSet = !json[QString("ContinuousCheckID")].isNull() && m_continuous_check_id_isValid;

    m_continuous_check_status_isValid = ::OpenAPI::fromJsonValue(m_continuous_check_status, json[QString("ContinuousCheckStatus")]);
    m_continuous_check_status_isSet = !json[QString("ContinuousCheckStatus")].isNull() && m_continuous_check_status_isValid;

    m_creation_date_isValid = ::OpenAPI::fromJsonValue(m_creation_date, json[QString("CreationDate")]);
    m_creation_date_isSet = !json[QString("CreationDate")].isNull() && m_creation_date_isValid;

    m_enabled_isValid = ::OpenAPI::fromJsonValue(m_enabled, json[QString("Enabled")]);
    m_enabled_isSet = !json[QString("Enabled")].isNull() && m_enabled_isValid;

    m_frequency_isValid = ::OpenAPI::fromJsonValue(m_frequency, json[QString("Frequency")]);
    m_frequency_isSet = !json[QString("Frequency")].isNull() && m_frequency_isValid;

    m_history_isValid = ::OpenAPI::fromJsonValue(m_history, json[QString("History")]);
    m_history_isSet = !json[QString("History")].isNull() && m_history_isValid;

    m_last_check_id_isValid = ::OpenAPI::fromJsonValue(m_last_check_id, json[QString("LastCheckID")]);
    m_last_check_id_isSet = !json[QString("LastCheckID")].isNull() && m_last_check_id_isValid;

    m_next_run_date_isValid = ::OpenAPI::fromJsonValue(m_next_run_date, json[QString("NextRunDate")]);
    m_next_run_date_isSet = !json[QString("NextRunDate")].isNull() && m_next_run_date_isValid;

    m_original_check_isValid = ::OpenAPI::fromJsonValue(m_original_check, json[QString("OriginalCheck")]);
    m_original_check_isSet = !json[QString("OriginalCheck")].isNull() && m_original_check_isValid;

    m_update_date_isValid = ::OpenAPI::fromJsonValue(m_update_date, json[QString("UpdateDate")]);
    m_update_date_isSet = !json[QString("UpdateDate")].isNull() && m_update_date_isValid;
}

QString OAIContinuousCheck::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIContinuousCheck::asJsonObject() const {
    QJsonObject obj;
    if (m_continuous_check_id_isSet) {
        obj.insert(QString("ContinuousCheckID"), ::OpenAPI::toJsonValue(m_continuous_check_id));
    }
    if (m_continuous_check_status_isSet) {
        obj.insert(QString("ContinuousCheckStatus"), ::OpenAPI::toJsonValue(m_continuous_check_status));
    }
    if (m_creation_date_isSet) {
        obj.insert(QString("CreationDate"), ::OpenAPI::toJsonValue(m_creation_date));
    }
    if (m_enabled_isSet) {
        obj.insert(QString("Enabled"), ::OpenAPI::toJsonValue(m_enabled));
    }
    if (m_frequency_isSet) {
        obj.insert(QString("Frequency"), ::OpenAPI::toJsonValue(m_frequency));
    }
    if (m_history.isSet()) {
        obj.insert(QString("History"), ::OpenAPI::toJsonValue(m_history));
    }
    if (m_last_check_id_isSet) {
        obj.insert(QString("LastCheckID"), ::OpenAPI::toJsonValue(m_last_check_id));
    }
    if (m_next_run_date_isSet) {
        obj.insert(QString("NextRunDate"), ::OpenAPI::toJsonValue(m_next_run_date));
    }
    if (m_original_check.isSet()) {
        obj.insert(QString("OriginalCheck"), ::OpenAPI::toJsonValue(m_original_check));
    }
    if (m_update_date_isSet) {
        obj.insert(QString("UpdateDate"), ::OpenAPI::toJsonValue(m_update_date));
    }
    return obj;
}

QString OAIContinuousCheck::getContinuousCheckId() const {
    return m_continuous_check_id;
}
void OAIContinuousCheck::setContinuousCheckId(const QString &continuous_check_id) {
    m_continuous_check_id = continuous_check_id;
    m_continuous_check_id_isSet = true;
}

bool OAIContinuousCheck::is_continuous_check_id_Set() const{
    return m_continuous_check_id_isSet;
}

bool OAIContinuousCheck::is_continuous_check_id_Valid() const{
    return m_continuous_check_id_isValid;
}

QString OAIContinuousCheck::getContinuousCheckStatus() const {
    return m_continuous_check_status;
}
void OAIContinuousCheck::setContinuousCheckStatus(const QString &continuous_check_status) {
    m_continuous_check_status = continuous_check_status;
    m_continuous_check_status_isSet = true;
}

bool OAIContinuousCheck::is_continuous_check_status_Set() const{
    return m_continuous_check_status_isSet;
}

bool OAIContinuousCheck::is_continuous_check_status_Valid() const{
    return m_continuous_check_status_isValid;
}

QDate OAIContinuousCheck::getCreationDate() const {
    return m_creation_date;
}
void OAIContinuousCheck::setCreationDate(const QDate &creation_date) {
    m_creation_date = creation_date;
    m_creation_date_isSet = true;
}

bool OAIContinuousCheck::is_creation_date_Set() const{
    return m_creation_date_isSet;
}

bool OAIContinuousCheck::is_creation_date_Valid() const{
    return m_creation_date_isValid;
}

bool OAIContinuousCheck::isEnabled() const {
    return m_enabled;
}
void OAIContinuousCheck::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAIContinuousCheck::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAIContinuousCheck::is_enabled_Valid() const{
    return m_enabled_isValid;
}

QString OAIContinuousCheck::getFrequency() const {
    return m_frequency;
}
void OAIContinuousCheck::setFrequency(const QString &frequency) {
    m_frequency = frequency;
    m_frequency_isSet = true;
}

bool OAIContinuousCheck::is_frequency_Set() const{
    return m_frequency_isSet;
}

bool OAIContinuousCheck::is_frequency_Valid() const{
    return m_frequency_isValid;
}

OAIContinuousCheckEntry OAIContinuousCheck::getHistory() const {
    return m_history;
}
void OAIContinuousCheck::setHistory(const OAIContinuousCheckEntry &history) {
    m_history = history;
    m_history_isSet = true;
}

bool OAIContinuousCheck::is_history_Set() const{
    return m_history_isSet;
}

bool OAIContinuousCheck::is_history_Valid() const{
    return m_history_isValid;
}

QString OAIContinuousCheck::getLastCheckId() const {
    return m_last_check_id;
}
void OAIContinuousCheck::setLastCheckId(const QString &last_check_id) {
    m_last_check_id = last_check_id;
    m_last_check_id_isSet = true;
}

bool OAIContinuousCheck::is_last_check_id_Set() const{
    return m_last_check_id_isSet;
}

bool OAIContinuousCheck::is_last_check_id_Valid() const{
    return m_last_check_id_isValid;
}

QDate OAIContinuousCheck::getNextRunDate() const {
    return m_next_run_date;
}
void OAIContinuousCheck::setNextRunDate(const QDate &next_run_date) {
    m_next_run_date = next_run_date;
    m_next_run_date_isSet = true;
}

bool OAIContinuousCheck::is_next_run_date_Set() const{
    return m_next_run_date_isSet;
}

bool OAIContinuousCheck::is_next_run_date_Valid() const{
    return m_next_run_date_isValid;
}

OAICheck OAIContinuousCheck::getOriginalCheck() const {
    return m_original_check;
}
void OAIContinuousCheck::setOriginalCheck(const OAICheck &original_check) {
    m_original_check = original_check;
    m_original_check_isSet = true;
}

bool OAIContinuousCheck::is_original_check_Set() const{
    return m_original_check_isSet;
}

bool OAIContinuousCheck::is_original_check_Valid() const{
    return m_original_check_isValid;
}

QDate OAIContinuousCheck::getUpdateDate() const {
    return m_update_date;
}
void OAIContinuousCheck::setUpdateDate(const QDate &update_date) {
    m_update_date = update_date;
    m_update_date_isSet = true;
}

bool OAIContinuousCheck::is_update_date_Set() const{
    return m_update_date_isSet;
}

bool OAIContinuousCheck::is_update_date_Valid() const{
    return m_update_date_isValid;
}

bool OAIContinuousCheck::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_continuous_check_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_continuous_check_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_creation_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_frequency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_history.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_check_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_next_run_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_original_check.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_update_date_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIContinuousCheck::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_continuous_check_status_isValid && m_frequency_isValid && m_last_check_id_isValid && true;
}

} // namespace OpenAPI
