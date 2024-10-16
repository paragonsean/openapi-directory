/**
 * Flickr API Schema
 * A subset of Flickr's API defined in Swagger format.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPhoto_tags.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPhoto_tags::OAIPhoto_tags(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPhoto_tags::OAIPhoto_tags() {
    this->initializeModel();
}

OAIPhoto_tags::~OAIPhoto_tags() {}

void OAIPhoto_tags::initializeModel() {

    m_tag_isSet = false;
    m_tag_isValid = false;
}

void OAIPhoto_tags::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPhoto_tags::fromJsonObject(QJsonObject json) {

    m_tag_isValid = ::OpenAPI::fromJsonValue(m_tag, json[QString("tag")]);
    m_tag_isSet = !json[QString("tag")].isNull() && m_tag_isValid;
}

QString OAIPhoto_tags::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPhoto_tags::asJsonObject() const {
    QJsonObject obj;
    if (m_tag.size() > 0) {
        obj.insert(QString("tag"), ::OpenAPI::toJsonValue(m_tag));
    }
    return obj;
}

QList<OAITag> OAIPhoto_tags::getTag() const {
    return m_tag;
}
void OAIPhoto_tags::setTag(const QList<OAITag> &tag) {
    m_tag = tag;
    m_tag_isSet = true;
}

bool OAIPhoto_tags::is_tag_Set() const{
    return m_tag_isSet;
}

bool OAIPhoto_tags::is_tag_Valid() const{
    return m_tag_isValid;
}

bool OAIPhoto_tags::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_tag.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPhoto_tags::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
