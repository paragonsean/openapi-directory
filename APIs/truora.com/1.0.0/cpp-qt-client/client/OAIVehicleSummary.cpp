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

#include "OAIVehicleSummary.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVehicleSummary::OAIVehicleSummary(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVehicleSummary::OAIVehicleSummary() {
    this->initializeModel();
}

OAIVehicleSummary::~OAIVehicleSummary() {}

void OAIVehicleSummary::initializeModel() {

    m_capacity_isSet = false;
    m_capacity_isValid = false;

    m_color_isSet = false;
    m_color_isValid = false;

    m_license_plate_isSet = false;
    m_license_plate_isValid = false;

    m_manufacturer_isSet = false;
    m_manufacturer_isValid = false;

    m_model_isSet = false;
    m_model_isValid = false;

    m_number_of_doors_isSet = false;
    m_number_of_doors_isValid = false;

    m_obligatory_insurance_expiration_date_isSet = false;
    m_obligatory_insurance_expiration_date_isValid = false;

    m_obligatory_insurance_status_isSet = false;
    m_obligatory_insurance_status_isValid = false;

    m_service_type_isSet = false;
    m_service_type_isValid = false;

    m_vehicle_category_isSet = false;
    m_vehicle_category_isValid = false;

    m_vehicle_id_isSet = false;
    m_vehicle_id_isValid = false;

    m_vehicle_type_isSet = false;
    m_vehicle_type_isValid = false;

    m_year_isSet = false;
    m_year_isValid = false;
}

void OAIVehicleSummary::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVehicleSummary::fromJsonObject(QJsonObject json) {

    m_capacity_isValid = ::OpenAPI::fromJsonValue(m_capacity, json[QString("capacity")]);
    m_capacity_isSet = !json[QString("capacity")].isNull() && m_capacity_isValid;

    m_color_isValid = ::OpenAPI::fromJsonValue(m_color, json[QString("color")]);
    m_color_isSet = !json[QString("color")].isNull() && m_color_isValid;

    m_license_plate_isValid = ::OpenAPI::fromJsonValue(m_license_plate, json[QString("license_plate")]);
    m_license_plate_isSet = !json[QString("license_plate")].isNull() && m_license_plate_isValid;

    m_manufacturer_isValid = ::OpenAPI::fromJsonValue(m_manufacturer, json[QString("manufacturer")]);
    m_manufacturer_isSet = !json[QString("manufacturer")].isNull() && m_manufacturer_isValid;

    m_model_isValid = ::OpenAPI::fromJsonValue(m_model, json[QString("model")]);
    m_model_isSet = !json[QString("model")].isNull() && m_model_isValid;

    m_number_of_doors_isValid = ::OpenAPI::fromJsonValue(m_number_of_doors, json[QString("number_of_doors")]);
    m_number_of_doors_isSet = !json[QString("number_of_doors")].isNull() && m_number_of_doors_isValid;

    m_obligatory_insurance_expiration_date_isValid = ::OpenAPI::fromJsonValue(m_obligatory_insurance_expiration_date, json[QString("obligatory_insurance_expiration_date")]);
    m_obligatory_insurance_expiration_date_isSet = !json[QString("obligatory_insurance_expiration_date")].isNull() && m_obligatory_insurance_expiration_date_isValid;

    m_obligatory_insurance_status_isValid = ::OpenAPI::fromJsonValue(m_obligatory_insurance_status, json[QString("obligatory_insurance_status")]);
    m_obligatory_insurance_status_isSet = !json[QString("obligatory_insurance_status")].isNull() && m_obligatory_insurance_status_isValid;

    m_service_type_isValid = ::OpenAPI::fromJsonValue(m_service_type, json[QString("service_type")]);
    m_service_type_isSet = !json[QString("service_type")].isNull() && m_service_type_isValid;

    m_vehicle_category_isValid = ::OpenAPI::fromJsonValue(m_vehicle_category, json[QString("vehicle_category")]);
    m_vehicle_category_isSet = !json[QString("vehicle_category")].isNull() && m_vehicle_category_isValid;

    m_vehicle_id_isValid = ::OpenAPI::fromJsonValue(m_vehicle_id, json[QString("vehicle_id")]);
    m_vehicle_id_isSet = !json[QString("vehicle_id")].isNull() && m_vehicle_id_isValid;

    m_vehicle_type_isValid = ::OpenAPI::fromJsonValue(m_vehicle_type, json[QString("vehicle_type")]);
    m_vehicle_type_isSet = !json[QString("vehicle_type")].isNull() && m_vehicle_type_isValid;

    m_year_isValid = ::OpenAPI::fromJsonValue(m_year, json[QString("year")]);
    m_year_isSet = !json[QString("year")].isNull() && m_year_isValid;
}

QString OAIVehicleSummary::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVehicleSummary::asJsonObject() const {
    QJsonObject obj;
    if (m_capacity_isSet) {
        obj.insert(QString("capacity"), ::OpenAPI::toJsonValue(m_capacity));
    }
    if (m_color_isSet) {
        obj.insert(QString("color"), ::OpenAPI::toJsonValue(m_color));
    }
    if (m_license_plate_isSet) {
        obj.insert(QString("license_plate"), ::OpenAPI::toJsonValue(m_license_plate));
    }
    if (m_manufacturer_isSet) {
        obj.insert(QString("manufacturer"), ::OpenAPI::toJsonValue(m_manufacturer));
    }
    if (m_model_isSet) {
        obj.insert(QString("model"), ::OpenAPI::toJsonValue(m_model));
    }
    if (m_number_of_doors_isSet) {
        obj.insert(QString("number_of_doors"), ::OpenAPI::toJsonValue(m_number_of_doors));
    }
    if (m_obligatory_insurance_expiration_date_isSet) {
        obj.insert(QString("obligatory_insurance_expiration_date"), ::OpenAPI::toJsonValue(m_obligatory_insurance_expiration_date));
    }
    if (m_obligatory_insurance_status_isSet) {
        obj.insert(QString("obligatory_insurance_status"), ::OpenAPI::toJsonValue(m_obligatory_insurance_status));
    }
    if (m_service_type_isSet) {
        obj.insert(QString("service_type"), ::OpenAPI::toJsonValue(m_service_type));
    }
    if (m_vehicle_category_isSet) {
        obj.insert(QString("vehicle_category"), ::OpenAPI::toJsonValue(m_vehicle_category));
    }
    if (m_vehicle_id_isSet) {
        obj.insert(QString("vehicle_id"), ::OpenAPI::toJsonValue(m_vehicle_id));
    }
    if (m_vehicle_type_isSet) {
        obj.insert(QString("vehicle_type"), ::OpenAPI::toJsonValue(m_vehicle_type));
    }
    if (m_year_isSet) {
        obj.insert(QString("year"), ::OpenAPI::toJsonValue(m_year));
    }
    return obj;
}

qint32 OAIVehicleSummary::getCapacity() const {
    return m_capacity;
}
void OAIVehicleSummary::setCapacity(const qint32 &capacity) {
    m_capacity = capacity;
    m_capacity_isSet = true;
}

bool OAIVehicleSummary::is_capacity_Set() const{
    return m_capacity_isSet;
}

bool OAIVehicleSummary::is_capacity_Valid() const{
    return m_capacity_isValid;
}

QString OAIVehicleSummary::getColor() const {
    return m_color;
}
void OAIVehicleSummary::setColor(const QString &color) {
    m_color = color;
    m_color_isSet = true;
}

bool OAIVehicleSummary::is_color_Set() const{
    return m_color_isSet;
}

bool OAIVehicleSummary::is_color_Valid() const{
    return m_color_isValid;
}

QString OAIVehicleSummary::getLicensePlate() const {
    return m_license_plate;
}
void OAIVehicleSummary::setLicensePlate(const QString &license_plate) {
    m_license_plate = license_plate;
    m_license_plate_isSet = true;
}

bool OAIVehicleSummary::is_license_plate_Set() const{
    return m_license_plate_isSet;
}

bool OAIVehicleSummary::is_license_plate_Valid() const{
    return m_license_plate_isValid;
}

QString OAIVehicleSummary::getManufacturer() const {
    return m_manufacturer;
}
void OAIVehicleSummary::setManufacturer(const QString &manufacturer) {
    m_manufacturer = manufacturer;
    m_manufacturer_isSet = true;
}

bool OAIVehicleSummary::is_manufacturer_Set() const{
    return m_manufacturer_isSet;
}

bool OAIVehicleSummary::is_manufacturer_Valid() const{
    return m_manufacturer_isValid;
}

QString OAIVehicleSummary::getModel() const {
    return m_model;
}
void OAIVehicleSummary::setModel(const QString &model) {
    m_model = model;
    m_model_isSet = true;
}

bool OAIVehicleSummary::is_model_Set() const{
    return m_model_isSet;
}

bool OAIVehicleSummary::is_model_Valid() const{
    return m_model_isValid;
}

qint32 OAIVehicleSummary::getNumberOfDoors() const {
    return m_number_of_doors;
}
void OAIVehicleSummary::setNumberOfDoors(const qint32 &number_of_doors) {
    m_number_of_doors = number_of_doors;
    m_number_of_doors_isSet = true;
}

bool OAIVehicleSummary::is_number_of_doors_Set() const{
    return m_number_of_doors_isSet;
}

bool OAIVehicleSummary::is_number_of_doors_Valid() const{
    return m_number_of_doors_isValid;
}

QDate OAIVehicleSummary::getObligatoryInsuranceExpirationDate() const {
    return m_obligatory_insurance_expiration_date;
}
void OAIVehicleSummary::setObligatoryInsuranceExpirationDate(const QDate &obligatory_insurance_expiration_date) {
    m_obligatory_insurance_expiration_date = obligatory_insurance_expiration_date;
    m_obligatory_insurance_expiration_date_isSet = true;
}

bool OAIVehicleSummary::is_obligatory_insurance_expiration_date_Set() const{
    return m_obligatory_insurance_expiration_date_isSet;
}

bool OAIVehicleSummary::is_obligatory_insurance_expiration_date_Valid() const{
    return m_obligatory_insurance_expiration_date_isValid;
}

QString OAIVehicleSummary::getObligatoryInsuranceStatus() const {
    return m_obligatory_insurance_status;
}
void OAIVehicleSummary::setObligatoryInsuranceStatus(const QString &obligatory_insurance_status) {
    m_obligatory_insurance_status = obligatory_insurance_status;
    m_obligatory_insurance_status_isSet = true;
}

bool OAIVehicleSummary::is_obligatory_insurance_status_Set() const{
    return m_obligatory_insurance_status_isSet;
}

bool OAIVehicleSummary::is_obligatory_insurance_status_Valid() const{
    return m_obligatory_insurance_status_isValid;
}

QString OAIVehicleSummary::getServiceType() const {
    return m_service_type;
}
void OAIVehicleSummary::setServiceType(const QString &service_type) {
    m_service_type = service_type;
    m_service_type_isSet = true;
}

bool OAIVehicleSummary::is_service_type_Set() const{
    return m_service_type_isSet;
}

bool OAIVehicleSummary::is_service_type_Valid() const{
    return m_service_type_isValid;
}

QString OAIVehicleSummary::getVehicleCategory() const {
    return m_vehicle_category;
}
void OAIVehicleSummary::setVehicleCategory(const QString &vehicle_category) {
    m_vehicle_category = vehicle_category;
    m_vehicle_category_isSet = true;
}

bool OAIVehicleSummary::is_vehicle_category_Set() const{
    return m_vehicle_category_isSet;
}

bool OAIVehicleSummary::is_vehicle_category_Valid() const{
    return m_vehicle_category_isValid;
}

QString OAIVehicleSummary::getVehicleId() const {
    return m_vehicle_id;
}
void OAIVehicleSummary::setVehicleId(const QString &vehicle_id) {
    m_vehicle_id = vehicle_id;
    m_vehicle_id_isSet = true;
}

bool OAIVehicleSummary::is_vehicle_id_Set() const{
    return m_vehicle_id_isSet;
}

bool OAIVehicleSummary::is_vehicle_id_Valid() const{
    return m_vehicle_id_isValid;
}

QString OAIVehicleSummary::getVehicleType() const {
    return m_vehicle_type;
}
void OAIVehicleSummary::setVehicleType(const QString &vehicle_type) {
    m_vehicle_type = vehicle_type;
    m_vehicle_type_isSet = true;
}

bool OAIVehicleSummary::is_vehicle_type_Set() const{
    return m_vehicle_type_isSet;
}

bool OAIVehicleSummary::is_vehicle_type_Valid() const{
    return m_vehicle_type_isValid;
}

qint32 OAIVehicleSummary::getYear() const {
    return m_year;
}
void OAIVehicleSummary::setYear(const qint32 &year) {
    m_year = year;
    m_year_isSet = true;
}

bool OAIVehicleSummary::is_year_Set() const{
    return m_year_isSet;
}

bool OAIVehicleSummary::is_year_Valid() const{
    return m_year_isValid;
}

bool OAIVehicleSummary::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_capacity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_color_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_license_plate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_manufacturer_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_model_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_number_of_doors_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_obligatory_insurance_expiration_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_obligatory_insurance_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_service_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vehicle_category_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vehicle_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vehicle_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_year_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVehicleSummary::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
