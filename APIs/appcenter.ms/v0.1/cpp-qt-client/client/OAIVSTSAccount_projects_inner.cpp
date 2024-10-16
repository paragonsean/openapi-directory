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

#include "OAIVSTSAccount_projects_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVSTSAccount_projects_inner::OAIVSTSAccount_projects_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVSTSAccount_projects_inner::OAIVSTSAccount_projects_inner() {
    this->initializeModel();
}

OAIVSTSAccount_projects_inner::~OAIVSTSAccount_projects_inner() {}

void OAIVSTSAccount_projects_inner::initializeModel() {

    m_description_isSet = false;
    m_description_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;

    m_url_isSet = false;
    m_url_isValid = false;

    m_visibility_isSet = false;
    m_visibility_isValid = false;
}

void OAIVSTSAccount_projects_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVSTSAccount_projects_inner::fromJsonObject(QJsonObject json) {

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;

    m_url_isValid = ::OpenAPI::fromJsonValue(m_url, json[QString("url")]);
    m_url_isSet = !json[QString("url")].isNull() && m_url_isValid;

    m_visibility_isValid = ::OpenAPI::fromJsonValue(m_visibility, json[QString("visibility")]);
    m_visibility_isSet = !json[QString("visibility")].isNull() && m_visibility_isValid;
}

QString OAIVSTSAccount_projects_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVSTSAccount_projects_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_state_isSet) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    if (m_url_isSet) {
        obj.insert(QString("url"), ::OpenAPI::toJsonValue(m_url));
    }
    if (m_visibility_isSet) {
        obj.insert(QString("visibility"), ::OpenAPI::toJsonValue(m_visibility));
    }
    return obj;
}

QString OAIVSTSAccount_projects_inner::getDescription() const {
    return m_description;
}
void OAIVSTSAccount_projects_inner::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIVSTSAccount_projects_inner::is_description_Set() const{
    return m_description_isSet;
}

bool OAIVSTSAccount_projects_inner::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIVSTSAccount_projects_inner::getId() const {
    return m_id;
}
void OAIVSTSAccount_projects_inner::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIVSTSAccount_projects_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAIVSTSAccount_projects_inner::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIVSTSAccount_projects_inner::getName() const {
    return m_name;
}
void OAIVSTSAccount_projects_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIVSTSAccount_projects_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIVSTSAccount_projects_inner::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIVSTSAccount_projects_inner::getState() const {
    return m_state;
}
void OAIVSTSAccount_projects_inner::setState(const QString &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIVSTSAccount_projects_inner::is_state_Set() const{
    return m_state_isSet;
}

bool OAIVSTSAccount_projects_inner::is_state_Valid() const{
    return m_state_isValid;
}

QString OAIVSTSAccount_projects_inner::getUrl() const {
    return m_url;
}
void OAIVSTSAccount_projects_inner::setUrl(const QString &url) {
    m_url = url;
    m_url_isSet = true;
}

bool OAIVSTSAccount_projects_inner::is_url_Set() const{
    return m_url_isSet;
}

bool OAIVSTSAccount_projects_inner::is_url_Valid() const{
    return m_url_isValid;
}

QString OAIVSTSAccount_projects_inner::getVisibility() const {
    return m_visibility;
}
void OAIVSTSAccount_projects_inner::setVisibility(const QString &visibility) {
    m_visibility = visibility;
    m_visibility_isSet = true;
}

bool OAIVSTSAccount_projects_inner::is_visibility_Set() const{
    return m_visibility_isSet;
}

bool OAIVSTSAccount_projects_inner::is_visibility_Valid() const{
    return m_visibility_isValid;
}

bool OAIVSTSAccount_projects_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_visibility_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVSTSAccount_projects_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
