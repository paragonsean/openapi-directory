/**
 * Flinkster_API_NG
 * This REST-API enables you to query for private transport sharing offers provided by companies and cities in Germany, Netherland and Austria.  You can search for informations about the rental stations (points or areas) where you can find the rentals by utilizing the /areas/ ressource.  With the help of the proximity search in the /bookingproposals/ URI you can request the availabilities of the rentalobjects for spontaneous or planed usage in the future.   Feel free to browse through data by setting the parameter 'providernetwork' to the value:   1: Search for car sharing offers provided by the Flinkster platform (http://www.flinkster.de) 2: Finding bike rental offers from Call a Bike (http://www.callabike.de)   You can find more details in the documentation section (Unfortunately only available in german language).  Have lots of fun and we are lucky to take notice of your products or getting your feedback.
 *
 * The version of the OpenAPI document: v1
 * Contact: partner@flinkster.de
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIProviderJO.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProviderJO::OAIProviderJO(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProviderJO::OAIProviderJO() {
    this->initializeModel();
}

OAIProviderJO::~OAIProviderJO() {}

void OAIProviderJO::initializeModel() {

    m__links_isSet = false;
    m__links_isValid = false;

    m_attributes_isSet = false;
    m_attributes_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_expand_isSet = false;
    m_expand_isValid = false;

    m_href_isSet = false;
    m_href_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_uid_isSet = false;
    m_uid_isValid = false;
}

void OAIProviderJO::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProviderJO::fromJsonObject(QJsonObject json) {

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_attributes_isValid = ::OpenAPI::fromJsonValue(m_attributes, json[QString("attributes")]);
    m_attributes_isSet = !json[QString("attributes")].isNull() && m_attributes_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_expand_isValid = ::OpenAPI::fromJsonValue(m_expand, json[QString("expand")]);
    m_expand_isSet = !json[QString("expand")].isNull() && m_expand_isValid;

    m_href_isValid = ::OpenAPI::fromJsonValue(m_href, json[QString("href")]);
    m_href_isSet = !json[QString("href")].isNull() && m_href_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_uid_isValid = ::OpenAPI::fromJsonValue(m_uid, json[QString("uid")]);
    m_uid_isSet = !json[QString("uid")].isNull() && m_uid_isValid;
}

QString OAIProviderJO::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProviderJO::asJsonObject() const {
    QJsonObject obj;
    if (m__links.size() > 0) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
    if (m_attributes.size() > 0) {
        obj.insert(QString("attributes"), ::OpenAPI::toJsonValue(m_attributes));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_expand_isSet) {
        obj.insert(QString("expand"), ::OpenAPI::toJsonValue(m_expand));
    }
    if (m_href_isSet) {
        obj.insert(QString("href"), ::OpenAPI::toJsonValue(m_href));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_uid_isSet) {
        obj.insert(QString("uid"), ::OpenAPI::toJsonValue(m_uid));
    }
    return obj;
}

QList<OAILinkJO> OAIProviderJO::getLinks() const {
    return m__links;
}
void OAIProviderJO::setLinks(const QList<OAILinkJO> &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAIProviderJO::is__links_Set() const{
    return m__links_isSet;
}

bool OAIProviderJO::is__links_Valid() const{
    return m__links_isValid;
}

QMap<QString, OAIObject> OAIProviderJO::getAttributes() const {
    return m_attributes;
}
void OAIProviderJO::setAttributes(const QMap<QString, OAIObject> &attributes) {
    m_attributes = attributes;
    m_attributes_isSet = true;
}

bool OAIProviderJO::is_attributes_Set() const{
    return m_attributes_isSet;
}

bool OAIProviderJO::is_attributes_Valid() const{
    return m_attributes_isValid;
}

QString OAIProviderJO::getDescription() const {
    return m_description;
}
void OAIProviderJO::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIProviderJO::is_description_Set() const{
    return m_description_isSet;
}

bool OAIProviderJO::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIProviderJO::getExpand() const {
    return m_expand;
}
void OAIProviderJO::setExpand(const QString &expand) {
    m_expand = expand;
    m_expand_isSet = true;
}

bool OAIProviderJO::is_expand_Set() const{
    return m_expand_isSet;
}

bool OAIProviderJO::is_expand_Valid() const{
    return m_expand_isValid;
}

QString OAIProviderJO::getHref() const {
    return m_href;
}
void OAIProviderJO::setHref(const QString &href) {
    m_href = href;
    m_href_isSet = true;
}

bool OAIProviderJO::is_href_Set() const{
    return m_href_isSet;
}

bool OAIProviderJO::is_href_Valid() const{
    return m_href_isValid;
}

QString OAIProviderJO::getName() const {
    return m_name;
}
void OAIProviderJO::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIProviderJO::is_name_Set() const{
    return m_name_isSet;
}

bool OAIProviderJO::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIProviderJO::getUid() const {
    return m_uid;
}
void OAIProviderJO::setUid(const QString &uid) {
    m_uid = uid;
    m_uid_isSet = true;
}

bool OAIProviderJO::is_uid_Set() const{
    return m_uid_isSet;
}

bool OAIProviderJO::is_uid_Valid() const{
    return m_uid_isValid;
}

bool OAIProviderJO::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m__links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_attributes.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_expand_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_href_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_uid_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIProviderJO::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
