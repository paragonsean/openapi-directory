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

#include "OAICheckDetails.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICheckDetails::OAICheckDetails(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICheckDetails::OAICheckDetails() {
    this->initializeModel();
}

OAICheckDetails::~OAICheckDetails() {}

void OAICheckDetails::initializeModel() {

    m_check_id_isSet = false;
    m_check_id_isValid = false;

    m_data_set_isSet = false;
    m_data_set_isValid = false;

    m_database_name_isSet = false;
    m_database_name_isValid = false;

    m_group_isSet = false;
    m_group_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_result_isSet = false;
    m_result_isValid = false;

    m_score_isSet = false;
    m_score_isValid = false;

    m_tables_isSet = false;
    m_tables_isValid = false;
}

void OAICheckDetails::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICheckDetails::fromJsonObject(QJsonObject json) {

    m_check_id_isValid = ::OpenAPI::fromJsonValue(m_check_id, json[QString("check_id")]);
    m_check_id_isSet = !json[QString("check_id")].isNull() && m_check_id_isValid;

    m_data_set_isValid = ::OpenAPI::fromJsonValue(m_data_set, json[QString("data_set")]);
    m_data_set_isSet = !json[QString("data_set")].isNull() && m_data_set_isValid;

    m_database_name_isValid = ::OpenAPI::fromJsonValue(m_database_name, json[QString("database_name")]);
    m_database_name_isSet = !json[QString("database_name")].isNull() && m_database_name_isValid;

    m_group_isValid = ::OpenAPI::fromJsonValue(m_group, json[QString("group")]);
    m_group_isSet = !json[QString("group")].isNull() && m_group_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_result_isValid = ::OpenAPI::fromJsonValue(m_result, json[QString("result")]);
    m_result_isSet = !json[QString("result")].isNull() && m_result_isValid;

    m_score_isValid = ::OpenAPI::fromJsonValue(m_score, json[QString("score")]);
    m_score_isSet = !json[QString("score")].isNull() && m_score_isValid;

    m_tables_isValid = ::OpenAPI::fromJsonValue(m_tables, json[QString("tables")]);
    m_tables_isSet = !json[QString("tables")].isNull() && m_tables_isValid;
}

QString OAICheckDetails::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICheckDetails::asJsonObject() const {
    QJsonObject obj;
    if (m_check_id_isSet) {
        obj.insert(QString("check_id"), ::OpenAPI::toJsonValue(m_check_id));
    }
    if (m_data_set_isSet) {
        obj.insert(QString("data_set"), ::OpenAPI::toJsonValue(m_data_set));
    }
    if (m_database_name_isSet) {
        obj.insert(QString("database_name"), ::OpenAPI::toJsonValue(m_database_name));
    }
    if (m_group_isSet) {
        obj.insert(QString("group"), ::OpenAPI::toJsonValue(m_group));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_result_isSet) {
        obj.insert(QString("result"), ::OpenAPI::toJsonValue(m_result));
    }
    if (m_score_isSet) {
        obj.insert(QString("score"), ::OpenAPI::toJsonValue(m_score));
    }
    if (m_tables.size() > 0) {
        obj.insert(QString("tables"), ::OpenAPI::toJsonValue(m_tables));
    }
    return obj;
}

QString OAICheckDetails::getCheckId() const {
    return m_check_id;
}
void OAICheckDetails::setCheckId(const QString &check_id) {
    m_check_id = check_id;
    m_check_id_isSet = true;
}

bool OAICheckDetails::is_check_id_Set() const{
    return m_check_id_isSet;
}

bool OAICheckDetails::is_check_id_Valid() const{
    return m_check_id_isValid;
}

QString OAICheckDetails::getDataSet() const {
    return m_data_set;
}
void OAICheckDetails::setDataSet(const QString &data_set) {
    m_data_set = data_set;
    m_data_set_isSet = true;
}

bool OAICheckDetails::is_data_set_Set() const{
    return m_data_set_isSet;
}

bool OAICheckDetails::is_data_set_Valid() const{
    return m_data_set_isValid;
}

QString OAICheckDetails::getDatabaseName() const {
    return m_database_name;
}
void OAICheckDetails::setDatabaseName(const QString &database_name) {
    m_database_name = database_name;
    m_database_name_isSet = true;
}

bool OAICheckDetails::is_database_name_Set() const{
    return m_database_name_isSet;
}

bool OAICheckDetails::is_database_name_Valid() const{
    return m_database_name_isValid;
}

QString OAICheckDetails::getGroup() const {
    return m_group;
}
void OAICheckDetails::setGroup(const QString &group) {
    m_group = group;
    m_group_isSet = true;
}

bool OAICheckDetails::is_group_Set() const{
    return m_group_isSet;
}

bool OAICheckDetails::is_group_Valid() const{
    return m_group_isValid;
}

QString OAICheckDetails::getId() const {
    return m_id;
}
void OAICheckDetails::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICheckDetails::is_id_Set() const{
    return m_id_isSet;
}

bool OAICheckDetails::is_id_Valid() const{
    return m_id_isValid;
}

QString OAICheckDetails::getResult() const {
    return m_result;
}
void OAICheckDetails::setResult(const QString &result) {
    m_result = result;
    m_result_isSet = true;
}

bool OAICheckDetails::is_result_Set() const{
    return m_result_isSet;
}

bool OAICheckDetails::is_result_Valid() const{
    return m_result_isValid;
}

double OAICheckDetails::getScore() const {
    return m_score;
}
void OAICheckDetails::setScore(const double &score) {
    m_score = score;
    m_score_isSet = true;
}

bool OAICheckDetails::is_score_Set() const{
    return m_score_isSet;
}

bool OAICheckDetails::is_score_Valid() const{
    return m_score_isValid;
}

QList<OAITable> OAICheckDetails::getTables() const {
    return m_tables;
}
void OAICheckDetails::setTables(const QList<OAITable> &tables) {
    m_tables = tables;
    m_tables_isSet = true;
}

bool OAICheckDetails::is_tables_Set() const{
    return m_tables_isSet;
}

bool OAICheckDetails::is_tables_Valid() const{
    return m_tables_isValid;
}

bool OAICheckDetails::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_check_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_data_set_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_database_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_group_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_result_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tables.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICheckDetails::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_check_id_isValid && m_data_set_isValid && m_database_name_isValid && m_group_isValid && m_id_isValid && m_result_isValid && m_score_isValid && m_tables_isValid && true;
}

} // namespace OpenAPI
