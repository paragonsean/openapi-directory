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

#include "OAIRule.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRule::OAIRule(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRule::OAIRule() {
    this->initializeModel();
}

OAIRule::~OAIRule() {}

void OAIRule::initializeModel() {

    m_level_isSet = false;
    m_level_isValid = false;

    m_operation_isSet = false;
    m_operation_isValid = false;

    m_outcome_label_isSet = false;
    m_outcome_label_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIRule::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRule::fromJsonObject(QJsonObject json) {

    m_level_isValid = ::OpenAPI::fromJsonValue(m_level, json[QString("level")]);
    m_level_isSet = !json[QString("level")].isNull() && m_level_isValid;

    m_operation_isValid = ::OpenAPI::fromJsonValue(m_operation, json[QString("operation")]);
    m_operation_isSet = !json[QString("operation")].isNull() && m_operation_isValid;

    m_outcome_label_isValid = ::OpenAPI::fromJsonValue(m_outcome_label, json[QString("outcome_label")]);
    m_outcome_label_isSet = !json[QString("outcome_label")].isNull() && m_outcome_label_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIRule::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRule::asJsonObject() const {
    QJsonObject obj;
    if (m_level_isSet) {
        obj.insert(QString("level"), ::OpenAPI::toJsonValue(m_level));
    }
    if (m_operation_isSet) {
        obj.insert(QString("operation"), ::OpenAPI::toJsonValue(m_operation));
    }
    if (m_outcome_label_isSet) {
        obj.insert(QString("outcome_label"), ::OpenAPI::toJsonValue(m_outcome_label));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIRule::getLevel() const {
    return m_level;
}
void OAIRule::setLevel(const QString &level) {
    m_level = level;
    m_level_isSet = true;
}

bool OAIRule::is_level_Set() const{
    return m_level_isSet;
}

bool OAIRule::is_level_Valid() const{
    return m_level_isValid;
}

QString OAIRule::getOperation() const {
    return m_operation;
}
void OAIRule::setOperation(const QString &operation) {
    m_operation = operation;
    m_operation_isSet = true;
}

bool OAIRule::is_operation_Set() const{
    return m_operation_isSet;
}

bool OAIRule::is_operation_Valid() const{
    return m_operation_isValid;
}

QString OAIRule::getOutcomeLabel() const {
    return m_outcome_label;
}
void OAIRule::setOutcomeLabel(const QString &outcome_label) {
    m_outcome_label = outcome_label;
    m_outcome_label_isSet = true;
}

bool OAIRule::is_outcome_label_Set() const{
    return m_outcome_label_isSet;
}

bool OAIRule::is_outcome_label_Valid() const{
    return m_outcome_label_isValid;
}

double OAIRule::getValue() const {
    return m_value;
}
void OAIRule::setValue(const double &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIRule::is_value_Set() const{
    return m_value_isSet;
}

bool OAIRule::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIRule::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_level_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_operation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_outcome_label_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRule::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_level_isValid && m_operation_isValid && m_value_isValid && true;
}

} // namespace OpenAPI
