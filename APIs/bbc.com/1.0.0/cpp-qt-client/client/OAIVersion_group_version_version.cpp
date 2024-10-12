/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIVersion_group_version_version.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVersion_group_version_version::OAIVersion_group_version_version(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVersion_group_version_version::OAIVersion_group_version_version() {
    this->initializeModel();
}

OAIVersion_group_version_version::~OAIVersion_group_version_version() {}

void OAIVersion_group_version_version::initializeModel() {

    m_aspect_ratio_isSet = false;
    m_aspect_ratio_isValid = false;

    m_competition_warning_isSet = false;
    m_competition_warning_isValid = false;

    m_duration_isSet = false;
    m_duration_isValid = false;

    m_identifiers_isSet = false;
    m_identifiers_isValid = false;

    m_ids_isSet = false;
    m_ids_isValid = false;

    m_pid_isSet = false;
    m_pid_isValid = false;

    m_types_with_id_isSet = false;
    m_types_with_id_isValid = false;

    m_updated_time_isSet = false;
    m_updated_time_isValid = false;

    m_version_of_isSet = false;
    m_version_of_isValid = false;

    m_version_types_with_id_isSet = false;
    m_version_types_with_id_isValid = false;

    m_warnings_isSet = false;
    m_warnings_isValid = false;
}

void OAIVersion_group_version_version::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVersion_group_version_version::fromJsonObject(QJsonObject json) {

    m_aspect_ratio_isValid = ::OpenAPI::fromJsonValue(m_aspect_ratio, json[QString("aspect_ratio")]);
    m_aspect_ratio_isSet = !json[QString("aspect_ratio")].isNull() && m_aspect_ratio_isValid;

    m_competition_warning_isValid = ::OpenAPI::fromJsonValue(m_competition_warning, json[QString("competition_warning")]);
    m_competition_warning_isSet = !json[QString("competition_warning")].isNull() && m_competition_warning_isValid;

    m_duration_isValid = ::OpenAPI::fromJsonValue(m_duration, json[QString("duration")]);
    m_duration_isSet = !json[QString("duration")].isNull() && m_duration_isValid;

    m_identifiers_isValid = ::OpenAPI::fromJsonValue(m_identifiers, json[QString("identifiers")]);
    m_identifiers_isSet = !json[QString("identifiers")].isNull() && m_identifiers_isValid;

    m_ids_isValid = ::OpenAPI::fromJsonValue(m_ids, json[QString("ids")]);
    m_ids_isSet = !json[QString("ids")].isNull() && m_ids_isValid;

    m_pid_isValid = ::OpenAPI::fromJsonValue(m_pid, json[QString("pid")]);
    m_pid_isSet = !json[QString("pid")].isNull() && m_pid_isValid;

    m_types_with_id_isValid = ::OpenAPI::fromJsonValue(m_types_with_id, json[QString("types_with_id")]);
    m_types_with_id_isSet = !json[QString("types_with_id")].isNull() && m_types_with_id_isValid;

    m_updated_time_isValid = ::OpenAPI::fromJsonValue(m_updated_time, json[QString("updated_time")]);
    m_updated_time_isSet = !json[QString("updated_time")].isNull() && m_updated_time_isValid;

    m_version_of_isValid = ::OpenAPI::fromJsonValue(m_version_of, json[QString("version_of")]);
    m_version_of_isSet = !json[QString("version_of")].isNull() && m_version_of_isValid;

    m_version_types_with_id_isValid = ::OpenAPI::fromJsonValue(m_version_types_with_id, json[QString("version_types_with_id")]);
    m_version_types_with_id_isSet = !json[QString("version_types_with_id")].isNull() && m_version_types_with_id_isValid;

    m_warnings_isValid = ::OpenAPI::fromJsonValue(m_warnings, json[QString("warnings")]);
    m_warnings_isSet = !json[QString("warnings")].isNull() && m_warnings_isValid;
}

QString OAIVersion_group_version_version::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVersion_group_version_version::asJsonObject() const {
    QJsonObject obj;
    if (m_aspect_ratio_isSet) {
        obj.insert(QString("aspect_ratio"), ::OpenAPI::toJsonValue(m_aspect_ratio));
    }
    if (m_competition_warning_isSet) {
        obj.insert(QString("competition_warning"), ::OpenAPI::toJsonValue(m_competition_warning));
    }
    if (m_duration_isSet) {
        obj.insert(QString("duration"), ::OpenAPI::toJsonValue(m_duration));
    }
    if (m_identifiers.isSet()) {
        obj.insert(QString("identifiers"), ::OpenAPI::toJsonValue(m_identifiers));
    }
    if (m_ids.isSet()) {
        obj.insert(QString("ids"), ::OpenAPI::toJsonValue(m_ids));
    }
    if (m_pid_isSet) {
        obj.insert(QString("pid"), ::OpenAPI::toJsonValue(m_pid));
    }
    if (m_types_with_id.isSet()) {
        obj.insert(QString("types_with_id"), ::OpenAPI::toJsonValue(m_types_with_id));
    }
    if (m_updated_time_isSet) {
        obj.insert(QString("updated_time"), ::OpenAPI::toJsonValue(m_updated_time));
    }
    if (m_version_of.isSet()) {
        obj.insert(QString("version_of"), ::OpenAPI::toJsonValue(m_version_of));
    }
    if (m_version_types_with_id.isSet()) {
        obj.insert(QString("version_types_with_id"), ::OpenAPI::toJsonValue(m_version_types_with_id));
    }
    if (m_warnings.isSet()) {
        obj.insert(QString("warnings"), ::OpenAPI::toJsonValue(m_warnings));
    }
    return obj;
}

QString OAIVersion_group_version_version::getAspectRatio() const {
    return m_aspect_ratio;
}
void OAIVersion_group_version_version::setAspectRatio(const QString &aspect_ratio) {
    m_aspect_ratio = aspect_ratio;
    m_aspect_ratio_isSet = true;
}

bool OAIVersion_group_version_version::is_aspect_ratio_Set() const{
    return m_aspect_ratio_isSet;
}

bool OAIVersion_group_version_version::is_aspect_ratio_Valid() const{
    return m_aspect_ratio_isValid;
}

bool OAIVersion_group_version_version::isCompetitionWarning() const {
    return m_competition_warning;
}
void OAIVersion_group_version_version::setCompetitionWarning(const bool &competition_warning) {
    m_competition_warning = competition_warning;
    m_competition_warning_isSet = true;
}

bool OAIVersion_group_version_version::is_competition_warning_Set() const{
    return m_competition_warning_isSet;
}

bool OAIVersion_group_version_version::is_competition_warning_Valid() const{
    return m_competition_warning_isValid;
}

QString OAIVersion_group_version_version::getDuration() const {
    return m_duration;
}
void OAIVersion_group_version_version::setDuration(const QString &duration) {
    m_duration = duration;
    m_duration_isSet = true;
}

bool OAIVersion_group_version_version::is_duration_Set() const{
    return m_duration_isSet;
}

bool OAIVersion_group_version_version::is_duration_Valid() const{
    return m_duration_isValid;
}

OAIIdentifiers OAIVersion_group_version_version::getIdentifiers() const {
    return m_identifiers;
}
void OAIVersion_group_version_version::setIdentifiers(const OAIIdentifiers &identifiers) {
    m_identifiers = identifiers;
    m_identifiers_isSet = true;
}

bool OAIVersion_group_version_version::is_identifiers_Set() const{
    return m_identifiers_isSet;
}

bool OAIVersion_group_version_version::is_identifiers_Valid() const{
    return m_identifiers_isValid;
}

OAIIds OAIVersion_group_version_version::getIds() const {
    return m_ids;
}
void OAIVersion_group_version_version::setIds(const OAIIds &ids) {
    m_ids = ids;
    m_ids_isSet = true;
}

bool OAIVersion_group_version_version::is_ids_Set() const{
    return m_ids_isSet;
}

bool OAIVersion_group_version_version::is_ids_Valid() const{
    return m_ids_isValid;
}

QString OAIVersion_group_version_version::getPid() const {
    return m_pid;
}
void OAIVersion_group_version_version::setPid(const QString &pid) {
    m_pid = pid;
    m_pid_isSet = true;
}

bool OAIVersion_group_version_version::is_pid_Set() const{
    return m_pid_isSet;
}

bool OAIVersion_group_version_version::is_pid_Valid() const{
    return m_pid_isValid;
}

OAITypes_with_id OAIVersion_group_version_version::getTypesWithId() const {
    return m_types_with_id;
}
void OAIVersion_group_version_version::setTypesWithId(const OAITypes_with_id &types_with_id) {
    m_types_with_id = types_with_id;
    m_types_with_id_isSet = true;
}

bool OAIVersion_group_version_version::is_types_with_id_Set() const{
    return m_types_with_id_isSet;
}

bool OAIVersion_group_version_version::is_types_with_id_Valid() const{
    return m_types_with_id_isValid;
}

QDateTime OAIVersion_group_version_version::getUpdatedTime() const {
    return m_updated_time;
}
void OAIVersion_group_version_version::setUpdatedTime(const QDateTime &updated_time) {
    m_updated_time = updated_time;
    m_updated_time_isSet = true;
}

bool OAIVersion_group_version_version::is_updated_time_Set() const{
    return m_updated_time_isSet;
}

bool OAIVersion_group_version_version::is_updated_time_Valid() const{
    return m_updated_time_isValid;
}

OAIPidReference OAIVersion_group_version_version::getVersionOf() const {
    return m_version_of;
}
void OAIVersion_group_version_version::setVersionOf(const OAIPidReference &version_of) {
    m_version_of = version_of;
    m_version_of_isSet = true;
}

bool OAIVersion_group_version_version::is_version_of_Set() const{
    return m_version_of_isSet;
}

bool OAIVersion_group_version_version::is_version_of_Valid() const{
    return m_version_of_isValid;
}

OAIVersion_types_with_id OAIVersion_group_version_version::getVersionTypesWithId() const {
    return m_version_types_with_id;
}
void OAIVersion_group_version_version::setVersionTypesWithId(const OAIVersion_types_with_id &version_types_with_id) {
    m_version_types_with_id = version_types_with_id;
    m_version_types_with_id_isSet = true;
}

bool OAIVersion_group_version_version::is_version_types_with_id_Set() const{
    return m_version_types_with_id_isSet;
}

bool OAIVersion_group_version_version::is_version_types_with_id_Valid() const{
    return m_version_types_with_id_isValid;
}

OAIWarnings OAIVersion_group_version_version::getWarnings() const {
    return m_warnings;
}
void OAIVersion_group_version_version::setWarnings(const OAIWarnings &warnings) {
    m_warnings = warnings;
    m_warnings_isSet = true;
}

bool OAIVersion_group_version_version::is_warnings_Set() const{
    return m_warnings_isSet;
}

bool OAIVersion_group_version_version::is_warnings_Valid() const{
    return m_warnings_isValid;
}

bool OAIVersion_group_version_version::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_aspect_ratio_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_competition_warning_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_identifiers.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_ids.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_pid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_types_with_id.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_of.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_types_with_id.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_warnings.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVersion_group_version_version::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_pid_isValid && m_updated_time_isValid && true;
}

} // namespace OpenAPI
