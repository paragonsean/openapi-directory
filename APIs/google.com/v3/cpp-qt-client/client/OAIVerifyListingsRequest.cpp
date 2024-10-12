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

#include "OAIVerifyListingsRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVerifyListingsRequest::OAIVerifyListingsRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVerifyListingsRequest::OAIVerifyListingsRequest() {
    this->initializeModel();
}

OAIVerifyListingsRequest::~OAIVerifyListingsRequest() {}

void OAIVerifyListingsRequest::initializeModel() {

    m_xml_listing_isSet = false;
    m_xml_listing_isValid = false;
}

void OAIVerifyListingsRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVerifyListingsRequest::fromJsonObject(QJsonObject json) {

    m_xml_listing_isValid = ::OpenAPI::fromJsonValue(m_xml_listing, json[QString("xmlListing")]);
    m_xml_listing_isSet = !json[QString("xmlListing")].isNull() && m_xml_listing_isValid;
}

QString OAIVerifyListingsRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVerifyListingsRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_xml_listing_isSet) {
        obj.insert(QString("xmlListing"), ::OpenAPI::toJsonValue(m_xml_listing));
    }
    return obj;
}

QString OAIVerifyListingsRequest::getXmlListing() const {
    return m_xml_listing;
}
void OAIVerifyListingsRequest::setXmlListing(const QString &xml_listing) {
    m_xml_listing = xml_listing;
    m_xml_listing_isSet = true;
}

bool OAIVerifyListingsRequest::is_xml_listing_Set() const{
    return m_xml_listing_isSet;
}

bool OAIVerifyListingsRequest::is_xml_listing_Valid() const{
    return m_xml_listing_isValid;
}

bool OAIVerifyListingsRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_xml_listing_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVerifyListingsRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
