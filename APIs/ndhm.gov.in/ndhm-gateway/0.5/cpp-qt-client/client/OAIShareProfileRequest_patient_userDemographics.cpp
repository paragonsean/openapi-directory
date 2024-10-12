/**
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIShareProfileRequest_patient_userDemographics.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIShareProfileRequest_patient_userDemographics::OAIShareProfileRequest_patient_userDemographics(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIShareProfileRequest_patient_userDemographics::OAIShareProfileRequest_patient_userDemographics() {
    this->initializeModel();
}

OAIShareProfileRequest_patient_userDemographics::~OAIShareProfileRequest_patient_userDemographics() {}

void OAIShareProfileRequest_patient_userDemographics::initializeModel() {

    m_address_isSet = false;
    m_address_isValid = false;

    m_day_of_birth_isSet = false;
    m_day_of_birth_isValid = false;

    m_gender_isSet = false;
    m_gender_isValid = false;

    m_health_id_isSet = false;
    m_health_id_isValid = false;

    m_health_id_number_isSet = false;
    m_health_id_number_isValid = false;

    m_identifiers_isSet = false;
    m_identifiers_isValid = false;

    m_month_of_birth_isSet = false;
    m_month_of_birth_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_year_of_birth_isSet = false;
    m_year_of_birth_isValid = false;
}

void OAIShareProfileRequest_patient_userDemographics::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIShareProfileRequest_patient_userDemographics::fromJsonObject(QJsonObject json) {

    m_address_isValid = ::OpenAPI::fromJsonValue(m_address, json[QString("address")]);
    m_address_isSet = !json[QString("address")].isNull() && m_address_isValid;

    m_day_of_birth_isValid = ::OpenAPI::fromJsonValue(m_day_of_birth, json[QString("dayOfBirth")]);
    m_day_of_birth_isSet = !json[QString("dayOfBirth")].isNull() && m_day_of_birth_isValid;

    m_gender_isValid = ::OpenAPI::fromJsonValue(m_gender, json[QString("gender")]);
    m_gender_isSet = !json[QString("gender")].isNull() && m_gender_isValid;

    m_health_id_isValid = ::OpenAPI::fromJsonValue(m_health_id, json[QString("healthId")]);
    m_health_id_isSet = !json[QString("healthId")].isNull() && m_health_id_isValid;

    m_health_id_number_isValid = ::OpenAPI::fromJsonValue(m_health_id_number, json[QString("healthIdNumber")]);
    m_health_id_number_isSet = !json[QString("healthIdNumber")].isNull() && m_health_id_number_isValid;

    m_identifiers_isValid = ::OpenAPI::fromJsonValue(m_identifiers, json[QString("identifiers")]);
    m_identifiers_isSet = !json[QString("identifiers")].isNull() && m_identifiers_isValid;

    m_month_of_birth_isValid = ::OpenAPI::fromJsonValue(m_month_of_birth, json[QString("monthOfBirth")]);
    m_month_of_birth_isSet = !json[QString("monthOfBirth")].isNull() && m_month_of_birth_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_year_of_birth_isValid = ::OpenAPI::fromJsonValue(m_year_of_birth, json[QString("yearOfBirth")]);
    m_year_of_birth_isSet = !json[QString("yearOfBirth")].isNull() && m_year_of_birth_isValid;
}

QString OAIShareProfileRequest_patient_userDemographics::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIShareProfileRequest_patient_userDemographics::asJsonObject() const {
    QJsonObject obj;
    if (m_address.isSet()) {
        obj.insert(QString("address"), ::OpenAPI::toJsonValue(m_address));
    }
    if (m_day_of_birth_isSet) {
        obj.insert(QString("dayOfBirth"), ::OpenAPI::toJsonValue(m_day_of_birth));
    }
    if (m_gender.isSet()) {
        obj.insert(QString("gender"), ::OpenAPI::toJsonValue(m_gender));
    }
    if (m_health_id_isSet) {
        obj.insert(QString("healthId"), ::OpenAPI::toJsonValue(m_health_id));
    }
    if (m_health_id_number_isSet) {
        obj.insert(QString("healthIdNumber"), ::OpenAPI::toJsonValue(m_health_id_number));
    }
    if (m_identifiers.size() > 0) {
        obj.insert(QString("identifiers"), ::OpenAPI::toJsonValue(m_identifiers));
    }
    if (m_month_of_birth_isSet) {
        obj.insert(QString("monthOfBirth"), ::OpenAPI::toJsonValue(m_month_of_birth));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_year_of_birth_isSet) {
        obj.insert(QString("yearOfBirth"), ::OpenAPI::toJsonValue(m_year_of_birth));
    }
    return obj;
}

OAIPatientAddress OAIShareProfileRequest_patient_userDemographics::getAddress() const {
    return m_address;
}
void OAIShareProfileRequest_patient_userDemographics::setAddress(const OAIPatientAddress &address) {
    m_address = address;
    m_address_isSet = true;
}

bool OAIShareProfileRequest_patient_userDemographics::is_address_Set() const{
    return m_address_isSet;
}

bool OAIShareProfileRequest_patient_userDemographics::is_address_Valid() const{
    return m_address_isValid;
}

qint32 OAIShareProfileRequest_patient_userDemographics::getDayOfBirth() const {
    return m_day_of_birth;
}
void OAIShareProfileRequest_patient_userDemographics::setDayOfBirth(const qint32 &day_of_birth) {
    m_day_of_birth = day_of_birth;
    m_day_of_birth_isSet = true;
}

bool OAIShareProfileRequest_patient_userDemographics::is_day_of_birth_Set() const{
    return m_day_of_birth_isSet;
}

bool OAIShareProfileRequest_patient_userDemographics::is_day_of_birth_Valid() const{
    return m_day_of_birth_isValid;
}

OAIPatientGender OAIShareProfileRequest_patient_userDemographics::getGender() const {
    return m_gender;
}
void OAIShareProfileRequest_patient_userDemographics::setGender(const OAIPatientGender &gender) {
    m_gender = gender;
    m_gender_isSet = true;
}

bool OAIShareProfileRequest_patient_userDemographics::is_gender_Set() const{
    return m_gender_isSet;
}

bool OAIShareProfileRequest_patient_userDemographics::is_gender_Valid() const{
    return m_gender_isValid;
}

QString OAIShareProfileRequest_patient_userDemographics::getHealthId() const {
    return m_health_id;
}
void OAIShareProfileRequest_patient_userDemographics::setHealthId(const QString &health_id) {
    m_health_id = health_id;
    m_health_id_isSet = true;
}

bool OAIShareProfileRequest_patient_userDemographics::is_health_id_Set() const{
    return m_health_id_isSet;
}

bool OAIShareProfileRequest_patient_userDemographics::is_health_id_Valid() const{
    return m_health_id_isValid;
}

QString OAIShareProfileRequest_patient_userDemographics::getHealthIdNumber() const {
    return m_health_id_number;
}
void OAIShareProfileRequest_patient_userDemographics::setHealthIdNumber(const QString &health_id_number) {
    m_health_id_number = health_id_number;
    m_health_id_number_isSet = true;
}

bool OAIShareProfileRequest_patient_userDemographics::is_health_id_number_Set() const{
    return m_health_id_number_isSet;
}

bool OAIShareProfileRequest_patient_userDemographics::is_health_id_number_Valid() const{
    return m_health_id_number_isValid;
}

QList<OAIIdentifier> OAIShareProfileRequest_patient_userDemographics::getIdentifiers() const {
    return m_identifiers;
}
void OAIShareProfileRequest_patient_userDemographics::setIdentifiers(const QList<OAIIdentifier> &identifiers) {
    m_identifiers = identifiers;
    m_identifiers_isSet = true;
}

bool OAIShareProfileRequest_patient_userDemographics::is_identifiers_Set() const{
    return m_identifiers_isSet;
}

bool OAIShareProfileRequest_patient_userDemographics::is_identifiers_Valid() const{
    return m_identifiers_isValid;
}

qint32 OAIShareProfileRequest_patient_userDemographics::getMonthOfBirth() const {
    return m_month_of_birth;
}
void OAIShareProfileRequest_patient_userDemographics::setMonthOfBirth(const qint32 &month_of_birth) {
    m_month_of_birth = month_of_birth;
    m_month_of_birth_isSet = true;
}

bool OAIShareProfileRequest_patient_userDemographics::is_month_of_birth_Set() const{
    return m_month_of_birth_isSet;
}

bool OAIShareProfileRequest_patient_userDemographics::is_month_of_birth_Valid() const{
    return m_month_of_birth_isValid;
}

QString OAIShareProfileRequest_patient_userDemographics::getName() const {
    return m_name;
}
void OAIShareProfileRequest_patient_userDemographics::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIShareProfileRequest_patient_userDemographics::is_name_Set() const{
    return m_name_isSet;
}

bool OAIShareProfileRequest_patient_userDemographics::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAIShareProfileRequest_patient_userDemographics::getYearOfBirth() const {
    return m_year_of_birth;
}
void OAIShareProfileRequest_patient_userDemographics::setYearOfBirth(const qint32 &year_of_birth) {
    m_year_of_birth = year_of_birth;
    m_year_of_birth_isSet = true;
}

bool OAIShareProfileRequest_patient_userDemographics::is_year_of_birth_Set() const{
    return m_year_of_birth_isSet;
}

bool OAIShareProfileRequest_patient_userDemographics::is_year_of_birth_Valid() const{
    return m_year_of_birth_isValid;
}

bool OAIShareProfileRequest_patient_userDemographics::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_day_of_birth_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gender.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_health_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_health_id_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_identifiers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_month_of_birth_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_year_of_birth_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIShareProfileRequest_patient_userDemographics::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_gender_isValid && m_health_id_isValid && m_health_id_number_isValid && m_name_isValid && m_year_of_birth_isValid && true;
}

} // namespace OpenAPI
