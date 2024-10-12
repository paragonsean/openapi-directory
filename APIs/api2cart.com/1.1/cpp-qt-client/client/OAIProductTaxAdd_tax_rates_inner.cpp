/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIProductTaxAdd_tax_rates_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProductTaxAdd_tax_rates_inner::OAIProductTaxAdd_tax_rates_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProductTaxAdd_tax_rates_inner::OAIProductTaxAdd_tax_rates_inner() {
    this->initializeModel();
}

OAIProductTaxAdd_tax_rates_inner::~OAIProductTaxAdd_tax_rates_inner() {}

void OAIProductTaxAdd_tax_rates_inner::initializeModel() {

    m_name_isSet = false;
    m_name_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIProductTaxAdd_tax_rates_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProductTaxAdd_tax_rates_inner::fromJsonObject(QJsonObject json) {

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIProductTaxAdd_tax_rates_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProductTaxAdd_tax_rates_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIProductTaxAdd_tax_rates_inner::getName() const {
    return m_name;
}
void OAIProductTaxAdd_tax_rates_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIProductTaxAdd_tax_rates_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIProductTaxAdd_tax_rates_inner::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIProductTaxAdd_tax_rates_inner::getType() const {
    return m_type;
}
void OAIProductTaxAdd_tax_rates_inner::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIProductTaxAdd_tax_rates_inner::is_type_Set() const{
    return m_type_isSet;
}

bool OAIProductTaxAdd_tax_rates_inner::is_type_Valid() const{
    return m_type_isValid;
}

double OAIProductTaxAdd_tax_rates_inner::getValue() const {
    return m_value;
}
void OAIProductTaxAdd_tax_rates_inner::setValue(const double &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIProductTaxAdd_tax_rates_inner::is_value_Set() const{
    return m_value_isSet;
}

bool OAIProductTaxAdd_tax_rates_inner::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIProductTaxAdd_tax_rates_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIProductTaxAdd_tax_rates_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
