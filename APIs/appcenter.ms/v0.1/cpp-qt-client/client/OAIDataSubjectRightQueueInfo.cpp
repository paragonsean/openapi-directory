/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDataSubjectRightQueueInfo.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDataSubjectRightQueueInfo::OAIDataSubjectRightQueueInfo(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDataSubjectRightQueueInfo::OAIDataSubjectRightQueueInfo() {
    this->initializeModel();
}

OAIDataSubjectRightQueueInfo::~OAIDataSubjectRightQueueInfo() {}

void OAIDataSubjectRightQueueInfo::initializeModel() {

    m_expires_at_isSet = false;
    m_expires_at_isValid = false;

    m_queue_name_isSet = false;
    m_queue_name_isValid = false;

    m_sas_uri_isSet = false;
    m_sas_uri_isValid = false;
}

void OAIDataSubjectRightQueueInfo::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDataSubjectRightQueueInfo::fromJsonObject(QJsonObject json) {

    m_expires_at_isValid = ::OpenAPI::fromJsonValue(m_expires_at, json[QString("expiresAt")]);
    m_expires_at_isSet = !json[QString("expiresAt")].isNull() && m_expires_at_isValid;

    m_queue_name_isValid = ::OpenAPI::fromJsonValue(m_queue_name, json[QString("queueName")]);
    m_queue_name_isSet = !json[QString("queueName")].isNull() && m_queue_name_isValid;

    m_sas_uri_isValid = ::OpenAPI::fromJsonValue(m_sas_uri, json[QString("sasUri")]);
    m_sas_uri_isSet = !json[QString("sasUri")].isNull() && m_sas_uri_isValid;
}

QString OAIDataSubjectRightQueueInfo::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDataSubjectRightQueueInfo::asJsonObject() const {
    QJsonObject obj;
    if (m_expires_at_isSet) {
        obj.insert(QString("expiresAt"), ::OpenAPI::toJsonValue(m_expires_at));
    }
    if (m_queue_name_isSet) {
        obj.insert(QString("queueName"), ::OpenAPI::toJsonValue(m_queue_name));
    }
    if (m_sas_uri_isSet) {
        obj.insert(QString("sasUri"), ::OpenAPI::toJsonValue(m_sas_uri));
    }
    return obj;
}

QDateTime OAIDataSubjectRightQueueInfo::getExpiresAt() const {
    return m_expires_at;
}
void OAIDataSubjectRightQueueInfo::setExpiresAt(const QDateTime &expires_at) {
    m_expires_at = expires_at;
    m_expires_at_isSet = true;
}

bool OAIDataSubjectRightQueueInfo::is_expires_at_Set() const{
    return m_expires_at_isSet;
}

bool OAIDataSubjectRightQueueInfo::is_expires_at_Valid() const{
    return m_expires_at_isValid;
}

QString OAIDataSubjectRightQueueInfo::getQueueName() const {
    return m_queue_name;
}
void OAIDataSubjectRightQueueInfo::setQueueName(const QString &queue_name) {
    m_queue_name = queue_name;
    m_queue_name_isSet = true;
}

bool OAIDataSubjectRightQueueInfo::is_queue_name_Set() const{
    return m_queue_name_isSet;
}

bool OAIDataSubjectRightQueueInfo::is_queue_name_Valid() const{
    return m_queue_name_isValid;
}

QString OAIDataSubjectRightQueueInfo::getSasUri() const {
    return m_sas_uri;
}
void OAIDataSubjectRightQueueInfo::setSasUri(const QString &sas_uri) {
    m_sas_uri = sas_uri;
    m_sas_uri_isSet = true;
}

bool OAIDataSubjectRightQueueInfo::is_sas_uri_Set() const{
    return m_sas_uri_isSet;
}

bool OAIDataSubjectRightQueueInfo::is_sas_uri_Valid() const{
    return m_sas_uri_isValid;
}

bool OAIDataSubjectRightQueueInfo::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_expires_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_queue_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sas_uri_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDataSubjectRightQueueInfo::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_expires_at_isValid && m_queue_name_isValid && m_sas_uri_isValid && true;
}

} // namespace OpenAPI
