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

/*
 * OAICheck.h
 *
 * Represents a background check
 */

#ifndef OAICheck_H
#define OAICheck_H

#include <QJsonObject>

#include "OAICompanySummary.h"
#include "OAIScore.h"
#include "OAIStatus.h"
#include "OAISummary.h"
#include "OAIVehicleSummary.h"
#include "OAIWrongInput.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICompanySummary;
class OAIScore;
class OAIStatus;
class OAISummary;
class OAIVehicleSummary;
class OAIWrongInput;

class OAICheck : public OAIObject {
public:
    OAICheck();
    OAICheck(QString json);
    ~OAICheck() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBirthCertificate() const;
    void setBirthCertificate(const QString &birth_certificate);
    bool is_birth_certificate_Set() const;
    bool is_birth_certificate_Valid() const;

    QString getCheckId() const;
    void setCheckId(const QString &check_id);
    bool is_check_id_Set() const;
    bool is_check_id_Valid() const;

    OAICompanySummary getCompanySummary() const;
    void setCompanySummary(const OAICompanySummary &company_summary);
    bool is_company_summary_Set() const;
    bool is_company_summary_Valid() const;

    QString getCountry() const;
    void setCountry(const QString &country);
    bool is_country_Set() const;
    bool is_country_Valid() const;

    QDateTime getCreationDate() const;
    void setCreationDate(const QDateTime &creation_date);
    bool is_creation_date_Set() const;
    bool is_creation_date_Valid() const;

    QDateTime getDateOfBirth() const;
    void setDateOfBirth(const QDateTime &date_of_birth);
    bool is_date_of_birth_Set() const;
    bool is_date_of_birth_Valid() const;

    QString getDiplomaticId() const;
    void setDiplomaticId(const QString &diplomatic_id);
    bool is_diplomatic_id_Set() const;
    bool is_diplomatic_id_Valid() const;

    QString getDriverLicense() const;
    void setDriverLicense(const QString &driver_license);
    bool is_driver_license_Set() const;
    bool is_driver_license_Valid() const;

    QString getFirstName() const;
    void setFirstName(const QString &first_name);
    bool is_first_name_Set() const;
    bool is_first_name_Valid() const;

    QString getForeignId() const;
    void setForeignId(const QString &foreign_id);
    bool is_foreign_id_Set() const;
    bool is_foreign_id_Valid() const;

    float getHomonymProbability() const;
    void setHomonymProbability(const float &homonym_probability);
    bool is_homonym_probability_Set() const;
    bool is_homonym_probability_Valid() const;

    float getHomonymScore() const;
    void setHomonymScore(const float &homonym_score);
    bool is_homonym_score_Set() const;
    bool is_homonym_score_Valid() const;

    QList<OAIScore> getHomonymScores() const;
    void setHomonymScores(const QList<OAIScore> &homonym_scores);
    bool is_homonym_scores_Set() const;
    bool is_homonym_scores_Valid() const;

    float getIdScore() const;
    void setIdScore(const float &id_score);
    bool is_id_score_Set() const;
    bool is_id_score_Valid() const;

    QDateTime getIssueDate() const;
    void setIssueDate(const QDateTime &issue_date);
    bool is_issue_date_Set() const;
    bool is_issue_date_Valid() const;

    QString getLastName() const;
    void setLastName(const QString &last_name);
    bool is_last_name_Set() const;
    bool is_last_name_Valid() const;

    QString getLicensePlate() const;
    void setLicensePlate(const QString &license_plate);
    bool is_license_plate_Set() const;
    bool is_license_plate_Valid() const;

    QString getNationalId() const;
    void setNationalId(const QString &national_id);
    bool is_national_id_Set() const;
    bool is_national_id_Valid() const;

    QString getNativeCountry() const;
    void setNativeCountry(const QString &native_country);
    bool is_native_country_Set() const;
    bool is_native_country_Valid() const;

    QString getOwnerDocumentId() const;
    void setOwnerDocumentId(const QString &owner_document_id);
    bool is_owner_document_id_Set() const;
    bool is_owner_document_id_Valid() const;

    QString getOwnerDocumentType() const;
    void setOwnerDocumentType(const QString &owner_document_type);
    bool is_owner_document_type_Set() const;
    bool is_owner_document_type_Valid() const;

    QString getPassport() const;
    void setPassport(const QString &passport);
    bool is_passport_Set() const;
    bool is_passport_Valid() const;

    QString getPaymentDate() const;
    void setPaymentDate(const QString &payment_date);
    bool is_payment_date_Set() const;
    bool is_payment_date_Valid() const;

    QString getPep() const;
    void setPep(const QString &pep);
    bool is_pep_Set() const;
    bool is_pep_Valid() const;

    QString getPhoneNumber() const;
    void setPhoneNumber(const QString &phone_number);
    bool is_phone_number_Set() const;
    bool is_phone_number_Valid() const;

    QString getProfessionalCard() const;
    void setProfessionalCard(const QString &professional_card);
    bool is_professional_card_Set() const;
    bool is_professional_card_Valid() const;

    QString getPtp() const;
    void setPtp(const QString &ptp);
    bool is_ptp_Set() const;
    bool is_ptp_Valid() const;

    QString getRegion() const;
    void setRegion(const QString &region);
    bool is_region_Set() const;
    bool is_region_Valid() const;

    QString getReportId() const;
    void setReportId(const QString &report_id);
    bool is_report_id_Set() const;
    bool is_report_id_Valid() const;

    float getScore() const;
    void setScore(const float &score);
    bool is_score_Set() const;
    bool is_score_Valid() const;

    QList<OAIScore> getScores() const;
    void setScores(const QList<OAIScore> &scores);
    bool is_scores_Set() const;
    bool is_scores_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    QList<OAIStatus> getStatuses() const;
    void setStatuses(const QList<OAIStatus> &statuses);
    bool is_statuses_Set() const;
    bool is_statuses_Valid() const;

    OAISummary getSummary() const;
    void setSummary(const OAISummary &summary);
    bool is_summary_Set() const;
    bool is_summary_Valid() const;

    QString getTaxId() const;
    void setTaxId(const QString &tax_id);
    bool is_tax_id_Set() const;
    bool is_tax_id_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    QDateTime getUpdateDate() const;
    void setUpdateDate(const QDateTime &update_date);
    bool is_update_date_Set() const;
    bool is_update_date_Valid() const;

    QString getVehicleId() const;
    void setVehicleId(const QString &vehicle_id);
    bool is_vehicle_id_Set() const;
    bool is_vehicle_id_Valid() const;

    OAIVehicleSummary getVehicleSummary() const;
    void setVehicleSummary(const OAIVehicleSummary &vehicle_summary);
    bool is_vehicle_summary_Set() const;
    bool is_vehicle_summary_Valid() const;

    QList<OAIWrongInput> getWrongInputs() const;
    void setWrongInputs(const QList<OAIWrongInput> &wrong_inputs);
    bool is_wrong_inputs_Set() const;
    bool is_wrong_inputs_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_birth_certificate;
    bool m_birth_certificate_isSet;
    bool m_birth_certificate_isValid;

    QString m_check_id;
    bool m_check_id_isSet;
    bool m_check_id_isValid;

    OAICompanySummary m_company_summary;
    bool m_company_summary_isSet;
    bool m_company_summary_isValid;

    QString m_country;
    bool m_country_isSet;
    bool m_country_isValid;

    QDateTime m_creation_date;
    bool m_creation_date_isSet;
    bool m_creation_date_isValid;

    QDateTime m_date_of_birth;
    bool m_date_of_birth_isSet;
    bool m_date_of_birth_isValid;

    QString m_diplomatic_id;
    bool m_diplomatic_id_isSet;
    bool m_diplomatic_id_isValid;

    QString m_driver_license;
    bool m_driver_license_isSet;
    bool m_driver_license_isValid;

    QString m_first_name;
    bool m_first_name_isSet;
    bool m_first_name_isValid;

    QString m_foreign_id;
    bool m_foreign_id_isSet;
    bool m_foreign_id_isValid;

    float m_homonym_probability;
    bool m_homonym_probability_isSet;
    bool m_homonym_probability_isValid;

    float m_homonym_score;
    bool m_homonym_score_isSet;
    bool m_homonym_score_isValid;

    QList<OAIScore> m_homonym_scores;
    bool m_homonym_scores_isSet;
    bool m_homonym_scores_isValid;

    float m_id_score;
    bool m_id_score_isSet;
    bool m_id_score_isValid;

    QDateTime m_issue_date;
    bool m_issue_date_isSet;
    bool m_issue_date_isValid;

    QString m_last_name;
    bool m_last_name_isSet;
    bool m_last_name_isValid;

    QString m_license_plate;
    bool m_license_plate_isSet;
    bool m_license_plate_isValid;

    QString m_national_id;
    bool m_national_id_isSet;
    bool m_national_id_isValid;

    QString m_native_country;
    bool m_native_country_isSet;
    bool m_native_country_isValid;

    QString m_owner_document_id;
    bool m_owner_document_id_isSet;
    bool m_owner_document_id_isValid;

    QString m_owner_document_type;
    bool m_owner_document_type_isSet;
    bool m_owner_document_type_isValid;

    QString m_passport;
    bool m_passport_isSet;
    bool m_passport_isValid;

    QString m_payment_date;
    bool m_payment_date_isSet;
    bool m_payment_date_isValid;

    QString m_pep;
    bool m_pep_isSet;
    bool m_pep_isValid;

    QString m_phone_number;
    bool m_phone_number_isSet;
    bool m_phone_number_isValid;

    QString m_professional_card;
    bool m_professional_card_isSet;
    bool m_professional_card_isValid;

    QString m_ptp;
    bool m_ptp_isSet;
    bool m_ptp_isValid;

    QString m_region;
    bool m_region_isSet;
    bool m_region_isValid;

    QString m_report_id;
    bool m_report_id_isSet;
    bool m_report_id_isValid;

    float m_score;
    bool m_score_isSet;
    bool m_score_isValid;

    QList<OAIScore> m_scores;
    bool m_scores_isSet;
    bool m_scores_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    QList<OAIStatus> m_statuses;
    bool m_statuses_isSet;
    bool m_statuses_isValid;

    OAISummary m_summary;
    bool m_summary_isSet;
    bool m_summary_isValid;

    QString m_tax_id;
    bool m_tax_id_isSet;
    bool m_tax_id_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    QDateTime m_update_date;
    bool m_update_date_isSet;
    bool m_update_date_isValid;

    QString m_vehicle_id;
    bool m_vehicle_id_isSet;
    bool m_vehicle_id_isValid;

    OAIVehicleSummary m_vehicle_summary;
    bool m_vehicle_summary_isSet;
    bool m_vehicle_summary_isValid;

    QList<OAIWrongInput> m_wrong_inputs;
    bool m_wrong_inputs_isSet;
    bool m_wrong_inputs_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICheck)

#endif // OAICheck_H
