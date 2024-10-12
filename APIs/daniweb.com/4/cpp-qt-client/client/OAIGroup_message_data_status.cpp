/**
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGroup_message_data_status.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGroup_message_data_status::OAIGroup_message_data_status(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGroup_message_data_status::OAIGroup_message_data_status() {
    this->initializeModel();
}

OAIGroup_message_data_status::~OAIGroup_message_data_status() {}

void OAIGroup_message_data_status::initializeModel() {

    m_last_updated_timestamp_isSet = false;
    m_last_updated_timestamp_isValid = false;
}

void OAIGroup_message_data_status::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGroup_message_data_status::fromJsonObject(QJsonObject json) {

    m_last_updated_timestamp_isValid = ::OpenAPI::fromJsonValue(m_last_updated_timestamp, json[QString("last_updated_timestamp")]);
    m_last_updated_timestamp_isSet = !json[QString("last_updated_timestamp")].isNull() && m_last_updated_timestamp_isValid;
}

QString OAIGroup_message_data_status::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGroup_message_data_status::asJsonObject() const {
    QJsonObject obj;
    if (m_last_updated_timestamp_isSet) {
        obj.insert(QString("last_updated_timestamp"), ::OpenAPI::toJsonValue(m_last_updated_timestamp));
    }
    return obj;
}

QDateTime OAIGroup_message_data_status::getLastUpdatedTimestamp() const {
    return m_last_updated_timestamp;
}
void OAIGroup_message_data_status::setLastUpdatedTimestamp(const QDateTime &last_updated_timestamp) {
    m_last_updated_timestamp = last_updated_timestamp;
    m_last_updated_timestamp_isSet = true;
}

bool OAIGroup_message_data_status::is_last_updated_timestamp_Set() const{
    return m_last_updated_timestamp_isSet;
}

bool OAIGroup_message_data_status::is_last_updated_timestamp_Valid() const{
    return m_last_updated_timestamp_isValid;
}

bool OAIGroup_message_data_status::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_last_updated_timestamp_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGroup_message_data_status::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
