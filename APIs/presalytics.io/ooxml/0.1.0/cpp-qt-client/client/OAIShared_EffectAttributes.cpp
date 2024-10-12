/**
 * OOXML Automation
 * This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.
 *
 * The version of the OpenAPI document: 0.1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIShared_EffectAttributes.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIShared_EffectAttributes::OAIShared_EffectAttributes(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIShared_EffectAttributes::OAIShared_EffectAttributes() {
    this->initializeModel();
}

OAIShared_EffectAttributes::~OAIShared_EffectAttributes() {}

void OAIShared_EffectAttributes::initializeModel() {

    m_attributes_json_isSet = false;
    m_attributes_json_isValid = false;

    m_effect_id_isSet = false;
    m_effect_id_isValid = false;

    m_effect_type_id_isSet = false;
    m_effect_type_id_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;
}

void OAIShared_EffectAttributes::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIShared_EffectAttributes::fromJsonObject(QJsonObject json) {

    m_attributes_json_isValid = ::OpenAPI::fromJsonValue(m_attributes_json, json[QString("attributesJson")]);
    m_attributes_json_isSet = !json[QString("attributesJson")].isNull() && m_attributes_json_isValid;

    m_effect_id_isValid = ::OpenAPI::fromJsonValue(m_effect_id, json[QString("effectId")]);
    m_effect_id_isSet = !json[QString("effectId")].isNull() && m_effect_id_isValid;

    m_effect_type_id_isValid = ::OpenAPI::fromJsonValue(m_effect_type_id, json[QString("effectTypeId")]);
    m_effect_type_id_isSet = !json[QString("effectTypeId")].isNull() && m_effect_type_id_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;
}

QString OAIShared_EffectAttributes::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIShared_EffectAttributes::asJsonObject() const {
    QJsonObject obj;
    if (m_attributes_json_isSet) {
        obj.insert(QString("attributesJson"), ::OpenAPI::toJsonValue(m_attributes_json));
    }
    if (m_effect_id_isSet) {
        obj.insert(QString("effectId"), ::OpenAPI::toJsonValue(m_effect_id));
    }
    if (m_effect_type_id_isSet) {
        obj.insert(QString("effectTypeId"), ::OpenAPI::toJsonValue(m_effect_type_id));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    return obj;
}

QString OAIShared_EffectAttributes::getAttributesJson() const {
    return m_attributes_json;
}
void OAIShared_EffectAttributes::setAttributesJson(const QString &attributes_json) {
    m_attributes_json = attributes_json;
    m_attributes_json_isSet = true;
}

bool OAIShared_EffectAttributes::is_attributes_json_Set() const{
    return m_attributes_json_isSet;
}

bool OAIShared_EffectAttributes::is_attributes_json_Valid() const{
    return m_attributes_json_isValid;
}

QString OAIShared_EffectAttributes::getEffectId() const {
    return m_effect_id;
}
void OAIShared_EffectAttributes::setEffectId(const QString &effect_id) {
    m_effect_id = effect_id;
    m_effect_id_isSet = true;
}

bool OAIShared_EffectAttributes::is_effect_id_Set() const{
    return m_effect_id_isSet;
}

bool OAIShared_EffectAttributes::is_effect_id_Valid() const{
    return m_effect_id_isValid;
}

qint32 OAIShared_EffectAttributes::getEffectTypeId() const {
    return m_effect_type_id;
}
void OAIShared_EffectAttributes::setEffectTypeId(const qint32 &effect_type_id) {
    m_effect_type_id = effect_type_id;
    m_effect_type_id_isSet = true;
}

bool OAIShared_EffectAttributes::is_effect_type_id_Set() const{
    return m_effect_type_id_isSet;
}

bool OAIShared_EffectAttributes::is_effect_type_id_Valid() const{
    return m_effect_type_id_isValid;
}

QString OAIShared_EffectAttributes::getId() const {
    return m_id;
}
void OAIShared_EffectAttributes::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIShared_EffectAttributes::is_id_Set() const{
    return m_id_isSet;
}

bool OAIShared_EffectAttributes::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIShared_EffectAttributes::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_attributes_json_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_effect_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_effect_type_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIShared_EffectAttributes::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
