/**
 * Health Repository Provider Specifications for HIP
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIP. The specs are essentially duplicates from the Gateway and Health Repository, but put together so as to make it clear to *HIPs* which set of APIs they should implement to participate in the network.  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIHealthInformationNotification_notification_notifier.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIHealthInformationNotification_notification_notifier::OAIHealthInformationNotification_notification_notifier(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIHealthInformationNotification_notification_notifier::OAIHealthInformationNotification_notification_notifier() {
    this->initializeModel();
}

OAIHealthInformationNotification_notification_notifier::~OAIHealthInformationNotification_notification_notifier() {}

void OAIHealthInformationNotification_notification_notifier::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIHealthInformationNotification_notification_notifier::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIHealthInformationNotification_notification_notifier::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIHealthInformationNotification_notification_notifier::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIHealthInformationNotification_notification_notifier::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIHealthInformationNotification_notification_notifier::getId() const {
    return m_id;
}
void OAIHealthInformationNotification_notification_notifier::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIHealthInformationNotification_notification_notifier::is_id_Set() const{
    return m_id_isSet;
}

bool OAIHealthInformationNotification_notification_notifier::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIHealthInformationNotification_notification_notifier::getType() const {
    return m_type;
}
void OAIHealthInformationNotification_notification_notifier::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIHealthInformationNotification_notification_notifier::is_type_Set() const{
    return m_type_isSet;
}

bool OAIHealthInformationNotification_notification_notifier::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIHealthInformationNotification_notification_notifier::isSet() const {
    bool isObjectUpdated = false;
    do {
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

bool OAIHealthInformationNotification_notification_notifier::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
