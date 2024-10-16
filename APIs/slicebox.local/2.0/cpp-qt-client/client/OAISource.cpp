/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISource.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISource::OAISource(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISource::OAISource() {
    this->initializeModel();
}

OAISource::~OAISource() {}

void OAISource::initializeModel() {

    m_source_id_isSet = false;
    m_source_id_isValid = false;

    m_source_name_isSet = false;
    m_source_name_isValid = false;

    m_source_type_isSet = false;
    m_source_type_isValid = false;
}

void OAISource::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISource::fromJsonObject(QJsonObject json) {

    m_source_id_isValid = ::OpenAPI::fromJsonValue(m_source_id, json[QString("sourceId")]);
    m_source_id_isSet = !json[QString("sourceId")].isNull() && m_source_id_isValid;

    m_source_name_isValid = ::OpenAPI::fromJsonValue(m_source_name, json[QString("sourceName")]);
    m_source_name_isSet = !json[QString("sourceName")].isNull() && m_source_name_isValid;

    m_source_type_isValid = ::OpenAPI::fromJsonValue(m_source_type, json[QString("sourceType")]);
    m_source_type_isSet = !json[QString("sourceType")].isNull() && m_source_type_isValid;
}

QString OAISource::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISource::asJsonObject() const {
    QJsonObject obj;
    if (m_source_id_isSet) {
        obj.insert(QString("sourceId"), ::OpenAPI::toJsonValue(m_source_id));
    }
    if (m_source_name_isSet) {
        obj.insert(QString("sourceName"), ::OpenAPI::toJsonValue(m_source_name));
    }
    if (m_source_type_isSet) {
        obj.insert(QString("sourceType"), ::OpenAPI::toJsonValue(m_source_type));
    }
    return obj;
}

qint64 OAISource::getSourceId() const {
    return m_source_id;
}
void OAISource::setSourceId(const qint64 &source_id) {
    m_source_id = source_id;
    m_source_id_isSet = true;
}

bool OAISource::is_source_id_Set() const{
    return m_source_id_isSet;
}

bool OAISource::is_source_id_Valid() const{
    return m_source_id_isValid;
}

QString OAISource::getSourceName() const {
    return m_source_name;
}
void OAISource::setSourceName(const QString &source_name) {
    m_source_name = source_name;
    m_source_name_isSet = true;
}

bool OAISource::is_source_name_Set() const{
    return m_source_name_isSet;
}

bool OAISource::is_source_name_Valid() const{
    return m_source_name_isValid;
}

QString OAISource::getSourceType() const {
    return m_source_type;
}
void OAISource::setSourceType(const QString &source_type) {
    m_source_type = source_type;
    m_source_type_isSet = true;
}

bool OAISource::is_source_type_Set() const{
    return m_source_type_isSet;
}

bool OAISource::is_source_type_Valid() const{
    return m_source_type_isValid;
}

bool OAISource::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_source_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISource::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
