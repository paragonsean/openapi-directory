/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRelationshipData.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRelationshipData::OAIRelationshipData(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRelationshipData::OAIRelationshipData() {
    this->initializeModel();
}

OAIRelationshipData::~OAIRelationshipData() {}

void OAIRelationshipData::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIRelationshipData::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRelationshipData::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIRelationshipData::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRelationshipData::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

qint32 OAIRelationshipData::getId() const {
    return m_id;
}
void OAIRelationshipData::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIRelationshipData::is_id_Set() const{
    return m_id_isSet;
}

bool OAIRelationshipData::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIRelationshipData::getType() const {
    return m_type;
}
void OAIRelationshipData::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIRelationshipData::is_type_Set() const{
    return m_type_isSet;
}

bool OAIRelationshipData::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIRelationshipData::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRelationshipData::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
