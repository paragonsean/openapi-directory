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

#include "OAIOrganizationRepresentation.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOrganizationRepresentation::OAIOrganizationRepresentation(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOrganizationRepresentation::OAIOrganizationRepresentation() {
    this->initializeModel();
}

OAIOrganizationRepresentation::~OAIOrganizationRepresentation() {}

void OAIOrganizationRepresentation::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;
}

void OAIOrganizationRepresentation::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOrganizationRepresentation::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;
}

QString OAIOrganizationRepresentation::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOrganizationRepresentation::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    return obj;
}

QString OAIOrganizationRepresentation::getId() const {
    return m_id;
}
void OAIOrganizationRepresentation::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIOrganizationRepresentation::is_id_Set() const{
    return m_id_isSet;
}

bool OAIOrganizationRepresentation::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIOrganizationRepresentation::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOrganizationRepresentation::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && true;
}

} // namespace OpenAPI
