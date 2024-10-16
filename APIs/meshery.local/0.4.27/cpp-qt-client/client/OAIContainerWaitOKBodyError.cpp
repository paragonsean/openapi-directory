/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIContainerWaitOKBodyError.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIContainerWaitOKBodyError::OAIContainerWaitOKBodyError(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIContainerWaitOKBodyError::OAIContainerWaitOKBodyError() {
    this->initializeModel();
}

OAIContainerWaitOKBodyError::~OAIContainerWaitOKBodyError() {}

void OAIContainerWaitOKBodyError::initializeModel() {

    m_message_isSet = false;
    m_message_isValid = false;
}

void OAIContainerWaitOKBodyError::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIContainerWaitOKBodyError::fromJsonObject(QJsonObject json) {

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("Message")]);
    m_message_isSet = !json[QString("Message")].isNull() && m_message_isValid;
}

QString OAIContainerWaitOKBodyError::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIContainerWaitOKBodyError::asJsonObject() const {
    QJsonObject obj;
    if (m_message_isSet) {
        obj.insert(QString("Message"), ::OpenAPI::toJsonValue(m_message));
    }
    return obj;
}

QString OAIContainerWaitOKBodyError::getMessage() const {
    return m_message;
}
void OAIContainerWaitOKBodyError::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAIContainerWaitOKBodyError::is_message_Set() const{
    return m_message_isSet;
}

bool OAIContainerWaitOKBodyError::is_message_Valid() const{
    return m_message_isValid;
}

bool OAIContainerWaitOKBodyError::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_message_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIContainerWaitOKBodyError::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
