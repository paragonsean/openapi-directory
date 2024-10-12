/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on who is going to receive notifications associated with your Azure API Management deployment.
 *
 * The version of the OpenAPI document: 2019-01-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAINotificationRecipientUser_ListByNotification_200_response_value_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAINotificationRecipientUser_ListByNotification_200_response_value_inner::OAINotificationRecipientUser_ListByNotification_200_response_value_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAINotificationRecipientUser_ListByNotification_200_response_value_inner::OAINotificationRecipientUser_ListByNotification_200_response_value_inner() {
    this->initializeModel();
}

OAINotificationRecipientUser_ListByNotification_200_response_value_inner::~OAINotificationRecipientUser_ListByNotification_200_response_value_inner() {}

void OAINotificationRecipientUser_ListByNotification_200_response_value_inner::initializeModel() {

    m_properties_isSet = false;
    m_properties_isValid = false;
}

void OAINotificationRecipientUser_ListByNotification_200_response_value_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAINotificationRecipientUser_ListByNotification_200_response_value_inner::fromJsonObject(QJsonObject json) {

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;
}

QString OAINotificationRecipientUser_ListByNotification_200_response_value_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAINotificationRecipientUser_ListByNotification_200_response_value_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_properties.isSet()) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    return obj;
}

OAINotificationRecipientUser_ListByNotification_200_response_value_inner_properties OAINotificationRecipientUser_ListByNotification_200_response_value_inner::getProperties() const {
    return m_properties;
}
void OAINotificationRecipientUser_ListByNotification_200_response_value_inner::setProperties(const OAINotificationRecipientUser_ListByNotification_200_response_value_inner_properties &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAINotificationRecipientUser_ListByNotification_200_response_value_inner::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAINotificationRecipientUser_ListByNotification_200_response_value_inner::is_properties_Valid() const{
    return m_properties_isValid;
}

bool OAINotificationRecipientUser_ListByNotification_200_response_value_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_properties.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAINotificationRecipientUser_ListByNotification_200_response_value_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
