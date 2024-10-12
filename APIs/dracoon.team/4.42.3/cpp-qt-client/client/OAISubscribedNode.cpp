/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISubscribedNode.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISubscribedNode::OAISubscribedNode(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISubscribedNode::OAISubscribedNode() {
    this->initializeModel();
}

OAISubscribedNode::~OAISubscribedNode() {}

void OAISubscribedNode::initializeModel() {

    m_auth_parent_id_isSet = false;
    m_auth_parent_id_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAISubscribedNode::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISubscribedNode::fromJsonObject(QJsonObject json) {

    m_auth_parent_id_isValid = ::OpenAPI::fromJsonValue(m_auth_parent_id, json[QString("authParentId")]);
    m_auth_parent_id_isSet = !json[QString("authParentId")].isNull() && m_auth_parent_id_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAISubscribedNode::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISubscribedNode::asJsonObject() const {
    QJsonObject obj;
    if (m_auth_parent_id_isSet) {
        obj.insert(QString("authParentId"), ::OpenAPI::toJsonValue(m_auth_parent_id));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

qint64 OAISubscribedNode::getAuthParentId() const {
    return m_auth_parent_id;
}
void OAISubscribedNode::setAuthParentId(const qint64 &auth_parent_id) {
    m_auth_parent_id = auth_parent_id;
    m_auth_parent_id_isSet = true;
}

bool OAISubscribedNode::is_auth_parent_id_Set() const{
    return m_auth_parent_id_isSet;
}

bool OAISubscribedNode::is_auth_parent_id_Valid() const{
    return m_auth_parent_id_isValid;
}

qint64 OAISubscribedNode::getId() const {
    return m_id;
}
void OAISubscribedNode::setId(const qint64 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAISubscribedNode::is_id_Set() const{
    return m_id_isSet;
}

bool OAISubscribedNode::is_id_Valid() const{
    return m_id_isValid;
}

QString OAISubscribedNode::getType() const {
    return m_type;
}
void OAISubscribedNode::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAISubscribedNode::is_type_Set() const{
    return m_type_isSet;
}

bool OAISubscribedNode::is_type_Valid() const{
    return m_type_isValid;
}

bool OAISubscribedNode::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_auth_parent_id_isSet) {
            isObjectUpdated = true;
            break;
        }

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

bool OAISubscribedNode::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && true;
}

} // namespace OpenAPI
