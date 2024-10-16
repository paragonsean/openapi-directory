/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBenefit_CurrencyWithGrowth.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBenefit_CurrencyWithGrowth::OAIBenefit_CurrencyWithGrowth(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBenefit_CurrencyWithGrowth::OAIBenefit_CurrencyWithGrowth() {
    this->initializeModel();
}

OAIBenefit_CurrencyWithGrowth::~OAIBenefit_CurrencyWithGrowth() {}

void OAIBenefit_CurrencyWithGrowth::initializeModel() {

    m_benefit_type_isSet = false;
    m_benefit_type_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIBenefit_CurrencyWithGrowth::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBenefit_CurrencyWithGrowth::fromJsonObject(QJsonObject json) {

    m_benefit_type_isValid = ::OpenAPI::fromJsonValue(m_benefit_type, json[QString("benefitType")]);
    m_benefit_type_isSet = !json[QString("benefitType")].isNull() && m_benefit_type_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIBenefit_CurrencyWithGrowth::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBenefit_CurrencyWithGrowth::asJsonObject() const {
    QJsonObject obj;
    if (m_benefit_type_isSet) {
        obj.insert(QString("benefitType"), ::OpenAPI::toJsonValue(m_benefit_type));
    }
    if (m_value.isSet()) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIBenefit_CurrencyWithGrowth::getBenefitType() const {
    return m_benefit_type;
}
void OAIBenefit_CurrencyWithGrowth::setBenefitType(const QString &benefit_type) {
    m_benefit_type = benefit_type;
    m_benefit_type_isSet = true;
}

bool OAIBenefit_CurrencyWithGrowth::is_benefit_type_Set() const{
    return m_benefit_type_isSet;
}

bool OAIBenefit_CurrencyWithGrowth::is_benefit_type_Valid() const{
    return m_benefit_type_isValid;
}

OAICurrencyWithGrowth OAIBenefit_CurrencyWithGrowth::getValue() const {
    return m_value;
}
void OAIBenefit_CurrencyWithGrowth::setValue(const OAICurrencyWithGrowth &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIBenefit_CurrencyWithGrowth::is_value_Set() const{
    return m_value_isSet;
}

bool OAIBenefit_CurrencyWithGrowth::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIBenefit_CurrencyWithGrowth::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_benefit_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBenefit_CurrencyWithGrowth::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
