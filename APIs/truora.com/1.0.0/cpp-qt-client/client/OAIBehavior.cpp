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

#include "OAIBehavior.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBehavior::OAIBehavior(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBehavior::OAIBehavior() {
    this->initializeModel();
}

OAIBehavior::~OAIBehavior() {}

void OAIBehavior::initializeModel() {

    m_birth_date_isSet = false;
    m_birth_date_isValid = false;

    m_country_isSet = false;
    m_country_isValid = false;

    m_creation_date_isSet = false;
    m_creation_date_isValid = false;

    m_document_id_isSet = false;
    m_document_id_isValid = false;

    m_document_type_isSet = false;
    m_document_type_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_feedback_date_isSet = false;
    m_feedback_date_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_phone_number_isSet = false;
    m_phone_number_isValid = false;

    m_reason_isSet = false;
    m_reason_isValid = false;
}

void OAIBehavior::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBehavior::fromJsonObject(QJsonObject json) {

    m_birth_date_isValid = ::OpenAPI::fromJsonValue(m_birth_date, json[QString("birth_date")]);
    m_birth_date_isSet = !json[QString("birth_date")].isNull() && m_birth_date_isValid;

    m_country_isValid = ::OpenAPI::fromJsonValue(m_country, json[QString("country")]);
    m_country_isSet = !json[QString("country")].isNull() && m_country_isValid;

    m_creation_date_isValid = ::OpenAPI::fromJsonValue(m_creation_date, json[QString("creation_date")]);
    m_creation_date_isSet = !json[QString("creation_date")].isNull() && m_creation_date_isValid;

    m_document_id_isValid = ::OpenAPI::fromJsonValue(m_document_id, json[QString("document_id")]);
    m_document_id_isSet = !json[QString("document_id")].isNull() && m_document_id_isValid;

    m_document_type_isValid = ::OpenAPI::fromJsonValue(m_document_type, json[QString("document_type")]);
    m_document_type_isSet = !json[QString("document_type")].isNull() && m_document_type_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_feedback_date_isValid = ::OpenAPI::fromJsonValue(m_feedback_date, json[QString("feedback_date")]);
    m_feedback_date_isSet = !json[QString("feedback_date")].isNull() && m_feedback_date_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("first_name")]);
    m_first_name_isSet = !json[QString("first_name")].isNull() && m_first_name_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("last_name")]);
    m_last_name_isSet = !json[QString("last_name")].isNull() && m_last_name_isValid;

    m_phone_number_isValid = ::OpenAPI::fromJsonValue(m_phone_number, json[QString("phone_number")]);
    m_phone_number_isSet = !json[QString("phone_number")].isNull() && m_phone_number_isValid;

    m_reason_isValid = ::OpenAPI::fromJsonValue(m_reason, json[QString("reason")]);
    m_reason_isSet = !json[QString("reason")].isNull() && m_reason_isValid;
}

QString OAIBehavior::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBehavior::asJsonObject() const {
    QJsonObject obj;
    if (m_birth_date_isSet) {
        obj.insert(QString("birth_date"), ::OpenAPI::toJsonValue(m_birth_date));
    }
    if (m_country_isSet) {
        obj.insert(QString("country"), ::OpenAPI::toJsonValue(m_country));
    }
    if (m_creation_date_isSet) {
        obj.insert(QString("creation_date"), ::OpenAPI::toJsonValue(m_creation_date));
    }
    if (m_document_id_isSet) {
        obj.insert(QString("document_id"), ::OpenAPI::toJsonValue(m_document_id));
    }
    if (m_document_type_isSet) {
        obj.insert(QString("document_type"), ::OpenAPI::toJsonValue(m_document_type));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_feedback_date_isSet) {
        obj.insert(QString("feedback_date"), ::OpenAPI::toJsonValue(m_feedback_date));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("first_name"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("last_name"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_phone_number_isSet) {
        obj.insert(QString("phone_number"), ::OpenAPI::toJsonValue(m_phone_number));
    }
    if (m_reason_isSet) {
        obj.insert(QString("reason"), ::OpenAPI::toJsonValue(m_reason));
    }
    return obj;
}

QDate OAIBehavior::getBirthDate() const {
    return m_birth_date;
}
void OAIBehavior::setBirthDate(const QDate &birth_date) {
    m_birth_date = birth_date;
    m_birth_date_isSet = true;
}

bool OAIBehavior::is_birth_date_Set() const{
    return m_birth_date_isSet;
}

bool OAIBehavior::is_birth_date_Valid() const{
    return m_birth_date_isValid;
}

QString OAIBehavior::getCountry() const {
    return m_country;
}
void OAIBehavior::setCountry(const QString &country) {
    m_country = country;
    m_country_isSet = true;
}

bool OAIBehavior::is_country_Set() const{
    return m_country_isSet;
}

bool OAIBehavior::is_country_Valid() const{
    return m_country_isValid;
}

QDateTime OAIBehavior::getCreationDate() const {
    return m_creation_date;
}
void OAIBehavior::setCreationDate(const QDateTime &creation_date) {
    m_creation_date = creation_date;
    m_creation_date_isSet = true;
}

bool OAIBehavior::is_creation_date_Set() const{
    return m_creation_date_isSet;
}

bool OAIBehavior::is_creation_date_Valid() const{
    return m_creation_date_isValid;
}

QString OAIBehavior::getDocumentId() const {
    return m_document_id;
}
void OAIBehavior::setDocumentId(const QString &document_id) {
    m_document_id = document_id;
    m_document_id_isSet = true;
}

bool OAIBehavior::is_document_id_Set() const{
    return m_document_id_isSet;
}

bool OAIBehavior::is_document_id_Valid() const{
    return m_document_id_isValid;
}

QString OAIBehavior::getDocumentType() const {
    return m_document_type;
}
void OAIBehavior::setDocumentType(const QString &document_type) {
    m_document_type = document_type;
    m_document_type_isSet = true;
}

bool OAIBehavior::is_document_type_Set() const{
    return m_document_type_isSet;
}

bool OAIBehavior::is_document_type_Valid() const{
    return m_document_type_isValid;
}

QString OAIBehavior::getEmail() const {
    return m_email;
}
void OAIBehavior::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIBehavior::is_email_Set() const{
    return m_email_isSet;
}

bool OAIBehavior::is_email_Valid() const{
    return m_email_isValid;
}

QDate OAIBehavior::getFeedbackDate() const {
    return m_feedback_date;
}
void OAIBehavior::setFeedbackDate(const QDate &feedback_date) {
    m_feedback_date = feedback_date;
    m_feedback_date_isSet = true;
}

bool OAIBehavior::is_feedback_date_Set() const{
    return m_feedback_date_isSet;
}

bool OAIBehavior::is_feedback_date_Valid() const{
    return m_feedback_date_isValid;
}

QString OAIBehavior::getFirstName() const {
    return m_first_name;
}
void OAIBehavior::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAIBehavior::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAIBehavior::is_first_name_Valid() const{
    return m_first_name_isValid;
}

QString OAIBehavior::getLastName() const {
    return m_last_name;
}
void OAIBehavior::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAIBehavior::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAIBehavior::is_last_name_Valid() const{
    return m_last_name_isValid;
}

QString OAIBehavior::getPhoneNumber() const {
    return m_phone_number;
}
void OAIBehavior::setPhoneNumber(const QString &phone_number) {
    m_phone_number = phone_number;
    m_phone_number_isSet = true;
}

bool OAIBehavior::is_phone_number_Set() const{
    return m_phone_number_isSet;
}

bool OAIBehavior::is_phone_number_Valid() const{
    return m_phone_number_isValid;
}

QString OAIBehavior::getReason() const {
    return m_reason;
}
void OAIBehavior::setReason(const QString &reason) {
    m_reason = reason;
    m_reason_isSet = true;
}

bool OAIBehavior::is_reason_Set() const{
    return m_reason_isSet;
}

bool OAIBehavior::is_reason_Valid() const{
    return m_reason_isValid;
}

bool OAIBehavior::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_birth_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_creation_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_document_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_document_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_feedback_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phone_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reason_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBehavior::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_birth_date_isValid && m_country_isValid && m_document_id_isValid && m_document_type_isValid && m_email_isValid && m_feedback_date_isValid && m_first_name_isValid && m_last_name_isValid && m_reason_isValid && true;
}

} // namespace OpenAPI
