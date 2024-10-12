/**
 * RecoveryServicesBackupClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-07-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDpmJobExtendedInfo.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDpmJobExtendedInfo::OAIDpmJobExtendedInfo(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDpmJobExtendedInfo::OAIDpmJobExtendedInfo() {
    this->initializeModel();
}

OAIDpmJobExtendedInfo::~OAIDpmJobExtendedInfo() {}

void OAIDpmJobExtendedInfo::initializeModel() {

    m_dynamic_error_message_isSet = false;
    m_dynamic_error_message_isValid = false;

    m_property_bag_isSet = false;
    m_property_bag_isValid = false;

    m_tasks_list_isSet = false;
    m_tasks_list_isValid = false;
}

void OAIDpmJobExtendedInfo::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDpmJobExtendedInfo::fromJsonObject(QJsonObject json) {

    m_dynamic_error_message_isValid = ::OpenAPI::fromJsonValue(m_dynamic_error_message, json[QString("dynamicErrorMessage")]);
    m_dynamic_error_message_isSet = !json[QString("dynamicErrorMessage")].isNull() && m_dynamic_error_message_isValid;

    m_property_bag_isValid = ::OpenAPI::fromJsonValue(m_property_bag, json[QString("propertyBag")]);
    m_property_bag_isSet = !json[QString("propertyBag")].isNull() && m_property_bag_isValid;

    m_tasks_list_isValid = ::OpenAPI::fromJsonValue(m_tasks_list, json[QString("tasksList")]);
    m_tasks_list_isSet = !json[QString("tasksList")].isNull() && m_tasks_list_isValid;
}

QString OAIDpmJobExtendedInfo::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDpmJobExtendedInfo::asJsonObject() const {
    QJsonObject obj;
    if (m_dynamic_error_message_isSet) {
        obj.insert(QString("dynamicErrorMessage"), ::OpenAPI::toJsonValue(m_dynamic_error_message));
    }
    if (m_property_bag.size() > 0) {
        obj.insert(QString("propertyBag"), ::OpenAPI::toJsonValue(m_property_bag));
    }
    if (m_tasks_list.size() > 0) {
        obj.insert(QString("tasksList"), ::OpenAPI::toJsonValue(m_tasks_list));
    }
    return obj;
}

QString OAIDpmJobExtendedInfo::getDynamicErrorMessage() const {
    return m_dynamic_error_message;
}
void OAIDpmJobExtendedInfo::setDynamicErrorMessage(const QString &dynamic_error_message) {
    m_dynamic_error_message = dynamic_error_message;
    m_dynamic_error_message_isSet = true;
}

bool OAIDpmJobExtendedInfo::is_dynamic_error_message_Set() const{
    return m_dynamic_error_message_isSet;
}

bool OAIDpmJobExtendedInfo::is_dynamic_error_message_Valid() const{
    return m_dynamic_error_message_isValid;
}

QMap<QString, QString> OAIDpmJobExtendedInfo::getPropertyBag() const {
    return m_property_bag;
}
void OAIDpmJobExtendedInfo::setPropertyBag(const QMap<QString, QString> &property_bag) {
    m_property_bag = property_bag;
    m_property_bag_isSet = true;
}

bool OAIDpmJobExtendedInfo::is_property_bag_Set() const{
    return m_property_bag_isSet;
}

bool OAIDpmJobExtendedInfo::is_property_bag_Valid() const{
    return m_property_bag_isValid;
}

QList<OAIDpmJobTaskDetails> OAIDpmJobExtendedInfo::getTasksList() const {
    return m_tasks_list;
}
void OAIDpmJobExtendedInfo::setTasksList(const QList<OAIDpmJobTaskDetails> &tasks_list) {
    m_tasks_list = tasks_list;
    m_tasks_list_isSet = true;
}

bool OAIDpmJobExtendedInfo::is_tasks_list_Set() const{
    return m_tasks_list_isSet;
}

bool OAIDpmJobExtendedInfo::is_tasks_list_Valid() const{
    return m_tasks_list_isValid;
}

bool OAIDpmJobExtendedInfo::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_dynamic_error_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_property_bag.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_tasks_list.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDpmJobExtendedInfo::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
