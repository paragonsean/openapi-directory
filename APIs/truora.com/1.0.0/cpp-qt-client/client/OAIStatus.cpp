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

#include "OAIStatus.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIStatus::OAIStatus(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIStatus::OAIStatus() {
    this->initializeModel();
}

OAIStatus::~OAIStatus() {}

void OAIStatus::initializeModel() {

    m_data_set_isSet = false;
    m_data_set_isValid = false;

    m_database_id_isSet = false;
    m_database_id_isValid = false;

    m_database_name_isSet = false;
    m_database_name_isValid = false;

    m_invalid_inputs_isSet = false;
    m_invalid_inputs_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAIStatus::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIStatus::fromJsonObject(QJsonObject json) {

    m_data_set_isValid = ::OpenAPI::fromJsonValue(m_data_set, json[QString("data_set")]);
    m_data_set_isSet = !json[QString("data_set")].isNull() && m_data_set_isValid;

    m_database_id_isValid = ::OpenAPI::fromJsonValue(m_database_id, json[QString("database_id")]);
    m_database_id_isSet = !json[QString("database_id")].isNull() && m_database_id_isValid;

    m_database_name_isValid = ::OpenAPI::fromJsonValue(m_database_name, json[QString("database_name")]);
    m_database_name_isSet = !json[QString("database_name")].isNull() && m_database_name_isValid;

    m_invalid_inputs_isValid = ::OpenAPI::fromJsonValue(m_invalid_inputs, json[QString("invalid_inputs")]);
    m_invalid_inputs_isSet = !json[QString("invalid_inputs")].isNull() && m_invalid_inputs_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;
}

QString OAIStatus::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIStatus::asJsonObject() const {
    QJsonObject obj;
    if (m_data_set_isSet) {
        obj.insert(QString("data_set"), ::OpenAPI::toJsonValue(m_data_set));
    }
    if (m_database_id_isSet) {
        obj.insert(QString("database_id"), ::OpenAPI::toJsonValue(m_database_id));
    }
    if (m_database_name_isSet) {
        obj.insert(QString("database_name"), ::OpenAPI::toJsonValue(m_database_name));
    }
    if (m_invalid_inputs.size() > 0) {
        obj.insert(QString("invalid_inputs"), ::OpenAPI::toJsonValue(m_invalid_inputs));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

QString OAIStatus::getDataSet() const {
    return m_data_set;
}
void OAIStatus::setDataSet(const QString &data_set) {
    m_data_set = data_set;
    m_data_set_isSet = true;
}

bool OAIStatus::is_data_set_Set() const{
    return m_data_set_isSet;
}

bool OAIStatus::is_data_set_Valid() const{
    return m_data_set_isValid;
}

QString OAIStatus::getDatabaseId() const {
    return m_database_id;
}
void OAIStatus::setDatabaseId(const QString &database_id) {
    m_database_id = database_id;
    m_database_id_isSet = true;
}

bool OAIStatus::is_database_id_Set() const{
    return m_database_id_isSet;
}

bool OAIStatus::is_database_id_Valid() const{
    return m_database_id_isValid;
}

QString OAIStatus::getDatabaseName() const {
    return m_database_name;
}
void OAIStatus::setDatabaseName(const QString &database_name) {
    m_database_name = database_name;
    m_database_name_isSet = true;
}

bool OAIStatus::is_database_name_Set() const{
    return m_database_name_isSet;
}

bool OAIStatus::is_database_name_Valid() const{
    return m_database_name_isValid;
}

QList<QString> OAIStatus::getInvalidInputs() const {
    return m_invalid_inputs;
}
void OAIStatus::setInvalidInputs(const QList<QString> &invalid_inputs) {
    m_invalid_inputs = invalid_inputs;
    m_invalid_inputs_isSet = true;
}

bool OAIStatus::is_invalid_inputs_Set() const{
    return m_invalid_inputs_isSet;
}

bool OAIStatus::is_invalid_inputs_Valid() const{
    return m_invalid_inputs_isValid;
}

QString OAIStatus::getStatus() const {
    return m_status;
}
void OAIStatus::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIStatus::is_status_Set() const{
    return m_status_isSet;
}

bool OAIStatus::is_status_Valid() const{
    return m_status_isValid;
}

bool OAIStatus::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_data_set_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_database_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_database_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_invalid_inputs.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIStatus::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
