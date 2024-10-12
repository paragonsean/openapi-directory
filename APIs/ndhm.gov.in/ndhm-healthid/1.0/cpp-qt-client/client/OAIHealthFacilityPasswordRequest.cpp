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

#include "OAIHealthFacilityPasswordRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIHealthFacilityPasswordRequest::OAIHealthFacilityPasswordRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIHealthFacilityPasswordRequest::OAIHealthFacilityPasswordRequest() {
    this->initializeModel();
}

OAIHealthFacilityPasswordRequest::~OAIHealthFacilityPasswordRequest() {}

void OAIHealthFacilityPasswordRequest::initializeModel() {

    m_hfr_uid_isSet = false;
    m_hfr_uid_isValid = false;
}

void OAIHealthFacilityPasswordRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIHealthFacilityPasswordRequest::fromJsonObject(QJsonObject json) {

    m_hfr_uid_isValid = ::OpenAPI::fromJsonValue(m_hfr_uid, json[QString("hfrUid")]);
    m_hfr_uid_isSet = !json[QString("hfrUid")].isNull() && m_hfr_uid_isValid;
}

QString OAIHealthFacilityPasswordRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIHealthFacilityPasswordRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_hfr_uid_isSet) {
        obj.insert(QString("hfrUid"), ::OpenAPI::toJsonValue(m_hfr_uid));
    }
    return obj;
}

QString OAIHealthFacilityPasswordRequest::getHfrUid() const {
    return m_hfr_uid;
}
void OAIHealthFacilityPasswordRequest::setHfrUid(const QString &hfr_uid) {
    m_hfr_uid = hfr_uid;
    m_hfr_uid_isSet = true;
}

bool OAIHealthFacilityPasswordRequest::is_hfr_uid_Set() const{
    return m_hfr_uid_isSet;
}

bool OAIHealthFacilityPasswordRequest::is_hfr_uid_Valid() const{
    return m_hfr_uid_isValid;
}

bool OAIHealthFacilityPasswordRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_hfr_uid_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIHealthFacilityPasswordRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
