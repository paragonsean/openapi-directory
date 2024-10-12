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

#include "OAIConfig.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIConfig::OAIConfig(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIConfig::OAIConfig() {
    this->initializeModel();
}

OAIConfig::~OAIConfig() {}

void OAIConfig::initializeModel() {

    m_client_id_isSet = false;
    m_client_id_isValid = false;

    m_config_id_isSet = false;
    m_config_id_isValid = false;

    m_score_config_isSet = false;
    m_score_config_isValid = false;
}

void OAIConfig::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIConfig::fromJsonObject(QJsonObject json) {

    m_client_id_isValid = ::OpenAPI::fromJsonValue(m_client_id, json[QString("client_id")]);
    m_client_id_isSet = !json[QString("client_id")].isNull() && m_client_id_isValid;

    m_config_id_isValid = ::OpenAPI::fromJsonValue(m_config_id, json[QString("config_id")]);
    m_config_id_isSet = !json[QString("config_id")].isNull() && m_config_id_isValid;

    m_score_config_isValid = ::OpenAPI::fromJsonValue(m_score_config, json[QString("score_config")]);
    m_score_config_isSet = !json[QString("score_config")].isNull() && m_score_config_isValid;
}

QString OAIConfig::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIConfig::asJsonObject() const {
    QJsonObject obj;
    if (m_client_id_isSet) {
        obj.insert(QString("client_id"), ::OpenAPI::toJsonValue(m_client_id));
    }
    if (m_config_id_isSet) {
        obj.insert(QString("config_id"), ::OpenAPI::toJsonValue(m_config_id));
    }
    if (m_score_config.isSet()) {
        obj.insert(QString("score_config"), ::OpenAPI::toJsonValue(m_score_config));
    }
    return obj;
}

QString OAIConfig::getClientId() const {
    return m_client_id;
}
void OAIConfig::setClientId(const QString &client_id) {
    m_client_id = client_id;
    m_client_id_isSet = true;
}

bool OAIConfig::is_client_id_Set() const{
    return m_client_id_isSet;
}

bool OAIConfig::is_client_id_Valid() const{
    return m_client_id_isValid;
}

QString OAIConfig::getConfigId() const {
    return m_config_id;
}
void OAIConfig::setConfigId(const QString &config_id) {
    m_config_id = config_id;
    m_config_id_isSet = true;
}

bool OAIConfig::is_config_id_Set() const{
    return m_config_id_isSet;
}

bool OAIConfig::is_config_id_Valid() const{
    return m_config_id_isValid;
}

OAIScoreConfig OAIConfig::getScoreConfig() const {
    return m_score_config;
}
void OAIConfig::setScoreConfig(const OAIScoreConfig &score_config) {
    m_score_config = score_config;
    m_score_config_isSet = true;
}

bool OAIConfig::is_score_config_Set() const{
    return m_score_config_isSet;
}

bool OAIConfig::is_score_config_Valid() const{
    return m_score_config_isValid;
}

bool OAIConfig::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_client_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_config_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_score_config.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIConfig::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_client_id_isValid && m_config_id_isValid && m_score_config_isValid && true;
}

} // namespace OpenAPI
