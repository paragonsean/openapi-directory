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

#include "OAIShared_ColorTransformationAttributes.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIShared_ColorTransformationAttributes::OAIShared_ColorTransformationAttributes(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIShared_ColorTransformationAttributes::OAIShared_ColorTransformationAttributes() {
    this->initializeModel();
}

OAIShared_ColorTransformationAttributes::~OAIShared_ColorTransformationAttributes() {}

void OAIShared_ColorTransformationAttributes::initializeModel() {

    m_color_transformations_id_isSet = false;
    m_color_transformations_id_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIShared_ColorTransformationAttributes::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIShared_ColorTransformationAttributes::fromJsonObject(QJsonObject json) {

    m_color_transformations_id_isValid = ::OpenAPI::fromJsonValue(m_color_transformations_id, json[QString("colorTransformationsId")]);
    m_color_transformations_id_isSet = !json[QString("colorTransformationsId")].isNull() && m_color_transformations_id_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIShared_ColorTransformationAttributes::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIShared_ColorTransformationAttributes::asJsonObject() const {
    QJsonObject obj;
    if (m_color_transformations_id_isSet) {
        obj.insert(QString("colorTransformationsId"), ::OpenAPI::toJsonValue(m_color_transformations_id));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIShared_ColorTransformationAttributes::getColorTransformationsId() const {
    return m_color_transformations_id;
}
void OAIShared_ColorTransformationAttributes::setColorTransformationsId(const QString &color_transformations_id) {
    m_color_transformations_id = color_transformations_id;
    m_color_transformations_id_isSet = true;
}

bool OAIShared_ColorTransformationAttributes::is_color_transformations_id_Set() const{
    return m_color_transformations_id_isSet;
}

bool OAIShared_ColorTransformationAttributes::is_color_transformations_id_Valid() const{
    return m_color_transformations_id_isValid;
}

QString OAIShared_ColorTransformationAttributes::getId() const {
    return m_id;
}
void OAIShared_ColorTransformationAttributes::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIShared_ColorTransformationAttributes::is_id_Set() const{
    return m_id_isSet;
}

bool OAIShared_ColorTransformationAttributes::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIShared_ColorTransformationAttributes::getName() const {
    return m_name;
}
void OAIShared_ColorTransformationAttributes::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIShared_ColorTransformationAttributes::is_name_Set() const{
    return m_name_isSet;
}

bool OAIShared_ColorTransformationAttributes::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIShared_ColorTransformationAttributes::getValue() const {
    return m_value;
}
void OAIShared_ColorTransformationAttributes::setValue(const QString &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIShared_ColorTransformationAttributes::is_value_Set() const{
    return m_value_isSet;
}

bool OAIShared_ColorTransformationAttributes::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIShared_ColorTransformationAttributes::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_color_transformations_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
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

bool OAIShared_ColorTransformationAttributes::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
