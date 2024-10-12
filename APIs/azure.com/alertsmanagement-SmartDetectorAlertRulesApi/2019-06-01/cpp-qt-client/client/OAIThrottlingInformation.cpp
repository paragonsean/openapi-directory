/**
 * Azure Alerts Management Service Resource Provider
 * APIs for Azure Smart Detector Alert Rules CRUD operations.
 *
 * The version of the OpenAPI document: 2019-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIThrottlingInformation.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIThrottlingInformation::OAIThrottlingInformation(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIThrottlingInformation::OAIThrottlingInformation() {
    this->initializeModel();
}

OAIThrottlingInformation::~OAIThrottlingInformation() {}

void OAIThrottlingInformation::initializeModel() {

    m_duration_isSet = false;
    m_duration_isValid = false;
}

void OAIThrottlingInformation::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIThrottlingInformation::fromJsonObject(QJsonObject json) {

    m_duration_isValid = ::OpenAPI::fromJsonValue(m_duration, json[QString("duration")]);
    m_duration_isSet = !json[QString("duration")].isNull() && m_duration_isValid;
}

QString OAIThrottlingInformation::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIThrottlingInformation::asJsonObject() const {
    QJsonObject obj;
    if (m_duration_isSet) {
        obj.insert(QString("duration"), ::OpenAPI::toJsonValue(m_duration));
    }
    return obj;
}

QString OAIThrottlingInformation::getDuration() const {
    return m_duration;
}
void OAIThrottlingInformation::setDuration(const QString &duration) {
    m_duration = duration;
    m_duration_isSet = true;
}

bool OAIThrottlingInformation::is_duration_Set() const{
    return m_duration_isSet;
}

bool OAIThrottlingInformation::is_duration_Valid() const{
    return m_duration_isValid;
}

bool OAIThrottlingInformation::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_duration_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIThrottlingInformation::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
