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

#include "OAIPerformanceReport_video_video_metadata_events_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPerformanceReport_video_video_metadata_events_inner::OAIPerformanceReport_video_video_metadata_events_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPerformanceReport_video_video_metadata_events_inner::OAIPerformanceReport_video_video_metadata_events_inner() {
    this->initializeModel();
}

OAIPerformanceReport_video_video_metadata_events_inner::~OAIPerformanceReport_video_video_metadata_events_inner() {}

void OAIPerformanceReport_video_video_metadata_events_inner::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_millis_isSet = false;
    m_millis_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIPerformanceReport_video_video_metadata_events_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPerformanceReport_video_video_metadata_events_inner::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_millis_isValid = ::OpenAPI::fromJsonValue(m_millis, json[QString("millis")]);
    m_millis_isSet = !json[QString("millis")].isNull() && m_millis_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIPerformanceReport_video_video_metadata_events_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPerformanceReport_video_video_metadata_events_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_millis_isSet) {
        obj.insert(QString("millis"), ::OpenAPI::toJsonValue(m_millis));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIPerformanceReport_video_video_metadata_events_inner::getId() const {
    return m_id;
}
void OAIPerformanceReport_video_video_metadata_events_inner::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIPerformanceReport_video_video_metadata_events_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAIPerformanceReport_video_video_metadata_events_inner::is_id_Valid() const{
    return m_id_isValid;
}

double OAIPerformanceReport_video_video_metadata_events_inner::getMillis() const {
    return m_millis;
}
void OAIPerformanceReport_video_video_metadata_events_inner::setMillis(const double &millis) {
    m_millis = millis;
    m_millis_isSet = true;
}

bool OAIPerformanceReport_video_video_metadata_events_inner::is_millis_Set() const{
    return m_millis_isSet;
}

bool OAIPerformanceReport_video_video_metadata_events_inner::is_millis_Valid() const{
    return m_millis_isValid;
}

QString OAIPerformanceReport_video_video_metadata_events_inner::getName() const {
    return m_name;
}
void OAIPerformanceReport_video_video_metadata_events_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIPerformanceReport_video_video_metadata_events_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIPerformanceReport_video_video_metadata_events_inner::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIPerformanceReport_video_video_metadata_events_inner::getType() const {
    return m_type;
}
void OAIPerformanceReport_video_video_metadata_events_inner::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIPerformanceReport_video_video_metadata_events_inner::is_type_Set() const{
    return m_type_isSet;
}

bool OAIPerformanceReport_video_video_metadata_events_inner::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIPerformanceReport_video_video_metadata_events_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_millis_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPerformanceReport_video_video_metadata_events_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
