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

#include "OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties::OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties::OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties() {
    this->initializeModel();
}

OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties::~OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties() {}

void OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties::initializeModel() {

    m_email_isSet = false;
    m_email_isValid = false;
}

void OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties::fromJsonObject(QJsonObject json) {

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;
}

QString OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties::asJsonObject() const {
    QJsonObject obj;
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    return obj;
}

QString OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties::getEmail() const {
    return m_email;
}
void OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties::is_email_Set() const{
    return m_email_isSet;
}

bool OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties::is_email_Valid() const{
    return m_email_isValid;
}

bool OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
