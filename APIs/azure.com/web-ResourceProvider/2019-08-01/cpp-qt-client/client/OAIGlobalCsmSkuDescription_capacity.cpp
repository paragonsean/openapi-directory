/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGlobalCsmSkuDescription_capacity.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGlobalCsmSkuDescription_capacity::OAIGlobalCsmSkuDescription_capacity(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGlobalCsmSkuDescription_capacity::OAIGlobalCsmSkuDescription_capacity() {
    this->initializeModel();
}

OAIGlobalCsmSkuDescription_capacity::~OAIGlobalCsmSkuDescription_capacity() {}

void OAIGlobalCsmSkuDescription_capacity::initializeModel() {

    m_r_default_isSet = false;
    m_r_default_isValid = false;

    m_maximum_isSet = false;
    m_maximum_isValid = false;

    m_minimum_isSet = false;
    m_minimum_isValid = false;

    m_scale_type_isSet = false;
    m_scale_type_isValid = false;
}

void OAIGlobalCsmSkuDescription_capacity::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGlobalCsmSkuDescription_capacity::fromJsonObject(QJsonObject json) {

    m_r_default_isValid = ::OpenAPI::fromJsonValue(m_r_default, json[QString("default")]);
    m_r_default_isSet = !json[QString("default")].isNull() && m_r_default_isValid;

    m_maximum_isValid = ::OpenAPI::fromJsonValue(m_maximum, json[QString("maximum")]);
    m_maximum_isSet = !json[QString("maximum")].isNull() && m_maximum_isValid;

    m_minimum_isValid = ::OpenAPI::fromJsonValue(m_minimum, json[QString("minimum")]);
    m_minimum_isSet = !json[QString("minimum")].isNull() && m_minimum_isValid;

    m_scale_type_isValid = ::OpenAPI::fromJsonValue(m_scale_type, json[QString("scaleType")]);
    m_scale_type_isSet = !json[QString("scaleType")].isNull() && m_scale_type_isValid;
}

QString OAIGlobalCsmSkuDescription_capacity::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGlobalCsmSkuDescription_capacity::asJsonObject() const {
    QJsonObject obj;
    if (m_r_default_isSet) {
        obj.insert(QString("default"), ::OpenAPI::toJsonValue(m_r_default));
    }
    if (m_maximum_isSet) {
        obj.insert(QString("maximum"), ::OpenAPI::toJsonValue(m_maximum));
    }
    if (m_minimum_isSet) {
        obj.insert(QString("minimum"), ::OpenAPI::toJsonValue(m_minimum));
    }
    if (m_scale_type_isSet) {
        obj.insert(QString("scaleType"), ::OpenAPI::toJsonValue(m_scale_type));
    }
    return obj;
}

qint32 OAIGlobalCsmSkuDescription_capacity::getRDefault() const {
    return m_r_default;
}
void OAIGlobalCsmSkuDescription_capacity::setRDefault(const qint32 &r_default) {
    m_r_default = r_default;
    m_r_default_isSet = true;
}

bool OAIGlobalCsmSkuDescription_capacity::is_r_default_Set() const{
    return m_r_default_isSet;
}

bool OAIGlobalCsmSkuDescription_capacity::is_r_default_Valid() const{
    return m_r_default_isValid;
}

qint32 OAIGlobalCsmSkuDescription_capacity::getMaximum() const {
    return m_maximum;
}
void OAIGlobalCsmSkuDescription_capacity::setMaximum(const qint32 &maximum) {
    m_maximum = maximum;
    m_maximum_isSet = true;
}

bool OAIGlobalCsmSkuDescription_capacity::is_maximum_Set() const{
    return m_maximum_isSet;
}

bool OAIGlobalCsmSkuDescription_capacity::is_maximum_Valid() const{
    return m_maximum_isValid;
}

qint32 OAIGlobalCsmSkuDescription_capacity::getMinimum() const {
    return m_minimum;
}
void OAIGlobalCsmSkuDescription_capacity::setMinimum(const qint32 &minimum) {
    m_minimum = minimum;
    m_minimum_isSet = true;
}

bool OAIGlobalCsmSkuDescription_capacity::is_minimum_Set() const{
    return m_minimum_isSet;
}

bool OAIGlobalCsmSkuDescription_capacity::is_minimum_Valid() const{
    return m_minimum_isValid;
}

QString OAIGlobalCsmSkuDescription_capacity::getScaleType() const {
    return m_scale_type;
}
void OAIGlobalCsmSkuDescription_capacity::setScaleType(const QString &scale_type) {
    m_scale_type = scale_type;
    m_scale_type_isSet = true;
}

bool OAIGlobalCsmSkuDescription_capacity::is_scale_type_Set() const{
    return m_scale_type_isSet;
}

bool OAIGlobalCsmSkuDescription_capacity::is_scale_type_Valid() const{
    return m_scale_type_isValid;
}

bool OAIGlobalCsmSkuDescription_capacity::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_r_default_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_maximum_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_minimum_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_scale_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGlobalCsmSkuDescription_capacity::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
