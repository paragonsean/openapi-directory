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

#include "OAIPlayed_in_links_played_in.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPlayed_in_links_played_in::OAIPlayed_in_links_played_in(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPlayed_in_links_played_in::OAIPlayed_in_links_played_in() {
    this->initializeModel();
}

OAIPlayed_in_links_played_in::~OAIPlayed_in_links_played_in() {}

void OAIPlayed_in_links_played_in::initializeModel() {

    m_href_isSet = false;
    m_href_isValid = false;

    m_played_in_isSet = false;
    m_played_in_isValid = false;

    m_result_type_isSet = false;
    m_result_type_isValid = false;
}

void OAIPlayed_in_links_played_in::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPlayed_in_links_played_in::fromJsonObject(QJsonObject json) {

    m_href_isValid = ::OpenAPI::fromJsonValue(m_href, json[QString("href")]);
    m_href_isSet = !json[QString("href")].isNull() && m_href_isValid;

    m_played_in_isValid = ::OpenAPI::fromJsonValue(m_played_in, json[QString("played_in")]);
    m_played_in_isSet = !json[QString("played_in")].isNull() && m_played_in_isValid;

    m_result_type_isValid = ::OpenAPI::fromJsonValue(m_result_type, json[QString("result_type")]);
    m_result_type_isSet = !json[QString("result_type")].isNull() && m_result_type_isValid;
}

QString OAIPlayed_in_links_played_in::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPlayed_in_links_played_in::asJsonObject() const {
    QJsonObject obj;
    if (m_href_isSet) {
        obj.insert(QString("href"), ::OpenAPI::toJsonValue(m_href));
    }
    if (m_played_in.isSet()) {
        obj.insert(QString("played_in"), ::OpenAPI::toJsonValue(m_played_in));
    }
    if (m_result_type_isSet) {
        obj.insert(QString("result_type"), ::OpenAPI::toJsonValue(m_result_type));
    }
    return obj;
}

QString OAIPlayed_in_links_played_in::getHref() const {
    return m_href;
}
void OAIPlayed_in_links_played_in::setHref(const QString &href) {
    m_href = href;
    m_href_isSet = true;
}

bool OAIPlayed_in_links_played_in::is_href_Set() const{
    return m_href_isSet;
}

bool OAIPlayed_in_links_played_in::is_href_Valid() const{
    return m_href_isValid;
}

OAIImages_mixin_images_image_images_image_inherited_from OAIPlayed_in_links_played_in::getPlayedIn() const {
    return m_played_in;
}
void OAIPlayed_in_links_played_in::setPlayedIn(const OAIImages_mixin_images_image_images_image_inherited_from &played_in) {
    m_played_in = played_in;
    m_played_in_isSet = true;
}

bool OAIPlayed_in_links_played_in::is_played_in_Set() const{
    return m_played_in_isSet;
}

bool OAIPlayed_in_links_played_in::is_played_in_Valid() const{
    return m_played_in_isValid;
}

QString OAIPlayed_in_links_played_in::getResultType() const {
    return m_result_type;
}
void OAIPlayed_in_links_played_in::setResultType(const QString &result_type) {
    m_result_type = result_type;
    m_result_type_isSet = true;
}

bool OAIPlayed_in_links_played_in::is_result_type_Set() const{
    return m_result_type_isSet;
}

bool OAIPlayed_in_links_played_in::is_result_type_Valid() const{
    return m_result_type_isValid;
}

bool OAIPlayed_in_links_played_in::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_href_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_played_in.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_result_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPlayed_in_links_played_in::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
