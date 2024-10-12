/**
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPatientCareContextLinkResponse_acknowledgement.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPatientCareContextLinkResponse_acknowledgement::OAIPatientCareContextLinkResponse_acknowledgement(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPatientCareContextLinkResponse_acknowledgement::OAIPatientCareContextLinkResponse_acknowledgement() {
    this->initializeModel();
}

OAIPatientCareContextLinkResponse_acknowledgement::~OAIPatientCareContextLinkResponse_acknowledgement() {}

void OAIPatientCareContextLinkResponse_acknowledgement::initializeModel() {

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAIPatientCareContextLinkResponse_acknowledgement::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPatientCareContextLinkResponse_acknowledgement::fromJsonObject(QJsonObject json) {

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;
}

QString OAIPatientCareContextLinkResponse_acknowledgement::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPatientCareContextLinkResponse_acknowledgement::asJsonObject() const {
    QJsonObject obj;
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

QString OAIPatientCareContextLinkResponse_acknowledgement::getStatus() const {
    return m_status;
}
void OAIPatientCareContextLinkResponse_acknowledgement::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIPatientCareContextLinkResponse_acknowledgement::is_status_Set() const{
    return m_status_isSet;
}

bool OAIPatientCareContextLinkResponse_acknowledgement::is_status_Valid() const{
    return m_status_isValid;
}

bool OAIPatientCareContextLinkResponse_acknowledgement::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPatientCareContextLinkResponse_acknowledgement::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_status_isValid && true;
}

} // namespace OpenAPI
