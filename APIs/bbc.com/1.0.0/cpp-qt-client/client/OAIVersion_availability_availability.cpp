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

#include "OAIVersion_availability_availability.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVersion_availability_availability::OAIVersion_availability_availability(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVersion_availability_availability::OAIVersion_availability_availability() {
    this->initializeModel();
}

OAIVersion_availability_availability::~OAIVersion_availability_availability() {}

void OAIVersion_availability_availability::initializeModel() {

    m_availability_isSet = false;
    m_availability_isValid = false;

    m_availability_end_isSet = false;
    m_availability_end_isValid = false;

    m_availability_start_isSet = false;
    m_availability_start_isValid = false;

    m_available_media_sets_isSet = false;
    m_available_media_sets_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAIVersion_availability_availability::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVersion_availability_availability::fromJsonObject(QJsonObject json) {

    m_availability_isValid = ::OpenAPI::fromJsonValue(m_availability, json[QString("availability")]);
    m_availability_isSet = !json[QString("availability")].isNull() && m_availability_isValid;

    m_availability_end_isValid = ::OpenAPI::fromJsonValue(m_availability_end, json[QString("availability_end")]);
    m_availability_end_isSet = !json[QString("availability_end")].isNull() && m_availability_end_isValid;

    m_availability_start_isValid = ::OpenAPI::fromJsonValue(m_availability_start, json[QString("availability_start")]);
    m_availability_start_isSet = !json[QString("availability_start")].isNull() && m_availability_start_isValid;

    m_available_media_sets_isValid = ::OpenAPI::fromJsonValue(m_available_media_sets, json[QString("available_media_sets")]);
    m_available_media_sets_isSet = !json[QString("available_media_sets")].isNull() && m_available_media_sets_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;
}

QString OAIVersion_availability_availability::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVersion_availability_availability::asJsonObject() const {
    QJsonObject obj;
    if (m_availability.isSet()) {
        obj.insert(QString("availability"), ::OpenAPI::toJsonValue(m_availability));
    }
    if (m_availability_end_isSet) {
        obj.insert(QString("availability_end"), ::OpenAPI::toJsonValue(m_availability_end));
    }
    if (m_availability_start_isSet) {
        obj.insert(QString("availability_start"), ::OpenAPI::toJsonValue(m_availability_start));
    }
    if (m_available_media_sets.isSet()) {
        obj.insert(QString("available_media_sets"), ::OpenAPI::toJsonValue(m_available_media_sets));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

OAIVersion_availability_availability_availability OAIVersion_availability_availability::getAvailability() const {
    return m_availability;
}
void OAIVersion_availability_availability::setAvailability(const OAIVersion_availability_availability_availability &availability) {
    m_availability = availability;
    m_availability_isSet = true;
}

bool OAIVersion_availability_availability::is_availability_Set() const{
    return m_availability_isSet;
}

bool OAIVersion_availability_availability::is_availability_Valid() const{
    return m_availability_isValid;
}

QDateTime OAIVersion_availability_availability::getAvailabilityEnd() const {
    return m_availability_end;
}
void OAIVersion_availability_availability::setAvailabilityEnd(const QDateTime &availability_end) {
    m_availability_end = availability_end;
    m_availability_end_isSet = true;
}

bool OAIVersion_availability_availability::is_availability_end_Set() const{
    return m_availability_end_isSet;
}

bool OAIVersion_availability_availability::is_availability_end_Valid() const{
    return m_availability_end_isValid;
}

QDateTime OAIVersion_availability_availability::getAvailabilityStart() const {
    return m_availability_start;
}
void OAIVersion_availability_availability::setAvailabilityStart(const QDateTime &availability_start) {
    m_availability_start = availability_start;
    m_availability_start_isSet = true;
}

bool OAIVersion_availability_availability::is_availability_start_Set() const{
    return m_availability_start_isSet;
}

bool OAIVersion_availability_availability::is_availability_start_Valid() const{
    return m_availability_start_isValid;
}

OAIAvailable_media_sets OAIVersion_availability_availability::getAvailableMediaSets() const {
    return m_available_media_sets;
}
void OAIVersion_availability_availability::setAvailableMediaSets(const OAIAvailable_media_sets &available_media_sets) {
    m_available_media_sets = available_media_sets;
    m_available_media_sets_isSet = true;
}

bool OAIVersion_availability_availability::is_available_media_sets_Set() const{
    return m_available_media_sets_isSet;
}

bool OAIVersion_availability_availability::is_available_media_sets_Valid() const{
    return m_available_media_sets_isValid;
}

QString OAIVersion_availability_availability::getStatus() const {
    return m_status;
}
void OAIVersion_availability_availability::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIVersion_availability_availability::is_status_Set() const{
    return m_status_isSet;
}

bool OAIVersion_availability_availability::is_status_Valid() const{
    return m_status_isValid;
}

bool OAIVersion_availability_availability::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_availability.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_availability_end_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_availability_start_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_available_media_sets.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVersion_availability_availability::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_availability_isValid && m_available_media_sets_isValid && true;
}

} // namespace OpenAPI
