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
 * OAIVehicleSummary.h
 *
 * Represents the summary of a vehicle background check
 */

#ifndef OAIVehicleSummary_H
#define OAIVehicleSummary_H

#include <QJsonObject>

#include <QDate>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIVehicleSummary : public OAIObject {
public:
    OAIVehicleSummary();
    OAIVehicleSummary(QString json);
    ~OAIVehicleSummary() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getCapacity() const;
    void setCapacity(const qint32 &capacity);
    bool is_capacity_Set() const;
    bool is_capacity_Valid() const;

    QString getColor() const;
    void setColor(const QString &color);
    bool is_color_Set() const;
    bool is_color_Valid() const;

    QString getLicensePlate() const;
    void setLicensePlate(const QString &license_plate);
    bool is_license_plate_Set() const;
    bool is_license_plate_Valid() const;

    QString getManufacturer() const;
    void setManufacturer(const QString &manufacturer);
    bool is_manufacturer_Set() const;
    bool is_manufacturer_Valid() const;

    QString getModel() const;
    void setModel(const QString &model);
    bool is_model_Set() const;
    bool is_model_Valid() const;

    qint32 getNumberOfDoors() const;
    void setNumberOfDoors(const qint32 &number_of_doors);
    bool is_number_of_doors_Set() const;
    bool is_number_of_doors_Valid() const;

    QDate getObligatoryInsuranceExpirationDate() const;
    void setObligatoryInsuranceExpirationDate(const QDate &obligatory_insurance_expiration_date);
    bool is_obligatory_insurance_expiration_date_Set() const;
    bool is_obligatory_insurance_expiration_date_Valid() const;

    QString getObligatoryInsuranceStatus() const;
    void setObligatoryInsuranceStatus(const QString &obligatory_insurance_status);
    bool is_obligatory_insurance_status_Set() const;
    bool is_obligatory_insurance_status_Valid() const;

    QString getServiceType() const;
    void setServiceType(const QString &service_type);
    bool is_service_type_Set() const;
    bool is_service_type_Valid() const;

    QString getVehicleCategory() const;
    void setVehicleCategory(const QString &vehicle_category);
    bool is_vehicle_category_Set() const;
    bool is_vehicle_category_Valid() const;

    QString getVehicleId() const;
    void setVehicleId(const QString &vehicle_id);
    bool is_vehicle_id_Set() const;
    bool is_vehicle_id_Valid() const;

    QString getVehicleType() const;
    void setVehicleType(const QString &vehicle_type);
    bool is_vehicle_type_Set() const;
    bool is_vehicle_type_Valid() const;

    qint32 getYear() const;
    void setYear(const qint32 &year);
    bool is_year_Set() const;
    bool is_year_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_capacity;
    bool m_capacity_isSet;
    bool m_capacity_isValid;

    QString m_color;
    bool m_color_isSet;
    bool m_color_isValid;

    QString m_license_plate;
    bool m_license_plate_isSet;
    bool m_license_plate_isValid;

    QString m_manufacturer;
    bool m_manufacturer_isSet;
    bool m_manufacturer_isValid;

    QString m_model;
    bool m_model_isSet;
    bool m_model_isValid;

    qint32 m_number_of_doors;
    bool m_number_of_doors_isSet;
    bool m_number_of_doors_isValid;

    QDate m_obligatory_insurance_expiration_date;
    bool m_obligatory_insurance_expiration_date_isSet;
    bool m_obligatory_insurance_expiration_date_isValid;

    QString m_obligatory_insurance_status;
    bool m_obligatory_insurance_status_isSet;
    bool m_obligatory_insurance_status_isValid;

    QString m_service_type;
    bool m_service_type_isSet;
    bool m_service_type_isValid;

    QString m_vehicle_category;
    bool m_vehicle_category_isSet;
    bool m_vehicle_category_isValid;

    QString m_vehicle_id;
    bool m_vehicle_id_isSet;
    bool m_vehicle_id_isValid;

    QString m_vehicle_type;
    bool m_vehicle_type_isSet;
    bool m_vehicle_type_isValid;

    qint32 m_year;
    bool m_year_isSet;
    bool m_year_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIVehicleSummary)

#endif // OAIVehicleSummary_H
