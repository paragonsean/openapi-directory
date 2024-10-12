/**
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIARMBaseModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIARMBaseModel::OAIARMBaseModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIARMBaseModel::OAIARMBaseModel() {
    this->initializeModel();
}

OAIARMBaseModel::~OAIARMBaseModel() {}

void OAIARMBaseModel::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIARMBaseModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIARMBaseModel::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIARMBaseModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIARMBaseModel::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIARMBaseModel::getId() const {
    return m_id;
}
void OAIARMBaseModel::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIARMBaseModel::is_id_Set() const{
    return m_id_isSet;
}

bool OAIARMBaseModel::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIARMBaseModel::getName() const {
    return m_name;
}
void OAIARMBaseModel::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIARMBaseModel::is_name_Set() const{
    return m_name_isSet;
}

bool OAIARMBaseModel::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIARMBaseModel::getType() const {
    return m_type;
}
void OAIARMBaseModel::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIARMBaseModel::is_type_Set() const{
    return m_type_isSet;
}

bool OAIARMBaseModel::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIARMBaseModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
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

bool OAIARMBaseModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
