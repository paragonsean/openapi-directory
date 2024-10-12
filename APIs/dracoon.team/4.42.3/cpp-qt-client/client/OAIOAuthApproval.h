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

/*
 * OAIOAuthApproval.h
 *
 * OAuth client approval information
 */

#ifndef OAIOAuthApproval_H
#define OAIOAuthApproval_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIOAuthApproval : public OAIObject {
public:
    OAIOAuthApproval();
    OAIOAuthApproval(QString json);
    ~OAIOAuthApproval() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getClientId() const;
    void setClientId(const QString &client_id);
    bool is_client_id_Set() const;
    bool is_client_id_Valid() const;

    QString getClientName() const;
    void setClientName(const QString &client_name);
    bool is_client_name_Set() const;
    bool is_client_name_Valid() const;

    QDateTime getExpiresAt() const;
    void setExpiresAt(const QDateTime &expires_at);
    bool is_expires_at_Set() const;
    bool is_expires_at_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_client_id;
    bool m_client_id_isSet;
    bool m_client_id_isValid;

    QString m_client_name;
    bool m_client_name_isSet;
    bool m_client_name_isValid;

    QDateTime m_expires_at;
    bool m_expires_at_isSet;
    bool m_expires_at_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOAuthApproval)

#endif // OAIOAuthApproval_H
