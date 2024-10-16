/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISystemVersionNameGroup.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISystemVersionNameGroup::OAISystemVersionNameGroup(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISystemVersionNameGroup::OAISystemVersionNameGroup() {
    this->initializeModel();
}

OAISystemVersionNameGroup::~OAISystemVersionNameGroup() {}

void OAISystemVersionNameGroup::initializeModel() {

    m_name_isSet = false;
    m_name_isValid = false;

    m_versions_isSet = false;
    m_versions_isValid = false;
}

void OAISystemVersionNameGroup::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISystemVersionNameGroup::fromJsonObject(QJsonObject json) {

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_versions_isValid = ::OpenAPI::fromJsonValue(m_versions, json[QString("versions")]);
    m_versions_isSet = !json[QString("versions")].isNull() && m_versions_isValid;
}

QString OAISystemVersionNameGroup::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISystemVersionNameGroup::asJsonObject() const {
    QJsonObject obj;
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_versions.size() > 0) {
        obj.insert(QString("versions"), ::OpenAPI::toJsonValue(m_versions));
    }
    return obj;
}

QString OAISystemVersionNameGroup::getName() const {
    return m_name;
}
void OAISystemVersionNameGroup::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAISystemVersionNameGroup::is_name_Set() const{
    return m_name_isSet;
}

bool OAISystemVersionNameGroup::is_name_Valid() const{
    return m_name_isValid;
}

QList<QString> OAISystemVersionNameGroup::getVersions() const {
    return m_versions;
}
void OAISystemVersionNameGroup::setVersions(const QList<QString> &versions) {
    m_versions = versions;
    m_versions_isSet = true;
}

bool OAISystemVersionNameGroup::is_versions_Set() const{
    return m_versions_isSet;
}

bool OAISystemVersionNameGroup::is_versions_Valid() const{
    return m_versions_isValid;
}

bool OAISystemVersionNameGroup::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_versions.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISystemVersionNameGroup::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
