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

#include "OAIAPIKeyVersion.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAPIKeyVersion::OAIAPIKeyVersion(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAPIKeyVersion::OAIAPIKeyVersion() {
    this->initializeModel();
}

OAIAPIKeyVersion::~OAIAPIKeyVersion() {}

void OAIAPIKeyVersion::initializeModel() {

    m_changelog_isSet = false;
    m_changelog_isValid = false;

    m_expiration_date_isSet = false;
    m_expiration_date_isValid = false;

    m_release_date_isSet = false;
    m_release_date_isValid = false;

    m_version_isSet = false;
    m_version_isValid = false;
}

void OAIAPIKeyVersion::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAPIKeyVersion::fromJsonObject(QJsonObject json) {

    m_changelog_isValid = ::OpenAPI::fromJsonValue(m_changelog, json[QString("changelog")]);
    m_changelog_isSet = !json[QString("changelog")].isNull() && m_changelog_isValid;

    m_expiration_date_isValid = ::OpenAPI::fromJsonValue(m_expiration_date, json[QString("expiration_date")]);
    m_expiration_date_isSet = !json[QString("expiration_date")].isNull() && m_expiration_date_isValid;

    m_release_date_isValid = ::OpenAPI::fromJsonValue(m_release_date, json[QString("release_date")]);
    m_release_date_isSet = !json[QString("release_date")].isNull() && m_release_date_isValid;

    m_version_isValid = ::OpenAPI::fromJsonValue(m_version, json[QString("version")]);
    m_version_isSet = !json[QString("version")].isNull() && m_version_isValid;
}

QString OAIAPIKeyVersion::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAPIKeyVersion::asJsonObject() const {
    QJsonObject obj;
    if (m_changelog.isSet()) {
        obj.insert(QString("changelog"), ::OpenAPI::toJsonValue(m_changelog));
    }
    if (m_expiration_date_isSet) {
        obj.insert(QString("expiration_date"), ::OpenAPI::toJsonValue(m_expiration_date));
    }
    if (m_release_date_isSet) {
        obj.insert(QString("release_date"), ::OpenAPI::toJsonValue(m_release_date));
    }
    if (m_version_isSet) {
        obj.insert(QString("version"), ::OpenAPI::toJsonValue(m_version));
    }
    return obj;
}

OAIAPIKeyVersionChangelog OAIAPIKeyVersion::getChangelog() const {
    return m_changelog;
}
void OAIAPIKeyVersion::setChangelog(const OAIAPIKeyVersionChangelog &changelog) {
    m_changelog = changelog;
    m_changelog_isSet = true;
}

bool OAIAPIKeyVersion::is_changelog_Set() const{
    return m_changelog_isSet;
}

bool OAIAPIKeyVersion::is_changelog_Valid() const{
    return m_changelog_isValid;
}

QDate OAIAPIKeyVersion::getExpirationDate() const {
    return m_expiration_date;
}
void OAIAPIKeyVersion::setExpirationDate(const QDate &expiration_date) {
    m_expiration_date = expiration_date;
    m_expiration_date_isSet = true;
}

bool OAIAPIKeyVersion::is_expiration_date_Set() const{
    return m_expiration_date_isSet;
}

bool OAIAPIKeyVersion::is_expiration_date_Valid() const{
    return m_expiration_date_isValid;
}

QDate OAIAPIKeyVersion::getReleaseDate() const {
    return m_release_date;
}
void OAIAPIKeyVersion::setReleaseDate(const QDate &release_date) {
    m_release_date = release_date;
    m_release_date_isSet = true;
}

bool OAIAPIKeyVersion::is_release_date_Set() const{
    return m_release_date_isSet;
}

bool OAIAPIKeyVersion::is_release_date_Valid() const{
    return m_release_date_isValid;
}

QString OAIAPIKeyVersion::getVersion() const {
    return m_version;
}
void OAIAPIKeyVersion::setVersion(const QString &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAIAPIKeyVersion::is_version_Set() const{
    return m_version_isSet;
}

bool OAIAPIKeyVersion::is_version_Valid() const{
    return m_version_isValid;
}

bool OAIAPIKeyVersion::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_changelog.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_expiration_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_release_date_isSet) {
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

bool OAIAPIKeyVersion::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
