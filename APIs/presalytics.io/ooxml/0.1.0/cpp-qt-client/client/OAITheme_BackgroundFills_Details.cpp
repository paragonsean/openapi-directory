/**
 * OOXML Automation
 * This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.
 *
 * The version of the OpenAPI document: 0.1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITheme_BackgroundFills_Details.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITheme_BackgroundFills_Details::OAITheme_BackgroundFills_Details(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITheme_BackgroundFills_Details::OAITheme_BackgroundFills_Details() {
    this->initializeModel();
}

OAITheme_BackgroundFills_Details::~OAITheme_BackgroundFills_Details() {}

void OAITheme_BackgroundFills_Details::initializeModel() {

    m_date_created_isSet = false;
    m_date_created_isValid = false;

    m_date_modified_isSet = false;
    m_date_modified_isValid = false;

    m_fill_map_isSet = false;
    m_fill_map_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_intensity_id_isSet = false;
    m_intensity_id_isValid = false;

    m_theme_isSet = false;
    m_theme_isValid = false;

    m_theme_id_isSet = false;
    m_theme_id_isValid = false;

    m_user_created_isSet = false;
    m_user_created_isValid = false;

    m_user_modified_isSet = false;
    m_user_modified_isValid = false;
}

void OAITheme_BackgroundFills_Details::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITheme_BackgroundFills_Details::fromJsonObject(QJsonObject json) {

    m_date_created_isValid = ::OpenAPI::fromJsonValue(m_date_created, json[QString("dateCreated")]);
    m_date_created_isSet = !json[QString("dateCreated")].isNull() && m_date_created_isValid;

    m_date_modified_isValid = ::OpenAPI::fromJsonValue(m_date_modified, json[QString("dateModified")]);
    m_date_modified_isSet = !json[QString("dateModified")].isNull() && m_date_modified_isValid;

    m_fill_map_isValid = ::OpenAPI::fromJsonValue(m_fill_map, json[QString("fillMap")]);
    m_fill_map_isSet = !json[QString("fillMap")].isNull() && m_fill_map_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_intensity_id_isValid = ::OpenAPI::fromJsonValue(m_intensity_id, json[QString("intensityId")]);
    m_intensity_id_isSet = !json[QString("intensityId")].isNull() && m_intensity_id_isValid;

    m_theme_isValid = ::OpenAPI::fromJsonValue(m_theme, json[QString("theme")]);
    m_theme_isSet = !json[QString("theme")].isNull() && m_theme_isValid;

    m_theme_id_isValid = ::OpenAPI::fromJsonValue(m_theme_id, json[QString("themeId")]);
    m_theme_id_isSet = !json[QString("themeId")].isNull() && m_theme_id_isValid;

    m_user_created_isValid = ::OpenAPI::fromJsonValue(m_user_created, json[QString("userCreated")]);
    m_user_created_isSet = !json[QString("userCreated")].isNull() && m_user_created_isValid;

    m_user_modified_isValid = ::OpenAPI::fromJsonValue(m_user_modified, json[QString("userModified")]);
    m_user_modified_isSet = !json[QString("userModified")].isNull() && m_user_modified_isValid;
}

QString OAITheme_BackgroundFills_Details::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITheme_BackgroundFills_Details::asJsonObject() const {
    QJsonObject obj;
    if (m_date_created_isSet) {
        obj.insert(QString("dateCreated"), ::OpenAPI::toJsonValue(m_date_created));
    }
    if (m_date_modified_isSet) {
        obj.insert(QString("dateModified"), ::OpenAPI::toJsonValue(m_date_modified));
    }
    if (m_fill_map.isSet()) {
        obj.insert(QString("fillMap"), ::OpenAPI::toJsonValue(m_fill_map));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_intensity_id_isSet) {
        obj.insert(QString("intensityId"), ::OpenAPI::toJsonValue(m_intensity_id));
    }
    if (m_theme.isSet()) {
        obj.insert(QString("theme"), ::OpenAPI::toJsonValue(m_theme));
    }
    if (m_theme_id_isSet) {
        obj.insert(QString("themeId"), ::OpenAPI::toJsonValue(m_theme_id));
    }
    if (m_user_created_isSet) {
        obj.insert(QString("userCreated"), ::OpenAPI::toJsonValue(m_user_created));
    }
    if (m_user_modified_isSet) {
        obj.insert(QString("userModified"), ::OpenAPI::toJsonValue(m_user_modified));
    }
    return obj;
}

QDateTime OAITheme_BackgroundFills_Details::getDateCreated() const {
    return m_date_created;
}
void OAITheme_BackgroundFills_Details::setDateCreated(const QDateTime &date_created) {
    m_date_created = date_created;
    m_date_created_isSet = true;
}

bool OAITheme_BackgroundFills_Details::is_date_created_Set() const{
    return m_date_created_isSet;
}

bool OAITheme_BackgroundFills_Details::is_date_created_Valid() const{
    return m_date_created_isValid;
}

QDateTime OAITheme_BackgroundFills_Details::getDateModified() const {
    return m_date_modified;
}
void OAITheme_BackgroundFills_Details::setDateModified(const QDateTime &date_modified) {
    m_date_modified = date_modified;
    m_date_modified_isSet = true;
}

bool OAITheme_BackgroundFills_Details::is_date_modified_Set() const{
    return m_date_modified_isSet;
}

bool OAITheme_BackgroundFills_Details::is_date_modified_Valid() const{
    return m_date_modified_isValid;
}

OAIShared_FillMap_Details OAITheme_BackgroundFills_Details::getFillMap() const {
    return m_fill_map;
}
void OAITheme_BackgroundFills_Details::setFillMap(const OAIShared_FillMap_Details &fill_map) {
    m_fill_map = fill_map;
    m_fill_map_isSet = true;
}

bool OAITheme_BackgroundFills_Details::is_fill_map_Set() const{
    return m_fill_map_isSet;
}

bool OAITheme_BackgroundFills_Details::is_fill_map_Valid() const{
    return m_fill_map_isValid;
}

QString OAITheme_BackgroundFills_Details::getId() const {
    return m_id;
}
void OAITheme_BackgroundFills_Details::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAITheme_BackgroundFills_Details::is_id_Set() const{
    return m_id_isSet;
}

bool OAITheme_BackgroundFills_Details::is_id_Valid() const{
    return m_id_isValid;
}

qint32 OAITheme_BackgroundFills_Details::getIntensityId() const {
    return m_intensity_id;
}
void OAITheme_BackgroundFills_Details::setIntensityId(const qint32 &intensity_id) {
    m_intensity_id = intensity_id;
    m_intensity_id_isSet = true;
}

bool OAITheme_BackgroundFills_Details::is_intensity_id_Set() const{
    return m_intensity_id_isSet;
}

bool OAITheme_BackgroundFills_Details::is_intensity_id_Valid() const{
    return m_intensity_id_isValid;
}

OAITheme_Themes_Details OAITheme_BackgroundFills_Details::getTheme() const {
    return m_theme;
}
void OAITheme_BackgroundFills_Details::setTheme(const OAITheme_Themes_Details &theme) {
    m_theme = theme;
    m_theme_isSet = true;
}

bool OAITheme_BackgroundFills_Details::is_theme_Set() const{
    return m_theme_isSet;
}

bool OAITheme_BackgroundFills_Details::is_theme_Valid() const{
    return m_theme_isValid;
}

QString OAITheme_BackgroundFills_Details::getThemeId() const {
    return m_theme_id;
}
void OAITheme_BackgroundFills_Details::setThemeId(const QString &theme_id) {
    m_theme_id = theme_id;
    m_theme_id_isSet = true;
}

bool OAITheme_BackgroundFills_Details::is_theme_id_Set() const{
    return m_theme_id_isSet;
}

bool OAITheme_BackgroundFills_Details::is_theme_id_Valid() const{
    return m_theme_id_isValid;
}

QString OAITheme_BackgroundFills_Details::getUserCreated() const {
    return m_user_created;
}
void OAITheme_BackgroundFills_Details::setUserCreated(const QString &user_created) {
    m_user_created = user_created;
    m_user_created_isSet = true;
}

bool OAITheme_BackgroundFills_Details::is_user_created_Set() const{
    return m_user_created_isSet;
}

bool OAITheme_BackgroundFills_Details::is_user_created_Valid() const{
    return m_user_created_isValid;
}

QString OAITheme_BackgroundFills_Details::getUserModified() const {
    return m_user_modified;
}
void OAITheme_BackgroundFills_Details::setUserModified(const QString &user_modified) {
    m_user_modified = user_modified;
    m_user_modified_isSet = true;
}

bool OAITheme_BackgroundFills_Details::is_user_modified_Set() const{
    return m_user_modified_isSet;
}

bool OAITheme_BackgroundFills_Details::is_user_modified_Valid() const{
    return m_user_modified_isValid;
}

bool OAITheme_BackgroundFills_Details::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_date_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_modified_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fill_map.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_intensity_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_theme.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_theme_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_modified_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITheme_BackgroundFills_Details::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
