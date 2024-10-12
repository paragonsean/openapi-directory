/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAttributeUnassignGroup_200_response_result.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAttributeUnassignGroup_200_response_result::OAIAttributeUnassignGroup_200_response_result(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAttributeUnassignGroup_200_response_result::OAIAttributeUnassignGroup_200_response_result() {
    this->initializeModel();
}

OAIAttributeUnassignGroup_200_response_result::~OAIAttributeUnassignGroup_200_response_result() {}

void OAIAttributeUnassignGroup_200_response_result::initializeModel() {

    m_unassigned_isSet = false;
    m_unassigned_isValid = false;
}

void OAIAttributeUnassignGroup_200_response_result::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAttributeUnassignGroup_200_response_result::fromJsonObject(QJsonObject json) {

    m_unassigned_isValid = ::OpenAPI::fromJsonValue(m_unassigned, json[QString("unassigned")]);
    m_unassigned_isSet = !json[QString("unassigned")].isNull() && m_unassigned_isValid;
}

QString OAIAttributeUnassignGroup_200_response_result::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAttributeUnassignGroup_200_response_result::asJsonObject() const {
    QJsonObject obj;
    if (m_unassigned_isSet) {
        obj.insert(QString("unassigned"), ::OpenAPI::toJsonValue(m_unassigned));
    }
    return obj;
}

QString OAIAttributeUnassignGroup_200_response_result::getUnassigned() const {
    return m_unassigned;
}
void OAIAttributeUnassignGroup_200_response_result::setUnassigned(const QString &unassigned) {
    m_unassigned = unassigned;
    m_unassigned_isSet = true;
}

bool OAIAttributeUnassignGroup_200_response_result::is_unassigned_Set() const{
    return m_unassigned_isSet;
}

bool OAIAttributeUnassignGroup_200_response_result::is_unassigned_Valid() const{
    return m_unassigned_isValid;
}

bool OAIAttributeUnassignGroup_200_response_result::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_unassigned_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAttributeUnassignGroup_200_response_result::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
