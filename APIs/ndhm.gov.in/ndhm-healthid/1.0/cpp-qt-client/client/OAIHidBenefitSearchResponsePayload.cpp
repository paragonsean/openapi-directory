/**
 * Health ID Service
 * It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent.  In order to issue a Health ID to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIHidBenefitSearchResponsePayload.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIHidBenefitSearchResponsePayload::OAIHidBenefitSearchResponsePayload(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIHidBenefitSearchResponsePayload::OAIHidBenefitSearchResponsePayload() {
    this->initializeModel();
}

OAIHidBenefitSearchResponsePayload::~OAIHidBenefitSearchResponsePayload() {}

void OAIHidBenefitSearchResponsePayload::initializeModel() {

    m_benefit_id_isSet = false;
    m_benefit_id_isValid = false;

    m_benefit_name_isSet = false;
    m_benefit_name_isValid = false;

    m_health_id_number_isSet = false;
    m_health_id_number_isValid = false;

    m_state_code_isSet = false;
    m_state_code_isValid = false;
}

void OAIHidBenefitSearchResponsePayload::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIHidBenefitSearchResponsePayload::fromJsonObject(QJsonObject json) {

    m_benefit_id_isValid = ::OpenAPI::fromJsonValue(m_benefit_id, json[QString("benefitId")]);
    m_benefit_id_isSet = !json[QString("benefitId")].isNull() && m_benefit_id_isValid;

    m_benefit_name_isValid = ::OpenAPI::fromJsonValue(m_benefit_name, json[QString("benefitName")]);
    m_benefit_name_isSet = !json[QString("benefitName")].isNull() && m_benefit_name_isValid;

    m_health_id_number_isValid = ::OpenAPI::fromJsonValue(m_health_id_number, json[QString("healthIdNumber")]);
    m_health_id_number_isSet = !json[QString("healthIdNumber")].isNull() && m_health_id_number_isValid;

    m_state_code_isValid = ::OpenAPI::fromJsonValue(m_state_code, json[QString("stateCode")]);
    m_state_code_isSet = !json[QString("stateCode")].isNull() && m_state_code_isValid;
}

QString OAIHidBenefitSearchResponsePayload::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIHidBenefitSearchResponsePayload::asJsonObject() const {
    QJsonObject obj;
    if (m_benefit_id_isSet) {
        obj.insert(QString("benefitId"), ::OpenAPI::toJsonValue(m_benefit_id));
    }
    if (m_benefit_name_isSet) {
        obj.insert(QString("benefitName"), ::OpenAPI::toJsonValue(m_benefit_name));
    }
    if (m_health_id_number_isSet) {
        obj.insert(QString("healthIdNumber"), ::OpenAPI::toJsonValue(m_health_id_number));
    }
    if (m_state_code_isSet) {
        obj.insert(QString("stateCode"), ::OpenAPI::toJsonValue(m_state_code));
    }
    return obj;
}

QString OAIHidBenefitSearchResponsePayload::getBenefitId() const {
    return m_benefit_id;
}
void OAIHidBenefitSearchResponsePayload::setBenefitId(const QString &benefit_id) {
    m_benefit_id = benefit_id;
    m_benefit_id_isSet = true;
}

bool OAIHidBenefitSearchResponsePayload::is_benefit_id_Set() const{
    return m_benefit_id_isSet;
}

bool OAIHidBenefitSearchResponsePayload::is_benefit_id_Valid() const{
    return m_benefit_id_isValid;
}

QString OAIHidBenefitSearchResponsePayload::getBenefitName() const {
    return m_benefit_name;
}
void OAIHidBenefitSearchResponsePayload::setBenefitName(const QString &benefit_name) {
    m_benefit_name = benefit_name;
    m_benefit_name_isSet = true;
}

bool OAIHidBenefitSearchResponsePayload::is_benefit_name_Set() const{
    return m_benefit_name_isSet;
}

bool OAIHidBenefitSearchResponsePayload::is_benefit_name_Valid() const{
    return m_benefit_name_isValid;
}

QString OAIHidBenefitSearchResponsePayload::getHealthIdNumber() const {
    return m_health_id_number;
}
void OAIHidBenefitSearchResponsePayload::setHealthIdNumber(const QString &health_id_number) {
    m_health_id_number = health_id_number;
    m_health_id_number_isSet = true;
}

bool OAIHidBenefitSearchResponsePayload::is_health_id_number_Set() const{
    return m_health_id_number_isSet;
}

bool OAIHidBenefitSearchResponsePayload::is_health_id_number_Valid() const{
    return m_health_id_number_isValid;
}

QString OAIHidBenefitSearchResponsePayload::getStateCode() const {
    return m_state_code;
}
void OAIHidBenefitSearchResponsePayload::setStateCode(const QString &state_code) {
    m_state_code = state_code;
    m_state_code_isSet = true;
}

bool OAIHidBenefitSearchResponsePayload::is_state_code_Set() const{
    return m_state_code_isSet;
}

bool OAIHidBenefitSearchResponsePayload::is_state_code_Valid() const{
    return m_state_code_isValid;
}

bool OAIHidBenefitSearchResponsePayload::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_benefit_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_benefit_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_health_id_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_code_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIHidBenefitSearchResponsePayload::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
