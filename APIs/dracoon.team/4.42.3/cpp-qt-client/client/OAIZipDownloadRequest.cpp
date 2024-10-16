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

#include "OAIZipDownloadRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIZipDownloadRequest::OAIZipDownloadRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIZipDownloadRequest::OAIZipDownloadRequest() {
    this->initializeModel();
}

OAIZipDownloadRequest::~OAIZipDownloadRequest() {}

void OAIZipDownloadRequest::initializeModel() {

    m_node_ids_isSet = false;
    m_node_ids_isValid = false;
}

void OAIZipDownloadRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIZipDownloadRequest::fromJsonObject(QJsonObject json) {

    m_node_ids_isValid = ::OpenAPI::fromJsonValue(m_node_ids, json[QString("nodeIds")]);
    m_node_ids_isSet = !json[QString("nodeIds")].isNull() && m_node_ids_isValid;
}

QString OAIZipDownloadRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIZipDownloadRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_node_ids.size() > 0) {
        obj.insert(QString("nodeIds"), ::OpenAPI::toJsonValue(m_node_ids));
    }
    return obj;
}

QList<qint64> OAIZipDownloadRequest::getNodeIds() const {
    return m_node_ids;
}
void OAIZipDownloadRequest::setNodeIds(const QList<qint64> &node_ids) {
    m_node_ids = node_ids;
    m_node_ids_isSet = true;
}

bool OAIZipDownloadRequest::is_node_ids_Set() const{
    return m_node_ids_isSet;
}

bool OAIZipDownloadRequest::is_node_ids_Valid() const{
    return m_node_ids_isValid;
}

bool OAIZipDownloadRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_node_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIZipDownloadRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_node_ids_isValid && true;
}

} // namespace OpenAPI
