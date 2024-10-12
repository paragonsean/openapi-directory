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

#include "OAIRelated_links.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRelated_links::OAIRelated_links(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRelated_links::OAIRelated_links() {
    this->initializeModel();
}

OAIRelated_links::~OAIRelated_links() {}

void OAIRelated_links::initializeModel() {

    m_related_link_isSet = false;
    m_related_link_isValid = false;
}

void OAIRelated_links::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRelated_links::fromJsonObject(QJsonObject json) {

    m_related_link_isValid = ::OpenAPI::fromJsonValue(m_related_link, json[QString("related_link")]);
    m_related_link_isSet = !json[QString("related_link")].isNull() && m_related_link_isValid;
}

QString OAIRelated_links::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRelated_links::asJsonObject() const {
    QJsonObject obj;
    if (m_related_link.size() > 0) {
        obj.insert(QString("related_link"), ::OpenAPI::toJsonValue(m_related_link));
    }
    return obj;
}

QList<OAIRelated_link> OAIRelated_links::getRelatedLink() const {
    return m_related_link;
}
void OAIRelated_links::setRelatedLink(const QList<OAIRelated_link> &related_link) {
    m_related_link = related_link;
    m_related_link_isSet = true;
}

bool OAIRelated_links::is_related_link_Set() const{
    return m_related_link_isSet;
}

bool OAIRelated_links::is_related_link_Valid() const{
    return m_related_link_isValid;
}

bool OAIRelated_links::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_related_link.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRelated_links::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
