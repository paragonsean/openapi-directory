/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRoomGuestUserAddRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRoomGuestUserAddRequest::OAIRoomGuestUserAddRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRoomGuestUserAddRequest::OAIRoomGuestUserAddRequest() {
    this->initializeModel();
}

OAIRoomGuestUserAddRequest::~OAIRoomGuestUserAddRequest() {}

void OAIRoomGuestUserAddRequest::initializeModel() {

    m_room_guest_invitations_isSet = false;
    m_room_guest_invitations_isValid = false;
}

void OAIRoomGuestUserAddRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRoomGuestUserAddRequest::fromJsonObject(QJsonObject json) {

    m_room_guest_invitations_isValid = ::OpenAPI::fromJsonValue(m_room_guest_invitations, json[QString("roomGuestInvitations")]);
    m_room_guest_invitations_isSet = !json[QString("roomGuestInvitations")].isNull() && m_room_guest_invitations_isValid;
}

QString OAIRoomGuestUserAddRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRoomGuestUserAddRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_room_guest_invitations.size() > 0) {
        obj.insert(QString("roomGuestInvitations"), ::OpenAPI::toJsonValue(m_room_guest_invitations));
    }
    return obj;
}

QList<OAIRoomGuestUserInvitation> OAIRoomGuestUserAddRequest::getRoomGuestInvitations() const {
    return m_room_guest_invitations;
}
void OAIRoomGuestUserAddRequest::setRoomGuestInvitations(const QList<OAIRoomGuestUserInvitation> &room_guest_invitations) {
    m_room_guest_invitations = room_guest_invitations;
    m_room_guest_invitations_isSet = true;
}

bool OAIRoomGuestUserAddRequest::is_room_guest_invitations_Set() const{
    return m_room_guest_invitations_isSet;
}

bool OAIRoomGuestUserAddRequest::is_room_guest_invitations_Valid() const{
    return m_room_guest_invitations_isValid;
}

bool OAIRoomGuestUserAddRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_room_guest_invitations.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRoomGuestUserAddRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_room_guest_invitations_isValid && true;
}

} // namespace OpenAPI
