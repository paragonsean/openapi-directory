/**
 * VAT API
 * A developer friendly API to help your business achieve VAT compliance
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIVat_Rates_Countries.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVat_Rates_Countries::OAIVat_Rates_Countries(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVat_Rates_Countries::OAIVat_Rates_Countries() {
    this->initializeModel();
}

OAIVat_Rates_Countries::~OAIVat_Rates_Countries() {}

void OAIVat_Rates_Countries::initializeModel() {

    m_country_code_isSet = false;
    m_country_code_isValid = false;
}

void OAIVat_Rates_Countries::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVat_Rates_Countries::fromJsonObject(QJsonObject json) {

    m_country_code_isValid = ::OpenAPI::fromJsonValue(m_country_code, json[QString("country_code")]);
    m_country_code_isSet = !json[QString("country_code")].isNull() && m_country_code_isValid;
}

QString OAIVat_Rates_Countries::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVat_Rates_Countries::asJsonObject() const {
    QJsonObject obj;
    if (m_country_code.isSet()) {
        obj.insert(QString("country_code"), ::OpenAPI::toJsonValue(m_country_code));
    }
    return obj;
}

OAICountry_Data OAIVat_Rates_Countries::getCountryCode() const {
    return m_country_code;
}
void OAIVat_Rates_Countries::setCountryCode(const OAICountry_Data &country_code) {
    m_country_code = country_code;
    m_country_code_isSet = true;
}

bool OAIVat_Rates_Countries::is_country_code_Set() const{
    return m_country_code_isSet;
}

bool OAIVat_Rates_Countries::is_country_code_Valid() const{
    return m_country_code_isValid;
}

bool OAIVat_Rates_Countries::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_country_code.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVat_Rates_Countries::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_country_code_isValid && true;
}

} // namespace OpenAPI
