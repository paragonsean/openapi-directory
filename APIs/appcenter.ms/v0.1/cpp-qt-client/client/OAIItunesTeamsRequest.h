/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIItunesTeamsRequest.h
 *
 * Apple credentials with username, password or service_connection_id of the stored credentials is needed.
 */

#ifndef OAIItunesTeamsRequest_H
#define OAIItunesTeamsRequest_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIItunesTeamsRequest : public OAIObject {
public:
    OAIItunesTeamsRequest();
    OAIItunesTeamsRequest(QString json);
    ~OAIItunesTeamsRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCookie() const;
    void setCookie(const QString &cookie);
    bool is_cookie_Set() const;
    bool is_cookie_Valid() const;

    QString getPassword() const;
    void setPassword(const QString &password);
    bool is_password_Set() const;
    bool is_password_Valid() const;

    QString getServiceConnectionId() const;
    void setServiceConnectionId(const QString &service_connection_id);
    bool is_service_connection_id_Set() const;
    bool is_service_connection_id_Valid() const;

    QString getUsername() const;
    void setUsername(const QString &username);
    bool is_username_Set() const;
    bool is_username_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_cookie;
    bool m_cookie_isSet;
    bool m_cookie_isValid;

    QString m_password;
    bool m_password_isSet;
    bool m_password_isValid;

    QString m_service_connection_id;
    bool m_service_connection_id_isSet;
    bool m_service_connection_id_isValid;

    QString m_username;
    bool m_username_isSet;
    bool m_username_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIItunesTeamsRequest)

#endif // OAIItunesTeamsRequest_H
