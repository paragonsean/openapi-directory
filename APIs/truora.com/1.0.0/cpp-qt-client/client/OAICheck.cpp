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

#include "OAICheck.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICheck::OAICheck(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICheck::OAICheck() {
    this->initializeModel();
}

OAICheck::~OAICheck() {}

void OAICheck::initializeModel() {

    m_birth_certificate_isSet = false;
    m_birth_certificate_isValid = false;

    m_check_id_isSet = false;
    m_check_id_isValid = false;

    m_company_summary_isSet = false;
    m_company_summary_isValid = false;

    m_country_isSet = false;
    m_country_isValid = false;

    m_creation_date_isSet = false;
    m_creation_date_isValid = false;

    m_date_of_birth_isSet = false;
    m_date_of_birth_isValid = false;

    m_diplomatic_id_isSet = false;
    m_diplomatic_id_isValid = false;

    m_driver_license_isSet = false;
    m_driver_license_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_foreign_id_isSet = false;
    m_foreign_id_isValid = false;

    m_homonym_probability_isSet = false;
    m_homonym_probability_isValid = false;

    m_homonym_score_isSet = false;
    m_homonym_score_isValid = false;

    m_homonym_scores_isSet = false;
    m_homonym_scores_isValid = false;

    m_id_score_isSet = false;
    m_id_score_isValid = false;

    m_issue_date_isSet = false;
    m_issue_date_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_license_plate_isSet = false;
    m_license_plate_isValid = false;

    m_national_id_isSet = false;
    m_national_id_isValid = false;

    m_native_country_isSet = false;
    m_native_country_isValid = false;

    m_owner_document_id_isSet = false;
    m_owner_document_id_isValid = false;

    m_owner_document_type_isSet = false;
    m_owner_document_type_isValid = false;

    m_passport_isSet = false;
    m_passport_isValid = false;

    m_payment_date_isSet = false;
    m_payment_date_isValid = false;

    m_pep_isSet = false;
    m_pep_isValid = false;

    m_phone_number_isSet = false;
    m_phone_number_isValid = false;

    m_professional_card_isSet = false;
    m_professional_card_isValid = false;

    m_ptp_isSet = false;
    m_ptp_isValid = false;

    m_region_isSet = false;
    m_region_isValid = false;

    m_report_id_isSet = false;
    m_report_id_isValid = false;

    m_score_isSet = false;
    m_score_isValid = false;

    m_scores_isSet = false;
    m_scores_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_statuses_isSet = false;
    m_statuses_isValid = false;

    m_summary_isSet = false;
    m_summary_isValid = false;

    m_tax_id_isSet = false;
    m_tax_id_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_update_date_isSet = false;
    m_update_date_isValid = false;

    m_vehicle_id_isSet = false;
    m_vehicle_id_isValid = false;

    m_vehicle_summary_isSet = false;
    m_vehicle_summary_isValid = false;

    m_wrong_inputs_isSet = false;
    m_wrong_inputs_isValid = false;
}

void OAICheck::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICheck::fromJsonObject(QJsonObject json) {

    m_birth_certificate_isValid = ::OpenAPI::fromJsonValue(m_birth_certificate, json[QString("birth_certificate")]);
    m_birth_certificate_isSet = !json[QString("birth_certificate")].isNull() && m_birth_certificate_isValid;

    m_check_id_isValid = ::OpenAPI::fromJsonValue(m_check_id, json[QString("check_id")]);
    m_check_id_isSet = !json[QString("check_id")].isNull() && m_check_id_isValid;

    m_company_summary_isValid = ::OpenAPI::fromJsonValue(m_company_summary, json[QString("company_summary")]);
    m_company_summary_isSet = !json[QString("company_summary")].isNull() && m_company_summary_isValid;

    m_country_isValid = ::OpenAPI::fromJsonValue(m_country, json[QString("country")]);
    m_country_isSet = !json[QString("country")].isNull() && m_country_isValid;

    m_creation_date_isValid = ::OpenAPI::fromJsonValue(m_creation_date, json[QString("creation_date")]);
    m_creation_date_isSet = !json[QString("creation_date")].isNull() && m_creation_date_isValid;

    m_date_of_birth_isValid = ::OpenAPI::fromJsonValue(m_date_of_birth, json[QString("date_of_birth")]);
    m_date_of_birth_isSet = !json[QString("date_of_birth")].isNull() && m_date_of_birth_isValid;

    m_diplomatic_id_isValid = ::OpenAPI::fromJsonValue(m_diplomatic_id, json[QString("diplomatic_id")]);
    m_diplomatic_id_isSet = !json[QString("diplomatic_id")].isNull() && m_diplomatic_id_isValid;

    m_driver_license_isValid = ::OpenAPI::fromJsonValue(m_driver_license, json[QString("driver_license")]);
    m_driver_license_isSet = !json[QString("driver_license")].isNull() && m_driver_license_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("first_name")]);
    m_first_name_isSet = !json[QString("first_name")].isNull() && m_first_name_isValid;

    m_foreign_id_isValid = ::OpenAPI::fromJsonValue(m_foreign_id, json[QString("foreign_id")]);
    m_foreign_id_isSet = !json[QString("foreign_id")].isNull() && m_foreign_id_isValid;

    m_homonym_probability_isValid = ::OpenAPI::fromJsonValue(m_homonym_probability, json[QString("homonym_probability")]);
    m_homonym_probability_isSet = !json[QString("homonym_probability")].isNull() && m_homonym_probability_isValid;

    m_homonym_score_isValid = ::OpenAPI::fromJsonValue(m_homonym_score, json[QString("homonym_score")]);
    m_homonym_score_isSet = !json[QString("homonym_score")].isNull() && m_homonym_score_isValid;

    m_homonym_scores_isValid = ::OpenAPI::fromJsonValue(m_homonym_scores, json[QString("homonym_scores")]);
    m_homonym_scores_isSet = !json[QString("homonym_scores")].isNull() && m_homonym_scores_isValid;

    m_id_score_isValid = ::OpenAPI::fromJsonValue(m_id_score, json[QString("id_score")]);
    m_id_score_isSet = !json[QString("id_score")].isNull() && m_id_score_isValid;

    m_issue_date_isValid = ::OpenAPI::fromJsonValue(m_issue_date, json[QString("issue_date")]);
    m_issue_date_isSet = !json[QString("issue_date")].isNull() && m_issue_date_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("last_name")]);
    m_last_name_isSet = !json[QString("last_name")].isNull() && m_last_name_isValid;

    m_license_plate_isValid = ::OpenAPI::fromJsonValue(m_license_plate, json[QString("license_plate")]);
    m_license_plate_isSet = !json[QString("license_plate")].isNull() && m_license_plate_isValid;

    m_national_id_isValid = ::OpenAPI::fromJsonValue(m_national_id, json[QString("national_id")]);
    m_national_id_isSet = !json[QString("national_id")].isNull() && m_national_id_isValid;

    m_native_country_isValid = ::OpenAPI::fromJsonValue(m_native_country, json[QString("native_country")]);
    m_native_country_isSet = !json[QString("native_country")].isNull() && m_native_country_isValid;

    m_owner_document_id_isValid = ::OpenAPI::fromJsonValue(m_owner_document_id, json[QString("owner_document_id")]);
    m_owner_document_id_isSet = !json[QString("owner_document_id")].isNull() && m_owner_document_id_isValid;

    m_owner_document_type_isValid = ::OpenAPI::fromJsonValue(m_owner_document_type, json[QString("owner_document_type")]);
    m_owner_document_type_isSet = !json[QString("owner_document_type")].isNull() && m_owner_document_type_isValid;

    m_passport_isValid = ::OpenAPI::fromJsonValue(m_passport, json[QString("passport")]);
    m_passport_isSet = !json[QString("passport")].isNull() && m_passport_isValid;

    m_payment_date_isValid = ::OpenAPI::fromJsonValue(m_payment_date, json[QString("payment_date")]);
    m_payment_date_isSet = !json[QString("payment_date")].isNull() && m_payment_date_isValid;

    m_pep_isValid = ::OpenAPI::fromJsonValue(m_pep, json[QString("pep")]);
    m_pep_isSet = !json[QString("pep")].isNull() && m_pep_isValid;

    m_phone_number_isValid = ::OpenAPI::fromJsonValue(m_phone_number, json[QString("phone_number")]);
    m_phone_number_isSet = !json[QString("phone_number")].isNull() && m_phone_number_isValid;

    m_professional_card_isValid = ::OpenAPI::fromJsonValue(m_professional_card, json[QString("professional_card")]);
    m_professional_card_isSet = !json[QString("professional_card")].isNull() && m_professional_card_isValid;

    m_ptp_isValid = ::OpenAPI::fromJsonValue(m_ptp, json[QString("ptp")]);
    m_ptp_isSet = !json[QString("ptp")].isNull() && m_ptp_isValid;

    m_region_isValid = ::OpenAPI::fromJsonValue(m_region, json[QString("region")]);
    m_region_isSet = !json[QString("region")].isNull() && m_region_isValid;

    m_report_id_isValid = ::OpenAPI::fromJsonValue(m_report_id, json[QString("report_id")]);
    m_report_id_isSet = !json[QString("report_id")].isNull() && m_report_id_isValid;

    m_score_isValid = ::OpenAPI::fromJsonValue(m_score, json[QString("score")]);
    m_score_isSet = !json[QString("score")].isNull() && m_score_isValid;

    m_scores_isValid = ::OpenAPI::fromJsonValue(m_scores, json[QString("scores")]);
    m_scores_isSet = !json[QString("scores")].isNull() && m_scores_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_statuses_isValid = ::OpenAPI::fromJsonValue(m_statuses, json[QString("statuses")]);
    m_statuses_isSet = !json[QString("statuses")].isNull() && m_statuses_isValid;

    m_summary_isValid = ::OpenAPI::fromJsonValue(m_summary, json[QString("summary")]);
    m_summary_isSet = !json[QString("summary")].isNull() && m_summary_isValid;

    m_tax_id_isValid = ::OpenAPI::fromJsonValue(m_tax_id, json[QString("tax_id")]);
    m_tax_id_isSet = !json[QString("tax_id")].isNull() && m_tax_id_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_update_date_isValid = ::OpenAPI::fromJsonValue(m_update_date, json[QString("update_date")]);
    m_update_date_isSet = !json[QString("update_date")].isNull() && m_update_date_isValid;

    m_vehicle_id_isValid = ::OpenAPI::fromJsonValue(m_vehicle_id, json[QString("vehicle_id")]);
    m_vehicle_id_isSet = !json[QString("vehicle_id")].isNull() && m_vehicle_id_isValid;

    m_vehicle_summary_isValid = ::OpenAPI::fromJsonValue(m_vehicle_summary, json[QString("vehicle_summary")]);
    m_vehicle_summary_isSet = !json[QString("vehicle_summary")].isNull() && m_vehicle_summary_isValid;

    m_wrong_inputs_isValid = ::OpenAPI::fromJsonValue(m_wrong_inputs, json[QString("wrong_inputs")]);
    m_wrong_inputs_isSet = !json[QString("wrong_inputs")].isNull() && m_wrong_inputs_isValid;
}

QString OAICheck::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICheck::asJsonObject() const {
    QJsonObject obj;
    if (m_birth_certificate_isSet) {
        obj.insert(QString("birth_certificate"), ::OpenAPI::toJsonValue(m_birth_certificate));
    }
    if (m_check_id_isSet) {
        obj.insert(QString("check_id"), ::OpenAPI::toJsonValue(m_check_id));
    }
    if (m_company_summary.isSet()) {
        obj.insert(QString("company_summary"), ::OpenAPI::toJsonValue(m_company_summary));
    }
    if (m_country_isSet) {
        obj.insert(QString("country"), ::OpenAPI::toJsonValue(m_country));
    }
    if (m_creation_date_isSet) {
        obj.insert(QString("creation_date"), ::OpenAPI::toJsonValue(m_creation_date));
    }
    if (m_date_of_birth_isSet) {
        obj.insert(QString("date_of_birth"), ::OpenAPI::toJsonValue(m_date_of_birth));
    }
    if (m_diplomatic_id_isSet) {
        obj.insert(QString("diplomatic_id"), ::OpenAPI::toJsonValue(m_diplomatic_id));
    }
    if (m_driver_license_isSet) {
        obj.insert(QString("driver_license"), ::OpenAPI::toJsonValue(m_driver_license));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("first_name"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_foreign_id_isSet) {
        obj.insert(QString("foreign_id"), ::OpenAPI::toJsonValue(m_foreign_id));
    }
    if (m_homonym_probability_isSet) {
        obj.insert(QString("homonym_probability"), ::OpenAPI::toJsonValue(m_homonym_probability));
    }
    if (m_homonym_score_isSet) {
        obj.insert(QString("homonym_score"), ::OpenAPI::toJsonValue(m_homonym_score));
    }
    if (m_homonym_scores.size() > 0) {
        obj.insert(QString("homonym_scores"), ::OpenAPI::toJsonValue(m_homonym_scores));
    }
    if (m_id_score_isSet) {
        obj.insert(QString("id_score"), ::OpenAPI::toJsonValue(m_id_score));
    }
    if (m_issue_date_isSet) {
        obj.insert(QString("issue_date"), ::OpenAPI::toJsonValue(m_issue_date));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("last_name"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_license_plate_isSet) {
        obj.insert(QString("license_plate"), ::OpenAPI::toJsonValue(m_license_plate));
    }
    if (m_national_id_isSet) {
        obj.insert(QString("national_id"), ::OpenAPI::toJsonValue(m_national_id));
    }
    if (m_native_country_isSet) {
        obj.insert(QString("native_country"), ::OpenAPI::toJsonValue(m_native_country));
    }
    if (m_owner_document_id_isSet) {
        obj.insert(QString("owner_document_id"), ::OpenAPI::toJsonValue(m_owner_document_id));
    }
    if (m_owner_document_type_isSet) {
        obj.insert(QString("owner_document_type"), ::OpenAPI::toJsonValue(m_owner_document_type));
    }
    if (m_passport_isSet) {
        obj.insert(QString("passport"), ::OpenAPI::toJsonValue(m_passport));
    }
    if (m_payment_date_isSet) {
        obj.insert(QString("payment_date"), ::OpenAPI::toJsonValue(m_payment_date));
    }
    if (m_pep_isSet) {
        obj.insert(QString("pep"), ::OpenAPI::toJsonValue(m_pep));
    }
    if (m_phone_number_isSet) {
        obj.insert(QString("phone_number"), ::OpenAPI::toJsonValue(m_phone_number));
    }
    if (m_professional_card_isSet) {
        obj.insert(QString("professional_card"), ::OpenAPI::toJsonValue(m_professional_card));
    }
    if (m_ptp_isSet) {
        obj.insert(QString("ptp"), ::OpenAPI::toJsonValue(m_ptp));
    }
    if (m_region_isSet) {
        obj.insert(QString("region"), ::OpenAPI::toJsonValue(m_region));
    }
    if (m_report_id_isSet) {
        obj.insert(QString("report_id"), ::OpenAPI::toJsonValue(m_report_id));
    }
    if (m_score_isSet) {
        obj.insert(QString("score"), ::OpenAPI::toJsonValue(m_score));
    }
    if (m_scores.size() > 0) {
        obj.insert(QString("scores"), ::OpenAPI::toJsonValue(m_scores));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_statuses.size() > 0) {
        obj.insert(QString("statuses"), ::OpenAPI::toJsonValue(m_statuses));
    }
    if (m_summary.isSet()) {
        obj.insert(QString("summary"), ::OpenAPI::toJsonValue(m_summary));
    }
    if (m_tax_id_isSet) {
        obj.insert(QString("tax_id"), ::OpenAPI::toJsonValue(m_tax_id));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_update_date_isSet) {
        obj.insert(QString("update_date"), ::OpenAPI::toJsonValue(m_update_date));
    }
    if (m_vehicle_id_isSet) {
        obj.insert(QString("vehicle_id"), ::OpenAPI::toJsonValue(m_vehicle_id));
    }
    if (m_vehicle_summary.isSet()) {
        obj.insert(QString("vehicle_summary"), ::OpenAPI::toJsonValue(m_vehicle_summary));
    }
    if (m_wrong_inputs.size() > 0) {
        obj.insert(QString("wrong_inputs"), ::OpenAPI::toJsonValue(m_wrong_inputs));
    }
    return obj;
}

QString OAICheck::getBirthCertificate() const {
    return m_birth_certificate;
}
void OAICheck::setBirthCertificate(const QString &birth_certificate) {
    m_birth_certificate = birth_certificate;
    m_birth_certificate_isSet = true;
}

bool OAICheck::is_birth_certificate_Set() const{
    return m_birth_certificate_isSet;
}

bool OAICheck::is_birth_certificate_Valid() const{
    return m_birth_certificate_isValid;
}

QString OAICheck::getCheckId() const {
    return m_check_id;
}
void OAICheck::setCheckId(const QString &check_id) {
    m_check_id = check_id;
    m_check_id_isSet = true;
}

bool OAICheck::is_check_id_Set() const{
    return m_check_id_isSet;
}

bool OAICheck::is_check_id_Valid() const{
    return m_check_id_isValid;
}

OAICompanySummary OAICheck::getCompanySummary() const {
    return m_company_summary;
}
void OAICheck::setCompanySummary(const OAICompanySummary &company_summary) {
    m_company_summary = company_summary;
    m_company_summary_isSet = true;
}

bool OAICheck::is_company_summary_Set() const{
    return m_company_summary_isSet;
}

bool OAICheck::is_company_summary_Valid() const{
    return m_company_summary_isValid;
}

QString OAICheck::getCountry() const {
    return m_country;
}
void OAICheck::setCountry(const QString &country) {
    m_country = country;
    m_country_isSet = true;
}

bool OAICheck::is_country_Set() const{
    return m_country_isSet;
}

bool OAICheck::is_country_Valid() const{
    return m_country_isValid;
}

QDateTime OAICheck::getCreationDate() const {
    return m_creation_date;
}
void OAICheck::setCreationDate(const QDateTime &creation_date) {
    m_creation_date = creation_date;
    m_creation_date_isSet = true;
}

bool OAICheck::is_creation_date_Set() const{
    return m_creation_date_isSet;
}

bool OAICheck::is_creation_date_Valid() const{
    return m_creation_date_isValid;
}

QDateTime OAICheck::getDateOfBirth() const {
    return m_date_of_birth;
}
void OAICheck::setDateOfBirth(const QDateTime &date_of_birth) {
    m_date_of_birth = date_of_birth;
    m_date_of_birth_isSet = true;
}

bool OAICheck::is_date_of_birth_Set() const{
    return m_date_of_birth_isSet;
}

bool OAICheck::is_date_of_birth_Valid() const{
    return m_date_of_birth_isValid;
}

QString OAICheck::getDiplomaticId() const {
    return m_diplomatic_id;
}
void OAICheck::setDiplomaticId(const QString &diplomatic_id) {
    m_diplomatic_id = diplomatic_id;
    m_diplomatic_id_isSet = true;
}

bool OAICheck::is_diplomatic_id_Set() const{
    return m_diplomatic_id_isSet;
}

bool OAICheck::is_diplomatic_id_Valid() const{
    return m_diplomatic_id_isValid;
}

QString OAICheck::getDriverLicense() const {
    return m_driver_license;
}
void OAICheck::setDriverLicense(const QString &driver_license) {
    m_driver_license = driver_license;
    m_driver_license_isSet = true;
}

bool OAICheck::is_driver_license_Set() const{
    return m_driver_license_isSet;
}

bool OAICheck::is_driver_license_Valid() const{
    return m_driver_license_isValid;
}

QString OAICheck::getFirstName() const {
    return m_first_name;
}
void OAICheck::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAICheck::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAICheck::is_first_name_Valid() const{
    return m_first_name_isValid;
}

QString OAICheck::getForeignId() const {
    return m_foreign_id;
}
void OAICheck::setForeignId(const QString &foreign_id) {
    m_foreign_id = foreign_id;
    m_foreign_id_isSet = true;
}

bool OAICheck::is_foreign_id_Set() const{
    return m_foreign_id_isSet;
}

bool OAICheck::is_foreign_id_Valid() const{
    return m_foreign_id_isValid;
}

float OAICheck::getHomonymProbability() const {
    return m_homonym_probability;
}
void OAICheck::setHomonymProbability(const float &homonym_probability) {
    m_homonym_probability = homonym_probability;
    m_homonym_probability_isSet = true;
}

bool OAICheck::is_homonym_probability_Set() const{
    return m_homonym_probability_isSet;
}

bool OAICheck::is_homonym_probability_Valid() const{
    return m_homonym_probability_isValid;
}

float OAICheck::getHomonymScore() const {
    return m_homonym_score;
}
void OAICheck::setHomonymScore(const float &homonym_score) {
    m_homonym_score = homonym_score;
    m_homonym_score_isSet = true;
}

bool OAICheck::is_homonym_score_Set() const{
    return m_homonym_score_isSet;
}

bool OAICheck::is_homonym_score_Valid() const{
    return m_homonym_score_isValid;
}

QList<OAIScore> OAICheck::getHomonymScores() const {
    return m_homonym_scores;
}
void OAICheck::setHomonymScores(const QList<OAIScore> &homonym_scores) {
    m_homonym_scores = homonym_scores;
    m_homonym_scores_isSet = true;
}

bool OAICheck::is_homonym_scores_Set() const{
    return m_homonym_scores_isSet;
}

bool OAICheck::is_homonym_scores_Valid() const{
    return m_homonym_scores_isValid;
}

float OAICheck::getIdScore() const {
    return m_id_score;
}
void OAICheck::setIdScore(const float &id_score) {
    m_id_score = id_score;
    m_id_score_isSet = true;
}

bool OAICheck::is_id_score_Set() const{
    return m_id_score_isSet;
}

bool OAICheck::is_id_score_Valid() const{
    return m_id_score_isValid;
}

QDateTime OAICheck::getIssueDate() const {
    return m_issue_date;
}
void OAICheck::setIssueDate(const QDateTime &issue_date) {
    m_issue_date = issue_date;
    m_issue_date_isSet = true;
}

bool OAICheck::is_issue_date_Set() const{
    return m_issue_date_isSet;
}

bool OAICheck::is_issue_date_Valid() const{
    return m_issue_date_isValid;
}

QString OAICheck::getLastName() const {
    return m_last_name;
}
void OAICheck::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAICheck::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAICheck::is_last_name_Valid() const{
    return m_last_name_isValid;
}

QString OAICheck::getLicensePlate() const {
    return m_license_plate;
}
void OAICheck::setLicensePlate(const QString &license_plate) {
    m_license_plate = license_plate;
    m_license_plate_isSet = true;
}

bool OAICheck::is_license_plate_Set() const{
    return m_license_plate_isSet;
}

bool OAICheck::is_license_plate_Valid() const{
    return m_license_plate_isValid;
}

QString OAICheck::getNationalId() const {
    return m_national_id;
}
void OAICheck::setNationalId(const QString &national_id) {
    m_national_id = national_id;
    m_national_id_isSet = true;
}

bool OAICheck::is_national_id_Set() const{
    return m_national_id_isSet;
}

bool OAICheck::is_national_id_Valid() const{
    return m_national_id_isValid;
}

QString OAICheck::getNativeCountry() const {
    return m_native_country;
}
void OAICheck::setNativeCountry(const QString &native_country) {
    m_native_country = native_country;
    m_native_country_isSet = true;
}

bool OAICheck::is_native_country_Set() const{
    return m_native_country_isSet;
}

bool OAICheck::is_native_country_Valid() const{
    return m_native_country_isValid;
}

QString OAICheck::getOwnerDocumentId() const {
    return m_owner_document_id;
}
void OAICheck::setOwnerDocumentId(const QString &owner_document_id) {
    m_owner_document_id = owner_document_id;
    m_owner_document_id_isSet = true;
}

bool OAICheck::is_owner_document_id_Set() const{
    return m_owner_document_id_isSet;
}

bool OAICheck::is_owner_document_id_Valid() const{
    return m_owner_document_id_isValid;
}

QString OAICheck::getOwnerDocumentType() const {
    return m_owner_document_type;
}
void OAICheck::setOwnerDocumentType(const QString &owner_document_type) {
    m_owner_document_type = owner_document_type;
    m_owner_document_type_isSet = true;
}

bool OAICheck::is_owner_document_type_Set() const{
    return m_owner_document_type_isSet;
}

bool OAICheck::is_owner_document_type_Valid() const{
    return m_owner_document_type_isValid;
}

QString OAICheck::getPassport() const {
    return m_passport;
}
void OAICheck::setPassport(const QString &passport) {
    m_passport = passport;
    m_passport_isSet = true;
}

bool OAICheck::is_passport_Set() const{
    return m_passport_isSet;
}

bool OAICheck::is_passport_Valid() const{
    return m_passport_isValid;
}

QString OAICheck::getPaymentDate() const {
    return m_payment_date;
}
void OAICheck::setPaymentDate(const QString &payment_date) {
    m_payment_date = payment_date;
    m_payment_date_isSet = true;
}

bool OAICheck::is_payment_date_Set() const{
    return m_payment_date_isSet;
}

bool OAICheck::is_payment_date_Valid() const{
    return m_payment_date_isValid;
}

QString OAICheck::getPep() const {
    return m_pep;
}
void OAICheck::setPep(const QString &pep) {
    m_pep = pep;
    m_pep_isSet = true;
}

bool OAICheck::is_pep_Set() const{
    return m_pep_isSet;
}

bool OAICheck::is_pep_Valid() const{
    return m_pep_isValid;
}

QString OAICheck::getPhoneNumber() const {
    return m_phone_number;
}
void OAICheck::setPhoneNumber(const QString &phone_number) {
    m_phone_number = phone_number;
    m_phone_number_isSet = true;
}

bool OAICheck::is_phone_number_Set() const{
    return m_phone_number_isSet;
}

bool OAICheck::is_phone_number_Valid() const{
    return m_phone_number_isValid;
}

QString OAICheck::getProfessionalCard() const {
    return m_professional_card;
}
void OAICheck::setProfessionalCard(const QString &professional_card) {
    m_professional_card = professional_card;
    m_professional_card_isSet = true;
}

bool OAICheck::is_professional_card_Set() const{
    return m_professional_card_isSet;
}

bool OAICheck::is_professional_card_Valid() const{
    return m_professional_card_isValid;
}

QString OAICheck::getPtp() const {
    return m_ptp;
}
void OAICheck::setPtp(const QString &ptp) {
    m_ptp = ptp;
    m_ptp_isSet = true;
}

bool OAICheck::is_ptp_Set() const{
    return m_ptp_isSet;
}

bool OAICheck::is_ptp_Valid() const{
    return m_ptp_isValid;
}

QString OAICheck::getRegion() const {
    return m_region;
}
void OAICheck::setRegion(const QString &region) {
    m_region = region;
    m_region_isSet = true;
}

bool OAICheck::is_region_Set() const{
    return m_region_isSet;
}

bool OAICheck::is_region_Valid() const{
    return m_region_isValid;
}

QString OAICheck::getReportId() const {
    return m_report_id;
}
void OAICheck::setReportId(const QString &report_id) {
    m_report_id = report_id;
    m_report_id_isSet = true;
}

bool OAICheck::is_report_id_Set() const{
    return m_report_id_isSet;
}

bool OAICheck::is_report_id_Valid() const{
    return m_report_id_isValid;
}

float OAICheck::getScore() const {
    return m_score;
}
void OAICheck::setScore(const float &score) {
    m_score = score;
    m_score_isSet = true;
}

bool OAICheck::is_score_Set() const{
    return m_score_isSet;
}

bool OAICheck::is_score_Valid() const{
    return m_score_isValid;
}

QList<OAIScore> OAICheck::getScores() const {
    return m_scores;
}
void OAICheck::setScores(const QList<OAIScore> &scores) {
    m_scores = scores;
    m_scores_isSet = true;
}

bool OAICheck::is_scores_Set() const{
    return m_scores_isSet;
}

bool OAICheck::is_scores_Valid() const{
    return m_scores_isValid;
}

QString OAICheck::getStatus() const {
    return m_status;
}
void OAICheck::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAICheck::is_status_Set() const{
    return m_status_isSet;
}

bool OAICheck::is_status_Valid() const{
    return m_status_isValid;
}

QList<OAIStatus> OAICheck::getStatuses() const {
    return m_statuses;
}
void OAICheck::setStatuses(const QList<OAIStatus> &statuses) {
    m_statuses = statuses;
    m_statuses_isSet = true;
}

bool OAICheck::is_statuses_Set() const{
    return m_statuses_isSet;
}

bool OAICheck::is_statuses_Valid() const{
    return m_statuses_isValid;
}

OAISummary OAICheck::getSummary() const {
    return m_summary;
}
void OAICheck::setSummary(const OAISummary &summary) {
    m_summary = summary;
    m_summary_isSet = true;
}

bool OAICheck::is_summary_Set() const{
    return m_summary_isSet;
}

bool OAICheck::is_summary_Valid() const{
    return m_summary_isValid;
}

QString OAICheck::getTaxId() const {
    return m_tax_id;
}
void OAICheck::setTaxId(const QString &tax_id) {
    m_tax_id = tax_id;
    m_tax_id_isSet = true;
}

bool OAICheck::is_tax_id_Set() const{
    return m_tax_id_isSet;
}

bool OAICheck::is_tax_id_Valid() const{
    return m_tax_id_isValid;
}

QString OAICheck::getType() const {
    return m_type;
}
void OAICheck::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAICheck::is_type_Set() const{
    return m_type_isSet;
}

bool OAICheck::is_type_Valid() const{
    return m_type_isValid;
}

QDateTime OAICheck::getUpdateDate() const {
    return m_update_date;
}
void OAICheck::setUpdateDate(const QDateTime &update_date) {
    m_update_date = update_date;
    m_update_date_isSet = true;
}

bool OAICheck::is_update_date_Set() const{
    return m_update_date_isSet;
}

bool OAICheck::is_update_date_Valid() const{
    return m_update_date_isValid;
}

QString OAICheck::getVehicleId() const {
    return m_vehicle_id;
}
void OAICheck::setVehicleId(const QString &vehicle_id) {
    m_vehicle_id = vehicle_id;
    m_vehicle_id_isSet = true;
}

bool OAICheck::is_vehicle_id_Set() const{
    return m_vehicle_id_isSet;
}

bool OAICheck::is_vehicle_id_Valid() const{
    return m_vehicle_id_isValid;
}

OAIVehicleSummary OAICheck::getVehicleSummary() const {
    return m_vehicle_summary;
}
void OAICheck::setVehicleSummary(const OAIVehicleSummary &vehicle_summary) {
    m_vehicle_summary = vehicle_summary;
    m_vehicle_summary_isSet = true;
}

bool OAICheck::is_vehicle_summary_Set() const{
    return m_vehicle_summary_isSet;
}

bool OAICheck::is_vehicle_summary_Valid() const{
    return m_vehicle_summary_isValid;
}

QList<OAIWrongInput> OAICheck::getWrongInputs() const {
    return m_wrong_inputs;
}
void OAICheck::setWrongInputs(const QList<OAIWrongInput> &wrong_inputs) {
    m_wrong_inputs = wrong_inputs;
    m_wrong_inputs_isSet = true;
}

bool OAICheck::is_wrong_inputs_Set() const{
    return m_wrong_inputs_isSet;
}

bool OAICheck::is_wrong_inputs_Valid() const{
    return m_wrong_inputs_isValid;
}

bool OAICheck::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_birth_certificate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_check_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_company_summary.isSet()) {
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

        if (m_date_of_birth_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_diplomatic_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_driver_license_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_foreign_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_homonym_probability_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_homonym_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_homonym_scores.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_issue_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_license_plate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_national_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_native_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_owner_document_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_owner_document_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_passport_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pep_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phone_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_professional_card_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ptp_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_region_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_report_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_scores.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_statuses.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_summary.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_update_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vehicle_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vehicle_summary.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_wrong_inputs.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICheck::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_check_id_isValid && m_country_isValid && m_creation_date_isValid && m_id_score_isValid && m_score_isValid && m_status_isValid && m_statuses_isValid && m_summary_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
