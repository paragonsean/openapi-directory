/**
 * HDInsightManagementClient
 * The HDInsight Management Client.
 *
 * The version of the OpenAPI document: 2015-03-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIApplicationProperties_computeProfile.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIApplicationProperties_computeProfile::OAIApplicationProperties_computeProfile(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIApplicationProperties_computeProfile::OAIApplicationProperties_computeProfile() {
    this->initializeModel();
}

OAIApplicationProperties_computeProfile::~OAIApplicationProperties_computeProfile() {}

void OAIApplicationProperties_computeProfile::initializeModel() {

    m_roles_isSet = false;
    m_roles_isValid = false;
}

void OAIApplicationProperties_computeProfile::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIApplicationProperties_computeProfile::fromJsonObject(QJsonObject json) {

    m_roles_isValid = ::OpenAPI::fromJsonValue(m_roles, json[QString("roles")]);
    m_roles_isSet = !json[QString("roles")].isNull() && m_roles_isValid;
}

QString OAIApplicationProperties_computeProfile::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIApplicationProperties_computeProfile::asJsonObject() const {
    QJsonObject obj;
    if (m_roles.size() > 0) {
        obj.insert(QString("roles"), ::OpenAPI::toJsonValue(m_roles));
    }
    return obj;
}

QList<OAIApplicationProperties_computeProfile_roles_inner> OAIApplicationProperties_computeProfile::getRoles() const {
    return m_roles;
}
void OAIApplicationProperties_computeProfile::setRoles(const QList<OAIApplicationProperties_computeProfile_roles_inner> &roles) {
    m_roles = roles;
    m_roles_isSet = true;
}

bool OAIApplicationProperties_computeProfile::is_roles_Set() const{
    return m_roles_isSet;
}

bool OAIApplicationProperties_computeProfile::is_roles_Valid() const{
    return m_roles_isValid;
}

bool OAIApplicationProperties_computeProfile::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_roles.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIApplicationProperties_computeProfile::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
