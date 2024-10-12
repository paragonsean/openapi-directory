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

#include "OAICreateAPIKeyInput.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateAPIKeyInput::OAICreateAPIKeyInput(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateAPIKeyInput::OAICreateAPIKeyInput() {
    this->initializeModel();
}

OAICreateAPIKeyInput::~OAICreateAPIKeyInput() {}

void OAICreateAPIKeyInput::initializeModel() {

    m_days_exp_isSet = false;
    m_days_exp_isValid = false;

    m_key_name_isSet = false;
    m_key_name_isValid = false;

    m_tenant_isSet = false;
    m_tenant_isValid = false;

    m_version_isSet = false;
    m_version_isValid = false;
}

void OAICreateAPIKeyInput::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateAPIKeyInput::fromJsonObject(QJsonObject json) {

    m_days_exp_isValid = ::OpenAPI::fromJsonValue(m_days_exp, json[QString("days_exp")]);
    m_days_exp_isSet = !json[QString("days_exp")].isNull() && m_days_exp_isValid;

    m_key_name_isValid = ::OpenAPI::fromJsonValue(m_key_name, json[QString("key_name")]);
    m_key_name_isSet = !json[QString("key_name")].isNull() && m_key_name_isValid;

    m_tenant_isValid = ::OpenAPI::fromJsonValue(m_tenant, json[QString("tenant")]);
    m_tenant_isSet = !json[QString("tenant")].isNull() && m_tenant_isValid;

    m_version_isValid = ::OpenAPI::fromJsonValue(m_version, json[QString("version")]);
    m_version_isSet = !json[QString("version")].isNull() && m_version_isValid;
}

QString OAICreateAPIKeyInput::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateAPIKeyInput::asJsonObject() const {
    QJsonObject obj;
    if (m_days_exp_isSet) {
        obj.insert(QString("days_exp"), ::OpenAPI::toJsonValue(m_days_exp));
    }
    if (m_key_name_isSet) {
        obj.insert(QString("key_name"), ::OpenAPI::toJsonValue(m_key_name));
    }
    if (m_tenant_isSet) {
        obj.insert(QString("tenant"), ::OpenAPI::toJsonValue(m_tenant));
    }
    if (m_version_isSet) {
        obj.insert(QString("version"), ::OpenAPI::toJsonValue(m_version));
    }
    return obj;
}

qint32 OAICreateAPIKeyInput::getDaysExp() const {
    return m_days_exp;
}
void OAICreateAPIKeyInput::setDaysExp(const qint32 &days_exp) {
    m_days_exp = days_exp;
    m_days_exp_isSet = true;
}

bool OAICreateAPIKeyInput::is_days_exp_Set() const{
    return m_days_exp_isSet;
}

bool OAICreateAPIKeyInput::is_days_exp_Valid() const{
    return m_days_exp_isValid;
}

QString OAICreateAPIKeyInput::getKeyName() const {
    return m_key_name;
}
void OAICreateAPIKeyInput::setKeyName(const QString &key_name) {
    m_key_name = key_name;
    m_key_name_isSet = true;
}

bool OAICreateAPIKeyInput::is_key_name_Set() const{
    return m_key_name_isSet;
}

bool OAICreateAPIKeyInput::is_key_name_Valid() const{
    return m_key_name_isValid;
}

QString OAICreateAPIKeyInput::getTenant() const {
    return m_tenant;
}
void OAICreateAPIKeyInput::setTenant(const QString &tenant) {
    m_tenant = tenant;
    m_tenant_isSet = true;
}

bool OAICreateAPIKeyInput::is_tenant_Set() const{
    return m_tenant_isSet;
}

bool OAICreateAPIKeyInput::is_tenant_Valid() const{
    return m_tenant_isValid;
}

QString OAICreateAPIKeyInput::getVersion() const {
    return m_version;
}
void OAICreateAPIKeyInput::setVersion(const QString &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAICreateAPIKeyInput::is_version_Set() const{
    return m_version_isSet;
}

bool OAICreateAPIKeyInput::is_version_Valid() const{
    return m_version_isValid;
}

bool OAICreateAPIKeyInput::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_days_exp_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_key_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tenant_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateAPIKeyInput::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_days_exp_isValid && m_key_name_isValid && m_tenant_isValid && m_version_isValid && true;
}

} // namespace OpenAPI
