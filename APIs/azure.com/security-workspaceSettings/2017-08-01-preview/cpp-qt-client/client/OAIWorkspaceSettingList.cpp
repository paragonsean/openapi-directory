/**
 * Security Center
 * API spec for Microsoft.Security (Azure Security Center) resource provider
 *
 * The version of the OpenAPI document: 2017-08-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIWorkspaceSettingList.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIWorkspaceSettingList::OAIWorkspaceSettingList(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIWorkspaceSettingList::OAIWorkspaceSettingList() {
    this->initializeModel();
}

OAIWorkspaceSettingList::~OAIWorkspaceSettingList() {}

void OAIWorkspaceSettingList::initializeModel() {

    m_next_link_isSet = false;
    m_next_link_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIWorkspaceSettingList::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIWorkspaceSettingList::fromJsonObject(QJsonObject json) {

    m_next_link_isValid = ::OpenAPI::fromJsonValue(m_next_link, json[QString("nextLink")]);
    m_next_link_isSet = !json[QString("nextLink")].isNull() && m_next_link_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIWorkspaceSettingList::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIWorkspaceSettingList::asJsonObject() const {
    QJsonObject obj;
    if (m_next_link_isSet) {
        obj.insert(QString("nextLink"), ::OpenAPI::toJsonValue(m_next_link));
    }
    if (m_value.size() > 0) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIWorkspaceSettingList::getNextLink() const {
    return m_next_link;
}
void OAIWorkspaceSettingList::setNextLink(const QString &next_link) {
    m_next_link = next_link;
    m_next_link_isSet = true;
}

bool OAIWorkspaceSettingList::is_next_link_Set() const{
    return m_next_link_isSet;
}

bool OAIWorkspaceSettingList::is_next_link_Valid() const{
    return m_next_link_isValid;
}

QList<OAIWorkspaceSetting> OAIWorkspaceSettingList::getValue() const {
    return m_value;
}
void OAIWorkspaceSettingList::setValue(const QList<OAIWorkspaceSetting> &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIWorkspaceSettingList::is_value_Set() const{
    return m_value_isSet;
}

bool OAIWorkspaceSettingList::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIWorkspaceSettingList::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_next_link_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIWorkspaceSettingList::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid && true;
}

} // namespace OpenAPI
