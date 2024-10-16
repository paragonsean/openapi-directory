/**
 * Bufferapp
 * Social media management for marketers and agencies
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAINewUpdate.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAINewUpdate::OAINewUpdate(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAINewUpdate::OAINewUpdate() {
    this->initializeModel();
}

OAINewUpdate::~OAINewUpdate() {}

void OAINewUpdate::initializeModel() {

    m_buffer_count_isSet = false;
    m_buffer_count_isValid = false;

    m_buffer_percentage_isSet = false;
    m_buffer_percentage_isValid = false;

    m_success_isSet = false;
    m_success_isValid = false;

    m_updates_isSet = false;
    m_updates_isValid = false;
}

void OAINewUpdate::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAINewUpdate::fromJsonObject(QJsonObject json) {

    m_buffer_count_isValid = ::OpenAPI::fromJsonValue(m_buffer_count, json[QString("buffer_count")]);
    m_buffer_count_isSet = !json[QString("buffer_count")].isNull() && m_buffer_count_isValid;

    m_buffer_percentage_isValid = ::OpenAPI::fromJsonValue(m_buffer_percentage, json[QString("buffer_percentage")]);
    m_buffer_percentage_isSet = !json[QString("buffer_percentage")].isNull() && m_buffer_percentage_isValid;

    m_success_isValid = ::OpenAPI::fromJsonValue(m_success, json[QString("success")]);
    m_success_isSet = !json[QString("success")].isNull() && m_success_isValid;

    m_updates_isValid = ::OpenAPI::fromJsonValue(m_updates, json[QString("updates")]);
    m_updates_isSet = !json[QString("updates")].isNull() && m_updates_isValid;
}

QString OAINewUpdate::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAINewUpdate::asJsonObject() const {
    QJsonObject obj;
    if (m_buffer_count_isSet) {
        obj.insert(QString("buffer_count"), ::OpenAPI::toJsonValue(m_buffer_count));
    }
    if (m_buffer_percentage_isSet) {
        obj.insert(QString("buffer_percentage"), ::OpenAPI::toJsonValue(m_buffer_percentage));
    }
    if (m_success_isSet) {
        obj.insert(QString("success"), ::OpenAPI::toJsonValue(m_success));
    }
    if (m_updates.size() > 0) {
        obj.insert(QString("updates"), ::OpenAPI::toJsonValue(m_updates));
    }
    return obj;
}

double OAINewUpdate::getBufferCount() const {
    return m_buffer_count;
}
void OAINewUpdate::setBufferCount(const double &buffer_count) {
    m_buffer_count = buffer_count;
    m_buffer_count_isSet = true;
}

bool OAINewUpdate::is_buffer_count_Set() const{
    return m_buffer_count_isSet;
}

bool OAINewUpdate::is_buffer_count_Valid() const{
    return m_buffer_count_isValid;
}

double OAINewUpdate::getBufferPercentage() const {
    return m_buffer_percentage;
}
void OAINewUpdate::setBufferPercentage(const double &buffer_percentage) {
    m_buffer_percentage = buffer_percentage;
    m_buffer_percentage_isSet = true;
}

bool OAINewUpdate::is_buffer_percentage_Set() const{
    return m_buffer_percentage_isSet;
}

bool OAINewUpdate::is_buffer_percentage_Valid() const{
    return m_buffer_percentage_isValid;
}

bool OAINewUpdate::isSuccess() const {
    return m_success;
}
void OAINewUpdate::setSuccess(const bool &success) {
    m_success = success;
    m_success_isSet = true;
}

bool OAINewUpdate::is_success_Set() const{
    return m_success_isSet;
}

bool OAINewUpdate::is_success_Valid() const{
    return m_success_isValid;
}

QList<OAINewUpdate_updates_inner> OAINewUpdate::getUpdates() const {
    return m_updates;
}
void OAINewUpdate::setUpdates(const QList<OAINewUpdate_updates_inner> &updates) {
    m_updates = updates;
    m_updates_isSet = true;
}

bool OAINewUpdate::is_updates_Set() const{
    return m_updates_isSet;
}

bool OAINewUpdate::is_updates_Valid() const{
    return m_updates_isValid;
}

bool OAINewUpdate::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_buffer_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_buffer_percentage_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_success_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updates.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAINewUpdate::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
