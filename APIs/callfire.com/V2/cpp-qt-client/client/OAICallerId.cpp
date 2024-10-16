/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICallerId.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICallerId::OAICallerId(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICallerId::OAICallerId() {
    this->initializeModel();
}

OAICallerId::~OAICallerId() {}

void OAICallerId::initializeModel() {

    m_phone_number_isSet = false;
    m_phone_number_isValid = false;
}

void OAICallerId::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICallerId::fromJsonObject(QJsonObject json) {

    m_phone_number_isValid = ::OpenAPI::fromJsonValue(m_phone_number, json[QString("phoneNumber")]);
    m_phone_number_isSet = !json[QString("phoneNumber")].isNull() && m_phone_number_isValid;
}

QString OAICallerId::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICallerId::asJsonObject() const {
    QJsonObject obj;
    if (m_phone_number_isSet) {
        obj.insert(QString("phoneNumber"), ::OpenAPI::toJsonValue(m_phone_number));
    }
    return obj;
}

QString OAICallerId::getPhoneNumber() const {
    return m_phone_number;
}
void OAICallerId::setPhoneNumber(const QString &phone_number) {
    m_phone_number = phone_number;
    m_phone_number_isSet = true;
}

bool OAICallerId::is_phone_number_Set() const{
    return m_phone_number_isSet;
}

bool OAICallerId::is_phone_number_Valid() const{
    return m_phone_number_isValid;
}

bool OAICallerId::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_phone_number_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICallerId::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
