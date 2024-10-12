/**
 * Figshare API
 * Figshare apiv2. Using Swagger 2.0
 *
 * The version of the OpenAPI document: 2.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUploadFilePart.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUploadFilePart::OAIUploadFilePart(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUploadFilePart::OAIUploadFilePart() {
    this->initializeModel();
}

OAIUploadFilePart::~OAIUploadFilePart() {}

void OAIUploadFilePart::initializeModel() {

    m_end_offset_isSet = false;
    m_end_offset_isValid = false;

    m_locked_isSet = false;
    m_locked_isValid = false;

    m_part_no_isSet = false;
    m_part_no_isValid = false;

    m_start_offset_isSet = false;
    m_start_offset_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAIUploadFilePart::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUploadFilePart::fromJsonObject(QJsonObject json) {

    m_end_offset_isValid = ::OpenAPI::fromJsonValue(m_end_offset, json[QString("endOffset")]);
    m_end_offset_isSet = !json[QString("endOffset")].isNull() && m_end_offset_isValid;

    m_locked_isValid = ::OpenAPI::fromJsonValue(m_locked, json[QString("locked")]);
    m_locked_isSet = !json[QString("locked")].isNull() && m_locked_isValid;

    m_part_no_isValid = ::OpenAPI::fromJsonValue(m_part_no, json[QString("partNo")]);
    m_part_no_isSet = !json[QString("partNo")].isNull() && m_part_no_isValid;

    m_start_offset_isValid = ::OpenAPI::fromJsonValue(m_start_offset, json[QString("startOffset")]);
    m_start_offset_isSet = !json[QString("startOffset")].isNull() && m_start_offset_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;
}

QString OAIUploadFilePart::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUploadFilePart::asJsonObject() const {
    QJsonObject obj;
    if (m_end_offset_isSet) {
        obj.insert(QString("endOffset"), ::OpenAPI::toJsonValue(m_end_offset));
    }
    if (m_locked_isSet) {
        obj.insert(QString("locked"), ::OpenAPI::toJsonValue(m_locked));
    }
    if (m_part_no_isSet) {
        obj.insert(QString("partNo"), ::OpenAPI::toJsonValue(m_part_no));
    }
    if (m_start_offset_isSet) {
        obj.insert(QString("startOffset"), ::OpenAPI::toJsonValue(m_start_offset));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

qint64 OAIUploadFilePart::getEndOffset() const {
    return m_end_offset;
}
void OAIUploadFilePart::setEndOffset(const qint64 &end_offset) {
    m_end_offset = end_offset;
    m_end_offset_isSet = true;
}

bool OAIUploadFilePart::is_end_offset_Set() const{
    return m_end_offset_isSet;
}

bool OAIUploadFilePart::is_end_offset_Valid() const{
    return m_end_offset_isValid;
}

bool OAIUploadFilePart::isLocked() const {
    return m_locked;
}
void OAIUploadFilePart::setLocked(const bool &locked) {
    m_locked = locked;
    m_locked_isSet = true;
}

bool OAIUploadFilePart::is_locked_Set() const{
    return m_locked_isSet;
}

bool OAIUploadFilePart::is_locked_Valid() const{
    return m_locked_isValid;
}

qint64 OAIUploadFilePart::getPartNo() const {
    return m_part_no;
}
void OAIUploadFilePart::setPartNo(const qint64 &part_no) {
    m_part_no = part_no;
    m_part_no_isSet = true;
}

bool OAIUploadFilePart::is_part_no_Set() const{
    return m_part_no_isSet;
}

bool OAIUploadFilePart::is_part_no_Valid() const{
    return m_part_no_isValid;
}

qint64 OAIUploadFilePart::getStartOffset() const {
    return m_start_offset;
}
void OAIUploadFilePart::setStartOffset(const qint64 &start_offset) {
    m_start_offset = start_offset;
    m_start_offset_isSet = true;
}

bool OAIUploadFilePart::is_start_offset_Set() const{
    return m_start_offset_isSet;
}

bool OAIUploadFilePart::is_start_offset_Valid() const{
    return m_start_offset_isValid;
}

QString OAIUploadFilePart::getStatus() const {
    return m_status;
}
void OAIUploadFilePart::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIUploadFilePart::is_status_Set() const{
    return m_status_isSet;
}

bool OAIUploadFilePart::is_status_Valid() const{
    return m_status_isValid;
}

bool OAIUploadFilePart::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_end_offset_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_locked_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_part_no_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_offset_isSet) {
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

bool OAIUploadFilePart::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
