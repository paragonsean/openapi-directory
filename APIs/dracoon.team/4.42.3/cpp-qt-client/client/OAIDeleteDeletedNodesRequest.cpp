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

#include "OAIDeleteDeletedNodesRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDeleteDeletedNodesRequest::OAIDeleteDeletedNodesRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDeleteDeletedNodesRequest::OAIDeleteDeletedNodesRequest() {
    this->initializeModel();
}

OAIDeleteDeletedNodesRequest::~OAIDeleteDeletedNodesRequest() {}

void OAIDeleteDeletedNodesRequest::initializeModel() {

    m_deleted_node_ids_isSet = false;
    m_deleted_node_ids_isValid = false;
}

void OAIDeleteDeletedNodesRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDeleteDeletedNodesRequest::fromJsonObject(QJsonObject json) {

    m_deleted_node_ids_isValid = ::OpenAPI::fromJsonValue(m_deleted_node_ids, json[QString("deletedNodeIds")]);
    m_deleted_node_ids_isSet = !json[QString("deletedNodeIds")].isNull() && m_deleted_node_ids_isValid;
}

QString OAIDeleteDeletedNodesRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDeleteDeletedNodesRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_deleted_node_ids.size() > 0) {
        obj.insert(QString("deletedNodeIds"), ::OpenAPI::toJsonValue(m_deleted_node_ids));
    }
    return obj;
}

QList<qint64> OAIDeleteDeletedNodesRequest::getDeletedNodeIds() const {
    return m_deleted_node_ids;
}
void OAIDeleteDeletedNodesRequest::setDeletedNodeIds(const QList<qint64> &deleted_node_ids) {
    m_deleted_node_ids = deleted_node_ids;
    m_deleted_node_ids_isSet = true;
}

bool OAIDeleteDeletedNodesRequest::is_deleted_node_ids_Set() const{
    return m_deleted_node_ids_isSet;
}

bool OAIDeleteDeletedNodesRequest::is_deleted_node_ids_Valid() const{
    return m_deleted_node_ids_isValid;
}

bool OAIDeleteDeletedNodesRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_deleted_node_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDeleteDeletedNodesRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_deleted_node_ids_isValid && true;
}

} // namespace OpenAPI
