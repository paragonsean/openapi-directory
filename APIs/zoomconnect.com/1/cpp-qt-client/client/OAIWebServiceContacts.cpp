/**
 * www.zoomconnect.com
 * The world's greatest SMS API
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIWebServiceContacts.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIWebServiceContacts::OAIWebServiceContacts(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIWebServiceContacts::OAIWebServiceContacts() {
    this->initializeModel();
}

OAIWebServiceContacts::~OAIWebServiceContacts() {}

void OAIWebServiceContacts::initializeModel() {

    m_links_isSet = false;
    m_links_isValid = false;

    m_web_service_contacts_isSet = false;
    m_web_service_contacts_isValid = false;
}

void OAIWebServiceContacts::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIWebServiceContacts::fromJsonObject(QJsonObject json) {

    m_links_isValid = ::OpenAPI::fromJsonValue(m_links, json[QString("links")]);
    m_links_isSet = !json[QString("links")].isNull() && m_links_isValid;

    m_web_service_contacts_isValid = ::OpenAPI::fromJsonValue(m_web_service_contacts, json[QString("webServiceContacts")]);
    m_web_service_contacts_isSet = !json[QString("webServiceContacts")].isNull() && m_web_service_contacts_isValid;
}

QString OAIWebServiceContacts::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIWebServiceContacts::asJsonObject() const {
    QJsonObject obj;
    if (m_links.size() > 0) {
        obj.insert(QString("links"), ::OpenAPI::toJsonValue(m_links));
    }
    if (m_web_service_contacts.size() > 0) {
        obj.insert(QString("webServiceContacts"), ::OpenAPI::toJsonValue(m_web_service_contacts));
    }
    return obj;
}

QList<OAILink> OAIWebServiceContacts::getLinks() const {
    return m_links;
}
void OAIWebServiceContacts::setLinks(const QList<OAILink> &links) {
    m_links = links;
    m_links_isSet = true;
}

bool OAIWebServiceContacts::is_links_Set() const{
    return m_links_isSet;
}

bool OAIWebServiceContacts::is_links_Valid() const{
    return m_links_isValid;
}

QList<OAIWebServiceContact> OAIWebServiceContacts::getWebServiceContacts() const {
    return m_web_service_contacts;
}
void OAIWebServiceContacts::setWebServiceContacts(const QList<OAIWebServiceContact> &web_service_contacts) {
    m_web_service_contacts = web_service_contacts;
    m_web_service_contacts_isSet = true;
}

bool OAIWebServiceContacts::is_web_service_contacts_Set() const{
    return m_web_service_contacts_isSet;
}

bool OAIWebServiceContacts::is_web_service_contacts_Valid() const{
    return m_web_service_contacts_isValid;
}

bool OAIWebServiceContacts::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_web_service_contacts.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIWebServiceContacts::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
