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

#include "OAIApps_update_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIApps_update_request::OAIApps_update_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIApps_update_request::OAIApps_update_request() {
    this->initializeModel();
}

OAIApps_update_request::~OAIApps_update_request() {}

void OAIApps_update_request::initializeModel() {

    m_description_isSet = false;
    m_description_isValid = false;

    m_display_name_isSet = false;
    m_display_name_isValid = false;

    m_icon_asset_id_isSet = false;
    m_icon_asset_id_isValid = false;

    m_icon_url_isSet = false;
    m_icon_url_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_release_type_isSet = false;
    m_release_type_isValid = false;
}

void OAIApps_update_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIApps_update_request::fromJsonObject(QJsonObject json) {

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_display_name_isValid = ::OpenAPI::fromJsonValue(m_display_name, json[QString("display_name")]);
    m_display_name_isSet = !json[QString("display_name")].isNull() && m_display_name_isValid;

    m_icon_asset_id_isValid = ::OpenAPI::fromJsonValue(m_icon_asset_id, json[QString("icon_asset_id")]);
    m_icon_asset_id_isSet = !json[QString("icon_asset_id")].isNull() && m_icon_asset_id_isValid;

    m_icon_url_isValid = ::OpenAPI::fromJsonValue(m_icon_url, json[QString("icon_url")]);
    m_icon_url_isSet = !json[QString("icon_url")].isNull() && m_icon_url_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_release_type_isValid = ::OpenAPI::fromJsonValue(m_release_type, json[QString("release_type")]);
    m_release_type_isSet = !json[QString("release_type")].isNull() && m_release_type_isValid;
}

QString OAIApps_update_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIApps_update_request::asJsonObject() const {
    QJsonObject obj;
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_display_name_isSet) {
        obj.insert(QString("display_name"), ::OpenAPI::toJsonValue(m_display_name));
    }
    if (m_icon_asset_id_isSet) {
        obj.insert(QString("icon_asset_id"), ::OpenAPI::toJsonValue(m_icon_asset_id));
    }
    if (m_icon_url_isSet) {
        obj.insert(QString("icon_url"), ::OpenAPI::toJsonValue(m_icon_url));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_release_type_isSet) {
        obj.insert(QString("release_type"), ::OpenAPI::toJsonValue(m_release_type));
    }
    return obj;
}

QString OAIApps_update_request::getDescription() const {
    return m_description;
}
void OAIApps_update_request::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIApps_update_request::is_description_Set() const{
    return m_description_isSet;
}

bool OAIApps_update_request::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIApps_update_request::getDisplayName() const {
    return m_display_name;
}
void OAIApps_update_request::setDisplayName(const QString &display_name) {
    m_display_name = display_name;
    m_display_name_isSet = true;
}

bool OAIApps_update_request::is_display_name_Set() const{
    return m_display_name_isSet;
}

bool OAIApps_update_request::is_display_name_Valid() const{
    return m_display_name_isValid;
}

QString OAIApps_update_request::getIconAssetId() const {
    return m_icon_asset_id;
}
void OAIApps_update_request::setIconAssetId(const QString &icon_asset_id) {
    m_icon_asset_id = icon_asset_id;
    m_icon_asset_id_isSet = true;
}

bool OAIApps_update_request::is_icon_asset_id_Set() const{
    return m_icon_asset_id_isSet;
}

bool OAIApps_update_request::is_icon_asset_id_Valid() const{
    return m_icon_asset_id_isValid;
}

QString OAIApps_update_request::getIconUrl() const {
    return m_icon_url;
}
void OAIApps_update_request::setIconUrl(const QString &icon_url) {
    m_icon_url = icon_url;
    m_icon_url_isSet = true;
}

bool OAIApps_update_request::is_icon_url_Set() const{
    return m_icon_url_isSet;
}

bool OAIApps_update_request::is_icon_url_Valid() const{
    return m_icon_url_isValid;
}

QString OAIApps_update_request::getName() const {
    return m_name;
}
void OAIApps_update_request::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIApps_update_request::is_name_Set() const{
    return m_name_isSet;
}

bool OAIApps_update_request::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIApps_update_request::getReleaseType() const {
    return m_release_type;
}
void OAIApps_update_request::setReleaseType(const QString &release_type) {
    m_release_type = release_type;
    m_release_type_isSet = true;
}

bool OAIApps_update_request::is_release_type_Set() const{
    return m_release_type_isSet;
}

bool OAIApps_update_request::is_release_type_Valid() const{
    return m_release_type_isValid;
}

bool OAIApps_update_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_display_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_icon_asset_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_icon_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_release_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIApps_update_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
