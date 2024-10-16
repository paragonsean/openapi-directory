/**
 * Travel Partner API
 * The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts.
 *
 * The version of the OpenAPI document: v3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIIcon.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIcon::OAIIcon(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIcon::OAIIcon() {
    this->initializeModel();
}

OAIIcon::~OAIIcon() {}

void OAIIcon::initializeModel() {

    m_disapproval_reasons_isSet = false;
    m_disapproval_reasons_isValid = false;

    m_icon_uri_isSet = false;
    m_icon_uri_isValid = false;

    m_image_data_isSet = false;
    m_image_data_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_reference_isSet = false;
    m_reference_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;
}

void OAIIcon::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIcon::fromJsonObject(QJsonObject json) {

    m_disapproval_reasons_isValid = ::OpenAPI::fromJsonValue(m_disapproval_reasons, json[QString("disapprovalReasons")]);
    m_disapproval_reasons_isSet = !json[QString("disapprovalReasons")].isNull() && m_disapproval_reasons_isValid;

    m_icon_uri_isValid = ::OpenAPI::fromJsonValue(m_icon_uri, json[QString("iconUri")]);
    m_icon_uri_isSet = !json[QString("iconUri")].isNull() && m_icon_uri_isValid;

    m_image_data_isValid = ::OpenAPI::fromJsonValue(m_image_data, json[QString("imageData")]);
    m_image_data_isSet = !json[QString("imageData")].isNull() && m_image_data_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_reference_isValid = ::OpenAPI::fromJsonValue(m_reference, json[QString("reference")]);
    m_reference_isSet = !json[QString("reference")].isNull() && m_reference_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;
}

QString OAIIcon::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIcon::asJsonObject() const {
    QJsonObject obj;
    if (m_disapproval_reasons.size() > 0) {
        obj.insert(QString("disapprovalReasons"), ::OpenAPI::toJsonValue(m_disapproval_reasons));
    }
    if (m_icon_uri_isSet) {
        obj.insert(QString("iconUri"), ::OpenAPI::toJsonValue(m_icon_uri));
    }
    if (m_image_data_isSet) {
        obj.insert(QString("imageData"), ::OpenAPI::toJsonValue(m_image_data));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_reference_isSet) {
        obj.insert(QString("reference"), ::OpenAPI::toJsonValue(m_reference));
    }
    if (m_state_isSet) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    return obj;
}

QList<QString> OAIIcon::getDisapprovalReasons() const {
    return m_disapproval_reasons;
}
void OAIIcon::setDisapprovalReasons(const QList<QString> &disapproval_reasons) {
    m_disapproval_reasons = disapproval_reasons;
    m_disapproval_reasons_isSet = true;
}

bool OAIIcon::is_disapproval_reasons_Set() const{
    return m_disapproval_reasons_isSet;
}

bool OAIIcon::is_disapproval_reasons_Valid() const{
    return m_disapproval_reasons_isValid;
}

QString OAIIcon::getIconUri() const {
    return m_icon_uri;
}
void OAIIcon::setIconUri(const QString &icon_uri) {
    m_icon_uri = icon_uri;
    m_icon_uri_isSet = true;
}

bool OAIIcon::is_icon_uri_Set() const{
    return m_icon_uri_isSet;
}

bool OAIIcon::is_icon_uri_Valid() const{
    return m_icon_uri_isValid;
}

QByteArray OAIIcon::getImageData() const {
    return m_image_data;
}
void OAIIcon::setImageData(const QByteArray &image_data) {
    m_image_data = image_data;
    m_image_data_isSet = true;
}

bool OAIIcon::is_image_data_Set() const{
    return m_image_data_isSet;
}

bool OAIIcon::is_image_data_Valid() const{
    return m_image_data_isValid;
}

QString OAIIcon::getName() const {
    return m_name;
}
void OAIIcon::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIIcon::is_name_Set() const{
    return m_name_isSet;
}

bool OAIIcon::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIIcon::getReference() const {
    return m_reference;
}
void OAIIcon::setReference(const QString &reference) {
    m_reference = reference;
    m_reference_isSet = true;
}

bool OAIIcon::is_reference_Set() const{
    return m_reference_isSet;
}

bool OAIIcon::is_reference_Valid() const{
    return m_reference_isValid;
}

QString OAIIcon::getState() const {
    return m_state;
}
void OAIIcon::setState(const QString &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIIcon::is_state_Set() const{
    return m_state_isSet;
}

bool OAIIcon::is_state_Valid() const{
    return m_state_isValid;
}

bool OAIIcon::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_disapproval_reasons.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_icon_uri_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reference_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIcon::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
