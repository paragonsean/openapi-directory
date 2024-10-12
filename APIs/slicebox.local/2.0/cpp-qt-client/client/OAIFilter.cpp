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

#include "OAIFilter.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFilter::OAIFilter(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFilter::OAIFilter() {
    this->initializeModel();
}

OAIFilter::~OAIFilter() {}

void OAIFilter::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_tag_filter_type_isSet = false;
    m_tag_filter_type_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;
}

void OAIFilter::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFilter::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_tag_filter_type_isValid = ::OpenAPI::fromJsonValue(m_tag_filter_type, json[QString("tagFilterType")]);
    m_tag_filter_type_isSet = !json[QString("tagFilterType")].isNull() && m_tag_filter_type_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;
}

QString OAIFilter::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFilter::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_tag_filter_type_isSet) {
        obj.insert(QString("tagFilterType"), ::OpenAPI::toJsonValue(m_tag_filter_type));
    }
    if (m_tags.size() > 0) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    return obj;
}

qint64 OAIFilter::getId() const {
    return m_id;
}
void OAIFilter::setId(const qint64 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIFilter::is_id_Set() const{
    return m_id_isSet;
}

bool OAIFilter::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIFilter::getName() const {
    return m_name;
}
void OAIFilter::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIFilter::is_name_Set() const{
    return m_name_isSet;
}

bool OAIFilter::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIFilter::getTagFilterType() const {
    return m_tag_filter_type;
}
void OAIFilter::setTagFilterType(const QString &tag_filter_type) {
    m_tag_filter_type = tag_filter_type;
    m_tag_filter_type_isSet = true;
}

bool OAIFilter::is_tag_filter_type_Set() const{
    return m_tag_filter_type_isSet;
}

bool OAIFilter::is_tag_filter_type_Valid() const{
    return m_tag_filter_type_isValid;
}

QList<OAITagPathTag> OAIFilter::getTags() const {
    return m_tags;
}
void OAIFilter::setTags(const QList<OAITagPathTag> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAIFilter::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAIFilter::is_tags_Valid() const{
    return m_tags_isValid;
}

bool OAIFilter::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tag_filter_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFilter::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
