/**
 * Bufferapp
 * Social media management for marketers and agencies
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIProfiles_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProfiles_inner::OAIProfiles_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProfiles_inner::OAIProfiles_inner() {
    this->initializeModel();
}

OAIProfiles_inner::~OAIProfiles_inner() {}

void OAIProfiles_inner::initializeModel() {

    m__id_isSet = false;
    m__id_isValid = false;

    m_avatar_isSet = false;
    m_avatar_isValid = false;

    m_avatar_https_isSet = false;
    m_avatar_https_isValid = false;

    m_counts_isSet = false;
    m_counts_isValid = false;

    m_cover_photo_isSet = false;
    m_cover_photo_isValid = false;

    m_r_default_isSet = false;
    m_r_default_isValid = false;

    m_disabled_features_isSet = false;
    m_disabled_features_isValid = false;

    m_disconnected_isSet = false;
    m_disconnected_isValid = false;

    m_formatted_service_isSet = false;
    m_formatted_service_isValid = false;

    m_formatted_username_isSet = false;
    m_formatted_username_isValid = false;

    m_has_used_suggestions_isSet = false;
    m_has_used_suggestions_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_schedules_isSet = false;
    m_schedules_isValid = false;

    m_service_isSet = false;
    m_service_isValid = false;

    m_service_id_isSet = false;
    m_service_id_isValid = false;

    m_service_type_isSet = false;
    m_service_type_isValid = false;

    m_service_username_isSet = false;
    m_service_username_isValid = false;

    m_shortener_isSet = false;
    m_shortener_isValid = false;

    m_statistics_isSet = false;
    m_statistics_isValid = false;

    m_timezone_isSet = false;
    m_timezone_isValid = false;

    m_user_id_isSet = false;
    m_user_id_isValid = false;

    m_utm_tracking_isSet = false;
    m_utm_tracking_isValid = false;

    m_verb_isSet = false;
    m_verb_isValid = false;
}

void OAIProfiles_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProfiles_inner::fromJsonObject(QJsonObject json) {

    m__id_isValid = ::OpenAPI::fromJsonValue(m__id, json[QString("_id")]);
    m__id_isSet = !json[QString("_id")].isNull() && m__id_isValid;

    m_avatar_isValid = ::OpenAPI::fromJsonValue(m_avatar, json[QString("avatar")]);
    m_avatar_isSet = !json[QString("avatar")].isNull() && m_avatar_isValid;

    m_avatar_https_isValid = ::OpenAPI::fromJsonValue(m_avatar_https, json[QString("avatar_https")]);
    m_avatar_https_isSet = !json[QString("avatar_https")].isNull() && m_avatar_https_isValid;

    m_counts_isValid = ::OpenAPI::fromJsonValue(m_counts, json[QString("counts")]);
    m_counts_isSet = !json[QString("counts")].isNull() && m_counts_isValid;

    m_cover_photo_isValid = ::OpenAPI::fromJsonValue(m_cover_photo, json[QString("cover_photo")]);
    m_cover_photo_isSet = !json[QString("cover_photo")].isNull() && m_cover_photo_isValid;

    m_r_default_isValid = ::OpenAPI::fromJsonValue(m_r_default, json[QString("default")]);
    m_r_default_isSet = !json[QString("default")].isNull() && m_r_default_isValid;

    m_disabled_features_isValid = ::OpenAPI::fromJsonValue(m_disabled_features, json[QString("disabled_features")]);
    m_disabled_features_isSet = !json[QString("disabled_features")].isNull() && m_disabled_features_isValid;

    m_disconnected_isValid = ::OpenAPI::fromJsonValue(m_disconnected, json[QString("disconnected")]);
    m_disconnected_isSet = !json[QString("disconnected")].isNull() && m_disconnected_isValid;

    m_formatted_service_isValid = ::OpenAPI::fromJsonValue(m_formatted_service, json[QString("formatted_service")]);
    m_formatted_service_isSet = !json[QString("formatted_service")].isNull() && m_formatted_service_isValid;

    m_formatted_username_isValid = ::OpenAPI::fromJsonValue(m_formatted_username, json[QString("formatted_username")]);
    m_formatted_username_isSet = !json[QString("formatted_username")].isNull() && m_formatted_username_isValid;

    m_has_used_suggestions_isValid = ::OpenAPI::fromJsonValue(m_has_used_suggestions, json[QString("has_used_suggestions")]);
    m_has_used_suggestions_isSet = !json[QString("has_used_suggestions")].isNull() && m_has_used_suggestions_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_schedules_isValid = ::OpenAPI::fromJsonValue(m_schedules, json[QString("schedules")]);
    m_schedules_isSet = !json[QString("schedules")].isNull() && m_schedules_isValid;

    m_service_isValid = ::OpenAPI::fromJsonValue(m_service, json[QString("service")]);
    m_service_isSet = !json[QString("service")].isNull() && m_service_isValid;

    m_service_id_isValid = ::OpenAPI::fromJsonValue(m_service_id, json[QString("service_id")]);
    m_service_id_isSet = !json[QString("service_id")].isNull() && m_service_id_isValid;

    m_service_type_isValid = ::OpenAPI::fromJsonValue(m_service_type, json[QString("service_type")]);
    m_service_type_isSet = !json[QString("service_type")].isNull() && m_service_type_isValid;

    m_service_username_isValid = ::OpenAPI::fromJsonValue(m_service_username, json[QString("service_username")]);
    m_service_username_isSet = !json[QString("service_username")].isNull() && m_service_username_isValid;

    m_shortener_isValid = ::OpenAPI::fromJsonValue(m_shortener, json[QString("shortener")]);
    m_shortener_isSet = !json[QString("shortener")].isNull() && m_shortener_isValid;

    m_statistics_isValid = ::OpenAPI::fromJsonValue(m_statistics, json[QString("statistics")]);
    m_statistics_isSet = !json[QString("statistics")].isNull() && m_statistics_isValid;

    m_timezone_isValid = ::OpenAPI::fromJsonValue(m_timezone, json[QString("timezone")]);
    m_timezone_isSet = !json[QString("timezone")].isNull() && m_timezone_isValid;

    m_user_id_isValid = ::OpenAPI::fromJsonValue(m_user_id, json[QString("user_id")]);
    m_user_id_isSet = !json[QString("user_id")].isNull() && m_user_id_isValid;

    m_utm_tracking_isValid = ::OpenAPI::fromJsonValue(m_utm_tracking, json[QString("utm_tracking")]);
    m_utm_tracking_isSet = !json[QString("utm_tracking")].isNull() && m_utm_tracking_isValid;

    m_verb_isValid = ::OpenAPI::fromJsonValue(m_verb, json[QString("verb")]);
    m_verb_isSet = !json[QString("verb")].isNull() && m_verb_isValid;
}

QString OAIProfiles_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProfiles_inner::asJsonObject() const {
    QJsonObject obj;
    if (m__id_isSet) {
        obj.insert(QString("_id"), ::OpenAPI::toJsonValue(m__id));
    }
    if (m_avatar_isSet) {
        obj.insert(QString("avatar"), ::OpenAPI::toJsonValue(m_avatar));
    }
    if (m_avatar_https_isSet) {
        obj.insert(QString("avatar_https"), ::OpenAPI::toJsonValue(m_avatar_https));
    }
    if (m_counts.isSet()) {
        obj.insert(QString("counts"), ::OpenAPI::toJsonValue(m_counts));
    }
    if (m_cover_photo_isSet) {
        obj.insert(QString("cover_photo"), ::OpenAPI::toJsonValue(m_cover_photo));
    }
    if (m_r_default_isSet) {
        obj.insert(QString("default"), ::OpenAPI::toJsonValue(m_r_default));
    }
    if (m_disabled_features.size() > 0) {
        obj.insert(QString("disabled_features"), ::OpenAPI::toJsonValue(m_disabled_features));
    }
    if (m_disconnected_isSet) {
        obj.insert(QString("disconnected"), ::OpenAPI::toJsonValue(m_disconnected));
    }
    if (m_formatted_service_isSet) {
        obj.insert(QString("formatted_service"), ::OpenAPI::toJsonValue(m_formatted_service));
    }
    if (m_formatted_username_isSet) {
        obj.insert(QString("formatted_username"), ::OpenAPI::toJsonValue(m_formatted_username));
    }
    if (m_has_used_suggestions_isSet) {
        obj.insert(QString("has_used_suggestions"), ::OpenAPI::toJsonValue(m_has_used_suggestions));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_schedules.size() > 0) {
        obj.insert(QString("schedules"), ::OpenAPI::toJsonValue(m_schedules));
    }
    if (m_service_isSet) {
        obj.insert(QString("service"), ::OpenAPI::toJsonValue(m_service));
    }
    if (m_service_id_isSet) {
        obj.insert(QString("service_id"), ::OpenAPI::toJsonValue(m_service_id));
    }
    if (m_service_type_isSet) {
        obj.insert(QString("service_type"), ::OpenAPI::toJsonValue(m_service_type));
    }
    if (m_service_username_isSet) {
        obj.insert(QString("service_username"), ::OpenAPI::toJsonValue(m_service_username));
    }
    if (m_shortener.isSet()) {
        obj.insert(QString("shortener"), ::OpenAPI::toJsonValue(m_shortener));
    }
    if (m_statistics.isSet()) {
        obj.insert(QString("statistics"), ::OpenAPI::toJsonValue(m_statistics));
    }
    if (m_timezone_isSet) {
        obj.insert(QString("timezone"), ::OpenAPI::toJsonValue(m_timezone));
    }
    if (m_user_id_isSet) {
        obj.insert(QString("user_id"), ::OpenAPI::toJsonValue(m_user_id));
    }
    if (m_utm_tracking_isSet) {
        obj.insert(QString("utm_tracking"), ::OpenAPI::toJsonValue(m_utm_tracking));
    }
    if (m_verb_isSet) {
        obj.insert(QString("verb"), ::OpenAPI::toJsonValue(m_verb));
    }
    return obj;
}

QString OAIProfiles_inner::getId() const {
    return m__id;
}
void OAIProfiles_inner::setId(const QString &_id) {
    m__id = _id;
    m__id_isSet = true;
}

bool OAIProfiles_inner::is__id_Set() const{
    return m__id_isSet;
}

bool OAIProfiles_inner::is__id_Valid() const{
    return m__id_isValid;
}

QString OAIProfiles_inner::getAvatar() const {
    return m_avatar;
}
void OAIProfiles_inner::setAvatar(const QString &avatar) {
    m_avatar = avatar;
    m_avatar_isSet = true;
}

bool OAIProfiles_inner::is_avatar_Set() const{
    return m_avatar_isSet;
}

bool OAIProfiles_inner::is_avatar_Valid() const{
    return m_avatar_isValid;
}

QString OAIProfiles_inner::getAvatarHttps() const {
    return m_avatar_https;
}
void OAIProfiles_inner::setAvatarHttps(const QString &avatar_https) {
    m_avatar_https = avatar_https;
    m_avatar_https_isSet = true;
}

bool OAIProfiles_inner::is_avatar_https_Set() const{
    return m_avatar_https_isSet;
}

bool OAIProfiles_inner::is_avatar_https_Valid() const{
    return m_avatar_https_isValid;
}

OAIProfiles_inner_counts OAIProfiles_inner::getCounts() const {
    return m_counts;
}
void OAIProfiles_inner::setCounts(const OAIProfiles_inner_counts &counts) {
    m_counts = counts;
    m_counts_isSet = true;
}

bool OAIProfiles_inner::is_counts_Set() const{
    return m_counts_isSet;
}

bool OAIProfiles_inner::is_counts_Valid() const{
    return m_counts_isValid;
}

QString OAIProfiles_inner::getCoverPhoto() const {
    return m_cover_photo;
}
void OAIProfiles_inner::setCoverPhoto(const QString &cover_photo) {
    m_cover_photo = cover_photo;
    m_cover_photo_isSet = true;
}

bool OAIProfiles_inner::is_cover_photo_Set() const{
    return m_cover_photo_isSet;
}

bool OAIProfiles_inner::is_cover_photo_Valid() const{
    return m_cover_photo_isValid;
}

bool OAIProfiles_inner::isRDefault() const {
    return m_r_default;
}
void OAIProfiles_inner::setRDefault(const bool &r_default) {
    m_r_default = r_default;
    m_r_default_isSet = true;
}

bool OAIProfiles_inner::is_r_default_Set() const{
    return m_r_default_isSet;
}

bool OAIProfiles_inner::is_r_default_Valid() const{
    return m_r_default_isValid;
}

QList<OAIObject> OAIProfiles_inner::getDisabledFeatures() const {
    return m_disabled_features;
}
void OAIProfiles_inner::setDisabledFeatures(const QList<OAIObject> &disabled_features) {
    m_disabled_features = disabled_features;
    m_disabled_features_isSet = true;
}

bool OAIProfiles_inner::is_disabled_features_Set() const{
    return m_disabled_features_isSet;
}

bool OAIProfiles_inner::is_disabled_features_Valid() const{
    return m_disabled_features_isValid;
}

QString OAIProfiles_inner::getDisconnected() const {
    return m_disconnected;
}
void OAIProfiles_inner::setDisconnected(const QString &disconnected) {
    m_disconnected = disconnected;
    m_disconnected_isSet = true;
}

bool OAIProfiles_inner::is_disconnected_Set() const{
    return m_disconnected_isSet;
}

bool OAIProfiles_inner::is_disconnected_Valid() const{
    return m_disconnected_isValid;
}

QString OAIProfiles_inner::getFormattedService() const {
    return m_formatted_service;
}
void OAIProfiles_inner::setFormattedService(const QString &formatted_service) {
    m_formatted_service = formatted_service;
    m_formatted_service_isSet = true;
}

bool OAIProfiles_inner::is_formatted_service_Set() const{
    return m_formatted_service_isSet;
}

bool OAIProfiles_inner::is_formatted_service_Valid() const{
    return m_formatted_service_isValid;
}

QString OAIProfiles_inner::getFormattedUsername() const {
    return m_formatted_username;
}
void OAIProfiles_inner::setFormattedUsername(const QString &formatted_username) {
    m_formatted_username = formatted_username;
    m_formatted_username_isSet = true;
}

bool OAIProfiles_inner::is_formatted_username_Set() const{
    return m_formatted_username_isSet;
}

bool OAIProfiles_inner::is_formatted_username_Valid() const{
    return m_formatted_username_isValid;
}

bool OAIProfiles_inner::isHasUsedSuggestions() const {
    return m_has_used_suggestions;
}
void OAIProfiles_inner::setHasUsedSuggestions(const bool &has_used_suggestions) {
    m_has_used_suggestions = has_used_suggestions;
    m_has_used_suggestions_isSet = true;
}

bool OAIProfiles_inner::is_has_used_suggestions_Set() const{
    return m_has_used_suggestions_isSet;
}

bool OAIProfiles_inner::is_has_used_suggestions_Valid() const{
    return m_has_used_suggestions_isValid;
}

QString OAIProfiles_inner::getId() const {
    return m_id;
}
void OAIProfiles_inner::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIProfiles_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAIProfiles_inner::is_id_Valid() const{
    return m_id_isValid;
}

QList<OAIProfiles_inner_schedules_inner> OAIProfiles_inner::getSchedules() const {
    return m_schedules;
}
void OAIProfiles_inner::setSchedules(const QList<OAIProfiles_inner_schedules_inner> &schedules) {
    m_schedules = schedules;
    m_schedules_isSet = true;
}

bool OAIProfiles_inner::is_schedules_Set() const{
    return m_schedules_isSet;
}

bool OAIProfiles_inner::is_schedules_Valid() const{
    return m_schedules_isValid;
}

QString OAIProfiles_inner::getService() const {
    return m_service;
}
void OAIProfiles_inner::setService(const QString &service) {
    m_service = service;
    m_service_isSet = true;
}

bool OAIProfiles_inner::is_service_Set() const{
    return m_service_isSet;
}

bool OAIProfiles_inner::is_service_Valid() const{
    return m_service_isValid;
}

QString OAIProfiles_inner::getServiceId() const {
    return m_service_id;
}
void OAIProfiles_inner::setServiceId(const QString &service_id) {
    m_service_id = service_id;
    m_service_id_isSet = true;
}

bool OAIProfiles_inner::is_service_id_Set() const{
    return m_service_id_isSet;
}

bool OAIProfiles_inner::is_service_id_Valid() const{
    return m_service_id_isValid;
}

QString OAIProfiles_inner::getServiceType() const {
    return m_service_type;
}
void OAIProfiles_inner::setServiceType(const QString &service_type) {
    m_service_type = service_type;
    m_service_type_isSet = true;
}

bool OAIProfiles_inner::is_service_type_Set() const{
    return m_service_type_isSet;
}

bool OAIProfiles_inner::is_service_type_Valid() const{
    return m_service_type_isValid;
}

QString OAIProfiles_inner::getServiceUsername() const {
    return m_service_username;
}
void OAIProfiles_inner::setServiceUsername(const QString &service_username) {
    m_service_username = service_username;
    m_service_username_isSet = true;
}

bool OAIProfiles_inner::is_service_username_Set() const{
    return m_service_username_isSet;
}

bool OAIProfiles_inner::is_service_username_Valid() const{
    return m_service_username_isValid;
}

OAIProfiles_inner_shortener OAIProfiles_inner::getShortener() const {
    return m_shortener;
}
void OAIProfiles_inner::setShortener(const OAIProfiles_inner_shortener &shortener) {
    m_shortener = shortener;
    m_shortener_isSet = true;
}

bool OAIProfiles_inner::is_shortener_Set() const{
    return m_shortener_isSet;
}

bool OAIProfiles_inner::is_shortener_Valid() const{
    return m_shortener_isValid;
}

OAIProfiles_inner_statistics OAIProfiles_inner::getStatistics() const {
    return m_statistics;
}
void OAIProfiles_inner::setStatistics(const OAIProfiles_inner_statistics &statistics) {
    m_statistics = statistics;
    m_statistics_isSet = true;
}

bool OAIProfiles_inner::is_statistics_Set() const{
    return m_statistics_isSet;
}

bool OAIProfiles_inner::is_statistics_Valid() const{
    return m_statistics_isValid;
}

QString OAIProfiles_inner::getTimezone() const {
    return m_timezone;
}
void OAIProfiles_inner::setTimezone(const QString &timezone) {
    m_timezone = timezone;
    m_timezone_isSet = true;
}

bool OAIProfiles_inner::is_timezone_Set() const{
    return m_timezone_isSet;
}

bool OAIProfiles_inner::is_timezone_Valid() const{
    return m_timezone_isValid;
}

QString OAIProfiles_inner::getUserId() const {
    return m_user_id;
}
void OAIProfiles_inner::setUserId(const QString &user_id) {
    m_user_id = user_id;
    m_user_id_isSet = true;
}

bool OAIProfiles_inner::is_user_id_Set() const{
    return m_user_id_isSet;
}

bool OAIProfiles_inner::is_user_id_Valid() const{
    return m_user_id_isValid;
}

QString OAIProfiles_inner::getUtmTracking() const {
    return m_utm_tracking;
}
void OAIProfiles_inner::setUtmTracking(const QString &utm_tracking) {
    m_utm_tracking = utm_tracking;
    m_utm_tracking_isSet = true;
}

bool OAIProfiles_inner::is_utm_tracking_Set() const{
    return m_utm_tracking_isSet;
}

bool OAIProfiles_inner::is_utm_tracking_Valid() const{
    return m_utm_tracking_isValid;
}

QString OAIProfiles_inner::getVerb() const {
    return m_verb;
}
void OAIProfiles_inner::setVerb(const QString &verb) {
    m_verb = verb;
    m_verb_isSet = true;
}

bool OAIProfiles_inner::is_verb_Set() const{
    return m_verb_isSet;
}

bool OAIProfiles_inner::is_verb_Valid() const{
    return m_verb_isValid;
}

bool OAIProfiles_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m__id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_avatar_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_avatar_https_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_counts.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_cover_photo_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_default_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_disabled_features.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_disconnected_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_formatted_service_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_formatted_username_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_used_suggestions_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_schedules.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_service_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_service_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_service_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_service_username_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shortener.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_statistics.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_timezone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_utm_tracking_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_verb_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIProfiles_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
