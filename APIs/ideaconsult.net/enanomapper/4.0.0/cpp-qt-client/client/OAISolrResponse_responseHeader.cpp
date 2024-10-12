/**
 * eNanoMapper database
 * AMBIT REST web services [eNanoMapper profile] with free text & faceted search
 *
 * The version of the OpenAPI document: 4.0.0
 * Contact: support@ideaconsult.net
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISolrResponse_responseHeader.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISolrResponse_responseHeader::OAISolrResponse_responseHeader(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISolrResponse_responseHeader::OAISolrResponse_responseHeader() {
    this->initializeModel();
}

OAISolrResponse_responseHeader::~OAISolrResponse_responseHeader() {}

void OAISolrResponse_responseHeader::initializeModel() {

    m_q_time_isSet = false;
    m_q_time_isValid = false;

    m_params_isSet = false;
    m_params_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_zk_connected_isSet = false;
    m_zk_connected_isValid = false;
}

void OAISolrResponse_responseHeader::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISolrResponse_responseHeader::fromJsonObject(QJsonObject json) {

    m_q_time_isValid = ::OpenAPI::fromJsonValue(m_q_time, json[QString("QTime")]);
    m_q_time_isSet = !json[QString("QTime")].isNull() && m_q_time_isValid;

    m_params_isValid = ::OpenAPI::fromJsonValue(m_params, json[QString("params")]);
    m_params_isSet = !json[QString("params")].isNull() && m_params_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_zk_connected_isValid = ::OpenAPI::fromJsonValue(m_zk_connected, json[QString("zkConnected")]);
    m_zk_connected_isSet = !json[QString("zkConnected")].isNull() && m_zk_connected_isValid;
}

QString OAISolrResponse_responseHeader::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISolrResponse_responseHeader::asJsonObject() const {
    QJsonObject obj;
    if (m_q_time_isSet) {
        obj.insert(QString("QTime"), ::OpenAPI::toJsonValue(m_q_time));
    }
    if (m_params_isSet) {
        obj.insert(QString("params"), ::OpenAPI::toJsonValue(m_params));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_zk_connected_isSet) {
        obj.insert(QString("zkConnected"), ::OpenAPI::toJsonValue(m_zk_connected));
    }
    return obj;
}

qint32 OAISolrResponse_responseHeader::getQTime() const {
    return m_q_time;
}
void OAISolrResponse_responseHeader::setQTime(const qint32 &q_time) {
    m_q_time = q_time;
    m_q_time_isSet = true;
}

bool OAISolrResponse_responseHeader::is_q_time_Set() const{
    return m_q_time_isSet;
}

bool OAISolrResponse_responseHeader::is_q_time_Valid() const{
    return m_q_time_isValid;
}

OAIObject OAISolrResponse_responseHeader::getParams() const {
    return m_params;
}
void OAISolrResponse_responseHeader::setParams(const OAIObject &params) {
    m_params = params;
    m_params_isSet = true;
}

bool OAISolrResponse_responseHeader::is_params_Set() const{
    return m_params_isSet;
}

bool OAISolrResponse_responseHeader::is_params_Valid() const{
    return m_params_isValid;
}

qint32 OAISolrResponse_responseHeader::getStatus() const {
    return m_status;
}
void OAISolrResponse_responseHeader::setStatus(const qint32 &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAISolrResponse_responseHeader::is_status_Set() const{
    return m_status_isSet;
}

bool OAISolrResponse_responseHeader::is_status_Valid() const{
    return m_status_isValid;
}

bool OAISolrResponse_responseHeader::isZkConnected() const {
    return m_zk_connected;
}
void OAISolrResponse_responseHeader::setZkConnected(const bool &zk_connected) {
    m_zk_connected = zk_connected;
    m_zk_connected_isSet = true;
}

bool OAISolrResponse_responseHeader::is_zk_connected_Set() const{
    return m_zk_connected_isSet;
}

bool OAISolrResponse_responseHeader::is_zk_connected_Valid() const{
    return m_zk_connected_isValid;
}

bool OAISolrResponse_responseHeader::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_q_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_params_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_zk_connected_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISolrResponse_responseHeader::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
