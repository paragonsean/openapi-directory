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

#include "OAICollectionPrivateLinkCreator.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICollectionPrivateLinkCreator::OAICollectionPrivateLinkCreator(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICollectionPrivateLinkCreator::OAICollectionPrivateLinkCreator() {
    this->initializeModel();
}

OAICollectionPrivateLinkCreator::~OAICollectionPrivateLinkCreator() {}

void OAICollectionPrivateLinkCreator::initializeModel() {

    m_expires_date_isSet = false;
    m_expires_date_isValid = false;

    m_read_only_isSet = false;
    m_read_only_isValid = false;
}

void OAICollectionPrivateLinkCreator::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICollectionPrivateLinkCreator::fromJsonObject(QJsonObject json) {

    m_expires_date_isValid = ::OpenAPI::fromJsonValue(m_expires_date, json[QString("expires_date")]);
    m_expires_date_isSet = !json[QString("expires_date")].isNull() && m_expires_date_isValid;

    m_read_only_isValid = ::OpenAPI::fromJsonValue(m_read_only, json[QString("read_only")]);
    m_read_only_isSet = !json[QString("read_only")].isNull() && m_read_only_isValid;
}

QString OAICollectionPrivateLinkCreator::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICollectionPrivateLinkCreator::asJsonObject() const {
    QJsonObject obj;
    if (m_expires_date_isSet) {
        obj.insert(QString("expires_date"), ::OpenAPI::toJsonValue(m_expires_date));
    }
    if (m_read_only_isSet) {
        obj.insert(QString("read_only"), ::OpenAPI::toJsonValue(m_read_only));
    }
    return obj;
}

QString OAICollectionPrivateLinkCreator::getExpiresDate() const {
    return m_expires_date;
}
void OAICollectionPrivateLinkCreator::setExpiresDate(const QString &expires_date) {
    m_expires_date = expires_date;
    m_expires_date_isSet = true;
}

bool OAICollectionPrivateLinkCreator::is_expires_date_Set() const{
    return m_expires_date_isSet;
}

bool OAICollectionPrivateLinkCreator::is_expires_date_Valid() const{
    return m_expires_date_isValid;
}

bool OAICollectionPrivateLinkCreator::isReadOnly() const {
    return m_read_only;
}
void OAICollectionPrivateLinkCreator::setReadOnly(const bool &read_only) {
    m_read_only = read_only;
    m_read_only_isSet = true;
}

bool OAICollectionPrivateLinkCreator::is_read_only_Set() const{
    return m_read_only_isSet;
}

bool OAICollectionPrivateLinkCreator::is_read_only_Valid() const{
    return m_read_only_isValid;
}

bool OAICollectionPrivateLinkCreator::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_expires_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_read_only_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICollectionPrivateLinkCreator::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
