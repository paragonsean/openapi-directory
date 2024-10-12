/**
 * UpdateAdminClient
 * Update run operation endpoints and objects.
 *
 * The version of the OpenAPI document: 2016-05-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUpdateRunModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateRunModel::OAIUpdateRunModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateRunModel::OAIUpdateRunModel() {
    this->initializeModel();
}

OAIUpdateRunModel::~OAIUpdateRunModel() {}

void OAIUpdateRunModel::initializeModel() {

    m_duration_isSet = false;
    m_duration_isValid = false;

    m_progress_isSet = false;
    m_progress_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;

    m_time_started_isSet = false;
    m_time_started_isValid = false;
}

void OAIUpdateRunModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateRunModel::fromJsonObject(QJsonObject json) {

    m_duration_isValid = ::OpenAPI::fromJsonValue(m_duration, json[QString("duration")]);
    m_duration_isSet = !json[QString("duration")].isNull() && m_duration_isValid;

    m_progress_isValid = ::OpenAPI::fromJsonValue(m_progress, json[QString("progress")]);
    m_progress_isSet = !json[QString("progress")].isNull() && m_progress_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;

    m_time_started_isValid = ::OpenAPI::fromJsonValue(m_time_started, json[QString("timeStarted")]);
    m_time_started_isSet = !json[QString("timeStarted")].isNull() && m_time_started_isValid;
}

QString OAIUpdateRunModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateRunModel::asJsonObject() const {
    QJsonObject obj;
    if (m_duration_isSet) {
        obj.insert(QString("duration"), ::OpenAPI::toJsonValue(m_duration));
    }
    if (m_progress.isSet()) {
        obj.insert(QString("progress"), ::OpenAPI::toJsonValue(m_progress));
    }
    if (m_state.isSet()) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    if (m_time_started_isSet) {
        obj.insert(QString("timeStarted"), ::OpenAPI::toJsonValue(m_time_started));
    }
    return obj;
}

QString OAIUpdateRunModel::getDuration() const {
    return m_duration;
}
void OAIUpdateRunModel::setDuration(const QString &duration) {
    m_duration = duration;
    m_duration_isSet = true;
}

bool OAIUpdateRunModel::is_duration_Set() const{
    return m_duration_isSet;
}

bool OAIUpdateRunModel::is_duration_Valid() const{
    return m_duration_isValid;
}

OAIStep OAIUpdateRunModel::getProgress() const {
    return m_progress;
}
void OAIUpdateRunModel::setProgress(const OAIStep &progress) {
    m_progress = progress;
    m_progress_isSet = true;
}

bool OAIUpdateRunModel::is_progress_Set() const{
    return m_progress_isSet;
}

bool OAIUpdateRunModel::is_progress_Valid() const{
    return m_progress_isValid;
}

OAIUpdateRunState OAIUpdateRunModel::getState() const {
    return m_state;
}
void OAIUpdateRunModel::setState(const OAIUpdateRunState &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIUpdateRunModel::is_state_Set() const{
    return m_state_isSet;
}

bool OAIUpdateRunModel::is_state_Valid() const{
    return m_state_isValid;
}

QDateTime OAIUpdateRunModel::getTimeStarted() const {
    return m_time_started;
}
void OAIUpdateRunModel::setTimeStarted(const QDateTime &time_started) {
    m_time_started = time_started;
    m_time_started_isSet = true;
}

bool OAIUpdateRunModel::is_time_started_Set() const{
    return m_time_started_isSet;
}

bool OAIUpdateRunModel::is_time_started_Valid() const{
    return m_time_started_isValid;
}

bool OAIUpdateRunModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_progress.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_state.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_started_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateRunModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
