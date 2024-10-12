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

#include "OAISummary.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISummary::OAISummary(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISummary::OAISummary() {
    this->initializeModel();
}

OAISummary::~OAISummary() {}

void OAISummary::initializeModel() {

    m_date_of_birth_isSet = false;
    m_date_of_birth_isValid = false;

    m_death_date_isSet = false;
    m_death_date_isValid = false;

    m_drivers_license_isSet = false;
    m_drivers_license_isValid = false;

    m_gender_isSet = false;
    m_gender_isValid = false;

    m_identity_status_isSet = false;
    m_identity_status_isValid = false;

    m_names_found_isSet = false;
    m_names_found_isValid = false;

    m_nss_isSet = false;
    m_nss_isValid = false;

    m_rfc_isSet = false;
    m_rfc_isValid = false;
}

void OAISummary::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISummary::fromJsonObject(QJsonObject json) {

    m_date_of_birth_isValid = ::OpenAPI::fromJsonValue(m_date_of_birth, json[QString("date_of_birth")]);
    m_date_of_birth_isSet = !json[QString("date_of_birth")].isNull() && m_date_of_birth_isValid;

    m_death_date_isValid = ::OpenAPI::fromJsonValue(m_death_date, json[QString("death_date")]);
    m_death_date_isSet = !json[QString("death_date")].isNull() && m_death_date_isValid;

    m_drivers_license_isValid = ::OpenAPI::fromJsonValue(m_drivers_license, json[QString("drivers_license")]);
    m_drivers_license_isSet = !json[QString("drivers_license")].isNull() && m_drivers_license_isValid;

    m_gender_isValid = ::OpenAPI::fromJsonValue(m_gender, json[QString("gender")]);
    m_gender_isSet = !json[QString("gender")].isNull() && m_gender_isValid;

    m_identity_status_isValid = ::OpenAPI::fromJsonValue(m_identity_status, json[QString("identity_status")]);
    m_identity_status_isSet = !json[QString("identity_status")].isNull() && m_identity_status_isValid;

    m_names_found_isValid = ::OpenAPI::fromJsonValue(m_names_found, json[QString("names_found")]);
    m_names_found_isSet = !json[QString("names_found")].isNull() && m_names_found_isValid;

    m_nss_isValid = ::OpenAPI::fromJsonValue(m_nss, json[QString("nss")]);
    m_nss_isSet = !json[QString("nss")].isNull() && m_nss_isValid;

    m_rfc_isValid = ::OpenAPI::fromJsonValue(m_rfc, json[QString("rfc")]);
    m_rfc_isSet = !json[QString("rfc")].isNull() && m_rfc_isValid;
}

QString OAISummary::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISummary::asJsonObject() const {
    QJsonObject obj;
    if (m_date_of_birth_isSet) {
        obj.insert(QString("date_of_birth"), ::OpenAPI::toJsonValue(m_date_of_birth));
    }
    if (m_death_date_isSet) {
        obj.insert(QString("death_date"), ::OpenAPI::toJsonValue(m_death_date));
    }
    if (m_drivers_license_isSet) {
        obj.insert(QString("drivers_license"), ::OpenAPI::toJsonValue(m_drivers_license));
    }
    if (m_gender_isSet) {
        obj.insert(QString("gender"), ::OpenAPI::toJsonValue(m_gender));
    }
    if (m_identity_status_isSet) {
        obj.insert(QString("identity_status"), ::OpenAPI::toJsonValue(m_identity_status));
    }
    if (m_names_found.size() > 0) {
        obj.insert(QString("names_found"), ::OpenAPI::toJsonValue(m_names_found));
    }
    if (m_nss_isSet) {
        obj.insert(QString("nss"), ::OpenAPI::toJsonValue(m_nss));
    }
    if (m_rfc_isSet) {
        obj.insert(QString("rfc"), ::OpenAPI::toJsonValue(m_rfc));
    }
    return obj;
}

QDateTime OAISummary::getDateOfBirth() const {
    return m_date_of_birth;
}
void OAISummary::setDateOfBirth(const QDateTime &date_of_birth) {
    m_date_of_birth = date_of_birth;
    m_date_of_birth_isSet = true;
}

bool OAISummary::is_date_of_birth_Set() const{
    return m_date_of_birth_isSet;
}

bool OAISummary::is_date_of_birth_Valid() const{
    return m_date_of_birth_isValid;
}

QDateTime OAISummary::getDeathDate() const {
    return m_death_date;
}
void OAISummary::setDeathDate(const QDateTime &death_date) {
    m_death_date = death_date;
    m_death_date_isSet = true;
}

bool OAISummary::is_death_date_Set() const{
    return m_death_date_isSet;
}

bool OAISummary::is_death_date_Valid() const{
    return m_death_date_isValid;
}

QString OAISummary::getDriversLicense() const {
    return m_drivers_license;
}
void OAISummary::setDriversLicense(const QString &drivers_license) {
    m_drivers_license = drivers_license;
    m_drivers_license_isSet = true;
}

bool OAISummary::is_drivers_license_Set() const{
    return m_drivers_license_isSet;
}

bool OAISummary::is_drivers_license_Valid() const{
    return m_drivers_license_isValid;
}

QString OAISummary::getGender() const {
    return m_gender;
}
void OAISummary::setGender(const QString &gender) {
    m_gender = gender;
    m_gender_isSet = true;
}

bool OAISummary::is_gender_Set() const{
    return m_gender_isSet;
}

bool OAISummary::is_gender_Valid() const{
    return m_gender_isValid;
}

QString OAISummary::getIdentityStatus() const {
    return m_identity_status;
}
void OAISummary::setIdentityStatus(const QString &identity_status) {
    m_identity_status = identity_status;
    m_identity_status_isSet = true;
}

bool OAISummary::is_identity_status_Set() const{
    return m_identity_status_isSet;
}

bool OAISummary::is_identity_status_Valid() const{
    return m_identity_status_isValid;
}

QList<OAINameFound> OAISummary::getNamesFound() const {
    return m_names_found;
}
void OAISummary::setNamesFound(const QList<OAINameFound> &names_found) {
    m_names_found = names_found;
    m_names_found_isSet = true;
}

bool OAISummary::is_names_found_Set() const{
    return m_names_found_isSet;
}

bool OAISummary::is_names_found_Valid() const{
    return m_names_found_isValid;
}

QString OAISummary::getNss() const {
    return m_nss;
}
void OAISummary::setNss(const QString &nss) {
    m_nss = nss;
    m_nss_isSet = true;
}

bool OAISummary::is_nss_Set() const{
    return m_nss_isSet;
}

bool OAISummary::is_nss_Valid() const{
    return m_nss_isValid;
}

QString OAISummary::getRfc() const {
    return m_rfc;
}
void OAISummary::setRfc(const QString &rfc) {
    m_rfc = rfc;
    m_rfc_isSet = true;
}

bool OAISummary::is_rfc_Set() const{
    return m_rfc_isSet;
}

bool OAISummary::is_rfc_Valid() const{
    return m_rfc_isValid;
}

bool OAISummary::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_date_of_birth_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_death_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_drivers_license_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gender_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_identity_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_names_found.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_nss_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rfc_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISummary::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_names_found_isValid && true;
}

} // namespace OpenAPI
