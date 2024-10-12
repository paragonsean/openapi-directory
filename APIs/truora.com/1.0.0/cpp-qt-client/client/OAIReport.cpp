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

#include "OAIReport.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIReport::OAIReport(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIReport::OAIReport() {
    this->initializeModel();
}

OAIReport::~OAIReport() {}

void OAIReport::initializeModel() {

    m_created_by_isSet = false;
    m_created_by_isValid = false;

    m_created_checks_count_isSet = false;
    m_created_checks_count_isValid = false;

    m_creation_date_isSet = false;
    m_creation_date_isValid = false;

    m_has_data_isSet = false;
    m_has_data_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_invalid_checks_count_isSet = false;
    m_invalid_checks_count_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_size_isSet = false;
    m_size_isValid = false;

    m_update_date_isSet = false;
    m_update_date_isValid = false;
}

void OAIReport::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIReport::fromJsonObject(QJsonObject json) {

    m_created_by_isValid = ::OpenAPI::fromJsonValue(m_created_by, json[QString("created_by")]);
    m_created_by_isSet = !json[QString("created_by")].isNull() && m_created_by_isValid;

    m_created_checks_count_isValid = ::OpenAPI::fromJsonValue(m_created_checks_count, json[QString("created_checks_count")]);
    m_created_checks_count_isSet = !json[QString("created_checks_count")].isNull() && m_created_checks_count_isValid;

    m_creation_date_isValid = ::OpenAPI::fromJsonValue(m_creation_date, json[QString("creation_date")]);
    m_creation_date_isSet = !json[QString("creation_date")].isNull() && m_creation_date_isValid;

    m_has_data_isValid = ::OpenAPI::fromJsonValue(m_has_data, json[QString("has_data")]);
    m_has_data_isSet = !json[QString("has_data")].isNull() && m_has_data_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_invalid_checks_count_isValid = ::OpenAPI::fromJsonValue(m_invalid_checks_count, json[QString("invalid_checks_count")]);
    m_invalid_checks_count_isSet = !json[QString("invalid_checks_count")].isNull() && m_invalid_checks_count_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_size_isValid = ::OpenAPI::fromJsonValue(m_size, json[QString("size")]);
    m_size_isSet = !json[QString("size")].isNull() && m_size_isValid;

    m_update_date_isValid = ::OpenAPI::fromJsonValue(m_update_date, json[QString("update_date")]);
    m_update_date_isSet = !json[QString("update_date")].isNull() && m_update_date_isValid;
}

QString OAIReport::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIReport::asJsonObject() const {
    QJsonObject obj;
    if (m_created_by_isSet) {
        obj.insert(QString("created_by"), ::OpenAPI::toJsonValue(m_created_by));
    }
    if (m_created_checks_count_isSet) {
        obj.insert(QString("created_checks_count"), ::OpenAPI::toJsonValue(m_created_checks_count));
    }
    if (m_creation_date_isSet) {
        obj.insert(QString("creation_date"), ::OpenAPI::toJsonValue(m_creation_date));
    }
    if (m_has_data_isSet) {
        obj.insert(QString("has_data"), ::OpenAPI::toJsonValue(m_has_data));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_invalid_checks_count_isSet) {
        obj.insert(QString("invalid_checks_count"), ::OpenAPI::toJsonValue(m_invalid_checks_count));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_size_isSet) {
        obj.insert(QString("size"), ::OpenAPI::toJsonValue(m_size));
    }
    if (m_update_date_isSet) {
        obj.insert(QString("update_date"), ::OpenAPI::toJsonValue(m_update_date));
    }
    return obj;
}

QString OAIReport::getCreatedBy() const {
    return m_created_by;
}
void OAIReport::setCreatedBy(const QString &created_by) {
    m_created_by = created_by;
    m_created_by_isSet = true;
}

bool OAIReport::is_created_by_Set() const{
    return m_created_by_isSet;
}

bool OAIReport::is_created_by_Valid() const{
    return m_created_by_isValid;
}

qint32 OAIReport::getCreatedChecksCount() const {
    return m_created_checks_count;
}
void OAIReport::setCreatedChecksCount(const qint32 &created_checks_count) {
    m_created_checks_count = created_checks_count;
    m_created_checks_count_isSet = true;
}

bool OAIReport::is_created_checks_count_Set() const{
    return m_created_checks_count_isSet;
}

bool OAIReport::is_created_checks_count_Valid() const{
    return m_created_checks_count_isValid;
}

QDateTime OAIReport::getCreationDate() const {
    return m_creation_date;
}
void OAIReport::setCreationDate(const QDateTime &creation_date) {
    m_creation_date = creation_date;
    m_creation_date_isSet = true;
}

bool OAIReport::is_creation_date_Set() const{
    return m_creation_date_isSet;
}

bool OAIReport::is_creation_date_Valid() const{
    return m_creation_date_isValid;
}

bool OAIReport::isHasData() const {
    return m_has_data;
}
void OAIReport::setHasData(const bool &has_data) {
    m_has_data = has_data;
    m_has_data_isSet = true;
}

bool OAIReport::is_has_data_Set() const{
    return m_has_data_isSet;
}

bool OAIReport::is_has_data_Valid() const{
    return m_has_data_isValid;
}

QString OAIReport::getId() const {
    return m_id;
}
void OAIReport::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIReport::is_id_Set() const{
    return m_id_isSet;
}

bool OAIReport::is_id_Valid() const{
    return m_id_isValid;
}

qint32 OAIReport::getInvalidChecksCount() const {
    return m_invalid_checks_count;
}
void OAIReport::setInvalidChecksCount(const qint32 &invalid_checks_count) {
    m_invalid_checks_count = invalid_checks_count;
    m_invalid_checks_count_isSet = true;
}

bool OAIReport::is_invalid_checks_count_Set() const{
    return m_invalid_checks_count_isSet;
}

bool OAIReport::is_invalid_checks_count_Valid() const{
    return m_invalid_checks_count_isValid;
}

QString OAIReport::getName() const {
    return m_name;
}
void OAIReport::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIReport::is_name_Set() const{
    return m_name_isSet;
}

bool OAIReport::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAIReport::getSize() const {
    return m_size;
}
void OAIReport::setSize(const qint32 &size) {
    m_size = size;
    m_size_isSet = true;
}

bool OAIReport::is_size_Set() const{
    return m_size_isSet;
}

bool OAIReport::is_size_Valid() const{
    return m_size_isValid;
}

QDateTime OAIReport::getUpdateDate() const {
    return m_update_date;
}
void OAIReport::setUpdateDate(const QDateTime &update_date) {
    m_update_date = update_date;
    m_update_date_isSet = true;
}

bool OAIReport::is_update_date_Set() const{
    return m_update_date_isSet;
}

bool OAIReport::is_update_date_Valid() const{
    return m_update_date_isValid;
}

bool OAIReport::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_created_by_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_checks_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_creation_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_invalid_checks_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_size_isSet) {
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

bool OAIReport::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_creation_date_isValid && m_id_isValid && m_name_isValid && m_update_date_isValid && true;
}

} // namespace OpenAPI
