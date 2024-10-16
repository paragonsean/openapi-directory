/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAILink.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILink::OAILink(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILink::OAILink() {
    this->initializeModel();
}

OAILink::~OAILink() {}

void OAILink::initializeModel() {

    m_as_dropdown_isSet = false;
    m_as_dropdown_isValid = false;

    m_dash_uri_isSet = false;
    m_dash_uri_isValid = false;

    m_dashboard_isSet = false;
    m_dashboard_isValid = false;

    m_icon_isSet = false;
    m_icon_isValid = false;

    m_include_vars_isSet = false;
    m_include_vars_isValid = false;

    m_keep_time_isSet = false;
    m_keep_time_isValid = false;

    m_params_isSet = false;
    m_params_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;

    m_target_blank_isSet = false;
    m_target_blank_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_tooltip_isSet = false;
    m_tooltip_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_url_isSet = false;
    m_url_isValid = false;
}

void OAILink::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILink::fromJsonObject(QJsonObject json) {

    m_as_dropdown_isValid = ::OpenAPI::fromJsonValue(m_as_dropdown, json[QString("asDropdown")]);
    m_as_dropdown_isSet = !json[QString("asDropdown")].isNull() && m_as_dropdown_isValid;

    m_dash_uri_isValid = ::OpenAPI::fromJsonValue(m_dash_uri, json[QString("dashUri")]);
    m_dash_uri_isSet = !json[QString("dashUri")].isNull() && m_dash_uri_isValid;

    m_dashboard_isValid = ::OpenAPI::fromJsonValue(m_dashboard, json[QString("dashboard")]);
    m_dashboard_isSet = !json[QString("dashboard")].isNull() && m_dashboard_isValid;

    m_icon_isValid = ::OpenAPI::fromJsonValue(m_icon, json[QString("icon")]);
    m_icon_isSet = !json[QString("icon")].isNull() && m_icon_isValid;

    m_include_vars_isValid = ::OpenAPI::fromJsonValue(m_include_vars, json[QString("includeVars")]);
    m_include_vars_isSet = !json[QString("includeVars")].isNull() && m_include_vars_isValid;

    m_keep_time_isValid = ::OpenAPI::fromJsonValue(m_keep_time, json[QString("keepTime")]);
    m_keep_time_isSet = !json[QString("keepTime")].isNull() && m_keep_time_isValid;

    m_params_isValid = ::OpenAPI::fromJsonValue(m_params, json[QString("params")]);
    m_params_isSet = !json[QString("params")].isNull() && m_params_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;

    m_target_blank_isValid = ::OpenAPI::fromJsonValue(m_target_blank, json[QString("targetBlank")]);
    m_target_blank_isSet = !json[QString("targetBlank")].isNull() && m_target_blank_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_tooltip_isValid = ::OpenAPI::fromJsonValue(m_tooltip, json[QString("tooltip")]);
    m_tooltip_isSet = !json[QString("tooltip")].isNull() && m_tooltip_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_url_isValid = ::OpenAPI::fromJsonValue(m_url, json[QString("url")]);
    m_url_isSet = !json[QString("url")].isNull() && m_url_isValid;
}

QString OAILink::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILink::asJsonObject() const {
    QJsonObject obj;
    if (m_as_dropdown_isSet) {
        obj.insert(QString("asDropdown"), ::OpenAPI::toJsonValue(m_as_dropdown));
    }
    if (m_dash_uri_isSet) {
        obj.insert(QString("dashUri"), ::OpenAPI::toJsonValue(m_dash_uri));
    }
    if (m_dashboard_isSet) {
        obj.insert(QString("dashboard"), ::OpenAPI::toJsonValue(m_dashboard));
    }
    if (m_icon_isSet) {
        obj.insert(QString("icon"), ::OpenAPI::toJsonValue(m_icon));
    }
    if (m_include_vars_isSet) {
        obj.insert(QString("includeVars"), ::OpenAPI::toJsonValue(m_include_vars));
    }
    if (m_keep_time_isSet) {
        obj.insert(QString("keepTime"), ::OpenAPI::toJsonValue(m_keep_time));
    }
    if (m_params_isSet) {
        obj.insert(QString("params"), ::OpenAPI::toJsonValue(m_params));
    }
    if (m_tags.size() > 0) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    if (m_target_blank_isSet) {
        obj.insert(QString("targetBlank"), ::OpenAPI::toJsonValue(m_target_blank));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    if (m_tooltip_isSet) {
        obj.insert(QString("tooltip"), ::OpenAPI::toJsonValue(m_tooltip));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_url_isSet) {
        obj.insert(QString("url"), ::OpenAPI::toJsonValue(m_url));
    }
    return obj;
}

bool OAILink::isAsDropdown() const {
    return m_as_dropdown;
}
void OAILink::setAsDropdown(const bool &as_dropdown) {
    m_as_dropdown = as_dropdown;
    m_as_dropdown_isSet = true;
}

bool OAILink::is_as_dropdown_Set() const{
    return m_as_dropdown_isSet;
}

bool OAILink::is_as_dropdown_Valid() const{
    return m_as_dropdown_isValid;
}

QString OAILink::getDashUri() const {
    return m_dash_uri;
}
void OAILink::setDashUri(const QString &dash_uri) {
    m_dash_uri = dash_uri;
    m_dash_uri_isSet = true;
}

bool OAILink::is_dash_uri_Set() const{
    return m_dash_uri_isSet;
}

bool OAILink::is_dash_uri_Valid() const{
    return m_dash_uri_isValid;
}

QString OAILink::getDashboard() const {
    return m_dashboard;
}
void OAILink::setDashboard(const QString &dashboard) {
    m_dashboard = dashboard;
    m_dashboard_isSet = true;
}

bool OAILink::is_dashboard_Set() const{
    return m_dashboard_isSet;
}

bool OAILink::is_dashboard_Valid() const{
    return m_dashboard_isValid;
}

QString OAILink::getIcon() const {
    return m_icon;
}
void OAILink::setIcon(const QString &icon) {
    m_icon = icon;
    m_icon_isSet = true;
}

bool OAILink::is_icon_Set() const{
    return m_icon_isSet;
}

bool OAILink::is_icon_Valid() const{
    return m_icon_isValid;
}

bool OAILink::isIncludeVars() const {
    return m_include_vars;
}
void OAILink::setIncludeVars(const bool &include_vars) {
    m_include_vars = include_vars;
    m_include_vars_isSet = true;
}

bool OAILink::is_include_vars_Set() const{
    return m_include_vars_isSet;
}

bool OAILink::is_include_vars_Valid() const{
    return m_include_vars_isValid;
}

bool OAILink::isKeepTime() const {
    return m_keep_time;
}
void OAILink::setKeepTime(const bool &keep_time) {
    m_keep_time = keep_time;
    m_keep_time_isSet = true;
}

bool OAILink::is_keep_time_Set() const{
    return m_keep_time_isSet;
}

bool OAILink::is_keep_time_Valid() const{
    return m_keep_time_isValid;
}

QString OAILink::getParams() const {
    return m_params;
}
void OAILink::setParams(const QString &params) {
    m_params = params;
    m_params_isSet = true;
}

bool OAILink::is_params_Set() const{
    return m_params_isSet;
}

bool OAILink::is_params_Valid() const{
    return m_params_isValid;
}

QList<QString> OAILink::getTags() const {
    return m_tags;
}
void OAILink::setTags(const QList<QString> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAILink::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAILink::is_tags_Valid() const{
    return m_tags_isValid;
}

bool OAILink::isTargetBlank() const {
    return m_target_blank;
}
void OAILink::setTargetBlank(const bool &target_blank) {
    m_target_blank = target_blank;
    m_target_blank_isSet = true;
}

bool OAILink::is_target_blank_Set() const{
    return m_target_blank_isSet;
}

bool OAILink::is_target_blank_Valid() const{
    return m_target_blank_isValid;
}

QString OAILink::getTitle() const {
    return m_title;
}
void OAILink::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAILink::is_title_Set() const{
    return m_title_isSet;
}

bool OAILink::is_title_Valid() const{
    return m_title_isValid;
}

QString OAILink::getTooltip() const {
    return m_tooltip;
}
void OAILink::setTooltip(const QString &tooltip) {
    m_tooltip = tooltip;
    m_tooltip_isSet = true;
}

bool OAILink::is_tooltip_Set() const{
    return m_tooltip_isSet;
}

bool OAILink::is_tooltip_Valid() const{
    return m_tooltip_isValid;
}

QString OAILink::getType() const {
    return m_type;
}
void OAILink::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAILink::is_type_Set() const{
    return m_type_isSet;
}

bool OAILink::is_type_Valid() const{
    return m_type_isValid;
}

QString OAILink::getUrl() const {
    return m_url;
}
void OAILink::setUrl(const QString &url) {
    m_url = url;
    m_url_isSet = true;
}

bool OAILink::is_url_Set() const{
    return m_url_isSet;
}

bool OAILink::is_url_Valid() const{
    return m_url_isValid;
}

bool OAILink::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_as_dropdown_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dash_uri_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dashboard_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_icon_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_include_vars_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_keep_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_params_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_target_blank_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tooltip_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILink::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
