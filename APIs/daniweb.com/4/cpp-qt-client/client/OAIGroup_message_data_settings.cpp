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

#include "OAIGroup_message_data_settings.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGroup_message_data_settings::OAIGroup_message_data_settings(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGroup_message_data_settings::OAIGroup_message_data_settings() {
    this->initializeModel();
}

OAIGroup_message_data_settings::~OAIGroup_message_data_settings() {}

void OAIGroup_message_data_settings::initializeModel() {

    m_privacy_isSet = false;
    m_privacy_isValid = false;
}

void OAIGroup_message_data_settings::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGroup_message_data_settings::fromJsonObject(QJsonObject json) {

    m_privacy_isValid = ::OpenAPI::fromJsonValue(m_privacy, json[QString("privacy")]);
    m_privacy_isSet = !json[QString("privacy")].isNull() && m_privacy_isValid;
}

QString OAIGroup_message_data_settings::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGroup_message_data_settings::asJsonObject() const {
    QJsonObject obj;
    if (m_privacy_isSet) {
        obj.insert(QString("privacy"), ::OpenAPI::toJsonValue(m_privacy));
    }
    return obj;
}

QString OAIGroup_message_data_settings::getPrivacy() const {
    return m_privacy;
}
void OAIGroup_message_data_settings::setPrivacy(const QString &privacy) {
    m_privacy = privacy;
    m_privacy_isSet = true;
}

bool OAIGroup_message_data_settings::is_privacy_Set() const{
    return m_privacy_isSet;
}

bool OAIGroup_message_data_settings::is_privacy_Valid() const{
    return m_privacy_isValid;
}

bool OAIGroup_message_data_settings::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_privacy_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGroup_message_data_settings::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
