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

#include "OAIUpdate.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdate::OAIUpdate(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdate::OAIUpdate() {
    this->initializeModel();
}

OAIUpdate::~OAIUpdate() {}

void OAIUpdate::initializeModel() {

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_day_isSet = false;
    m_day_isValid = false;

    m_due_at_isSet = false;
    m_due_at_isValid = false;

    m_due_time_isSet = false;
    m_due_time_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_profile_id_isSet = false;
    m_profile_id_isValid = false;

    m_profile_service_isSet = false;
    m_profile_service_isValid = false;

    m_sent_at_isSet = false;
    m_sent_at_isValid = false;

    m_service_update_id_isSet = false;
    m_service_update_id_isValid = false;

    m_statistics_isSet = false;
    m_statistics_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_text_isSet = false;
    m_text_isValid = false;

    m_text_formatted_isSet = false;
    m_text_formatted_isValid = false;

    m_user_id_isSet = false;
    m_user_id_isValid = false;

    m_via_isSet = false;
    m_via_isValid = false;
}

void OAIUpdate::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdate::fromJsonObject(QJsonObject json) {

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_day_isValid = ::OpenAPI::fromJsonValue(m_day, json[QString("day")]);
    m_day_isSet = !json[QString("day")].isNull() && m_day_isValid;

    m_due_at_isValid = ::OpenAPI::fromJsonValue(m_due_at, json[QString("due_at")]);
    m_due_at_isSet = !json[QString("due_at")].isNull() && m_due_at_isValid;

    m_due_time_isValid = ::OpenAPI::fromJsonValue(m_due_time, json[QString("due_time")]);
    m_due_time_isSet = !json[QString("due_time")].isNull() && m_due_time_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_profile_id_isValid = ::OpenAPI::fromJsonValue(m_profile_id, json[QString("profile_id")]);
    m_profile_id_isSet = !json[QString("profile_id")].isNull() && m_profile_id_isValid;

    m_profile_service_isValid = ::OpenAPI::fromJsonValue(m_profile_service, json[QString("profile_service")]);
    m_profile_service_isSet = !json[QString("profile_service")].isNull() && m_profile_service_isValid;

    m_sent_at_isValid = ::OpenAPI::fromJsonValue(m_sent_at, json[QString("sent_at")]);
    m_sent_at_isSet = !json[QString("sent_at")].isNull() && m_sent_at_isValid;

    m_service_update_id_isValid = ::OpenAPI::fromJsonValue(m_service_update_id, json[QString("service_update_id")]);
    m_service_update_id_isSet = !json[QString("service_update_id")].isNull() && m_service_update_id_isValid;

    m_statistics_isValid = ::OpenAPI::fromJsonValue(m_statistics, json[QString("statistics")]);
    m_statistics_isSet = !json[QString("statistics")].isNull() && m_statistics_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_text_isValid = ::OpenAPI::fromJsonValue(m_text, json[QString("text")]);
    m_text_isSet = !json[QString("text")].isNull() && m_text_isValid;

    m_text_formatted_isValid = ::OpenAPI::fromJsonValue(m_text_formatted, json[QString("text_formatted")]);
    m_text_formatted_isSet = !json[QString("text_formatted")].isNull() && m_text_formatted_isValid;

    m_user_id_isValid = ::OpenAPI::fromJsonValue(m_user_id, json[QString("user_id")]);
    m_user_id_isSet = !json[QString("user_id")].isNull() && m_user_id_isValid;

    m_via_isValid = ::OpenAPI::fromJsonValue(m_via, json[QString("via")]);
    m_via_isSet = !json[QString("via")].isNull() && m_via_isValid;
}

QString OAIUpdate::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdate::asJsonObject() const {
    QJsonObject obj;
    if (m_created_at_isSet) {
        obj.insert(QString("created_at"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_day_isSet) {
        obj.insert(QString("day"), ::OpenAPI::toJsonValue(m_day));
    }
    if (m_due_at_isSet) {
        obj.insert(QString("due_at"), ::OpenAPI::toJsonValue(m_due_at));
    }
    if (m_due_time_isSet) {
        obj.insert(QString("due_time"), ::OpenAPI::toJsonValue(m_due_time));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_profile_id_isSet) {
        obj.insert(QString("profile_id"), ::OpenAPI::toJsonValue(m_profile_id));
    }
    if (m_profile_service_isSet) {
        obj.insert(QString("profile_service"), ::OpenAPI::toJsonValue(m_profile_service));
    }
    if (m_sent_at_isSet) {
        obj.insert(QString("sent_at"), ::OpenAPI::toJsonValue(m_sent_at));
    }
    if (m_service_update_id_isSet) {
        obj.insert(QString("service_update_id"), ::OpenAPI::toJsonValue(m_service_update_id));
    }
    if (m_statistics.isSet()) {
        obj.insert(QString("statistics"), ::OpenAPI::toJsonValue(m_statistics));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_text_isSet) {
        obj.insert(QString("text"), ::OpenAPI::toJsonValue(m_text));
    }
    if (m_text_formatted_isSet) {
        obj.insert(QString("text_formatted"), ::OpenAPI::toJsonValue(m_text_formatted));
    }
    if (m_user_id_isSet) {
        obj.insert(QString("user_id"), ::OpenAPI::toJsonValue(m_user_id));
    }
    if (m_via_isSet) {
        obj.insert(QString("via"), ::OpenAPI::toJsonValue(m_via));
    }
    return obj;
}

double OAIUpdate::getCreatedAt() const {
    return m_created_at;
}
void OAIUpdate::setCreatedAt(const double &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIUpdate::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIUpdate::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIUpdate::getDay() const {
    return m_day;
}
void OAIUpdate::setDay(const QString &day) {
    m_day = day;
    m_day_isSet = true;
}

bool OAIUpdate::is_day_Set() const{
    return m_day_isSet;
}

bool OAIUpdate::is_day_Valid() const{
    return m_day_isValid;
}

double OAIUpdate::getDueAt() const {
    return m_due_at;
}
void OAIUpdate::setDueAt(const double &due_at) {
    m_due_at = due_at;
    m_due_at_isSet = true;
}

bool OAIUpdate::is_due_at_Set() const{
    return m_due_at_isSet;
}

bool OAIUpdate::is_due_at_Valid() const{
    return m_due_at_isValid;
}

QString OAIUpdate::getDueTime() const {
    return m_due_time;
}
void OAIUpdate::setDueTime(const QString &due_time) {
    m_due_time = due_time;
    m_due_time_isSet = true;
}

bool OAIUpdate::is_due_time_Set() const{
    return m_due_time_isSet;
}

bool OAIUpdate::is_due_time_Valid() const{
    return m_due_time_isValid;
}

QString OAIUpdate::getId() const {
    return m_id;
}
void OAIUpdate::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIUpdate::is_id_Set() const{
    return m_id_isSet;
}

bool OAIUpdate::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIUpdate::getProfileId() const {
    return m_profile_id;
}
void OAIUpdate::setProfileId(const QString &profile_id) {
    m_profile_id = profile_id;
    m_profile_id_isSet = true;
}

bool OAIUpdate::is_profile_id_Set() const{
    return m_profile_id_isSet;
}

bool OAIUpdate::is_profile_id_Valid() const{
    return m_profile_id_isValid;
}

QString OAIUpdate::getProfileService() const {
    return m_profile_service;
}
void OAIUpdate::setProfileService(const QString &profile_service) {
    m_profile_service = profile_service;
    m_profile_service_isSet = true;
}

bool OAIUpdate::is_profile_service_Set() const{
    return m_profile_service_isSet;
}

bool OAIUpdate::is_profile_service_Valid() const{
    return m_profile_service_isValid;
}

double OAIUpdate::getSentAt() const {
    return m_sent_at;
}
void OAIUpdate::setSentAt(const double &sent_at) {
    m_sent_at = sent_at;
    m_sent_at_isSet = true;
}

bool OAIUpdate::is_sent_at_Set() const{
    return m_sent_at_isSet;
}

bool OAIUpdate::is_sent_at_Valid() const{
    return m_sent_at_isValid;
}

QString OAIUpdate::getServiceUpdateId() const {
    return m_service_update_id;
}
void OAIUpdate::setServiceUpdateId(const QString &service_update_id) {
    m_service_update_id = service_update_id;
    m_service_update_id_isSet = true;
}

bool OAIUpdate::is_service_update_id_Set() const{
    return m_service_update_id_isSet;
}

bool OAIUpdate::is_service_update_id_Valid() const{
    return m_service_update_id_isValid;
}

OAIUpdate_statistics OAIUpdate::getStatistics() const {
    return m_statistics;
}
void OAIUpdate::setStatistics(const OAIUpdate_statistics &statistics) {
    m_statistics = statistics;
    m_statistics_isSet = true;
}

bool OAIUpdate::is_statistics_Set() const{
    return m_statistics_isSet;
}

bool OAIUpdate::is_statistics_Valid() const{
    return m_statistics_isValid;
}

QString OAIUpdate::getStatus() const {
    return m_status;
}
void OAIUpdate::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIUpdate::is_status_Set() const{
    return m_status_isSet;
}

bool OAIUpdate::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIUpdate::getText() const {
    return m_text;
}
void OAIUpdate::setText(const QString &text) {
    m_text = text;
    m_text_isSet = true;
}

bool OAIUpdate::is_text_Set() const{
    return m_text_isSet;
}

bool OAIUpdate::is_text_Valid() const{
    return m_text_isValid;
}

QString OAIUpdate::getTextFormatted() const {
    return m_text_formatted;
}
void OAIUpdate::setTextFormatted(const QString &text_formatted) {
    m_text_formatted = text_formatted;
    m_text_formatted_isSet = true;
}

bool OAIUpdate::is_text_formatted_Set() const{
    return m_text_formatted_isSet;
}

bool OAIUpdate::is_text_formatted_Valid() const{
    return m_text_formatted_isValid;
}

QString OAIUpdate::getUserId() const {
    return m_user_id;
}
void OAIUpdate::setUserId(const QString &user_id) {
    m_user_id = user_id;
    m_user_id_isSet = true;
}

bool OAIUpdate::is_user_id_Set() const{
    return m_user_id_isSet;
}

bool OAIUpdate::is_user_id_Valid() const{
    return m_user_id_isValid;
}

QString OAIUpdate::getVia() const {
    return m_via;
}
void OAIUpdate::setVia(const QString &via) {
    m_via = via;
    m_via_isSet = true;
}

bool OAIUpdate::is_via_Set() const{
    return m_via_isSet;
}

bool OAIUpdate::is_via_Valid() const{
    return m_via_isValid;
}

bool OAIUpdate::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_day_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_due_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_due_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_profile_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_profile_service_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sent_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_service_update_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_statistics.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_text_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_text_formatted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_via_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdate::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
