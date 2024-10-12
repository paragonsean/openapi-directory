/**
 * Health ID Service
 * It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent.  In order to issue a Health ID to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISearchByHealthIdRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISearchByHealthIdRequest::OAISearchByHealthIdRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISearchByHealthIdRequest::OAISearchByHealthIdRequest() {
    this->initializeModel();
}

OAISearchByHealthIdRequest::~OAISearchByHealthIdRequest() {}

void OAISearchByHealthIdRequest::initializeModel() {

    m_health_id_isSet = false;
    m_health_id_isValid = false;
}

void OAISearchByHealthIdRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISearchByHealthIdRequest::fromJsonObject(QJsonObject json) {

    m_health_id_isValid = ::OpenAPI::fromJsonValue(m_health_id, json[QString("healthId")]);
    m_health_id_isSet = !json[QString("healthId")].isNull() && m_health_id_isValid;
}

QString OAISearchByHealthIdRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISearchByHealthIdRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_health_id_isSet) {
        obj.insert(QString("healthId"), ::OpenAPI::toJsonValue(m_health_id));
    }
    return obj;
}

QString OAISearchByHealthIdRequest::getHealthId() const {
    return m_health_id;
}
void OAISearchByHealthIdRequest::setHealthId(const QString &health_id) {
    m_health_id = health_id;
    m_health_id_isSet = true;
}

bool OAISearchByHealthIdRequest::is_health_id_Set() const{
    return m_health_id_isSet;
}

bool OAISearchByHealthIdRequest::is_health_id_Valid() const{
    return m_health_id_isValid;
}

bool OAISearchByHealthIdRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_health_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISearchByHealthIdRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
