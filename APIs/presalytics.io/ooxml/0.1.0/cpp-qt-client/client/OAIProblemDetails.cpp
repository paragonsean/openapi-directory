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

#include "OAIProblemDetails.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProblemDetails::OAIProblemDetails(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProblemDetails::OAIProblemDetails() {
    this->initializeModel();
}

OAIProblemDetails::~OAIProblemDetails() {}

void OAIProblemDetails::initializeModel() {

    m_detail_isSet = false;
    m_detail_isValid = false;

    m_instance_isSet = false;
    m_instance_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIProblemDetails::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProblemDetails::fromJsonObject(QJsonObject json) {

    m_detail_isValid = ::OpenAPI::fromJsonValue(m_detail, json[QString("detail")]);
    m_detail_isSet = !json[QString("detail")].isNull() && m_detail_isValid;

    m_instance_isValid = ::OpenAPI::fromJsonValue(m_instance, json[QString("instance")]);
    m_instance_isSet = !json[QString("instance")].isNull() && m_instance_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIProblemDetails::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProblemDetails::asJsonObject() const {
    QJsonObject obj;
    if (m_detail_isSet) {
        obj.insert(QString("detail"), ::OpenAPI::toJsonValue(m_detail));
    }
    if (m_instance_isSet) {
        obj.insert(QString("instance"), ::OpenAPI::toJsonValue(m_instance));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIProblemDetails::getDetail() const {
    return m_detail;
}
void OAIProblemDetails::setDetail(const QString &detail) {
    m_detail = detail;
    m_detail_isSet = true;
}

bool OAIProblemDetails::is_detail_Set() const{
    return m_detail_isSet;
}

bool OAIProblemDetails::is_detail_Valid() const{
    return m_detail_isValid;
}

QString OAIProblemDetails::getInstance() const {
    return m_instance;
}
void OAIProblemDetails::setInstance(const QString &instance) {
    m_instance = instance;
    m_instance_isSet = true;
}

bool OAIProblemDetails::is_instance_Set() const{
    return m_instance_isSet;
}

bool OAIProblemDetails::is_instance_Valid() const{
    return m_instance_isValid;
}

qint32 OAIProblemDetails::getStatus() const {
    return m_status;
}
void OAIProblemDetails::setStatus(const qint32 &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIProblemDetails::is_status_Set() const{
    return m_status_isSet;
}

bool OAIProblemDetails::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIProblemDetails::getTitle() const {
    return m_title;
}
void OAIProblemDetails::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIProblemDetails::is_title_Set() const{
    return m_title_isSet;
}

bool OAIProblemDetails::is_title_Valid() const{
    return m_title_isValid;
}

QString OAIProblemDetails::getType() const {
    return m_type;
}
void OAIProblemDetails::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIProblemDetails::is_type_Set() const{
    return m_type_isSet;
}

bool OAIProblemDetails::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIProblemDetails::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_detail_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_instance_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
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

bool OAIProblemDetails::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
